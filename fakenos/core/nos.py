"""
Network Operating Systems (NOS). Base class to build NOS plugins instances to use with FakeNOS.
"""

from datetime import datetime, timedelta
import logging
import random
from typing import Optional, List, Union
import importlib.util
# import os
from jinja2 import Template
from pydantic import BaseModel
import yaml

# from fakenos.core.pydantic_models import ModelNosAttributes

log = logging.getLogger(__name__)

available_platforms: List[str] = [
    "alcatel_aos",
    "alcatel_sros",
    "allied_telesis_awplus",
    "arista_eos",
    "aruba_os",
    "avaya_ers",
    "avaya_vsp",
    "broadcom_icos",
    # "brocade_fastiron",
    "brocade_netiron",
    "checkpoint_gaia",
    # "ciena_saos",
    "cisco_asa",
    "cisco_ftd",
    "cisco_ios",
    "cisco_nxos",
    "cisco_s300",
    "cisco_xr",
    "dell_force10",
    # "dell_powerconnect",
    "dlink_ds",
    "eltex",
    "ericsson_ipos",
    "extreme_exos",
    # "fortinet",
    "hp_comware",
    "hp_procurve",
    "huawei_smartax",
    "huawei_vrp",
    "ipinfusion_ocnos",
    "juniper_junos",
    # "juniper_screenos",
    "linux",
    # "mikrotik_routeros",
    # "paloalto_panos",
    # "ruckus_fastiron",
    "ubiquiti_edgerouter",
    "ubiquiti_edgeswitch",
    "vyatta_vyos",
    "yamaha",
    "zyxel_os",
]


class Nos:
    """
    Base class to build NOS plugins instances to use with FakeNOS.
    """

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        name: str = "FakeNOS",
        configuration_file: Optional[str] = None,
        platform: Optional[str] = None,
        nos_plugins: Optional[Union[str, List[str]]] = None,
    ) -> None:
        """
        Method to instantiate Nos Instance

        :param name: NOS plugin name
        :param configuration_file: file with the configurations
        :param platform: platform name
        """
        self.name = name
        self.configuration_file = configuration_file
        self.platform = platform
        self.nos_plugins = nos_plugins
        if platform:
            self._load_constants(platform)
            self.configurations = self._load_basic_configurations(platform)
        self.configurations.update(self.load_configurations(configuration_file))
        self.configurations["system_startup_time"] = datetime.now() \
            - timedelta(days=random.randint(1, 365),
                        hours=random.randint(1, 24),
                        minutes=random.randint(1, 60),
                        seconds=random.randint(1, 60))
        
        
    def _load_constants(self, platform: str) -> None:
        """
        Load the basic configurations under platforms.
        """
        module_path = f"fakenos.plugins.nos.platforms_py.platforms.{platform}"
        platform_module = importlib.import_module(module_path)
        for constant in dir(platform_module):
            if constant.isupper():
                setattr(self, constant, getattr(platform_module, constant))
        
    def _load_basic_configurations(self, platform: str) -> dict:
        """
        Load the basic configurations.
        """
        default_configurations_filename = getattr(self, "DEFAULT_CONFIGURATION", None)
        if not default_configurations_filename:
            return {}
        return self.load_configurations(default_configurations_filename)

    def load_configurations(self, configuration_file: str) -> dict:
        """
        Load configurations from a file.
        The file can be either a YAML file or a Jinja2 template.
        """
        if not configuration_file:
            return {}
        if not configuration_file.endswith((".yaml", ".j2")):
            raise ValueError("Configuration file must be a YAML file or a Jinja2 template.")
        # TODO: Partial Configurations
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