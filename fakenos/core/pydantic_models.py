"""
File to contain pydantic models for plugins input/output data validation
"""
import sys

from typing import Union, Optional, List, Dict, Callable

from pydantic import (
    BaseModel,
    StrictInt,
    StrictStr,
    IPvAnyAddress,
    root_validator,
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
    output: Optional[Union[StrictStr, None, Callable]]
    help: Optional[StrictStr]
    prompt: Optional[Union[StrictStr, List[StrictStr]]]
    new_prompt: Optional[StrictStr]
    alias: Optional[StrictStr]


class ModelNosAttributes(BaseModel):
    """
    Pydantic model for NOS attributes.
    """
    commands: Dict[StrictStr, ModelNosCommand]
    name: StrictStr
    initial_prompt: StrictStr


# ---------------------------------------------------------------------------------------
# FakeNOS inventory data model components
# ---------------------------------------------------------------------------------------


class NosPluginConfig(BaseModel):
    """
    Pydantic model for NOS plugin configuration.
    """
    commands: Optional[Dict[StrictStr, ModelNosCommand]]


class NosPlugin(BaseModel):
    """
    Pydantic model for NOS plugin.
    """
    plugin: StrictStr
    configuration: Optional[NosPluginConfig]


class ParamikoSshServerConfig(BaseModel):
    """
    Pydantic model for Paramiko SSH server configuration.
    """
    ssh_key_file: Optional[StrictStr] = None
    ssh_key_file_password: Optional[StrictStr] = None
    ssh_banner: Optional[StrictStr] = "FakeNOS Paramiko SSH Server"
    timeout: Optional[StrictInt] = 1
    address: Optional[Union[Literal["localhost"], IPvAnyAddress]]
    watchdog_interval: Optional[StrictInt] = 1


class ParamikoSshServerPlugin(BaseModel):
    """
    Pydantic model for Paramiko SSH server plugin.
    """
    plugin: Literal["ParamikoSshServer"]
    configuration: Optional[ParamikoSshServerConfig]


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
    configuration: Optional[CMDShellConfig]


class InventoryDefaultSection(BaseModel):
    """
    Pydantic model for FakeNOS inventory default section.
    """
    username: Optional[StrictStr]
    password: Optional[StrictStr]
    # port: Optional[Union[conint(strict=True, gt=0, le=65535), conlist(conint(strict=True, gt=0, le=65535), min_items=2, max_items=2, unique_items=True)]]
    # use this for now, mkdocstring having issue with pydantic - https://github.com/mkdocstrings/griffe/issues/66
    port: Optional[Union[StrictInt, List[StrictInt]]]
    server: Optional[Union[ParamikoSshServerPlugin]]
    shell: Optional[Union[CMDShellPlugin]]
    nos: Optional[NosPlugin]


class HostConfig(InventoryDefaultSection):
    """
    Pydantic model for FakeNOS inventory host configuration.
    """
    # count: Optional[conint(strict=True, gt=0)]
    # use this for now, mkdocstring having issue with pydantic - https://github.com/mkdocstrings/griffe/issues/66
    count: Optional[StrictInt]

    @root_validator(pre=True)
    def check_port_value(cls, values):
        """
        Method to validate port value based on 'count' value.
        """
        port = values.get("port")
        if "count" not in values and port:
            assert isinstance(port, int), "If no host 'count' given, port must be an integer"
        elif "count" in values and port:
            assert isinstance(port, list), "If host 'count' given, port must be a list"
        return values


class ModelFakenosInventory(BaseModel):
    """FakeNOS inventory data schema"""
    default: Optional[InventoryDefaultSection]
    hosts: Dict[StrictStr, HostConfig]

    class Config:
        """Pydantic model configuration"""
        extra = "forbid"



