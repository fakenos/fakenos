import time

name = "foobar_py"

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