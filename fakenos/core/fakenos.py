"""
Main module to interact with FakeNOS servers.
It is the entry point to start, stop and list FakeNOS servers.
"""

import logging
import copy
import threading
import time
import platform

import yaml
import detect

from fakenos.core.host import Host
from fakenos.core.nos import Nos
from fakenos.core.pydantic_models import ModelFakenosInventory

from fakenos.plugins.servers import servers_plugins
from fakenos.plugins.nos import nos_plugins
from fakenos.plugins.shell import shell_plugins

log = logging.getLogger(__name__)

default_inventory = {
    "default": {
        "username": "user",
        "password": "user",
        "port": 6000,
        "server": {
            "plugin": "ParamikoSshServer",
            "configuration": {
                "address": "127.0.0.1",
                "timeout": 1,
            },
        },
        "shell": {"plugin": "CMDShell", "configuration": {}},
        "nos": {"plugin": "cisco_ios", "configuration": {}},
    },
    "hosts": {
        "router0": {"port": 6000, "platform": "cisco_ios"},
        "router1": {"port": 6001, "platform": "huawei_smartax"},
    },
}

# If Windows or WSL, the configuration address is 0.0.0.0
# WSL Bug: https://github.com/microsoft/WSL/issues/4983
if detect.docker and "WSL2" in platform.release():
    server_config = default_inventory["default"]["server"]["configuration"]
    server_config["address"] = "0.0.0.0"


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

        self.hosts: dict[str, Host] = {}
        self.allocated_ports: set[str] = set()

        self.shell_plugins = shell_plugins
        self.nos_plugins = nos_plugins
        self.servers_plugins = servers_plugins

        self._load_inventory()
        self._init()
        self._register_nos_plugins()

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
            port: int | list = params.pop("port")
            replicas: int = params.pop("replicas", None)
            self._check_ports_and_replicas_are_okey(port, replicas)
            self._instantiate_host_object(host_name, port, replicas, params)

    def _check_ports_and_replicas_are_okey(self, port, replicas):
        """
        Method to check if the port and replicas are okey

        :param port: integer or list of two integers - port to allocate
        :param replicas: integer - number of hosts to create
        """
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

    def _instantiate_host_object(self, host_name: str, port: int | list[int], replicas: int, params: dict):
        """
        Method that instantiate the host objects. It initializes the hosts
        with the corresponding name, port and network operating system

        :param host: string - name of the host
        :param port: integer or list of two integers - port to allocate
        :param count: integer - number of hosts to create
        :param params: dictionary - parameters to pass to
                                    the host like configurations
        """
        hosts_name, ports = self._get_hosts_and_ports(host_name, port, replicas)
        for h_name, p in zip(hosts_name, ports):
            self._instantiate_single_host_object(h_name, p, params)

    def _get_hosts_and_ports(self, host_name: str, port: int | list[int], replicas: int = None):
        """
        Method to get hosts and ports correctly
        depending on the number of replicas (if exists).

        :param host_name: string - name of the host
        :param port: integer or list of two integers - port to allocate
        :param replicas: integer - number of hosts to create
        """
        hosts_name: set[str] = {}
        ports: set[int] = {}

        if replicas:
            hosts_name = {f"{host_name}{i}" for i in range(replicas)}
            ports = set(range(port[0], port[1] + 1))
        else:
            hosts_name = {host_name}
            ports = {port}
        return hosts_name, ports

    def _instantiate_single_host_object(self, host, port, params):
        """
        Method that instantiate the host objects. It initializes the hosts

        :param host: string - name of the host
        :param port: integer or list of two integers - port to allocate
        :param params: dictionary - parameters to pass to
                                    the host like configurations
        """
        self._allocate_port(port)
        self.hosts[host] = Host(name=host, port=port, fakenos=self, **params)

    def _allocate_port(self, port: int | list[int]) -> None:
        """
        Method to allocate port for host

        :param port: integer or list of two integers -
                     range to allocate port from
        """
        if isinstance(port, int):
            port: list[int] = [port]

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

    def _get_hosts_as_list(self, hosts: str | list = None) -> list[Host]:
        """
        Helper method to get hosts as list

        :param hosts: string or list of strings
        :return: list of strings
        """
        hosts_list: list[Host] = []
        if not hosts:
            hosts = list(self.hosts.keys())
        if isinstance(hosts, str):
            hosts = [hosts]
        hosts_list = [self.hosts[host] for host in hosts]
        return hosts_list

    def start(self, hosts: str | list = None) -> None:
        """
        Function to start NOS servers instances

        :param hosts: single or list of hosts to start by their name.
        """
        hosts: list[str] = self._get_hosts_as_list(hosts)
        self._execute_function_over_hosts(hosts, "start", host_running=False)
        print(
            f"The following devices has been initiated: \
              {[host.name for host in hosts]}"
        )
        log.info("The following devices has been initiated: %s", [host.name for host in hosts])

    def stop(self, hosts: str | list = None) -> None:
        """
        Function to stop NOS servers instances. It waits 2 seconds
        just in case that there is any thread doing something.

        :param hosts: single or list of hosts to stop by their name.
        """
        hosts: list[str] = self._get_hosts_as_list(hosts)
        self._execute_function_over_hosts(hosts, "stop", host_running=True)
        if hosts == list(self.hosts.values()):
            self._join_threads()

    def _join_threads(self) -> None:
        """
        Method to join threads in case that all hosts are stopped.
        """
        all_threads = threading.enumerate()
        for thread in all_threads:
            if thread is not threading.main_thread():
                thread.join()
        while threading.active_count() > 1:
            time.sleep(0.01)

    def _execute_function_over_hosts(self, hosts: list[Host], func: str, host_running: bool = True):
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

    def _register_nos_plugins(self) -> None:
        """
        Method to register NOS plugin with FakeNOS object, all plugins
        must be registered before calling start method.

        :param plugin: OS path string to NOS plugin `.yaml/.yml` or `.py` file,
          dictionary or instance if Nos class
        """
        for plugin in self.plugins:
            if isinstance(plugin, Nos):
                nos_instance = plugin
            else:
                nos_instance = Nos()
                if isinstance(plugin, dict):
                    nos_instance.from_dict(plugin)
                elif isinstance(plugin, str):
                    nos_instance.from_file(plugin)
                else:
                    raise TypeError(f"Unsupported NOS type {type(plugin)}, supported str, dict or Nos")
            self.nos_plugins[nos_instance.name] = nos_instance
