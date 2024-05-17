Es poden crear plugins NOS personalitzats per a FakeNOS i registrar-los amb una instància de servidor FakeNOS abans d'iniciar els servidors.

Hi ha diverses maneres de crear un plugin NOS:

1. [Crear un plugin NOS des d'un fitxer YAML](creating_nos_plugin.md#crear-un-plugin-nos-des-dun-fitxer-yaml)
2. [Crear un plugin NOS des d'un fitxer Python](creating_nos_plugin.md#crear-un-plugin-nos-des-dun-fitxer-python)
3. [Crear un plugin NOS des de la classe Nos](creating_nos_plugin.md#crear-un-plugin-nos-des-de-la-classe-nos)

Cap d'aquestes maneres és millor que l'altra, totes elles tenen els seus propis casos d'ús. Però
estan llistats en una seqüència de més senzill de crear/menys flexible a més involucrat/més
flexible.

Els plugins NOS poden tenir aquests atributs definits:

- `name` - nom de referència del plugin per utilitzar a l'inventari
- `initial_prompt` - s'utilitza per definir o alterar el prompt de la consola mostrat
- `enable_prompt` - prompt de la consola d'habilitació
- `commands` - diccionari de comandes que aquest plugin NOS és capaç de retornar la sortida

Cada vegada que es crea un plugin NOS personalitzat a partir de la classe Nos o utilitzant una de les mètodes `from_x` de la classe Nos, es realitza una validació dels atributs utilitzant models Pydantic per assegurar-se que són compatibles amb el format previst.

## Indicador de prompt inicial

El prompt inicial utilitzat pel plugin de shell per formar l'indicador inicial que es mostra a l'usuari de la interfície d'usuari de la línia d'ordres.

L'atribut de prompt inicial és una cadena que té el mètode de format de Python cridat
per derivar el valor final del prompt a utilitzar pel plugin de shell, com a resultat aquests formadors
compatibles:

- `base_prompt` - valor establert igual al nom de l'amfitrió de l'inventari

Per exemple, aquesta és la informació de l'inventari:

```yaml
hosts:
  R1:
    port: 6000
  R2:
    port: 6001
```

En l'inventari anterior, `R1` i `R2` són els noms dels amfitrions i si `initial_prompt` s'estableix a
`RP0/CPU0:{base_prompt}#` valor, després d'aplicar el mètode de format, els indicadors finals seran
`RP0/CPU0:R1#` i `RP0/CPU0:R2#` per a R1 i R2 respectivament.

## Comandes NOS

Les comandes són un diccionari de Python que conté detalls de comandes NOS que gestionen una de les principals fortaleses de FakeNOS.

Les comandes són un diccionari indexat per una cadena de comanda amb un valor que és un altre diccionari
que conté detalls de la comanda com ara la sortida a retornar, indicacions de gestió del prompt, missatge d'ajuda de la comanda i altres.

Contingut de mostra del diccionari de Python de comandes:

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

1. Funció personalitzada per produir la sortida de la comanda
2. Nou prompt per mostrar després de la sortida de la comanda
3. Llista dels indicadors actuals on aquesta comanda és vàlida, és a dir, l'abast de la comanda
4. Sortida de la comanda de múltiples línies
5. Missatge d'ajuda per mostrar per a aquesta comanda si s'entra `?` o `ajuda` a la consola
6. Retornar `None` com a sortida de la comanda no produirà cap resposta
7. Retornar True com a sortida de la comanda tancarà la consola i aturarà aquesta instància del fil del servidor
8. Retornar una sortida buida amb produirà una resposta que només conté caràcters de nova línia
9. La sortida de la comanda pot contenir el formador `base_prompt`
10. El prompt únic on aquesta comanda és vàlida
11. Contingut de resposta per defecte utilitzat per a comandes no definides
12. La soritda pot tenir el `base_prompt`.

Atributs compatibles amb el diccionari de comandes:

| Atribut       | Descripció                                                                                 |
| -------------- | ------------------------------------------------------------------------------------------- |
| `output`       | :material-text-box-multiple-outline:  Sortida de la comanda per retornar en resposta         |
| `help`         | :material-help:                       Contingut del missatge d'ajuda de la comanda          |
| `prompt`       | :material-console-line:               Indicador o llista d'indicadors on aquesta comanda és vàlida |
| `new_prompt`   | :material-line-scan:                  Nou prompt per mostrar després de la resposta de la comanda |

El valor de l'atribut `output` del diccionari de comandes pot ser d'aquests tipus:

- `string` - cadena de línia única o múltiple per retornar en resposta, aquesta cadena
   pot contenir el formador `base_prompt`.
- `None` - no es retorna cap resposta
- `True` - tancarà la consola i aturarà la instància d'aquest servidor
- `callable` - la sortida pot fer referència a una funció, com ara una funció, que es crida
  pel connector de la consola per produir el contingut de la resposta

La funció cridada que fa referència a la sortida de la comanda `output` ha de ser capaç d'acceptar aquests arguments:

- `base_prompt` - valor del nom de l'amfitrió de l'inventari
- `current_prompt` - valor actual del prompt de la consola
- `command` - cadena de comanda introduïda

Alguns apunts sobre els atributs `prompt` i `new_prompt`.

`prompt` serveix com a filtre que indica si aquesta comanda és vàlida en el context actual del prompt, de manera que si el valor actual del prompt no és igual al prompt de la comanda, la sortida de la resposta prové del valor de sortida de la comanda `_default_`, que normalment conté un missatge d'error.

`new_prompt` simplement indica que després que la resposta de la sortida de la comanda es retorni a l'usuari, el valor actual del prompt s'ha d'establir al valor de `new_prompt`.

## Crear un plugin NOS des d'un fitxer YAML

Creeu un fitxer YAML amb aquest contingut de mostra a `path/to/my_nos.yaml`:

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

Codi de mostra per registrar el plugin NOS amb FakeNOS utilitzant el fitxer YAML anterior:

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

1. Feu referència a l'atribut de nom definit al fitxer `path/to/my_nos.yaml`
2. Proporcioneu la ruta absoluta o relativa al fitxer YAML amb la definició NOS

## Crear un plugin NOS des d'un fitxer Python

Creeu un fitxer Python amb aquest contingut de mostra a `path/to/my_nos.py`:

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

Codi de mostra per registrar el plugin NOS amb FakeNOS utilitzant el fitxer Python anterior:

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

1. Feu referència a l'atribut de nom definit al fitxer `path/to/my_nos.py`
2. Proporcioneu la ruta absoluta o relativa al fitxer YAML amb la definició NOS

## Crear un plugin NOS des de la classe Nos

El paquet FakeNOS ve amb la classe base Nos que es pot utilitzar per crear
plugins NOS per registrar-los amb una instància de FakeNOS.

Núcleo de mostra per definir un plugin NOS personalitzat utilitzant
la classe Nos que subministra els atributs necessaris en la instanciació:

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

A més, els mètodes de classe Nos `from_dict` i `from_file` poden ser utilitzats per subministrar atributs Nos. Per exemple, es poden obtenir els resultats equivalents a la secció [Crear un plugin NOS des d'un fitxer Python](creating_nos_plugin.md#crear-un-plugin-nos-des-dun-fitxer-python) utilitzant aquest codi:

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

    Calling any of `from_x` methods replaces existing attributes, no merging performed.