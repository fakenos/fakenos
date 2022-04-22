import sys
import pprint
import time
import copy
import pytest
from pydantic import ValidationError

sys.path.insert(0, "..")

from fakenos import FakeNOS

fake_network = {
    "default": {
        "username": "user",
        "password": "user",
        "port": [5000, 6000],
        "server": {
            "plugin": "ParamikoSshServer",
            "configuration": {
                "ssh_key_file": "./ssh-keys/ssh_host_rsa_key",
                "timeout": 1,
                "address": "127.0.0.1",
            },
        },
        "shell": {"plugin": "CMDShell", "configuration": {}},
        "nos": {"plugin": "cisco_ios", "configuration": {}},
    },
    "hosts": {
        "R1": {
            "port": 5001,
            "username": "fakenos",
            "password": "fakenos",
            "server": {
                "plugin": "ParamikoSshServer",
                "configuration": {"address": "0.0.0.0"},
            },
            "shell": {
                "plugin": "CMDShell",
                "configuration": {"intro": "Custom SSH Shell"},
            },
        },
        "R2": {},
        "core-router": {"count": 2, "port": [5000, 6000]},
    },
}


def test_fakenos_base_inventory():
    """Base test to test start stop net opearions using default inventory"""
    net = FakeNOS()
    before_start = net.list_hosts()
    net.start()
    after_start = net.list_hosts()
    net.stop()
    after_stop = net.list_hosts()

    print("before_start: ")
    pprint.pprint(before_start)
    print("after_start: ")
    pprint.pprint(after_start)
    print("after_stop: ")
    pprint.pprint(after_stop)

    assert len(before_start) == len(after_start) == len(after_stop) == 2

    assert before_start[0]["name"] == "router1"
    assert before_start[0]["running"] == False
    assert before_start[1]["name"] == "router2"
    assert before_start[1]["running"] == False

    assert after_start[0]["name"] == "router1"
    assert after_start[0]["running"] == True
    assert after_start[1]["name"] == "router2"
    assert after_start[1]["running"] == True

    assert after_stop[0]["name"] == "router1"
    assert after_stop[0]["running"] == False
    assert after_stop[1]["name"] == "router2"
    assert after_stop[1]["running"] == False


# test_fakenos_base_inventory()

def test_validate_inventory_custom():
    # this should not raise any errors
    net = FakeNOS(inventory=fake_network)

# test_validate_inventory_custom()

def test_custom_inventory_network():
    from netmiko import ConnectHandler

    net = FakeNOS(inventory=fake_network)
    before_start = net.list_hosts()

    net.start()
    after_start = net.list_hosts()

    # try connecting to each device and running command
    outputs = {}
    default_username = fake_network["default"]["username"]
    default_password = fake_network["default"]["password"]
    for item in after_start:
        device_data = {
            "device_type": item["nos"],
            # "host": item["address"],
            "host": "127.0.0.1",
            "username": fake_network["hosts"]
            .get(item["name"], {})
            .get("username", default_username),
            "password": fake_network["hosts"]
            .get(item["name"], {})
            .get("password", default_password),
            "port": item["port"],
        }
        pprint.pprint(device_data)
        device = ConnectHandler(**device_data)
        outputs[item["name"]] = device.send_command("show clock")
        device.disconnect()

    net.stop()
    after_stop = net.list_hosts()

    print("before_start: ")
    pprint.pprint(before_start)
    print("after_start: ")
    pprint.pprint(after_start)
    print("after_stop: ")
    pprint.pprint(after_stop)
    print("devices outputs: ")
    pprint.pprint(outputs)

    assert len(before_start) == 4, "Was expecting 4 devices"
    assert all(i["running"] == True for i in after_start), "Not all hosts started"
    assert len(outputs) == 4, "Not all 4 hosts produced outputs"
    assert all(
        isinstance(i, str) for i in outputs.values()
    ), "Not all hosts output is a string"
    assert all(
        "Traceback" not in i for i in outputs.values()
    ), "Some hosts output contains traceback"
    assert all(i["running"] == False for i in after_stop), "Not all hosts stopped"


# test_custom_inventory()


def test_list_hosts_pattern_filter():
    net = FakeNOS(inventory=fake_network)
    all_hosts = net.list_hosts()
    all_hosts_with_filter = net.list_hosts(hosts="*")
    subset_one = net.list_hosts(hosts="*router[12]")

    print("all_hosts_with_filter:")
    pprint.pprint(all_hosts_with_filter)

    print("subset_one:")
    pprint.pprint(subset_one)

    assert all("router" in i["name"] for i in subset_one)
    assert all_hosts == all_hosts_with_filter != []

# test_list_hosts_pattern_filter()


def test_inventory_validation_host_port():
    # test inventory host has no count and port is list
    invcp = copy.deepcopy(fake_network)
    invcp["hosts"]["R1"]["port"] = [5001]
    with pytest.raises(ValidationError):
        net = FakeNOS(inventory=invcp)
    
    # test host has count but port is int
    invcp = copy.deepcopy(fake_network)
    invcp["hosts"]["core-router"]["port"] = 6000
    with pytest.raises(ValidationError):
        net = FakeNOS(inventory=invcp)
        
# test_inventory_validation_host_port()


def test_inventory_validation_shell_plugin_name():
    # test inventory wrong shell plugin name
    invcp = copy.deepcopy(fake_network)
    invcp["hosts"]["R1"]["shell"]["plugin"] = "undefined"
    with pytest.raises(ValidationError):
        net = FakeNOS(inventory=invcp)    

def test_inventory_validation_cmdshell_plugin():
    # test inventory CMDShell plugin params
    invcp = copy.deepcopy(fake_network)
    invcp["hosts"]["R1"]["shell"]["configuration"] = {
        "intro": "Custom SSH Shell",
        "ruler": "=",
        "completekey": "tab",
        "newline": "\r\n",
    }
    net = FakeNOS(inventory=invcp)
    
# test_inventory_validation_cmdshell_plugin()