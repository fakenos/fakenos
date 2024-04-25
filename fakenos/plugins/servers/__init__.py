"""
This module is the point of entry for server plugins in FakeNOS.

"""

from .ssh_server_paramiko import ParamikoSshServer

servers_plugins = {"ParamikoSshServer": ParamikoSshServer}
