"""
NOS module for Cisco IOS
"""

import time

from jinja2 import Environment, PackageLoader, select_autoescape

NAME: str = "cisco_ios"
INITIAL_PROMPT: str = "{base_prompt}>"
ENABLE_PROMPT: str = "{base_prompt}#"
CONFIG_PROMPT: str = "{base_prompt}(config)#"
DEVICE_CLASS: str = "CiscoIOS"

env = Environment(
    loader=PackageLoader("fakenos.plugins.nos.platforms_py", "templates"),
    autoescape=select_autoescape(["j2"]),
)

class CiscoIOS:
    """
    Class that keeps track of the state of the Cisco IOS device.
    """
    hola = "Hello test"

cisco_ios: CiscoIOS = CiscoIOS()

# pylint: disable=unused-argument
def make_show_clock(base_prompt, current_prompt, command):
    "Return String in format '*11:54:03.018 UTC Sat Apr 16 2022'"
    return time.strftime("*%H:%M:%S.000 %Z %a %b %d %Y")


def make_show_running_config(base_prompt, current_prompt, command):
    "Return String of running configuration"
    template = env.get_template("cisco_ios/show_running-config.j2")
    return template.render(base_prompt=base_prompt)

def make_test(base_prompt, current_prompt, command):
    "Return String of running configuration"
    return cisco_ios.hola

def make_modify_test(base_prompt, current_prompt, command):
    "Return String of running configuration"
    cisco_ios.hola = "Modified"
    return cisco_ios.hola


def make_show_version(base_prompt, current_prompt, command):
    "Return String of system hardware and software status"
    template = env.get_template("cisco_ios/show_version.j2")
    return template.render(base_prompt=base_prompt)


commands = {
    "enable": {
        "output": None,
        "new_prompt": ENABLE_PROMPT,
        "help": "enter exec prompt",
        "prompt": INITIAL_PROMPT,
    },
    "show clock": {
        "output": make_show_clock,
        "help": "Display the system clock",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT],
    },
    "show running-config": {
        "output": make_show_running_config,
        "help": "Current operating configuration",
        "prompt": ENABLE_PROMPT,
    },
    "show version": {
        "output": make_show_version,
        "help": "System hardware and software status",
        "prompt": ENABLE_PROMPT,
    },
    "_default_": {
        "output": "% Invalid input detected at '^' marker.",
        "help": "Output to print for unknown commands",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT],
    },
    "terminal width 511": {
        "output": "",
        "help": "Set terminal width to 511",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT],
    },
    "terminal length 0": {
        "output": "",
        "help": "Set terminal length to 0",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT],
    },
    "test": {
        "output": make_test,
        "help": "Test",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT],
    },
    "modify test": {
        "output": make_modify_test,
        "help": "Modify Test",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT],
    },
}
