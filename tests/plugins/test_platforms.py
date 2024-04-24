import re
import os
from importlib import import_module

import pytest
import yaml

from fakenos.core.nos import available_platforms


def get_py_nos_modules() -> list[str]:
    """
    It returns the list of all the python files
    that are in the nos directory.
    """
    return [f.split(".py", 1)[0] for f in os.listdir("fakenos/plugins/nos") if f.endswith(".py") and f != "__init__.py"]


def has_single_curly_brackets(text) -> bool:
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
        if "{" not in t or "}" not in t:
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
        with open(f"fakenos/plugins/nos/platforms/{platform}.yaml", "r") as file:
            data: dict = yaml.safe_load(file)
            for key in data.keys():
                assert key in ["name", "initial_prompt", "commands"]

    @pytest.mark.parametrize("platform", available_platforms)
    def test_platforms_yaml_commands_has_correct_format(self, platform: str):
        """
        It checks if the platform has the commands correctly set.
        At least all the commands need to have the following with any conflict:
        - output
        - help
        - prompt
        """
        with open(f"fakenos/plugins/nos/platforms/{platform}.yaml", "r") as file:
            data = yaml.safe_load(file)
            for _, values in data["commands"].items():
                assert "output" in values
                assert has_single_curly_brackets(values["output"]) is False
                assert "help" in values
                assert has_single_curly_brackets(values["help"]) is False
                assert "prompt" in values
                assert has_single_curly_brackets(values["prompt"]) is False

    @pytest.mark.parametrize("platform", get_py_nos_modules())
    def test_platforms_py_has_correct_format(self, platform: str):
        """
        It checks if the platform python file can be imported correctly.
        """
        try:
            module = import_module(f"fakenos.plugins.nos.{platform}")
        except ImportError:
            pytest.fail(f"Failed to import platform module for {platform}")

        assert module.__name__ == f"fakenos.plugins.nos.{platform}"
        assert hasattr(module, "commands")
        assert hasattr(module, "initial_prompt")

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
            module = import_module(f"fakenos.plugins.nos.{platform}")
        except ImportError:
            pytest.fail(f"Failed to import platform module for {platform}")

        for _, values in module.commands.items():
            if "alias" in values:
                continue
            assert "output" in values
            assert has_single_curly_brackets(values["output"]) is False
            assert "help" in values
            assert has_single_curly_brackets(values["help"]) is False
            assert "prompt" in values
