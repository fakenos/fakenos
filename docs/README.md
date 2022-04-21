# Fake Network Operating Systems - FakeNOS

> "Reality is merely an illusion, albeit a very persistent one."
>
> ~ Albert Einstein

FakeNOS created to simulate Network Operating Systems interactions.

[Documentation](https://dmulyalin.github.io/fakenos/)

## Installation

Install [GIT](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), next
install from master:

`python3 -m pip install git+https://github.com/dmulyalin/fakenos`

## Basic Usage

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
```

## Using Inventory

FakeNOS uses Inventory dictionary to define a set of SSH servers to start.

Sample inventory data and code to start the servers:

```
from fakenos import FakeNOS

fake_network = {
    "default": {
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
            "username": "fakenos",
            "password": "fakenos",
            "server": {
                "plugin": "ParamikoSshServer",
                "configuration": {"address": "0.0.0.0"},
            },
            "shell": {
                "plugin": "CMDShell",
                "configuration": {"intro": "Custom SSH Shell"},
            },
        },
        "R2": {},
        "core-router": {"count": 2, "port": [5000, 6000]},
    },
}

network = FakeNOS(inventory=fake_network)
network.starts()

print(network.list_hosts())
```

## FakeNOS Docker Container

FakeNOS GitHub repository contains `docker-compose` and `Docker` files to build
and start FakeNOS in a container. To use it, providing that GIT, Docker and
Docker-Compose installed on the system:

1. Clone FakeNOS repository: `git clone https://github.com/dmulyalin/fakenos.git`
2. Build container: `docker-compose up`
3. Access FakeNOS router: `ssh 10.100.0.2 -l user -p 6001`

## How to Generate SSH private key

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

## FakeNOS inspired by and borrowed from

- [sshim](https://pythonhosted.org/sshim/) - library for testing and debugging SSH automation clients
- [PythonSSHServerTutorial](https://github.com/ramonmeza/PythonSSHServerTutorial) - tutorial on creating paramiko based SSH server
- [fake-switches](https://github.com/internap/fake-switches) - pluggable switch/router command-line simulator
- [ncs-netsim](https://developer.cisco.com/docs/nso/guides/#!the-network-simulator) - tool to simulate a network of devices
- [cisshgo](https://github.com/tbotnz/cisshgo) - concurrent SSH server to emulate network equipment for testing purposes
- [scrapli-replay](https://pypi.org/project/scrapli-replay/) - tools to enable easy testing of SSH programs and to create semi-interactive SSH servers
