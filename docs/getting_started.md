# Basic Usage

This code starts two devices listening for SSH connections on 127.0.0.1 address
ports 6001 and 6002 named `router1` and `router2` respectively:

```
from fakenos import FakeNOS

network = FakeNOS()
network.start()
```

Initiate SSH connection using default username `user` and password `user`:

```
ssh 127.0.0.1 -l user -p 6001
ssh 127.0.0.1 -l user -p 6002
```

# Using Custom Inventory

FakeNOS uses Inventory dictionary to define a set of SSH servers to start.

Sample inventory data and code to start the servers:

```{ .python .annotate }
from fakenos import FakeNOS

fake_network = {
    "default": { # (4)
        "username": "user",
        "password": "user",
        "port": [5000, 6000],
        "server": {
            "plugin": "ParamikoSshServer",
            "configuration": {
                "ssh_key_file": "./ssh-keys/ssh_host_rsa_key",
                "timeout": 1,
                "address": "127.0.0.1",
            },
        },
        "shell": {"plugin": "CMDShell", "configuration": {}},
        "nos": {"plugin": "cisco_ios", "configuration": {}},
    },
    "hosts": {
        "R1": {
            "port": 5001,
            "username": "fakenos", # (2)
            "password": "fakenos",
            "server": {
                "plugin": "ParamikoSshServer",
                "configuration": {"address": "0.0.0.0"},  # (1)
            },
            "shell": {
                "plugin": "CMDShell",
                "configuration": {"intro": "Custom SSH Shell"},
            },
        },
        "R2": {},
        "core-router": {"count": 2, "port": [5000, 6000]}, # (3)
    },
}

network = FakeNOS(inventory=fake_network)
network.starts()

print(network.list_hosts())
```

1. `0.0.0.0` - Listen for connections on all interfaces
2. Override `username` and `password` defined in `default` section
3. Start two hosts `core-router1` and `core-router2` using next available
   ports from provided range
4. Settings used by all hosts by default

# Generating SSH private key

By default FakeNOS uses SSH private key embedded with the package, making that key
publicly available, which is insecure. Instead, FakeNOS can use locally generated SSH key.

**Linux**

Use the command `ssh-keygen -A` in terminal to generate all of your SSH keys. Once the command is run,
you can find the RSA key in the following location: `~/.ssh/id_rsa` a.k.a. `/home/username/.ssh/id_rsa`.
Supply above path as `ssh_key_file` argument to FakeNOS server configuration.

Alternatively can use `ckeygen -t rsa -f ssh-keys/ssh_host_rsa_key` command to generate private key.

**Windows 10**

Press Windows Key, type `Manage Optional Features`. If OpenSSH Client & Server is in the list, you're all set.
If either is not, click on "Add a feature" and search for `OpenSSH`, click on them to install.
Next, open cmd as administrator. Enter the command `ssh-keygen` and follow the on screen prompts.
The location of the key will be displayed. Supply displayed path as `ssh_key_file` argument to FakeNOS
server configuration. If you put a password, include it as the `ssh_key_file_password` parameter.
