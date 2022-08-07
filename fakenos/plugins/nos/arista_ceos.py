import time

initial_prompt = "{base_prompt}>"


def make_show_clock(base_prompt, current_prompt, command):
    return """{current_time}
Timezone: UTC
Clock source: local""".format(current_time=time.strftime("%a %b %d %H:%M:%S %Y"))

def make_exit(base_prompt, current_prompt, command):
    if current_prompt in [f"{base_prompt}>", f"{base_prompt}#"]:
        return True # close session
    elif current_prompt in [f"{base_prompt}(config)#"]:
        return {"output": "", "new_prompt": "{base_prompt}#"} # return to exec prompt
    else:
        raise RuntimeError(f"make_exit does not know how to handle '{current_prompt}' prompt")

running_configuration = """! Command: show running-config
! device: {base_prompt} (cEOSLab, EOS-4.26.0F-21792469.4260F (engineering build))
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
hostname {base_prompt}
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

show_version = """cEOSLab
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

show_ip_int_br = """                                                                          Address 
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
        "new_prompt": "{base_prompt}#",
        "help": "Enable commands for a specified privilege level",
        "prompt": initial_prompt,
    },
    "show clock": {
        "output": make_show_clock,
        "help": "System time",
        "prompt": [initial_prompt, "{base_prompt}#"],
    },
    "show running-config": {
        "output": running_configuration,
        "help": "System running configuration",
        "prompt": "{base_prompt}#",
    },
    "show version": {
        "output": show_version,
        "help": "Software and hardware versions",
        "prompt": "{base_prompt}#",
    },
    "_default_": {
        "output": "% Invalid input",
        "help": "Output to print for unknown commands",
    },
    "terminal width 511": {"output": "Width set to 511 columns.", "help": "Configure the terminal width to 511"},
    "term width 0": {"alias": "terminal width 511"},
    "terminal length 0": {"output": "Pagination disabled.", "help": "Configure the pagination length to 0"},
    "term length 0": {"alias": "terminal length 0"},
    "show ip int brief": {"output": show_ip_int_br, "help": "Condensed output"},
    "show ip interface brief": {"output": show_ip_int_br, "help": "Condensed output"},
    "conf t": {
        "prompt": "{base_prompt}#",
        "output": None,
        "new_prompt": "{base_prompt}(config)#",
        "help": "Config mode",
    },
    "config term": {"alias": "conf t"},
    "configure terminal": {"alias": "conf t"},
    "do show ip int brief": {"alias": "show ip int brief", "prompt": "{base_prompt}(config)#"},
    "exit": {"output": make_exit, "help": "Leave Exec mode"},
    "show hostname": {
        "output": """Hostname: {base_prompt}
FQDN:     {base_prompt}""",
        "help": "Show the system hostname"
    },
    "no logging console": {
        "output": "", 
        "help": "Set console logging parameters", 
        "prompt": "{base_prompt}(config)#"
    },
    "end": {
        "output": "", 
        "help": "Leave config mode", 
        "new_prompt": "{base_prompt}#", 
        "prompt": "{base_prompt}(config)#"
    },
}
