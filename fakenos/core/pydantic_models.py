"""
File to contain pydantic models for plugins input/output data validation
"""

from __future__ import annotations

import sys
from typing import Callable, Dict, List, Optional, Union

from pydantic import (
    BaseModel,
    IPvAnyAddress,
    model_validator,
    StrictBool,
    StrictInt,
    StrictStr,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # works with >=py3.8
else:
    from typing_extensions import Literal  # works with <py3.8I

# ---------------------------------------------------------------------------------------
# NOS plugin commands model
# ---------------------------------------------------------------------------------------


class ModelNosCommand(BaseModel):
    """
    Pydantic model for NOS command attributes.
    """

    output: Optional[Union[StrictStr, None, Callable, StrictBool]] = None
    help: Optional[StrictStr] = None
    prompt: Optional[Union[StrictStr, List[StrictStr]]] = None
    new_prompt: Optional[StrictStr] = None
    alias: Optional[StrictStr] = None


class ModelNosAttributes(BaseModel):
    """
    Pydantic model for NOS attributes.
    """

    commands: Dict[StrictStr, ModelNosCommand]
    name: StrictStr
    initial_prompt: StrictStr


class ModelHost(BaseModel):
    """
    Pydantic model for Host Attributes
    """

    name: StrictStr
    username: StrictStr
    password: StrictStr
    port: StrictInt
    platform: Optional[StrictStr] = None


# ---------------------------------------------------------------------------------------
# FakeNOS inventory data model components
# ---------------------------------------------------------------------------------------


class NosPluginConfig(BaseModel):
    """
    Pydantic model for NOS plugin configuration.
    """

    commands: Optional[Dict[StrictStr, ModelNosCommand]] = None


class NosPlugin(BaseModel):
    """
    Pydantic model for NOS plugin.
    """

    plugin: StrictStr
    configuration: Optional[NosPluginConfig] = None


class ParamikoSshServerConfig(BaseModel):
    """
    Pydantic model for Paramiko SSH server configuration.
    """

    ssh_key_file: Optional[StrictStr] = None
    ssh_key_file_password: Optional[StrictStr] = None
    ssh_banner: Optional[StrictStr] = "FakeNOS Paramiko SSH Server"
    timeout: Optional[StrictInt] = 1
    address: Optional[Union[Literal["localhost"], IPvAnyAddress]] = None
    watchdog_interval: Optional[StrictInt] = 1


class ParamikoSshServerPlugin(BaseModel):
    """
    Pydantic model for Paramiko SSH server plugin.
    """

    plugin: Literal["ParamikoSshServer"]
    configuration: Optional[ParamikoSshServerConfig] = None


class CMDShellConfig(BaseModel):
    """
    Pydantic model for CMD shell configuration.
    """

    intro: Optional[StrictStr] = "Custom SSH Shell"
    ruler: Optional[StrictStr] = ""
    completekey: Optional[StrictStr] = "tab"
    newline: Optional[StrictStr] = "\r\n"


class CMDShellPlugin(BaseModel):
    """
    Pydantic model for CMD shell plugin.
    """

    plugin: Literal["CMDShell"]
    configuration: Optional[CMDShellConfig] = None


class InventoryDefaultSection(BaseModel):
    """
    Pydantic model for FakeNOS inventory default section.
    """

    username: Optional[StrictStr] = None
    password: Optional[StrictStr] = None
    # port: Optional[Union[conint(strict=True, gt=0, le=65535),
    # conlist(conint(strict=True, gt=0, le=65535),
    # min_items=2, max_items=2, unique_items=True)]]
    # use this for now, mkdocstring having issue with pydantic
    # https://github.com/mkdocstrings/griffe/issues/66
    port: Optional[Union[StrictInt, List[StrictInt]]] = None
    configuration_file: Optional[StrictStr] = None
    server: Optional[Union[ParamikoSshServerPlugin]] = None
    shell: Optional[Union[CMDShellPlugin]] = None
    nos: Optional[NosPlugin] = None


class HostConfig(InventoryDefaultSection):
    """
    Pydantic model for FakeNOS inventory host configuration.
    """

    # count: Optional[conint(strict=True, gt=0)]
    # use this for now, mkdocstring having issue with pydantic
    # https://github.com/mkdocstrings/griffe/issues/66
    replicas: Optional[StrictInt] = None

    @model_validator(mode="before")
    @classmethod
    def check_port_value(cls, values):
        """
        Method to validate port value based on 'replicas' value.
        """
        port = values.get("port")
        if "replicas" not in values and port:
            if not isinstance(port, int):
                raise ValueError("If no host 'replicas' given, port must be an integer")
        elif "replicas" in values and port:
            if not isinstance(port, list):
                raise ValueError("If host 'replicas' given, port must be a list")
        return values


class ModelFakenosInventory(BaseModel):
    """FakeNOS inventory data schema"""

    default: Optional[InventoryDefaultSection] = None
    hosts: Dict[StrictStr, HostConfig]

    # pylint: disable=too-few-public-methods
    class ConfigDict:
        """Pydantic model configuration"""

        extra = "forbid"
