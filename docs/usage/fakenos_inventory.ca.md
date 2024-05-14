# Inventari
FakeNOS utilitza un inventari per definir un conjunt d'amfitrions SSH i la seva configuració. És una part clau del projecte. L'inventari és un diccionari que conté dues seccions: `default` i `hosts`. La secció `default` conté paràmetres i configuració que FakeNOS utilitza per defecte per a cada amfitrió. La secció `hosts` és un diccionari indexat pels noms dels amfitrions que contenen la definició de l'amfitrió. Qualsevol paràmetre definit per amfitrió substitueix els paràmetres definits a la secció `default`.

Hi ha dues maneres de proporcionar dades d'inventari a FakeNOS:

1. Utilitzant un fitxer YAML
2. Utilitzant un diccionari de Python

## Estructura bàsica
En tots els casos, les dades de l'inventari han de tenir la següent estructura, independentment del mètode utilitzat per proporcionar-les:

- **default**: Un diccionari que conté paràmetres per defecte i configuració que FakeNOS utilitza per defecte per a cada amfitrió.
- **hosts**: Un diccionari indexat pels noms dels amfitrions que contenen la definició de l'amfitrió. Qualsevol paràmetre definit per amfitrió substitueix els paràmetres definits a la secció `default`.

Sempre és obligatori proporcionar la secció `hosts`. La secció `default` és opcional. Si no es proporciona, FakeNOS utilitza una configuració per defecte. Aquesta estructura funciona de manera jeràrquica, de manera que la secció `hosts` substitueix la secció `default`.

!!! warning
    Tot i que pots canviar lliurement els paràmetres per defecte, es recomana mantenir-los com estan i substituir-los a través de la secció `hosts`. En cas que canvies la secció `default`, has de proporcionar tots els paràmetres que hi ha a la configuració per defecte.

### Inventari per defecte
Si no es proporcionen dades d'inventari en la instanciació de l'objecte FakeNOS, FakeNOS utilitza la configuració d'inventari per defecte. Aquestes són les configuracions per defecte actuals[^1]:
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
Aquesta és la manera més senzilla de proporcionar dades d'inventari. En un senzill fitxer YAML, pots definir les dades de l'inventari. El fitxer YAML ha de tenir l'estructura següent:

``` yaml
default:
  username: user
  password: user
  port: 6000
  platform: cisco_ios
```

En aquest cas, es crearà un amfitrió anomenat `router0` amb el nom d'usuari `user`, contrasenya `user` i port `6000`. La plataforma serà `cisco_ios`. Si vols crear més amfitrions, pots afegir-los a la secció `hosts`:
``` yaml
hosts:
    router1:
        port: 6001
        platform: huawei_smartax
    router2:
        port: 6002
        platform: cisco_ios
```

En aquest cas, es creen 2 amfitrions: `router1` i `router2`. `router1` tindrà el port `6001` i la plataforma `huawei_smartax`. `router2` tindrà el port `6002` i la plataforma `cisco_ios`. Com no s'han proporcionat les credencials a la secció `hosts`, FakeNOS utilitzarà les credencials per defecte.

Per utilitzar el fitxer YAML, pots utilitzar l'eina CLI de FakeNOS:

``` bash
fakenos -i path/to/inventory.yaml
```

## Diccionari de Python
Tot i que YAML és la manera més senzilla de proporcionar dades d'inventari a FakeNOS, utilitzar un diccionari de Python és més flexible i permet estructures de dades d'inventari més complexes. De fet, els diccionaris de Python s'utilitzen internament per gestionar les dades d'inventari a FakeNOS.

En cas que vulguis utilitzar el teu propi diccionari de Python, pots proporcionar-lo directament a FakeNOS. En el següent codi estem fent exactament el mateix que en el primer codi en YAML:

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

Com abans, en cas que vulguis crear més amfitrions, pots afegir-los a la secció `hosts`:
``` python
inventory_data = {
    "hosts": {
        "router1": {"port": 6001, "platform": "huawei_smartax"},
        "router2": {"port": 6002, "platform": "cisco_ios"}
    }
}
```


## Altres examples
Exemples d'inventari i codi per iniciar els servidors:

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

1. `0.0.0.0` - Escolta les connexions a totes les interfícies
2. Sobreescriu `username` i `password` definits a la secció `default`
3. Inicia dos amfitrions `core-router1` i `core-router2` utilitzant el següent port disponible de la gamma proporcionada
4. Configuració utilitzada per tots els amfitrions per defecte

Alternativament, pots utilitzar l'eina CLI de FakeNOS per proporcionar un inventari personalitzat:

``` bash
fakenos -i path/to/my_inventory.yaml
```

On `my_inventory.yaml` podria contenir l'equivalent al codi Python anterior en YAML:

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

O podria contenir un inventari encara més simplificat:

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

### Rèpliques de hosts
Pots veure abans que alguns amfitrions tenen el paràmetre de rèpliques establert. La definició de l'amfitrió pot contenir el paràmetre `replicas` per definir amfitrions en massa, per exemple, aquest inventari:
```python
inventory_data = {
    "hosts": {
        "router": {"replicas": 10, "port": [5001, 6000]}
    }
}
```

Aquesta configuració farà que FakeNOS executi 10 instàncies de servidors d'amfitrions anomenats `router1` a `router10` utilitzant els ports 5001 a 5010 respectivament. Això fa que sigui molt fàcil definir conjunts d'amfitrions que utilitzen la mateixa configuració per escalar el sistema.

!!! warning
    Si les dades de l'inventari de l'amfitrió contenen el paràmetre `replicas`, el paràmetre `port` ha de ser una llista de dos enters que representen l'interval per assignar ports. Si l'amfitrió no conté el paràmetre `replicas`, el port ha de ser un enter positiu de l'interval de 1 a 65535.

## Generar clau privada SSH

Per defecte, FakeNOS utilitza una clau privada SSH incrustada amb el paquet, fent que aquesta clau sigui pública, la qual cosa és insegura. En canvi, FakeNOS pot utilitzar una clau SSH generada localment.

### Linux i MacOS

Utilitza la comanda `ssh-keygen -A` al terminal per generar totes les claus SSH. Un cop s'hagi executat la comanda, pots trobar la clau RSA a la següent ubicació: `~/.ssh/id_rsa` a.k.a. `/home/<username>.ssh/id_rsa`. Proporciona la ruta anterior com a argument `ssh_key_file` a la configuració del servidor FakeNOS.

Alternativament, pots utilitzar la comanda `ckeygen -t rsa -f ssh-keys/ssh_host_rsa_key` per generar la clau privada.

### Windows 10

Prem la tecla de Windows, escriu `Manage Optional Features`. Si OpenSSH Client & Server està a la llista, ja estàs a punt. Si no ho està, fes clic a "Add a feature" i busca `OpenSSH`, fes clic-hi per instal·lar-lo. A continuació, obre l'ordre com a administrador. Introdueix la comanda `ssh-keygen` i segueix les instruccions que apareixen a la pantalla. La ubicació de la clau es mostrarà. Proporciona la ruta mostrada com a argument `ssh_key_file` a la configuració del servidor FakeNOS. Si poses una contrasenya, inclou-la com a paràmetre `ssh_key_file_password`.

## Esquema de l'inventari en JSON

FakeNOS utilitza internament models [Pydantic](https://pydantic-docs.helpmanual.io/usage/models/) per validar les dades de l'inventari i llançar `ValidationError` si l'inventari no compleix l'esquema definit.

Donat que l'inventari està modelat utilitzant Pydantic, l'esquema intern en format JSON seria el següent:

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

## Opcions de l'inventari
Les següents opcions es poden utilitzar tant a la secció `default` com a la secció `hosts` per substituir els valors per defecte.

### Opcions de nivell superior

| Opció        | Emoji         | Descripció                        | Exemple                                         |
| --------------| ------------- | ---------------------------------- | ----------------------------------------------- |
| `username`    | :person:      | nom d'usuari del dispositiu        | `username: admin`                               |
| `password`    | :key:         | contrasenya del dispositiu         | `password: admin`                               |
| `platform`    | :station:     | sistema operatiu de xarxa utilitzat| `platform: cisco_ios`                           |
| `port`        | :ship:        | port al qual connectar-se          | `port: 6000`                                    |
| `replicas`    | :repeat:      | nombre d'amfitrions a crear        | `replicas: 10`                                  |
| `server`      | :satellite:   | configuració del servidor          | Veure la secció [Opcions del servidor](#opcions-del-servidor)   |
| `shell`       | :shell:       | configuració de la shell | Veure la secció [Opcions de la shell](#opcions-de-la-shell)     |
| `nos`         | :computer:    | configuració del NOS               | Veure la secció [Opcions del NOS](#opcions-del-nos)         |

### Opcions del servidor

| Opció                   | Emoji                     | Descripció                           | E.g.                                                                      |
| ------------------------- | ------------------------- | ------------------------------------- | ------------------------------------------------------------------------- |
| `plugin`                  | :electric_plug:           | plugin de servidor a utilitzar                 | `plugin: ParamikoSshServer`                                               |
| `configuration`           | :gear:                    | configuració del servidor                  | Mira secció [Opcions de configuració del servidor](#opcions-de-configuracio-del-servidor) |

### Opcions de configuració del servidor

| Opció                    | Emoji                     | Descripció                           | E.g.                                           |
| ------------------------- | ------------------------- | ------------------------------------- | ---------------------------------------------- |
| `ssh_key_file`            | :key:                     | Ruta a la clau privada de SSH        | `ssh_key_file: /path/to/ssh_key`               |
| `ssh_key_file_password`   | :key:                     | Password de la clau privada de SSH   | `ssh_key_file_password: password`              |
| `ssh_banner`              | :scroll:                  | Banner a mostrar per SSH             | `ssh_banner: "Welcome to FakeNOS SSH Server"`  |
| `timeout`                 | :hourglass:               | timeout del servidor                    | `timeout: 1`                                   |
| `address`                 | :globe_with_meridians:    | Adreça a la que el servidor escolta        | `address: 127.0.0.1`                           |
| `watchdog_interval`       | :dog:                     | interval del watchdog                 | `watchdog_interval: 1`                         |


### Opcions de la shell

| Opció                    | Emoji                     | Descripció                           | E.g.                                                                    |
| ------------------------- | ------------------------- | ------------------------------------- | ----------------------------------------------------------------------- |
| `plugin`                  | :electric_plug:           | plugin de shell a utilizar                   | `plugin: CMDShell`                                                      |
| `configuration`           | :gear:                    | configuració de la shell            | La configuració depén completament del plugin                  |


### Opcions del NOS

| Opció                    | Emoji                     | Descripció                           | E.g.                                                                    |
| ------------------------- | ------------------------- | ------------------------------------- | ----------------------------------------------------------------------- | 
| `plugin`                  | :electric_plug:           | plugin NOS a utilitzar                     | `plugin: cisco_ios`                                                     |
| `configuration`           | :gear:                    | configuració del NOS                     | La configuració del plugin depén completament del plugin          |


[^1]: Per mirar els últims defaults correctament, mira al [codi font](https://github.com/fakenos/fakenos/blob/master/fakenos/core/fakenos.py) de FakeNOS.