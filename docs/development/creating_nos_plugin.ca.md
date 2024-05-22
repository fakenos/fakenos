Es poden crear plugins NOS i registrar-los amb una instància de FakeNOS abans d'iniciar els servidors.

Hi ha diverses maneres de crear un plugin NOS:

1. [Crear un plugin NOS a partir d'un arxiu YAML](creating_nos_plugin.md#crear-un-plugin-nos-a-partir-dun-arxiu-yaml)
2. [Crear un plugin NOS a partir d'un arxiu Python](creating_nos_plugin.md#crear-un-plugin-nos-a-partir-dun-arxiu-python)
3. [Crear un plugin NOS a partir de la classe Nos](creating_nos_plugin.md#crear-un-plugin-nos-a-partir-de-la-classe-nos)

Cap de les formes anteriors és millor que l'altra, totes tenen els seus propis casos d'ús. Però
s'enumeren en un ordre de més simple de crear/menys flexible a la més
involucrada/més flexible.

Els plugins NOS poden tenir aquests atributs definits:

- `name` - nom de referència del plugin per utilitzar en l'inventari
- `initial_prompt` - s'utilitza per definir o alterar l'indicador de shell que es mostra
- `enable_prompt` - s'utilitza per entrar el mode `enable` (opcional)
- `config_prompt` - s'utilitza per entrar el mode `config` (opcional)
- `commands` - diccionari de comandos que aquest plugin NOS és capaç de retornar la sortida

## Prompt inicial de la shell NOS
El prompt inicial de la shell NOS és l'indicador que es mostra a l'usuari quan s'inicia la shell.
En el cas que aquest estigui definit entre claudàtors `{}` es pot utilitzar el formatejador `base_prompt` per
fer referència al nom de l'amfitrió de l'inventari.

Per exemple, si el prompt inicial s'estableix en `{base_prompt}>`, després d'aplicar el mètode de format,
l'indicador final serà `R1>` per a l'amfitrió `R1` a l'inventari.

## Comandos NOS
Els comandos són un diccionari indexat per una cadena de comando amb un valor que és un altre diccionari
contenint detalls del comando com la sortida, l'ajuda d'aquest o els prompts necessaris perquè
es cridi correctament.

Contingut de mostra del diccionari Python de comandos:

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

1. Funció personalitzada per produir la sortida de la comanda
2. Nou indicador per mostrar després que es retorni la sortida de la comanda
3. Llista d'indicadors actuals on aquesta comanda és vàlida, és a dir, l'abast de la comanda
4. Sortida de comanda de diverses línies
5. Missatge d'ajuda per mostrar per a aquesta comanda si s'entra `?` o `help` a la shell
6. Retornar `None` com a sortida de la comanda no produirà resposta
7. Retornar True com a sortida de la comanda tancarà la shell i aturarà aquesta instància del fil del servidor
8. Retornar una sortida buida amb produirà una resposta que contingui només caràcters de nova línia
9. La sortida de retorn pot contenir el formatejador `base_prompt`
10. L'únic indicador quan aquesta comanda és vàlida
11. Contingut de resposta per defecte utilitzat per a comandes no definides
12. La sortida pot referir-se a un objecte cridable, com una funció, que s'executarà pel complement de la shell per produir el contingut de la resposta

Atributs admesos pel diccionari de comandos:

| Atribut       | Emoji                            | Descripció                                               |
| -------------- | ---------------------------------| --------------------------------------------------------- |
| `output`       | :octicons-command-palette-16:    | Sortida de la comanda per retornar en la resposta         |
| `help`         | :material-help-box:              |         Contingut del missatge d'ajuda de la comanda       |
| `prompt`       | :simple-powershell:              | Indicador o llista d'indicadors on aquesta comanda és vàlida |
| `new_prompt`   | :simple-nushell:                |  Nou indicador per mostrar després de la resposta de la comanda |
| `alias`        | :material-drama-masks:              |     Sortida de la comanda com una funció cridable          |

El valor de l'atribut `output` del diccionari de comandos pot ser d'aquests tipus:

- `string` - cadena d'una o més línies per retornar en la resposta, aquesta cadena
   pot contenir el formatejador `base_prompt`.
- `None` - no es retorna cap resposta
- `True` - tancarà la shell
- `callable` - la sortida pot referir-se a un objecte cridable, com una funció, que s'executarà pel complement de la shell per produir el contingut de la resposta

Algunes notes sobre els atributs `prompt` i `new_prompt`.

`prompt` serveix com a filtre que indica si aquesta comanda és vàlida en el context actual de l'indicador,
de manera que si el valor actual de l'indicador no és igual a l'indicador de la comanda,
la resposta de sortida s'obté del valor de sortida de la comanda `_default_`, que generalment
conté un missatge d'error.

`new_prompt` simplement indica que després que es retorni la resposta de sortida de la comanda a l'usuari,
el valor actual de l'indicador s'ha d'establir en el valor `new_prompt`.

## Crear un plugin NOS a partir d'un arxiu YAML

Creueu un arxiu YAML amb aquest contingut de mostra a `path/to/my_nos.yaml`:

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

Amb aquest arxiu YAML, es podria registrar un plugin NOS de la següent manera:

```yaml
hosts:
    R1:
        username: user
        password: user
        port: 6000
        nos:
            plugin: path/to/my_nos.yaml
```

I per provar-ho ràpidament, es podria executar la següent comanda al terminal:

```bash
fakenos -i path/to/inventory.yaml
```

## Crear un plugin NOS a partir d'un arxiu Python
Els plugins NOS creats a partir mòduls Python són una de les principals fortaleses de FakeNOS ja que permeten una interactivitat. La idea dels comandos és que la sortida d'aquests en lloc de ser una sortida predefinida, és que pots definir una funció que retorni la sortida del comando. Això permet que la sortida del comando sigui dinàmica i pugui canviar en funció de l'hora, el dia, l'amfitrió, etc. Si estàs desenvolupant un mòdul Python de NOS, llavors val la pena llegir detingudament aquesta secció.

El següent codi és un mòdul Python que utilitzem durant els tests, però és completament funcional (en Netmiko l'objecte és genèric):
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

Anem per parts. FakeNOS permet carregar mòduls de manera dinàmica, però necessita que el mòdul tingui una certa estructura. D'una banda ha de tenir unes constants (NAME, INITIAL_PROMPT, ENABLE_PROMPT, CONFIG_PROMPT i DEVICE_NAME), d'altra banda un diccionari de comandos i per últim una classe que hereti de BaseDevice. Això és obligatori perquè FakeNOS pugui carregar el mòdul.

En primer lloc, tenim els atributs NAME, INITIAL_PROMPT, ENABLE_PROMPT (opcional), CONFIG_PROMPT (opcional) i DEVICE_NAME. Aquests atributs són necessaris perquè FakeNOS pugui registrar el plugin NOS. NAME és el nom del plugin, INITIAL_PROMPT és l'indicador de shell inicial, ENABLE_PROMPT és l'indicador de shell per al mode enable, CONFIG_PROMPT és l'indicador de shell per al mode config i DEVICE_NAME és el nom del dispositiu.

En segon lloc, tenim el diccionari de comandos. Aquest diccionari és un diccionari de Python que conté els comandos que el plugin NOS és capaç de retornar la sortida. Cada comando és un diccionari amb els següents atributs: "output", "help" i "prompt". El output pot ser un string o una funció que retorni un string. El help és l'ajuda que es mostrarà a l'usuari si s'introdueix el comando `?` o `help`. El prompt és l'indicador de shell en el qual el comando és vàlid.

Per últim, tenim una classe que hereta de BaseDevice. Aquesta classe és necessària perquè FakeNOS pugui carregar el mòdul correctament. Internament ja inicialitza el mòdul amb un atribut `self.configurations` on es carregarà com un diccionari les dades de l'arxiu de configuració que s'hagi definit a l'atribut `DEFAULT_CONFIGURATION` per defecte. També inclou un mètode `render (self, template: str, **kwargs) -> str` que permet renderitzar un template Jinja2 sota la direcció `fakenos/plugins/nos/platforms_py/templates/`. El tenir aquesta classe amb aquests atributs ajuda a estadaritzar els mòduls. Al mateix, el tenir-lo en una classe en lloc de funcions soltes permet que es puguin compartir variables entre els comandos o fins i tot modificar l'estat del dispositiu. Per exemple si vull crear un comando per modificar la ip del dispositiu, puc modificar l'estat del dispositiu a la classe i que la resta de comandos tinguin en compte aquest canvi, retornant el string amb la nova ip.

Òbviament, també pots crear el teu propi mòdul Python amb els teus propis comandos i lògica. Simplement assegura't que tingui l'estructura correcta i que es pugui carregar correctament. Ho has d'indicar a l'inventari de FakeNOS i FakeNOS s'encarregarà de carregar-lo i registrar els comandos.

Per poder comprovar el codi anterior, podem crear un YAML amb l'inventari tal com hem fet anteriorment:
```yaml
hosts:
    R1:
        username: user
        password: user
        port: 6000
        nos:
            plugin: path/to/my_nos.py
```

I per provar-ho de manera ràpida podem executar la següent comanda al terminal:
```bash
fakenos -i path/to/inventory.yaml
```

## Crear un plugin NOS a partir de la classe Nos
!!! warning
    Es desaconsella desenvolupar plugins NOS utilitzant la classe Nos directament, ja que és més complicat de mantenir. En el seu lloc, es recomana utilitzar el mòdul Python.

El paquet FakeNOS ve amb la classe base Nos que es pot utilitzar per crear plugins NOS per registrar-los amb una instància de FakeNOS. Al final i al cap, anteriorment hem fet el mateix però en lloc de nosaltres crear directament hem deixat que FakeNOS ho faci per nosaltres.

Núcleo de mostra per definir un plugin NOS personalitzat utilitzant la classe Nos subministrant els atributs requerits en la instanciació:

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

try:
    while True:
        pass
except KeyboardInterrupt:
    net.stop()
```

En aquest exemple, es crea un objecte Nos amb els atributs requerits i es registra amb
una instància de FakeNOS.

A més, els mètodes `from_dict` i `from_file` de la classe Nos
es poden utilitzar per subministrar atributs Nos. Per exemple, es poden obtenir resultats equivalents a
[Crear un plugin NOS a partir d'un arxiu Python](#crear-un-plugin-nos-a-partir-dun-arxiu-python)
secció utilitzant aquest codi:

```python
nos = Nos(filename="path/to/my_nos.py")

inventory = {
    "hosts": {
        "router42": {
            "port": 6005,
            "nos": {"plugin": "MyFakeNOSPlugin"},
        },
    }
}
```

!!! note
    Si dos comandos coincideixen amb el mateix nom, el darrer comando que hagis carregat serà el que s'utilitzi.
