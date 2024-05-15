"""
This is a testing module
"""

import time

INITIAL_PROMPT = "{base_prompt}>"


# pylint: disable=unused-argument
def show_clock(**kwargs) -> str:
    """Show the current time."""
    return str(time.ctime())


commands = {
    "enable": {
        "output": None,
        "new_prompt": "{base_prompt}#",
        "help": "enter exec prompt",
        "prompt": INITIAL_PROMPT,
    },
    "show clock": {
        "output": show_clock,
        "help": "show current time",
        "prompt": ["{base_prompt}#", "{base_prompt}>"],
    },
}
