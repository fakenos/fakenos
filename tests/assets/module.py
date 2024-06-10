"""
This is a testing module
"""

import time

from fakenos.plugins.nos.platforms_py.platforms.base_template import BaseDevice

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

    def make_show_clock(self, **kwargs):
        """Return the current time."""
        return str(time.ctime())

    def make_show_version(self, **kwargs):
        """Return the system version."""
        return "TestModule version 1.0"

    def make_show_interface_status(self, **kwargs):
        """Return the interface status."""
        return f"Interface status {kwargs['args']}: up"


commands = {
    "enable": {
        "output": None,
        "new_prompt": "{base_prompt}#",
        "help": "enter exec prompt",
        "prompt": INITIAL_PROMPT,
    },
    "sh[[ow]] int[[erface]] st[[atus]] \\S+": {
        "output": TestModule.make_show_interface_status,
        "help": "show interface status",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT],
    },
    "sh[[ow]] cl[[ock]]": {
        "output": TestModule.make_show_clock,
        "help": "show current time",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT],
    },
    "show version": {
        "output": TestModule.make_show_version,
        "help": "show system version",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT],
    },
    "_default_": {
        "output": "Unknown command",
        "help": "Output to print for unknown commands",
    }
}
