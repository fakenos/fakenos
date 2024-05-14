# Inventario
FakeNOS utiliza un inventario para definir un conjunto de hosts SSH y su configuración. Es una parte clave del proyecto. El inventario es un diccionario que contiene dos secciones: `default` y `hosts`. La sección `default` contiene parámetros y configuración que FakeNOS utiliza por defecto para cada host. La sección `hosts` es un diccionario indexado por los nombres de los hosts que contienen la definición del host. Cualquier parámetro definido por host anula los parámetros definidos en la sección `default`.

Hay dos formas de proporcionar datos de inventario a FakeNOS:

1. Usando un archivo YAML
2. Usando un diccionario de Python

## Estructura básica
En todos los casos, los datos del inventario deben tener la siguiente estructura, independientemente del método utilizado para proporcionarlos:

- **default**: Un diccionario que contiene parámetros y configuración por defecto que FakeNOS utiliza por defecto para cada host.
- **hosts**: Un diccionario indexado por los nombres de los hosts que contienen la definición del host. Cualquier parámetro definido por host anula los parámetros definidos en la sección `default`.

Es obligatorio proporcionar siempre la sección `hosts`. La sección `default` es opcional. Si no se proporciona, FakeNOS utiliza una configuración por defecto. Esta estructura funciona de forma jerárquica, por lo que la sección `hosts` anulará la sección `default`.

!!! warning
    Aunque puedes cambiar libremente los parámetros por defecto, se recomienda mantenerlos como están y anularlos a través de la sección `hosts`. En caso de que cambies la sección `default`, debes proporcionar todos los parámetros que están en la configuración por defecto.

### Inventario por defecto
Si no se proporcionan datos de inventario en la instanciación del objeto FakeNOS, FakeNOS utiliza la configuración de inventario por defecto. Estos son los valores por defecto actuales[^1]:
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
Esta es la forma más sencilla de proporcionar datos de inventario. En un simple archivo YAML, puedes definir los datos del inventario. El archivo YAML debe tener la siguiente estructura:

``` yaml
default:
  username: user
  password: user
  port: 6000
  platform: cisco_ios
```

En este caso, creará un host llamado `router0` con el nombre de usuario `user`, la contraseña `user` y el puerto `6000`. La plataforma será `cisco_ios`. Si deseas crear más hosts, puedes añadirlos a la sección `hosts`:

``` yaml
hosts:
    router1:
        port: 6001
        platform: huawei_smartax
    router2:
        port: 6002
        platform: cisco_ios
```

En este caso, estás creando 2 hosts: `router1` y `router2`. `router1` tendrá el puerto `6001` y la plataforma `huawei_smartax`. `router2` tendrá el puerto `6002` y la plataforma `cisco_ios`. Como las credenciales no se proporcionan en la sección `hosts`, FakeNOS utilizará las credenciales por defecto.

Para utilizar el archivo YAML, puedes utilizar la herramienta CLI de FakeNOS:

``` bash
fakenos -i path/to/inventory.yaml
```

## Diccionario de Python
Aunque YAML es la forma más sencilla de proporcionar datos de inventario a FakeNOS, utilizar un diccionario de Python es más flexible y permite estructuras de datos de inventario más complejas. De hecho, los diccionarios de Python se utilizan internamente en FakeNOS para manejar los datos del inventario.

En caso de que quieras utilizar tu propio diccionario de Python, puedes proporcionarlo directamente a FakeNOS. En el siguiente código estamos haciendo exactamente lo mismo que en el primer código en YAML:

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

Como antes, en caso de que quieras crear más hosts, puedes añadirlos a la sección `hosts`:

``` python
inventory_data = {
    "hosts": {
        "router1": {"port": 6001, "platform": "huawei_smartax"},
        "router2": {"port": 6002, "platform": "cisco_ios"}
    }
}
```


## Otros ejemplos
Aquí tienes un ejemplo de datos de inventario y código para iniciar los servidores:

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

1. `0.0.0.0` - Dirección IP para escuchar todas las interfaces de red
2. Anula `username` y `password` definidos en la sección `default`
3. Inicia dos hosts `core-router1` y `core-router2` utilizando el siguiente puerto disponible del rango proporcionado
4. Configuración utilizada por todos los hosts por defecto

Una alternativa a ejecutar el código anterior es proporcionar un inventario personalizado a la herramienta CLI de FakeNOS:

``` bash
fakenos -i path/to/my_inventory.yaml
```

Donde `my_inventory.yaml` podría contener un inventario YAML equivalente al código Python anterior:

``` yaml
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

O podría contener este inventario simplificado:

``` yaml
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

### Réplicas de Hosts
Antes se podía ver que algunos hosts tenían el indicador de réplicas establecido. La definición de host puede contener el parámetro `replicas` para definir hosts en bloque, por ejemplo, este inventario:

``` python
inventory_data = {
    "hosts": {
        "router": {"replicas": 10, "port": [5001, 6000]}
    }
}
```

Esta configuración hará que FakeNOS ejecute 10 instancias de servidores de hosts llamados `router1` a `router10` utilizando los puertos 5001 a 5010 respectivamente. Esto hace que sea muy fácil definir conjuntos de hosts que utilizan la misma configuración para escalar la configuración.

!!! warning
    Si los datos del inventario del host contienen el parámetro `replicas`, el parámetro `port` debe ser una lista de dos enteros que representan el rango para asignar puertos. Si el host no contiene el parámetro `replicas`, `port` debe ser un entero positivo del rango de 1 a 65535.

## Generación de la clave privada SSH

Por defecto FakeNOS utiliza la clave privada SSH incrustada con el paquete, lo que hace que esa clave sea pública, lo cual es inseguro. En su lugar, FakeNOS puede utilizar una clave SSH generada localmente.

### Linux y MacOS

Utiliza el comando `ssh-keygen -A` en la terminal para generar todas tus claves SSH. Una vez ejecutado el comando, puedes encontrar la clave RSA en la siguiente ubicación: `~/.ssh/id_rsa` alias `/home/<username>.ssh/id_rsa`. Proporciona la ruta anterior como argumento `ssh_key_file` a la configuración del servidor FakeNOS.

Alternativamente, puedes utilizar el comando `ckeygen -t rsa -f ssh-keys/ssh_host_rsa_key` para generar la clave privada.

### Windows 10

Presiona la tecla de Windows, escribe `Manage Optional Features`. Si OpenSSH Client & Server está en la lista, estás listo.
Si no está, haz clic en "Add a feature" y busca `OpenSSH`, haz clic en ellos para instalarlos.
A continuación, abre cmd como administrador. Introduce el comando `ssh-keygen` y sigue las instrucciones en pantalla.
La ubicación de la clave se mostrará. Proporciona la ruta mostrada como argumento `ssh_key_file` a la configuración del servidor FakeNOS. Si pones una contraseña, inclúyela como el parámetro `ssh_key_file_password`.

## Esquema JSON del Inventario

FakeNOS utiliza internamente modelos [Pydantic](https://pydantic-docs.helpmanual.io/usage/models/) para validar los datos del inventario y lanzar `ValidationError` si el inventario no cumple con el esquema definido.

Mientras el inventario está modelado utilizando modelos de Pydantic, el esquema equivalente en JSON sería así:


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

## Opciones de Inventario
Las siguientes opciones pueden ser utilizadas en la sección `default` o en la sección `hosts` para anular los valores por defecto.

### Opciones de nivel superior

| Opción        | Emoji         | Descripción                        | E.g.                                            |
| --------------| ------------- | ---------------------------------- | ----------------------------------------------- |
| `username`    | :person:      | nombre de usuario del dispositivo  | `username: admin`                               |
| `password`    | :key:         | contraseña del dispositivo         | `password: admin`                               |
| `platform`    | :station:     | sistema operativo de red utilizado | `platform: cisco_ios`                           |
| `port`        | :ship:        | puerto al que conectarse           | `port: 6000`                                    |
| `replicas`    | :repeat:      | número de hosts a crear            | `replicas: 10`                                  |
| `server`      | :satellite:   | configuración del servidor         | Ver la sección [Opciones de servidor](#opciones-de-servidor)   |
| `shell`       | :shell:       | configuración de la shell          | Ver la sección [Opciones de shell](#opciones-de-shell)     |
| `nos`         | :computer:    | configuración de NOS               | Ver la sección [Opciones de NOS](#opciones-de-nos)         |

### Opciones de servidor

| Opción                    | Emoji                     | Descripción                           | E.g.                                                                      |
| ------------------------- | ------------------------- | ------------------------------------- | ------------------------------------------------------------------------- |
| `plugin`                  | :electric_plug:           | plugin del servidor a utilizar        | `plugin: ParamikoSshServer`                                               |
| `configuration`           | :gear:                    | configuración del servidor            | Ver la sección [Opciones de configuración del servidor](#opciones-de-configuración-del-servidor) |

### Opciones de configuración del servidor

| Opción                    | Emoji                     | Descripción                           | E.g.                                           |
| ------------------------- | ------------------------- | ------------------------------------- | ---------------------------------------------- |
| `ssh_key_file`            | :key:                     | ruta al archivo de clave privada SSH  | `ssh_key_file: /path/to/ssh_key`               |
| `ssh_key_file_password`   | :key:                     | contraseña para la clave privada SSH  | `ssh_key_file_password: password`              |
| `ssh_banner`              | :scroll:                  | banner SSH a mostrar                  | `ssh_banner: "Bienvenido al servidor SSH de FakeNOS"`  |
| `timeout`                 | :hourglass:               | tiempo de espera para el servidor     | `timeout: 1`                                   |
| `address`                 | :globe_with_meridians:    | dirección a la que enlazar el servidor | `address: 127.0.0.1`                           |
| `watchdog_interval`       | :dog:                     | interval for watchdog                 | `watchdog_interval: 1`                         |

### Opciones de shell

| Opción                    | Emoji                     | Descripción                           | E.g.                                                                    |
| ------------------------- | ------------------------- | ------------------------------------- | ----------------------------------------------------------------------- |
| `plugin`                  | :electric_plug:           | shell plugin que se utilizará                   | `plugin: CMDShell`                                                      |
| `configuration`           | :gear:                    | configuración del shell                   | La configuración depende completamente del plugin                           |

### Opciones de NOS

| Opción                    | Emoji                     | Descripción                           | E.g.                                                                    |
| ------------------------- | ------------------------- | ------------------------------------- | ----------------------------------------------------------------------- |
| `plugin`                  | :electric_plug:           | NOS plugin usado                     | `plugin: cisco_ios`                                                     |
| `configuration`           | :gear:                    | NOS configuración                     | La configuración depende completamente del plugin                           |

[^1]: Para ver los valores por defecto actuales, consulta el [código fuente](https://github.com/fakenos/fakenos/blob/master/fakenos/core/fakenos.py) de FakeNOS.
