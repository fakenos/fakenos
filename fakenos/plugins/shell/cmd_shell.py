from cmd import Cmd
import logging
import time
import traceback

log = logging.getLogger(__name__)


class CMDShell(Cmd):

    use_rawinput = False

    commands = {
        "exit": {"output": True, "help": "exist commands shell"},
        "default": {
            "output": "Uncknown command",
            "help": "Output to print for uncknown commands",
        },
    }

    def __init__(
        self,
        stdin,
        stdout,
        nos,
        base_prompt,
        intro="Custom SSH Shell",
        ruler="",
        completekey="tab",
    ):
        self.nos = nos
        self.ruler = ruler
        self.intro = intro
        self.base_prompt = base_prompt
        self.prompt = nos.initial_prompt.format(base_prompt=base_prompt)
        self.commands.update(nos.commands or {})

        # call the base constructor of cmd.Cmd, with our own stdin and stdout
        super(CMDShell, self).__init__(
            completekey=completekey,
            stdin=stdin,
            stdout=stdout,
        )

    def start(self):
        self.cmdloop()

    def stop(self):
        return True

    def writeline(self, value):
        for line in str(value).splitlines():
            self.stdout.write(line + "\r\n")

    def emptyline(self):
        self.stdout.write("")

    def precmd(self, line):
        return line

    def postcmd(self, stop, line):
        return stop

    def default(self, command):
        """ Method called if no do_xyz methods found """
        log.debug("shell.run_command running command '{}'".format(command))
        try:
            cmd_data = self.commands[command]
            ret = cmd_data["output"]
            if callable(ret):
                ret = ret(
                    base_prompt=self.base_prompt, 
                    current_prompt=self.prompt, 
                    command=command,
                )
            if "new_prompt" in cmd_data:
                self.prompt = cmd_data["new_prompt"].format(base_prompt=self.base_prompt)
        except KeyError:
            try:
                if self.commands.get("default"):
                    ret = self.commands["default"]["output"]
                    if callable(ret):
                        ret = ret(
                            base_prompt=self.base_prompt, 
                            current_prompt=self.prompt, 
                            command=command,
                        )
                else:
                    ret = "Undefined command"
            except:
                ret = traceback.format_exc()
                ret = ret.replace("\n", "\r\n")
        except:
            ret = traceback.format_exc()
            ret = ret.replace("\n", "\r\n")

        # returning True will close the shell
        if ret is True:
            return True
        # if not None, wite output to stdout
        elif ret is not None:
            self.writeline(ret)
