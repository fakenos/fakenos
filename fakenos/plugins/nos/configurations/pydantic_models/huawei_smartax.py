""" Pydantic models for Huawei SmartAX configurations."""
from __future__ import annotations
from typing import Optional, List, Literal

from pydantic import Field, BaseModel

PYDANTIC_MODEL: str = "HuaweiSmartAX"


class DBAProfile(BaseModel):
    """ Pydantic model for DBA Profile attributes."""
    additional_bandwidth: str = Optional[Literal['best-effort', 'fix']]
    assure_kbps: int = Field(gte=0)
    bandwidth_compensation: Optional[str] = Literal['No', 'Yes']
    best_effort_priority: int = Field(gte=0)
    best_effort_weight: int = Field(gte=0)
    bind_times: int = Field(gte=0)
    fix_delay: str = Optional[Literal['No', 'Yes']]
    fix_kbps: int = Field(gte=0)
    max_kbps: int = Field(gte=0)
    profile_id: int = Field(gte=0)
    profile_name: str = Field(min_length=1)
    type: int = Field(gt=0, lte=5)


class Frame(BaseModel):
    """ Frame model for Huawei SmartAX attributes."""
    frame_id: int
    slots: List[Slot]

class Slot(BaseModel):
    """ Slot model for Huawei SmartAX attributes."""
    boardname: str = Field(None, max_length=9)
    online_offline: Optional[str] = Literal['Online', 'Offline']
    slotid: int = Field(gte=0)
    subtype0: Optional[str] = Field(None, max_length=4)
    subtype1: Optional[str] = Field(None, max_length=4)
    ports: Optional[List[List[Port]]] = None

class Port(BaseModel):
    """ Port model for Huawei SmartAX attributes."""
    onts: Optional[List[ONT]] = None

class ONT(BaseModel):
    """ ONT model for Huawei SmartAX attributes."""
    checkcode: str = Field(min_length=12, max_length=12)
    config_state: Optional[str] = Literal['normal']
    control_flag: str = Literal['active']
    customized_info: str = Field(default='')
    description: str
    equipment_id: str
    equipment_sn: str
    extended_model: str
    hardware_version: str
    is_epon: bool = Field(default=False)
    loid: str
    mac: str
    match_state: str = Literal['mismatch', 'initial']
    model: str
    multi_channel: str = Literal['Not support']
    nni_type: str =  Literal['auto']
    online_offline: str = Literal['online', 'offline']
    ont_id: int
    oui_version: str
    password: str
    protect_side: str = Literal['yes', 'no']
    registered: bool = Field(default=False)
    run_state: Literal['online', 'offline']
    sn: str = Field(max_length=16, min_length=16)
    software_version: str
    vendor_id: str
    version: str

class Service(BaseModel):
    """ Service model for Huawei SmartAX attributes."""
    port: Optional[int] = Field(gte=0, lte=65535)
    service_name: str
    state: Optional[str] = Literal["enable, disable"]

class HuaweiSmartAX(BaseModel):
    """ Pydantic model for Huawei SmartAX attributes."""
    dba_profiles: List[DBAProfile]
    frames: List[Frame]
    services: List[Service]
    