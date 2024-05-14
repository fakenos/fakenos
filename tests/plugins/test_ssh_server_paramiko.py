"""
Test cases for the ssh_server_paramiko plugin.
"""

import threading
import unittest
from unittest.mock import Mock

import paramiko

from fakenos.plugins.servers.ssh_server_paramiko import ParamikoSshServerInterface, TapIO


class ParamikoSSHServerInterfaceTest(unittest.TestCase):
    """
    Test cases for the ParamikoSSHServerInterface class.
    """

    def test_create_server_with_banner(self):
        """Create a ParamikoSSHServerInterface object with a banner."""
        paramiko_server: ParamikoSshServerInterface = ParamikoSshServerInterface("banner")
        self.assertEqual(paramiko_server.ssh_banner, "banner")

    def test_create_server_with_username(self):
        """Create a ParamikoSSHServerInterface object with a username."""
        paramiko_server: ParamikoSshServerInterface = ParamikoSshServerInterface(username="username")
        self.assertEqual(paramiko_server.username, "username")

    def test_create_server_with_password(self):
        """Create a ParamikoSSHServerInterface object with a password."""
        paramiko_server: ParamikoSshServerInterface = ParamikoSshServerInterface(password="password")
        self.assertEqual(paramiko_server.password, "password")

    def test_create_server_with_username_and_password(self):
        """Create a ParamikoSSHServerInterface object with a username and password."""
        paramiko_server: ParamikoSshServerInterface = ParamikoSshServerInterface(
            username="username", password="password"
        )
        self.assertEqual(paramiko_server.username, "username")
        self.assertEqual(paramiko_server.password, "password")

    def test_create_server_with_banner_username_and_password(self):
        """Create a ParamikoSSHServerInterface object with a banner, username, and password."""
        paramiko_server: ParamikoSshServerInterface = ParamikoSshServerInterface("banner", "username", "password")
        self.assertEqual(paramiko_server.ssh_banner, "banner")
        self.assertEqual(paramiko_server.username, "username")
        self.assertEqual(paramiko_server.password, "password")

    def test_check_channel_request_is_correct_when_session_request(self):
        """Check that the channel request is correct when the session request is made."""
        paramiko_server: ParamikoSshServerInterface = ParamikoSshServerInterface()
        self.assertEqual(paramiko_server.check_channel_request(kind="session", chanid=1), paramiko.OPEN_SUCCEEDED)

    def test_check_channel_request_is_incorrect_when_session_is_not_request(self):
        """Check that the channel request is incorrect when the session request is not made."""
        paramiko_server: ParamikoSshServerInterface = ParamikoSshServerInterface()
        self.assertEqual(
            paramiko_server.check_channel_request(kind="shell", chanid=1),
            paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED,
        )

    def test_check_channel_pty_request_returns_always_true(self):
        """Check that the channel pty request always returns True."""
        paramiko_server: ParamikoSshServerInterface = ParamikoSshServerInterface()
        self.assertTrue(
            paramiko_server.check_channel_pty_request(
                channel=1, term="xterm", width=80, height=24, pixelwidth=0, pixelheight=0, modes=None
            )
        )

    def test_check_channel_shell_request_returns_always_true(self):
        """Check that the channel shell request always returns True."""
        paramiko_server: ParamikoSshServerInterface = ParamikoSshServerInterface()
        self.assertTrue(paramiko_server.check_channel_shell_request(channel=1))

    def test_check_auth_username_incorrect(self):
        """Check that the authentication username is incorrect."""
        paramiko_server: ParamikoSshServerInterface = ParamikoSshServerInterface(
            username="username", password="password"
        )
        self.assertEqual(
            paramiko_server.check_auth_password(username="incorrect", password="password"), paramiko.AUTH_FAILED
        )

    def test_check_auth_password_incorrect(self):
        """Check that the authentication password is incorrect."""
        paramiko_server: ParamikoSshServerInterface = ParamikoSshServerInterface(
            username="username", password="password"
        )
        self.assertEqual(
            paramiko_server.check_auth_password(username="username", password="incorrect"), paramiko.AUTH_FAILED
        )

    def test_check_auth_username_and_password_incorrect(self):
        """Check that the authentication username and password are incorrect."""
        paramiko_server: ParamikoSshServerInterface = ParamikoSshServerInterface(
            username="username", password="password"
        )
        self.assertEqual(
            paramiko_server.check_auth_password(username="incorrect", password="incorrect"), paramiko.AUTH_FAILED
        )

    def test_check_auth_correct(self):
        """Check that the authentication is correct."""
        paramiko_server: ParamikoSshServerInterface = ParamikoSshServerInterface(
            username="username", password="password"
        )
        self.assertEqual(
            paramiko_server.check_auth_password(username="username", password="password"), paramiko.AUTH_SUCCESSFUL
        )

    def test_get_banner(self):
        """Check that the banner is returned."""
        paramiko_server: ParamikoSshServerInterface = ParamikoSshServerInterface("banner")
        self.assertEqual(paramiko_server.get_banner(), ("banner\r\n", "en-US"))


class TapIOTest(unittest.TestCase):
    """
    Test cases for the TapIO class.
    """

    def test_init(self):
        """Check that the TapIO object is initialized correctly."""
        run_srv: threading.Event = threading.Event()
        run_srv.set()
        tap_io: TapIO = TapIO(run_srv=run_srv)
        self.assertTrue(tap_io.run_srv)
        self.assertEqual(tap_io.lines, [])
        self.assertEqual(tap_io.closed, False)
        run_srv.clear()

    def test_readline(self):
        """Check that the readline method returns the correct line."""
        mock_run_srv: Mock = Mock()
        mock_run_srv.is_set.side_effect = [True] * 10 + [False]
        tap_io: TapIO = TapIO(run_srv=mock_run_srv)
        tap_io.lines = ["line1", "line2"]

        self.assertEqual(tap_io.readline(), "line2")
        self.assertEqual(tap_io.readline(), "line1")
        self.assertEqual(tap_io.readline(), None)

        self.assertEqual(mock_run_srv.is_set.call_count, 11)

    def test_write(self):
        """Check that the write method appends the line to the lines list."""
        tap_io: TapIO = TapIO(run_srv=threading.Event())
        tap_io.write("line1")
        self.assertEqual(tap_io.lines, ["line1"])


class ChannelToShellTapTest(unittest.TestCase):
    """
    Test cases for the ChannelToShellTap class.
    """

    def setUp(self):
        self.mock_channel_stdin: Mock = Mock()
        self.mock_shell_stdin: Mock = Mock()
        self.mock_shell_replied_event: Mock = Mock()
        self.mock_run_srv: Mock = Mock()
