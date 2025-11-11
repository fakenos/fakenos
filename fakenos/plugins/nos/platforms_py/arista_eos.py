"""
NOS module for Arista EOS
"""

import time

from fakenos.plugins.nos.platforms_py.base_template import BaseDevice

NAME: str = "arista_eos"
INITIAL_PROMPT: str = "{base_prompt}>"
ENABLE_PROMPT: str = "{base_prompt}#"
CONFIG_PROMPT: str = "{base_prompt}(config)#"
DEVICE_NAME: str = "AristaEOS"

DEFAULT_CONFIGURATION: str = "fakenos/plugins/nos/platforms_py/configurations/arista_eos.yaml.j2"


# pylint: disable=unused-argument
class AristaEOS(BaseDevice):
    """
    Class that keeps track of the state of the Arista EOS device.
    """

    def make_show_clock(self, base_prompt, current_prompt, command):
        """Return the current time."""
        return self.render("arista_eos/show_clock.j2", time=time.strftime("%a %b %d %H:%M:%S %Y"))

    def make_exit(self, base_prompt, current_prompt, command):
        """Exit the current level of the CLI."""
        initial_prompt = INITIAL_PROMPT.format(base_prompt=base_prompt)
        enable_prompt = ENABLE_PROMPT.format(base_prompt=base_prompt)
        config_prompt = CONFIG_PROMPT.format(base_prompt=base_prompt)
        if current_prompt in [initial_prompt, enable_prompt]:
            return True  # close session
        if current_prompt in config_prompt:
            return {"output": "", "new_prompt": ENABLE_PROMPT}
        raise RuntimeError(f"make_exit does not know how to handle '{current_prompt}' prompt")

    def make_running_configuration(self, base_prompt, current_prompt, command):
        """Return the running configuration."""
        return self.render("arista_eos/show_running-config.j2", base_prompt=base_prompt)

    def make_show_ip_int_br(self, base_prompt, current_prompt, command):
        """Return the IP interface brief output."""
        return self.render("arista_eos/show_ip_int_br.j2", base_prompt=base_prompt)

    def make_show_running_config(self, base_prompt, current_prompt, command):
        """Return the running configuration."""
        return self.render("arista_eos/show_running-config.j2", base_prompt=base_prompt)

    def make_show_version(self, base_prompt, current_prompt, command):
        """Return the system version."""
        return self.render("arista_eos/show_version.j2", base_prompt=base_prompt)


commands = {
    "enable": {
        "output": None,
        "new_prompt": ENABLE_PROMPT,
        "help": "Enable commands for a specified privilege level",
        "prompt": INITIAL_PROMPT,
    },
    "show clock": {
        "output": AristaEOS.make_show_clock,
        "help": "System time",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT],
    },
    "show running-config": {
        "output": AristaEOS.make_show_running_config,
        "help": "System running configuration",
        "prompt": ENABLE_PROMPT,
    },
    "show version": {
        "output": AristaEOS.make_show_version,
        "help": "Software and hardware versions",
        "prompt": ENABLE_PROMPT,
    },
    "_default_": {
        "output": "% Invalid input",
        "help": "Output to print for unknown commands",
        "prompt": [ENABLE_PROMPT, INITIAL_PROMPT],
    },
    "terminal width 511": {
        "output": "Width set to 511 columns.",
        "help": "Configure the terminal width to 511",
        "prompt": [ENABLE_PROMPT, INITIAL_PROMPT],
    },
    "term width 0": {
        "alias": "terminal width 511",
    },
    "terminal length 0": {
        "output": "Pagination disabled.",
        "help": "Configure the pagination length to 0",
        "prompt": [ENABLE_PROMPT, INITIAL_PROMPT],
    },
    "term length 0": {"alias": "terminal length 0"},
    "show ip int brief": {
        "output": AristaEOS.make_show_ip_int_br,
        "help": "Condensed output",
        "prompt": [ENABLE_PROMPT, INITIAL_PROMPT],
    },
    "show ip interface brief": {
        "output": AristaEOS.make_show_ip_int_br,
        "help": "Condensed output",
        "prompt": [ENABLE_PROMPT, INITIAL_PROMPT],
    },
    "conf t": {
        "prompt": ENABLE_PROMPT,
        "output": None,
        "new_prompt": CONFIG_PROMPT,
        "help": "Config mode",
    },
    "config term": {"alias": "conf t"},
    "configure terminal": {"alias": "conf t"},
    "do show ip int brief": {"alias": "show ip int brief", "prompt": CONFIG_PROMPT},
    "exit": {
        "output": AristaEOS.make_exit,
        "help": "Leave Exec mode",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT, CONFIG_PROMPT],
    },
    "show hostname": {
        "output": """Hostname: {{base_prompt}}
FQDN:     {{base_prompt}}""",
        "help": "Show the system hostname",
        "prompt": ENABLE_PROMPT,
    },
    "no logging console": {
        "output": "",
        "help": "Set console logging parameters",
        "prompt": CONFIG_PROMPT,
    },
    "end": {
        "output": "",
        "help": "Leave config mode",
        "new_prompt": ENABLE_PROMPT,
        "prompt": CONFIG_PROMPT,
    },
}
