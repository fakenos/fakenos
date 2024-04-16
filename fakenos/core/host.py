"""
Host classes
"""
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
        platform: str,
        fakenos,
    ) -> None:
        self.name = name
        self.server_inventory = server
        self.shell_inventory = shell
        self.nos_inventory = nos
        self.username = username
        self.password = password
        self.port = port
        self.platform = platform
        self.fakenos = fakenos
        self.shell_inventory["configuration"].setdefault("base_prompt", self.name)
        self.running = False
        self.server = None
        self.server_plugin = None
        self.shell_plugin = None
        self.nos_plugin = None

    def start(self):
        """Method to start server instance for this hosts"""
        self.server_plugin = self.fakenos.servers_plugins[self.server_inventory["plugin"]]
        self.shell_plugin = self.fakenos.shell_plugins[self.shell_inventory["plugin"]]
        if self.platform:
            self.nos_inventory["plugin"] = self.platform
        self.nos_plugin = self.fakenos.nos_plugins[self.nos_inventory["plugin"]]

        self.server = self.server_plugin(
            shell=self.shell_plugin,
            shell_configuration=self.shell_inventory["configuration"],
            nos=self.nos_plugin,
            nos_inventory_config=self.nos_inventory.get("configuration", {}),
            port=self.port,
            username=self.username,
            password=self.password,
            **self.server_inventory["configuration"],
        )
        self.server.start()
        self.running = True

    def stop(self):
        """Method to stop server instance of this host"""
        self.server.stop()
        self.server = None
        self.running = False
