from fakenos.plugins.servers import servers_plugins
from fakenos.plugins.nos import nos_plugins
from fakenos.plugins.shell import shell_plugins
import logging

log = logging.getLogger(__name__)
logging.basicConfig(level="DEBUG")

default_server = {
    "plugin": "ParamikoSshServer",
    "configuration": {
        # "ssh_key_file": "./ssh-keys/ssh_host_rsa_key",
        "username": "user",
        "password": "user",
    },
}

default_shell = {"plugin": "CMDShell", "configuration": {"intro": "Custom SSH Shell"}}

default_hosts = {
    "router1": {"nos": "cisco_ios", "port": 6001},
    "router2": {"nos": "cisco_ios", "port": 6002},
    "router-x": {"nos": "cisco_ios", "count": 5, "port": [10001, 10005]},
}


class FakeNOS:
    def __init__(self, server=None, shell=None, hosts=None):
        self.server = server or default_server
        self.shell = shell or default_shell
        self.hosts = hosts or default_hosts
        self.nos = {}

        self.start()

    def start(self):
        """Function to start NOS servers instances"""
        server = servers_plugins[self.server["plugin"]]

        for hostname, host_config in self.hosts.items():
            if host_config.get("count"):
                ports = host_config["port"]
                ports = list(range(ports[0], ports[1] + 1))
                for i in range(0, host_config["count"]):
                    derived_hostname = f"{hostname}{i+1}"
                    self.nos[derived_hostname] = {
                        "server": server(
                            shell=shell_plugins[self.shell["plugin"]],
                            shell_configuration={
                                "base_prompt": derived_hostname,
                                **self.shell["configuration"],
                            },
                            nos=nos_plugins[host_config["nos"]],
                            port=ports[i],
                            **self.server["configuration"],
                        ),
                        "port": ports[i],
                        "shell_plugin": self.shell["plugin"],
                        "server_plugin": self.server["plugin"],
                        "address": self.server["configuration"].get(
                            "address", "127.0.0.1"
                        ),
                        "nos": host_config["nos"],
                    }
                    self.nos[derived_hostname]["server"].start()
            else:
                self.nos[hostname] = {
                    "server": server(
                        shell=shell_plugins[self.shell["plugin"]],
                        shell_configuration={
                            "base_prompt": hostname,
                            **self.shell["configuration"],
                        },
                        nos=nos_plugins[host_config["nos"]],
                        port=host_config["port"],
                        **self.server["configuration"],
                    ),
                    "port": host_config["port"],
                    "shell_plugin": self.shell["plugin"],
                    "server_plugin": self.server["plugin"],
                    "address": self.server["configuration"].get("address", "127.0.0.1"),
                    "nos": host_config["nos"],
                }
                self.nos[hostname]["server"].start()

    def stop(self):
        """Function to stop NOS servers instances"""
        for host in self.nos.values():
            host.stop()
