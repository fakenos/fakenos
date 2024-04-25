"""
Test module for the module fakenos.core.host
under fakenos/core/host.py
"""

from unittest.mock import MagicMock, Mock, patch

import pytest

from fakenos.core.host import Host
from fakenos.core.nos import available_platforms
from fakenos import FakeNOS


class TestHost:
    """
    Test module for the Host class
    """

    @pytest.fixture
    def host(self):
        """Initial fixture for the setup"""
        server = {"plugin": "server_plugin", "configuration": {}}
        shell = {"plugin": "shell_plugin", "configuration": {}}
        nos = {"plugin": "nos_plugin", "configuration": {}}
        fakenos = Mock()
        fakenos.servers_plugins = {"server_plugin": Mock()}
        fakenos.shell_plugins = {"shell_plugin": Mock()}
        fakenos.nos_plugins = {"nos_plugin": Mock()}
        with patch.object(Host, "_check_if_platform_is_supported") as mock_check_platform:
            mock_check_platform.return_value = None
            host = Host("name", "username", "password", 22, server, shell, nos, fakenos)
        return host

    def test_init(self, host):
        """
        The test passes if the host is correctly initialized.
        """
        assert host.name == "name"
        assert host.username == "username"
        assert host.password == "password"
        assert host.port == 22
        assert host.server_inventory == {"plugin": "server_plugin", "configuration": {}}
        assert host.shell_inventory == {"plugin": "shell_plugin", "configuration": {"base_prompt": "name"}}
        assert host.nos_inventory == {"plugin": "nos_plugin", "configuration": {}}
        assert not host.running

    def test_start(self, host):
        """
        The test passes if the start method is called and the server is started.
        """
        host.start()
        assert host.running
        host.server.start.assert_called_once()

    def test_stop(self, host):
        """
        It test that when the host is called the stop,
        the server is correctly stoped and called
        its stop function.
        """
        host.start()
        mock_server = MagicMock()
        host.server = mock_server
        host.stop()
        assert not host.running
        mock_server.stop.assert_called_once()
        assert host.server is None

    def test_platform_is_wrong(self, host):
        """
        The test passes if the ValueError is raised when the platform is not supported.
        """
        platform = "wrong_platform"
        host.fakenos = FakeNOS()
        with pytest.raises(ValueError):
            # pylint: disable=protected-access
            host._check_if_platform_is_supported(platform)

    def test_platform_is_supported(self, host):
        """
        The test passes if the platform is supported.
        """
        host.fakenos = FakeNOS()
        platform = available_platforms[0]
        # pylint: disable=protected-access
        host._check_if_platform_is_supported(platform)
