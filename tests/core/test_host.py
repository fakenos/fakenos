import pytest
from unittest.mock import MagicMock, Mock, patch
from fakenos.core.host import Host

class TestHost:
    @pytest.fixture
    def host(self):
        server = {'plugin': 'server_plugin', 'configuration': {}}
        shell = {'plugin': 'shell_plugin', 'configuration': {}}
        nos = {'plugin': 'nos_plugin', 'configuration': {}}
        fakenos = Mock()
        fakenos.servers_plugins = {'server_plugin': Mock()}
        fakenos.shell_plugins = {'shell_plugin': Mock()}
        fakenos.nos_plugins = {'nos_plugin': Mock()}
        host = Host('name', 'username', 'password', 22, server, shell, nos, fakenos)
        return host

    def test_init(self, host):
        assert host.name == 'name'
        assert host.username == 'username'
        assert host.password == 'password'
        assert host.port == 22
        assert host.server_inventory == {'plugin': 'server_plugin', 'configuration': {}}
        assert host.shell_inventory == {'plugin': 'shell_plugin', 'configuration': {'base_prompt': 'name'}}
        assert host.nos_inventory == {'plugin': 'nos_plugin', 'configuration': {}}
        assert not host.running

    def test_start(self, host):
        """
        The test passes if the start method is called and the server is started.
        """
        host.start()
        assert host.running
        host.server.start.assert_called_once()

    def test_stop(self, host):
        host.start()
        mock_server = MagicMock()
        host.server = mock_server
        host.stop()
        assert not host.running
        mock_server.stop.assert_called_once()
        assert host.server is None
    