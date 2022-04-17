from . import cisco_ios
from .dict_builder import dict_builder
from .yaml_builder import yaml_builder

nos_builders = {"dict_builder": dict_builder, "yaml_builder": yaml_builder}
nos_plugins = {"cisco_ios": cisco_ios}
