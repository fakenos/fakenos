FakeNOS uses inventory data to control its behavior. 

Code example demonstrating how to use FakeNOS inventory dictionary:

```{ .python .annotate }
from fakenos import FakeNOS

inventory_data = {
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
    }
}

network = FakeNOS(inventory=inventory_data)
network.starts()

print(network.list_hosts())
```

1. `0.0.0.0` - Listen for connections on all interfaces
2. Override `username` and `password` defined in `default` section
3. Start two hosts `core-router1` and `core-router2` using next available
   ports from provided range
4. Settings used by all hosts by default 

## FakeNOS Inventory Explained

FakeNOS inventory consists of two top sections - `default` and `hosts` - 
comprising two levels of inventory hierarchy. 

Inventory `default` section contains parameters and configuration that FakeNOS
uses by default for each host.

Inventory `hosts` section is a dictionary keyed by hosts' names containing host
definition. Any parameter defined per-host overrides parameters defined in 
`default` section.

Host definition can contain `count` parameter to define hosts in bulk, e.g.
this inventory:

```python
inventory_data = {
    "hosts": {
        "router": {"count": 10, "port": [5001, 6000]}
    }
}
``` 

will result in FakeNOS running 10 instances of hosts servers named `router1`
to `router10` using ports 5001 to 5010 respectively. That makes it very easy to 
define sets of hosts that use same configuration to scale the setup out.

!!! warning
    
    If host inventory data contains `count` parameter, `port` parameter must be a list 
    of two integers representing range to allocate ports from. If host does not contains
    `count` parameter, `port` must be a positive integer from 1 - 65535 range.

## Inventory JSON Schema

FakeNOS internally uses [Pydantic](https://pydantic-docs.helpmanual.io/usage/models/) 
models to validate inventory data and raise `ValidationError` if inventory does 
not comply with defined schema. 

While inventory modeled using Pydantic models, equivalent JSON Schema looks
like this:

```json
{
    "title": "model_fakenos_inventory",
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

## Default Inventory

If not inventory data provided on FakeNOS object instantiation, FakeNOS falls back 
on using default inventory configuration:

```python
default_inventory = {
    "default": {
        "username": "user",
        "password": "user",
        "port": [10000, 60000],
        "server": {
            "plugin": "ParamikoSshServer",
            "configuration": {
                "address": "0.0.0.0",
                "timeout": 1,
            },
        },
        "shell": {"plugin": "CMDShell", "configuration": {}},
        "nos": {"plugin": "cisco_ios", "configuration": {}},
    },
    "hosts": {
        "router1": {"port": 6001},
        "router2": {"port": 6002},
    },
}
```