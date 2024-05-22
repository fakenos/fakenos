NOS plugins could be created and registered with FakeNOS instance prior to 
starting the servers.

There are several ways to create NOS plugin:

1. [Create NOS plugin from YAML file](creating_nos_plugin.md#create-nos-plugin-from-yaml-file)
2. [Create NOS plugin from Python file](creating_nos_plugin.md#create-nos-plugin-from-python-file)
3. [Create NOS plugin from Nos class](creating_nos_plugin.md#create-nos-plugin-from-nos-class)

None of above is better, all of them have their own use cases. But 
they listed from simplest to create/less flexible to more involved/most
flexible order.

NOS plugins could have these attributes defined:

- `name` - reference plugin name to use in inventory
- `initial_prompt` - used to define or alter displayed shell prompt
- `enable_prompt` - prompt to enter the `enable` mode (optional)
- `config_prompt` - prompt to enter the `config` mode (optional)
- `commands` - dictionary of commands this NOS plugin capable of returning output for

Each time custom NOS plugin created out of Nos class or using one of Nos class 
`from_x` methods, attributes validation performed using Pydantic models to ensure 
they are compliant with intended format.

## NOS Initial Prompt

Initial prompt string used by shell plugin to form initial prompt displayed
to CLI user. 

Initial prompt attribute is a string that has Python format method called
to derive final prompt value to use by shell plugin, as a result these formatters
supported:

- `base_prompt` - value set equal to inventory host's name

For example, this is the inventory data:

```yaml
hosts:
  R1:
    port: 6000
  R2:
    port: 6001
```

In above inventory `R1` and `R2` are the host names and if `initial_prompt` set to
`{base_prompt}#` value, after applying format method final prompts will be 
`R1#` and `R2#` for R1 and R2 respectively.

## NOS Commands

NOS Commands handling one of (if not main) FakeNOS strength. 

Commands is a dictionary keyed by command string with value being another dictionary
containing command details such as output to return, prompt handling hints, command 
help message and others.

Sample commands Python dictionary content:

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

1. Custom function to produce command output
2. New prompt to display after command output returned
3. List of current prompts where this command is valid, i.e. command scope
4. Multi-line command output
5. Help message to display for this command if `?` or `help` entered in shell
6. Returning `None` as command output will produce no response
7. Returning True as command output will exit command line interface shell,
   close connection and terminate this instance of server thread
8. Returning empty output with produce a response containing new line characters only
9. Returned callable will be called by shell plugin to produce response 
10. The only prompt when this command is valid 
11. Default response content used for undefined commands
12. Output can contain `base_promt` formatter

Attributes supported by command dictionary:

| Attribute      | Description                                                                                 |
| -------------- | ------------------------------------------------------------------------------------------- |
| `output`       | :material-text-box-multiple-outline:  Command output to return in response                  |
| `help`         | :material-help:                       Command help message content                          |
| `prompt`       | :material-console-line:               Prompt or list of prompts where this command is valid |
| `new_prompt`   | :material-line-scan:                  New prompt to display after command response          |

Command dictionary `output` attribute value can be of these types:

- `string` - single or multi line string to return in response, that string 
   can contain `base_prompt` formatter.
- `None` - no response returned at all
- `True` - will result in closing shell and stopping instance of this server
- `callable` - output can refer to callable, such as function, that callable 
  executed by shell plugin to produce response content
  
Callable function that command `output` refers to should accept these arguments:

- `base_prompt` - inventory host name value
- `current_prompt` - shell's current prompt value
- `command` - entered command string

Few notes on `prompt` and `new_prompt` atributes.

`prompt` serves as a filter that indicates whether this command is valid in current 
prompt context, in such a way that if current prompt value does not equal to command's 
`prompt`, response output sourced from `_default_` command output value, which usually 
contains error message. 

`new_prompt` simply indicates that after command output response delivered back to the 
user current prompt value need to be set to `new_prompt` value.

## Create NOS plugin from YAML file

Create YAML file with this sample content at `path/to/my_nos.yaml`:

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

Sample code to register NOS plugin with FakeNOS using above YAML file:

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

1. Refer to name attribute defined in `path/to/my_nos.yaml` file
2. Supply absolute or relative path to YAML file with NOS definition

## Create NOS plugin from Python file

Create Python file with this sample content at `path/to/my_nos.py`:

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

Sample code to register NOS plugin with FakeNOS using above py file:

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

1. Refer to name attribute defined in `path/to/my_nos.py` file
2. Supply absolute or relative path to YAML file with NOS definition

## Create NOS plugin from Nos class

FakeNOS package comes with base Nos class that can be used to create
NOS plugins to register them with FakeNOS instance.

Sample core to define custom NOS plugin using Nos class supplying
required attributes on instantiation:

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

In addition, Nos class `from_dict` or `from_file` methods 
can be used to supply Nos attributes. For example, equivalent to 
[Create NOS plugin from Python file](creating_nos_plugin.md#create-nos-plugin-from-python-file)
section results can be obtained using this code:

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
	
