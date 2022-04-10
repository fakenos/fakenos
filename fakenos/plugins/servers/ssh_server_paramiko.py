import logging
import paramiko
import io
import threading
import time
import traceback

from fakenos.core.servers import TCPServerBase

log = logging.getLogger(__name__)


class ParamikoSshServerInterface(paramiko.ServerInterface):
    def __init__(
        self,
        ssh_banner="My SSH Server",
        username="user",
        password="user",
    ):
        self.ssh_banner = ssh_banner
        self.username = username
        self.password = password

    # This will allow the SSH server to provide a
    # channel for the client to communicate over.
    # By default, this will return OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED,
    # so  we have to override it to return OPEN_SUCCEEDED
    # when the kind of channel requested is "session".
    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    # AFAIK, pty (pseudo-tty (TeleTYpewriter)) will allow our
    # client to interact with our shell.
    def check_channel_pty_request(
        self, channel, term, width, height, pixelwidth, pixelheight, modes
    ):
        return True

    # This allows us to provide the channel with a shell we can connect to it.
    def check_channel_shell_request(self, channel):
        return True

    # This let's us setup password authentication.
    # There are better ways to do this than using plain text,
    # but for ease of development for me and this tutorial
    # I think plain text is acceptable.
    #
    # For posterity, you could setup a database that encrypts
    # passwords and will grab them to decrypt here.
    def check_auth_password(self, username, password):
        if (username == self.username) and (password == self.password):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    # String that will display when a client connects,
    # before authentication has happened. This is different
    # than the shell's intro property, which is displayed
    # after the authentication.
    def get_banner(self):
        return (self.ssh_banner + "\r\n", "en-US")


class TapIO(io.StringIO):
    """ Class to implement StringIO subclass but with blocking readline method """

    def __init__(self, initial_value="", newline="\n"):
        self.lines = []
        super(TapIO, self).__init__(initial_value, newline)

    def readline(self, size=-1):
        """ readline in indefinite block mode """
        while True:
            if self.lines:
                return self.lines.pop(-1)
            time.sleep(0.01)

    def write(self, value):
        self.lines.insert(0, value)


def channel_to_shell_tap(channel_stdio, shell_stdin):
    buffer = io.BytesIO()
    while True:
        byte = channel_stdio.read(1)
        if byte in (b"\r", b"\n"):
            # echo input back to the client
            channel_stdio.write("\r\n")
            # read line from buffer, clear buffer, send line to cmd shell
            buffer.write(b"\r\n")
            buffer.seek(0)
            line = buffer.read().decode(encoding="utf-8")
            buffer.seek(0)
            buffer.truncate()
            log.debug(
                "ssh_server.channel_to_shell_tap sending line to shell: {}".format(
                    [line]
                )
            )
            shell_stdin.write(line)
        else:
            # echo input back to the client
            channel_stdio.write(byte)
            # safe received character to buffer
            buffer.write(byte)


def shell_to_channel_tap(channel_stdio, shell_stdout):
    while True:
        line = shell_stdout.readline()
        if "\r\n" not in line and "\n" in line:
            line = line.replace("\n", "\r\n")
        log.debug(
            "ssh_server.shell_to_channel_tap sending line to channel {}".format([line])
        )
        channel_stdio.write(line.encode(encoding="utf-8"))


class ParamikoSshServer(TCPServerBase):
    def __init__(
        self,
        shell,
        nos,
        ssh_key_file,
        port,
        ssh_key_file_password=None,
        ssh_banner="My SSH Server",
        shell_configuration=None,
        username="user",
        password="user",
        address="127.0.0.1",
        timeout=1,
    ):
        super(ParamikoSshServer, self).__init__()

        self.nos = nos
        self.shell = shell
        self.shell_configuration = shell_configuration
        self.ssh_banner = ssh_banner
        self.username = username
        self.password = password
        self.port = port
        self.address = address
        self.timeout = timeout

        self._ssh_server_key = paramiko.RSAKey.from_private_key_file(
            ssh_key_file, ssh_key_file_password
        )

    def connection_function(self, client):
        # create the SSH transport object
        session = paramiko.Transport(client)
        session.add_server_key(self._ssh_server_key)

        # create the server
        server = ParamikoSshServerInterface(
            ssh_banner=self.ssh_banner,
            username=self.username,
            password=self.password,
        )

        # start the SSH server
        session.start_server(server=server)

        # create the channel and get the stdio
        channel = session.accept()
        channel_stdio = channel.makefile("rw")

        # create stdio for the shell
        shell_stdin = TapIO()
        shell_stdout = TapIO()

        # start intermidiate thread to tap into the channel_stdio->shell_stdin bytes stream
        channel_to_shell_tapper = threading.Thread(
            target=channel_to_shell_tap, args=(channel_stdio, shell_stdin)
        )
        channel_to_shell_tapper.start()

        # start intermidiate thread to tap into the shell_stdout->channel_stdio bytes stream
        shell_to_channel_tapper = threading.Thread(
            target=shell_to_channel_tap, args=(channel_stdio, shell_stdout)
        )
        shell_to_channel_tapper.start()

        # create the client shell and start it
        self.client_shell = self.shell(
            stdin=shell_stdin,
            stdout=shell_stdout,
            nos=self.nos,
            **self.shell_configuration
        )
        self.client_shell.start()

        # After execution continues, we can close the session
        # since the only way execution will continue from
        # cmdloop() is if we explicitly return True from it,
        # which we do with the exit command.
        session.close()
