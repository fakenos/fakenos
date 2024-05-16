"""
This module is the point of entry for all NOS plugins.
It imports all the NOS plugins and loads them into a dictionary.

The NOS plugins are loaded first, using the .py modules and
then the .yaml files in the platforms directory for those which are left.

With .py modules we can have functionality, while using YAML is only
intended for quick development of new NOS plugins.
"""

import glob
import os
from typing import Set

from fakenos.core.nos import Nos

nos_plugins: Set = {}

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)

# load NOS from YAML files
platforms_directory_yaml = os.path.join(current_directory, "platforms_yaml")
yaml_files = glob.glob(os.path.join(platforms_directory_yaml, "*.yaml"))
for file in yaml_files:
    nos_instance = Nos()
    nos_instance.from_file(file)
    nos_plugins[nos_instance.name] = nos_instance

# load NOS from python modules updating the NOS
platforms_directory_py: str = os.path.join(current_directory, "platforms_py")
py_files = glob.glob(os.path.join(platforms_directory_py, "*.py"))
py_files = [file for file in py_files if not file.endswith("__init__.py")]
for file in py_files:
    nos_instance = Nos()
    nos_instance.from_file(file)
    if nos_instance.name not in nos_plugins:
        nos_plugins[nos_instance.name] = nos_instance
    else:
        nos_plugins[nos_instance.name].commands.update(nos_instance.commands)
