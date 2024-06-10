"""
NOS module for Huawei SmartAX
"""

# import time
# import os
import copy
import os
# import re
# import time
from datetime import datetime, timedelta
import random
from typing import Dict, List

from fakenos.plugins.nos.cli.base_template import NosCLI

DEVICE_NAME: str = "HuaweiSmartAX"
INITIAL_PROMPT: str = "{base_prompt}>"
ENABLE_PROMPT: str = "{base_prompt}#"
CONFIG_PROMPT: str = "{base_prompt}(config)#"

# Huawei when doing tables use predefined spacing.
# The spacing corresponds to the largest possible value in the column
# unless the column title is larger than the largest value if there 
# isn't a space in between the title.
# Example:
# F/S/P: 0/ 1/11 (value is larger)
# ONT ID: 0 (title is larger)
FRAME_SPACING: Dict[str, int] = {
    "SlotID": ("left", len(max("SlotID", "0", "1", "2", "3", "4", "5", key=len))),
    "BoardName": ("left", len(max("BoardName", "A123ABCD", key=len))),
    "Status": ("left", len(max("Status", "Normal", "Active_normal", "Standby_failed", key=len))),
    "SubType0": ("left", len(max("SubType0", "CPCF", key=len))),
    "SubType1": ("left", len(max("SubType1", "CPCF", key=len))),
    "Online/Offline": ("left", len(max("Online/Offline", "Offline", "Online", key=len))),
    "F/S/P": ("left", len(max("F/S/P", "0/ 1/1", "0/ 1/11", key=len))),
    "ONT ID": ("right", len(max("ONT", "ID", "1", "11", key=len))),
    "ONT-ID": ("right", len(max("ONT-ID", "1", "11", key=len))),
    "SN": ("center", len(max("SN","1234567890ABCDEF", key=len))),
    "Control flag": ("left", len(max("control", "flag","active", "configuring", key=len))),
    "Config state": ("left", len(max("config", "state", "online", "normal", "failing" ,key=len))),
    "Run state": ("left", len(max("run", "state", "online", "offline", key=len))),
    "Match state": ("left", len(max("match", "state", "initial", "match", "mismatch", key=len))),
    "Protect side": ("left", len(max("protect", "side", "yes", "no", key=len))),
    "Description": ("left", len(max("description", "Generic_description", "The acoustic explanation slaps.", key=len))),
    "Network service": ("left", len(max("network service", "dhcpv6-relay", key=len))),
}

SERVICES_SPACING: Dict[str, int] = {
    "Network service": ("left", len(max("Network service", "dhcpv6-relay", key=len))),
    "Port": ("left", len(max("Port", "4294967295", key=len))),
    "State": ("left", len(max("State", "disable", "enable", key=len))),
}

DBA_PROFILES_SPACING: Dict[str, int] = {
    "Profile-ID": ("right", len(max("Profile-ID", "10", "1", key=len))),
    "Type": ("right", len(max("Type", "1", "2", "3", "4", "5", key=len))),
    "Bandwidth Compensation": ("right", len(max("Bandwidth", "Compensation", "no", "yes", key=len))),
    "Fix (kbps)": ("right", len(max("Fix", "(kbps)", "102400", "10240000", key=len))),
    "Assure (kbps)": ("right", len(max("Assure", "(kbps)", "102400", "10240000", key=len))),
    "Max (kbps)": ("right", len(max("Max", "(kbps)", "102400", "10240000", key=len))),
    "Bind times": ("right", len(max("Bind", "times", "1", "10", key=len))),
}

GPON_BOARDS: Dict[str, int] = {
    'H901XGHDE': 8,
    'H901OGHK': 24,
    'H901NXED': 8,
    'H901OXHD': 8,
    'H902OXHD': 8,
    'H901GPSFE': 16,
    'H901OXEG': 24,
    'H901TWEDE': 8,
    'H901XSHF': 16,
    'H902GPHFE': 16,
}

class HuaweiSmartAX(NosCLI):
    """
    Class that keeps track of the state of the Huawei SmartAX device.
    """
    NAME: str = "huawei_smartax"
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DEFAULT_CONFIGURATION: str = os.path.join(BASE_DIR, "../configurations/huawei_smartax.yaml.j2")
    PYDANTIC_FILE: str = os.path.join(BASE_DIR, "../configurations/pydantic_models/huawei_smartax.py")
    
    SYSTEM_STARTUP_TIME: datetime =  datetime.now() \
            - timedelta(days=random.randint(1, 365),
                                 hours=random.randint(1, 24),
                                 minutes=random.randint(1, 60),
                                 seconds=random.randint(1, 60))

    def _add_whitespaces_column(self, column: List[str], spacing: Dict[str, int] = None):
        """
        Add whitespacing to a column depending on the
        largest element in the column.
        """
        max_length = spacing[column[0]][1]
        if spacing[column[0]][0] == "right":
            return [str(row).rjust(max_length) for row in column]
        if spacing[column[0]][0] == "center":
            return [str(row).center(max_length) for row in column]
        return [str(row).ljust(max_length) for row in column]

    def _get_keywords(self, titles: List[str]):
        """ Return a list of keywords from a list of titles. """
        if any(' ' in t for t in titles):
            titles_parsed = [title.split(' ') if ' ' in title else [title, ""] for title in titles]
            titles_parsed = ["_".join(title).lower() if title[1] else title[0].lower() for title in titles_parsed]
            titles_parsed = [title.replace("/", "_").replace("-", "_").replace("(", "").replace(")", "") for title in titles_parsed]
            return titles_parsed
        return [title.lower().replace("/", "_") for title in titles]
    
    def make_display_board(self, **kwargs):
        """
        Return String of board informationc
        
        Example:
            -------------------------------------------------------------------------
            SlotID  BoardName  Status          SubType0  SubType1  Online/Offline
            -------------------------------------------------------------------------
            0       A123ABCD   Normal                                            
            1                                                                    
            2       A123ABCD   Normal                                            
            3       A123ABCD   Active_normal   CPCF                              
            4       A123ABCD   Standby_failed  CPCF                Offline       
            5                                                                    
            -------------------------------------------------------------------------
        """
        args = kwargs['args']
        if not args or not isinstance(args, str) or not args.isdigit():
            return "Please provide the frame number correctly."
        args = int(args)
        titles = ["SlotID", "BoardName", "Status", "SubType0", "SubType1", "Online/Offline"]
        titles: dict = {title:keyword for title, keyword in zip(titles, self._get_keywords(titles))}
        boards = [*copy.deepcopy(self.configurations["frames"][args]["slots"])]
        for title, keyword in titles.items():
            board_column = [board[keyword] for board in boards]
            results = self._add_whitespaces_column([title] + board_column, FRAME_SPACING)
            board_column = results[1:]
            titles[title] = results[0]
            for board in boards:
                board[keyword] = board_column[boards.index(board)]
        return self.render("huawei_smartax/display_board.j2", titles=titles.values(), boards=boards)

    def make_display_onts(self, **kwargs):
        """ Return the ONTs information 
        
        Example:
            -----------------------------------------------------------------------------
            F/S/P   ONT         SN         Control     Run      Config   Match    Protect
                    ID                     flag        state    state    state    side 
            -----------------------------------------------------------------------------
            0/ 1/0    0  1234567890ABCDEF  active      online   normal   match    no 
            0/ 1/0    1  1234567890ABCDEF  active      online   normal   match    no 
            0/ 1/0    2  1234567890ABCDEF  active      online   normal   match    no 
            -----------------------------------------------------------------------------
            F/S/P       ONT  Description  
                        ID  
            -----------------------------------------------------------------------------
            0/ 1/0       0   Generic_description
            0/ 1/0       1   Generic_description
            0/ 1/0       2   Generic_description
            -----------------------------------------------------------------------------
            In port 0/ 1/0 , the total of ONTs are: 3, online: 3
            -----------------------------------------------------------------------------
        """
        if not isinstance(kwargs['args'], str) \
            or not all(val.isdigit() for val in kwargs['args'].split(" ")) \
            or not len(kwargs['args'].split(" ")) >= 3:
            return "Please provide the port number correctly."

        if len(kwargs['args'].split(" ")) == 3:
            return self.make_display_ont_info_list(**kwargs)
        return self.make_display_ont_info_one(**kwargs)
    
    def make_display_ont_info_list(self, **kwargs):
        """ Return the ONTs information in a list format"""    
        try:

            frame_index, board_index, port_index = (int(value) for value in kwargs['args'].split(" "))
            
            titles_table_1 = ["F/S/P", "ONT ID", "SN", "Control flag", "Run state", "Config state", "Match state", "Protect side"]
            titles_table_2 = ["F/S/P", "ONT-ID", "Description"]
            titles_table_1 = {title:keyword for title, keyword in zip(titles_table_1, self._get_keywords(titles_table_1))}
            titles_table_2 = {title:keyword for title, keyword in zip(titles_table_2, self._get_keywords(titles_table_2))}
            frame = copy.deepcopy(self.configurations["frames"][frame_index])
            if frame['slots'][board_index]['boardname'] not in GPON_BOARDS:
                return "The board is not a PON board."
            if port_index >= GPON_BOARDS[frame['slots'][board_index]['boardname']]:
                return "The port does not exist in the board."
            board = frame['slots'][board_index]
            onts = board["ports"][port_index]
            port = f"{frame_index}/ {board_index}/{port_index}"
            for ont in onts:
                ont["f_s_p"] = port
                ont["ont-id"] = ont["ont_id"]
            for title, keyword in titles_table_1.items():
                onts_column = [ont[keyword] for ont in onts]
                results = self._add_whitespaces_column([title] + onts_column, FRAME_SPACING)
                onts_column = results[1:]
                titles_table_1[title] = results[0]
                for ont in onts:
                    ont[keyword] = onts_column[onts.index(ont)]
            for title, keyword in titles_table_2.items():
                onts_column = [ont[keyword] for ont in onts]
                results = self._add_whitespaces_column([title] + onts_column, FRAME_SPACING)
                onts_column = results[1:]
                titles_table_2[title] = results[0]
                for ont in onts:
                    ont[keyword] = onts_column[onts.index(ont)]
            return self.render("huawei_smartax/display_ont_info_list.j2", port=port, onts=onts)
        except (IndexError, ValueError):
            return "There are no ONTs in the specified port."
        
    def make_display_ont_info_one(self, **kwargs):
        """ Return the ONTs information in a single format"""    
        try:
            frame_index, board_index, port_index, ont_id = (int(value) for value in kwargs['args'].split(" "))
            frame = copy.deepcopy(self.configurations["frames"][frame_index])
            if frame['slots'][board_index]['boardname'] not in GPON_BOARDS:
                return "The board is not a PON board."
            if port_index >= GPON_BOARDS[frame['slots'][board_index]['boardname']]:
                return "The port does not exist in the board."
            board = frame['slots'][board_index]
            onts = board["ports"][port_index]
            ont = next((ont for ont in onts if ont["ont_id"] == ont_id), None)
            if not ont:
                return "The ONT does not exist in the port."
            ont['fsp'] = f"{frame_index}/ {board_index}/{port_index}"
            return self.render("huawei_smartax/display_ont_info_one.j2", **ont)
        except (IndexError, ValueError):
            return "There are no ONTs in the specified port."

    def make_display_sysman_service_state(self, **kwargs):
        """ Return the sysman service state information """
        services = copy.deepcopy(self.configurations["services"])
        titles = ["Network service", "Port", "State"]
        titles: dict = {title:keyword for title, keyword in zip(titles, self._get_keywords(titles))}
        for title, keyword in titles.items():
            services_column = [service[keyword] if service[keyword] is not None else "----" for service in services]
            results = self._add_whitespaces_column([title] + services_column, SERVICES_SPACING)
            services_column = results[1:]
            titles[title] = results[0]
            for service in services:
                service[keyword] = services_column[services.index(service)]
        return self.render("huawei_smartax/display_sysman_service_state.j2", titles=list(titles.values()), services=services)

    def make_dba__profile_add(self, **kwargs):
        """ Adds a DBA profile with the corresponding parameters. """
        if not isinstance(kwargs['args'], str):
            return "Please provide the profile name."
        args = kwargs['args'].split(' ')
        new_dba_profile = {
            'profile_id': len(self.configurations["dba_profiles"]) + 1,
            'profile_name': f'profile_id_{len(self.configurations["dba_profiles"]) + 1}',
            'type': None,
            'bandwidth_compensation': 'No',
            'fix_delay': 'No',
            'fix_kbps': 0,
            'assure_kbps': 0,
            'max_kbps': 0,
            'additional_bandwidth': 'best-effort',
            'best_effort_weight': 0,
            'best_effort_priority': 0,
            'bind_times': 0,
        }
        args_iterator = iter(args)
        for arg in args_iterator:
            if arg == "profile-id":
                next_arg = next(args_iterator)
                if not next_arg.isdigit():
                    return "Please provide the correct profile id."
                new_dba_profile['profile_id'] = int(next_arg)
            elif arg == "profile-name":
                next_arg = next(args_iterator)
                if next_arg.isdigit():
                    return "Please provide the correct profile name that is not only numbers."
                new_dba_profile['profile_name'] = next_arg
            elif arg in ["type1", "type2", "type3", "type4", "type5"]:
                new_dba_profile['type'] = int(arg[-1])
            elif arg == "bandwidth-compensation":
                next_arg = next(args_iterator)
                if not next_arg in ["yes", "no"]:
                    return "Please provide the correct bandwidth compensation."
                new_dba_profile['bandwidth-compensation'] = next_arg
            elif arg in ["fix", "assure", "max"]:
                next_arg = next(args_iterator)
                if not next_arg.isdigit():
                    return "Please provide the correct kbps value."
                new_dba_profile[f"{arg}_kbps"] = int(next_arg)
            else:
                return "Please provide the correct arguments."
        if new_dba_profile['profile_id'] in [dba_profile['profile_id'] for dba_profile in self.configurations["dba_profiles"]] \
            or new_dba_profile['profile_name'] in [dba_profile['profile_name'] for dba_profile in self.configurations["dba_profiles"]]:
            return "The DBA profile already exists."
        self.configurations["dba_profiles"].append(new_dba_profile)
        self.configurations["dba_profiles"].sort(key=lambda x: x['profile_id'])

        return self.render("huawei_smartax/dba__profile_add.j2", **new_dba_profile)

    def make_display_dba__profile(self, **kwargs):
        """ Display the DBAs based on the args. """
        args = kwargs['args'].split(' ')
        if args[0] == 'all':
            return self.make_display_dba__profile_all()
        elif args[0] == 'profile-name':
            if not len(args) != 2:
                return "Please provide the profile name correctly."
            return self.make_display_dba__profile_profile__name(profile_name=args[1])
        return "Please provide the correct arguments."
        
    def make_display_ont_autofind(self, **kwargs):
        """ Displays the ONT autofind information. """
        gpon_onts, epon_onts = self._get_onts_autofind()
        return self.render("huawei_smartax/display_ont_autofind_all.j2", gpon_onts = gpon_onts, epon_onts = epon_onts)
    
    def _get_onts_autofind(self):
        """ Return the ONTs information that are not registered yet. """
        frames = copy.deepcopy(self.configurations["frames"])
        autofind_time = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S%z")
        onts_autofind: List = []
        for frame in frames:
            for slot in frame["slots"]:
                if 'ports' not in slot:
                    continue
                for port in slot["ports"]:
                    for ont in port:
                        if not ont["registered"]:
                            ont["fsp"] = f"{frames.index(frame)}/{frame['slots'].index(slot)}/{port.index(ont)}"
                            ont["autofind_time"] = autofind_time
                            onts_autofind.append(ont)
        gpon_onts = [ont for ont in onts_autofind if not ont["is_epon"]]
        epon_onts = [ont for ont in onts_autofind if ont["is_epon"]]
        return gpon_onts, epon_onts
    
    def make_display_dba__profile_all(self, **kwargs):
        """ Displays all the DBA profiles. """
        dba_profiles = copy.deepcopy(self.configurations["dba_profiles"])
        titles = ["Profile-ID", "Type", "Bandwidth Compensation", "Fix (kbps)", "Assure (kbps)", "Max (kbps)", "Bind times"]
        titles: dict = {title:keyword for title, keyword in zip(titles, self._get_keywords(titles))}
        for title, keyword in titles.items():
            dba_profiles_column = [dba_profile[keyword] for dba_profile in dba_profiles]
            results = self._add_whitespaces_column([title] + dba_profiles_column, DBA_PROFILES_SPACING)
            dba_profiles_column = results[1:]
            titles[title] = results[0]
            for dba_profile in dba_profiles:
                dba_profile[keyword] = dba_profiles_column[dba_profiles.index(dba_profile)]
        return self.render("huawei_smartax/display_dba__profile_all.j2", dba_profiles=dba_profiles)
    
    def make_display_dba__profile_profile__name(self, profile_name: str = None):
        """ Displays one DBA profile based on the name. """
        dba_profiles= copy.deepcopy(self.configurations["dba_profiles"])
        dba_profile = next((dba_profile for dba_profile in dba_profiles if dba_profile["profile_name"] == profile_name), None)
        return self.render("huawei_smartax/display_dba__profile_profile__name.j2", **dba_profile)

    def make_quit(self, **kwargs):
        """ Exit the current level of the CLI """
        base_prompt = kwargs["base_prompt"]
        current_prompt = kwargs["current_prompt"]
        initial_prompt = INITIAL_PROMPT.format(base_prompt=base_prompt)
        enable_prompt = ENABLE_PROMPT.format(base_prompt=base_prompt)
        config_prompt = CONFIG_PROMPT.format(base_prompt=base_prompt)
        if current_prompt in [initial_prompt, enable_prompt]:
            return True
        if current_prompt in config_prompt:
            return {"output": None, "new_prompt": ENABLE_PROMPT}
        raise RuntimeError(f"make_quit does not know how to handle '{current_prompt}' prompt")

    def make_display_ont_info_all(self):
        """ Return the ONTs information that are not registered yet. """

    def make_display_ont_info(self, **kwargs):
        """ Return the ONTs information """
        args = kwargs['args']
        if args == "all":
            return self.make_display_ont_info_all()
        raise NotImplementedError(f"make_display_ont_info does not know how to handle '{args}'")

    def make_display_sysuptime(self, **kwargs):
        """ Return the system uptime. """
        uptime: datetime = datetime.now() - self.SYSTEM_STARTUP_TIME
        days: int = uptime.days
        hours: int = uptime.seconds // 3600
        minutes: int = (uptime.seconds // 60) % 60
        seconds: int = uptime.seconds % 60
        return self.render(
            "huawei_smartax/display_sysuptime.j2",
            days=days, hours=hours, minutes=minutes, seconds=seconds
        )
commands = {
    "enable": {
        "output": None,
        "new_prompt": ENABLE_PROMPT,
        "help": "enter exec prompt",
        "prompt": INITIAL_PROMPT,
    },
    "config": {
        "output": None,
        "new_prompt": CONFIG_PROMPT,
        "help": "enter configuration mode",
        "prompt": ENABLE_PROMPT,
    },
    "display sysuptime": {
        "output": HuaweiSmartAX.make_display_sysuptime,
        "regex": "di[[splay]] sys[[uptime]]",
        "help": "Display the system uptime",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT, CONFIG_PROMPT],
    },
    "di[[splay]] bo[[ard]] \\S+": {  # display board 0
        "output": HuaweiSmartAX.make_display_board,
        "help": "display board information",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT, CONFIG_PROMPT],
    },
    "di[[splay]] ont inf[[o]] \\S+": {  # display ont info 0 2 0
        "output": HuaweiSmartAX.make_display_onts,
        "help": "display ont information",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT, CONFIG_PROMPT],
    },
    "display sysman service state": {
        "output": HuaweiSmartAX.make_display_sysman_service_state,
        "help": "It shows the state of the running services",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT],
    },
    "display dba-profile": {
        "output": HuaweiSmartAX.make_display_dba__profile,
        "regex": "di[[splay]] db[[a-profile]] \\S+",
        "help": "Displays all the DBA profiles.",
        "prompt": [CONFIG_PROMPT],
    },
    "dba-profile add": {
        "output": HuaweiSmartAX.make_dba__profile_add,
        "regex": "dba-profile add \\S+",
        "help": "Adds a DBA profile with the corresponding parameters.",
        "prompt": [CONFIG_PROMPT],
    },
    "display ont autofind": {
        "output": HuaweiSmartAX.make_display_ont_autofind,
        "regex": "di[[splay]] ont autof[[ind]] \\S+",
        "help": "Displays the ONT autofind information.",
        "prompt": [CONFIG_PROMPT],
    },
    "quit": {
        "output": HuaweiSmartAX.make_quit,
        "help": "Exit the current level of the CLI",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT, CONFIG_PROMPT],
    },
    "_default_": {
        "output": "Unknown command",
        "help": "Output to print for unknown commands",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT, CONFIG_PROMPT],
    },
}
