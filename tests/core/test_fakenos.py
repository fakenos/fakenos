import pytest
from fakenos.core.fakenos import FakeNOS

class TestFakeNOS:
    def test_create_FakeNOS_without_arguments(self):
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
            assert host.port in [6000, 6001]
            assert host.server_inventory["plugin"] == "ParamikoSshServer"
            assert host.server_inventory["configuration"]["address"] == "127.0.0.1"
            assert host.server_inventory["configuration"]["timeout"] == 1
            assert host.shell_inventory["plugin"] == "CMDShell"
            assert host.shell_inventory["configuration"] == {'base_prompt': router_name}

    def test_create_FakeNOS_with_inventory_as_dict(self):
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
                    "username": "fakenos",
                    "password": "fakenos",
                },
                "R2": {
                    "port": 6000,
                    "username": "fakenos",
                    "password": "fakenos",
                }
            }
        }
        net = FakeNOS(inventory=inventory)
        assert len(net.hosts) == 2
        for router_name, host in net.hosts.items():
            assert router_name in ["R1", "R2"]
            assert host.username in ["fakenos"]
            assert host.password in ["fakenos"]
            assert host.port in [5001, 6000]

    def test_create_FakeNOS_with_inventory_as_file(self, tmp_path):
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
            assert host.username in ["fakenos"]
            assert host.password in ["fakenos"]
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
        assert net._is_inventory_in_yaml() == True

    def test_is_inventory_in_yaml_unit_false(self):
        """
        Test that the function _is_inventory_in_yaml returns False
        when the inventory is not in yaml format.
        """
        net = FakeNOS()
        net.inventory = "tests/assets/inventory.txt"
        assert net._is_inventory_in_yaml() == False

    def test_load_inventory_yaml_unit_true(self):
        """
        Test that the function _load_inventory_yaml returns a dictionary
        when the inventory is in yaml format.
        """
        net = FakeNOS()
        net.inventory = "tests/assets/inventory.yaml"
        assert isinstance(net._load_inventory_yaml(), dict)

    def test_load_inventory_yaml_unit_false(self):
        """
        Test that the function _load_inventory_yaml returns None
        when the inventory is not in yaml format.
        """
        net = FakeNOS()
        net.inventory = "tests/assets/inventory.txt"
        assert net._load_inventory_yaml() == None

    
        
