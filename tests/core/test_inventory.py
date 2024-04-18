import logging
import pprint
import copy
import socket
import time

import pytest
from pydantic import ValidationError
from netmiko import ConnectHandler

from fakenos import FakeNOS
from fakenos.core.host import Host
import threading

fake_network = {
    "default": {
        "username": "user",
        "password": "user",
        "port": [5000, 6000],
        "server": {
            "plugin": "ParamikoSshServer",
            "configuration": {
                "ssh_key_file": "tests/assets/ssh_host_rsa_key",
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
        "core-router": {"replicas": 2, "port": [5000, 5001]},
    },
}

def get_running_hosts(hosts: dict[str, Host]) -> dict[str, bool]:
    """
    Get the running hosts in the network.
    """
    return {host_name: host.running for host_name, host in hosts.items()}

def test_fakenos_base_inventory():
    """
    Base test for checking the start and stop operations
    using default inventory.
    """
    net = FakeNOS()
    before_start = get_running_hosts(net.hosts)
    for running_state in before_start.values():
        assert running_state == False
    
    net.start()
    after_start = get_running_hosts(net.hosts)
    for running_state in after_start.values():
        assert running_state == True

    net.stop()
    after_stop = get_running_hosts(net.hosts)
    for running_state in after_stop.values():
        assert running_state == False


    assert len(before_start) == len(after_start) == len(after_stop) == 2

def get_platforms() -> list[str]:
    """
    It gets the current supported platforms.
    """
    platforms = []
    with open('platforms.md', 'r') as file:
        for line in file:
            if line.startswith('-'):
                platform = line[1:].strip()  # Remove the dash and whitespace
                if "❌" in platform:
                    continue
                platform = platform.split(' ')[0]  # Get the first word
                platforms.append(platform)
    return platforms

def get_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

@pytest.mark.parametrize("device_type", get_platforms())
def test_custom_inventory_network(device_type: str):
    """
    This test tries to connect to device as Netmiko would
    do. It ensures that the current implemented devices are
    ready to used with Netmiko. We only look if any error
    has raised.
    """
    free_port = get_free_port()
    inventory = {
        "hosts": {
            "router": {
                "username" : "usertest",
                "password" : "passwordtest",
                "port" : free_port,
                "platform": device_type
            }
        }
    }
    net = FakeNOS(inventory=inventory)
    
    net.start()

    device_credentials = {
        "host": "localhost",
        "username": "usertest",
        "password": "passwordtest",
        "port": free_port,
        "device_type": device_type
    }

    with ConnectHandler(**device_credentials):
        pass
    net.stop()

    assert threading.active_count() == 1


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

def test_fakenos_start_stop_hosts_with_glob_pattern():
    net = FakeNOS(inventory=fake_network)
    before_start = net.list_hosts()

    net.start(hosts="R[12], core-router1")
    after_start = net.list_hosts()

    net.stop(hosts=["R1", "core-router1"])
    after_stop = net.list_hosts()

    net.stop(hosts=["*"])
    after_stop_all = net.list_hosts()

    print("after_start R[12], core-router1")
    pprint.pprint(after_start)
    print("after stop R1, core-router1")
    pprint.pprint(after_stop)
    print("after stop all ['*']")
    pprint.pprint(after_stop_all)

    for i in after_start:
        if i["name"] in ["R1", "R2", "core-router1"]:
            assert i["running"] == True, f"{i['name']} should be running"
        else:
            assert i["running"] == False, f"{i['name']} should not be running"
    for i in after_stop:
        if i["name"] in ["R2"]:
            assert i["running"] == True, f"{i['name']} should be running"
        else:
            assert i["running"] == False, f"{i['name']} should not be running"
    assert all(i["running"] == False for i in after_stop_all), "Not all hosts stopped"
