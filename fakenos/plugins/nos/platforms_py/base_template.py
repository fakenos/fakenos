"""
This module is intended to be used as a template
for creating new module devices for FakeNOS.
It has certain atributes and methods which are
generally common to all devices.
"""

from abc import ABC

from jinja2 import Environment, PackageLoader, Template, select_autoescape
import yaml


class BaseDevice(ABC):
    """Interface for all devices."""

    def __init__(self, configuration_file: str) -> None:
        self.configurations = self.load_configurations(configuration_file)
        self.env = Environment(
            loader=PackageLoader("fakenos.plugins.nos.platforms_py", "templates"),
            autoescape=select_autoescape(["j2"]),
        )

    def load_configurations(self, configuration_file: str) -> dict:
        """
        Load configurations from a file.
        The file can be either a YAML file or a Jinja2 template.
        """
        if not configuration_file:
            return {}
        if not configuration_file.endswith((".yaml", ".j2")):
            raise ValueError("Configuration file must be a YAML file or a Jinja2 template.")
        if configuration_file.endswith(".j2"):
            data: str = ""
            with open(configuration_file, "r", encoding="utf-8") as file:
                data = file.read()
            data_j2 = Template(data, autoescape=False, trim_blocks=True, lstrip_blocks=True).render()
            data = yaml.safe_load(data_j2)
            return data

        with open(configuration_file, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
        return data

    def render(self, template: str, **kwargs) -> str:
        """Render a template."""
        template = self.env.get_template(template)
        return template.render(**kwargs)
