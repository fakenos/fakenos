"""
NOS module for Huawei SmartAX
"""
import os
from typing import Dict

DEVICE_NAME: str = "HuaweiSmartAX"

GPON_BOARDS: Dict[str, int] = {
    'H901XGHDE': 8,
    'H901OGHK': 24,
    'H901NXED': 8,
    'H901OXHD': 8,
    'H902OXHD': 8,
    'H901GPSFE': 16,
    'H901OXEG': 24,
    'H901TWEDE': 8,
    'H901XSHF': 16,
    'H902GPHFE': 16,
}

NAME: str = "huawei_smartax"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CONFIGURATION: str = os.path.join(os.path.dirname(BASE_DIR), "configurations/huawei_smartax.yaml.j2")
PYDANTIC_FILE: str = os.path.join(os.path.dirname(BASE_DIR), "configurations/pydantic_models/huawei_smartax.py")

CLI_FILE: str = os.path.join(os.path.dirname(BASE_DIR), "cli/huawei_smartax/huawei_smartax.py")
