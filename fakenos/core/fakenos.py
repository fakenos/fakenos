from fakenos.plugins.servers import servers_plugins
from fakenos.plugins.nos import nos_plugins, nos_builders
from fakenos.plugins.shell import shell_plugins
from fakenos.core.host import Host
from fakenos.core.nos import Nos

from typing import (
    Union,
    Callable,
    Dict,
)
import logging
import fnmatch
import copy

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
    def __init__(self, inventory=None, log_level="DEBUG"):
        self.inventory = inventory or default_inventory
        self.hosts = {}
        self.allocated_ports = set()
        self.shell_plugins = shell_plugins
        self.nos_plugins = nos_plugins
        self.servers_plugins = servers_plugins
        self.log_level = log_level

        # set logging
        logging.basicConfig(level=self.log_level.upper())

        # make sure we have defaults
        self.inventory["default"] = {
            **default_inventory["default"],
            **self.inventory.get("default", {}),
        }

        # initiate host objects
        for host, host_config in self.inventory["hosts"].items():
            params = {
                **copy.deepcopy(self.inventory["default"]),
                **copy.deepcopy(host_config),
            }
            port = params.pop("port")
            count = params.pop("count", None)
            if count:
                for i in range(0, count):
                    name = f"{host}{i+1}"
                    port_ = self._allocate_port(port)
                    self.hosts[name] = Host(
                        name=name, port=port_, fakenos=self, **copy.deepcopy(params)
                    )
            else:
                port_ = self._allocate_port(port)
                self.hosts[host] = Host(name=host, port=port_, fakenos=self, **params)

    def _allocate_port(self, port):
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
            raise TypeError(
                "Unsupported port type {}, supported int or list".format(type(port))
            )

        self.allocated_ports.add(allocated_port)

        return allocated_port

    def start(self):
        """Function to start NOS servers instances"""
        for host in self.hosts.values():
            host.start()

    def stop(self):
        """Function to stop NOS servers instances"""
        for host in self.hosts.values():
            host.stop()

    def register_nos_plugin(self, name: str, nos: Union[str, Dict, Nos]):
        """
        Method to register NOS plugin with FakeNOS object, all plugins
        must be registered before calling start method.

        :param name: Name of NOS plugin
        :param nos: OS path string to plugin .yaml file, dictionary or instance if Nos
        """
        if isinstance(nos, Nos):
            self.nos_plugins[name] = nos
        elif isinstance(nos, dict):
            self.nos_plugins[name] = nos_builders["dict_builder"](nos)
        elif isinstance(nos, str):
            self.nos_plugins[name] = nos_builders["yaml_builder"](nos)
        else:
            raise TypeError(
                "Unsupported NOS type {}, supported str, dict or Nos".format(type(nos))
            )

    def list_hosts(self, hosts: str = "*"):
        """
        Method to produce a list of hosts wit inventory and status information

        :param hosts: glob pattern to match hosts by name
        """
        ret = []
        for h in self.hosts.values():
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
