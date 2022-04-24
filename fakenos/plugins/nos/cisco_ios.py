import time

initial_prompt = "{base_prompt}>"


def make_show_clock(base_prompt, current_prompt, command):
    "Return String in format '*11:54:03.018 UTC Sat Apr 16 2022'"
    return time.strftime("*%H:%M:%S.000 %Z %a %b %d %Y")


running_configuration = """
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname {base_prompt}
!
boot-start-marker
boot-end-marker
!
!
vrf definition MGMT
 rd 1:1
 !
 address-family ipv4
 exit-address-family
!
vrf definition abc-123
 rd 123:123
 !
 address-family ipv4
 exit-address-family
!
vrf definition def-456
 rd 456:456
 !
 address-family ipv4
 exit-address-family
!
!
aaa new-model
!
!
aaa authentication login default local
aaa authorization exec default local
!
!
aaa session-id common
!
!
clock timezone EET 2 0
mmi polling-interval 60
no mmi auto-configure
no mmi pvc
mmi snmp-timeout 180
!
!
no ip domain lookup
ip domain name lab.local
ip cef
no ipv6 cef
!
multilink bundle-name authenticated
!
!
archive
 path unix:BACKUP-
 write-memory
username cisco privilege 15 password 0 cisco
username nornir privilege 15 secret 5 $1$clqS$3CzLxkeHVJ9OYW83DOjuN/
!
redundancy
!
lldp run
!
!
!
interface Loopback0
 description Routing Loopback
 ip address 10.0.0.10 255.255.255.255
 ip ospf 1 area 0
 ipv6 address 2001::10/128
!
interface Loopback100
 ip address 1.1.1.100 255.255.255.255
!
interface Ethernet0/0
 description Main Interface for L3 features testing
 no ip address
 duplex auto
!
interface Ethernet0/0.102
 description to_vIOS1_Gi0/0.102
 encapsulation dot1Q 102
 ip address 10.1.102.10 255.255.255.0
 ipv6 address 2001:102::10/64
!
interface Ethernet0/0.107
 description to_IOL2_Eth0/0.107
 encapsulation dot1Q 107
 ip address 10.1.107.10 255.255.255.0
 ip ospf network point-to-point
 ip ospf 1 area 0
 ipv6 address 2001:107::10/64
!
interface Ethernet0/0.2000
 encapsulation dot1Q 2000
 vrf forwarding MGMT
 ip address 192.168.217.10 255.255.255.0
!
interface Ethernet0/1
 no ip address
 duplex auto
!
interface Ethernet0/2
 no ip address
 duplex auto
!
interface Ethernet0/3
 no ip address
 shutdown
 duplex auto
!
router ospf 1
 router-id 10.0.0.10
!
router bgp 100
 template peer-policy RR
  route-map rpl_in in
  route-map rpl_out out
  route-reflector-client
  next-hop-self
  maximum-prefix 1000 80
  send-community both
 exit-peer-policy
 !
 template peer-session RR
  remote-as 100
  update-source Loopback0
 exit-peer-session
 !
 bgp log-neighbor-changes
 neighbor peer_grpoup_a peer-group
 neighbor peer_grpoup_a remote-as 118
 neighbor peer_grpoup_a update-source Loopback0
 neighbor 10.0.0.4 inherit peer-session RR
 neighbor 10.0.0.8 inherit peer-session RR
 neighbor 10.1.48.4 peer-group peer_grpoup_a
 neighbor 10.1.48.4 description some peer description
 !
 address-family ipv4
  neighbor peer_grpoup_a send-community both
  neighbor peer_grpoup_a next-hop-self
  neighbor peer_grpoup_a route-map route-map-in in
  neighbor peer_grpoup_a route-map route-map-out out
  neighbor 10.0.0.4 activate
  neighbor 10.0.0.4 send-community extended
  neighbor 10.0.0.4 inherit peer-policy RR
  neighbor 10.0.0.8 activate
  neighbor 10.0.0.8 send-community extended
  neighbor 10.0.0.8 inherit peer-policy RR
  neighbor 10.1.48.4 activate
 exit-address-family
 !
 address-family vpnv4
  neighbor peer_grpoup_a send-community both
  neighbor peer_grpoup_a maximum-prefix 1000 80
  neighbor 10.0.0.4 activate
  neighbor 10.0.0.4 send-community extended
  neighbor 10.0.0.4 inherit peer-policy RR
  neighbor 10.0.0.8 activate
  neighbor 10.0.0.8 send-community extended
  neighbor 10.0.0.8 inherit peer-policy RR
  neighbor 10.1.48.4 activate
 exit-address-family
 !
 address-family ipv4 vrf abc-123
  neighbor 123.1.1.1 remote-as 321
  neighbor 123.1.1.1 activate
  neighbor 123.1.2.2 remote-as 321
  neighbor 123.1.2.2 activate
 exit-address-family
 !
 address-family ipv4 vrf def-456
  neighbor 251.1.1.5 remote-as 456
  neighbor 251.1.1.5 activate
  neighbor 251.6.1.6 remote-as 456
  neighbor 251.6.1.6 activate
 exit-address-family
!
ip forward-protocol nd
!
!
no ip http server
no ip http secure-server
ip route vrf MGMT 0.0.0.0 0.0.0.0 192.168.217.1 name inband_management
ip scp server enable
!
logging host 1.1.1.1
logging host 4.4.4.4
logging host 1.1.1.2
logging host 2.2.2.2
ipv6 ioam timestamp
!
control-plane
!

line con 0
 logging synchronous
line aux 0
line vty 0 4
 transport input telnet ssh
!
ntp server 8.8.8.8
ntp server 7.7.7.8
ntp server 1.1.1.2
ntp server 3.3.3.3
ntp server 7.7.7.7
!
end
"""

show_version = """
Cisco IOS XE Software, Version 17.03.01a
Cisco IOS Software [Amsterdam], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 17.3.1a, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2020 by Cisco Systems, Inc.
Compiled Wed 12-Aug-20 00:16 by mcpre


Cisco IOS-XE software, Copyright (c) 2005-2020 by cisco Systems, Inc.
All rights reserved.  Certain components of Cisco IOS-XE software are
licensed under the GNU General Public License ("GPL") Version 2.0.  The
software code licensed under GPL Version 2.0 is free software that comes
with ABSOLUTELY NO WARRANTY.  You can redistribute and/or modify such
GPL code under the terms of GPL Version 2.0.  For more details, see the
documentation or "License Notice" file accompanying the IOS-XE software,
or the applicable URL provided on the flyer accompanying the IOS-XE
software.


ROM: IOS-XE ROMMON
{base_prompt} uptime is 1 day, 17 hours, 32 minutes
Uptime for this control processor is 1 day, 17 hours, 33 minutes
System returned to ROM by reload
System image file is "bootflash:packages.conf"
Last reload reason: reload



This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

License Level: ax
License Type: N/A(Smart License Enabled)
Next reload license Level: ax

The current throughput level is 1000 kbps


Smart Licensing Status: UNREGISTERED/No Licenses in Use

cisco CSR1000V (VXE) processor (revision VXE) with 715705K/3075K bytes of memory.
Processor board ID 9ESGOBARV9D
Router operating mode: Autonomous
3 Gigabit Ethernet interfaces
32768K bytes of non-volatile configuration memory.
3978420K bytes of physical memory.
6188032K bytes of virtual hard disk at bootflash:.

Configuration register is 0x2102
"""

commands = {
    "enable": {
        "output": None,
        "new_prompt": "{base_prompt}#",
        "help": "enter exec prompt",
        "prompt": initial_prompt,
    },
    "show clock": {
        "output": make_show_clock,
        "help": "Display the system clock",
        "prompt": [initial_prompt, "{base_prompt}#"],
    },
    "show running-config": {
        "output": running_configuration,
        "help": "Current operating configuration",
        "prompt": "{base_prompt}#",
    },
    "show version": {
        "output": show_version,
        "help": "System hardware and software status",
        "prompt": "{base_prompt}#",
    },
    "_default_": {
        "output": "% Invalid input detected at '^' marker.",
        "help": "Output to print for unknown commands",
    },
    "terminal width 511": {"output": "", "help": "Set terminal width to 511"},
    "terminal length 0": {"output": "", "help": "Set terminal length to 0"},
}
