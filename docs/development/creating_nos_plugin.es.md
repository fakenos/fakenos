Se pueden crear NOS plugins y registrarlos con una instancia de FakeNOS antes de
iniciar los servidores.

Hay varias formas de crear un plugin NOS:

1. [Crear un plugin NOS a partir de un archivo YAML](creating_nos_plugin.md#crear-un-plugin-nos-a-partir-de-un-archivo-yaml)
2. [Crear un plugin NOS a partir de un archivo Python](creating_nos_plugin.md#crear-un-plugin-nos-a-partir-de-un-archivo-python)
3. [Crear un plugin NOS a partir de la clase Nos](creating_nos_plugin.md#crear-un-plugin-nos-a-partir-de-la-clase-nos)

Ninguna de las formas anteriores es mejor que la otra, todas tienen sus propios casos de uso. Pero
se enumeran en un orden de más simple de crear/menos flexible a la más
involucrada/más flexible.

Los plugins NOS pueden tener estos atributos definidos:

- `name` - nombre de referencia del plugin para usar en el inventario
- `initial_prompt` - se utiliza para definir o alterar el indicador de shell que se muestra
- `enable_prompt` - se utiliza para entrar el modo `enable` (opcional)
- `config_prompt` - se utiliza para entrar el modo `config` (opcional)
- `commands` - diccionario de comandos que este plugin NOS es capaz de devolver la salida

## Prompt inicial de la shell NOS
El prompt inicial de la shell NOS es el indicador que se muestra al usuario cuando se inicia la shell.
En el caso de que este definido entre corchetes `{}` se puede utilizar el formateador `base_prompt` para
hacer referencia al nombre del host del inventario.

Por ejemplo, si el prompt inicial se establece en `{base_prompt}>`, después de aplicar el método de formato,
el indicador final será `R1>` para el host `R1` en el inventario.

## Comandos NOS
Los comandos son un diccionario indexado por una cadena de comando con un valor que es otro diccionario
conteniendo detalles del comando como el output, la ayuda de este o los prompts necesario para que 
se llame correctamente.

Contenido de muestra del diccionario Python de comandos:

```{ .python .annotate }
commands = {
    "enable": {
        "output": None, # (6)
        "new_prompt": "{base_prompt}#", # (2)
        "help": "enter exec prompt", # (5)
        "prompt": "{base_prompt}>", # (10)
    },
    "show clock": {
        "output": MyDevice.make_show_clock, # (9)
        "help": "Display the system clock",
        "prompt": ["{base_prompt}>", "{base_prompt}#"], # (3)
    },
    "show running-config": {
        "output": """ # (4)
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname {base_prompt} # (12)
!
boot-start-marker
boot-end-marker
        """,
        "help": "Current operating configuration", 
        "prompt": "{base_prompt}#",
    },
    "show version": {
        "output": """
Version: 0.1.0
{base_prompt} uptime is 1 day, 17 hours, 32 minutes
Uptime for this control processor is 1 day, 17 hours, 33 minutes

Configuration register is 0x2102
        """,
        "help": "System hardware and software status",
        "prompt": "{base_prompt}#",
    },
    "_default_": { # (11)
        "output": "% Invalid input detected at '^' marker.",
        "help": "Output to print for unknown commands",
    },
    "terminal width 511": {
        "output": "", # (8)
        "help": "Set terminal width to 511"
    }, 
    "terminal length 0": {
        "output": "", 
        "help": "Set terminal length to 0"
    },
    "exit": {"output": True, "help": "Exit commands shell"} # (7)
}
```

1. Función personalizada para producir la salida del comando
2. Nuevo indicador para mostrar después de que se devuelva la salida del comando
3. Lista de indicadores actuales donde este comando es válido, es decir, el ámbito del comando
4. Salida de comando de varias líneas
5. Mensaje de ayuda para mostrar para este comando si se ingresa `?` o `help` en la shell
6. Devolver `None` como salida del comando no producirá respuesta
7. Devolver True como salida del comando cerrará la shell y detendrá esta instancia del hilo del servidor
8. Devolver una salida vacía con producirá una respuesta que contenga solo caracteres de nueva línea
9. La salida devuelta puede contener el formateador `base_prompt`
10. El único indicador cuando este comando es válido
11. Contenido de respuesta predeterminado utilizado para comandos no definidos
12. La salida puede referirse a un objeto llamable, como una función, que se ejecutará por el complemento de la shell para producir el contenido de la respuesta

Atributos admitidos por el diccionario de comandos:

| Atributo       | Emoji                            | Descripción                                               |
| -------------- | ---------------------------------| --------------------------------------------------------- |
| `output`       | :octicons-command-palette-16:    | Salida del comando para devolver en la respuesta         |
| `help`         | :material-help-box:              |         Contenido del mensaje de ayuda del comando       |
| `prompt`       | :simple-powershell:              | Indicador o lista de indicadores donde este comando es válido |
| `new_prompt`   | :simple-nushell:                |  Nuevo indicador para mostrar después de la respuesta del comando |
| `alias`        | :material-drama-masks:              |     Salida del comando como una función llamable          |

El valor del atributo `output` del diccionario de comandos puede ser de estos tipos:

- `string` - cadena de una o varias líneas para devolver en la respuesta, esa cadena
   puede contener el formateador `base_prompt`.
- `None` - no se devuelve ninguna respuesta
- `True` - cerrará la shell
- `callable` - la salida puede referirse a un objeto llamable, como una función, que se ejecutará por el complemento de la shell para producir el contenido de la respuesta

Algunas notas sobre los atributos `prompt` y `new_prompt`.

`prompt` sirve como un filtro que indica si este comando es válido en el contexto actual del indicador,
de tal manera que si el valor actual del indicador no es igual al indicador del comando,
la respuesta de salida se obtiene del valor de salida del comando `_default_`, que generalmente
contiene un mensaje de error.

`new_prompt` simplemente indica que después de que se devuelva la respuesta de salida del comando al usuario,
el valor actual del indicador debe establecerse en el valor `new_prompt`.

## Crear un plugin NOS a partir de un archivo YAML

Cree un archivo YAML con este contenido de muestra en `path/to/my_nos.yaml`:

```yaml
name: MyFakeNOSPlugin

initial_prompt: "{base_prompt}>"

commands:
  enable:
    output: null
    new_prompt: "{base_prompt}#"
    help: enter exec prompt
    prompt: "{base_prompt}>"
  show clock:
    output: "*21:01:33.000 AET 01 01 01 2022"
    help: "Display the system clock"
    prompt: ["{base_prompt}#"]
  show running-config:
    output: |
      service timestamps debug datetime msec
      service timestamps log datetime msec
      no service password-encryption
      !
      hostname {base_prompt}
      !
      boot-start-marker
      boot-end-marker
    help: "Current operating configuration"
    prompt: "{base_prompt}#"
  show version:
    output: |
      Version: 0.1.0
      {base_prompt} uptime is 1 day, 17 hours, 32 minutes
      Uptime for this control processor is 1 day, 17 hours, 33 minutes

      Configuration register is 0x2102
    help: System hardware and software status
    prompt: "{base_prompt}#"
  _default_:
    output: "% Invalid input detected at '^' marker."
    help: "Output to print for unknown commands"
  terminal width 511: {"output": "", "help": "Set terminal width to 511"}
  terminal length 0: {"output": "", "help": "Set terminal length to 0"}
```

Código de muestra para registrar el plugin NOS con FakeNOS usando el archivo YAML anterior:

```{ .python .annotate }
from fakenos import FakeNOS

inventory = {
    "hosts": {
        "router1": {
            "port": 6005,
            "nos": {"plugin": "MyFakeNOSPlugin"} # (1)
        }
    }
}

net = FakeNOS(inventory)

net.register_nos_plugin(plugin="path/to/my_nos.yaml") # (2)

net.start()    
```

1. Hacer referencia al atributo de nombre definido en el archivo `path/to/my_nos.yaml`
2. Proporcionar la ruta absoluta o relativa al archivo YAML con la definición de NOS

## Crear un plugin NOS a partir de un archivo Python
Los comandos NOS creados en los módulos Python son un de las principales fortalezas de FakeNOS. La idea de los comandos es que el output de estos en vez de ser una salida predefinida, es que puedes definir una función que devuelva la salida del comando. Esto permite que la salida del comando sea dinámica y pueda cambiar en función de la hora, el día, el host, etc. Si estás desarrollando un módulo Python de NOS, entonces merece la pena leer detenidamente esta sección.

El siguiente código es un módulo Python que utilizamos durantes los tests, pero es completamente funcional (en Netmiko el objeto es generic):
```python
"""
This is a testing module
"""

import time

from fakenos.plugins.nos.platforms_py.base_template import BaseDevice

NAME: str = "test_module"
INITIAL_PROMPT = "{base_prompt}>"
ENABLE_PROMPT = "{base_prompt}#"
CONFIG_PROMPT = "{base_prompt}(config)#"
DEVICE_NAME: str = "TestModule"

DEFAULT_CONFIGURATION: str = "tests/assets/test_module.yaml.j2"


# pylint: disable=unused-argument
class TestModule(BaseDevice):
    """
    Class that keeps track of the state of the TestModule device.
    """

    def make_show_clock(self, base_prompt, current_prompt, command):
        """Return the current time."""
        return str(time.ctime())

    def make_show_version(self, base_prompt, current_prompt, command):
        """Return the system version."""
        return "TestModule version 1.0"


commands = {
    "enable": {
        "output": None,
        "new_prompt": "{base_prompt}#",
        "help": "enter exec prompt",
        "prompt": INITIAL_PROMPT,
    },
    "show clock": {
        "output": TestModule.make_show_clock,
        "help": "show current time",
        "prompt": ["{base_prompt}#", "{base_prompt}>"],
    },
    "show version": {
        "output": TestModule.make_show_version,
        "help": "show system version",
        "prompt": "{base_prompt}#",
    },
}
```

Vayamos por partes. FakeNOS permite cargar los módulos de manera dinámica, pero necesita que el módulo tenga cierta estructura. Por una parte debe tener unas constantes (NAME, INITIAL_PROMPT, ENABLE_PROMPT, CONFIG_PROMPT y DEVICE_NAME), por otra parte un diccionario de comandos y por último una clase que herede de BaseDevice. Esto es obligatorio para que FakeNOS pueda cargar el módulo.

En primer lugar, tenemos los atributos NAME, INITIAL_PROMPT, ENABLE_PROMPT (opcional), CONFIG_PROMPT (opcional) y DEVICE_NAME. Estos atributos son necesarios para que FakeNOS pueda registrar el plugin NOS. NAME es el nombre del plugin, INITIAL_PROMPT es el indicador de shell inicial, ENABLE_PROMPT es el indicador de shell para el modo enable, CONFIG_PROMPT es el indicador de shell para el modo config y DEVICE_NAME es el nombre del dispositivo.

En segundo lugar, tenemos el diccionario de comandos. Este diccionario es un diccionario de Python que contiene los comandos que el plugin NOS es capaz de devolver la salida. Cada comando es un diccionario con los siguientes atributos: "output", "help" y "prompt". El output puede ser un string o una función que devuelva un string. El help es la ayuda que se mostrará al usuario si se introduce el comando `?` o `help`. El prompt es el indicador de shell en el que el comando es válido.

Por último, tenemos un clase que hereda de BaseDevice. Esta clase es necesaria para que FakeNOS pueda cargar el módulo correctamente. Internamente ya inicializa el módulo con un atributo `self.configurations` donde se cargará como un diccionario los datos del archivo de (configuración)[usage/configurations.md] que se haya definido en el atributo `DEFAULT_CONFIGURATION` por defecto. También incluye un método `render (self, template: str, **kwargs) -> str` que permite renderizar un template Jinja2 bajo la dirección `fakenos/plugins/nos/platforms_py/templates/`. El tener esta clase con estos atributos ayuda a estadarizar los módulos. Al mismo, el tenerlo en una clase en vez de funciones sueltas permite que se puedan compartir variables entre los comandos o incluso modificar el estado del dispositivo. Por ejemplo si hago creo un comando para modificar la ip del dispositivo, puedo modificar el estado del dispositivo en la clase y que el resto de comandos tengan en cuenta este cambio, devolviendo el string con la nueva ip.

Obviamente, también puedes crear tu propio módulo Python con tus propios comandos y lógica. Simplemente asegúrate de que tenga la estructura correcta y que se pueda cargar correctamente. Lo has de indicar en el inventario de FakeNOS y FakeNOS se encargará de cargarlo y registrar los comandos.

Código de muestra para registrar el plugin NOS con FakeNOS usando el archivo:

```{ .python .annotate }
from fakenos import FakeNOS

inventory = {
    "hosts": {
        "router1": {
            "port": 6005,
            "nos": {"plugin": "MyFakeNOSPlugin"} # (1)
        }
    }
}

net = FakeNOS(inventory)

net.register_nos_plugin(plugin="path/to/my_nos.py") # (2)

net.start()    
```
## Crear un plugin NOS a partir de la clase Nos
!!! warning
    Se desaconseja desarrollar plugins NOS utilizando la clase NOS directamente, ya que es más complicado de mantener. En su lugar, se recomienda utilizar el módulo Python.

El paquete FakeNOS viene con la clase base Nos que se puede utilizar para crear
plugins NOS para registrarlos con una instancia de FakeNOS.

Núcleo de muestra para definir un plugin NOS personalizado utilizando
la clase Nos suministrando los atributos requeridos en la instanciación:

```python
from fakenos import FakeNOS, Nos

nos = Nos(
    name="MyFakeNOSPlugin",
    initial_prompt="{base_prompt}>",
    commands={
        "terminal length 0": {"output": "", "help": "Set terminal length to 0", "prompt": "{base_prompt}>"},
        "show clock": {"output": "MyFakeNOSPlugin system time is 00:00:00", "help": "Display the system clock", "prompt": "{base_prompt}>"},
    },
)

inventory = {
    "hosts": {
        "router42": {
            "port": 6005,
            "nos": {"plugin": "MyFakeNOSPlugin"},
        },
    }
}

net = FakeNOS(inventory)

net.register_nos_plugin(plugin=nos)

net.start()
```

En este ejemplo, se crea un objeto Nos con los atributos requeridos y se registra con
una instancia de FakeNOS.

Además, los métodos `from_dict` y `from_file` de la clase Nos
se pueden utilizar para suministrar atributos Nos. Por ejemplo, se pueden obtener resultados equivalentes a
[Crear un plugin NOS a partir de un archivo Python](creating_nos_plugin.md#create-nos-plugin-from-python-file)
sección utilizando este código:

```python
from fakenos import FakeNOS, Nos

nos = Nos() # instantiate empty Nos object

nos.from_file("path/to/my_nos.py") # source NOS attributes from file

inventory = {
    "hosts": {
        "router42": {
            "port": 6005,
            "nos": {"plugin": "MyFakeNOSPlugin"},
        },
    }
}

net = FakeNOS(inventory)

net.register_nos_plugin(plugin=nos)

net.start()
```

!!! note
    Llamar a cualquiera de los métodos `from_x` reemplaza los atributos existentes, no se realiza ninguna fusión.
	
