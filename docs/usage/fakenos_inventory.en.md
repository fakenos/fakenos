# Inventory
FakeNOS uses an inventory to define a set of SSH hosts and their configuration. It is a key part to the project. The inventory is a dictionary that contains two sections: `default` and `hosts`. The `default` section contains parameters and configuration that FakeNOS uses by default for each host. The `hosts` section is a dictionary keyed by hosts' names containing host definition. Any parameter defined per-host overrides parameters defined in the `default` section.

The are two ways to provide inventory data to FakeNOS:

1. Using YAML file
2. Using Python dictionary

## Basic structure
In all cases the inventory data must have the following structure independently of the method used to provide it:

- **default**: A dictionary containing default parameters and configuration that FakeNOS uses by default for each host.
- **hosts**: A dictionary keyed by hosts' names containing host definition. Any parameter defined per-host overrides parameters defined in the `default` section.

It is mandatory always to provide the `hosts` section. The `default` section is optional. If not provided, FakeNOS uses a default configuration. This stucture works in hierarchical way, so the `hosts` section will override the `default` section.

!!! warning
    Even though you can freely change the default parameters, it is recommended to keep them as they are and override them through the `hosts` section. In case you change the `default` section, you must provide all the parameters that are in the default configuration.

### Default inventory
If no inventory data provided on FakeNOS object instantiation, FakeNOS falls back on using default inventory configuration. These are the current defaults[^1]:
``` py linenums="1" hl_lines="16 17 18 19"
default_inventory = {
    "default": {
        "username": "user",
        "password": "user",
        "port": 6000,
        "server": {
            "plugin": "ParamikoSshServer",
            "configuration": {
                "address": "127.0.0.1",
                "timeout": 1,
            },
        },
        "shell": {"plugin": "CMDShell", "configuration": {}},
        "nos": {"plugin": "cisco_ios", "configuration": {}},
    },
    "hosts": {
        "router_cisco_ios": {"port": 6000, "platform":"cisco_ios"},
        "router_huawei_smartax": {"port": 6001, "platform": "huawei_smartax"}
        "router_arista_eos": {"port": 6002, "platform": "arista_eos"}
    }
}
```

## YAML
This is the easier way to provide inventory data. In a simple YAML file, you can define the inventory data. The YAML file must have the following structure:

``` yaml
default:
  username: user
  password: user
  port: 6000
  platform: cisco_ios
```

In this case, it will create a host named `router0` with the username `user`, password `user`, and port `6000`. The platform will be `cisco_ios`. If you want to create more hosts, you can add them to the `hosts` section:

``` yaml
hosts:
    router1:
        port: 6001
        platform: huawei_smartax
    router2:
        port: 6002
        platform: cisco_ios
```

In this case, you are creating 2 hosts: `router1` and `router2`. `router1` will have the port `6001` and the platform `huawei_smartax`. `router2` will have the port `6002` and the platform `cisco_ios`. As the credentials are not provided in the `hosts` section, FakeNOS will use the default credentials.

To use the YAML file, you can use the FakeNOS CLI tool:

``` bash
fakenos -i path/to/inventory.yaml
```

## Python dictionary
Although YAML is the easier way to provide inventory data to FakeNOS, using Python dictionary is more flexible and allows for more complex inventory data structures. As a matter of fact, python dictionaries are used internally by FakeNOS to handle the inventory data.

In case you want to use your own Python dictionary, you can provide it directly to FakeNOS. In the following code we are doing exactly the same as the first code in YAML:

``` python
from fakenos import FakeNOS

inventory_data = {
    "hosts": {
        "username": "user",
        "password": "user",
        "port": 6000,
        "platform": "cisco_ios",
    }
}

network = FakeNOS(inventory=inventory_data)
```

As before, in case that you want to create more hosts, you can add them to the `hosts` section:

``` python
inventory_data = {
    "hosts": {
        "router1": {"port": 6001, "platform": "huawei_smartax"},
        "router2": {"port": 6002, "platform": "cisco_ios"}
    }
}
```


## Other examples
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
        "core-router": {"replicas": 2, "port": [5000, 6000]}, # (3)
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

Alternative to running above code is to supply custom inventory to
FakeNOS CLI tool:

```bash
fakenos -i path/to/my_inventory.yaml
```

Where `my_inventory.yaml` could contain equivalent to above Python code 
YAML structured inventory:

```yaml
default:
  password: user
  username: user
  port: [5000, 6000]
  server:
    plugin: ParamikoSshServer
    configuration:
      address: 127.0.0.1
      ssh_key_file: ./ssh-keys/ssh_host_rsa_key
      timeout: 1
  shell:
    configuration: {}
    plugin: CMDShell
  nos:
    configuration: {}
    plugin: cisco_ios
hosts:
  R1:
    password: fakenos
    port: 5001
    username: fakenos
    server:
      plugin: ParamikoSshServer
      configuration:
        address: 0.0.0.0
    shell:
      plugin: CMDShell
      configuration:
        intro: Custom SSH Shell
  R2: {}
  core-router:
    replicas: 2
    port: [5000, 6000]
```

Or could contain this simplified inventory:

```yaml
default:
  password: user
  username: user
  port: [5000, 6000]
  server:
    plugin: ParamikoSshServer
    configuration:
      address: 0.0.0.0
hosts:
  router:
    replicas: 10
    platform: cisco_ios
```

### Hosts replicas
You could see before that some host have the replicas flag set. Host definition can contain `replicas` parameter to define hosts in bulk, e.g. this inventory:

```python
inventory_data = {
    "hosts": {
        "router": {"replicas": 10, "port": [5001, 6000]}
    }
}
```

This configuration will result in FakeNOS running 10 instances of hosts servers named `router1` to `router10` using ports 5001 to 5010 respectively. That makes it very easy to define sets of hosts that use same configuration to scale the setup out.

!!! warning
    If host inventory data contains `replicas` parameter, `port` parameter must be a list
    of two integers representing range to allocate ports from. If host does not contains
    `replicas` parameter, `port` must be a positive integer from 1 - 65535 range.

## Generating SSH private key

By default FakeNOS uses SSH private key embedded with the package, making that key publicly available, which is insecure. Instead, FakeNOS can use locally generated SSH key.

### Linux and MacOS

Use the command `ssh-keygen -A` in terminal to generate all of your SSH keys. Once the command is run,
you can find the RSA key in the following location: `~/.ssh/id_rsa` a.k.a. `/home/<username>.ssh/id_rsa`.
Supply above path as `ssh_key_file` argument to FakeNOS server configuration.

Alternatively can use `ckeygen -t rsa -f ssh-keys/ssh_host_rsa_key` command to generate private key.

### Windows 10

Press Windows Key, type `Manage Optional Features`. If OpenSSH Client & Server is in the list, you're all set.
If either is not, click on "Add a feature" and search for `OpenSSH`, click on them to install.
Next, open cmd as administrator. Enter the command `ssh-keygen` and follow the on screen prompts.
The location of the key will be displayed. Supply displayed path as `ssh_key_file` argument to FakeNOS
server configuration. If you put a password, include it as the `ssh_key_file_password` parameter.


## Inventory JSON Schema

FakeNOS internally uses [Pydantic](https://pydantic-docs.helpmanual.io/usage/models/)
models to validate inventory data and raise `ValidationError` if inventory does
not comply with defined schema.

While inventory modeled using Pydantic models, equivalent JSON Schema looks
like this:

```json
{
    "title": "ModelFakenosInventory",
    "description": "FakeNOS inventory data schema",
    "type": "object",
    "properties": {
        "default": {
            "$ref": "#/definitions/InventoryDefaultSection"
        },
        "hosts": {
            "title": "Hosts",
            "type": "object",
            "additionalProperties": {
                "$ref": "#/definitions/HostConfig"
            }
        }
    },
    "required": [
        "hosts"
    ],
    "additionalProperties": false,
    "definitions": {
        "ParamikoSshServerConfig": {
            "title": "ParamikoSshServerConfig",
            "type": "object",
            "properties": {
                "ssh_key_file": {
                    "title": "Ssh Key File",
                    "type": "string"
                },
                "ssh_key_file_password": {
                    "title": "Ssh Key File Password",
                    "type": "string"
                },
                "ssh_banner": {
                    "title": "Ssh Banner",
                    "default": "FakeNOS Paramiko SSH Server",
                    "type": "string"
                },
                "timeout": {
                    "title": "Timeout",
                    "default": 1,
                    "type": "integer"
                },
                "address": {
                    "title": "Address",
                    "anyOf": [
                        {
                            "enum": [
                                "localhost"
                            ],
                            "type": "string"
                        },
                        {
                            "type": "string",
                            "format": "ipvanyaddress"
                        }
                    ]
                },
                "watchdog_interval": {
                    "title": "Watchdog Interval",
                    "default": 1,
                    "type": "integer"
                }
            }
        },
        "ParamikoSshServerPlugin": {
            "title": "ParamikoSshServerPlugin",
            "type": "object",
            "properties": {
                "plugin": {
                    "title": "Plugin",
                    "enum": [
                        "ParamikoSshServer"
                    ],
                    "type": "string"
                },
                "configuration": {
                    "$ref": "#/definitions/ParamikoSshServerConfig"
                }
            },
            "required": [
                "plugin"
            ]
        },
        "CMDShellConfig": {
            "title": "CMDShellConfig",
            "type": "object",
            "properties": {
                "intro": {
                    "title": "Intro",
                    "default": "Custom SSH Shell",
                    "type": "string"
                },
                "ruler": {
                    "title": "Ruler",
                    "default": "",
                    "type": "string"
                },
                "completekey": {
                    "title": "Completekey",
                    "default": "tab",
                    "type": "string"
                },
                "newline": {
                    "title": "Newline",
                    "default": "\r\n",
                    "type": "string"
                }
            }
        },
        "CMDShellPlugin": {
            "title": "CMDShellPlugin",
            "type": "object",
            "properties": {
                "plugin": {
                    "title": "Plugin",
                    "enum": [
                        "CMDShell"
                    ],
                    "type": "string"
                },
                "configuration": {
                    "$ref": "#/definitions/CMDShellConfig"
                }
            },
            "required": [
                "plugin"
            ]
        },
        "NosPlugin": {
            "title": "NosPlugin",
            "type": "object",
            "properties": {
                "plugin": {
                    "title": "Plugin",
                    "type": "string"
                },
                "configuration": {
                    "title": "Configuration",
                    "type": "object"
                }
            },
            "required": [
                "plugin"
            ]
        },
        "InventoryDefaultSection": {
            "title": "InventoryDefaultSection",
            "type": "object",
            "properties": {
                "username": {
                    "title": "Username",
                    "type": "string"
                },
                "password": {
                    "title": "Password",
                    "type": "string"
                },
                "port": {
                    "title": "Port",
                    "anyOf": [
                        {
                            "type": "integer",
                            "exclusiveMinimum": 0,
                            "maximum": 65535
                        },
                        {
                            "type": "array",
                            "items": {
                                "type": "integer",
                                "exclusiveMinimum": 0,
                                "maximum": 65535
                            },
                            "minItems": 2,
                            "maxItems": 2,
                            "uniqueItems": true
                        }
                    ]
                },
                "server": {
                    "$ref": "#/definitions/ParamikoSshServerPlugin"
                },
                "shell": {
                    "$ref": "#/definitions/CMDShellPlugin"
                },
                "nos": {
                    "$ref": "#/definitions/NosPlugin"
                }
            }
        },
        "HostConfig": {
            "title": "HostConfig",
            "type": "object",
            "properties": {
                "username": {
                    "title": "Username",
                    "type": "string"
                },
                "password": {
                    "title": "Password",
                    "type": "string"
                },
                "port": {
                    "title": "Port",
                    "anyOf": [
                        {
                            "type": "integer",
                            "exclusiveMinimum": 0,
                            "maximum": 65535
                        },
                        {
                            "type": "array",
                            "items": {
                                "type": "integer",
                                "exclusiveMinimum": 0,
                                "maximum": 65535
                            },
                            "minItems": 2,
                            "maxItems": 2,
                            "uniqueItems": true
                        }
                    ]
                },
                "server": {
                    "$ref": "#/definitions/ParamikoSshServerPlugin"
                },
                "shell": {
                    "$ref": "#/definitions/CMDShellPlugin"
                },
                "nos": {
                    "$ref": "#/definitions/NosPlugin"
                },
                "count": {
                    "title": "Count",
                    "exclusiveMinimum": 0,
                    "type": "integer"
                }
            }
        }
    }
}
```

## Inventory options
The following options can be used either in the `default` section or in the `hosts` section to override the default values.

### Top-level options

| Option        | Emoji         | Description                        | E.g.                                            |
| --------------| ------------- | ---------------------------------- | ----------------------------------------------- |
| `username`    | :person:      | username of the device             | `username: admin`                               |
| `password`    | :key:         | password of the device             | `password: admin`                               |
| `platform`    | :station:     | network operating system used      | `platform: cisco_ios`                           |
| `port`        | :ship:        | port to connect to                 | `port: 6000`                                    |
| `replicas`    | :repeat:      | number of hosts to create          | `replicas: 10`                                  |
| `server`      | :satellite:   | server configuration               | See section [Server options](#server-options)   |
| `shell`       | :shell:       | shell configuration                | See section [Shell options](#shell-options)     |
| `nos`         | :computer:    | NOS configuration                  | See section [NOS options](#nos-options)         |

### Server options

| Option                    | Emoji                     | Description                           | E.g.                                                                      |
| ------------------------- | ------------------------- | ------------------------------------- | ------------------------------------------------------------------------- |
| `plugin`                  | :electric_plug:           | server plugin to use                  | `plugin: ParamikoSshServer`                                               |
| `configuration`           | :gear:                    | server configuration                  | See section [Server configuration options](#server-configuration-options) |

### Server configuration options

| Option                    | Emoji                     | Description                           | E.g.                                           |
| ------------------------- | ------------------------- | ------------------------------------- | ---------------------------------------------- |
| `ssh_key_file`            | :key:                     | path to SSH private key file          | `ssh_key_file: /path/to/ssh_key`               |
| `ssh_key_file_password`   | :key:                     | password for SSH private key          | `ssh_key_file_password: password`              |
| `ssh_banner`              | :scroll:                  | SSH banner to display                 | `ssh_banner: "Welcome to FakeNOS SSH Server"`  |
| `timeout`                 | :hourglass:               | timeout for server                    | `timeout: 1`                                   |
| `address`                 | :globe_with_meridians:    | address to bind server to             | `address: 127.0.0.1`                           |
| `watchdog_interval`       | :dog:                     | interval for watchdog                 | `watchdog_interval: 1`                         |


### Shell options

| Option                    | Emoji                     | Description                           | E.g.                                                                    |
| ------------------------- | ------------------------- | ------------------------------------- | ----------------------------------------------------------------------- |
| `plugin`                  | :electric_plug:           | shell plugin to use                   | `plugin: CMDShell`                                                      |
| `configuration`           | :gear:                    | shell configuration                   | The configuration entirely rely on the plugin                           |


### NOS options

| Option                    | Emoji                     | Description                           | E.g.                                                                    |
| ------------------------- | ------------------------- | ------------------------------------- | ----------------------------------------------------------------------- | 
| `plugin`                  | :electric_plug:           | NOS plugin to use                     | `plugin: cisco_ios`                                                     |
| `configuration`           | :gear:                    | NOS configuration                     | The configuration entirely rely on the plugin                           |


[^1]: To see the current defaults, check the [source code](https://github.com/fakenos/fakenos/blob/master/fakenos/core/fakenos.py) of FakeNOS.