import pytest
from unittest.mock import Mock, patch
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
        assert host.shell_inventory == {'plugin': 'shell_plugin', 'configuration': {}}
        assert host.nos_inventory == {'plugin': 'nos_plugin', 'configuration': {}}
        assert not host.running

    @patch.object(Host, 'start')
    def test_start(self, mock_start, host):
        host.start()
        assert host.running
        mock_start.assert_called_once()

    @patch.object(Host, 'stop')
    def test_stop(self, mock_stop, host):
        host.start()
        host.stop()
        assert not host.running
        mock_stop.assert_called_once()

    @patch('host.Host')
    def test_host_start(self, mock_host):
        server = {'plugin': 'server_plugin', 'configuration': {}}
        shell = {'plugin': 'shell_plugin', 'configuration': {}}
        nos = {'plugin': 'nos_plugin', 'configuration': {}}
        fakenos = Mock()
        fakenos.servers_plugins = {'server_plugin': Mock()}
        fakenos.shell_plugins = {'shell_plugin': Mock()}
        fakenos.nos_plugins = {'nos_plugin': Mock()}
        host = Host('name', 'username', 'password', 22, server, shell, nos, fakenos)
        host.start()
        mock_host.assert_called_once()
        assert host.running
        assert host.server_plugin == fakenos.servers_plugins['server_plugin']
        assert host.shell_plugin == fakenos.shell_plugins['shell_plugin']
        assert host.nos_plugin == fakenos.nos_plugins['nos_plugin']
        assert host.server is not None
        assert host.server_plugin is not None
        assert host.shell_plugin is not None
        assert host.nos_plugin is not None
        host.stop()
        assert not host.running
        assert host.server is None