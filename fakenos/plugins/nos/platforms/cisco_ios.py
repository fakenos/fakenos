"""
NOS module for Cisco IOS
"""

import os

NAME: str = "cisco_ios"
INITIAL_PROMPT: str = "{base_prompt}>"
ENABLE_PROMPT: str = "{base_prompt}#"
CONFIG_PROMPT: str = "{base_prompt}(config)#"
DEVICE_NAME: str = "CiscoIOS"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CONFIGURATION = os.path.join(BASE_DIR, "configurations/cisco_ios.yaml.j2")
