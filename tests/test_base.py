import sys
import pprint

sys.path.insert(0, "..")

from fakenos import FakeNOS

fake_network = {
    "server": {
        "plugin": "ParamikoSshServer",
        "configuration": {
            "ssh_host_key": "./ssh-keys/ssh_host_rsa_key",
            "username": "user",
            "password": "user",
            "address": "127.0.0.1",
            "ports": [5000, 6000],
            "timeout": 1,
        }
    },
    "shell": {
        "plugin": "CMDShell",
        "configuration": {
            "intro": "Custom SSH Shell"
        }        
    },
    "hosts": {
        "ceos1": {
            "nos": "cisco_ios",
            "port": 5001,
            "address": "127.0.0.1",
        },
        "ceos2": {
            "nos": "cisco_ios",
            "port": 5002,
            "address": "127.0.0.1",
        },
        "core-router": {
            "count": 10,
            "nos": "cisco_ios",
            "address": "127.0.0.1",
        }
    }
}


def test_fakenos_base():
    net = FakeNOS()
    pprint.pprint(net.nos)
    
test_fakenos_base()
