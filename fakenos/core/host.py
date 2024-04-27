"""
This module sets up the host object which is the main object in FakeNOS.
It provides the methods to start and stop the server instance for the host.
It also validates the host object using pydantic.
"""

import logging

from fakenos.core.pydantic_models import ModelHost
from fakenos.core.nos import available_platforms

log = logging.getLogger(__name__)


class Host:
    """
    Host class to build host instances to use with FakeNOS.
    """

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-instance-attributes
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
        platform: str = None,
    ) -> None:
        self.name: str = name
        self.server_inventory: dict = server
        self.shell_inventory: dict = shell
        self.nos_inventory: dict = nos
        self.username: str = username
        self.password: str = password
        self.port: int = port
        self.fakenos = fakenos  # FakeNOS object
        self.shell_inventory["configuration"].setdefault("base_prompt", self.name)
        self.running = False
        self.server = None
        self.server_plugin = None
        self.shell_plugin = None
        self.nos_plugin = None
        self.platform: str = platform

        if self.platform:
            self.nos_inventory["plugin"] = self.platform

        self._validate()

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

    def _validate(self):
        """Validate that the host has the required attributes using pydantic"""
        self._check_if_platform_is_supported(self.platform)
        ModelHost(**self.__dict__)

    def _check_if_platform_is_supported(self, platform: str):
        """Check if the platform is supported"""
        if platform not in available_platforms:
            raise ValueError(
                f"Platform {platform} is not supported by FakeNOS. \
                    Supported platforms are: {available_platforms}"
            )
