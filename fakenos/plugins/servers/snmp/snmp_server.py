"""
TO BE IMPLEMENTED.

This module is a default server
for SNMP functions.
"""

from fakenos.core.nos import Nos


class SNMPServer:
    """ This class is a placeholder for the SNMP server plugin."""
    def __init__(
            self,
            nos=Nos,
            configuration=dict,
    ):
        self.service_name: str = "SNMP"
        self.port: int  = configuration['port']
        
    def start(self):
        pass

    def stop(self):
        pass
