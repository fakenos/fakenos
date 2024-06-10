"""
NOS module for Arista EOS
"""

import os

NAME: str = "arista_eos"
INITIAL_PROMPT: str = "{base_prompt}>"
ENABLE_PROMPT: str = "{base_prompt}#"
CONFIG_PROMPT: str = "{base_prompt}(config)#"
DEVICE_NAME: str = "AristaEOS"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CONFIGURATION = os.path.join(BASE_DIR, "configurations/arista_eos.yaml.j2")
