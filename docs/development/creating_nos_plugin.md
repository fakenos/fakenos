You can create NOS plugins and register them with a FakeNOS instance before
starting the servers.

There are several ways to create a NOS plugin:

1. [Create a NOS plugin from a YAML file](creating_nos_plugin.md#create-nos-plugin-from-a-yaml-file)
2. [Create a NOS plugin from a Python file](creating_nos_plugin.md#create-nos-plugin-from-a-python-file)
3. [Create a NOS plugin from the Nos class](creating_nos_plugin.md#create-nos-plugin-from-the-nos-class)

None of the above ways is better than the other, all have their own use cases. But
they are listed in an order of more simple to create/less flexible to more
involved/more flexible.

NOS plugins can have these attributes defined:

- `name` - reference name of the plugin to use in the inventory
- `initial_prompt` - used to define or alter the shell prompt that is displayed
- `enable_prompt` - used to enter the `enable` mode (optional)
- `config_prompt` - used to enter the `config` mode (optional)
- `commands` - dictionary of commands that this NOS plugin is capable of returning output

## Initial NOS shell prompt
The initial NOS shell prompt is the indicator that is shown to the user when the shell is started.
In case it is defined within curly braces `{}` you can use the `base_prompt` formatter to
reference the host name from the inventory.

For example, if the initial prompt is set to `{base_prompt}>`, after applying the format method,
the final prompt will be `R1>` for the host `R1` in the inventory.

## NOS commands
Commands are a dictionary indexed by a command string with a value that is another dictionary
containing details of the command like the output, help of this or the prompts needed for it
to be called correctly.

Sample content of the Python commands dictionary:

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

1. Custom function to produce the command output
2. New prompt to show after the command output is returned
3. List of current prompts where this command is valid, i.e., the scope of the command
4. Multi-line command output
5. Help message to show for this command if `?` or `help` is entered in the shell
6. Returning `None` as command output will not produce a response
7. Returning True as command output will close the shell
8. Returning an empty output with produce a response containing only newline characters
9. The returned output can contain the `base_prompt` formatter
10. The only prompt where this command is valid
11. Default response content used for undefined commands
12. The output can refer to a callable object, like a function, that will be executed by the shell plugin to produce the response content

Attributes supported by the commands dictionary:

| Attribute       | Emoji                            | Description                                               |
| -------------- | ---------------------------------| --------------------------------------------------------- |
| `output`       | :octicons-command-palette-16:    | Command output to return in the response                  |
| `help`         | :material-help-box:              | Command help message content                              |
| `prompt`       | :simple-powershell:              | Indicator or list of indicators where this command is valid |
| `new_prompt`   | :simple-nushell:                | New prompt to show after the command output is returned   |
| `alias`        | :material-drama-masks:              | Command output as a callable function                      |


The value of the `output` attribute of the commands dictionary can be of these types:

- `string` - string of one or more lines to return in the response, that string
   can contain the `base_prompt` formatter.
- `None` - no response is returned
- `True` - will close the shell
- `callable` - the returned output can refer to a callable object, like a function, that will be executed by the shell plugin to produce the response content

Some notes about the `prompt` and `new_prompt` attributes.

`prompt` serves as a filter indicating if this command is valid in the current context of the prompt,
so that if the current value of the prompt is not equal to the command prompt,
the response output is obtained from the output value of the `_default_` command, which usually
contains an error message.

`new_prompt` simply indicates that after the command output is returned to the user,
the current prompt value should be set to the `new_prompt` value.

## Create a NOS plugin from a YAML file

Create a YAML file with this sample content in `path/to/my_nos.yaml`:

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

With this YAML file, you can register a NOS plugin like this:

```yaml
hosts:
    R1:
        username: user
        password: user
        port: 6000
        nos:
            plugin: path/to/my_nos.yaml
```

And to quickly test it, you can run this command in the terminal:

```bash
fakenos -i path/to/inventory.yaml
```

## Create a NOS plugin from a Python file

NOS plugins created from Python modules are one of the main strengths of FakeNOS as they allow for interactivity. The idea of the commands is that the output of these instead of being a predefined output, you can define a function that returns the output of the command. This allows the output of the command to be dynamic and can change depending on the time, day, host, etc. If you are developing a Python NOS module, then it is worth reading this section carefully.

The following code is a Python module that we use during tests, but it is fully functional (in Netmiko the object is generic):

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

Let's break it down. FakeNOS allows loading modules dynamically, but it needs the module to have a certain structure. On one hand, it must have some constants (NAME, INITIAL_PROMPT, ENABLE_PROMPT, CONFIG_PROMPT, and DEVICE_NAME), on the other hand, a dictionary of commands, and lastly a class that inherits from BaseDevice. This is mandatory for FakeNOS to be able to load the module.

First, we have the attributes NAME, INITIAL_PROMPT, ENABLE_PROMPT (optional), CONFIG_PROMPT (optional), and DEVICE_NAME. These attributes are necessary for FakeNOS to register the NOS plugin. NAME is the name of the plugin, INITIAL_PROMPT is the initial shell indicator, ENABLE_PROMPT is the shell indicator for the enable mode, CONFIG_PROMPT is the shell indicator for the config mode, and DEVICE_NAME is the name of the device.

Second, we have the dictionary of commands. This dictionary is a Python dictionary that contains the commands that the NOS plugin is capable of returning the output. Each command is a dictionary with the following attributes: "output", "help", and "prompt". The output can be a string or a function that returns a string. The help is the help that will be shown to the user if the `?` or `help` command is entered. The prompt is the shell indicator in which the command is valid.

Lastly, we have a class that inherits from BaseDevice. This class is necessary for FakeNOS to be able to load the module correctly. Internally, it already initializes the module with an attribute `self.configurations` where the data from the [configuration](usage/configurations.md) file defined in the `DEFAULT_CONFIGURATION` attribute by default will be loaded as a dictionary. It also includes a method `render(self, template: str, **kwargs) -> str` that allows rendering a Jinja2 template under the `fakenos/plugins/nos/platforms_py/templates/` directory. Having this class with these attributes helps to standardize the modules. At the same time, having it in a class instead of separate functions allows you to share variables between commands or even modify the state of the device. For example, if I create a command to modify the IP of the device, I can modify the state of the device in the class and have the rest of the commands take this change into account, returning the string with the new IP.

Obviously, you can also create your own Python module with your own commands and logic. Just make sure it has the correct structure and can be loaded correctly. You have to indicate it in the FakeNOS inventory and FakeNOS will take care of loading it and registering the commands.

To be able to check the above code, we can create a YAML with the inventory as we have done before:
```yaml
hosts:
    R1:
        username: user
        password: user
        port: 6000
        nos:
            plugin: path/to/my_nos.py
```

And to test it quickly, you can run the following command in the terminal:
```bash
fakenos -i path/to/inventory.yaml
```

## Create a NOS plugin from the Nos class
!!! warning
    It is discouraged to develop NOS plugins using the Nos class directly as it is more complicated to maintain. Instead, it is recommended to use the Python module.

The FakeNOS package comes with the base class Nos that can be used to create
NOS plugins to register them with a FakeNOS instance. After all, we have previously done the same but instead of creating it ourselves, we have let FakeNOS do it for us.

Sample core to define a custom NOS plugin using
the Nos class by supplying the required attributes during instantiation:

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

In this example, an object Nos is created with the required attributes and registered with
an instance of FakeNOS.

Additionally, the methods `from_dict` and `from_file` of the Nos class
can be used to supply Nos attributes. For example, you can get equivalent results to
[Create a NOS plugin from a Python file](creating_nos_plugin.md#create-nos-plugin-from-a-python-file)
section using this code:

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
    If two commands match the same name, the last command loaded will be used.

