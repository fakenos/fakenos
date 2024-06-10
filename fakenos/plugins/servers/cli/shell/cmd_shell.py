"""
Custom shell class to interact with NOS.
"""

from cmd import Cmd
import logging
import traceback
import copy
import os
from typing import List, Tuple, Union
import re

from fakenos.core.nos import Nos
from fakenos.plugins import nos

from fakenos.plugins.nos.cli.base_template import NosCLI
from fakenos.plugins.servers.cli.shell.utils import get_files_changed

log = logging.getLogger(__name__)

BASIC_COMMANDS: dict = {
    "exit": {"output": True, "help": "Exit commands shell"},
    "_default_": {
        "output": "Unknown command",
        "help": "Output to print for unknown commands",
    },
}


# pylint: disable=too-many-instance-attributes
class CMDShell(Cmd):
    """
    Custom shell class to interact with NOS.
    """

    use_rawinput = False

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        stdin,
        stdout,
        nos: Nos,
        base_prompt,
        is_running,
        intro="Custom SSH Shell",
        ruler="",
        completekey="tab",
        newline="\r\n",
    ):
        self.nos: Nos = nos
        self.nos_cli: NosCLI = NosCLI.get_nos(nos)
        self.ruler = ruler
        self.intro = intro
        self.base_prompt = base_prompt
        self.newline = newline
        # self.prompt = nos.initial_prompt.format(base_prompt=base_prompt)
        self.is_running = is_running

        # form commands
        self.commands = {
            **copy.deepcopy(BASIC_COMMANDS),
            **copy.deepcopy(nos_cli.commands or {}),
        }

        self.commands = self.get_commands_formatted()

        # call the base constructor of cmd.Cmd, with our own stdin and stdout
        super().__init__(
            completekey=completekey,
            stdin=stdin,
            stdout=stdout,
        )

    def get_commands_formatted(self):
        """ Method to transform the command to the correct format """
        default = self.commands.pop("_default_", {})
        commands = {command.replace("[", "(").replace("]", ")?"): value for command, value in self.commands.items()}
        commands = {command.replace("\\S+", "(.*)"): value for command, value in commands.items()}
        commands = {re.compile(command): value for command, value in commands.items()}
        commands["_default_"] = default
        return commands

    def start(self):
        """Method to start the shell"""
        self.cmdloop()

    def stop(self):
        """Method to stop the shell"""
        self.stdin.write("exit" + self.newline)

    def writeline(self, value):
        """Method to write a line to stdout with newline at the end"""
        for line in str(value).splitlines():
            self.stdout.write(line + self.newline)

    def emptyline(self):
        """This method to do nothing if empty line entered"""

    def reload_commands(self, changed_files: list):
        """Method to reload commands"""
        for file in changed_files:
            # self.nos.from_file(file)
            self.commands.clear()
            # self.commands.update(self.nos.commands)
            self.commands = self.get_commands_formatted()

    def precmd(self, line):
        """Method to return line before processing the command"""
        if os.environ.get("FAKENOS_RELOAD_COMMANDS"):
            changed_files = get_files_changed(nos.__path__[0])
            if changed_files:
                log.debug("Reloading... Files changed: %s", changed_files)
                self.reload_commands(changed_files)
        return line

    # pylint: disable=unused-argument
    def postcmd(self, stop, line):
        """Method to return stop value to stop the shell"""
        return stop

    # pylint: disable=unused-argument
    def do_help(self, arg):
        """Method to return help for commands"""
        lines = {}  # dict of {cmd: cmd_help}
        width = 0  # record longest command width for padding
        # form help for all commands
        for regex, cmd_data in self.commands.items():
            cmd = self._get_command_name(regex)
            # skip special commands
            if cmd.startswith("_") and cmd.endswith("_"):
                continue
            # skip commands that does not match current prompt
            if not self._check_prompt(cmd_data.get("prompt")):
                continue
            lines[cmd] = cmd_data.get("help", "")
            width = max(width, len(cmd))
        # form help lines
        help_msg = []
        for k, v in lines.items():
            padding = " " * (width - len(k)) + "  "
            help_msg.append(f"{k}{padding}{v}")
        self.writeline(self.newline.join(help_msg))

    def _get_command_name(self, regex):
        """Method to get the command name from regex"""
        if isinstance(regex, str):
            return regex
        pattern: str = regex.pattern
        command = pattern.replace("(","")
        command = command.replace("?","")
        command = command.replace(")","")
        command = command.replace(".*","")
        return command.strip()

    def _check_prompt(self, prompt_: Union[str, List[str]]):
        """
        Helper method to check if prompt_ matches current prompt

        :param prompt_: (string or None)  prompt to check
        """
        # prompt_ is None if no 'prompt' key defined for command
        if prompt_ is None:
            return True
        if isinstance(prompt_, str):
            return self.prompt == prompt_.format(base_prompt=self.base_prompt)
        return any(self.prompt == i.format(base_prompt=self.base_prompt) for i in prompt_)

    def get_match_command_and_args(self, line: str) -> Union[Tuple[str, List], Tuple[None, None]]:
        """ Method that checks if the line matches any regex """
        commands = {k: v for k, v in self.commands.items() if not isinstance(k, str)}
        for regex, cmd in commands.items():
            found = regex.search(line)
            if not found:
                continue
            args = None
            if found.groups():
                args = found.groups()[-1]
            return cmd, args
        raise KeyError

    def get_command_response(self, line):
        """ Method that handles the execution and response of the command """
        response = self.commands["_default_"]["output"]
        try:
            cmd_data, args = self.get_match_command_and_args(line)
            if not self._check_prompt(cmd_data.get("prompt")):
                log.warning(
                    "'%s' command prompt '%s' not matching current prompt '%s'",
                    line,
                    (
                        ", ".join(cmd_data.get("prompt", []))
                        if isinstance(cmd_data.get("prompt"), list)
                        else cmd_data.get("prompt", "")
                    ),
                    self.prompt,
                )
                return response
            response = cmd_data["output"]
            if callable(response):
                response = response(
                    # self.nos.device,
                    base_prompt=self.base_prompt,
                    current_prompt=self.prompt,
                    args=args,
                )
                if isinstance(response, dict):
                    if "new_prompt" in response:
                        self.prompt = response["new_prompt"].format(base_prompt=self.base_prompt)
                    response = response["output"]
            if "new_prompt" in cmd_data:
                self.prompt = cmd_data["new_prompt"].format(base_prompt=self.base_prompt)
        except KeyError:
            log.error("shell.default '%s' command '%s' not found", self.base_prompt, [line])
            if callable(response):
                response = "An error occurred related to the command function"
        # pylint: disable=broad-except
        except ValueError:
            log.error("Output is still a callable")
            response = "An error occurred"
        except (Exception,) as e:
            log.error("An error occurred: %s", str(e))
            response = traceback.format_exc()
            response = response.replace("\n", self.newline)
        return response
    
    def send_response(self, response):
        """ Method to send the response correctly. """
        try:
            final_response = response.format(base_prompt=self.base_prompt)
        except KeyError:
            log.error("Error in formatting output")
        self.writeline(final_response)

    def default(self, line):
        """Method called if no do_xyz methods found"""
        log.debug("shell.default '%s' running command '%s'", self.base_prompt, [line])
        response = self.get_command_response(line)
        if response is True or not self.is_running.is_set():
            # We exit the terminal
            return True
        if response is not None:
            self.send_response(response)
        return False
