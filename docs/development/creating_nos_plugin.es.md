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
- `enable_prompt` - se utiliza para definir o alterar el indicador de shell que se muestra después de habilitar el modo de ejecución privilegiado.
- `commands` - diccionario de comandos que este plugin NOS es capaz de devolver la salida

Cada vez que se crea un plugin NOS personalizado a partir de la clase Nos o utilizando uno de los métodos `from_x` de Nos, se realiza una validación de los atributos utilizando modelos Pydantic para asegurarse de que cumplan con el formato previsto.

## Indicador de shell inicial NOS

La cadena de indicador inicial utilizada por el plugin de shell para formar el indicador inicial mostrado al usuario de la CLI.

El atributo de indicador inicial es una cadena que tiene un método de formato de Python llamado
para derivar el valor final del indicador a usar por el plugin de shell, como resultado, estos formateadores
son compatibles:

- `base_prompt` - valor establecido igual al nombre del host del inventario

Por ejemplo, estos son los datos del inventario:

```yaml
hosts:
  R1:
    port: 6000
  R2:
    port: 6001
```

En el inventario anterior, `R1` y `R2` son los nombres de los hosts y si `initial_prompt` se establece en
`RP0/CPU0:{base_prompt}#`, después de aplicar el método de formato, los indicadores finales serán
`RP0/CPU0:R1#` y `RP0/CPU0:R2#` para R1 y R2 respectivamente.

## Comandos NOS

Comandos NOS que manejan una de las principales fortalezas de FakeNOS.

Los comandos son un diccionario indexado por una cadena de comando con un valor que es otro diccionario
conteniendo detalles del comando como la salida a devolver, sugerencias de manejo de indicadores, comando
mensaje de ayuda y otros.

Contenido de muestra del diccionario Python de comandos:

```{ .python .annotate }
def make_show_clock(base_prompt, current_prompt, command): # (1)
    "Return String in format '*11:54:03.018 UTC Sat Apr 16 2022'"
    return time.strftime("*%H:%M:%S.000 %Z %a %b %d %Y")
    
commands = {
    "enable": {
        "output": None, # (6)
        "new_prompt": "{base_prompt}#", # (2)
        "help": "enter exec prompt", # (5)
        "prompt": "{base_prompt}>", # (10)
    },
    "show clock": {
        "output": make_show_clock, # (9)
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

| Atributo      | Descripción                                                                                 |
| -------------- | ------------------------------------------------------------------------------------------- |
| `output`       | :material-text-box-multiple-outline:  Salida del comando para devolver en la respuesta      |
| `help`         | :material-help:                       Contenido del mensaje de ayuda del comando          |
| `prompt`       | :material-console-line:               Indicador o lista de indicadores donde este comando es válido |
| `new_prompt`   | :material-line-scan:                  Nuevo indicador para mostrar después de la respuesta del comando |

El valor del atributo `output` del diccionario de comandos puede ser de estos tipos:

- `string` - cadena de una o varias líneas para devolver en la respuesta, esa cadena
   puede contener el formateador `base_prompt`.
- `None` - no se devuelve ninguna respuesta
- `True` - cerrará la shell y detendrá la instancia de este servidor
- `callable` - la salida puede referirse a un objeto llamable, como una función, que se ejecutará por el complemento de la shell para producir el contenido de la respuesta

La función llamable a la que se refiere el comando `output` debe aceptar estos argumentos:

- `base_prompt` - valor del nombre del host del inventario
- `current_prompt` - valor del indicador actual de la shell
- `command` - cadena de comando ingresada

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

Cree un archivo Python con este contenido de muestra en `path/to/my_nos.py`:

```python
name = "MyFakeNOSPlugin"

initial_prompt = "{base_prompt}>"

def make_show_clock(base_prompt, current_prompt, command):
    "Return String in format '*11:54:03.018 UTC Sat Apr 16 2022'"
    return time.strftime("*%H:%M:%S.000 %Z %a %b %d %Y")

running_configuration = """
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname {base_prompt}
!
boot-start-marker
boot-end-marker
"""

show_version = """
Version: 0.1.0
{base_prompt} uptime is 1 day, 17 hours, 32 minutes
Uptime for this control processor is 1 day, 17 hours, 33 minutes

Configuration register is 0x2102
"""

commands = {
    "enable": {
        "output": None,
        "new_prompt": "{base_prompt}#",
        "help": "enter exec prompt",
        "prompt": initial_prompt,
    },
    "show clock": {
        "output": make_show_clock,
        "help": "Display the system clock",
        "prompt": [initial_prompt, "{base_prompt}#"],
    },
    "show running-config": {
        "output": running_configuration,
        "help": "Current operating configuration",
        "prompt": "{base_prompt}#",
    },
    "show version": {
        "output": show_version,
        "help": "System hardware and software status",
        "prompt": "{base_prompt}#",
    },
    "_default_": {
        "output": "% Invalid input detected at '^' marker.",
        "help": "Output to print for unknown commands",
    },
    "terminal width 511": {"output": "", "help": "Set terminal width to 511"},
    "terminal length 0": {"output": "", "help": "Set terminal length to 0"},
}
```

Código de muestra para registrar el plugin NOS con FakeNOS usando el archivo Python anterior:

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

1. Hacer referencia al atributo de nombre definido en el archivo `path/to/my_nos.py`
2. Proporcionar la ruta absoluta o relativa al archivo Python con la definición de NOS

## Crear un plugin NOS a partir de la clase Nos

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
        "terminal length 0": {"output": "", "help": "Set terminal length to 0"},
        "show clock": {"output": "MyFakeNOSPlugin system time is 00:00:00"},
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
	
