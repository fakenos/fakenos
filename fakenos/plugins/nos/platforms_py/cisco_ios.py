"""
NOS module for Cisco IOS
"""

import time

from fakenos.plugins.nos.platforms_py.base_template import BaseDevice

NAME: str = "cisco_ios"
INITIAL_PROMPT: str = "{base_prompt}>"
ENABLE_PROMPT: str = "{base_prompt}#"
CONFIG_PROMPT: str = "{base_prompt}(config)#"
DEVICE_NAME: str = "CiscoIOS"

DEFAULT_CONFIGURATION: str = "fakenos/plugins/nos/platforms_py/configurations/cisco_ios.yaml.j2"


# pylint: disable=unused-argument
class CiscoIOS(BaseDevice):
    """
    Class that keeps track of the state of the Cisco IOS device.
    """

    hola = "Hello test"

    def make_show_clock(self, base_prompt, current_prompt, command):
        "Return String in format '*11:54:03.018 UTC Sat Apr 16 2022'"
        return time.strftime("*%H:%M:%S.000 %Z %a %b %d %Y")

    def make_show_running_config(self, base_prompt, current_prompt, command):
        "Return String of running configuration"
        return self.render("cisco_ios/show_running-config.j2", base_prompt=base_prompt)

    def make_show_version(self, base_prompt, current_prompt, command):
        "Return String of system hardware and software status"
        return self.render("cisco_ios/show_version.j2", base_prompt=base_prompt)


commands = {
    "enable": {
        "output": None,
        "new_prompt": ENABLE_PROMPT,
        "help": "enter exec prompt",
        "prompt": INITIAL_PROMPT,
    },
    "show clock": {
        "output": CiscoIOS.make_show_clock,
        "help": "Display the system clock",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT],
    },
    "show running-config": {
        "output": CiscoIOS.make_show_running_config,
        "help": "Current operating configuration",
        "prompt": ENABLE_PROMPT,
    },
    "show version": {
        "output": CiscoIOS.make_show_version,
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
}
