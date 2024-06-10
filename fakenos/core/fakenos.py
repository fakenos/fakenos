"""
Main module to interact with FakeNOS servers.
It is the entry point to start, stop and list FakeNOS servers.
"""

import logging
import copy
import socket
import threading
import time
import platform
from typing import Union, List, Dict, Set

import yaml
import detect

from fakenos.core.host import Host
from fakenos.core.pydantic_models import ModelFakenosInventory


log = logging.getLogger(__name__)

default_inventory = {
    "default": {
        "username": "user",
        "password": "user",
        "port": 6000,
        "servers": [
            {
                "name": "SSH",
                "plugin": "ParamikoSshServer",
                "configuration": {
                    "shell": {
                        "plugin": "CMDShell", 
                        "configuration": {}
                    },
                },
            },
            {
                "name": "SNMP",
                "plugin": "SNMPServer",
                "configuration": {
                    "port": 7000
                }
            },
            {
                "name": "NETCONF",
                "plugin": "NETCONFServer",
                "configuration": {
                    "port": 9000
                }
            }
        ],
        "servers_configuration": {
            "address": "127.0.0.1",
        },
        "nos": {"plugin": "cisco_ios", "configuration": {}},
    },
    "hosts": {
        "router_cisco_ios": {"port": 6000, "platform": "cisco_ios"},
        "router_huawei_smartax": {"port": 6001, "platform": "huawei_smartax"},
        "router_arista_eos": {"port": 6002, "platform": "arista_eos"},
    },
}

# If Windows or WSL, the configuration address is 0.0.0.0
# WSL Bug: https://github.com/microsoft/WSL/issues/4983
if detect.docker and "WSL2" in platform.release():
    for server_config in default_inventory["default"]["servers"]:
        if "configuration" in server_config:
            server_config["configuration"]["address"] = "0.0.0.0"


class FakeNOS:
    """
    FakeNOS class is a main entry point to interact
    with fake NOS servers - start, stop, list.

    :param inventory: FakeNOS inventory dictionary or
                      OS path to .yaml file with inventory data
    :param plugins: Plugins to add extra devices/commands
                    currently not supported easily.

    Sample usage:

    ```python
    from fakenos import FakeNOS

    net = FakeNOS()
    net.start()
    ```
    """

    def __init__(
        self,
        inventory: dict = None,
        plugins: list = None,
    ) -> None:
        self.inventory: dict = inventory or default_inventory
        self.plugins: list = plugins or []
        self.nos_plugins: list = []

        self.hosts: Dict[str, Host] = {}
        self.allocated_ports: Set[str] = set()

        self._load_inventory()
        self._init()
        # self._register_nos_plugins()

    def __enter__(self):
        """
        Method to start the FakeNOS servers when entering the context manager.
        It is meant to be used with the `with` statement.
        """
        self.start()
        return self

    def __exit__(self, *args):
        """
        Method to stop the FakeNOS servers when exiting the context manager.
        It is meant to be used with the `with` statement.
        """
        self.stop()

    def _is_inventory_in_yaml(self) -> bool:
        """method that checks if the inventory is a yaml file."""
        return isinstance(self.inventory, str) and self.inventory.endswith(".yaml")

    def _load_inventory_yaml(self) -> None:
        """Helper method to load FakeNOS inventory if it is yaml."""
        with open(self.inventory, "r", encoding="utf-8") as f:
            self.inventory = yaml.safe_load(f.read())

    def _load_inventory(self) -> None:
        """Helper method to load FakeNOS inventory"""
        if self._is_inventory_in_yaml():
            self._load_inventory_yaml()

        self.inventory["default"] = {
            **default_inventory["default"],
            **self.inventory.get("default", {}),
        }

        ModelFakenosInventory(**self.inventory)
        log.debug("FakeNOS inventory validation succeeded")

    def _init(self) -> None:
        """
        Helper method to initiate host objects
        and store them in self.hosts, this
        method called automatically on FakeNOS object instantiation.
        """
        for host_name, host_config in self.inventory["hosts"].items():
            params = {
                **copy.deepcopy(self.inventory["default"]),
                **copy.deepcopy(host_config),
            }
            params = self._add_config_to_cli(params)
            params = self._add_config_general_params(params)
            replicas: int = params.pop("replicas", None)
            self._check_ports_and_replicas_are_okey(params["servers"], replicas)
            self._instantiate_host_object(host_name, replicas, params)

    def _add_config_to_cli(self, params: dict):
        """
        Method that changes the port, username and password
        to the corresponding CLI server.

        This is a helper method as before you could create
        a NOS like so:
        hosts:
          R1:
            username: user                  -> cli_username
            password: user                  -> cli_password
            port: 6000                      -> cli_port
            configuration_file: filename    -> configuration_file
        """
        new_params = copy.deepcopy(params)
        for server in new_params["servers"]:
            if "configuration" in server and "shell" in server["configuration"]:
                server["configuration"] = {
                    "port": new_params.pop("port"),
                    "username": new_params.pop("username"),
                    "password": new_params.pop("password"),
                    "configuration_file": new_params.pop("configuration_file", None),
                    **server["configuration"]
                }
        return new_params


    def _add_config_general_params(self, params: dict):
        """ Method to add the general params to each server. """
        new_params = copy.deepcopy(params)
        general_server_configurations: dict = new_params.pop("servers_configuration")
        for server in new_params["servers"]:
            server["configuration"].update(general_server_configurations)
        return new_params


    def _check_ports_and_replicas_are_okey(self, servers: dict, replicas):
        """
        Method to check if the port and replicas are okey

        :param port: integer or list of two integers - port to allocate
        :param replicas: integer - number of hosts to create
        """
        for server in servers:
            port = server["configuration"]["port"]
            if not replicas and isinstance(port, list):
                raise ValueError("If replicas is not set, port must be an integer.")
            if replicas and not isinstance(port, list):
                raise ValueError("If replicas is set, port must be a list of two integers.")
            if replicas and len(port) != 2:
                raise ValueError("If replicas is set, port must be a list of two integers.")
            if replicas and port[0] >= port[1]:
                raise ValueError("If replicas is set, port[0] must be less than port[1].")
            if replicas and replicas < 1:
                raise ValueError("If replicas is set, replicas must be greater than 0.")
            if replicas and port[1] - port[0] + 1 != replicas:
                raise ValueError(
                    "If replicas is set, port range \
                        must be equal to the number of replicas."
                )

    def _instantiate_host_object(self, host_name: str, replicas: int, params: dict):
        """
        Method that instantiate the host objects. It initializes the hosts
        with the corresponding name, port and network operating system

        :param host: string - name of the host
        :param count: integer - number of hosts to create
        :param params: dictionary - parameters to pass to
                                    the host like configurations
        """
        hosts_name= self._get_hosts(host_name, replicas)
        for h_name in hosts_name:
            self._instantiate_single_host_object(h_name, params)

    def _get_hosts(self, host_name: str, replicas: int = None):
        """
        Method to get hosts and ports correctly
        depending on the number of replicas (if exists).

        :param host_name: string - name of the host
        :param port: integer or list of two integers - port to allocate
        :param replicas: integer - number of hosts to create
        """
        hosts_name: Set[str] = {}

        if replicas:
            hosts_name = {f"{host_name}{i}" for i in range(replicas)}
        else:
            hosts_name = {host_name}
        return hosts_name

    def _instantiate_single_host_object(self, host, params):
        """
        Method that instantiate the host objects. It initializes the hosts

        :param host: string - name of the host
        :param port: integer or list of two integers - port to allocate
        :param params: dictionary - parameters to pass to
                                    the host like configurations
        """
        for server in params["servers"]:
            self._allocate_port(server["configuration"]["port"])
        self.hosts[host] = Host(name=host, fakenos=self, **params)

    def _allocate_port(self, port: Union[int, List[int]]) -> None:
        """
        Method to allocate port for host

        :param port: integer or list of two integers -
                     range to allocate port from
        """
        if isinstance(port, int):
            port: List[int] = [port]

        for p in port:
            allocated_port = self._allocate_port_single(p)
            self.allocated_ports.add(allocated_port)

    def _allocate_port_single(self, port: int) -> int:
        """
        Method to allocate single port for host.

        :param port: integer - port to allocate
        """
        if port in self.allocated_ports:
            raise ValueError(f"Port {port} already in use")
        self.allocated_ports.add(port)
        return port

    def _get_hosts_as_list(self, hosts: Union[str, List[str]] = None) -> List[Host]:
        """
        Helper method to get hosts as list

        :param hosts: string or list of strings
        :return: list of strings
        """
        hosts_list: List[Host] = []
        if not hosts:
            hosts = list(self.hosts.keys())
        if isinstance(hosts, str):
            hosts = [hosts]
        hosts_list = [self.hosts[host] for host in hosts]
        return hosts_list

    def start(self, hosts: Union[str, list] = None) -> None:  # type: ignore
        """
        Function to start NOS servers instances

        :param hosts: single or list of hosts to start by their name.
        """
        hosts: List[str] = self._get_hosts_as_list(hosts)
        self._execute_function_over_hosts(hosts, "start", host_running=False)
        log.info("The following devices has been initiated: %s", [host.name for host in hosts])
        for host in hosts:
            for server in host.servers:
                log.info("Device %s - %s is running on port %s",
                         host.name, server.service_name, server.port)

    def stop(self, hosts: Union[str, List[str]] = None) -> None:
        """
        Function to stop NOS servers instances. It waits 2 seconds
        just in case that there is any thread doing something.

        :param hosts: single or list of hosts to stop by their name.
        """
        hosts: List[str] = self._get_hosts_as_list(hosts)
        self._execute_function_over_hosts(hosts, "stop", host_running=True)
        if hosts == list(self.hosts.values()):
            self._join_threads()

    def _join_threads(self) -> None:
        """
        Method to join threads in case that all hosts are stopped.
        """
        all_threads = threading.enumerate()
        for thread in all_threads:
            if thread is not threading.main_thread() and "pytest_timeout" not in thread.name:
                thread.join()
        n_threads: int = 2 if detect.windows else 1
        while threading.active_count() > n_threads:
            time.sleep(0.01)

    def _execute_function_over_hosts(self, hosts: List[Host], func: str, host_running: bool = True):
        """
        Function that executes a function like start or stop over
        the selected hosts.

        :param hosts: list of Hosts objects in which the function will
        be executed.
        """
        for host in hosts:
            if host not in self.hosts.values():
                raise ValueError(f"Host {host} not found")
            if host.running == host_running:
                getattr(host, func)()

    # def _register_nos_plugins(self) -> None:
    #     """
    #     Method to register NOS plugin with FakeNOS object, all plugins
    #     must be registered before calling start method.

    #     :param plugin: OS path string to NOS plugin `.yaml/.yml` or `.py` file,
    #       dictionary or instance if Nos class
    #     """
    #     for plugin in self.plugins:
    #         if isinstance(plugin, Nos):
    #             nos_instance = plugin
    #         else:
    #             nos_instance = Nos()
    #             if isinstance(plugin, dict):
    #                 nos_instance.from_dict(plugin)
    #             elif isinstance(plugin, str):
    #                 nos_instance.from_file(plugin)
    #             else:
    #                 raise TypeError(f"Unsupported NOS type {type(plugin)}, supported str, dict or Nos")
    #         self.nos_plugins[nos_instance.name] = nos_instance


def _get_free_port() -> int:
    """
    Method to get a free port for the FakeNOS server.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def fakenos(platform: str = None, inventory: dict = None, return_instance: bool = False):
    """
    Decorator to run a test with FakeNOS server.
    """
    if platform and inventory:
        raise ValueError("platform and inventory cannot be used together")
    if not platform and not inventory:
        raise ValueError("platform or inventory must be set")
    if platform:
        inventory = {
            "hosts": {
                "FakeNOS": {
                    "username": "test",
                    "password": "test",
                    "port": _get_free_port(),
                    "platform": platform,
                }
            }
        }

    def decorator(func):
        def wrapper(*args, **kwargs):
            with FakeNOS(inventory=inventory) as net:
                if return_instance:
                    return func(*args, net=net, **kwargs)
                return func(*args, **kwargs)

        return wrapper

    return decorator
