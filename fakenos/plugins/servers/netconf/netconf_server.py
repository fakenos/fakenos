"""
TO BE IMPLEMENTED.

This module is a default server
for NETCONF functions.
"""

from fakenos.core.nos import Nos


class NETCONFServer:
    """ This class is a placeholder for the NETCONF server plugin."""
    def __init__(
            self,
            nos=Nos,
            configuration=dict,
    ):
        self.service_name: str = "NETCONF"
        self.port: int = configuration["port"]

    def start(self):
        pass

    def stop(self):
        pass
