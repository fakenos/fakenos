"""
This module is intended to be used as a template
for creating new module devices for FakeNOS.
It has certain atributes and methods which are
generally common to all devices.
"""

from abc import ABC

from jinja2 import Environment, PackageLoader, select_autoescape
import yaml


class BaseDevice(ABC):
    """ Interface for all devices."""
    
    def __init__(self, configuration_file: str) -> None:
        self.configurations = self.load_configurations(configuration_file)
        self.env = Environment(
            loader=PackageLoader("fakenos.plugins.nos.platforms_py", "templates"),
            autoescape=select_autoescape(["j2"]),
        )

    def load_configurations(self, configuration_file: str) -> dict:
        """Load configurations from a file."""
        if configuration_file.endswith(".j2"):
            config_env = Environment(
                loader=PackageLoader("fakenos.plugins.nos.platforms_py", "configurations"),
                autoescape=select_autoescape(["j2"]),
            )
            template = config_env.get_template(configuration_file)
            data_j2 = template.render()
            data = yaml.safe_load(data_j2)
            return data
        
        with open(configuration_file, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
        return data
    
    def render(self, template: str, **kwargs) -> str:
        """Render a template."""
        template = self.env.get_template(template)
        return template.render(**kwargs)
