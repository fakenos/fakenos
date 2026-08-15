"""
Test module for fakenos.core.fakenos.
The file can be found in fakenos/core/fakenos.py
"""

# pylint: disable=protected-access
import platform
import threading
from unittest.mock import Mock, patch

import detect
import pytest
import yaml

from fakenos.core.fakenos import FakeNOS, fakenos
from fakenos.core.host import Host
from fakenos.core.nos import available_platforms, Nos
from fakenos.plugins.nos import nos_plugins
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
        assert len(net.hosts) == 3
        for router_name, host in net.hosts.items():
            assert router_name in [
                "router_cisco_ios",
                "router_huawei_smartax",
                "router_arista_eos",
            ]
            assert host.username in ["user"]
            assert host.password in ["user"]
            assert host.port in {6000, 6001, 6002}
            assert host.server_inventory["plugin"] == "ParamikoSshServer"
            if detect.docker and "WSL2" in platform.release():
                assert host.server_inventory["configuration"]["address"] == "0.0.0.0"
            else:
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
        inventory = {
            "default": {"port": [5000, 5001, 5002], "replicas": 2},
            "hosts": {"R1": {}},
        }
        with pytest.raises(ValueError):
            FakeNOS(inventory=inventory)

    def test_replicas_set_and_port_1_larger_than_port_2(self):
        """
        Test that the function _check_ports_and_replicas_are_okey raises an exception
        when replicas is set and the first port is larger than the second port.
        """
        inventory = {
            "default": {"port": [5001, 5000], "replicas": 2},
            "hosts": {"R1": {}},
        }
        with pytest.raises(ValueError):
            FakeNOS(inventory=inventory)

    def test_replicas_set_and_replicas_less_than_1(self):
        """
        Test that the function _check_ports_and_replicas_are_okey raises an exception
        when replicas is set and the replicas are less than 1.
        """
        inventory = {
            "default": {"port": [5000, 5001], "replicas": 0},
            "hosts": {"R1": {}},
        }
        with pytest.raises(ValueError):
            FakeNOS(inventory=inventory)

    def test_replicas_set_and_ports_set_not_same_length(self):
        """
        Test that the function _check_ports_and_replicas_are_okey raises an exception
        when replicas is set and the ports are not the same length.
        """
        inventory = {
            "default": {"port": [5000, 5001], "replicas": 3},
            "hosts": {"R1": {}},
        }
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

    def test_inventory_configuration_dict(self):
        """
        Test that the inventory is validated when
        it contains a configuration.
        """
        configurations: dict = {}
        with open("tests/assets/test_module.yaml.j2", "r", encoding="utf-8") as file:
            data = file.read()
            configurations = yaml.safe_load(data)
        inventory = {
            "hosts": {
                "R1": {
                    "port": 6000,
                    "platform": "huawei_smartax",
                    "configuration_file": "tests/assets/test_module.yaml.j2",
                }
            }
        }
        with FakeNOS(inventory=inventory) as net:
            host: Host = next(iter(net.hosts.values()))
            assert host.nos.device.configurations == configurations

    def test_inventory_configuration_yaml(self):
        """
        Test that the inventory is validated when
        it contains a configuration_file.
        """
        configurations: dict = {}
        with open("tests/assets/test_module.yaml.j2", "r", encoding="utf-8") as file:
            data = file.read()
            configurations = yaml.safe_load(data)
        with FakeNOS(inventory="tests/assets/inventory_configuration.yaml") as net:
            host: Host = next(iter(net.hosts.values()))
            assert host.nos.device.configurations == configurations

    def test_fakenos_start_stop_hosts(self):
        """
        Test that the function start and stop hosts by the name.
        """
        net = FakeNOS()

        net.start(hosts="router_cisco_ios")
        assert net.hosts["router_cisco_ios"].running is True
        assert net.hosts["router_huawei_smartax"].running is False
        assert net.hosts["router_arista_eos"].running is False

        net.start(hosts="router_huawei_smartax")
        assert net.hosts["router_cisco_ios"].running is True
        assert net.hosts["router_huawei_smartax"].running is True
        assert net.hosts["router_arista_eos"].running is False

        net.start(hosts="router_arista_eos")
        assert net.hosts["router_cisco_ios"].running is True
        assert net.hosts["router_huawei_smartax"].running is True
        assert net.hosts["router_arista_eos"].running is True

        net.stop(hosts="router_cisco_ios")
        assert net.hosts["router_cisco_ios"].running is False
        assert net.hosts["router_huawei_smartax"].running is True
        assert net.hosts["router_arista_eos"].running is True

        net.stop(hosts="router_huawei_smartax")
        assert net.hosts["router_cisco_ios"].running is False
        assert net.hosts["router_huawei_smartax"].running is False
        assert net.hosts["router_arista_eos"].running is True

        net.stop(hosts="router_arista_eos")
        assert net.hosts["router_cisco_ios"].running is False
        assert net.hosts["router_huawei_smartax"].running is False
        assert net.hosts["router_arista_eos"].running is False

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

        assert len(before_start) == len(after_start) == len(after_stop) == 3

    def test_number_of_threads_after_stop_is_only_main(self):
        """
        Test that the number of threads after stopping the network is only the main thread.
        """
        net = FakeNOS()
        net.start()
        net.stop()
        active_threads = threading.active_count()
        assert active_threads == 1

    def test_nos_load_inventory_from_py_and_yaml(self):
        """
        Test cisco_ios NOS loaded correctly as it has both
        cisco_ios.py and cisco_ios.yaml definitions
        """
        inventory = {"hosts": {"R1": {"port": 5001, "platform": "cisco_ios"}}}
        net = FakeNOS(inventory)
        assert len(net.nos_plugins["cisco_ios"]) == 2, "Not all files detected"


class TestCustomNosPlugins:
    """Regression tests for custom NOS plugin registration and selection."""

    @pytest.fixture(autouse=True)
    def isolate_nos_plugins(self, monkeypatch):
        """Keep custom plugin registration local to each test."""
        monkeypatch.setattr("fakenos.core.fakenos.nos_plugins", nos_plugins.copy())

    @pytest.fixture
    def custom_nos_plugin(self):
        """Return a custom NOS plugin accepted by FakeNOS."""
        return {
            "name": "NFIOSXR",
            "initial_prompt": "{base_prompt}>",
            "commands": {},
        }

    def test_custom_nos_plugin_is_registered_before_hosts(self, monkeypatch, custom_nos_plugin):
        """Custom plugins must be available while host objects are constructed."""
        original_host = Host

        def build_host(*args, **kwargs):
            assert "NFIOSXR" in kwargs["fakenos"].nos_plugins
            return original_host(*args, **kwargs)

        monkeypatch.setattr("fakenos.core.fakenos.Host", build_host)
        net = FakeNOS(
            inventory={"hosts": {"xr1": {"port": 7001, "nos": {"plugin": "NFIOSXR"}}}},
            plugins=[custom_nos_plugin],
        )

        assert net.nos_plugins["NFIOSXR"].name == "NFIOSXR"

    def test_custom_nos_plugin_with_platform_is_used_at_runtime(self, custom_nos_plugin):
        """Platform metadata must not replace an explicit custom NOS plugin."""
        net = FakeNOS(
            inventory={
                "hosts": {
                    "xr1": {
                        "port": 7001,
                        "platform": "cisco_xr",
                        "nos": {"plugin": "NFIOSXR"},
                    }
                }
            },
            plugins=[custom_nos_plugin],
        )
        server = Mock()
        server_plugin = Mock(return_value=server)
        net.servers_plugins = {**net.servers_plugins, "ParamikoSshServer": server_plugin}

        host = net.hosts["xr1"]
        host.start()

        assert host.platform == "cisco_xr"
        assert host.nos_inventory["plugin"] == "NFIOSXR"
        assert host.nos is net.nos_plugins["NFIOSXR"]
        assert server_plugin.call_args.kwargs["nos"] is net.nos_plugins["NFIOSXR"]

        host.stop()

    def test_custom_nos_plugin_without_platform_is_supported(self, custom_nos_plugin):
        """An explicit custom NOS plugin does not require platform metadata."""
        net = FakeNOS(
            inventory={"hosts": {"xr1": {"port": 7001, "nos": {"plugin": "NFIOSXR"}}}},
            plugins=[custom_nos_plugin],
        )

        assert net.hosts["xr1"].platform is None
        assert net.hosts["xr1"].nos_inventory["plugin"] == "NFIOSXR"

    def test_custom_nos_instance_is_registered(self):
        """FakeNOS accepts an already constructed Nos plugin instance."""
        plugin = Nos(name="CustomNos", initial_prompt="{base_prompt}>")
        net = FakeNOS(
            inventory={"hosts": {"router": {"port": 7001, "nos": {"plugin": "CustomNos"}}}},
            plugins=[plugin],
        )

        assert net.nos_plugins["CustomNos"] is plugin
        assert net.hosts["router"].nos_inventory["plugin"] == "CustomNos"

    def test_explicit_default_custom_nos_plugin_takes_precedence(self, custom_nos_plugin):
        """An explicit default NOS plugin takes precedence over host platform."""
        net = FakeNOS(
            inventory={
                "default": {"nos": {"plugin": "NFIOSXR"}},
                "hosts": {"xr1": {"port": 7001, "platform": "cisco_xr"}},
            },
            plugins=[custom_nos_plugin],
        )

        assert net.hosts["xr1"].nos_inventory["plugin"] == "NFIOSXR"

    def test_platform_only_inventory_derives_nos_plugin(self):
        """Platform-only inventories retain their legacy plugin selection."""
        net = FakeNOS(inventory={"hosts": {"xr1": {"port": 7001, "platform": "cisco_xr"}}})

        assert net.hosts["xr1"].nos_inventory["plugin"] == "cisco_xr"

    def test_custom_nos_plugin_name_is_not_valid_platform(self, custom_nos_plugin):
        """Registering a plugin must not also register platform metadata."""
        inventory = {
            "hosts": {
                "xr1": {
                    "port": 7001,
                    "platform": "NFIOSXR",
                    "nos": {"plugin": "NFIOSXR"},
                }
            }
        }

        with pytest.raises(ValueError, match="Platform NFIOSXR is not supported"):
            FakeNOS(inventory=inventory, plugins=[custom_nos_plugin])


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

    def test_with_works(self):
        """
        Test that the with statement works.
        """
        with FakeNOS() as net:
            assert len(net.hosts) == 3
        assert threading.active_count() == 1

    @fakenos(platform="cisco_ios", return_instance=True)
    def test_decorator_with_platform(self, net: FakeNOS):
        """Test that the decorator works with a platform."""
        platforms_used = [host.nos.name for host in net.hosts.values()]
        assert len(net.hosts) == 1
        assert "cisco_ios" in platforms_used
        assert "huawei_smartax" not in platforms_used
        assert "arista_eos" not in platforms_used

    @fakenos(inventory="tests/assets/inventory.yaml")
    def test_decorator_with_inventory(self):
        """
        Test that the decorator works with an inventory.
        This test is empty on purpose. If it loads
        correctly the inventory, it will work.
        """

    def test_decorator_raise_error_if_platform_and_inventory_provided(self):
        """Test that the decorator raises an exception if both platform and inventory are set."""
        with pytest.raises(ValueError):

            @fakenos(platform="cisco_ios", inventory="tests/assets/inventory.yaml")
            def dummy_function():
                pass

            dummy_function()

    def test_decorator_raise_error_if_not_platform_or_inventory_provided(self):
        """Test that the decorator raises an exception if neither platform nor inventory are set."""
        with pytest.raises(ValueError):

            @fakenos()
            def dummy_function():
                pass

            dummy_function()
