from cmd import Cmd
import logging
import time
import traceback
import copy

log = logging.getLogger(__name__)


class CMDShell(Cmd):
    """"""

    use_rawinput = False

    commands = {
        "exit": {"output": True, "help": "Exit commands shell"},
        "_default_": {
            "output": "Unknown command",
            "help": "Output to print for unknown commands",
        },
    }

    def __init__(
        self,
        stdin,
        stdout,
        nos,
        nos_inventory_config,
        base_prompt,
        is_running,
        intro="Custom SSH Shell",
        ruler="",
        completekey="tab",
        newline="\r\n",
    ):
        self.nos = nos
        self.ruler = ruler
        self.intro = intro
        self.base_prompt = base_prompt
        self.newline = newline
        self.prompt = nos.initial_prompt.format(base_prompt=base_prompt)
        self.is_running = is_running

        # form commands
        self.commands = {
            **copy.deepcopy(self.commands),
            **copy.deepcopy(nos.commands or {}),
            **copy.deepcopy(nos_inventory_config.get("commands", {})),
        }

        # call the base constructor of cmd.Cmd, with our own stdin and stdout
        super(CMDShell, self).__init__(
            completekey=completekey,
            stdin=stdin,
            stdout=stdout,
        )

    def start(self):
        self.cmdloop()

    def stop(self):
        self.stdin.write("exit" + self.newline)

    def writeline(self, value):
        for line in str(value).splitlines():
            self.stdout.write(line + self.newline)

    def emptyline(self):
        """This method to do nothing if empty line entered"""
        pass

    def precmd(self, line):
        return line

    def postcmd(self, stop, line):
        return stop

    def do_help(self, *args):
        """Method to return help for commands"""
        lines = {}  # dict of {cmd: cmd_help}
        width = 0  # record longest command width for padding
        cmd_string = " ".join(args)
        # form help for all commands
        for cmd, cmd_data in self.commands.items():
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

    def _check_prompt(self, prompt_):
        """
        Helper method to check if prompt_ matches current prompt

        :param prompt_: (string or None)  prompt to check
        """
        # prompt_ is None if no 'prompt' key defined for command
        if prompt_ is None:
            return True
        if isinstance(prompt_, str):
            return self.prompt == prompt_.format(base_prompt=self.base_prompt)
        if isinstance(prompt_, list):
            return any(
                self.prompt == i.format(base_prompt=self.base_prompt) for i in prompt_
            )

    def default(self, command):
        """Method called if no do_xyz methods found"""
        log.debug("shell.default '{}' running command '{}'".format(self.base_prompt, [command]))
        ret = self.commands["_default_"]["output"]
        try:
            cmd_data = self.commands[command]
            # check of command is alis to other command definition
            if "alias" in cmd_data:
                cmd_data = {**self.commands[cmd_data.pop("alias")], **cmd_data}
            # check current prompt and work with command output
            if self._check_prompt(cmd_data.get("prompt")):
                ret = cmd_data["output"]
                if callable(ret):
                    ret = ret(
                        base_prompt=self.base_prompt,
                        current_prompt=self.prompt,
                        command=command,
                    )
                    # handle the case when callable return dictionary
                    if isinstance(ret, dict):
                        if "new_prompt" in ret:
                            self.prompt = ret["new_prompt"].format(
                                base_prompt=self.base_prompt
                            )
                        ret = ret["output"]
                if "new_prompt" in cmd_data:
                    self.prompt = cmd_data["new_prompt"].format(
                        base_prompt=self.base_prompt
                    )
        except KeyError:
            log.error("shell.default '{}' command '{}' not found".format(self.base_prompt, [command]))
            pass
        except:
            ret = traceback.format_exc()
            ret = ret.replace("\n", self.newline)

        # returning True will close the shell
        if ret is True:
            return True
        # if not None, write output to stdout
        elif ret is not None:
            ret = ret.format(
                base_prompt=self.base_prompt
            )
            self.writeline(ret)
