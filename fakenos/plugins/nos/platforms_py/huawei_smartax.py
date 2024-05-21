"""
NOS module for Huawei SmartAX
"""

# import time
import os
from typing import List
from fakenos.plugins.nos.platforms_py.base_template import BaseDevice


NAME: str = "huawei_smartax"
INITIAL_PROMPT: str = "{base_prompt}>"
ENABLE_PROMPT: str = "{base_prompt}#"
CONFIG_PROMPT: str = "{base_prompt}(config)#"
DEVICE_NAME: str = "HuaweiSmartAX"

DEFAULT_CONFIGURATION: str = "huawei_smartax.yaml.j2"


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
        titles = ["SlotID", "BoardType", "Status", "SubType0", "SubType1", "Online/Offline"]
        boards = []
        for board in range(self.configurations["boards"]["num"]):
            boards.append({
                "SlotID": self.configurations["boards"]["slots"][board]["slot_id"],
                "BoardName": self.configurations["boards"]["slots"][board]["boardname"],
                "Status": self.configurations["boards"]["slots"][board]["status"],
                "SubType0": self.configurations["boards"]["slots"][board]["subtype0"],
                "SubType1": self.configurations["boards"]["slots"][board]["subtype1"],
                "Online/Offline": self.configurations["boards"]["slots"][board]["online_offline"],
            })
        for index, title in enumerate(titles):
            board_column = [board[title] for board in boards]
            results = self._add_whitespaces([title] + board_column)
            title = results[0]
            board_column = results[1:]
            titles[index] = title
            for i, board in enumerate(boards):
                board[title] = board_column[i]
        return self.render("huawei_smartax/display_board.j2", boards=boards)


commands = {
    "enable": {
        "output": None,
        "new_prompt": ENABLE_PROMPT,
        "help": "enter exec prompt",
        "prompt": INITIAL_PROMPT,
    },
    "display board": {
        "output": HuaweiSmartAX.make_display_board,
        "help": "display board information",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT],
    },
}
