from abc import ABC, abstractmethod
from sys import platform
import socket, threading
import logging
import traceback

log = logging.getLogger(__name__)


class TCPServerBase(ABC):
    def __init__(self):
        # create a multithreaded event, which is basically a
        # thread-safe boolean
        self._is_running = threading.Event()

        # this socket will be used to listen to incoming connections
        self._socket = None

        # this will contain the shell for the connected client.
        # we don't yet initialize it, since we need to get the
        # stdin and stdout objects after the connection is made.
        self.client_shell = None

        # this will contain the thread that will listen for incoming
        # connections and data.
        self._listen_thread = None

    # To start the server, we open the socket and create
    # the listening thread.
    def start(self, address=None, port=None, timeout=None):
        address = address or self.address
        port = port or self.port
        timeout = timeout or self.timeout

        if not self._is_running.is_set():
            self._is_running.set()

            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

            # reuse port is not avaible on windows
            if platform == "linux" or platform == "linux2":
                self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, True)

            self._socket.settimeout(timeout)
            self._socket.bind((address, port))

            self._listen_thread = threading.Thread(target=self._listen)
            self._listen_thread.start()

    # To stop the server, we must join the listen thread
    # and close the socket.
    def stop(self):
        if self._is_running.is_set():
            self._is_running.clear()
            self._listen_thread.join()
            self._socket.close()

    # The listen function will constantly run if the server is running.
    # We wait for a connection, if a connection is made, we will call
    # our connection function.
    def _listen(self):
        while self._is_running.is_set():
            try:
                self._socket.listen()
                client, addr = self._socket.accept()
                self.connection_function(client)
            except socket.timeout:
                pass

    @abstractmethod
    def connection_function(self, client):
        pass
