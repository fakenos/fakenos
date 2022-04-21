"""
Host classes
"""
from typing import Union, Callable, Dict, List
import logging

log = logging.getLogger(__name__)

class Host:
    def __init__(
        self,
        name: str,
        username: str,
        password: str,
        port: int,
        server: dict,
        shell: dict,
        nos: dict,
        fakenos,
    ) -> None:
        self.name = name
        self.server_params = server
        self.shell_params = shell
        self.nos_params = nos
        self.username = username
        self.password = password
        self.port = port
        self.fakenos = fakenos
        self.shell_params["configuration"].setdefault("base_prompt", self.name)
        self.running = False
        self.server = None
        self.server_plugin = None
        self.shell_plugin = None
        self.nos_plugin = None

    def start(self):
        """Method to start server instance for this hosts"""
        self.server_plugin = self.fakenos.servers_plugins[self.server_params["plugin"]]
        self.shell_plugin = self.fakenos.shell_plugins[self.shell_params["plugin"]]
        self.nos_plugin = self.fakenos.nos_plugins[self.nos_params["plugin"]]

        self.server = self.server_plugin(
            shell=self.shell_plugin,
            shell_configuration=self.shell_params["configuration"],
            nos=self.nos_plugin,
            port=self.port,
            username=self.username,
            password=self.password,
            **self.server_params["configuration"],
        )
        self.server.start()
        self.running = True

    def stop(self):
        """Method to stop server instance of this host"""
        self.server.stop()
        self.server = None
        self.running = False
