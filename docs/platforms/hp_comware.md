# hp_comware


!!! warning
    This is automatically generated. In case of any issues, 
    please refer to the source code or, even better, 
    open an issue on the GitHub repository. Thanks! 🤗📖
## Platforms:

## Commands

### enable

**Output:** None

**Help:** enter enable mode

**Prompt:**
- hp_comware>

### screen-length disable

**Output:** None

**Help:** set the terminal width to maximum

**Prompt:**
- hp_comware>
- hp_comware#

### ex

**Output:**
```
True
```

**Help:** exit the terminal

**Prompt:**
- hp_comware>
- hp_comware#

### display vlan all

**Output:**
```
 VLAN ID: 1
 VLAN type: Static
 Route interface: Not configured
 Description: VLAN 0001
 Name: VLAN 0001
 Tagged ports:   None
 Untagged ports: 
    Bridge-Aggregation1           Bridge-Aggregation2           
    Bridge-Aggregation3           Bridge-Aggregation4           
    Ten-GigabitEthernet1/0/1      
    Ten-GigabitEthernet1/0/2      

 VLAN ID: 100
 VLAN type: Static
 Route interface: Configured
 IPv4 address: 10.9.0.1
 IPv4 subnet mask: 255.255.255.0
 Description: User VLAN
 Name: VLAN_100
 Tagged ports:   
    Bridge-Aggregation5           Bridge-Aggregation6           
    Ten-GigabitEthernet1/0/1      
    Ten-GigabitEthernet1/0/3      
 Untagged ports: None

 VLAN ID: 101
 VLAN type: Static
 Route interface: Configured
 IPv4 address: 10.9.1.1
 IPv4 subnet mask: 255.255.255.0
 Description: VLAN 101
 Name: VLAN_101
 Tagged ports:   
    Bridge-Aggregation7           Bridge-Aggregation8           
    Ten-GigabitEthernet2/0/35     
    Ten-GigabitEthernet2/0/37     
 Untagged ports:
    Ten-GigabitEthernet1/0/46     

```

**Help:** execute the command "display vlan all"

**Prompt:**
- hp_comware>
- hp_comware#

### display interface brief

**Output:**
```
The brief information of interface(s) under route mode:
Link: ADM - administratively down; Stby - standby
Protocol: (s) - spoofing
Interface            Link Protocol Main IP         Description
Aux0                 UP   UP       --
Cellular0/0          DOWN DOWN     --
GE0/0                UP   UP       192.168.100.1   The interface for connecting RouterA.
Loop0                UP   UP(s)    --              --
MP0                  DOWN DOWN     --
NULL0                UP   UP(s)    --              --
Vlan1                DOWN DOWN     192.168.1.1

The brief information of interface(s) under bridge mode:
Link: ADM - administratively down; Stby - standby
Speed or Duplex: (a)/A - auto; H - half; F - full
Type: A - access; T - trunk; H - hybrid
Interface            Link Speed   Duplex Type PVID Description
GE0/1                DOWN auto    A      A    1
GE0/2                DOWN auto    A      A    1
GE0/3                DOWN auto    A      A    1
GE0/4                DOWN auto    A      A    1

```

**Help:** execute the command "display interface brief"

**Prompt:**
- hp_comware>
- hp_comware#

### display device manuinfo

**Output:**
```

 Slot 1 CPU 0:
 DEVICE_NAME          : SecPath F1000-AK115
 DEVICE_SERIAL_NUMBER : 219801A1C39214Q00075
 MAC_ADDRESS          : 1451-7EB8-D4DE
 MANUFACTURING_DATE   : 2021-04-14
 VENDOR_NAME          : H3C
Power 0:
The operation is not supported on the specified power.

```

**Help:** execute the command "display device manuinfo"

**Prompt:**
- hp_comware>
- hp_comware#

### display lldp neighbor-information list

**Output:**
```
Chassis ID : * -- -- Nearest nontpmr bridge neighbor
             # -- -- Nearest customer bridge neighbor
             Default -- -- Nearest bridge neighbor
Local Interface Chassis ID      Port ID                    System Name          
XGE1/0/0/1      bcea-fa00-0033  Ten-GigabitEthernet1/0/47  SWITCH01
XGE1/0/0/2      bcea-fa00-0033  Ten-GigabitEthernet2/0/47  SWITCH01

```

**Help:** execute the command "display lldp neighbor-information list"

**Prompt:**
- hp_comware>
- hp_comware#

### display arp

**Output:**
```
  Type: S-Static   D-Dynamic   O-Openflow   R-Rule   M-Multiport  I-Invalid
 IP address      MAC address    VLAN     Interface                Aging Type
10.20.10.1      001e-c1dc-fc01 N/A      M-GE0/0/0                16    D
10.20.1.254     001e-c1dc-fc01 1        XGE1/0/47                16    D
10.20.1.2       2c23-3a40-7e18 1        XGE1/0/48                5     D

```

**Help:** execute the command "display arp"

**Prompt:**
- hp_comware>
- hp_comware#

### display ip routing-table

**Output:**
```
<HS125X>dis ip routing-table 

Destinations : 17604     Routes : 28601

Destination/Mask    Proto  Pre  Cost         NextHop         Interface
0.0.0.0/32          Direct 0    0            127.0.0.1       InLoop0
9.72.47.0/24        OSPF   150  1            172.16.43.2     Vlan1600
                                             172.16.43.6     Vlan1601
10.1.0.0/16         OSPF   10   14           172.16.43.2     Vlan1600
                                             172.16.43.6     Vlan1601
10.1.14.0/24        Static 60   0            172.16.39.2     Vlan1920
0.0.0.0/0          Static  60  0           192.168.56.1      GE0/1
1.1.1.0/24         Static  60  0           192.168.56.1      GE0/1
                                           192.168.56.2      GE0/2
                                           192.168.56.3      GE0/3
127.0.0.0/8        Direct  0   0           127.0.0.1         InLoop0
127.0.0.0/32       Direct  0   0           127.0.0.1         InLoop0
127.0.0.1/32       Direct  0   0           127.0.0.1         InLoop0
127.255.255.255/32 Direct  0   0           127.0.0.1         InLoop0
192.168.56.0/24    Direct  0   0           192.168.56.101    GE0/1
192.168.56.0/32    Direct  0   0           192.168.56.101    GE0/1
192.168.56.101/32  Direct  0   0           127.0.0.1         InLoop0
192.168.56.255/32  Direct  0   0           192.168.56.101    GE0/1
224.0.0.0/4        Direct  0   0           0.0.0.0           NULL0
224.0.0.0/24       Direct  0   0           0.0.0.0           NULL0
255.255.255.255/32 Direct  0   0           127.0.0.1         InLoop0
9.72.47.0/24        BGP    130  0          172.16.42.221     GE0/0/9
                    BGP    130  0          172.16.42.229     GE0/0/10
10.1.0.0/16         OSPF   10   13         172.16.43.82      GE0/0/45
10.1.14.0/24        O_ASE  150  1          172.16.43.1       RAGG40
10.1.208.0/20       O_ASE  150  1          172.16.43.82      GE0/0/45
10.210.0.0/16       BGP    130  0          10.6.12.106       GE9/1/3.1132
10.210.4.0/24       BGP    130  0          172.16.42.221     GE0/0/9
                    BGP    130  0          172.16.42.229     GE0/0/10
10.210.4.201/32     O_ASE  150  1          172.16.43.10      RAGG44
10.211.0.0/16       BGP    130  0          10.6.12.86        GE9/1/1.1114

```

**Help:** execute the command "display ip routing-table"

**Prompt:**
- hp_comware>
- hp_comware#

### display ip vpn-instance

**Output:**
```
  Total VPN-Instances configured : 1
  VPN-Instance Name               RD                     Create time
  red                             1:1                    2017/05/18 05:48:17
  green                           2:4                    2017/05/18 05:48:21
  blue                            5:7                    2017/05/18 05:48:47
  black                                                  2017/05/18 05:48:53

```

**Help:** execute the command "display ip vpn-instance"

**Prompt:**
- hp_comware>
- hp_comware#

### display clock

**Output:**
```
10:09:00 UTC Fri 03/16/2015
```

**Help:** execute the command "display clock"

**Prompt:**
- hp_comware>
- hp_comware#

### display link-aggregation verbose

**Output:**
```
Loadsharing Type: Shar -- Loadsharing, NonS -- Non-Loadsharing
Port Status: S -- Selected, U -- Unselected
Flags:  A -- LACP_Activity, B -- LACP_Timeout, C -- Aggregation,
        D -- Synchronization, E -- Collecting, F -- Distributing,
        G -- Defaulted, H -- Expired

Aggregation Interface: Route-Aggregation1
 Aggregation Mode: Dynamic
Loadsharing Type: Shar
System ID: 0x8000, aaaa-bbbb-75bc
Local:
  Port             Status  Priority Oper-Key  Flag
--------------------------------------------------------------------------------
  GE0/0/0          S       32768    1         {{ACDEF}}
  GE0/0/1          S       32768    1         {{ACDEF}}
Remote:
  Actor            Partner Priority Oper-Key  SystemID               Flag
--------------------------------------------------------------------------------
  GE0/0/0          21      32768    7         0x8000, aaaa-bbbb-6485 {{ACDEF}}
  GE0/0/1          23      32768    7         0x8000, aaaa-bbbb-6485 {{ACDEF}}

```

**Help:** execute the command "display link-aggregation verbose"

**Prompt:**
- hp_comware>
- hp_comware#

### display vlan brief

**Output:**
```
Brief information about all VLANs:
Supported Minimum VLAN ID: 1
Supported Maximum VLAN ID: 4094
Default VLAN ID: 1
VLAN ID   Name                             Port
1         VLAN 0001                        FGE1/0/1  FGE1/0/2  FGE1/0/3
                                           FGE1/0/4  FGE1/0/5  FGE1/0/6
                                           FGE1/0/7  FGE1/0/8  FGE1/0/9
                                           FGE1/0/10  FGE1/0/11  FGE1/0/12
                                           FGE1/0/13  FGE1/0/14  FGE1/0/15
                                           FGE1/0/16  FGE1/0/17  FGE1/0/18
                                           FGE1/0/19  FGE1/0/20  FGE1/0/22
                                           FGE1/0/23  FGE1/0/24  FGE1/0/25
                                           FGE1/0/26  FGE1/0/27  FGE1/0/28
                                           FGE1/0/29  FGE1/0/30  FGE1/0/31
                                           FGE1/0/32
10        VLAN 0010                        FGE1/0/21
20        VLAN 0020
30        VLAN 0030
200       VLAN 0200
500       VLAN 0500
```

**Help:** execute the command "display vlan brief"

**Prompt:**
- hp_comware>
- hp_comware#

### display lldp neighbor-information verbose

**Output:**
```
LLDP neighbor-information of port 1[Ten-GigabitEthernet1/0/0/1]:
LLDP agent nearest-bridge:
 LLDP neighbor index : 1
 Update time         : 457 days, 22 hours, 1 minutes, 46 seconds
 Chassis type        : MAC address
 Chassis ID          : 70f9-6d6b-1234
 Port ID type        : Interface name
 Port ID             : GigabitEthernet0/0/1
 Time to live        : 120
 Port description    : TO_CORE_1
 System name         : SW1
 System description  : H3C Comware software. H3C SR8800 Product Version SR8800-C
                       MW520-R3725P01. Copyright (c) 2004-2014 Hangzhou H3C Tech
                       . Co., Ltd. All rights reserved.
 System capabilities supported : Bridge, Router
 System capabilities enabled   : Bridge, Router
 Link aggregation supported : Yes
 Link aggregation enabled   : Yes
 Aggregation port ID        : 71
 Auto-negotiation supported : No
 Auto-negotiation enabled   : Yes
 OperMau                    : Speed(1000)/Duplex(Full)
 Power port class           : PD
 PSE power supported        : No
 PSE power enabled          : No
 PSE pairs control ability  : No
 Power pairs                : Signal
 Port power classification  : Class 0
 Maximum frame size         : 9216

LLDP neighbor-information of port 2[Ten-GigabitEthernet1/0/0/2]:
 LLDP agent nearest-bridge:
 LLDP neighbor index : 1
 Update time         : 457 days, 22 hours, 1 minutes, 38 seconds
 Chassis type        : MAC address
 Chassis ID          : 70f9-6d17-1235
 Port ID type        : Interface name
 Port ID             : Ten-GigabitEthernet1/0/0/5
 Time to live        : 120
 Port description    : TO_CORE_2
 System name         : SW2
 System description  : H3C Comware Platform Software, Software Version 7.1.045, 
                       Release 1005P09
                       H3C S12510-X
                       Copyright (c) 2004-2014 Hangzhou H3C Tech. Co., Ltd. All 
                       rights reserved.
 System capabilities supported : Bridge, Router, Customer Bridge, Service Bridge
 System capabilities enabled   : Bridge, Router, Customer Bridge
 Management address type           : IPv4
 Management address                : 10.6.5.4
 Management address interface type : IfIndex
 Management address interface ID   : 6576
 Management address OID            : 0
 Port VLAN ID(PVID)  : 10
 Link aggregation supported : Yes
 Link aggregation enabled   : Yes
 Aggregation port ID        : 5
 Auto-negotiation supported : Yes
 Auto-negotiation enabled   : Yes
 OperMau                    : Speed(10000)/Duplex(Full)
 Power port class           : PSE
 PSE power supported        : No
 PSE power enabled          : No
 PSE pairs control ability  : No
 Power pairs                : Signal
 Port power classification  : Class 0
 Maximum frame size         : 9216

LLDP neighbor-information of port 3[Ten-GigabitEthernet1/0/0/3]:
LLDP agent nearest-bridge:
 LLDP neighbor index : 1
 Update time         : 457 days, 22 hours, 1 minutes, 31 seconds
 Chassis type        : MAC address
 Chassis ID          : 70f9-6d17-1236
 Port ID type        : Interface name
 Port ID             : Ten-GigabitEthernet2/0/0/5
 Time to live        : 120
 Port description    : TO_SPINE
 System name         : SW3
 System description  : H3C Comware Platform Software, Software Version 7.1.045, 
                       Release 1005P09
                       H3C S12510-X
                       Copyright (c) 2004-2014 Hangzhou H3C Tech. Co., Ltd. All 
                       rights reserved.
 System capabilities supported : Bridge, Router, Customer Bridge, Service Bridge
 System capabilities enabled   : Bridge, Router, Customer Bridge
 Management address type           : IPv4
 Management address                : 10.6.5.3
 Management address interface type : IfIndex
 Management address interface ID   : 6576
 Management address OID            : 0
 Port VLAN ID(PVID)  : 10
 Link aggregation supported : Yes
 Link aggregation enabled   : Yes
 Aggregation port ID        : 1565
 Auto-negotiation supported : Yes
 Auto-negotiation enabled   : Yes
 OperMau                    : Speed(10000)/Duplex(Full)
 Power port class           : PSE
 PSE power supported        : No
 PSE power enabled          : No
 PSE pairs control ability  : No
 Power pairs                : Signal
 Port power classification  : Class 0
 Maximum frame size         : 9216

 [H3C-GigabitEthernet0/0]dis lldp neighbor-information verbose
LLDP neighbor-information of port 1[GigabitEthernet0/0]:
 LLDP agent nearest-bridge:
 LLDP neighbor index : 1
 Update time         : 0 days, 0 hours, 3 minutes, 9 seconds
 Chassis type        : MAC address
 Chassis ID          : 4c1c-503a-1234
 Port ID type        : Interface name
 Port ID             : GigabitEthernet0/0
 Time to live        : 121
 Port description    : GigabitEthernet0/0 Interface
 System name         : Test-Router
 System description  : H3C Comware Platform Software, Software Version 7.1.075,
                       Alpha 7571
                       H3C MSR36-20
                       Copyright (c) 2004-2017 New H3C Technologies Co., Ltd. Al
                       l rights reserved.
 System capabilities supported : Bridge, Router, Customer Bridge, Service Bridge
 System capabilities enabled   : Bridge, Router, Customer Bridge
 Management address type           : IPv4
 Management address                : 10.1.1.2
 Management address interface type : IfIndex
 Management address interface ID   : 1
 Management address OID            : 0
 Link aggregation supported : Yes
 Link aggregation enabled   : No
 Aggregation port ID        : 0
 Auto-negotiation supported : No
 Auto-negotiation enabled   : No
 OperMau                    : Speed(0)/Duplex(Unknown)
 Power port class           : PSE
 PSE power supported        : Yes
 PSE power enabled          : No
 PSE pairs control ability  : Yes
 Power pairs                : Signal
 Port power classification  : Class 0
 Maximum frame size         : 9216
```

**Help:** execute the command "display lldp neighbor-information verbose"

**Prompt:**
- hp_comware>
- hp_comware#

### display interface

**Output:**
```
Vlan-interface2000
Current state: UP
Line protocol state: UP
Description: Servers
Bandwidth: 10000000 kbps
Maximum transmission unit: 1500
Internet address: 10.1.1.1/24 (Primary)
IP packet frame type: Ethernet II, hardware address: abab-cdcd-6486
IPv6 packet frame type: Ethernet II, hardware address: abab-cdcd-6486
Last clearing of counters: Never
Last 300 seconds input rate: 7 bytes/sec, 56 bits/sec, 0 packets/sec
Last 300 seconds output rate: 16 bytes/sec, 128 bits/sec, 0 packets/sec
Input: 9103 packets, 611444 bytes, 0 drops
Output: 18587 packets, 1143610 bytes, 0 drops

Bridge-Aggregation20
Current state: UP
Line protocol state: UP
IP packet frame type: Ethernet II, hardware address: abab-cdcd-6485
Description: FIRST_BLOCK
Bandwidth: 40000000 kbps
40Gbps-speed mode, full-duplex mode
Link speed type is autonegotiation, link duplex type is autonegotiation
PVID: 1
Port link-type: Trunk
 VLAN Passing:   1(default vlan), 4001-4002
 VLAN permitted: 1(default vlan), 2001-2020, 2190, 4001-4002
 Trunk port encapsulation: IEEE 802.1q
Last clearing of counters: Never
Last 300 seconds input:  3143 packets/sec 929430 bytes/sec 0%
Last 300 seconds output:  5674 packets/sec 5945156 bytes/sec 0%
Input (total):  80274398 packets, 24384580165 bytes
        80218843 unicasts, 12 broadcasts, 55543 multicasts, 0 pauses
Input (normal):  80274398 packets, - bytes
        80218843 unicasts, 12 broadcasts, 55543 multicasts, 0 pauses
Input:  0 input errors, 0 runts, 0 giants, 0 throttles
        0 CRC, 0 frame, - overruns, 0 aborts
        - ignored, - parity errors
Output (total): 110103849 packets, 90115617821 bytes
        109953707 unicasts, 9 broadcasts, 150133 multicasts, 0 pauses
 Output (normal): 110103849 packets, - bytes
        109953707 unicasts, 9 broadcasts, 150133 multicasts, 0 pauses
Output: 0 output errors, - underruns, - buffer failures
        0 aborts, 0 deferred, 0 collisions, 0 late collisions
        0 lost carrier, - no carrier

GigabitEthernet1/1/0/31
Current state: DOWN
Line protocol state: DOWN
IP packet frame type: Ethernet II, hardware address: abab-cdcd-6485
Description: WIFI
Bandwidth: 1000000 kbps
Loopback is not set
Media type is twisted pair, port hardware type is 1000_BASE_T
 Unknown-speed mode, unknown-duplex mode
Link speed type is autonegotiation, link duplex type is autonegotiation
Flow-control is not enabled
Maximum frame length: 9216
Allow jumbo frames to pass
Broadcast max-ratio: 100%
Multicast max-ratio: 100%
Unicast max-ratio: 100%
PVID: 2190
MDI type: Automdix
Port link-type: Trunk
 VLAN Passing:   2000, 3230, 4001-4005, 4049-4052
 VLAN permitted: 2-4094
 Trunk port encapsulation: IEEE 802.1q
Port priority: 0
Last link flapping: Never
Last clearing of counters: Never
Current system time:2022-12-04 09:59:42 EEST+03:00:00
Last time when physical state changed to up:-
Last time when physical state changed to down:2022-12-03 14:48:11 EEST+03:00:00
 Peak input rate: 0 bytes/sec, at 2022-12-03 14:48:40 
Peak output rate: 0 bytes/sec, at 2022-12-03 14:48:40 
Last 300 seconds input: 0 packets/sec 0 bytes/sec -%
 Last 300 seconds output: 0 packets/sec 0 bytes/sec -%
Input (total):  0 packets, 0 bytes
        0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses
Input (normal):  0 packets, - bytes
        0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses
Input:  0 input errors, 0 runts, 0 giants, 0 throttles
        0 CRC, 0 frame, - overruns, 0 aborts
        - ignored, - parity errors
Output (total): 0 packets, 0 bytes
        0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses
 Output (normal): 0 packets, - bytes
        0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses
Output: 0 output errors, - underruns, - buffer failures
        0 aborts, 0 deferred, 0 collisions, 0 late collisions
        0 lost carrier, - no carrier
IPv4 traffic statistics:
 Last 300 seconds input rate: 0 packets/sec, 0 bytes/sec
 Last 300 seconds output rate: 0 packets/sec, 0 bytes/sec
 Input: 0 packets, 0 bytes
 Output: 0 packets, 0 bytes
IPv6 traffic statistics:
 Last 300 seconds input rate: 0 packets/sec, 0 bytes/sec
 Last 300 seconds output rate: 0 packets/sec, 0 bytes/sec
 Input: 0 packets, 0 bytes
 Output: 0 packets, 0 bytes

Ten-GigabitEthernet1/0/1
Current state: DOWN
Line protocol state: DOWN
IP packet frame type: Ethernet II, hardware address: 000c-2963-b767
 Description: Ten-GigabitEthernet1/0/1 Interface
Bandwidth: 100000 kbps
Loopback is not set
Media type is twisted pair, port hardware type is 1000_BASE_T_AN_SFP
 Unknown-speed mode, unknown-duplex mode
Link speed type is autonegotiation, link duplex type is autonegotiation
Flow-control is not enabled
Maximum frame length: 9216
Allow jumbo frame to pass
Broadcast max-ratio: 100%
Multicast max-ratio: 100%
Unicast max-ratio: 100%
PVID: 1
MDI type: Automdix
Port link-type: Access
 Tagged VLANs:   None
 UnTagged VLANs: 1
Port priority: 2
Last link flapping: 6 hours 39 minutes 25 seconds
Last clearing of counters:  14:34:09 Tue 11/01/2011
Peak input rate: 0 bytes/sec, at 2013-07-17 22:06:19
 Peak output rate: 0 bytes/sec, at 2013-07-17 22:06:19
Last 300 second input:  0 packets/sec 0 bytes/sec -%
Last 300 second output:  0 packets/sec 0 bytes/sec -%
Input (total):  0 packets, 0 bytes
        0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses
Input (normal):  0 packets, 0 bytes
        0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses
Input:  0 input errors, 0 runts, 0 giants, 0 throttles
        0 CRC, 0 frame, 0 overruns, 0 aborts
        0 ignored, 0 parity errors
Output (total): 0 packets, 0 bytes
        0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses
Output (normal): 0 packets, 0 bytes
        0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses
Output: 0 output errors, 0 underruns, 0 buffer failures
        0 aborts, 0 deferred, 0 collisions, 0 late collisions
        0 lost carrier, 0 no carrier

```

**Help:** execute the command "display interface"

**Prompt:**
- hp_comware>
- hp_comware#

### display ip vpn-instance instance-name

**Output:**
```
  VPN-Instance Name and Index : vpnb, 2
  Route Distinguisher : 100:2
  Interfaces : Vlan-interface20, FortyGigE1/0/53,
               GigabitEthernet1/0/25
  Address-family IPv4:
   Export VPN Targets :
       222:2
   Import VPN Targets :
       222:2 111:1

```

**Help:** execute the command "display ip vpn-instance instance-name"

**Prompt:**
- hp_comware>
- hp_comware#

### display ip interface

**Output:**
```
Route-Aggregation1.4 current state :UP
Line protocol current state :UP
 Internet Address is 10.1.1.1/24 Primary
Broadcast address : 10.1.1.255
The Maximum Transmit Unit : 1500 bytes
input packets : 519880114, bytes : 2114446514, multicasts : 1523365
output packets : 892477481, bytes : 2635360909, multicasts : 1513360
ARP packet input number:        4648
  Request packet:                  9
  Reply packet:                 4639
  Unknown packet:                  0
TTL invalid packet number:   1067079
ICMP packet input number:         27
  Echo reply:                     15
  Unreachable:                     0
  Source quench:                   0
  Routing redirect:                0
  Echo request:                    0
  Router advert:                   0
  Router solicit:                  0
  Time exceed:                    12
  IP header bad:                   0
  Timestamp request:               0
  Timestamp reply:                 0
  Information request:             0
  Information reply:               0
  Netmask request:                 0
  Netmask reply:                   0
  Unknown type:                    0
Policy routing is enabled, using route map TO_INTERNET

```

**Help:** execute the command "display ip interface"

**Prompt:**
- hp_comware>
- hp_comware#

### display mac-address

**Output:**
```
MAC ADDR       VLAN ID  STATE          PORT INDEX               AGING TIME(s)
0000-1111-2222 1        Learned        Bridge-Aggregation1      AGING
 fedc-ba09-8765 10       Learned        GigabitEthernet1/0/20    NOAGED
aaaa-bbbb-cccc 10       Learned        GigabitEthernet1/0/41    AGING
dead-beef-0042 20       Learned        GigabitEthernet1/0/10    AGING

```

**Help:** execute the command "display mac-address"

**Prompt:**
- hp_comware>
- hp_comware#

### display counters bound interface

**Output:**
```
Interface         Total (pkts)   Broadcast (pkts)   Multicast (pkts)  Err (pkts)
GE1/0/1                 573422               2580               8560           0
GE1/0/2                 975121               7513              34906          30
GE6/0/47                     0                  0                  0           0
GE6/0/48             429854186              16658              86584           0
XGE1/0/49          17495987683           12706052        16927885391           0
XGE1/0/50          53840866263           13138308        21011041401          19
XGE6/0/51                    0                  0                  0           0
XGE6/0/52                46490              16009               7582           0

 Overflow: More than 14 digits (7 digits for column "Err").
       --: Not supported.

```

**Help:** execute the command "display counters bound interface"

**Prompt:**
- hp_comware>
- hp_comware#

