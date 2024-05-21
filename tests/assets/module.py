"""
This is a testing module
"""

import time

NAME: str = "test_module"
INITIAL_PROMPT = "{base_prompt}>"
ENABLE_PROMPT = "{base_prompt}#"
DEVICE_NAME: str = "TestModule"


# pylint: disable=unused-argument
class TestModule:
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
