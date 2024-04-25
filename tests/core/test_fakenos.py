"""
Test module for fakenos.core.fakenos.
The file can be found in fakenos/core/fakenos.py
"""

# pylint: disable=protected-access
import threading
from unittest.mock import patch
import pytest
from fakenos.core.nos import available_platforms
from fakenos.core.fakenos import FakeNOS

from tests.utils import get_platforms_from_md, get_running_hosts


# pylint: disable=too-many-public-methods
class TestFakeNOS:
    """
    Test class for the FakeNOS class.
    """

    def test_create_fakenos_without_arguments(self):
        """
        Test that fakeNOS creates two hosts when no
        arguments are passed.
        Those routers should have the following:
        - names are router0 and router1
        - port are 6000 and 6001
        - address is localhost
        - timeout is 1
        - username is user
        - password is user
        - server plugin is ParamikoSshServer
        - shell plugin is CMDShell
        """
        net = FakeNOS()
        assert len(net.hosts) == 2
        for router_name, host in net.hosts.items():
            assert router_name in ["router0", "router1"]
            assert host.username in ["user"]
            assert host.password in ["user"]
            assert host.port in {6000, 6001}
            assert host.server_inventory["plugin"] == "ParamikoSshServer"
            assert host.server_inventory["configuration"]["address"] == "127.0.0.1"
            assert host.server_inventory["configuration"]["timeout"] == 1
            assert host.shell_inventory["plugin"] == "CMDShell"
            assert host.shell_inventory["configuration"] == {"base_prompt": router_name}

    def test_create_fakenos_with_inventory_as_dict(self):
        """
        Test that fakeNOS creates two hosts when an inventory is passed.
        Those routers should have the following:
        - names are R1 and R2
        - port are 5001 and 6000
        - username is fakenos
        - password is fakenos
        """
        inventory = {
            "hosts": {
                "R1": {
                    "port": 5001,
                    "username": "fakenos_R1",
                    "password": "fakenos_R1",
                    "platform": available_platforms[0],
                },
                "R2": {
                    "port": 6000,
                    "username": "fakenos_R2",
                    "password": "fakenos_R2",
                    "platform": available_platforms[0],
                },
            }
        }
        net = FakeNOS(inventory=inventory)
        assert len(net.hosts) == 2
        for router_name, host in net.hosts.items():
            assert router_name in ["R1", "R2"]
            assert host.username in ["fakenos_R1", "fakenos_R2"]
            assert host.password in ["fakenos_R1", "fakenos_R2"]
            assert host.port in [5001, 6000]

    def test_create_fakenos_with_inventory_as_file(self):
        """
        Test that fakeNOS creates two hosts when an inventory is passed as a file.
        Those routers should have the following:
        - names are R1 and R2
        - port are 5001 and 6000
        - username is fakenos
        - password is fakenos
        """
        net = FakeNOS(inventory="tests/assets/inventory.yaml")
        assert len(net.hosts) == 2
        for router_name, host in net.hosts.items():
            assert router_name in ["R1", "R2"]
            assert host.username in "fakenos"
            assert host.password in "fakenos"
            assert host.port in [5001, 6000]

    def test_is_inventory_in_yaml(self):
        """
        Test that the inventory is in yaml format.
        """
        net = FakeNOS(inventory="tests/assets/inventory.yaml")
        assert isinstance(net.inventory, dict)

    def test_is_inventory_in_yaml_false(self):
        """
        Test that the inventory is in yaml format.
        """
        with pytest.raises(Exception):
            FakeNOS(inventory="tests/assets/inventory.txt")

    def test_is_inventory_in_yaml_unit(self):
        """
        Test that the function _is_inventory_in_yaml returns True
        when the inventory is in yaml format.
        """
        net = FakeNOS()
        net.inventory = "tests/assets/inventory.yaml"
        assert net._is_inventory_in_yaml() is True

    def test_is_inventory_in_yaml_unit_false(self):
        """
        Test that the function _is_inventory_in_yaml returns False
        when the inventory is not in yaml format.
        """
        net = FakeNOS()
        net.inventory = "tests/assets/inventory.txt"
        assert net._is_inventory_in_yaml() is False

    def test_load_inventory_yaml_unit_true(self):
        """
        Test that the function _load_inventory_yaml returns a dictionary
        when the inventory is in yaml format.
        """
        net = FakeNOS()
        net.inventory = "tests/assets/inventory.yaml"
        net._load_inventory_yaml()
        assert isinstance(net.inventory, dict)

    def test_load_inventory_yaml_unit_false(self):
        """
        Test that the function _load_inventory_yaml returns None
        when the inventory is not in yaml format.
        """
        net = FakeNOS()
        net.inventory = "tests/assets/inventory.txt"
        assert net._load_inventory_yaml() is None

    def test_load_inventory_unit_yaml(self):
        """
        Test that the function _load_inventory loads the inventory
        when the inventory is in yaml format.
        """
        net = FakeNOS()
        net.inventory = "tests/assets/inventory.yaml"
        net._load_inventory()
        assert isinstance(net.inventory, dict)

    def test_load_inventory_unit_dict(self):
        """
        Test that the function _load_inventory loads the inventory
        when the inventory is a dictionary.
        """
        net = FakeNOS()
        net.inventory = {"hosts": {"R1": {"port": 5001}}}
        net._load_inventory()
        assert isinstance(net.inventory, dict)

    def test_load_inventory_unit_default(self):
        """
        Test that the function _load_inventory loads the inventory
        when the inventory is a dictionary with a default key.
        """
        net = FakeNOS()
        net.inventory = {"default": {"port": 5001}, "hosts": {"R1": {}}}
        net._load_inventory()
        assert isinstance(net.inventory, dict)

    def test_load_inventory_unit_wrong_dict(self):
        """
        Test that the function _load_inventory raises an exception
        when the inventory is not a dictionary.
        """
        net = FakeNOS()
        net.inventory = "tests/assets/inventory.txt"
        with pytest.raises(Exception):
            net._load_inventory()

    @patch("fakenos.core.fakenos.FakeNOS._allocate_port")
    def test_init_unit(self, mock_allocate_port):
        """
        Test that the function _init creates the hosts.
        """
        inventory = {"hosts": {"R1": {"port": 5001, "platform": "cisco_ios"}}}
        net = FakeNOS(inventory)
        assert len(net.hosts) == 1
        assert "R1" in net.hosts
        assert mock_allocate_port.call_count == 1

    def test_port_already_allocated(self):
        """
        Test that the function _allocate_port raises an exception
        when the port is already allocated.
        """
        net = FakeNOS()
        net.allocated_ports = [5000]
        with pytest.raises(ValueError):
            net._allocate_port(5000)

    def test_allocate_port(self):
        """
        Test that the function _allocate_port allocates the port.
        """
        inventory = {"hosts": {"R1": {"port": 5000, "platform": "cisco_ios"}}}
        net = FakeNOS(inventory=inventory)
        assert 5000 in net.allocated_ports
        assert len(net.allocated_ports) == 1

    def test_allocate_port_range(self):
        """
        Test that the function _allocate_port allocates the port.
        """
        inventory = {"hosts": {"R1": {"port": [5000, 5001], "replicas": 2, "platform": "cisco_ios"}}}
        net = FakeNOS(inventory=inventory)
        assert net.allocated_ports == {5000, 5001}

    def test_replicas_not_set_and_port_list(self):
        """
        Test that the function _check_ports_and_replicas_are_okey raises an exception
        when replicas is not set.
        """
        inventory = {"default": {"port": [5000, 5001]}, "hosts": {"R1": {}}}
        with pytest.raises(ValueError):
            FakeNOS(inventory=inventory)

    def test_replicas_set_and_port_int(self):
        """
        Test that the function _check_ports_and_replicas_are_okey raises an exception
        when replicas is set and port is an int.
        """
        inventory = {"default": {"port": 5000, "replicas": 2}, "hosts": {"R1": {}}}
        with pytest.raises(ValueError):
            FakeNOS(inventory=inventory)

    def test_replicas_set_and_port_list_not_enough_ports(self):
        """
        Test that the function _check_ports_and_replicas_are_okey raises an exception
        when replicas is set and there are not enough ports.
        """
        inventory = {"default": {"port": [5000], "replicas": 2}, "hosts": {"R1": {}}}
        with pytest.raises(ValueError):
            FakeNOS(inventory=inventory)

    def test_replicas_set_and_port_list_too_many_ports(self):
        """
        Test that the function _check_ports_and_replicas_are_okey raises an exception
        when replicas is set and there are too many ports.
        """
        inventory = {"default": {"port": [5000, 5001, 5002], "replicas": 2}, "hosts": {"R1": {}}}
        with pytest.raises(ValueError):
            FakeNOS(inventory=inventory)

    def test_replicas_set_and_port_1_larger_than_port_2(self):
        """
        Test that the function _check_ports_and_replicas_are_okey raises an exception
        when replicas is set and the first port is larger than the second port.
        """
        inventory = {"default": {"port": [5001, 5000], "replicas": 2}, "hosts": {"R1": {}}}
        with pytest.raises(ValueError):
            FakeNOS(inventory=inventory)

    def test_replicas_set_and_replicas_less_than_1(self):
        """
        Test that the function _check_ports_and_replicas_are_okey raises an exception
        when replicas is set and the replicas are less than 1.
        """
        inventory = {"default": {"port": [5000, 5001], "replicas": 0}, "hosts": {"R1": {}}}
        with pytest.raises(ValueError):
            FakeNOS(inventory=inventory)

    def test_replicas_set_and_ports_set_not_same_length(self):
        """
        Test that the function _check_ports_and_replicas_are_okey raises an exception
        when replicas is set and the ports are not the same length.
        """
        inventory = {"default": {"port": [5000, 5001], "replicas": 3}, "hosts": {"R1": {}}}
        with pytest.raises(ValueError):
            FakeNOS(inventory=inventory)

    def test_wrong_plugin_name(self):
        """
        Test that the function _check_plugin_name raises an exception
        when the plugin name is wrong.
        """
        inventory = {"hosts": {"R1": {"server": {"plugin": "wrong_plugin"}}}}
        with pytest.raises(ValueError):
            FakeNOS(inventory=inventory)

    def test_wrong_platform(self):
        """
        Test that the function _check_platform raises an exception
        when the platform is wrong.
        """
        inventory = {"hosts": {"R1": {"platform": "wrong_platform"}}}
        with pytest.raises(ValueError):
            FakeNOS(inventory=inventory)

    def test_inventory_validation_cmdshell_plugin(self):
        """
        Test that the inventory is validated when
        it contains a shell plugin.
        """
        inventory = {
            "hosts": {
                "R1": {
                    "port": 6000,
                    "platform": available_platforms[0],
                    "shell": {
                        "plugin": "CMDShell",
                        "configuration": {},
                    },
                }
            }
        }
        net = FakeNOS(inventory=inventory)
        assert net.inventory["hosts"]["R1"]["shell"]["plugin"] == "CMDShell"

    def test_fakenos_start_stop_hosts(self):
        """
        Test that the function start and stop hosts by the name.
        """
        net = FakeNOS()

        net.start(hosts="router0")
        assert net.hosts["router0"].running is True
        assert net.hosts["router1"].running is False

        net.start(hosts="router1")
        assert net.hosts["router0"].running is True
        assert net.hosts["router1"].running is True

        net.stop(hosts="router0")
        assert net.hosts["router0"].running is False
        assert net.hosts["router1"].running is True

        net.stop(hosts="router1")
        assert net.hosts["router0"].running is False
        assert net.hosts["router1"].running is False

        net.stop()

    def test_fakenos_base_inventory(self):
        """
        Base test for checking the start and stop operations
        using default inventory.
        """
        net = FakeNOS()
        before_start = get_running_hosts(net.hosts)
        for running_state in before_start.values():
            assert running_state is False

        net.start()
        after_start = get_running_hosts(net.hosts)
        for running_state in after_start.values():
            assert running_state is True

        net.stop()
        after_stop = get_running_hosts(net.hosts)
        for running_state in after_stop.values():
            assert running_state is False

        assert len(before_start) == len(after_start) == len(after_stop) == 2

    def test_number_of_threads_after_stop_is_only_main(self):
        """
        Test that the number of threads after stopping the network is only the main thread.
        """
        net = FakeNOS()
        net.start()
        net.stop()
        active_threads = threading.active_count()
        assert active_threads == 1


class TestPlatforms:
    """
    Tests directly related to the platforms like the ordering
    or if the platforms match the docs and the real in the code.
    """

    def test_available_platforms_match_docs(self):
        """
        Test if the available platforms are correct set
        in the platforms.md and platforms.py file.
        """
        assert sorted(available_platforms) == sorted(get_platforms_from_md())

    def test_available_platforms_in_py_file_are_ordered(self):
        """
        Test if the available platforms in the platforms.py file
        are ordered alphabetically.
        """
        assert available_platforms == sorted(available_platforms)

    def test_available_platforms_in_docs_are_ordered(self):
        """
        Test if the available platforms in the platforms.md file
        are ordered alphabetically.
        """
        platforms = get_platforms_from_md()
        assert platforms == sorted(platforms)
