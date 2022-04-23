import yaml
import importlib.util
import logging

from fakenos.core.pydantic_models import model_nos_attributes

log = logging.getLogger(__name__)


class Nos:
    """
    Base class to build NOS plugins instances to use with FakeNOS.
    """

    def __init__(
        self, name: str = None, commands: dict = None, initial_prompt: str = None
    ) -> None:
        """
        Method to instantiate Nos Instance

        :param name: NOS plugin name
        :param commands: dictionary of NOS commands
        :param initial_prompt: NOS initial prompt
        """
        self.name = name or "noname"
        self.commands = commands or {}
        self.initial_prompt = initial_prompt or "noprompt"
        
        # make sure to validate NOS attributes if Nos class instantiated with them
        if commands or name or initial_prompt:
            self.validate()
        
    def validate(self) -> None:
        """
        Method to validate NOS attributes: commands, name, initial prompt - using 
        Pydantic models, raises ValidationError on failure.
        """
        _ = model_nos_attributes(
            name=self.name,
            initial_prompt=self.initial_prompt,
            commands=self.commands,
        )
        log.debug(f"{self.name} NOS attributes validation succeeded")
        
    def from_dict(self, data: dict) -> None:
        """
        Method to build NOS from dictionary data.

        Sample NOS dictionary::

            nos_plugin_dict = {
                "name": "MyFakeNOSPlugin",
                "initial_prompt": "{base_prompt}>",
                "commands": {
                    "terminal width 511": {"output": "", "help": "Set terminal width to 511"},
                    "terminal length 0": {"output": "", "help": "Set terminal length to 0"},
                    "show clock": {"output": "MyFakeNOSPlugin system time is 00:00:00"},
                },
            }

        :param data: NOS dictionary
        """
        self.name = data.get("name", self.name)
        self.commands = data.get("commands", self.commands)
        self.initial_prompt = data.get("initial_prompt", self.initial_prompt)
        self.validate()
        
    def from_yaml(self, data: str) -> None:
        """
        Method to build NOS from YAML data.

        Sample NOS YAML file content::

            name: "MyFakeNOSPlugin"
            initial_prompt: "{base_prompt}>"
            commands:
              terminal width 511: {"output": "", "help": "Set terminal width to 511"}
              terminal length 0: {"output": "", "help": "Set terminal length to 0"}
              show clock: {"output": "MyFakeNOSPlugin system time is 00:00:00"}

        :param data: YAML structured text
        """
        self.from_dict(yaml.safe_load(data))
        self.validate()
        
    def from_module(self, data: str) -> None:
        """
        Method to import NOS data from python file.

        Sample Python NOS plugin file::

            name = "MyFakeNOSPlugin"

            initial_prompt = "{base_prompt}>"

            commands = {
                "terminal width 511": {"output": "", "help": "Set terminal width to 511"},
                "terminal length 0": {"output": "", "help": "Set terminal length to 0"},
                "show clock": {"output": "MyFakeNOSPlugin system time is 00:00:00"},
            }

        :param data: OS path string to Python .py file
        """
        # load .py file using this recipe
        # https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
        spec = importlib.util.spec_from_file_location("nos_module", data)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # source attributes from loaded .py module
        self.name = getattr(module, "name", self.name)
        self.commands = getattr(module, "commands", self.commands)
        self.initial_prompt = getattr(module, "initial_prompt", self.initial_prompt)
        self.validate()
        
    def from_file(self, data: str) -> None:
        """
        Method to load NOS from YAML or Python file

        :param data: OS path string to `.yaml/.yml` or `.py` file with NOS data
        """
        if data.endswith(".yaml") or data.endswith(".yml"):
            with open(data, "r", encoding="utf-8") as f:
                self.from_yaml(f.read())
        elif data.endswith(".py"):
            self.from_module(data)
        else:
            raise ValueError(
                f"Unsupported '{data}' file extension, supported .py, .yml, .yaml"
            )
