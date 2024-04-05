import sys
import pprint
import time
import yaml
import pytest
from pydantic import ValidationError


from netmiko import ConnectHandler
from fakenos import FakeNOS
from fakenos import Nos

initial_prompt = "{base_prompt}>"


def make_show_clock(base_prompt, current_prompt, command):
    "Return String in format '*11:54:03.018 UTC Sat Apr 16 2022'"
    return time.strftime("*%H:%M:%S.000 %Z %a %b %d %Y")


running_configuration = """
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname {base_prompt}
!
boot-start-marker
boot-end-marker
"""

show_version = """
Version: 0.1.0
{base_prompt} uptime is 1 day, 17 hours, 32 minutes
Uptime for this control processor is 1 day, 17 hours, 33 minutes

Configuration register is 0x2102
"""

commands = {
    "enable": {
        "output": None,
        "new_prompt": "{base_prompt}#",
        "help": "enter exec prompt",
        "prompt": initial_prompt,
    },
    "show clock": {
        "output": make_show_clock,
        "help": "Display the system clock",
        "prompt": [initial_prompt, "{base_prompt}#"],
    },
    "show running-config": {
        "output": running_configuration,
        "help": "Current operating configuration",
        "prompt": "{base_prompt}#",
    },
    "show version": {
        "output": show_version,
        "help": "System hardware and software status",
        "prompt": "{base_prompt}#",
    },
    "_default_": {
        "output": "% Invalid input detected at '^' marker.",
        "help": "Output to print for unknown commands",
    },
    "terminal width 511": {"output": "", "help": "Set terminal width to 511"},
    "terminal length 0": {"output": "", "help": "Set terminal length to 0"},
}

with open("tests/integration_tests/assets/yaml_nos_1.yaml", "r", encoding="utf-8") as f:
    yaml_nos = f.read()


def test_build_nos_from_class():
    nos = Nos(commands=commands, initial_prompt=initial_prompt, name="foobar")
    assert nos.name == "foobar"
    assert nos.commands == commands
    assert nos.initial_prompt == initial_prompt


# test_build_nos_from_class()


def test_build_nos_from_dict():
    nos = Nos()
    nos.from_dict(
        {
            "commands": commands,
            "initial_prompt": initial_prompt,
        }
    )
    assert nos.commands == commands
    assert nos.initial_prompt == initial_prompt


# test_build_nos_from_dict()


def test_build_nos_from_yaml():
    nos = Nos()
    nos.from_yaml(yaml_nos)
    pprint.pprint(nos.commands)
    yaml_data = yaml.safe_load(yaml_nos)
    assert nos.commands == yaml_data["commands"]
    assert nos.initial_prompt == yaml_data["initial_prompt"]
    assert nos.name == yaml_data["name"]


# test_build_nos_from_yaml()


def test_build_nos_from_yaml_file():
    nos = Nos()
    nos.from_file("./assets/yaml_nos_1.yaml")
    pprint.pprint(nos.commands)
    yaml_data = yaml.safe_load(yaml_nos)
    assert nos.commands == yaml_data["commands"]
    assert nos.initial_prompt == yaml_data["initial_prompt"]
    assert nos.name == yaml_data["name"]


# test_build_nos_from_yaml_file()


def test_build_nos_from_py_file():
    nos = Nos()
    nos.from_file("./assets/yaml_nos_1.py")
    pprint.pprint(nos.commands)
    assert nos.name == "foobar_py"
    assert nos.initial_prompt == "{base_prompt}>"
    assert isinstance(nos.commands, dict)


# test_build_nos_from_py_file()


def test_fakenos_register_nos_plugin_class():
    fakerouter2 = {
        "device_type": "cisco_ios",
        "host": "127.0.0.1",
        "username": "user",
        "password": "user",
        "port": 6005,
    }
    nos = Nos(
        name="MyFakeNOSPlugin",
        initial_prompt="{base_prompt}>",
        commands={
            "terminal width 511": {"output": "", "help": "Set terminal width to 511"},
            "terminal length 0": {"output": "", "help": "Set terminal length to 0"},
            "show clock": {"output": "MyFakeNOSPlugin system time is 00:00:00"},
        },
    )
    inventory = {
        "hosts": {
            "router1": {"port": 6001, "nos": {"plugin": "cisco_ios"}},
            "router2": {
                "port": 6005,
                "nos": {"plugin": "MyFakeNOSPlugin"},
                "shell": {
                    "plugin": "CMDShell",
                    "configuration": {"intro": "MyFakeNOSPlugin Shell"},
                },
            },
        }
    }
    net = FakeNOS(inventory)
    net.register_nos_plugin(plugin=nos)
    net.start()

    after_start_hosts = net.list_hosts()

    device2 = ConnectHandler(**fakerouter2)
    output = device2.send_command("show clock")
    device2.disconnect()

    net.stop()

    pprint.pprint(after_start_hosts)
    pprint.pprint(output)

    assert "MyFakeNOSPlugin system time is 00:00:0" in output
    assert after_start_hosts == [
        {
            "address": "0.0.0.0",
            "base_prompt": "router1",
            "name": "router1",
            "nos": "cisco_ios",
            "port": 6001,
            "running": True,
            "server": "ParamikoSshServer",
            "shell": "CMDShell",
        },
        {
            "address": "0.0.0.0",
            "base_prompt": "router2",
            "name": "router2",
            "nos": "MyFakeNOSPlugin",
            "port": 6005,
            "running": True,
            "server": "ParamikoSshServer",
            "shell": "CMDShell",
        },
    ]


# test_fakenos_register_nos_plugin_class()


def test_fakenos_register_nos_plugin_from_dict():
    fakerouter2 = {
        "device_type": "cisco_ios",
        "host": "127.0.0.1",
        "username": "user",
        "password": "user",
        "port": 6005,
    }
    nos_plugin_dict = {
        "name": "MyFakeNOSPlugin",
        "initial_prompt": "{base_prompt}>",
        "commands": {
            "terminal width 511": {"output": "", "help": "Set terminal width to 511"},
            "terminal length 0": {"output": "", "help": "Set terminal length to 0"},
            "show clock": {"output": "MyFakeNOSPlugin system time is 00:00:00"},
        },
    }
    inventory = {
        "hosts": {
            "router1": {"port": 6001, "nos": {"plugin": "cisco_ios"}},
            "router2": {
                "port": 6005,
                "nos": {"plugin": "MyFakeNOSPlugin"},
                "shell": {
                    "plugin": "CMDShell",
                    "configuration": {"intro": "MyFakeNOSPlugin Shell"},
                },
            },
        }
    }
    net = FakeNOS(inventory)
    net.register_nos_plugin(plugin=nos_plugin_dict)
    net.start()

    after_start_hosts = net.list_hosts()

    device2 = ConnectHandler(**fakerouter2)
    output = device2.send_command("show clock")
    device2.disconnect()

    net.stop()

    pprint.pprint(after_start_hosts)
    pprint.pprint(output)

    assert "MyFakeNOSPlugin system time is 00:00:0" in output
    assert after_start_hosts == [
        {
            "address": "0.0.0.0",
            "base_prompt": "router1",
            "name": "router1",
            "nos": "cisco_ios",
            "port": 6001,
            "running": True,
            "server": "ParamikoSshServer",
            "shell": "CMDShell",
        },
        {
            "address": "0.0.0.0",
            "base_prompt": "router2",
            "name": "router2",
            "nos": "MyFakeNOSPlugin",
            "port": 6005,
            "running": True,
            "server": "ParamikoSshServer",
            "shell": "CMDShell",
        },
    ]


# test_fakenos_register_nos_plugin_from_dict()


def test_fakenos_register_nos_plugin_from_yaml_file():
    fakerouter2 = {
        "device_type": "cisco_ios",
        "host": "127.0.0.1",
        "username": "user",
        "password": "user",
        "port": 6005,
    }
    inventory = {
        "hosts": {
            "router1": {"port": 6001, "nos": {"plugin": "cisco_ios"}},
            "router2": {
                "port": 6005,
                "nos": {"plugin": "MyFakeNOSPlugin"},
                "shell": {
                    "plugin": "CMDShell",
                    "configuration": {"intro": "MyFakeNOSPlugin Shell"},
                },
            },
        }
    }
    net = FakeNOS(inventory)
    net.register_nos_plugin(
        plugin="./assets/test_fakenos_register_nos_plugin_from_yaml_file.yaml"
    )
    net.start()

    after_start_hosts = net.list_hosts()

    device2 = ConnectHandler(**fakerouter2)
    output = device2.send_command("show clock")
    device2.disconnect()

    net.stop()

    pprint.pprint(after_start_hosts)
    pprint.pprint(output)

    assert "MyFakeNOSPlugin system time is 00:00:0" in output
    assert after_start_hosts == [
        {
            "address": "0.0.0.0",
            "base_prompt": "router1",
            "name": "router1",
            "nos": "cisco_ios",
            "port": 6001,
            "running": True,
            "server": "ParamikoSshServer",
            "shell": "CMDShell",
        },
        {
            "address": "0.0.0.0",
            "base_prompt": "router2",
            "name": "router2",
            "nos": "MyFakeNOSPlugin",
            "port": 6005,
            "running": True,
            "server": "ParamikoSshServer",
            "shell": "CMDShell",
        },
    ]


# test_fakenos_register_nos_plugin_from_yaml_file()


def test_fakenos_register_nos_plugin_from_py_file():
    fakerouter2 = {
        "device_type": "cisco_ios",
        "host": "127.0.0.1",
        "username": "user",
        "password": "user",
        "port": 6005,
    }
    inventory = {
        "hosts": {
            "router1": {"port": 6001, "nos": {"plugin": "cisco_ios"}},
            "router2": {
                "port": 6005,
                "nos": {"plugin": "MyFakeNOSPlugin"},
                "shell": {
                    "plugin": "CMDShell",
                    "configuration": {"intro": "MyFakeNOSPlugin Shell"},
                },
            },
        }
    }
    net = FakeNOS(inventory)
    net.register_nos_plugin(
        plugin="./assets/test_fakenos_register_nos_plugin_from_yaml_file.py"
    )
    net.start()

    after_start_hosts = net.list_hosts()

    device2 = ConnectHandler(**fakerouter2)
    output = device2.send_command("show clock")
    device2.disconnect()

    net.stop()

    pprint.pprint(after_start_hosts)
    pprint.pprint(output)

    assert "MyFakeNOSPlugin system time is 00:00:0" in output
    assert after_start_hosts == [
        {
            "address": "0.0.0.0",
            "base_prompt": "router1",
            "name": "router1",
            "nos": "cisco_ios",
            "port": 6001,
            "running": True,
            "server": "ParamikoSshServer",
            "shell": "CMDShell",
        },
        {
            "address": "0.0.0.0",
            "base_prompt": "router2",
            "name": "router2",
            "nos": "MyFakeNOSPlugin",
            "port": 6005,
            "running": True,
            "server": "ParamikoSshServer",
            "shell": "CMDShell",
        },
    ]


# test_fakenos_register_nos_plugin_from_py_file()


def test_fakenos_register_nos_plugin_class_validation():
    with pytest.raises(ValidationError):
        nos = Nos(
            name="MyFakeNOSPlugin",
            initial_prompt="{base_prompt}>",
            commands={
                "show clock": {"output": True},
            },
        )
        
    with pytest.raises(ValidationError):
        nos = Nos(
            name=42,
            initial_prompt="{base_prompt}>",
            commands={
                "show clock": {"output": "foo"},
            },
        )
        
    with pytest.raises(ValidationError):
        nos = Nos(
            commands={
                "show clock": {"output": 42},
            },
        )
        
    with pytest.raises(ValidationError):
        nos = Nos(
            commands={
                "show clock": {"output": "foo", "new_prompt": 42},
            },
        )
        
    with pytest.raises(ValidationError):
        nos = Nos(
            commands={
                "show clock": {"output": "foo", "new_prompt": 42},
            },
        )

# test_fakenos_register_nos_plugin_class_validation_error()