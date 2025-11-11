"""
NOS module for Huawei SmartAX
"""

# import time
# import os
from typing import List

from fakenos.plugins.nos.platforms_py.base_template import BaseDevice

NAME: str = "huawei_smartax"
INITIAL_PROMPT: str = "{base_prompt}>"
ENABLE_PROMPT: str = "{base_prompt}#"
CONFIG_PROMPT: str = "{base_prompt}(config)#"
DEVICE_NAME: str = "HuaweiSmartAX"

DEFAULT_CONFIGURATION: str = "fakenos/plugins/nos/platforms_py/configurations/huawei_smartax.yaml.j2"


class HuaweiSmartAX(BaseDevice):
    """
    Class that keeps track of the state of the Huawei SmartAX device.
    """

    def _add_whitespaces(self, column: List[str]):
        """
        Add whitespacing to a column depending on the
        largest element in the column.
        """
        max_length = max(len(str(row)) for row in column)
        return [str(row).ljust(max_length) for row in column]

    def make_display_board(self, base_prompt, current_prompt, command):
        "Return String of board information"
        titles = [
            "SlotID",
            "BoardName",
            "Status",
            "SubType0",
            "SubType1",
            "Online/Offline",
        ]
        boards = []
        for board in range(self.configurations["boards"]["num"]):
            boards.append(
                {
                    titles[0]: self.configurations["boards"]["slots"][board]["slot_id"],
                    titles[1]: self.configurations["boards"]["slots"][board]["boardname"],
                    titles[2]: self.configurations["boards"]["slots"][board]["status"],
                    titles[3]: self.configurations["boards"]["slots"][board]["subtype0"],
                    titles[4]: self.configurations["boards"]["slots"][board]["subtype1"],
                    titles[5]: self.configurations["boards"]["slots"][board]["online_offline"],
                }
            )
        for index, title in enumerate(titles):
            board_column = [board[title] for board in boards]
            results = self._add_whitespaces([title, *board_column])
            board_column = results[1:]
            titles[index] = results[0]
            for board in boards:
                board[title] = board_column[boards.index(board)]
        rows = [list(board.values()) for board in boards]
        return self.render("huawei_smartax/display_board.j2", titles=titles, rows=rows)

    def _return(self, base_prompt, current_prompt, command):
        "Return to user prompt"
        if current_prompt.endswith(">"):
            return {"output": "", "new_prompt": INITIAL_PROMPT}
        if current_prompt.endswith("#"):
            return {"output": "", "new_prompt": ENABLE_PROMPT}
        return {"output": "", "new_prompt": INITIAL_PROMPT}

    def quit(self, base_prompt, current_prompt, command):
        "Exit from device"
        return True

    def disable(self, base_prompt, current_prompt, command):
        "Exit exec prompt"
        if current_prompt.endswith("#"):
            return {"output": "", "new_prompt": INITIAL_PROMPT}
        return {"output": "", "new_prompt": current_prompt}


commands = {
    "enable": {
        "output": None,
        "new_prompt": ENABLE_PROMPT,
        "help": "enter exec prompt",
        "prompt": INITIAL_PROMPT,
    },
    "undo smart": {
        "output": None,
        "help": "undo smart command",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT],
    },
    "infoswitch cli OFF": {
        "output": None,
        "help": "turn off infoswitch cli",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT],
    },
    "return": {
        "output": HuaweiSmartAX._return,
        "help": "return to user prompt",
        "prompt": ENABLE_PROMPT,
    },
    "scroll": {
        "output": None,
        "help": "set scroll",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT],
    },
    "disable": {
        "output": HuaweiSmartAX.disable,
        "help": "exit exec prompt",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT],
    },
    "display board": {
        "output": HuaweiSmartAX.make_display_board,
        "help": "display board information",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT],
    },
    "quit": {
        "output": HuaweiSmartAX.quit,
        "help": "exit from device",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT],
    },
}
