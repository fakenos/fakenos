"""
Main module to interact with FakeNOS servers.
It is the entry point to start, stop and list FakeNOS servers.
"""

import copy
from functools import wraps
import inspect
import logging
import os
import platform
import socket
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union

import detect
import yaml

from fakenos.core.host import Host
from fakenos.core.nos import Nos
from fakenos.core.pydantic_models import ModelFakenosInventory
from fakenos.plugins.nos import nos_plugins
from fakenos.plugins.servers import servers_plugins
from fakenos.plugins.shell import shell_plugins

log = logging.getLogger(__name__)

default_inventory: Dict[str, Any] = {
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
        "router_cisco_ios": {"port": 6000, "platform": "cisco_ios"},
        "router_huawei_smartax": {"port": 6001, "platform": "huawei_smartax"},
        "router_arista_eos": {"port": 6002, "platform": "arista_eos"},
    },
}

Inventory = Union[dict, str, os.PathLike[str]]

# If Windows or WSL, the configuration address is 0.0.0.0
# WSL Bug: https://github.com/microsoft/WSL/issues/4983
if detect.docker and "WSL2" in platform.release():
    server_config = default_inventory["default"]["server"]["configuration"]
    server_config["address"] = "0.0.0.0"  # noqa: S104


class FakeNOS:
    """
    FakeNOS class is a main entry point to interact
    with fake NOS servers - start, stop, list.

    :param inventory: FakeNOS inventory dictionary or
                      OS path to a .yaml/.yml file with inventory data
    :param plugins: Custom NOS definitions to register.

    Sample usage:

    ```python
    from fakenos import FakeNOS

    net = FakeNOS()
    net.start()
    ```
    """

    def __init__(
        self,
        inventory: Optional[Inventory] = None,
        plugins: Optional[list] = None,
    ) -> None:
        self._using_default_inventory = inventory is None
        self._default_nos_plugin_configured = False
        self.inventory: Inventory = copy.deepcopy(default_inventory if inventory is None else inventory)
        self.plugins: list = plugins or []

        self.hosts: Dict[str, Host] = {}
        self.allocated_ports: Set[int] = set()

        self.shell_plugins = shell_plugins.copy()
        self.nos_plugins = nos_plugins.copy()
        self.servers_plugins = servers_plugins.copy()

        self._load_inventory()
        self._register_nos_plugins()
        self._init()

    def __enter__(self) -> "FakeNOS":
        """
        Method to start the FakeNOS servers when entering the context manager.
        It is meant to be used with the `with` statement.
        """
        self.start()
        return self

    def __exit__(self, *args) -> None:
        """
        Method to stop the FakeNOS servers when exiting the context manager.
        It is meant to be used with the `with` statement.
        """
        self.stop()

    def _is_inventory_in_yaml(self) -> bool:
        """method that checks if the inventory is a yaml file."""
        return isinstance(self.inventory, (str, os.PathLike)) and os.fspath(self.inventory).lower().endswith(
            (".yaml", ".yml")
        )

    def _load_inventory_yaml(self) -> None:
        """Helper method to load FakeNOS inventory if it is yaml."""
        with open(os.fspath(self.inventory), "r", encoding="utf-8") as f:
            self.inventory = yaml.safe_load(f.read())

    def _load_inventory(self) -> None:
        """Helper method to load FakeNOS inventory"""
        if self._is_inventory_in_yaml():
            self._load_inventory_yaml()

        if not isinstance(self.inventory, dict):
            raise TypeError("Inventory must be a dictionary or a path to a .yaml/.yml file")

        if not self._using_default_inventory:
            default_nos = (self.inventory.get("default") or {}).get("nos") or {}
            self._default_nos_plugin_configured = bool(default_nos.get("plugin"))

        self.inventory["default"] = self._merge_dicts(
            default_inventory["default"],
            self.inventory.get("default") or {},
        )
        ModelFakenosInventory(**self.inventory)
        log.debug("FakeNOS inventory validation succeeded")

    @classmethod
    def _merge_dicts(cls, defaults: dict, overrides: dict) -> dict:
        """Recursively merge inventory mappings without mutating either input."""
        merged = copy.deepcopy(defaults)
        for key, value in overrides.items():
            if isinstance(merged.get(key), dict) and isinstance(value, dict):
                merged[key] = cls._merge_dicts(merged[key], value)
            else:
                merged[key] = copy.deepcopy(value)
        return merged

    def _init(self) -> None:
        """
        Helper method to initiate host objects
        and store them in self.hosts, this
        method called automatically on FakeNOS object instantiation.
        """
        for host_name, host_config in self.inventory["hosts"].items():
            params = self._merge_dicts(self.inventory["default"], host_config)
            for section in ("server", "shell", "nos"):
                if not params.get(section):
                    params[section] = copy.deepcopy(default_inventory["default"][section])
            port: Union[int, List[int]] = params.pop("port")
            replicas: Optional[int] = params.pop("replicas", None)
            self._set_platform_as_nos_plugin(host_config, params)
            self._check_ports_and_replicas_are_valid(port, replicas)
            self._instantiate_host_object(host_name, port, replicas, params)

    def _set_platform_as_nos_plugin(self, host_config: dict, params: dict) -> None:
        """Derive the NOS plugin from platform unless one was configured explicitly."""
        host_nos = host_config.get("nos") or {}
        host_nos_plugin_configured = bool(host_nos.get("plugin"))
        if params.get("platform") and not host_nos_plugin_configured and not self._default_nos_plugin_configured:
            params["nos"]["plugin"] = params["platform"]

    def _check_ports_and_replicas_are_valid(
        self,
        port: Union[int, List[int]],
        replicas: Optional[int],
    ) -> None:
        """
        Method to check if the port and replicas are valid.

        :param port: integer or list of two integers - port to allocate
        :param replicas: integer - number of hosts to create
        """
        ports = port if isinstance(port, list) else [port]
        if any(port_number < 1 or port_number > 65535 for port_number in ports):
            raise ValueError("Ports must be between 1 and 65535.")
        if replicas is None:
            if isinstance(port, list):
                raise ValueError("If replicas is not set, port must be an integer.")
            return
        if not isinstance(port, list):
            raise ValueError("If replicas is set, port must be a list of two integers.")
        if len(port) != 2:
            raise ValueError("If replicas is set, port must be a list of two integers.")
        if port[0] >= port[1]:
            raise ValueError("If replicas is set, port[0] must be less than port[1].")
        if replicas < 1:
            raise ValueError("If replicas is set, replicas must be greater than 0.")
        if port[1] - port[0] + 1 != replicas:
            raise ValueError(
                "If replicas is set, port range \
                    must be equal to the number of replicas."
            )

    def _instantiate_host_object(
        self,
        host_name: str,
        port: Union[int, List[int]],
        replicas: Optional[int],
        params: dict,
    ) -> None:
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

    def _get_hosts_and_ports(
        self,
        host_name: str,
        port: Union[int, List[int]],
        replicas: Optional[int] = None,
    ) -> Tuple[List[str], List[int]]:
        """
        Method to get hosts and ports correctly
        depending on the number of replicas (if exists).

        :param host_name: string - name of the host
        :param port: integer or list of two integers - port to allocate
        :param replicas: integer - number of hosts to create
        """
        if replicas is not None:
            if not isinstance(port, list):
                raise TypeError("Replica ports must be a list")
            return (
                [f"{host_name}{i}" for i in range(replicas)],
                list(range(port[0], port[1] + 1)),
            )
        if not isinstance(port, int):
            raise TypeError("A non-replica port must be an integer")
        return [host_name], [port]

    def _instantiate_single_host_object(self, host: str, port: int, params: dict) -> None:
        """
        Method that instantiate the host objects. It initializes the hosts

        :param host: string - name of the host
        :param port: integer or list of two integers - port to allocate
        :param params: dictionary - parameters to pass to
                                    the host like configurations
        """
        self._allocate_port(port)
        self.hosts[host] = Host(name=host, port=port, fakenos=self, **params)

    def _allocate_port(self, port: Union[int, List[int]]) -> None:
        """
        Method to allocate port for host

        :param port: integer or list of two integers -
                     range to allocate port from
        """
        if isinstance(port, int):
            ports = [port]
        else:
            ports = port

        for allocated_port in ports:
            self._allocate_port_single(allocated_port)

    def _allocate_port_single(self, port: int) -> None:
        """
        Method to allocate single port for host.

        :param port: integer - port to allocate
        """
        if port in self.allocated_ports:
            raise ValueError(f"Port {port} already in use")
        self.allocated_ports.add(port)

    def _get_hosts_as_list(self, hosts: Optional[Union[str, List[str]]] = None) -> List[Host]:
        """
        Helper method to get hosts as list

        :param hosts: string or list of strings
        :return: list of Host objects
        """
        if not hosts:
            hosts = list(self.hosts.keys())
        if isinstance(hosts, str):
            hosts = [hosts]
        return [self.hosts[host] for host in hosts]

    def start(self, hosts: Optional[Union[str, List[str]]] = None) -> None:
        """
        Function to start NOS servers instances

        :param hosts: single or list of hosts to start by their name.
        """
        resolved_hosts = self._get_hosts_as_list(hosts)
        self._execute_function_over_hosts(resolved_hosts, "start", host_running=False)
        log.info(
            "The following devices have been initiated: %s",
            [host.name for host in resolved_hosts],
        )
        for host in resolved_hosts:
            log.info("Device %s is running on port %s", host.name, host.port)

    def stop(self, hosts: Optional[Union[str, List[str]]] = None) -> None:
        """
        Function to stop NOS server instances.

        :param hosts: single or list of hosts to stop by their name.
        """
        resolved_hosts = self._get_hosts_as_list(hosts)
        self._execute_function_over_hosts(resolved_hosts, "stop", host_running=True)

    def _execute_function_over_hosts(self, hosts: List[Host], func: str, host_running: bool = True) -> None:
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
            nos_instance.validate()
            self.nos_plugins[nos_instance.name] = nos_instance


def _get_free_port() -> int:
    """
    Method to get a free port for the FakeNOS server.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def fakenos(
    platform: Optional[str] = None,
    inventory: Optional[Inventory] = None,
    return_instance: bool = False,
) -> Callable:
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

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            with FakeNOS(inventory=inventory) as net:
                if return_instance:
                    return func(*args, net=net, **kwargs)
                return func(*args, **kwargs)

        if return_instance:
            parameters = [
                parameter for parameter in inspect.signature(func).parameters.values() if parameter.name != "net"
            ]
            setattr(wrapper, "__signature__", inspect.signature(func).replace(parameters=parameters))
        return wrapper

    return decorator
