"""
NOS base class
"""
import yaml
import importlib.util


class Nos:
    """
    Base class to build NOS plugins instances to use with FakeNOS.
    """
    def __init__(self, name:str=None, commands:dict=None, initial_prompt:str=None):
        """
        Method to instantiate Nos Instance

        :param name: NOS name
        :param commands: dictionary of NOS commands
        :param initial_prompt: NOS initial prompt
        """
        self.name = name or "noname"
        self.commands = commands or {}
        self.initial_prompt = initial_prompt or "noprompt"
        
        
    def from_dict(self, data):
        """
        Method to build NOS from dictionary data.
        
        :param data: NOS dictionary
        """
        self.name = data.get("name", self.name)
        self.commands = data.get("commands", self.commands)
        self.initial_prompt = data.get("initial_prompt", self.initial_prompt)
        
        
    def from_yaml(self, data):
        """
        Method to build NOS from YAML data.
        
        :param data: YAML structured text
        """
        self.from_dict(yaml.safe_load(data))
        
        
    def from_module(self, data):
        """
        Method to import NOS data from python file.
        
        :param data: OSP path string to Python .py file
        """
        # load .py file using this recipe
        # https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
        spec = importlib.util.spec_from_file_location("nos_module", data)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # source attributes from loaded .py module
        self.name = getattr(module, "name", self.name)
        self.commands = getattr(module, "commands", self.commands)
        self.initial_prompt = getattr(module, "initial_prompt", self.initial_prompt)
        
        
    def from_file(self, data):
        """
        Method to load NOS from YAML or Python file
        
        :param data: OS path to .yml, .yaml or .py file wit NOS data
        """
        if data.endswith(".yaml") or data.endswith(".yml"):
            with open(data, "r", encoding="utf-8") as f:
                self.from_yaml(f.read())
        elif data.endswith(".py"):
            self.from_module(data)
        else:
            raise ValueError(f"Unsupported '{data}' file extension, supported .py, .yml, .yaml")
            
            
        
