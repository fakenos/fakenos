"""
This module contains the base model for any
server implemented as a plugin. To see an example
look for fakenos/plugins/servers/ssh_server_paramiko.py
"""

# pylint: disable=no-name-in-module
from abc import ABC, abstractmethod
import logging
import socket
import sys
import threading
import time
from typing import Optional

log = logging.getLogger(__name__)


# pylint: disable=too-many-instance-attributes
class TCPServerBase(ABC):
    """
    This module provides the base class for a TCP Server.
    It provides the methods to start and stop the server.

    Note: We are looking to switch to socketserver as it is
    the standard library in python.
    """

    def __init__(self, address: str = "localhost", port: int = 6000, timeout: float = 1) -> None:
        """
        Initialize the server with the address and port
        and the timeout for the socket.
        """
        self.address = address
        self.port = port
        self.timeout = timeout
        self._is_running = threading.Event()
        self._socket: Optional[socket.socket] = None
        self.client_shell = None
        self._listen_thread: Optional[threading.Thread] = None
        self._connection_threads: list[threading.Thread] = []

    def start(self) -> None:
        """
        Start Server which distributes the connections.
        It handles the creation of the socket, binding to the address and port,
        and starting the listening thread.
        """
        if self._is_running.is_set():
            return

        try:
            self._bind_sockets()
        except Exception:
            if self._socket is not None:
                self._socket.close()
                self._socket = None
            raise
        self._is_running.set()
        self._listen_thread = threading.Thread(target=self._listen)
        self._listen_thread.start()

    def _get_shutdown_timeout(self) -> float:
        """Return the total time allowed for this server's workers to stop."""
        return max(float(self.timeout or 1), 1.0)

    def _close_active_connections(self) -> None:
        """Allow server plugins to unblock active connection workers."""

    def _bind_sockets(self) -> None:
        """
        It binds the sockets to the corresponding IPs and Ports.
        In Linux and OSX it reuses the port if needed but
        not in Windows
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        reuse_port = getattr(socket, "SO_REUSEPORT", None)
        if sys.platform == "linux" and reuse_port is not None:
            self._socket.setsockopt(socket.SOL_SOCKET, reuse_port, True)

        self._socket.settimeout(self.timeout)
        self._socket.bind((self.address, self.port))

    def stop(self) -> None:
        """
        It stops the server joining the threads
        and closing the corresponding sockets.
        """
        if not self._is_running.is_set():
            return

        shutdown_deadline = time.monotonic() + self._get_shutdown_timeout()
        self._is_running.clear()
        try:
            if self._socket is not None:
                self._socket.close()
            self._close_active_connections()
        finally:
            if self._listen_thread is not None:
                self._listen_thread.join(timeout=max(0.0, shutdown_deadline - time.monotonic()))

            for connection_thread in self._connection_threads:
                connection_thread.join(timeout=max(0.0, shutdown_deadline - time.monotonic()))

            self._connection_threads = [thread for thread in self._connection_threads if thread.is_alive()]
            if self._listen_thread is not None and not self._listen_thread.is_alive():
                self._listen_thread = None
            self._socket = None

    def _listen(self) -> None:
        """
        This function is constantly running if the server is running.
        It waits for a connection, and if a connection is made, it will
        call the connection function.
        """
        listener = self._socket
        if listener is None:
            return
        listener.listen()
        while self._is_running.is_set():
            try:
                client, _ = listener.accept()
                connection_thread = threading.Thread(
                    target=self.connection_function,
                    args=(
                        client,
                        self._is_running,
                    ),
                )
                connection_thread.start()
                self._connection_threads.append(connection_thread)
            except socket.timeout:
                pass
            except OSError:
                if self._is_running.is_set():
                    log.exception("TCP server listener stopped after a socket error")
                break

    @abstractmethod
    def connection_function(self, client: socket.socket, is_running: threading.Event) -> None:
        """
        This abstract method it is called when a new connection
        is made. The implementation should handle all the
        latter connection.
        """
