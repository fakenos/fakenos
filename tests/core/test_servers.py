"""
Test moudle for fakenos.core.servers.
The file can be found under fakenos/core/servers.py
"""

# pylint: disable=protected-access, attribute-defined-outside-init
import socket
import unittest
from unittest.mock import MagicMock, patch

from fakenos.core.servers import TCPServerBase


class FakeServer(TCPServerBase):
    """
    FakeServer class that inherits from TCPServerBase
    to test the abstract class.
    """

    def __init__(self):
        super().__init__()
        self.timeout = 1
        self.address = "127.0.0.1"
        self.port = 22

    def connection_function(self, client):
        pass


class ServersTest(unittest.TestCase):
    """
    Test class for the TCPServerBase class.
    """

    @patch("threading.Event")
    def test_init(self, mock_thread_event):
        """
        Test that the init method works as
        expected creating the needed threads.
        """
        servers = FakeServer()

        assert servers._is_running == mock_thread_event.return_value
        mock_thread_event.assert_called_once()
        assert servers._socket is None
        assert servers.client_shell is None
        assert servers._listen_thread is None
        assert not servers._connection_threads

    @patch("threading.Event")
    @patch("threading.Thread")
    @patch("fakenos.core.servers.TCPServerBase._bind_sockets")
    def test_start_executed_without_arguments(
        self,
        mock_bind_sockets,
        mock_thread,
        mock_thread_event,
    ):
        """
        It passes if the start can be executed correctly
        if no arguments are given.
        """
        mock_thread_event().is_set.return_value = False

        servers = FakeServer()
        servers.start()

        mock_bind_sockets.assert_called_once()
        mock_thread_event().set.assert_called_once()
        mock_thread.assert_called_once_with(target=servers._listen)
        mock_thread().start.assert_called_once()

    @patch("threading.Event")
    def test_start_does_not_execute_thread_if_running(self, mock_thread_event):
        """
        It passes if the start does not execute the
        thread if the server is already running.
        """
        mock_thread_event().is_set.return_value = True

        servers = FakeServer()
        servers.start()

        mock_thread_event().set.assert_not_called()

    @patch("socket.socket")
    @patch("sys.platform", "linux")
    def test_bind_sockets_works_in_linux(self, mock_socket):
        """
        It passes if the socket is created and the
        setsockopt is called with the right parameters
        in Linux.
        """
        servers = FakeServer()
        servers._bind_sockets()

        mock_socket.assert_called_once_with(socket.AF_INET, socket.SOCK_STREAM)
        mock_socket().setsockopt.assert_any_call(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        mock_socket().setsockopt.assert_any_call(socket.SOL_SOCKET, socket.SO_REUSEPORT, True)
        mock_socket().settimeout.assert_called_once_with(servers.timeout)
        mock_socket().bind.assert_called_once_with((servers.address, servers.port))

    @patch("socket.socket")
    @patch("sys.platform", "darwin")
    def test_bind_sockets_works_in_osx(self, mock_socket):
        """
        It passes if the socket is created and the
        setsockopt is called with the right parameters
        in OSX.
        """
        servers = FakeServer()
        servers._bind_sockets()

        mock_socket.assert_called_once_with(socket.AF_INET, socket.SOCK_STREAM)
        mock_socket().setsockopt.assert_any_call(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        mock_socket().settimeout.assert_called_once_with(servers.timeout)
        mock_socket().bind.assert_called_once_with((servers.address, servers.port))

    @patch("socket.socket")
    @patch("sys.platform", "win32")
    def test_bind_sockets_works_in_windows(self, mock_socket):
        """
        It passes if the socket is created and the
        setsockopt is called with the right parameters
        in Windows.
        """
        servers = FakeServer()
        servers._bind_sockets()

        mock_socket.assert_called_once_with(socket.AF_INET, socket.SOCK_STREAM)
        mock_socket().setsockopt.assert_called_once_with(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        mock_socket().settimeout.assert_called_once_with(servers.timeout)
        mock_socket().bind.assert_called_once_with((servers.address, servers.port))

    @patch("threading.Event")
    def test_stop_works_does_not_stop_if_not_running(self, mock_thread_event):
        """
        It passes if the functions exits correctly when
        the is_running flag is set to false.
        """
        mock_thread_event().is_set.return_value = False

        servers = FakeServer()
        servers.stop()

        mock_thread_event().clear.assert_not_called()

    @patch("threading.Event")
    @patch("threading.Thread")
    @patch("socket.socket")
    def test_stop_works_stop_if_running_is_set(self, mock_socket, mock_thread, mock_thread_event):
        """
        It passes if the functions exits correctly when
        the is_running flag is still set to true.
        """
        self._connection_thread = [MagicMock() for _ in range(3)]
        mock_thread_event().is_set.return_value = True
        servers = FakeServer()
        servers._listen_thread = mock_thread()
        servers._socket = mock_socket()
        servers.stop()

        mock_thread_event().clear.assert_called_once()

    @patch("threading.Event")
    @patch("threading.Thread")
    @patch("socket.socket")
    def test_stop_works_closing_sockets(self, mock_socket, mock_thread, mock_thread_event):
        """
        It passes if the sockets have the close() being
        called.
        """
        mock_thread_event().is_set.return_value = True
        servers = FakeServer()
        servers._listen_thread = mock_thread()
        servers._socket = mock_socket()

        servers.stop()
        mock_socket().close.assert_called_once()

    @patch("threading.Event")
    @patch("threading.Thread")
    @patch("socket.socket")
    def test_stop_works_joining_threads(self, mock_socket, mock_thread, mock_thread_event):
        """
        It passes if the connection threads are joined
        after the program is interrupted.
        """
        self._connection_thread = [MagicMock() for _ in range(3)]
        mock_thread_event().is_set.return_value = True
        servers = FakeServer()
        servers._listen_thread = mock_thread()
        servers._socket = mock_socket()

        servers.stop()
        for connection_thread in servers._connection_threads:
            connection_thread.join.assert_called_once()

    @patch("threading.Event")
    @patch("threading.Thread")
    @patch("socket.socket")
    def test_listen_works_when_new_connection(self, mock_socket, mock_thread, mock_thread_event):
        """
        Test passes if the listening thread opens
        a new thread whenever there is a new connection
        coming in.
        """
        mock_thread_event().is_set.side_effect = [True, False]
        servers = FakeServer()
        servers._socket = mock_socket()
        servers._socket.accept.return_value = (MagicMock(), MagicMock())

        servers._listen()
        mock_socket().listen.assert_called_once()
        mock_socket().accept.assert_called_once()
        mock_thread.assert_called_once_with(
            target=servers.connection_function, args=(mock_socket().accept.return_value[0],)
        )
        mock_thread().start.assert_called_once()
        self.assertEqual(len(servers._connection_threads), 1)

    @patch("threading.Event")
    @patch("threading.Thread")
    @patch("socket.socket")
    def test_listen_socket_timeout_go_back_to_loop(self, mock_socket, mock_thread, mock_thread_event):
        """
        The test passes if the listening thread goes
        back to the loop if the socket timeout is
        reached.
        """
        mock_thread_event().is_set.side_effect = [True, False]
        servers = FakeServer()
        servers._socket = mock_socket()
        servers._socket.accept.side_effect = socket.timeout

        servers._listen()
        mock_socket().listen.assert_called_once()
        mock_socket().accept.assert_called_once()
        mock_thread.assert_not_called()
        self.assertEqual(len(servers._connection_threads), 0)

    @patch("threading.Event")
    @patch("threading.Thread")
    @patch("socket.socket")
    def test_listen_works_all_the_time(self, mock_socket, mock_thread, mock_thread_event):
        """
        Test passes if it detects that it passes at least
        100 times in the while and when there is the
        thread not running anymore stops.
        """
        mock_thread_event().is_set.side_effect = [True] * 100 + [False]
        servers = FakeServer()
        servers._socket = mock_socket()
        servers._socket.accept.return_value = (MagicMock(), MagicMock())
        servers._listen()
        self.assertEqual(mock_socket().listen.call_count, 100)
        self.assertEqual(mock_socket().accept.call_count, 100)
        self.assertEqual(mock_thread.call_count, 100)
        self.assertEqual(mock_thread().start.call_count, 100)
        self.assertEqual(len(servers._connection_threads), 100)
