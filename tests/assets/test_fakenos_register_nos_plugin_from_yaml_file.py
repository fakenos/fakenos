"""
This is a fake NOS plugin for testing purposes.
"""

NAME = "MyFakeNOSPlugin"

INITIAL_PROMPT = "{base_prompt}>"

commands = {
    "terminal width 511": {"output": "", "help": "Set terminal width to 511"},
    "terminal length 0": {"output": "", "help": "Set terminal length to 0"},
    "show clock": {"output": "MyFakeNOSPlugin system time is 00:00:00"},
}
