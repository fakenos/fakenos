"""
NOS base class
"""


class Nos:
    def __init__(self, commands=None, initial_prompt=None):
        """
        Method to instantiate Nos Instance

        :param commands: dictionary of commands
        """
        self.commands = commands or {}
        self.initial_prompt = initial_prompt or "noprompt"
