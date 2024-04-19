import glob
import os

from fakenos.core.nos import Nos

from . import cisco_ios
from . import arista_eos


nos_plugins = {"cisco_ios": cisco_ios, "arista_eos": arista_eos}

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
platforms_directory = os.path.join(current_directory, 'platforms')
yaml_files = glob.glob(os.path.join(platforms_directory, '*.yaml'))

for file in yaml_files:
    nos_instance = Nos()
    nos_instance.from_file(file)
    nos_plugins[nos_instance.name] = nos_instance


