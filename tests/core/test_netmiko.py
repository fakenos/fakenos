"""
Test the Netmiko compatibility as this library can be used
as a testing tool for Netmiko.
"""

import re
import threading
import random

import pytest
import detect
from netmiko import ConnectHandler, NetMikoAuthenticationException, NetMikoTimeoutException
from fakenos.core.nos import available_platforms
from fakenos import FakeNOS

from tests.utils import get_platforms_from_md, get_free_port, generate_random_string


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


class TestNetmiko:
    """
    Test the Netmiko compatibility as this library can be used
    as a testing tool for Netmiko.
    """

    @pytest.mark.timeout(30)
    @pytest.mark.parametrize("device_type", get_platforms_from_md())
    def test_custom_inventory_network(self, device_type: str):
        """
        This test tries to connect to device as Netmiko would
        do. It ensures that the current implemented devices are
        ready to used with Netmiko. We only look if any error
        has raised.
        """
        try:
            free_port = get_free_port()
            inventory = {
                "hosts": {
                    "router": {
                        "username": "usertest",
                        "password": "passwordtest",
                        "port": free_port,
                        "platform": device_type,
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
                "device_type": device_type,
            }

            with ConnectHandler(**device_credentials):
                pass
            net.stop()

            n_threads: int = 2 if detect.windows else 1
            assert threading.active_count() == n_threads
        finally:
            all_threads = threading.enumerate()
            for thread in all_threads:
                if thread is not threading.main_thread() and "pytest_timeout" not in thread.name:
                    thread.join()

    @pytest.mark.timeout(20 * 10)
    def test_fakenos_start_stop_hosts(self):
        """
        Test that the function start and stop hosts by the name.
        """
        port_router0 = get_free_port()
        port_router1 = get_free_port()
        inventory = {
            "hosts": {
                "router0": {
                    "port": port_router0,
                    "username": generate_random_string(5),
                    "password": generate_random_string(8),
                    "platform": random.choice(available_platforms),
                },
                "router1": {
                    "port": port_router1,
                    "username": generate_random_string(5),
                    "password": generate_random_string(8),
                    "platform": random.choice(available_platforms),
                },
            }
        }
        credentials = {}
        for router in inventory["hosts"]:
            credentials[router] = {
                "host": "localhost",
                "username": inventory["hosts"][router]["username"],
                "password": inventory["hosts"][router]["password"],
                "port": inventory["hosts"][router]["port"],
                "device_type": inventory["hosts"][router]["platform"],
            }

        net = FakeNOS(inventory=inventory)

        for _ in range(10):  # Run the loop 10 times
            router_to_toggle = random.choice(list(inventory["hosts"].keys()))  # Choose a router randomly

            if net.hosts[router_to_toggle].running:
                net.stop(hosts=router_to_toggle)
            else:
                net.start(hosts=router_to_toggle)

            # Always check the state of both routers
            for router in inventory["hosts"]:
                try:
                    with ConnectHandler(**credentials[router]):
                        assert net.hosts[router].running is True
                except (NetMikoTimeoutException, NetMikoAuthenticationException):
                    assert net.hosts[router].running is False

        net.stop()

    def test_testing_module(self):
        free_port: int = get_free_port()
        inventory: dict = {
            "hosts": {
                "R1": {
                    "username": "user",
                    "password": "user",
                    "port": free_port,
                    "nos": {
                        "plugin": "tests/assets/module.py",
                    },
                }
            }
        }
        credentials: dict = {
            "host": "localhost",
            "username": "user",
            "password": "user",
            "port": free_port,
            "device_type": "generic",
        }
        with FakeNOS(inventory=inventory):
            with ConnectHandler(**credentials) as conn:
                output = conn.send_command("show clock")
                assert re.match(r"^\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}$", output)
