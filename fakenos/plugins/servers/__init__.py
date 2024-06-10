"""
This module is the point of entry for server plugins in FakeNOS.

"""

from .cli.ssh_server_paramiko import ParamikoSshServer
from .netconf.netconf_server import NETCONFServer
from .snmp.snmp_server import SNMPServer

servers_plugins = {
    "ParamikoSshServer": ParamikoSshServer,
    "SNMPServer": SNMPServer,
    "NETCONFServer": NETCONFServer,
    }
