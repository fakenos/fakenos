import threading
import random

import pytest
from netmiko import ConnectHandler
from fakenos import FakeNOS, available_platforms

from tests.utils import get_platforms, get_free_port, generate_random_string


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

    @pytest.mark.filterwarnings("ignore:DeprecationWarning")
    @pytest.mark.timeout(30)
    @pytest.mark.parametrize("device_type", get_platforms())
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
        finally:
            all_threads = threading.enumerate()
            for thread in all_threads:
                if thread is not threading.main_thread():
                    thread.join()

    @pytest.mark.filterwarnings("ignore:'telnetlib' is deprecated")
    @pytest.mark.timeout(60)
    def test_fakenos_start_stop_hosts(self):
        """
        Test that the function start and stop hosts by the name.
        """
        inventory = {
            "hosts": {
                "router0": {
                    "port": get_free_port(),
                    "username": generate_random_string(5),
                    "password": generate_random_string(8),
                    "platform": random.choice(available_platforms),
                },
                "router1": {
                    "port": get_free_port(),
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
            for router in inventory["hosts"].keys():
                try:
                    with ConnectHandler(**credentials[router]):
                        assert net.hosts[router].running == True
                except (Exception,) as e:
                    assert net.hosts[router].running == False

        net.stop()