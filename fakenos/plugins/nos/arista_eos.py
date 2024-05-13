"""
NOS module for Arista EOS
"""

import time

NAME: str = "arista_eos"
INITIAL_PROMPT: str = "{base_prompt}>"
ENABLE_PROMPT: str = "{base_prompt}#"
CONFIG_PROMPT: str = "{base_prompt}(config)#"



# pylint: disable=unused-argument
def make_show_clock(base_prompt, current_prompt, command):
    """Return the current time."""
    return f"""{time.strftime('%a %b %d %H:%M:%S %Y')}
Timezone: UTC
Clock source: local"""


# pylint: disable=unused-argument
def make_exit(base_prompt, current_prompt, command):
    """Exit the current level of the CLI."""
    if current_prompt in [INITIAL_PROMPT, ENABLE_PROMPT]:
        return True  # close session
    if current_prompt in [CONFIG_PROMPT]:
        return {"output": "", "new_prompt": ENABLE_PROMPT}  # return to exec prompt
    raise RuntimeError(f"make_exit does not know how to handle '{current_prompt}' prompt")


RUNNING_CONFIGURATION = """! Command: show running-config
! device: {{base_prompt}} (cEOSLab, EOS-4.26.0F-21792469.4260F (engineering build))
!
transceiver qsfp default-mode 4x10G
!
service routing protocols model ribd
!
agent Bfd shutdown
agent PowerManager shutdown
agent LedPolicy shutdown
agent Thermostat shutdown
agent PowerFuse shutdown
agent StandbyCpld shutdown
agent LicenseManager shutdown
!
no logging console
logging host 1.1.1.1 514
logging host 1.2.3.4 514
logging host 1.2.3.5 514
logging host 1.2.3.6 514
logging host 2.2.2.2 514
logging host 4.3.2.1 514
logging host 5.5.5.5 514
logging host 7.7.7.7 514
logging host 9.9.9.9 514
!
logging level AAA informational
!
hostname {{base_prompt}}
!
ntp server 1.1.1.1
ntp server 1.1.1.2
ntp server 1.1.1.10
ntp server 1.1.1.11
ntp server 2.2.2.2
ntp server 2.2.2.3
ntp server 3.3.3.3
ntp server 3.3.3.4
ntp server 4.3.2.1
ntp server 6.6.6.6
ntp server 7.7.7.7
ntp server 7.7.7.8
!
snmp-server location "North West Hall DC1"
snmp-server local-interface Ethernet1
snmp-server host 1.2.3.4 version 2c test
snmp-server host 1.2.3.5 version 2c test
!
spanning-tree mode mstp
!
no aaa root
!
username nornir privilege 15 secret sha512 $6$EkriX8oB5g3Midq4$ErOpqzIWT7FxiW1IkSNQKS8gEqsn9HsbRVm8.Zw47y3Xm9a.GywP9zPF/avyTBBS8c5/ZSMMj/6BHL64KcW2I1
!
interface Ethernet1
   description Configured by NETCONF
   mtu 9200
   no switchport
   ip address 10.0.1.4/24
!
interface Loopback1
   ip address 1.1.1.1/24
!
interface Loopback2
   description Lopback2 for Customer 27123
   ip address 2.2.2.2/24
!
interface Loopback3
   description Customer #56924 service
   ip address 1.2.3.4/24
!
no ip routing
!
management api http-commands
   protocol http
   no shutdown
!
management api gnmi
   transport grpc default
!
management api netconf
   transport ssh def
!
end"""

SHOW_VERSION = """cEOSLab
Hardware version: 
Serial number: 
Hardware MAC address: 0242.0af6.c8a5
System MAC address: 0242.0af6.c8a5

Software image version: 4.26.0F-21792469.4260F (engineering build)
Architecture: i686
Internal build version: 4.26.0F-21792469.4260F
Internal build ID: c5b41f65-54cd-44b1-b576-b5c48700ee19

cEOS tools version: 1.1
Kernel version: 3.10.0-1160.21.1.el7.x86_64

Uptime: 0 weeks, 0 days, 0 hours and 8 minutes
Total memory: 4918832 kB
Free memory: 1816320 kB"""

SHOW_IP_INT_BR = """
                                                                          Address 
Interface       IP Address        Status       Protocol            MTU    Owner   
--------------- ----------------- ------------ -------------- ----------- ------- 
Ethernet1       10.0.1.4/24       up           up                 9200            
Loopback1       1.1.1.1/24        up           up                65535            
Loopback2       2.2.2.2/24        up           up                65535            
Loopback3       1.2.3.4/24        up           up                65535            

"""

commands = {
    "enable": {
        "output": None,
        "new_prompt": ENABLE_PROMPT,
        "help": "Enable commands for a specified privilege level",
        "prompt": INITIAL_PROMPT,
    },
    "show clock": {
        "output": make_show_clock,
        "help": "System time",
        "prompt": [INITIAL_PROMPT, ENABLE_PROMPT],
    },
    "show running-config": {
        "output": RUNNING_CONFIGURATION,
        "help": "System running configuration",
        "prompt": ENABLE_PROMPT,
    },
    "show version": {
        "output": SHOW_VERSION,
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
        "output": SHOW_IP_INT_BR,
        "help": "Condensed output",
        "prompt": [ENABLE_PROMPT, INITIAL_PROMPT],
    },
    "show ip interface brief": {
        "output": SHOW_IP_INT_BR,
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
    "exit": {"output": make_exit, "help": "Leave Exec mode", "prompt": [ENABLE_PROMPT, CONFIG_PROMPT]},
    "show hostname": {
        "output": """Hostname: {{base_prompt}}
FQDN:     {{base_prompt}}""",
        "help": "Show the system hostname",
        "prompt": ENABLE_PROMPT,
    },
    "no logging console": {"output": "", "help": "Set console logging parameters", "prompt": CONFIG_PROMPT},
    "end": {
        "output": "",
        "help": "Leave config mode",
        "new_prompt": ENABLE_PROMPT,
        "prompt": CONFIG_PROMPT,
    },
}
