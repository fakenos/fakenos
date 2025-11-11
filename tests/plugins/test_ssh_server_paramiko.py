"""
Test cases for the ssh_server_paramiko plugin.
"""

import io
import threading
from typing import Dict
import unittest
from unittest import mock
from unittest.mock import MagicMock, Mock

import paramiko

from fakenos.plugins.servers.ssh_server_paramiko import (
    channel_to_shell_tap,
    DEFAULT_SSH_KEY,
    ParamikoSshServer,
    ParamikoSshServerInterface,
    shell_to_channel_tap,
    TapIO,
)


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
        self.assertEqual(
            paramiko_server.check_channel_request(kind="session", chanid=1),
            paramiko.OPEN_SUCCEEDED,
        )

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
                channel=1,
                term="xterm",
                width=80,
                height=24,
                pixelwidth=0,
                pixelheight=0,
                modes=None,
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
            paramiko_server.check_auth_password(username="incorrect", password="password"),
            paramiko.AUTH_FAILED,
        )

    def test_check_auth_password_incorrect(self):
        """Check that the authentication password is incorrect."""
        paramiko_server: ParamikoSshServerInterface = ParamikoSshServerInterface(
            username="username", password="password"
        )
        self.assertEqual(
            paramiko_server.check_auth_password(username="username", password="incorrect"),
            paramiko.AUTH_FAILED,
        )

    def test_check_auth_username_and_password_incorrect(self):
        """Check that the authentication username and password are incorrect."""
        paramiko_server: ParamikoSshServerInterface = ParamikoSshServerInterface(
            username="username", password="password"
        )
        self.assertEqual(
            paramiko_server.check_auth_password(username="incorrect", password="incorrect"),
            paramiko.AUTH_FAILED,
        )

    def test_check_auth_correct(self):
        """Check that the authentication is correct."""
        paramiko_server: ParamikoSshServerInterface = ParamikoSshServerInterface(
            username="username", password="password"
        )
        self.assertEqual(
            paramiko_server.check_auth_password(username="username", password="password"),
            paramiko.AUTH_SUCCESSFUL,
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
        """Set up the ChannelToShellTap object."""
        self.mock_channel_stdio: Mock = Mock()
        self.mock_channel_stdio.read.return_value = b"b"
        self.mock_shell_stdin: Mock = Mock()
        self.mock_shell_replied_event: Mock = Mock()
        self.mock_run_srv: Mock = Mock()

    def test_channel_to_shell_tap_received_byte(self):
        """Check that the ChannelToShellTap object receives a byte."""
        self.mock_run_srv.is_set.side_effect = [True] * 10 + [False]
        channel_to_shell_tap(
            channel_stdio=self.mock_channel_stdio,
            shell_stdin=self.mock_shell_stdin,
            shell_replied_event=self.mock_shell_replied_event,
            run_srv=self.mock_run_srv,
        )
        self.mock_channel_stdio.read.assert_called_with(1)

    def test_channel_to_shell_tap_shell_replied_event_wait(self):
        """Check that the ChannelToShellTap object waits for the shell_replied_event."""
        self.mock_run_srv.is_set.side_effect = [True] * 10 + [False]
        channel_to_shell_tap(
            channel_stdio=self.mock_channel_stdio,
            shell_stdin=self.mock_shell_stdin,
            shell_replied_event=self.mock_shell_replied_event,
            run_srv=self.mock_run_srv,
        )
        self.mock_shell_replied_event.wait.assert_called_with(10)

    def test_channel_to_shell_tap_break_loop_when_channel_stdio_not_active(self):
        """Check that the ChannelToShellTap object breaks the loop when the channel_stdio is not active."""
        self.mock_channel_stdio.read.return_value = b""
        self.mock_channel_stdio.channel.active = False
        channel_to_shell_tap(
            channel_stdio=self.mock_channel_stdio,
            shell_stdin=self.mock_shell_stdin,
            shell_replied_event=self.mock_shell_replied_event,
            run_srv=self.mock_run_srv,
        )
        self.assertEqual(self.mock_run_srv.is_set.call_count, 1)

    def test_channel_to_shell_tap_break_loop_if_os_error(self):
        """Check that the ChannelToShellTap object breaks the loop if an OSError occurs."""
        self.mock_channel_stdio.write.side_effect = OSError
        channel_to_shell_tap(
            channel_stdio=self.mock_channel_stdio,
            shell_stdin=self.mock_shell_stdin,
            shell_replied_event=self.mock_shell_replied_event,
            run_srv=self.mock_run_srv,
        )
        self.assertEqual(self.mock_run_srv.is_set.call_count, 1)

    def test_channel_to_shell_tap_break_loop_if_eof_error(self):
        """Check that the ChannelToShellTap object breaks the loop if an EOFError occurs."""
        self.mock_channel_stdio.write.side_effect = EOFError
        channel_to_shell_tap(
            channel_stdio=self.mock_channel_stdio,
            shell_stdin=self.mock_shell_stdin,
            shell_replied_event=self.mock_shell_replied_event,
            run_srv=self.mock_run_srv,
        )
        self.assertEqual(self.mock_run_srv.is_set.call_count, 1)

    def test_channel_to_shell_tap_byte_return_character(self):
        """Check that the ChannelToShellTap object returns a character."""
        self.mock_run_srv.is_set.side_effect = [True] * 2 + [False]
        self.mock_channel_stdio.read.side_effect = [b"\r", b"\n"]
        channel_to_shell_tap(
            channel_stdio=self.mock_channel_stdio,
            shell_stdin=self.mock_shell_stdin,
            shell_replied_event=self.mock_shell_replied_event,
            run_srv=self.mock_run_srv,
        )
        self.mock_channel_stdio.write.assert_called_with(b"\r\n")
        self.assertEqual(self.mock_channel_stdio.write.call_count, 2)

        self.mock_shell_stdin.write.assert_called_with("\n")
        self.assertEqual(self.mock_shell_stdin.write.call_count, 2)

        self.assertEqual(self.mock_shell_replied_event.clear.call_count, 2)

    def test_channel_to_shell_tap_byte_return_x00_or_empty(self):
        """Check that the ChannelToShellTap object returns a character."""
        self.mock_run_srv.is_set.side_effect = [True] * 3 + [False]
        self.mock_channel_stdio.read.side_effect = [b"\x00", b"", b"\n"]
        channel_to_shell_tap(
            channel_stdio=self.mock_channel_stdio,
            shell_stdin=self.mock_shell_stdin,
            shell_replied_event=self.mock_shell_replied_event,
            run_srv=self.mock_run_srv,
        )
        self.mock_channel_stdio.write.assert_any_call(b"\x00")
        self.mock_channel_stdio.write.assert_any_call(b"")
        self.assertEqual(self.mock_channel_stdio.write.call_count, 3)

        self.assertEqual(self.mock_channel_stdio.write.call_count, 3)
        self.mock_shell_stdin.write.assert_called_with("\n")

    def test_channel_to_shell_tap_byte_return_other(self):
        """Check that the ChannelToShellTap object returns a character."""
        self.mock_run_srv.is_set.side_effect = [True] * 3 + [False]
        self.mock_channel_stdio.read.side_effect = [b"b", b"c", b"\n"]
        channel_to_shell_tap(
            channel_stdio=self.mock_channel_stdio,
            shell_stdin=self.mock_shell_stdin,
            shell_replied_event=self.mock_shell_replied_event,
            run_srv=self.mock_run_srv,
        )
        self.mock_channel_stdio.write.assert_any_call(b"b")
        self.mock_channel_stdio.write.assert_any_call(b"c")
        self.assertEqual(self.mock_channel_stdio.write.call_count, 3)

        self.assertEqual(self.mock_shell_stdin.write.call_count, 1)

    def test_channel_to_shell_tap_exit_run_srv(self):
        """Check that the ChannelToShellTap object exits the run_srv."""
        self.mock_run_srv.is_set.side_effect = [True, False]
        self.mock_channel_stdio.read.side_effect = [b"\x00"]
        channel_to_shell_tap(
            channel_stdio=self.mock_channel_stdio,
            shell_stdin=self.mock_shell_stdin,
            shell_replied_event=self.mock_shell_replied_event,
            run_srv=self.mock_run_srv,
        )
        self.assertEqual(self.mock_run_srv.is_set.call_count, 2)
        self.assertEqual(self.mock_channel_stdio.read.call_count, 1)


class ShellToChannelTapTest(unittest.TestCase):
    """
    Test cases for the ShellToChannelTap class.
    """

    def setUp(self):
        """Set up the ShellToChannelTap object."""
        self.mock_channel_stdio: Mock = Mock()
        self.mock_channel_stdio.closed = False
        self.mock_shell_stdout: Mock = Mock()
        self.mock_shell_replied_event: Mock = Mock()
        self.mock_run_srv: Mock = Mock()

    def test_shell_to_channel_tap_channel_stdio_closed(self):
        """Check that the ShellToChannelTap object closes the channel_stdio."""
        self.mock_channel_stdio.closed = True
        shell_to_channel_tap(
            channel_stdio=self.mock_channel_stdio,
            shell_stdout=self.mock_shell_stdout,
            shell_replied_event=self.mock_shell_replied_event,
            run_srv=self.mock_run_srv,
        )
        self.mock_run_srv.is_set.assert_called_once()

    def test_shell_to_channel_tap_shell_stdout_readline_return_none(self):
        """
        Check that the ShellToChannelTap object reads a line
        from the shell_stdout that is None.
        """
        self.mock_shell_stdout.readline.return_value = None
        shell_to_channel_tap(
            channel_stdio=self.mock_channel_stdio,
            shell_stdout=self.mock_shell_stdout,
            shell_replied_event=self.mock_shell_replied_event,
            run_srv=self.mock_run_srv,
        )
        self.mock_shell_stdout.readline.assert_called_once()
        self.mock_run_srv.is_set.assert_called_once()

    def test_shell_to_channel_tap_shell_stdout_readline_return_carry_return(self):
        """
        Check that the ShellToChannelTap object reads a line
        from the shell_stdout that is a carriage return and newline.
        """
        self.mock_run_srv.is_set.side_effect = [True, False]
        self.mock_shell_stdout.readline.return_value = "\r\n"
        shell_to_channel_tap(
            channel_stdio=self.mock_channel_stdio,
            shell_stdout=self.mock_shell_stdout,
            shell_replied_event=self.mock_shell_replied_event,
            run_srv=self.mock_run_srv,
        )
        self.mock_shell_stdout.readline.assert_called_once()
        self.mock_channel_stdio.write.assert_called_once_with(b"\r\n")

    def test_shell_to_channel_tap_shell_stdout_readline_return_newline(self):
        """
        Check that the ShellToChannelTap object reads a line
        from the shell_stdout that is a newline.
        """
        self.mock_run_srv.is_set.side_effect = [True, False]
        self.mock_shell_stdout.readline.return_value = "\n"
        shell_to_channel_tap(
            channel_stdio=self.mock_channel_stdio,
            shell_stdout=self.mock_shell_stdout,
            shell_replied_event=self.mock_shell_replied_event,
            run_srv=self.mock_run_srv,
        )
        self.mock_shell_stdout.readline.assert_called_once()
        self.mock_channel_stdio.write.assert_called_once_with(b"\r\n")

    def test_shell_to_channel_tap_shell_stdout_readline_return_other(self):
        """
        Check that the ShellToChannelTap object reads a line
        from the shell_stdout that is a character.
        """
        self.mock_run_srv.is_set.side_effect = [True, False]
        self.mock_shell_stdout.readline.return_value = "b"
        shell_to_channel_tap(
            channel_stdio=self.mock_channel_stdio,
            shell_stdout=self.mock_shell_stdout,
            shell_replied_event=self.mock_shell_replied_event,
            run_srv=self.mock_run_srv,
        )
        self.mock_shell_stdout.readline.assert_called_once()
        self.mock_channel_stdio.write.assert_called_once_with(b"b")

    def test_shell_to_channel_tap_socket_error(self):
        """Check that the ShellToChannelTap object breaks the loop if a socket error occurs."""
        self.mock_shell_stdout.readline.return_value = "b"
        self.mock_channel_stdio.write.side_effect = OSError(104, "Connection reset by peer")
        shell_to_channel_tap(
            channel_stdio=self.mock_channel_stdio,
            shell_stdout=self.mock_shell_stdout,
            shell_replied_event=self.mock_shell_replied_event,
            run_srv=self.mock_run_srv,
        )
        self.mock_run_srv.is_set.assert_called_once()

    def test_shell_to_channel_tap_set_replied_flag(self):
        """Check that the ShellToChannelTap object sets the replied flag."""
        self.mock_run_srv.is_set.side_effect = [True, False]
        self.mock_shell_stdout.readline.return_value = "b"
        shell_to_channel_tap(
            channel_stdio=self.mock_channel_stdio,
            shell_stdout=self.mock_shell_stdout,
            shell_replied_event=self.mock_shell_replied_event,
            run_srv=self.mock_run_srv,
        )
        self.mock_shell_replied_event.set.assert_called_once()

    def test_shell_to_channel_tap_exit_run_srv(self):
        """Check that the ShellToChannelTap object exits the run_srv."""
        self.mock_run_srv.is_set.side_effect = [True, False]
        self.mock_shell_stdout.readline.return_value = "b"
        shell_to_channel_tap(
            channel_stdio=self.mock_channel_stdio,
            shell_stdout=self.mock_shell_stdout,
            shell_replied_event=self.mock_shell_replied_event,
            run_srv=self.mock_run_srv,
        )
        self.assertEqual(self.mock_run_srv.is_set.call_count, 2)


class ParamikoSshServerTest(unittest.TestCase):
    """
    Test cases for the ParamikoSshServer class.
    """

    def setUp(self):
        """Set up the ParamikoSshServer tests."""
        self.arguments: Dict = {
            "shell": Mock(),
            "nos": Mock(),
            "nos_inventory_config": {},
            "port": 22,
            "username": "admin",
            "password": "admin",
        }

    def test_init_with_minimum_arguments(self):
        """
        Check that the ParamikoSshServer object is initialized correctly with
        the minimum parameters needed.
        """
        paramiko_server: ParamikoSshServer = ParamikoSshServer(**self.arguments)
        self.assertEqual(paramiko_server.nos, self.arguments["nos"])
        self.assertEqual(paramiko_server.nos_inventory_config, self.arguments["nos_inventory_config"])
        self.assertEqual(paramiko_server.shell, self.arguments["shell"])
        self.assertEqual(paramiko_server.shell_configuration, {})
        self.assertEqual(paramiko_server.ssh_banner, "FakeNOS Paramiko SSH Server")
        self.assertEqual(paramiko_server.username, self.arguments["username"])
        self.assertEqual(paramiko_server.password, self.arguments["password"])
        self.assertEqual(paramiko_server.port, self.arguments["port"])
        self.assertEqual(paramiko_server.address, "127.0.0.1")
        self.assertEqual(paramiko_server.timeout, 1)
        self.assertEqual(paramiko_server.watchdog_interval, 1)
        # pylint: disable=protected-access
        self.assertEqual(
            paramiko_server._ssh_server_key,
            paramiko.RSAKey(file_obj=io.StringIO(DEFAULT_SSH_KEY)),
        )

    def test_init_with_ssh_key_file(self):
        """
        Check th<at the ParamikoSshServer object is initialized correctly with
        the ssh_key_file parameter.
        """
        paramiko_server: ParamikoSshServer = ParamikoSshServer(
            **self.arguments,
            ssh_key_file="tests/assets/ssh_host_rsa_key",
        )
        self.assertEqual(paramiko_server.nos, self.arguments["nos"])
        self.assertEqual(paramiko_server.nos_inventory_config, self.arguments["nos_inventory_config"])
        self.assertEqual(paramiko_server.shell, self.arguments["shell"])
        self.assertEqual(paramiko_server.shell_configuration, {})
        self.assertEqual(paramiko_server.ssh_banner, "FakeNOS Paramiko SSH Server")
        self.assertEqual(paramiko_server.username, self.arguments["username"])
        self.assertEqual(paramiko_server.password, self.arguments["password"])
        self.assertEqual(paramiko_server.port, self.arguments["port"])
        self.assertEqual(paramiko_server.address, "127.0.0.1")
        self.assertEqual(paramiko_server.timeout, 1)
        self.assertEqual(paramiko_server.watchdog_interval, 1)
        # pylint: disable=protected-access
        self.assertEqual(
            paramiko_server._ssh_server_key,
            paramiko.RSAKey(filename="tests/assets/ssh_host_rsa_key"),
        )

    def test_init_with_ssh_key_file_and_password(self):
        """
        Check that the ParamikoSshServer object is initialized correctly with
        the ssh_key_file and ssh_key_password parameters.
        """
        paramiko_server: ParamikoSshServer = ParamikoSshServer(
            **self.arguments,
            ssh_key_file="tests/assets/ssh_host_rsa_key_with_password",
            ssh_key_file_password="password",
        )
        self.assertEqual(paramiko_server.nos, self.arguments["nos"])
        self.assertEqual(paramiko_server.nos_inventory_config, self.arguments["nos_inventory_config"])
        self.assertEqual(paramiko_server.shell, self.arguments["shell"])
        self.assertEqual(paramiko_server.shell_configuration, {})
        self.assertEqual(paramiko_server.ssh_banner, "FakeNOS Paramiko SSH Server")
        self.assertEqual(paramiko_server.username, self.arguments["username"])
        self.assertEqual(paramiko_server.password, self.arguments["password"])
        self.assertEqual(paramiko_server.port, self.arguments["port"])
        self.assertEqual(paramiko_server.address, "127.0.0.1")
        self.assertEqual(paramiko_server.timeout, 1)
        self.assertEqual(paramiko_server.watchdog_interval, 1)
        # pylint: disable=protected-access
        self.assertEqual(
            paramiko_server._ssh_server_key,
            paramiko.RSAKey(
                filename="tests/assets/ssh_host_rsa_key_with_password",
                password="password",
            ),
        )

    def test_init_with_ssh_banner(self):
        """
        Check that the ParamikoSshServer object is initialized correctly with
        the ssh_banner parameter.
        """
        paramiko_server: ParamikoSshServer = ParamikoSshServer(
            **self.arguments,
            ssh_banner="SSH Banner",
        )
        self.assertEqual(paramiko_server.nos, self.arguments["nos"])
        self.assertEqual(paramiko_server.nos_inventory_config, self.arguments["nos_inventory_config"])
        self.assertEqual(paramiko_server.shell, self.arguments["shell"])
        self.assertEqual(paramiko_server.shell_configuration, {})
        self.assertEqual(paramiko_server.ssh_banner, "SSH Banner")
        self.assertEqual(paramiko_server.username, self.arguments["username"])
        self.assertEqual(paramiko_server.password, self.arguments["password"])
        self.assertEqual(paramiko_server.port, self.arguments["port"])
        self.assertEqual(paramiko_server.address, "127.0.0.1")
        self.assertEqual(paramiko_server.timeout, 1)
        self.assertEqual(paramiko_server.watchdog_interval, 1)
        # pylint: disable=protected-access
        self.assertEqual(
            paramiko_server._ssh_server_key,
            paramiko.RSAKey(file_obj=io.StringIO(DEFAULT_SSH_KEY)),
        )

    def test_init_with_shell_configuration(self):
        """
        Check that the ParamikoSshServer object is initialized correctly with
        the shell_configuration parameter.
        """
        paramiko_server: ParamikoSshServer = ParamikoSshServer(
            **self.arguments,
            shell_configuration={"shell": "configuration"},
        )
        self.assertEqual(paramiko_server.nos, self.arguments["nos"])
        self.assertEqual(paramiko_server.nos_inventory_config, self.arguments["nos_inventory_config"])
        self.assertEqual(paramiko_server.shell, self.arguments["shell"])
        self.assertEqual(paramiko_server.shell_configuration, {"shell": "configuration"})
        self.assertEqual(paramiko_server.ssh_banner, "FakeNOS Paramiko SSH Server")
        self.assertEqual(paramiko_server.username, self.arguments["username"])
        self.assertEqual(paramiko_server.password, self.arguments["password"])
        self.assertEqual(paramiko_server.port, self.arguments["port"])
        self.assertEqual(paramiko_server.address, "127.0.0.1")
        self.assertEqual(paramiko_server.timeout, 1)
        self.assertEqual(paramiko_server.watchdog_interval, 1)
        # pylint: disable=protected-access
        self.assertEqual(
            paramiko_server._ssh_server_key,
            paramiko.RSAKey(file_obj=io.StringIO(DEFAULT_SSH_KEY)),
        )

    def test_init_with_address(self):
        """
        Check that the ParamikoSshServer object is initialized correctly with
        the address parameter.
        """
        paramiko_server: ParamikoSshServer = ParamikoSshServer(
            **self.arguments,
            address="127.0.0.2",
        )
        self.assertEqual(paramiko_server.nos, self.arguments["nos"])
        self.assertEqual(paramiko_server.nos_inventory_config, self.arguments["nos_inventory_config"])
        self.assertEqual(paramiko_server.shell, self.arguments["shell"])
        self.assertEqual(paramiko_server.shell_configuration, {})
        self.assertEqual(paramiko_server.ssh_banner, "FakeNOS Paramiko SSH Server")
        self.assertEqual(paramiko_server.username, self.arguments["username"])
        self.assertEqual(paramiko_server.password, self.arguments["password"])
        self.assertEqual(paramiko_server.port, self.arguments["port"])
        self.assertEqual(paramiko_server.address, "127.0.0.2")
        self.assertEqual(paramiko_server.timeout, 1)
        self.assertEqual(paramiko_server.watchdog_interval, 1)
        # pylint: disable=protected-access
        self.assertEqual(
            paramiko_server._ssh_server_key,
            paramiko.RSAKey(file_obj=io.StringIO(DEFAULT_SSH_KEY)),
        )

    def test_init_with_timeout(self):
        """
        Check that the ParamikoSshServer object is initialized correctly with
        the timeout parameter.
        """
        paramiko_server: ParamikoSshServer = ParamikoSshServer(
            **self.arguments,
            timeout=2,
        )
        self.assertEqual(paramiko_server.nos, self.arguments["nos"])
        self.assertEqual(paramiko_server.nos_inventory_config, self.arguments["nos_inventory_config"])
        self.assertEqual(paramiko_server.shell, self.arguments["shell"])
        self.assertEqual(paramiko_server.shell_configuration, {})
        self.assertEqual(paramiko_server.ssh_banner, "FakeNOS Paramiko SSH Server")
        self.assertEqual(paramiko_server.username, self.arguments["username"])
        self.assertEqual(paramiko_server.password, self.arguments["password"])
        self.assertEqual(paramiko_server.port, self.arguments["port"])
        self.assertEqual(paramiko_server.address, "127.0.0.1")
        self.assertEqual(paramiko_server.timeout, 2)
        self.assertEqual(paramiko_server.watchdog_interval, 1)
        # pylint: disable=protected-access
        self.assertEqual(
            paramiko_server._ssh_server_key,
            paramiko.RSAKey(file_obj=io.StringIO(DEFAULT_SSH_KEY)),
        )

    def test_init_with_watchdog_interval(self):
        """
        Check that the ParamikoSshServer object is initialized correctly with
        the watchdog_interval parameter.
        """
        paramiko_server: ParamikoSshServer = ParamikoSshServer(
            **self.arguments,
            watchdog_interval=2,
        )
        self.assertEqual(paramiko_server.nos, self.arguments["nos"])
        self.assertEqual(paramiko_server.nos_inventory_config, self.arguments["nos_inventory_config"])
        self.assertEqual(paramiko_server.shell, self.arguments["shell"])
        self.assertEqual(paramiko_server.shell_configuration, {})
        self.assertEqual(paramiko_server.ssh_banner, "FakeNOS Paramiko SSH Server")
        self.assertEqual(paramiko_server.username, self.arguments["username"])
        self.assertEqual(paramiko_server.password, self.arguments["password"])
        self.assertEqual(paramiko_server.port, self.arguments["port"])
        self.assertEqual(paramiko_server.address, "127.0.0.1")
        self.assertEqual(paramiko_server.timeout, 1)
        self.assertEqual(paramiko_server.watchdog_interval, 2)
        # pylint: disable=protected-access
        self.assertEqual(
            paramiko_server._ssh_server_key,
            paramiko.RSAKey(file_obj=io.StringIO(DEFAULT_SSH_KEY)),
        )

    def test_init_with_all_parameters(self):
        """
        Check that the ParamikoSshServer object is initialized correctly with
        all the parameters.
        """
        paramiko_server: ParamikoSshServer = ParamikoSshServer(
            **self.arguments,
            ssh_banner="SSH Banner",
            shell_configuration={"shell": "configuration"},
            address="127.0.0.2",
            timeout=2,
            watchdog_interval=2,
        )
        self.assertEqual(paramiko_server.nos, self.arguments["nos"])
        self.assertEqual(paramiko_server.nos_inventory_config, self.arguments["nos_inventory_config"])
        self.assertEqual(paramiko_server.shell, self.arguments["shell"])
        self.assertEqual(paramiko_server.shell_configuration, {"shell": "configuration"})
        self.assertEqual(paramiko_server.ssh_banner, "SSH Banner")
        self.assertEqual(paramiko_server.username, self.arguments["username"])
        self.assertEqual(paramiko_server.password, self.arguments["password"])
        self.assertEqual(paramiko_server.port, self.arguments["port"])
        self.assertEqual(paramiko_server.address, "127.0.0.2")
        self.assertEqual(paramiko_server.timeout, 2)
        self.assertEqual(paramiko_server.watchdog_interval, 2)
        # pylint: disable=protected-access
        self.assertEqual(
            paramiko_server._ssh_server_key,
            paramiko.RSAKey(file_obj=io.StringIO(DEFAULT_SSH_KEY)),
        )

    def test_watchdog_run_srv_loop(self):
        """Check that the watchdog run_srv loop is executed."""
        paramiko_server: ParamikoSshServer = ParamikoSshServer(**self.arguments, watchdog_interval=0.01)
        mock_is_running: Mock = Mock()
        mock_run_srv: Mock = Mock()
        mock_session: Mock = Mock()
        mock_shell: Mock = Mock()
        mock_run_srv.is_set.side_effect = [True, False]
        paramiko_server.watchdog(mock_is_running, mock_run_srv, mock_session, mock_shell)
        self.assertEqual(mock_run_srv.is_set.call_count, 2)

    def test_watchdog_session_is_not_alive(self):
        """Check that the watchdog session is not alive."""
        paramiko_server: ParamikoSshServer = ParamikoSshServer(**self.arguments, watchdog_interval=0.01)
        mock_is_running: Mock = Mock()
        mock_run_srv: Mock = Mock()
        mock_session: Mock = Mock()
        mock_shell: Mock = Mock()
        mock_session.is_alive.return_value = False
        paramiko_server.watchdog(mock_is_running, mock_run_srv, mock_session, mock_shell)
        mock_session.is_alive.assert_called_once()
        mock_run_srv.is_set.assert_called_once()
        mock_shell.stop.assert_called_once()

    def test_watchdog_shell_stop_when_is_running_false(self):
        """Check that the watchdog shell is stopped when is_running is False."""
        paramiko_server: ParamikoSshServer = ParamikoSshServer(**self.arguments, watchdog_interval=0.01)
        mock_is_running: Mock = Mock()
        mock_run_srv: Mock = Mock()
        mock_session: Mock = Mock()
        mock_shell: Mock = Mock()
        mock_run_srv.is_set.side_effect = [True] * 2 + [False]
        mock_is_running.is_set.side_effect = [True] * 1 + [False]
        paramiko_server.watchdog(mock_is_running, mock_run_srv, mock_session, mock_shell)
        mock_shell.stop.assert_called_once()

    def test_watchdog_shell_stop_when_session_is_alive_false(self):
        """Check that the watchdog shell is stopped when the session is alive is False."""
        paramiko_server: ParamikoSshServer = ParamikoSshServer(**self.arguments, watchdog_interval=0.01)
        mock_is_running: Mock = Mock()
        mock_run_srv: Mock = Mock()
        mock_session: Mock = Mock()
        mock_shell: Mock = Mock()
        mock_session.is_alive.side_effect = [True] * 1 + [False]
        paramiko_server.watchdog(mock_is_running, mock_run_srv, mock_session, mock_shell)
        mock_shell.stop.assert_called_once()

    # pylint: disable=unused-argument
    @mock.patch("fakenos.plugins.servers.ssh_server_paramiko.channel_to_shell_tap")
    @mock.patch("fakenos.plugins.servers.ssh_server_paramiko.shell_to_channel_tap")
    @mock.patch("paramiko.Transport")
    def test_connection_function(
        self,
        mock_transport: MagicMock,
        mock_shell_to_channel_tap: MagicMock,
        mock_channel_to_shell_tap: MagicMock,
    ):
        """Check that the connection function is executed correctly."""
        mock_client: MagicMock = MagicMock()
        mock_is_running = Mock()
        paramiko_server: ParamikoSshServer = ParamikoSshServer(**self.arguments)
        paramiko_server.connection_function(mock_client, mock_is_running)

        mock_transport.assert_called_once()
        mock_shell_to_channel_tap.assert_called_once()
        mock_channel_to_shell_tap.assert_called_once()
