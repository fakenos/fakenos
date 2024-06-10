"""
This module is intended to be used as a template
for creating new module devices for FakeNOS.
It has certain atributes and methods which are
generally common to all devices.
"""

from abc import ABC
import importlib

from jinja2 import Template
from pydantic import BaseModel
import yaml


class BaseDevice(ABC):
    """Interface for all devices."""

    def __init__(self, configuration_file: str) -> None:
        self.configuration_file = configuration_file
        self.configurations = self.load_configurations(configuration_file)
        self._verify_configurations()

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
            return self._load_jinja2_configuration(configuration_file)
        return self._load_yaml_configuration(configuration_file)
    
    def _load_jinja2_configuration(self, configuration_file: str) -> dict:
        """Load configurations from a Jinja2 template."""
        data: str = ""
        with open(configuration_file, "r", encoding="utf-8") as file:
            data = file.read()
        data_j2 = Template(data, autoescape=False, trim_blocks=True, lstrip_blocks=True).render()
        data = yaml.safe_load(data_j2)
        return data

    def _load_yaml_configuration(self, configuration_file: str) -> dict:
        """Load configurations from a YAML file."""
        with open(configuration_file, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
        return data

    def _verify_configurations(self) -> None:
        """Verify configurations."""
        filename: str = getattr(self, "PYDANTIC_FILE", None)
        if not filename:
            return
        spec = importlib.util.spec_from_file_location("module.name", filename)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        pydantic_model: str = getattr(module, "PYDANTIC_MODEL", None)
        pydantic_class: BaseModel = getattr(module, pydantic_model)
        pydantic_class.model_validate(self.configurations)
