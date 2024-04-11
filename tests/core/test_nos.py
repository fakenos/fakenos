import unittest

from pydantic import ValidationError
import pytest
import yaml

from fakenos.core.nos import Nos as NOS


class NosTest(unittest.TestCase):
    commands: dict = {}

    @classmethod
    def setup_class(cls):
        """
        Setup class for NosTest.
        """
        with open("tests/assets/yaml_nos_1.yaml", "r") as yml_file:
            cls.commands = yaml.safe_load(yml_file)["commands"]

    def test_init_without_arguments(self):
        """
        Test that the init method works when no arguments are provided.
        """
        nos = NOS()
        assert nos.name == "FakeNOS"
        assert nos.initial_prompt == "FakeNOS>"
        assert nos.commands == {}

    def test_init_with_arguments(self):
        """
        Test that the init method works when arguments are provided.
        """
        print(self.commands)
        nos = NOS(name="MyFakeNOS", initial_prompt="MyFakeNOS>", commands=self.commands)
        assert nos.name == "MyFakeNOS"
        assert nos.initial_prompt == "MyFakeNOS>"
        assert nos.commands == self.commands

    def test_init_with_argument_name(self):
        """
        Test that the init method works when the name argument is provided.
        """
        nos = NOS(name="MyFakeNOS")
        assert nos.name == "MyFakeNOS"
        assert nos.initial_prompt == "FakeNOS>"
        assert nos.commands == {}

    def test_init_with_argument_initial_prompt(self):
        """
        Test that the init method works when
        the initial_prompt argument is provided.
        """
        nos = NOS(initial_prompt="MyFakeNOS>")
        assert nos.name == "FakeNOS"
        assert nos.initial_prompt == "MyFakeNOS>"
        assert nos.commands == {}

    def test_init_with_argument_commands(self):
        """
        Test that the init method works when the commands argument is provided.
        """
        nos = NOS(commands=self.commands)
        assert nos.name == "FakeNOS"
        assert nos.initial_prompt == "FakeNOS>"
        assert nos.commands == self.commands

    def test_validate(self):
        """
        Test that the validate raises a ValidationError
        when the NOS attributes are invalid.
        """
        with pytest.raises(ValidationError):
            nos = NOS(commands="invalid_commands")
            nos.validate()

    def test_from_dict_correct(self):
        """
        Test that the from_dict method works when the data is correct.
        """
        nos = NOS()
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
            NOS({"name": 123, "initial_prompt": "MyFakeNOS>", "commands": self.commands})

    def test_from_dict_incorrect_initial_prompt(self):
        """
        Test that the from_dict method raises a
        ValidationError when the initial_prompt is incorrect.
        """
        with pytest.raises(ValidationError):
            NOS({"name": "MyFakeNOS", "initial_prompt": 123, "commands": self.commands})

    def test_from_dict_incorrect_commands(self):
        """
        Test that the from_dict method raises a
        ValidationError when the commands are incorrect.
        """
        with pytest.raises(ValidationError):
            NOS({"name": "MyFakeNOS", "initial_prompt": "MyFakeNOS>", "commands": "invalid_commands"})

    def test_from_dict_only_name(self):
        """
        Test that the from_dict method works when only the name is provided.
        """
        nos = NOS()
        nos.from_dict({"name": "MyFakeNOS"})
        assert nos.name == "MyFakeNOS"
        assert nos.initial_prompt == "FakeNOS>"
        assert nos.commands == {}

    def test_from_dict_only_initial_prompt(self):
        """
        Test that the from_dict method works
        when only the initial_prompt is provided.
        """
        nos = NOS()
        nos.from_dict({"initial_prompt": "MyFakeNOS>"})
        assert nos.name == "FakeNOS"
        assert nos.initial_prompt == "MyFakeNOS>"
        assert nos.commands == {}

    def test_from_dict_only_commands(self):
        """
        Test that the from_dict method works
        when only the commands are provided.
        """
        nos = NOS()
        nos.from_dict({"commands": self.commands})
        assert nos.name == "FakeNOS"
        assert nos.initial_prompt == "FakeNOS>"
        assert nos.commands == self.commands

    def test_from_dict_no_data(self):
        """
        Test that the from_dict method works when no data is provided.
        """
        nos = NOS()
        nos.from_dict({})
        assert nos.name == "FakeNOS"
        assert nos.initial_prompt == "FakeNOS>"
        assert nos.commands == {}

    def test_from_file(self):
        """
        Test that the from_file method works.
        """
        nos = NOS()
        nos.from_file("tests/assets/yaml_nos_1.yaml")
        assert nos.name == "Custom Nos 0.1.0"
        assert nos.initial_prompt == "{base_prompt}>"
        assert nos.commands == self.commands

    def test_from_file_incorrect_file(self):
        """
        Test that the from_file method raises a
        FileNotFoundError when the file is incorrect.
        """
        with pytest.raises(FileNotFoundError):
            nos = NOS()
            nos.from_file("tests/assets/incorrect_file.yaml")

    def test_from_module(self):
        """
        Test that the from_module method works.
        """
        import tests.assets.module_nos_1

        nos = NOS()
        nos.from_module("tests/assets/module_nos_1.py")
        assert nos.name == "FakeNOS"
        assert nos.initial_prompt == "{base_prompt}>"
        assert nos.commands == tests.assets.module_nos_1.commands

    def test_from_module_incorrect_file(self):
        """
        Test that the from_module method raises a
        FileNotFoundError when the file is incorrect.
        """
        with pytest.raises(FileNotFoundError):
            nos = NOS()
            nos.from_module("tests/assets/incorrect_file.py")
