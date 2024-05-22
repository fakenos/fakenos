"""
Test the platforms that are supported by FakeNOS.
Currently, it checks if the platforms are correctly set
in the yaml and python files.
"""

import re
import os
from importlib import import_module
import types
from typing import Any, List

from netmiko import ConnectHandler
import pytest
import yaml

from fakenos.core.fakenos import FakeNOS
from fakenos.core.nos import available_platforms
from tests.utils import get_free_port, get_host_commands


def get_py_nos_modules() -> List[str]:
    """
    It returns the list of all the python files
    that are in the nos directory.
    """
    return [
        f.split(".py", 1)[0]
        for f in os.listdir("fakenos/plugins/nos/platforms_py")
        if f.endswith(".py") and f != "__init__.py" and f != "base_template.py"
    ]


def has_single_curly_brackets(text: Any, exceptions: List[str]) -> bool:
    """
    It returns False if the single curly
    brackets are in the text.
    The strategy is to check if the text has
    the curly brackets and if so it checks that
    those are double, otherwise returns True.
    """
    pattern = r"\{\{[^\{\}]*\}\}"
    if not text or isinstance(text, bool) or callable(text):
        return False
    if isinstance(text, str):
        text = [text]
    for t in text:
        if "{" not in t or "}" not in t or any(e in t for e in exceptions):
            continue
        matches = re.search(pattern, t)
        if not matches:
            return True
    return False


class TestPlatforms:
    """
    This class tests all the platforms that are supported by FakeNOS
    and checks if they are correctly set
    """

    @pytest.mark.parametrize("platform", available_platforms)
    def test_platforms_yaml_has_correct_format(self, platform: str):
        """
        It checks if the platform yaml file can be opened correctly using
        the yaml library.
        """
        with open(f"fakenos/plugins/nos/platforms_yaml/{platform}.yaml", "r", encoding="utf-8") as file:
            data: dict = yaml.safe_load(file)
            for key in data.keys():
                assert key in ["name", "initial_prompt", "enable_prompt", "config_prompt", "commands"]

    @pytest.mark.parametrize("platform", available_platforms)
    def test_platforms_yaml_commands_has_correct_format(self, platform: str):
        """
        It checks if the platform has the commands correctly set.
        At least all the commands need to have the following with any conflict:
        - output
        - help
        - prompt
        """
        with open(f"fakenos/plugins/nos/platforms_yaml/{platform}.yaml", "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
            exceptions: List[str] = [data["initial_prompt"]]
            if "enable_prompt" in data:
                exceptions.append(data["enable_prompt"])
            if "config_prompt" in data:
                exceptions.append(data["config_prompt"])
            for _, values in data["commands"].items():
                assert "output" in values
                assert has_single_curly_brackets(values["output"], exceptions) is False
                assert "help" in values
                assert has_single_curly_brackets(values["help"], exceptions) is False
                assert "prompt" in values
                assert has_single_curly_brackets(values["prompt"], exceptions) is False

    @pytest.mark.parametrize("platform", get_py_nos_modules())
    def test_platforms_py_has_correct_format(self, platform: str):
        """
        It checks if the platform python file can be imported correctly.
        """
        try:
            module = import_module(f"fakenos.plugins.nos.platforms_py.{platform}")
        except ImportError:
            pytest.fail(f"Failed to import platform module for {platform}")

        assert module.__name__ == f"fakenos.plugins.nos.platforms_py.{platform}"
        assert hasattr(module, "commands")
        assert hasattr(module, "INITIAL_PROMPT")
        assert hasattr(module, "DEVICE_NAME")
        assert hasattr(module, module.DEVICE_NAME)

    @pytest.mark.parametrize("platform", get_py_nos_modules())
    def test_platforms_py_commands_has_correct_format(self, platform: str):
        """
        It checks if the platform has the commands correctly set.
        At least all the commands need to have the following with any conflict:
        - output
        - help
        - prompt
        """
        try:
            module = import_module(f"fakenos.plugins.nos.platforms_py.{platform}")
        except ImportError:
            pytest.fail(f"Failed to import platform module for {platform}")

        module_class = getattr(module, module.DEVICE_NAME)

        for value in module.commands.values():
            if "alias" in value:
                continue
            exceptions: List[str] = [module.INITIAL_PROMPT]
            if hasattr(module, "ENABLE_PROMPT"):
                exceptions.append(module.ENABLE_PROMPT)
            if hasattr(module, "CONFIG_PROMPT"):
                exceptions.append(module.CONFIG_PROMPT)
            assert "output" in value
            if callable(value["output"]):
                assert isinstance(value["output"], types.FunctionType)
                assert value["output"].__name__ in dir(module_class)
            else:
                assert has_single_curly_brackets(value["output"], exceptions) is False
            assert "help" in value
            assert has_single_curly_brackets(value["help"], exceptions) is False
            assert "prompt" in value

    @pytest.mark.parametrize("platform", get_py_nos_modules())
    def test_platforms_py_all_commands_are_running(self, platform: str):
        """
        Test that all the platforms commands can
        run without any error.
        """
        free_port: int = get_free_port()
        credentials: dict = {
            "host": "localhost",
            "username": "test_user",
            "password": "test_password",
            "port": free_port,
            "device_type": platform,
        }
        inventory: dict = {
            "hosts": {
                "test_device": {
                    "username": credentials["username"],
                    "password": credentials["password"],
                    "port": credentials["port"],
                    "platform": platform,
                }
            }
        }
        initial_commands, enable_commands, config_commands = [], [], []
        initial_commands: List[str] = []
        enable_commands: List[str] = []
        config_commands: List[str] = []
        with FakeNOS(inventory=inventory) as net:
            host = list(net.hosts.values())[0]
            initial_commands, enable_commands, config_commands = get_host_commands(host)
            with ConnectHandler(**credentials) as conn:
                for command in initial_commands:
                    output = conn.send_command(command)
                    assert output or output == ""
                if enable_commands:
                    conn.enable()
                    for command in enable_commands:
                        output = conn.send_command(command)
                        assert output or output == ""
                if config_commands:
                    conn.config_mode()
                    for command in config_commands:
                        output = conn.send_command(command)
                        assert output or output == ""
