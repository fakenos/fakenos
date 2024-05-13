"""
Test module for fakenos.core.nos module.
This module can be found at fakenos/core/nos.py
"""

import unittest

from pydantic import ValidationError
import pytest
import yaml

from fakenos.core.nos import Nos
from tests.assets import module


# pylint: disable=too-many-public-methods
class NosTest(unittest.TestCase):
    """
    Test class for Nos.
    """

    commands: dict = {}

    @classmethod
    def setup_class(cls):
        """
        Setup class for NosTest.
        """
        with open("tests/assets/yaml_nos.yaml", "r", encoding="utf-8") as yml_file:
            cls.commands = yaml.safe_load(yml_file)["commands"]

    def test_init_without_arguments(self):
        """
        Test that the init method works when no arguments are provided.
        """
        nos = Nos()
        assert nos.name == "FakeNOS"
        assert nos.initial_prompt == "FakeNOS>"
        assert nos.commands == {}

    def test_init_with_arguments(self):
        """
        Test that the init method works when arguments are provided.
        """
        nos = Nos(name="MyFakeNOS", initial_prompt="MyFakeNOS>", commands=self.commands)
        assert nos.name == "MyFakeNOS"
        assert nos.initial_prompt == "MyFakeNOS>"
        assert nos.commands == self.commands

    def test_init_with_argument_name(self):
        """
        Test that the init method works when the name argument is provided.
        """
        nos = Nos(name="MyFakeNOS")
        assert nos.name == "MyFakeNOS"
        assert nos.initial_prompt == "FakeNOS>"
        assert nos.commands == {}

    def test_init_with_argument_initial_prompt(self):
        """
        Test that the init method works when
        the initial_prompt argument is provided.
        """
        nos = Nos(initial_prompt="MyFakeNOS>")
        assert nos.name == "FakeNOS"
        assert nos.initial_prompt == "MyFakeNOS>"
        assert nos.commands == {}

    def test_init_with_argument_commands(self):
        """
        Test that the init method works when the commands argument is provided.
        """
        nos = Nos(commands=self.commands)
        assert nos.name == "FakeNOS"
        assert nos.initial_prompt == "FakeNOS>"
        assert nos.commands == self.commands

    def test_validate(self):
        """
        Test that the validate raises a ValidationError
        when the NOS attributes are invalid.
        """
        with pytest.raises(ValidationError):
            nos = Nos(commands="invalid_commands")
            nos.validate()

    def test_from_dict_correct(self):
        """
        Test that the from_dict method works when the data is correct.
        """
        nos = Nos()
        nos.from_dict({"name": "MyFakeNOS", "initial_prompt": "MyFakeNOS>", "commands": self.commands})
        assert nos.name == "MyFakeNOS"
        assert nos.initial_prompt == "MyFakeNOS>"
        assert nos.commands == self.commands

    def test_from_dict_incorrect_name(self):
        """
        Test that the from_dict method raises a
        ValidationError when the name is incorrect.
        """
        with pytest.raises(ValidationError):
            Nos({"name": 123, "initial_prompt": "MyFakeNOS>", "commands": self.commands})

    def test_from_dict_incorrect_initial_prompt(self):
        """
        Test that the from_dict method raises a
        ValidationError when the initial_prompt is incorrect.
        """
        with pytest.raises(ValidationError):
            Nos({"name": "MyFakeNOS", "initial_prompt": 123, "commands": self.commands})

    def test_from_dict_incorrect_commands(self):
        """
        Test that the from_dict method raises a
        ValidationError when the commands are incorrect.
        """
        with pytest.raises(ValidationError):
            Nos({"name": "MyFakeNOS", "initial_prompt": "MyFakeNOS>", "commands": "invalid_commands"})

    def test_from_dict_only_name(self):
        """
        Test that the from_dict method works when only the name is provided.
        """
        nos = Nos()
        nos.from_dict({"name": "MyFakeNOS"})
        assert nos.name == "MyFakeNOS"
        assert nos.initial_prompt == "FakeNOS>"
        assert nos.commands == {}

    def test_from_dict_only_initial_prompt(self):
        """
        Test that the from_dict method works
        when only the initial_prompt is provided.
        """
        nos = Nos()
        nos.from_dict({"initial_prompt": "MyFakeNOS>"})
        assert nos.name == "FakeNOS"
        assert nos.initial_prompt == "MyFakeNOS>"
        assert nos.commands == {}

    def test_from_dict_only_commands(self):
        """
        Test that the from_dict method works
        when only the commands are provided.
        """
        nos = Nos()
        nos.from_dict({"commands": self.commands})
        assert nos.name == "FakeNOS"
        assert nos.initial_prompt == "FakeNOS>"
        assert nos.commands == self.commands

    def test_from_dict_no_data(self):
        """
        Test that the from_dict method works when no data is provided.
        """
        nos = Nos()
        nos.from_dict({})
        assert nos.name == "FakeNOS"
        assert nos.initial_prompt == "FakeNOS>"
        assert nos.commands == {}

    def test_from_yaml_file(self):
        """
        Test that the from_file method works .yaml.
        """
        nos = Nos()
        nos.from_file("tests/assets/yaml_nos.yaml")
        assert nos.name == "Custom Nos 0.1.0"
        assert nos.initial_prompt == "{base_prompt}>"
        assert nos.commands == self.commands

    def test_from_file_incorrect_yaml_file(self):
        """
        Test that the from_file method raises a
        FileNotFoundError when the file is incorrect.
        """
        with pytest.raises(FileNotFoundError):
            nos = Nos()
            nos.from_file("tests/assets/incorrect_file.yaml")

    def test_from_py_file(self):
        """
        Test that the from_file method works with .py.
        """
        nos = Nos()
        nos.from_file("tests/assets/module.py")
        assert nos.name == "FakeNOS"
        assert nos.initial_prompt == "{base_prompt}>"
        self.assertTrue(all(item in nos.commands.items() for item in module.commands.items()))

    def test_from_file_incorrect_py_file(self):
        """
        Test that the from_file method raises a
        FileNotFoundError when the file is incorrect.
        """
        with pytest.raises(FileNotFoundError):
            nos = Nos()
            nos.from_file("tests/assets/incorrect_file.py")

    def test_from_module(self):
        """
        Test that the from_module method works.
        """
        nos = Nos()
        # pylint: disable=protected-access
        nos._from_module("tests/assets/module.py")
        assert nos.name == "FakeNOS"
        assert nos.initial_prompt == "{base_prompt}>"
        assert nos.commands == module.commands

    def test_from_module_incorrect_file(self):
        """
        Test that the from_module method raises a
        FileNotFoundError when the file is incorrect.
        """
        with pytest.raises(FileNotFoundError):
            nos = Nos()
            # pylint: disable=protected-access
            nos._from_module("tests/assets/incorrect_file.py")

    def test_register_nos_plugin_directly(self):
        """
        Test that we can register a nos model directly.
        """
        commands = {
            "terminal width 511": {"output": "", "help": "Set terminal width to 511"},
            "terminal length 0": {"output": "", "help": "Set terminal length to 0"},
            "show clock": {"output": "MyFakeNOSPlugin system time is 00:00:00"},
        }
        nos = Nos(
            name="MyFakeNOSPlugin",
            initial_prompt="{base_prompt}>",
            commands=commands,
        )

        assert nos.name == "MyFakeNOSPlugin"
        assert nos.initial_prompt == "{base_prompt}>"
        assert nos.commands == commands

    def test_register_nos_plugin_from_dict(self):
        """
        Test that we can register a nos model from a dict.
        """
        nos_dict = {
            "name": "MyFakeNOSPlugin",
            "initial_prompt": "{base_prompt}>",
            "commands": {
                "terminal width 511": {"output": "", "help": "Set terminal width to 511"},
                "terminal length 0": {"output": "", "help": "Set terminal length to 0"},
                "show clock": {"output": "MyFakeNOSPlugin system time is 00:00:00"},
            },
        }

        nos = Nos(**nos_dict)

        assert nos_dict["name"] == nos.name
        assert nos_dict["initial_prompt"] == nos.initial_prompt
        assert nos_dict["commands"] == nos.commands

    def test_register_nos_plugin_from_yaml_file(self):
        """
        Test that we can register a nos model from a yaml file.
        """
        nos = Nos(filename="tests/assets/yaml_nos.yaml")

        assert nos.name == "Custom Nos 0.1.0"
        assert nos.initial_prompt == "{base_prompt}>"
        assert nos.commands == self.commands

    def test_register_nos_plugin_incorrect_commands(self):
        """
        Test that we can register a nos model from a dict.
        """
        with pytest.raises(ValidationError):
            Nos(
                name="MyFakeNOSPlugin",
                initial_prompt="{base_prompt}>",
                commands={
                    "show clock": {"output": True},
                },
            )

    def test_register_nos_plugin_incorrect_name(self):
        """
        Test that we can register a nos model from a dict.
        """
        with pytest.raises(ValidationError):
            Nos(
                name=123,
                initial_prompt="{base_prompt}>",
                commands={
                    "show clock": {"output": ""},
                },
            )

    def test_register_nos_plugin_incorrect_output(self):
        """
        Test that we can register a nos model from a dict.
        """
        with pytest.raises(ValidationError):
            Nos(commands={"show clock": {"output": 42}})
