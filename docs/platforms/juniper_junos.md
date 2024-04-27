# juniper_junos


!!! warning
    This is automatically generated. In case of any issues, 
    please refer to the source code or, even better, 
    open an issue on the GitHub repository. Thanks! 🤗📖
## Platforms:

## Commands

### enable

**Output:**
```
null
```

**Help:** enter enable mode

**Prompt:**
- juniper_junos>

### set cli screen-width 511

**Output:**
```
Screen width set to 511
```

**Help:** Sets the terminal width to maximum

**Prompt:**
- juniper_junos>
- juniper_junos#

### show vlans

**Output:**
```
Routing instance        VLAN name             Tag          Interfaces
default-switch          v100-Control           100
                                                           ae0.0*
                                                           et-0/0/24.0*
                                                           ge-0/0/3.0
                                                           xe-0/0/13.0*
                                                           xe-0/0/15.0*
                                                           xe-0/0/17.0*
                                                           xe-0/0/9.0*
default-switch          v1005-HelpDesk        1005
                                                           ae0.0*
                                                           et-0/0/24.0*
                                                           ge-0/0/7.0
                                                           xe-0/0/13.0*
                                                           xe-0/0/15.0*
                                                           xe-0/0/17.0*
                                                           xe-0/0/9.0*
default-switch          v109-TEMP-Project-Data 109
                                                           ae0.0*
                                                           et-0/0/24.0*
                                                           ge-0/0/7.0
                                                           xe-0/0/13.0*
                                                           xe-0/0/15.0*
                                                           xe-0/0/17.0*
                                                           xe-0/0/22.0
                                                           xe-0/0/9.0*

{{master:0}}
```

**Help:** execute the command "show vlans"

**Prompt:**
- juniper_junos>
- juniper_junos#

### show interfaces

**Output:**
```
Physical interface: ge-0/0/0, Enabled, Physical link is Up
  Interface index: 134, SNMP ifIndex: 502
  Description: Test
  Link-level type: Ethernet, MTU: 1514, MRU: 0, LAN-PHY mode,
  Link-mode: Half-duplex, Speed: 1000mbps, BPDU Error: None,
  MAC-REWRITE Error: None, Loopback: Disabled, Source filtering: Disabled,
  Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
  Device flags   : Present Running
  Interface flags: SNMP-Traps Internal: 0x4000
  Link flags     : None
  CoS queues     : 8 supported, 8 maximum usable queues
  Current address: 00:0c:29:5e:2c:1a, Hardware address: 00:0c:29:5e:2c:1a
  Last flapped   : 2016-02-09 13:37:59 UTC (23:39:35 ago)
  Input rate     : 0 bps (0 pps)
  Output rate    : 0 bps (0 pps)
  Active alarms  : None
  Active defects : None
  Interface transmit statistics: Disabled

  Logical interface ge-0/0/0.2036 (Index 74) (SNMP ifIndex 535)
    Flags: Up SNMP-Traps 0x0 VLAN-Tag [ 0x8100.2036 ]  Encapsulation: ENET2
    Input packets : 12439041
    Output packets: 2552075
    Security: Zone: Null
    Protocol inet, MTU: 1500
      Flags: Sendbcast-pkt-to-re, Sample-input, Sample-output
      Addresses, Flags: Is-Preferred Is-Primary
        Destination: 10.10.199.176/29, Local: 10.10.199.180, Broadcast: 10.10.199.183

Physical interface: gr-0/0/0, Enabled, Physical link is Up
  Interface index: 139, SNMP ifIndex: 506
  Type: GRE, Link-level type: GRE, MTU: Unlimited, Speed: 800mbps
  Link flags     : Scheduler Keepalives DTE
  Device flags   : Present Running
  Interface flags: Point-To-Point
  Input rate     : 0 bps (0 pps)
  Output rate    : 0 bps (0 pps)

Physical interface: ip-0/0/0, Enabled, Physical link is Up
  Interface index: 140, SNMP ifIndex: 507
  Type: IPIP, Link-level type: IP-over-IP, MTU: Unlimited, Speed: 800mbps
  Link flags     : Scheduler Keepalives DTE
  Device flags   : Present Running
  Input rate     : 0 bps (0 pps)
  Output rate    : 0 bps (0 pps)
 
Physical interface: lsq-0/0/0, Enabled, Physical link is Up
  Interface index: 141, SNMP ifIndex: 509
  Link-level type: LinkService, MTU: 1504
  Device flags   : Present Running
  Interface flags: Point-To-Point SNMP-Traps Internal: 0x4000
  Last flapped   : 2016-02-09 13:37:59 UTC (22:25:23 ago)
  Input rate     : 0 bps (0 pps)
  Output rate    : 0 bps (0 pps)

Physical interface: lt-0/0/0, Enabled, Physical link is Up
  Interface index: 143, SNMP ifIndex: 510
  Type: Logical-tunnel, Link-level type: Logical-tunnel, MTU: Unlimited, Speed: 800mbps
  Device flags   : Present Running
  Interface flags: Point-To-Point SNMP-Traps Internal: 0x4000
  Link flags     : None
  Physical info  : 13
  Current address: 02:96:14:57:ee:b3, Hardware address: 02:96:14:57:ee:b3
  Last flapped   : Never
  Input rate     : 0 bps (0 pps)
  Output rate    : 0 bps (0 pps)

Physical interface: mt-0/0/0, Enabled, Physical link is Up
  Interface index: 142, SNMP ifIndex: 511
  Type: Multicast-GRE, Link-level type: GRE, MTU: Unlimited, Speed: 800mbps
  Link flags     : Keepalives DTE
  Device flags   : Present Running
  Interface flags: SNMP-Traps
  Input rate     : 0 bps (0 pps)
  Output rate    : 0 bps (0 pps)

Physical interface: sp-0/0/0, Enabled, Physical link is Up
  Interface index: 138, SNMP ifIndex: 515
  Type: Adaptive-Services, Link-level type: Adaptive-Services, MTU: 9192, Speed: 800mbps
  Device Flags   : Present Running
  Interface flags: Point-To-Point SNMP-Traps Internal: 0x4000

{{master:0}}

```

**Help:** execute the command "show interfaces"

**Prompt:**
- juniper_junos>
- juniper_junos#

### show chassis hardware

**Output:**
```
Hardware inventory:
Item             Version  Part number  Serial number     Description
Chassis                                A0000             MX104
Midplane         REV 49   750-000000   XXXXXX04          MX104
PEM 0            REV 04   740-000000   XXXXXX20039       AC Power Entry Module
 PEM 1            REV 04   740-000000   XXXXXX20125       AC Power Entry Module
 Routing Engine 0 REV 07   750-000000   XXXXXX28          RE-MX-104
AFEB 0                    BUILTIN      BUILTIN           Forwarding Engine Processor
 FPC 0                     BUILTIN      BUILTIN           MPC BUILTIN
  MIC 0          REV 25   750-000000   XXXXXX26          3D 2x 10GE XFP
    PIC 0                 BUILTIN      BUILTIN           1x 10GE XFP
      Xcvr 0     REV 01   740-000000   XXXXXXXX0001      XFP-10G-LR
    PIC 1                 BUILTIN      BUILTIN           1x 10GE XFP
      Xcvr 0     REV 01   740-000000   XXXXXXXX0001      XFP-10G-LR
  MIC 1          REV 25   750-000000   ABCV0000          3D 2x 10GE XFP
    PIC 2                 BUILTIN      BUILTIN           1x 10GE XFP
      Xcvr 0     REV 01   740-000000   XXXXXXXX0001      XFP-10G-LR
    PIC 3                 BUILTIN      BUILTIN           1x 10GE XFP
      Xcvr 0              NON-JNPR     AAAA0000A         XFP-10G-SR
 FPC 1                     BUILTIN      BUILTIN           MPC BUILTIN
  MIC 0          REV 30   750-000000   AAAA000A          3D 20x 1GE(LAN) SFP
    PIC 0                 BUILTIN      BUILTIN           10x 1GE(LAN) SFP
      Xcvr 0     REV 02   740-000000   XXXXX1G22474      SFP-T
      Xcvr 1     REV 02   740-000000   XXXXX1G22472      SFP-T
      Xcvr 2     REV 01   740-000000   XXXXX23           SFP-T
      Xcvr 3     REV 01   740-000000   XXXXX01           SFP-T
      Xcvr 4     REV 02   740-000000   XXXXX1G22481      SFP-T
      Xcvr 5     REV 02   740-000000   XXXXX1G22479      SFP-T
    PIC 1                 BUILTIN      BUILTIN           10x 1GE(LAN) SFP
      Xcvr 0     REV 01   740-000000   XXXXXX20000       SFP-T
      Xcvr 1     REV 02   740-000000   XXXXX1G20000      SFP-T
  MIC 1          REV 26   750-000000   XXXXX000          3D 2x 10GE XFP
    PIC 2                 BUILTIN      BUILTIN           1x 10GE XFP
      Xcvr 0     REV 01   740-000000   A00098A           XFP-10G-LR
    PIC 3                 BUILTIN      BUILTIN           1x 10GE XFP
      Xcvr 0     REV 01   740-000000   XXXXX00000        XFP-10G-LR
FPC 2                     BUILTIN      BUILTIN           MPC BUILTIN
  MIC 0                   BUILTIN      BUILTIN           4x 10GE(LAN) SFP+
    PIC 0                 BUILTIN      BUILTIN           4x 10GE(LAN) SFP+
      Xcvr 0     REV      740-000000   XXXXX00000        SFP+-10G-LR
      Xcvr 1     REV 01   740-000000   XXXXX00000        SFP+-10G-SR
      Xcvr 2     REV      740-000000   XXXXX00000        SFP+-10G-LR
      Xcvr 3     REV      740-000000   XXXXX00000        SFP+-10G-LR
Fan Tray 0       REV 03   711-000000   ABCD0000          Fan Tray

```

**Help:** execute the command "show chassis hardware"

**Prompt:**
- juniper_junos>
- juniper_junos#

### show arp no-resolve

**Output:**
```
MAC Address       Address         Interface     Flags
00:00:00:00:00:04 10.1.100.130    vlan.20        none
00:00:00:00:00:05 10.1.100.132    vlan.20        none
00:00:00:00:00:08 10.1.100.72     vlan.20        none
00:00:00:00:00:09 10.1.100.73     vlan.20        none
00:00:00:00:00:0a 10.1.100.74     vlan.20        none
00:00:00:00:00:0b 10.1.100.75     vlan.20        none
00:00:00:00:00:0c 10.1.100.76     vlan.20        none
00:00:00:00:11:11 10.1.111.11     vlan.20        none
00:00:00:00:13:13 10.1.13.13      vlan.20        none
Total entries: 9

{{master:0}}

```

**Help:** execute the command "show arp no-resolve"

**Prompt:**
- juniper_junos>
- juniper_junos#

### show lacp interfaces

**Output:**
```
Aggregated interface: ae33
    LACP state:       Role   Exp   Def  Dist  Col  Syn  Aggr  Timeout  Activity
      xe-0/0/0:0     Actor    No    No   Yes  Yes  Yes   Yes     Fast    Active
      xe-0/0/0:0   Partner    No    No   Yes  Yes  Yes   Yes     Slow    Active
    LACP protocol:        Receive State  Transmit State          Mux State
      xe-0/0/0:0                Current   Slow periodic Collecting distributing

Aggregated interface: ae111
    LACP state:       Role   Exp   Def  Dist  Col  Syn  Aggr  Timeout  Activity
      et-0/0/32      Actor    No    No   Yes  Yes  Yes   Yes     Fast    Active
      et-0/0/32    Partner    No    No   Yes  Yes  Yes   Yes     Fast    Active
      et-0/0/33      Actor    No    No   Yes  Yes  Yes   Yes     Fast    Active
      et-0/0/33    Partner    No    No   Yes  Yes  Yes   Yes     Fast    Active
    LACP protocol:        Receive State  Transmit State          Mux State
      et-0/0/32                 Current   Fast periodic Collecting distributing
      et-0/0/33                 Current   Fast periodic Collecting distributing

Aggregated interface: ae112
    LACP state:       Role   Exp   Def  Dist  Col  Syn  Aggr  Timeout  Activity
      et-0/0/34      Actor    No    No   Yes  Yes  Yes   Yes     Fast    Active
      et-0/0/34    Partner    No    No   Yes  Yes  Yes   Yes     Fast    Active
      et-0/0/35      Actor    No    No   Yes  Yes  Yes   Yes     Fast    Active
      et-0/0/35    Partner    No    No   Yes  Yes  Yes   Yes     Fast    Active
    LACP protocol:        Receive State  Transmit State          Mux State
      et-0/0/34                 Current   Fast periodic Collecting distributing
      et-0/0/35                 Current   Fast periodic Collecting distributing
 
Aggregated interface: ae115
    LACP state:       Role   Exp   Def  Dist  Col  Syn  Aggr  Timeout  Activity
      et-0/0/25      Actor    No    No   Yes  Yes  Yes   Yes     Fast    Active
      et-0/0/25    Partner    No    No   Yes  Yes  Yes   Yes     Fast    Active
      et-0/0/29      Actor    No    No   Yes  Yes  Yes   Yes     Fast    Active
      et-0/0/29    Partner    No    No   Yes  Yes  Yes   Yes     Fast    Active
    LACP protocol:        Receive State  Transmit State          Mux State
      et-0/0/25                 Current   Fast periodic Collecting distributing
      et-0/0/29                 Current   Fast periodic Collecting distributing

{{master:0}}

```

**Help:** execute the command "show lacp interfaces"

**Prompt:**
- juniper_junos>
- juniper_junos#

### show chassis firmware

**Output:**
```
Part                     Type       Version
FPC                      ROM        PC Bios
                         O/S        Version 15.1F4.15 by builder on 2015-12-23 18:14:32 UTC

Part                     Type       Version
FPC                      O/S        Version 15.1X49-D15 by ssd-builder on 2015-07-31 06:28:30 UTC
FWDD                     O/S        Version 15.1X49-D15 by ssd-builder on 2015-07-31 06:28:30 UTC

Part                     Type       Version
Forwarding engine board  ROM        Juniper ROM Monitor Version 4.1b2
                         O/S        Version 4.1I1 by tlim on 2000-04-24 11:27

Part                     Type       Version
System switch board      ROM        Juniper ROM Monitor Version 3.4b26
                         O/S        Version 3.4I16 by smackie on 2000-02-29 2
FPC 1                    ROM        Juniper ROM Monitor Version 3.0b1
                         O/S        Version 3.4I4 by smackie on 2000-02-25 21
FPC 2                    ROM        Juniper ROM Monitor Version 3.0b1
                         O/S        Version 3.4I4 by smackie on 2000-02-25 21

Part                     Type       Version
System control board     ROM        Juniper ROM Monitor Version 2.0i126Copyri
                         O/S        Version 2.0i1 by root on Thu Jul 23 00:51
FPC 5                    ROM        Juniper ROM Monitor Version 2.0i49Copyrig
                         O/S        Version 2.0i1 by root on Thu Jul 23 00:59

FPC 2                    ROM        Juniper ROM Monitor Version 8.0b29         
                         O/S        Version 8.2B1 by builder on 2006-10-18 16:2
FPC 3                    ROM        Juniper ROM Monitor Version 8.0b29         
                         O/S        Version 8.2B1 by builder on 2006-10-18 16:2
FPC 4                    ROM        Juniper ROM Monitor Version 8.0b29         
                         O/S        Version 8.2B1 by builder on 2006-10-18 16:2
FEB 3                    ROM        Juniper ROM Monitor Version 8.0b29         
                         O/S        Version 8.2B1 by builder on 2006-10-18 16:1
FEB 4                    ROM        Juniper ROM Monitor Version 8.0b29         
                         O/S        Version 8.2B1 by builder on 2006-10-18 16:1

Part                     Type       Version
 SFM 0                    ROM        Juniper ROM Monitor Version 4.0b2
                         O/S        Version 4.0I1 by tlim on 2000-02-29 11:50
 SFM 1                    ROM        Juniper ROM Monitor Version 4.0b2
                         O/S        Version 4.0I1 by tlim on 2000-02-29 11:50
 FPC 0                    ROM        Juniper ROM Monitor Version 4.0b2
                         O/S        Version 4.0I1 by tlim on 2000-02-29 11:56
 FPC 1                    ROM        Juniper ROM Monitor Version 4.0b2
                         O/S        Version 4.0I1 by tlim on 2000-02-29 11:56
 FPC 2                    ROM        Juniper ROM Monitor Version 4.0b3
                         O/S        Version 4.0I1 by tlim on 2000-02-29 11:56

Part                     Type       Version
FPC 0                    ROM        Juniper ROM Monitor Version 13.1b24       
                         O/S        Version 13.2-20130514.1 by builder on 2013-
FPC 1                    ROM        Juniper ROM Monitor Version 13.1b24       
                         O/S        Version 13.2-20130514.1 by builder on 2013-
FPC 2                    ROM        Juniper ROM Monitor Version 13.1b24       
                         O/S        Version 13.2-20130514.1 by builder on 2013-
AFEB                     ROM        Juniper ROM Monitor Version 13.1b24       
                         O/S        Version 13.2-20130514.1 by builder on 2013-

Part                     Type       Version
FPC 1                    ROM        Juniper ROM Monitor Version 8.3b1          
                         O/S        Version 9.0-20080103.0 by builder on 2008-0
FPC 2                    ROM        Juniper ROM Monitor Version 8.3b1          
                         O/S        Version 9.0-20080103.0 by builder on 2008-0

Part                     Type       Version
FPC 1                    ROM        Juniper ROM Monitor Version 8.3b1          
                         O/S        Version 9.0-20070916.3 by builder on 2007-0

Part                     Type       Version
FPC 4                    ROM        Juniper ROM Monitor Version 8.0b8          
                         O/S        Version 8.2I59 by artem on 2006-10-31 19:22
FPC 7                    ROM        Juniper ROM Monitor Version 8.2b1          
                         O/S        Version 8.2-20061026.1 by builder on 2006-1

Part                     Type       Version
 FPC 0                    ROM        Juniper ROM Monitor Version 12.3b1
                         O/S        Version 12.3-20121220.0 by builder on 2012-
 FPC 1                    ROM        Juniper ROM Monitor Version 10.1b3
                         O/S        Version 12.3-20121220.0 by builder on 2012-
 FPC 2                    ROM        Juniper ROM Monitor Version 10.1b3
                         O/S        Version 12.3-20121220.0 by builder on 2012-
 FPC 3                    ROM        Juniper ROM Monitor Version 10.1b3
                         O/S        Version 12.3-20121220.0 by builder on 2012-
 FPC 4                    ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20121220.0 by builder on 2012-
 FPC 5                    ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20121220.0 by builder on 2012-
 FPC 6                    ROM        Juniper ROM Monitor Version 10.4b1
                         O/S        Version 12.3-20121220.0 by builder on 2012-
 FPC 7                    ROM        Juniper ROM Monitor Version 10.1b3
                         O/S        Version 12.3-20121220.0 by builder on 2012-
 FPC 8                    ROM        Juniper ROM Monitor Version 10.4b1
                         O/S        Version 12.3-20121220.0 by builder on 2012-
 FPC 9                    ROM        Juniper ROM Monitor Version 10.4b1
                         O/S        Version 12.3-20121220.0 by builder on 2012-
 SPMB 0                   ROM        Juniper ROM Monitor Version 12.1b1
                         O/S        Version 12.3-20121220.0 by builder on 2012-
 SPMB 1                   ROM        Juniper ROM Monitor Version 12.1b1
                         O/S        Version 12.3-20121220.0 by builder on 2012-

Part                     Type       Version
FPC 0                    ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20130415.0 by builder on 2013-
FPC 1                    ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20130415.0 by builder on 2013-
FPC 2                    ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20130415.0 by builder on 2013-
FPC 3                    ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20130415.0 by builder on 2013-
FPC 4                    ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20130415.0 by builder on 2013-
 FPC 5                    ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20130415.0 by builder on 2013-
 FPC 6                    ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20130415.0 by builder on 2013-
 FPC 7                    ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20130415.0 by builder on 2013-
 FPC 8                    ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20130415.0 by builder on 2013-
 FPC 9                    ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20130415.0 by builder on 2013-
 FPC 10                   ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20130415.0 by builder on 2013-
 FPC 11                   ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20130415.0 by builder on 2013-
 FPC 12                   ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20130415.0 by builder on 2013-
 FPC 13                   ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20130415.0 by builder on 2013-
 FPC 14                   ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20130415.0 by builder on 2013-
 FPC 15                   ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20130415.0 by builder on 2013-
 FPC 16                   ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20130415.0 by builder on 2013-
 FPC 17                   ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20130415.0 by builder on 2013-
 FPC 18                   ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20130415.0 by builder on 2013-
 FPC 19                   ROM        Juniper ROM Monitor Version 10.0b39
                         O/S        Version 12.3-20130415.0 by builder on 2013-
 SPMB 0                   ROM        Juniper ROM Monitor Version 12.1b1
                         O/S        Version 12.3-20130415.0 by builder on 2013-
 SPMB 1                   ROM        Juniper ROM Monitor Version 12.1b1
                         O/S        Version 12.3-20130415.0 by builder on 2013-

Part                     Type       Version
FPC 1                    ROM        Juniper ROM Monitor Version 12.1b1
                         O/S        Version 12.2I21 by manish on 2012-06-19 17:

Part                   Type       Version
FPC 0                  uboot      U-Boot 1.1.6 (Feb  6 2008 - 11:27:42)
                       loader     FreeBSD/PowerPC U-Boot bootstrap loader 2.1
FPC 1                  uboot      U-Boot 1.1.6 (Feb  6 2008 - 11:27:42)
                       loader     FreeBSD/PowerPC U-Boot bootstrap loader 2.1
FPC 2                  uboot      U-Boot 1.1.6 (Feb  6 2008 - 11:27:42)
                       loader     FreeBSD/PowerPC U-Boot bootstrap loader 2.1

Part                     Type       Version
FPC 0                    U-Boot     U-Boot 1.1.6 (Mar 25 2009 - 06:13:12) 2.4.0
                         loader     FreeBSD/PowerPC U-Boot bootstrap loader 2.2
FPC 3                    U-Boot     U-Boot 1.1.6 (Dec  4 2009 - 13:17:34) 3.1.0
                         loader     FreeBSD/PowerPC U-Boot bootstrap loader 2.2
FPC 5                    U-Boot     U-Boot 1.1.6 (Mar 25 2009 - 06:13:12) 2.4.0
                         loader     FreeBSD/PowerPC U-Boot bootstrap loader 2.2
FPC 7                    U-Boot     U-Boot 1.1.6 (Feb  6 2009 - 05:31:46) 2.4.0
                         loader     FreeBSD/PowerPC U-Boot bootstrap loader 2.2
Routing Engine 0         U-Boot     U-Boot 1.1.6 (Mar 25 2009 - 06:13:12) 2.4.0
                         loader     FreeBSD/PowerPC U-Boot bootstrap loader 2.2                                                
Routing Engine 1         U-Boot     U-Boot 1.1.6 (Mar 25 2009 - 06:13:12) 2.4.0
                         loader     FreeBSD/PowerPC U-Boot bootstrap loader 2.2

lcc0-re0:
--------------------------------------------------------------------------
Part                     Type       Version
FPC 1                    ROM        Juniper ROM Monitor Version 6.4b18         
                         O/S        Version 7.0-20040804.0 by builder on 2004-0
FPC 2                    ROM        Juniper ROM Monitor Version 6.4b20         
                         O/S        Version 7.0-20040804.0 by builder on 2004-0
SPMB 0                   ROM        Juniper ROM Monitor Version 6.4b18         
                         O/S        Version 7.0-20040804.0 by builder on 2004-0
                         O/S        Version 7.0-20040804.0 by builder on 2004-0

{{master:0}}

```

**Help:** execute the command "show chassis firmware"

**Prompt:**
- juniper_junos>
- juniper_junos#

### show chassis cluster interfaces

**Output:**
```
Control link status: Down

Control interfaces:
Index   Interface        Status   Internal-SA
0       fxp1             Down     Disabled

 Fabric link status: Down

Fabric interfaces:
Name    Child-interface    Status
(Physical/Monitored)
fab0    ge-0/0/2           Down / Down
fab0

Redundant-ethernet Information:
Name         Status      Redundancy-group
reth0        Up          1
reth1        Up          3
reth2        Down        Not configured
reth3        Down        Not configured
reth4        Down        Not configured
 
Redundant-pseudo-interface Information:
Name         Status      Redundancy-group
lo0          Up          0

Interface Monitoring:
Interface         Weight    Status    Redundancy-group
ge-11/0/0         255       Down      1
ge-2/0/0          255       Up        1

```

**Help:** execute the command "show chassis cluster interfaces"

**Prompt:**
- juniper_junos>
- juniper_junos#

### show chassis cluster status

**Output:**
```
Monitor Failure codes:
CS  Cold Sync monitoring        FL  Fabric Connection monitoring
GR  GRES monitoring             HW  Hardware monitoring
IF  Interface monitoring        IP  IP monitoring
LB  Loopback monitoring         MB  Mbuf monitoring
NH  Nexthop monitoring          NP  NPC monitoring
SP  SPU monitoring              SM  Schedule monitoring

Cluster ID: 1
Node   Priority Status         Preempt Manual   Monitor-failures

Redundancy group: 0 , Failover count: 1
node0  100      primary        no      no       None
node1  0        lost           n/a     n/a      n/a

Redundancy group: 1 , Failover count: 1
node0  0        primary        no      no       CS
node1  0        lost           n/a     n/a      n/a

Redundancy group: 3 , Failover count: 1
node0  0        primary        no      no       CS
node1  0        lost           n/a     n/a      n/a

```

**Help:** execute the command "show chassis cluster status"

**Prompt:**
- juniper_junos>
- juniper_junos#

### show isis adjacency

**Output:**
```
Interface             System         L State        Hold (secs) SNPA
ge-0/0/2.0            CSR2           1  Up                   22  50:0:0:2:0:1
ge-0/0/2.0            CSR2           2  Up                   25  50:0:0:2:0:1
ge-0/0/2.0            XRv3           1  Up                    8  50:0:0:3:0:2
ge-0/0/2.0            XRv3           2  Up                    8  50:0:0:3:0:2
ge-0/0/3.0            XRv3           3  Up                   25

{{master:0}}

```

**Help:** execute the command "show isis adjacency"

**Prompt:**
- juniper_junos>
- juniper_junos#

### show system uptime

**Output:**
```
Current time: 2021-08-31 12:29:34 MSK
Time Source:  NTP CLOCK
System booted: 2021-02-26 18:30:12 MSK (26w3d 17:59 ago)
Protocols started: 2021-02-26 18:34:06 MSK (26w3d 17:55 ago)
Last configured: 2021-07-13 16:35:18 MSK (6w6d 19:54 ago) by admin
12:29PM  up 185 days, 17:59, 1 user, load averages: 0.11, 0.05, 0.01
```

**Help:** execute the command "show system uptime"

**Prompt:**
- juniper_junos>
- juniper_junos#

### show ethernet-switching table

**Output:**
```

MAC flags (S - static MAC, D - dynamic MAC, L - locally learned, P - Persistent static
           SE - statistics enabled, NM - non configured MAC, R - remote PE MAC, O - ovsdb MAC)


Ethernet switching table : 2 entries, 2 learned
Routing instance : default-switch
    Vlan                MAC                 MAC         Age    Logical
    name                address             flags              interface
    Vlan100             2c:5a:0f:bc:a3:cd   DL            -   ae112.0
    Vlan100             ca:fe:ca:fe:00:07   DL            -   ae112.0

{{master:0}}

```

**Help:** execute the command "show ethernet-switching table"

**Prompt:**
- juniper_junos>
- juniper_junos#

### show ospf neighbor

**Output:**
```
Address          Interface              State     ID               Pri  Dead
10.1.2.2         ge-0/0/2.0             Full      2.2.2.2            1    37
10.1.3.3         ge-0/0/3.0             Full      3.3.3.3            1    31

{{master:0}}

```

**Help:** execute the command "show ospf neighbor"

**Prompt:**
- juniper_junos>
- juniper_junos#

### show lldp neighbors

**Output:**
```
Local Interface    Parent Interface    Chassis Id          Port info          System Name
ge-0/0/1           -                   2c:6b:f5:a1:c2:c0   ge-0/0/1           vmx2
ge-0/0/0           -                   2c:6b:f5:a2:08:c0   ge-0/0/0           vmx3
```

**Help:** execute the command "show lldp neighbors"

**Prompt:**
- juniper_junos>
- juniper_junos#

### show version

**Output:**
```
fpc0:
--------------------------------------------------------------------------
 Hostname: lab
Model: ex4550-32f
JUNOS EX  Software Suite [13.2X51-D35.3]
 JUNOS FIPS mode utilities [13.2X51-D35.3]
JUNOS Online Documentation [13.2X51-D35.3]
 JUNOS EX 4500 Software Suite [13.2X51-D35.3]
JUNOS Web Management [13.2X51-D35.3]
 
fpc1:
--------------------------------------------------------------------------
 Hostname: lab
Model: ex4550-32f
JUNOS EX  Software Suite [13.2X51-D35.3]
 JUNOS FIPS mode utilities [13.2X51-D35.3]
JUNOS Online Documentation [13.2X51-D35.3]
 JUNOS EX 4500 Software Suite [13.2X51-D35.3]
JUNOS Web Management [13.2X51-D35.3]

{{master:0}}

```

**Help:** execute the command "show version"

**Prompt:**
- juniper_junos>
- juniper_junos#

### set cli screen-length 0

**Output:** None

**Help:** Execute the command set cli screen-length 0. This automatically generated. Feel free to change it!

**Prompt:**
- juniper_junos>
- juniper_junos#

### set cli complete-on-space off

**Output:** None

**Help:** Execute the command set cli complete-on-space off. This automatically generated. Feel free to change it!

**Prompt:**
- juniper_junos>
- juniper_junos#

