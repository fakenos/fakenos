"""
This module handles is the base model for any
server implemented as a plugin. To see an example
look for fakenos/plugins/servers/ssh_server_paramiko.py
"""

# pylint: disable=no-name-in-module
from abc import ABC, abstractmethod
import sys
import socket
import threading
import logging

log = logging.getLogger(__name__)


class TCPServerBase(ABC):
    """
    Base class to host common TCP server methods.
    """

    def __init__(self):
        """
        Initialize the server instance.

        Attributes:
        _is_running: A multithreaded event, which is a thread-safe boolean.
        _socket: A socket used to listen to incoming connections.
        client_shell: The shell for the connected client. It is not initialized yet,
                    since we need to get the stdin and stdout objects after the connection is made.
        _listen_thread: The thread that will listen for incoming connections and data.
        _connection_threads: A list of active connections maintained by this server.
        address: It is the address to which the device will be listening to.
        port: It is the port to which the device will be listening to.
        timeout: The time after which
        """
        self._is_running = threading.Event()
        self._socket = None
        self.client_shell = None
        self._listen_thread = None
        self._connection_threads: list = []

    def start(self):
        """
        Start Server which distributes the connections.
        It handles the creation of the socket, binding to the address and port,
        and starting the listening thread.
        """
        if self._is_running.is_set():
            return

        self._is_running.set()

        self._bind_sockets()

        self._listen_thread = threading.Thread(target=self._listen)
        self._listen_thread.start()

    def _bind_sockets(self):
        """
        It binds the sockets to the corresponding IPs and Ports.
        In Linux and OSX it reuses the port if needed but
        not in Windows
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        if sys.platform in ["linux"]:
            self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, True)

        self._socket.settimeout(self.timeout)
        self._socket.bind((self.address, self.port))

    def stop(self):
        """
        It stops the server joining the threads
        and closing the corresponding sockets.
        """
        if not self._is_running.is_set():
            return

        self._is_running.clear()
        self._listen_thread.join()
        self._socket.close()

        for connection_thread in self._connection_threads:
            connection_thread.join()

    def _listen(self):
        """
        This funciton is constantly running if the server is running.
        It waits for a connection, and if a connection is made, it will
        call the connection function.
        """
        while self._is_running.is_set():
            try:
                self._socket.listen()
                client, _ = self._socket.accept()
                connection_thread = threading.Thread(target=self.connection_function, args=(client,))
                connection_thread.start()
                self._connection_threads.append(connection_thread)
            except socket.timeout:
                pass

    @abstractmethod
    def connection_function(self, client):
        """
        This abstract method it is called when a new connection
        is made. The implementation should handle all the
        latter connection.
        """
