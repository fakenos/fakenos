"""
Base template for all the templates
in the CLI.
"""

from jinja2 import Environment, PackageLoader, select_autoescape

from fakenos.core.nos import Nos
import os


class NosCLI:
    """ Class for the CLI. """
    def __init__(self, nos: Nos) -> None:
        self.nos: Nos = nos
        self.platform: str = nos.platform
        self.env = None
        if self.platform:
            self.env = Environment(
                loader=PackageLoader(f"fakenos.plugins.nos.platforms_py.cli.{self.platform}", "templates"),
                autoescape=select_autoescape(["j2"]),
                trim_blocks=False, lstrip_blocks=False
            )
        file_path = os.path.abspath(__file__)
        for files in os.listdir(os.path.dirname(f'{file_path}/{self.platform}')):
            self.
        

    def render(self, template: str, **kwargs) -> str:
        """Render a template."""
        if not self.env:
            raise ValueError("No platform set.")
        template = self.env.get_template(template)
        return template.render(**kwargs)


        # if isinstance(filename, str):
        #     self.from_file(filename)
        # elif isinstance(filename, list):
        #     for file in filename:
        #         self.from_file(file)
        # elif dict_args:
        #     self.from_dict(dict_args)

    # def validate(self) -> None:
    #     """
    #     Method to validate NOS attributes: commands, name,
    #     initial prompt - using Pydantic models,
    #     raises ValidationError on failure.
    #     """
    #     ModelNosAttributes(**self.__dict__)
    #     log.debug("%s NOS attributes validation succeeded", self.name)

    # def from_dict(self, data: dict) -> None:
    #     """
    #     Method to build NOS from dictionary data.

    #     Sample NOS dictionary::

    #         nos_plugin_dict = {
    #             "name": "MyFakeNOSPlugin",
    #             "initial_prompt": "{base_prompt}>",
    #             "commands": {
    #                 "terminal width 511": {
    #                     "output": "",
    #                     "help": "Set terminal width to 511",
    #                     "prompt": "{base_prompt}>",
    #                 },
    #                 "terminal length 0": {
    #                     "output": "",
    #                     "help": "Set terminal length to 0",
    #                     "prompt": "{base_prompt}>",
    #                 },
    #                 "show clock": {
    #                     "output": "MyFakeNOSPlugin system time is 00:00:00",
    #                     "help": "Show system time",
    #                     "prompt": "{base_prompt}>",
    #                 },
    #             },
    #         }

    #     :param data: NOS dictionary
    #     """
    #     self.name = data.get("name", self.name)
    #     self.commands.update(data.get("commands", self.commands))
    #     self.initial_prompt = data.get("initial_prompt", self.initial_prompt)

    # def _from_yaml(self, data: str) -> None:
    #     """
    #     Method to build NOS from YAML data.

    #     Sample NOS YAML file content::

    #         name: "MyFakeNOSPlugin"
    #         initial_prompt: "{base_prompt}>"
    #         commands:
    #             terminal width 511: {
    #                 "output": "",
    #                 "help": "Set terminal width to 511",
    #                 "prompt": "{base_prompt}>",
    #             }
    #             terminal length 0: {
    #                 "output": "",
    #                 "help": "Set terminal length to 0",
    #                 "prompt": "{base_prompt}>",
    #             }
    #             show clock: {
    #                 "output": "MyFakeNOSPlugin system time is 00:00:00",
    #                 "help": "Show system time",
    #                 "prompt": "{base_prompt}>",
    #             }

    #     :param data: YAML structured text
    #     """
    #     with open(data, "r", encoding="utf-8") as f:
    #         self.from_dict(yaml.safe_load(f))

    # def _from_module(self, filename: str) -> None:
    #     """
    #     Method to import NOS data from python file or python module.

    #     Loads from the .py file using the recipe:
    #     https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly

    #     Sample Python NOS plugin file::

    #         name = "MyFakeNOSPlugin"

    #         INITIAL_PROMPT = "{base_prompt}>"

    #         commands = {
    #             "terminal width 511": {
    #                 "output": "",
    #                 "help": "Set terminal width to 511",
    #                 "prompt": "{base_prompt}>",
    #             },
    #             "terminal length 0": {
    #                 "output": "",
    #                 "help": "Set terminal length to 0",
    #                 "prompt": "{base_prompt}>",
    #             },
    #             "show clock": {
    #                 "output": "MyFakeNOSPlugin system time is 00:00:00",
    #                 "help": "Show system time",
    #                 "prompt": "{base_prompt}>",
    #             },
    #         }

    #     :param data: OS path string to Python .py file
    #     """
    #     spec = importlib.util.spec_from_file_location("module.name", filename)
    #     module = importlib.util.module_from_spec(spec)
    #     spec.loader.exec_module(module)
    #     self.commands.update(getattr(module, "commands", self.commands))
    #     self.name = getattr(module, "NAME", self.name)
    #     classname = getattr(module, "DEVICE_NAME", None)
    #     configuration_file = getattr(module, "DEFAULT_CONFIGURATION", self.configuration_file)
    #     self.device = getattr(module, classname)(configuration_file=configuration_file)

    # def from_file(self, filename: str) -> None:
    #     """
    #     Method to load NOS from YAML or Python file

    #     :param data: OS path string to `.yaml/.yml` or `.py` file with NOS data
    #     """
    #     if not self.is_file_ending_correct(filename):
    #         raise ValueError(
    #             f'Unsupported "{filename}" file extension.\
    #                           Supported: .py, .yml, .yaml'
    #         )
    #     if not os.path.isfile(filename):
    #         raise FileNotFoundError(filename)
    #     if filename.endswith((".yaml", ".yml")):
    #         self._from_yaml(filename)
    #     elif filename.endswith(".py"):
    #         self._from_module(filename)

    # def is_file_ending_correct(self, filename: str) -> None:
    #     """
    #     Method to check if file extension is correct and load NOS data.
    #     Correct types are: .yaml, .yml and .py
    #     """
    #     return filename.endswith((".yaml", ".yml", ".py"))
