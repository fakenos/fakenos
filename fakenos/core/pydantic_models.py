"""
File to contain pydantic models for plugins input/output data validation
"""
from pydantic import (
    BaseModel,
    StrictBool,
    StrictInt,
    StrictFloat,
    StrictStr,
    conlist,
    IPvAnyAddress,
    conint,
    root_validator,
)
from typing import Union, Optional, List, Any, Dict, Callable, Tuple

try:
    from typing import Literal  # works with >=py3.8
except ImportError:
    from typing_extensions import Literal  # works with <py3.8

# ---------------------------------------------------------------------------------------
# NOS plugin commands model
# ---------------------------------------------------------------------------------------

class model_nos_command(BaseModel):
    output: Optional[Union[StrictStr, None, Callable]]
    help: Optional[StrictStr]
    prompt: Optional[Union[StrictStr, List[StrictStr]]]
    new_prompt: Optional[StrictStr]
    alias: Optional[StrictStr]
        
class model_nos_attributes(BaseModel):
    commands: Dict[StrictStr, model_nos_command]
    name: StrictStr
    initial_prompt: StrictStr
        
# ---------------------------------------------------------------------------------------
# FakeNOS inventory data model components
# ---------------------------------------------------------------------------------------

class NosPluginConfig(BaseModel):
    commands: Optional[Dict[StrictStr, model_nos_command]]
        
class NosPlugin(BaseModel):
    plugin: StrictStr
    configuration: Optional[NosPluginConfig]

class ParamikoSshServerConfig(BaseModel):
    ssh_key_file: Optional[StrictStr] = None
    ssh_key_file_password: Optional[StrictStr] = None
    ssh_banner: Optional[StrictStr] = "FakeNOS Paramiko SSH Server"
    timeout: Optional[StrictInt] = 1
    address: Optional[Union[Literal["localhost"], IPvAnyAddress]]
    watchdog_interval: Optional[StrictInt] = 1


class ParamikoSshServerPlugin(BaseModel):
    plugin: Literal["ParamikoSshServer"]
    configuration: Optional[ParamikoSshServerConfig]


class CMDShellConfig(BaseModel):
    intro: Optional[StrictStr] = "Custom SSH Shell"
    ruler: Optional[StrictStr] = ""
    completekey: Optional[StrictStr] = "tab"
    newline: Optional[StrictStr] = "\r\n"


class CMDShellPlugin(BaseModel):
    plugin: Literal["CMDShell"]
    configuration: Optional[CMDShellConfig]


class InventoryDefaultSection(BaseModel):
    username: Optional[StrictStr]
    password: Optional[StrictStr]
    # port: Optional[Union[conint(strict=True, gt=0, le=65535), conlist(conint(strict=True, gt=0, le=65535), min_items=2, max_items=2, unique_items=True)]]
    # use this for now, mkdocstring having issue with pydantic - https://github.com/mkdocstrings/griffe/issues/66
    port: Optional[Union[StrictInt, List[StrictInt]]]
    server: Optional[Union[ParamikoSshServerPlugin]]
    shell: Optional[Union[CMDShellPlugin]]
    nos: Optional[NosPlugin]


class HostConfig(InventoryDefaultSection):
    # count: Optional[conint(strict=True, gt=0)]
    # use this for now, mkdocstring having issue with pydantic - https://github.com/mkdocstrings/griffe/issues/66
    count: Optional[StrictInt]
        
    @root_validator(pre=True)
    def check_port_value(cls, values):
        port = values.get("port")
        if "count" not in values and port:
            assert isinstance(
                port, int
            ), "If no host 'count' given, port must be an integer"
        elif "count" in values and port:
            assert isinstance(port, list), "If host 'count' given, port must be a list"
        return values


class model_fakenos_inventory(BaseModel):
    """FakeNOS inventory data schema"""

    default: Optional[InventoryDefaultSection]
    hosts: Dict[StrictStr, HostConfig]

    class Config:
        extra = "forbid"


