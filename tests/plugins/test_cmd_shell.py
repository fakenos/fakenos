"""
Module to test the cmd_shell plugin.
"""

import os
import shutil
import threading
import time
from typing import List
from unittest import TestCase
from unittest.mock import Mock, patch
import importlib

from netmiko import ConnectHandler
import yaml

from fakenos.core.fakenos import FakeNOS, fakenos
from fakenos.core.nos import Nos
from fakenos.plugins.shell.cmd_shell import CMDShell


# pylint: disable=too-many-public-methods
class TestCmdShell(TestCase):
    """Test the CmdShell class."""

    def setUp(self):
        """Setup the test."""
        self.arguments = {
            "stdin": None,
            "stdout": None,
            "nos": Nos(filename="tests/assets/yaml_nos.yaml"),
            "nos_inventory_config": {},
            "base_prompt": "test",
            "is_running": threading.Event(),
        }

    def test_init(self):
        """Test the init method."""
        shell = CMDShell(**self.arguments)
        self.assertEqual(shell.intro, "Custom SSH Shell")
        self.assertEqual(shell.ruler, "")
        self.assertEqual(shell.completekey, "tab")
        self.assertEqual(shell.newline, "\r\n")
        self.assertEqual(shell.prompt, "test>")
        self.assertEqual(shell.is_running, self.arguments["is_running"])
        self.assertNotEqual(shell.commands, {})
        self.assertEqual(shell.nos, self.arguments["nos"])
        self.assertEqual(shell.base_prompt, self.arguments["base_prompt"])

    def test_init_with_intro(self):
        """Test the init method with intro."""
        shell = CMDShell(**self.arguments, intro="Test Intro")
        self.assertEqual(shell.intro, "Test Intro")
        self.assertEqual(shell.ruler, "")
        self.assertEqual(shell.completekey, "tab")
        self.assertEqual(shell.newline, "\r\n")
        self.assertEqual(shell.prompt, "test>")
        self.assertEqual(shell.is_running, self.arguments["is_running"])
        self.assertNotEqual(shell.commands, {})
        self.assertEqual(shell.nos, self.arguments["nos"])
        self.assertEqual(shell.base_prompt, self.arguments["base_prompt"])

    def test_init_with_ruler(self):
        """Test the init method with ruler."""
        shell = CMDShell(**self.arguments, ruler="Test Ruler")
        self.assertEqual(shell.intro, "Custom SSH Shell")
        self.assertEqual(shell.ruler, "Test Ruler")
        self.assertEqual(shell.completekey, "tab")
        self.assertEqual(shell.newline, "\r\n")
        self.assertEqual(shell.prompt, "test>")
        self.assertEqual(shell.is_running, self.arguments["is_running"])
        self.assertNotEqual(shell.commands, {})
        self.assertEqual(shell.nos, self.arguments["nos"])
        self.assertEqual(shell.base_prompt, self.arguments["base_prompt"])

    def test_init_with_completekey(self):
        """Test the init method with completekey."""
        shell = CMDShell(**self.arguments, completekey="Test Completekey")
        self.assertEqual(shell.intro, "Custom SSH Shell")
        self.assertEqual(shell.ruler, "")
        self.assertEqual(shell.completekey, "Test Completekey")
        self.assertEqual(shell.newline, "\r\n")
        self.assertEqual(shell.prompt, "test>")
        self.assertEqual(shell.is_running, self.arguments["is_running"])
        self.assertNotEqual(shell.commands, {})
        self.assertEqual(shell.nos, self.arguments["nos"])
        self.assertEqual(shell.base_prompt, self.arguments["base_prompt"])

    def test_init_with_newline(self):
        """Test the init method with newline."""
        shell = CMDShell(**self.arguments, newline="Test Newline")
        self.assertEqual(shell.intro, "Custom SSH Shell")
        self.assertEqual(shell.ruler, "")
        self.assertEqual(shell.completekey, "tab")
        self.assertEqual(shell.newline, "Test Newline")
        self.assertEqual(shell.prompt, "test>")
        self.assertEqual(shell.is_running, self.arguments["is_running"])
        self.assertNotEqual(shell.commands, {})
        self.assertEqual(shell.nos, self.arguments["nos"])
        self.assertEqual(shell.base_prompt, self.arguments["base_prompt"])

    def test_init_all_args(self):
        """Test the init method with all args."""
        shell = CMDShell(
            **self.arguments,
            intro="Test Intro",
            ruler="Test Ruler",
            completekey="Test Completekey",
            newline="Test Newline",
        )
        self.assertEqual(shell.intro, "Test Intro")
        self.assertEqual(shell.ruler, "Test Ruler")
        self.assertEqual(shell.completekey, "Test Completekey")
        self.assertEqual(shell.newline, "Test Newline")
        self.assertEqual(shell.prompt, "test>")
        self.assertEqual(shell.is_running, self.arguments["is_running"])
        self.assertNotEqual(shell.commands, {})
        self.assertEqual(shell.nos, self.arguments["nos"])
        self.assertEqual(shell.base_prompt, self.arguments["base_prompt"])

    def test_init_error_if_nos_not_provided(self):
        """Test the init method raises an error if nos is not provided."""
        with self.assertRaises(TypeError):
            # pylint: disable=no-value-for-parameter
            CMDShell()

    def test_init_error_if_nos_inventory_config_not_provided(self):
        """Test the init method raises an error if nos_inventory_config is not provided."""
        with self.assertRaises(TypeError):
            # pylint: disable=no-value-for-parameter
            CMDShell(nos=Nos(filename="tests/assets/yaml_nos.yaml"))

    def test_init_error_if_base_prompt_not_provided(self):
        """Test the init method raises an error if base_prompt is not provided."""
        with self.assertRaises(TypeError):
            # pylint: disable=no-value-for-parameter
            CMDShell(nos=Nos(filename="tests/assets/yaml_nos.yaml"), nos_inventory_config={})

    def test_init_error_if_is_running_not_provided(self):
        """Test the init method raises an error if is_running is not provided."""
        with self.assertRaises(TypeError):
            # pylint: disable=no-value-for-parameter
            CMDShell(
                nos=Nos(filename="tests/assets/yaml_nos.yaml"),
                nos_inventory_config={},
                base_prompt="test",
            )

    def test_start(self):
        """Test that the start method calls cmdloop."""
        shell = CMDShell(**self.arguments)
        mock_cmdloop = Mock()
        shell.cmdloop = mock_cmdloop
        shell.start()
        mock_cmdloop.assert_called_once()

    def test_stop(self):
        """Test that the stop method writes "exit" to stdin."""
        shell = CMDShell(**self.arguments)
        shell.stdin = Mock()
        shell.stop()
        shell.stdin.write.assert_called_once_with("exit\r\n")

    def test_writeline(self):
        """Test that the writeline method writes a line to stdout with a newline at the end."""
        shell = CMDShell(**self.arguments)
        shell.stdout = Mock()
        shell.writeline("test")
        shell.stdout.write.assert_called_once_with("test\r\n")

    def test_emptyline(self):
        """Test that the emptyline method does nothing."""
        shell = CMDShell(**self.arguments)
        shell.emptyline()

    def test_precmd(self):
        """Test that the precmd method returns the line."""
        shell = CMDShell(**self.arguments)
        self.assertEqual(shell.precmd("test"), "test")

    def test_postcmd(self):
        """Test that the postcmd method returns the stop and line."""
        shell = CMDShell(**self.arguments)
        self.assertEqual(shell.postcmd(False, "test"), False)

    def test_postcmd_with_stop(self):
        """Test that the postcmd method returns the stop and line."""
        shell = CMDShell(**self.arguments)
        self.assertEqual(shell.postcmd(True, "test"), True)

    def test_postcmd_with_stop_and_line(self):
        """Test that the postcmd method returns the stop and line."""
        shell = CMDShell(**self.arguments)
        self.assertEqual(shell.postcmd(True, "exit"), True)

    def test_postcmd_with_line(self):
        """Test that the postcmd method returns the stop and line."""
        shell = CMDShell(**self.arguments)
        self.assertEqual(shell.postcmd(False, "exit"), False)

    def test_postcmd_with_no_line(self):
        """Test that the postcmd method returns the stop and line."""
        shell = CMDShell(**self.arguments)
        self.assertEqual(shell.postcmd(False, ""), False)

    def test_do_help(self):
        """Test that the do_help method writes the help message to stdout."""
        shell = CMDShell(**self.arguments)
        shell.writeline = Mock()
        shell.do_help("")
        expected_output: List[str] = [
            "exit                Exit commands shell",
            "enable              enter exec prompt",
            "sh clock            ",
            "show clock          Display the system clock",
            "terminal width 511  Set terminal width to 511",
            "terminal length 0   Set terminal length to 0",
        ]
        shell.writeline.assert_called_once_with("\r\n".join(expected_output))

    def test__check_prompt_is_none(self):
        """Test that the _check_prompt method returns the prompt."""
        shell = CMDShell(**self.arguments)
        # pylint: disable=protected-access
        self.assertTrue(shell._check_prompt(None))

    def test__check_prompt_is_string(self):
        """Test that the _check_prompt method returns the prompt."""
        shell = CMDShell(**self.arguments)
        # pylint: disable=protected-access
        self.assertTrue(shell._check_prompt("{base_prompt}>"))

    def test__check_prompt_is_list(self):
        """Test that the _check_prompt method returns the prompt."""
        shell = CMDShell(**self.arguments)
        # pylint: disable=protected-access
        self.assertTrue(shell._check_prompt(["{base_prompt}>"]))

    def test__check_prompt_is_not_prompt(self):
        """Test that the _check_prompt method returns False."""
        shell = CMDShell(**self.arguments)
        # pylint: disable=protected-access
        self.assertFalse(shell._check_prompt("{base_prompt}"))

    def test_default_command_correct(self):
        """Test that the default method does nothing."""
        self.arguments["is_running"].set()
        shell = CMDShell(**self.arguments)
        shell.writeline = Mock()
        shell.default("show clock")
        shell.writeline.assert_called_once_with("*21:01:33.000 AET 01 01 01 2022")

    def test_default_command_with_alias(self):
        """Test that the default method does nothing."""
        self.arguments["is_running"].set()
        shell = CMDShell(**self.arguments)
        shell.writeline = Mock()
        shell.default("sh clock")
        shell.writeline.assert_called_once_with("*21:01:33.000 AET 01 01 01 2022")

    def test_default_command_is_function(self):
        """Test that the default method does nothing."""
        self.arguments["is_running"].set()
        self.arguments["nos"] = Nos(filename="tests/assets/module.py")
        shell = CMDShell(**self.arguments)
        shell.writeline = Mock()
        shell.default("show clock")
        shell.writeline.assert_called_once_with(time.ctime())

    def test_default_command_not_matching_prompt(self):
        """Test that the default method does nothing."""
        self.arguments["is_running"].set()
        shell = CMDShell(**self.arguments)
        shell.writeline = Mock()
        shell.default("show version")
        shell.writeline.assert_called_once_with("% Invalid input detected at '^' marker.")

    def test_default_command_incorrect(self):
        """Test that the default method does nothing."""
        self.arguments["is_running"].set()
        shell = CMDShell(**self.arguments)
        shell.writeline = Mock()
        shell.default("test")
        shell.writeline.assert_called_once_with("% Invalid input detected at '^' marker.")

    def test_default_command_new_prompt(self):
        """Test that the default method does nothing."""
        self.arguments["is_running"].set()
        shell = CMDShell(**self.arguments)
        shell.writeline = Mock()
        shell.default("enable")
        shell.prompt = "test#"

    def test_default_command_exit(self):
        """Test that the default method does nothing."""
        self.arguments["is_running"].set()
        shell = CMDShell(**self.arguments)
        self.assertTrue(shell.default("exit"))


class HotReloadTest(TestCase):
    """
    Test class for the hot reload feature
    """

    def setUp(self):
        self.arguments = {
            "stdin": None,
            "stdout": None,
            "nos": Nos(filename="tests/assets/yaml_nos.yaml"),
            "nos_inventory_config": {},
            "base_prompt": "test",
            "is_running": threading.Event(),
        }
        os.environ["FAKENOS_RELOAD_COMMANDS"] = "ON"

    def tearDown(self):
        if "FAKENOS_RELOAD_COMMANDS" in os.environ:
            os.environ.pop("FAKENOS_RELOAD_COMMANDS")

    def test_hot_reload_not_activated_doesnt_enter(self):
        """Test that the if is not set  hot_reload method does nothing."""
        os.environ.pop("FAKENOS_RELOAD_COMMANDS")
        mock_get_files_changed = Mock()
        shell = CMDShell(**self.arguments)
        shell.get_files_changed = mock_get_files_changed
        shell.precmd("show clock")
        mock_get_files_changed.assert_not_called()

    @patch("fakenos.plugins.shell.cmd_shell.get_files_changed")
    def test_hot_reload_activated_does_enter(self, mock_get_files_changed):
        """Test that if there are no changed files, nothing happens."""
        mock_get_files_changed.return_value = []
        shell = CMDShell(**self.arguments)
        shell.precmd("show clock")
        mock_get_files_changed.assert_called_once()

    @patch("fakenos.core.nos.Nos.from_file")
    @patch("fakenos.plugins.shell.cmd_shell.get_files_changed")
    def test_hot_reload_activated_update_commands(self, mock_get_files_changed, mock_from_file):
        """
        Test that if there are change files,
        the nos_from_file is called
        and the commands are updated correctly.
        """
        changed_module = "fakenos.plugins.nos.platforms_py.cisco_ios"
        mock_get_files_changed.return_value = [changed_module.replace(".", "/") + ".py"]
        shell = CMDShell(**self.arguments)
        shell.precmd("show clock")
        module = importlib.import_module(changed_module)
        mock_from_file.assert_called_once()
        mock_from_file.assert_called_once_with(module.__name__.replace(".", "/") + ".py")
        assert all(key in shell.commands for key in module.commands.keys())

    @fakenos(platform="cisco_ios", return_instance=True)
    def test_hot_reload_integration_yaml(self, net: FakeNOS):
        """
        Test that the hot reload feature works correctly
        """
        original_filename = "fakenos/plugins/nos/platforms_yaml/cisco_ios.yaml"
        copy_filename = "fakenos/plugins/nos/platforms_yaml/copy_ios.yaml"
        test_commands = {
            "test": {
                "output": "test output",
                "help": "test help",
                "prompt": ["{base_prompt}>"],
            }
        }

        def change_file():
            shutil.copyfile(original_filename, copy_filename)
            with open(original_filename, "r", encoding="utf-8") as file:
                values = yaml.safe_load(file)
            values["commands"].update(test_commands)
            with open(original_filename, "w", encoding="utf-8") as file:
                file.write(yaml.dump(values))

        def undo_change_file():
            os.remove(original_filename)
            shutil.move(copy_filename, original_filename)

        device = list(net.hosts.values())
        credentials = {
            "host": "localhost",
            "username": device[0].username,
            "password": device[0].password,
            "port": device[0].port,
            "device_type": "cisco_ios",
        }
        with ConnectHandler(**credentials) as conn:
            output = conn.send_command("test")
            assert output == "% Invalid input detected at '^' marker."
            change_file()
            output = conn.send_command("test")
            undo_change_file()
            assert output == "test output"

    @fakenos(platform="cisco_ios", return_instance=True)
    def test_hot_reload_integration_py_jinja(self, net: FakeNOS):
        """
        Test that the hot reload feature works correctly
        """
        original_filename = "fakenos/plugins/nos/platforms_py/templates/cisco_ios/show_version.j2"
        copy_filename = "fakenos/plugins/nos/platforms_py/templates/cisco_ios/copy_show_version.j2"

        def change_file():
            shutil.copyfile(original_filename, copy_filename)
            with open(original_filename, "w", encoding="utf-8") as file:
                file.write("test output")

        def undo_change_file():
            os.remove(original_filename)
            shutil.move(copy_filename, original_filename)

        device = list(net.hosts.values())
        credentials = {
            "host": "localhost",
            "username": device[0].username,
            "password": device[0].password,
            "port": device[0].port,
            "device_type": "cisco_ios",
        }
        with ConnectHandler(**credentials) as conn:
            conn.enable()
            output = conn.send_command("show version")
            assert output != "test output"
            change_file()
            output = conn.send_command("show version")
            undo_change_file()
            assert output == "test output"
