from fakenos.plugins.servers import servers_plugins
from fakenos.plugins.nos import nos_plugins
from fakenos.plugins.shell import shell_plugins
from fakenos.core.host import Host
from fakenos.core.nos import Nos
from fakenos.core.pydantic_models import model_fakenos_inventory

from typing import (
    Union,
    Dict,
    List,
)
import logging
import fnmatch
import copy
import yaml
import os

log = logging.getLogger(__name__)

default_inventory = {
    "default": {
        "username": "user",
        "password": "user",
        "port": [10000, 60000],
        "server": {
            "plugin": "ParamikoSshServer",
            "configuration": {
                "address": "0.0.0.0",
                "timeout": 1,
            },
        },
        "shell": {"plugin": "CMDShell", "configuration": {}},
        "nos": {"plugin": "cisco_ios", "configuration": {}},
    },
    "hosts": {
        "router1": {"port": 6001},
        "router2": {"port": 6002},
    },
}


class FakeNOS:
    """
    FakeNOS class is a main entry point to interact with fake NOS servers - start, stop, list.

    :param inventory: FakeNOS inventory dictionary or OS path to .yaml file with inventory data
    :param log_level: logging level to use
    :param inventory_dir: Inventory Directory to search for files, such as commands content

    Sample usage:

    ```python
    from fakenos import FakeNOS

    net = FakeNOS()
    net.start()
    ```
    """

    def __init__(self, inventory: Union[Dict, str] = None, log_level: str = "DEBUG", inventory_dir: str = None) -> None:
        self.inventory = inventory or default_inventory
        self.inventory_dir = inventory_dir
        self.hosts = {}
        self.allocated_ports = set()
        self.shell_plugins = shell_plugins
        self.nos_plugins = nos_plugins
        self.servers_plugins = servers_plugins
        self.log_level = log_level

        self._configure_logging()
        self._load_inventory()
        self.init()

    def _configure_logging(self) -> None:
        """Helper method to setup logging"""
        logging.basicConfig(level=self.log_level.upper())

    def _load_inventory(self) -> None:
        """Helper method to load FakeNOS inventory"""
        # load yaml inventory
        if isinstance(self.inventory, str) and self.inventory.endswith(".yaml"):
            # record inventory location directory
            if self.inventory_dir is None:
                self.inventory_dir = os.path.dirname(self.inventory)
            # open and read inventory file
            with open(self.inventory, "r", encoding="utf-8") as f:
                self.inventory = yaml.safe_load(f.read())

        # make sure we have defaults
        self.inventory["default"] = {
            **default_inventory["default"],
            **self.inventory.get("default", {}),
        }

        # validate inventory data
        inventory_model_instance = model_fakenos_inventory(**self.inventory)
        log.debug("FakeNOS inventory validation succeeded")
        # log.debug(str(inventory_model_instance.schema_json(indent=4)))

    def _load_commands_content(self, host_inventory: Dict) -> None:
        """
        Method to load commands content from files

        :param host_inventory: Dictionary of host's inventory data
        """
        # if no inventory_dir provided/detected - do nothing
        if self.inventory_dir is None:
            return
        # load commands content
        commands = host_inventory.get("nos", {}).get("configuration", {}).get("commands", {})
        for cmd_name, cmd_data in commands.items():
            # form path to command file
            if os.path.isfile(cmd_data.get("output", "")[:100]):
                path_to_cmd_file = cmd_data["output"]
            else:
                path_to_cmd_file = os.path.join(self.inventory_dir, cmd_data.get("output", "")[:100])
            # load file content
            if os.path.isfile(path_to_cmd_file):
                with open(path_to_cmd_file, encoding="utf-8", mode="r") as f:
                    cmd_data["output"] = f.read()

    def init(self) -> None:
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
            # load commands content from files if any
            self._load_commands_content(params)
            # instantiate host(s) object(s)
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

    def _split_pattern(self, pattern: Union[str, List[str]]) -> List[str]:
        """
        Helper method to split pattern into a list of patterns.

        :param pattern: glob pattern or list or comma separated list of patterns
        :return: list of patterns
        """
        return pattern if isinstance(pattern, list) else [i.strip() for i in pattern.split(",")]

    def start(self, hosts: Union[str, List[str]] = "*") -> None:
        """
        Function to start NOS servers instances

        :param hosts: glob pattern to match hosts to start by their name or
            list or comma separated list of patterns
        """
        hosts = self._split_pattern(hosts)
        for h in self.hosts.values():
            if not h.running and any(fnmatch.fnmatchcase(h.name, p) for p in hosts):
                h.start()

    def stop(self, hosts: Union[str, List[str]] = "*") -> None:
        """
        Function to stop NOS servers instances

        :param hosts: glob pattern to match hosts to stop by their name or
            list or comma separated list of patterns
        """
        hosts = self._split_pattern(hosts)
        for h in self.hosts.values():
            if h.running and any(fnmatch.fnmatchcase(h.name, p) for p in hosts):
                h.stop()

    def register_nos_plugin(self, plugin: Union[str, Dict, Nos]) -> None:
        """
        Method to register NOS plugin with FakeNOS object, all plugins
        must be registered before calling start method.

        :param plugin: OS path string to NOS plugin `.yaml/.yml` or `.py` file,
          dictionary or instance if Nos class
        """
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

    def list_hosts(self, hosts: Union[str, List[str]] = "*") -> list:
        """
        Method to produce a list of hosts wit inventory and status information

        :param hosts: glob pattern to match hosts to return by their name or
            list or comma separated list of patterns
        """
        ret = []
        hosts = self._split_pattern(hosts)
        for h in self.hosts.values():
            if any(fnmatch.fnmatchcase(h.name, p) for p in hosts):
                ret.append(
                    {
                        "name": h.name,
                        "nos": h.nos_params["plugin"],
                        "shell": h.shell_params["plugin"],
                        "server": h.server_params["plugin"],
                        "port": h.server.port if h.server else h.port,
                        "address": h.server.address if h.server else None,
                        "base_prompt": h.shell_params["configuration"]["base_prompt"],
                        "running": h.running,
                    }
                )
        return ret
