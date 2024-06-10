"""
This module sets up the host object which is the main object in FakeNOS.
It provides the methods to start and stop the server instance for the host.
It also validates the host object using pydantic.
"""

import logging

from fakenos.core.pydantic_models import ModelHost
from fakenos.core.nos import Nos, available_platforms
from fakenos.plugins.servers import servers_plugins

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
        servers: dict,
        nos: dict,
        fakenos,
        platform: str = None,
        configuration_file: str = None,
    ) -> None:
        self.name: str = name
        self.servers_inventory: dict = servers
        self.nos_inventory: dict = nos
        self.fakenos = fakenos
        self.servers: list = []
        self.running = False
        self.nos_plugin = None
        self.nos = None
        self.configuration_file: str = configuration_file
        self.platform: str = platform

        if self.platform:
            self.nos_inventory["plugin"] = self.platform

        self._validate()

    def start(self):
        """
        Method to start server instances for this hosts.
        Here it starts services like SSH, SNMP or NETCONF.
        """
        if self.platform:
            self.nos_inventory["plugin"] = self.platform
        self.nos=Nos(
                    configuration_file=self.configuration_file,
                    platform=self.platform
                )
        for server in self.servers_inventory:
            serv_obj = servers_plugins[server["plugin"]]
            serv = serv_obj(nos=self.nos, configuration=server["configuration"])
            serv.start()
            self.servers.append(serv)
        self.running = True

    def stop(self):
        """Method to stop server instance of this host"""
        for server in self.servers:
            server.stop()
        self.servers.clear()
        self.running = False

    def _validate(self):
        """Validate that the host has the required attributes using pydantic"""
        if self.platform:
            self._check_if_platform_is_supported(self.platform)
        ModelHost(**self.__dict__)

    def _check_if_platform_is_supported(self, platform: str):
        """Check if the platform is supported"""
        if platform not in available_platforms:
            raise ValueError(
                f"Platform {platform} is not supported by FakeNOS. \
                    Supported platforms are: {available_platforms}"
            )
