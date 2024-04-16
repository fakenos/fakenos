import logging
import copy
import os
import fnmatch
from typing import Union

import yaml

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
        "router0": {"port": 6000},
        "router1": {"port": 6001}
    }
}


class FakeNOS:
    """
    FakeNOS class is a main entry point to interact with fake NOS servers - start, stop, list.

    :param inventory: FakeNOS inventory dictionary or OS path to .yaml file with inventory data
    :param plugins: Plugins to add extra devices/commands currently not supported easily.
    :param log_level: logging level to use

    Sample usage:

    ```python
    from fakenos import FakeNOS

    net = FakeNOS()
    net.start()
    ```
    """

    def __init__(
            self,
            inventory: dict = default_inventory,
            plugins: list = [],
        ) -> None:
        self.inventory: dict = inventory
        self.plugins: list = plugins

        self.hosts: dict = {}
        self.allocated_ports: set[str] = set()

        self.shell_plugins = shell_plugins
        self.nos_plugins = nos_plugins
        self.servers_plugins = servers_plugins

        self._load_inventory()
        self._init()
        self._register_nos_plugins()

    def _is_inventory_in_yaml(self) -> bool:
        """method that checks if the inventory is a yaml file."""
        return isinstance(self.inventory, str) \
            and self.inventory.endswith(".yaml")

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

    def _load_commands_from_inventory_dir(self, host_inventory: dict) -> None:
        """
        Method to load commands content from the inventory dir

        :param host_inventory: dictionary of host's inventory data
        """
        return
        # load commands content
        commands = host_inventory.get("nos", {}).get("configuration", {}).get("commands", {})
        for _, cmd_data in commands.items():
            # form path to command file
            if os.path.isfile(cmd_data.get("output", "")[:100]):
                path_to_cmd_file = cmd_data["output"]
            else:
                path_to_cmd_file = os.path.join(self.inventory_dir, cmd_data.get("output", "")[:100])
            # load file content
            if os.path.isfile(path_to_cmd_file):
                with open(path_to_cmd_file, encoding="utf-8", mode="r") as f:
                    cmd_data["output"] = f.read()

    def _init(self) -> None:
        """
        Helper method to initiate host objects and store them in self.hosts, this
        method called automatically on FakeNOS object instantiation.
        """
        for host, host_config in self.inventory["hosts"].items():
            params = {
                **copy.deepcopy(self.inventory["default"]),
                **copy.deepcopy(host_config),
            }
            port = params.pop("port")
            count = params.pop("count", None)
            self._load_commands_from_inventory_dir(params)
            self._instantiate_host_object(host, port, count, params)


    def _instantiate_host_object(self, host, port, count, params):
        """
        Method that instantiate the host objects. It initializes the hosts
        with the corresponding name, port and network operating system
        """
        if count:
            for i in range(0, count):
                name = f"{host}{i+1}"
                port_ = self._allocate_port(port)
                self.hosts[name] = Host(name=name, port=port_, fakenos=self, **copy.deepcopy(params))
        else:
            port_ = self._allocate_port(port)
            self.hosts[host] = Host(name=host, port=port_, fakenos=self, **params)

    def _allocate_port(self, port: int) -> None:
        """
        Method to allocate port for host

        :param port: integer or list of two integers - range to allocate port from
        """
        if isinstance(port, int):
            if port in self.allocated_ports:
                raise ValueError(f"Port {port} already in use")
            allocated_port = port

        elif isinstance(port, list):
            for p in range(port[0], port[1] + 1):
                if p not in self.allocated_ports:
                    allocated_port = p
                    break
            else:
                raise RuntimeError("Port allocation failed")
        else:
            raise TypeError("Unsupported port type {}, supported int or list".format(type(port)))

        self.allocated_ports.add(allocated_port)

        return allocated_port

    def _split_pattern(self, pattern: Union[str, list[str]]) -> list[str]:
        """
        Helper method to split pattern into a list of patterns.

        :param pattern: glob pattern or list or comma separated list of patterns
        :return: list of patterns
        """
        return pattern if isinstance(pattern, list) else [i.strip() for i in pattern.split(",")]

    def start(self, hosts: Union[str, list[str]] = "*") -> None:
        """
        Function to start NOS servers instances

        :param hosts: glob pattern to match hosts to start by their name or
            list or comma separated list of patterns
        """
        hosts = self._split_pattern(hosts)
        for h in self.hosts.values():
            if not h.running and any(fnmatch.fnmatchcase(h.name, p) for p in hosts):
                h.start()

    def stop(self, hosts: Union[str, list[str]] = "*") -> None:
        """
        Function to stop NOS servers instances

        :param hosts: glob pattern to match hosts to stop by their name or
            list or comma separated list of patterns
        """
        hosts = self._split_pattern(hosts)
        for h in self.hosts.values():
            if h.running and any(fnmatch.fnmatchcase(h.name, p) for p in hosts):
                h.stop()

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
                    raise TypeError("Unsupported NOS type {}, supported str, dict or Nos".format(type(plugin)))
            self.nos_plugins[nos_instance.name] = nos_instance
