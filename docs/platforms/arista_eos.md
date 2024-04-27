# arista_eos


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
- arista_eos>

### terminal width 511

**Output:**
```
Width set to 511
```

**Help:** set the terminal width to maximum

**Prompt:**
- arista_eos>
- arista_eos#

### terminal length 0

**Output:**
```
Pagination disabled
```

**Help:** It disables the pagination

**Prompt:**
- arista_eos>
- arista_eos#

### show ip bgp

**Output:**
```
BGP routing table information for VRF default
Router identifier 10.103.1.1, local AS number 103
Route status codes: s - suppressed, * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup
Origin codes: i - IGP, e - EGP, ? - incomplete
 AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

       Network             Next Hop         Metric  LocPref Weight Path
 * >   10.103.1.0/24       -                1       0       -       i
 * >   10.103.2.0/24       -                1       0       -       i
 * >   10.103.3.0/24       -                1       0       -       i
 * >   10.103.4.0/24       -                1       0       -       i
 * #   10.104.1.0/24       10.10.10.20      0       100     0       104 i
 * #   10.104.2.0/24       10.10.10.20      0       100     0       104 i
 * #   10.104.3.0/24       10.10.10.20      0       100     0       104 i
 * #   10.104.4.0/24       10.10.10.20      0       100     0       104 i
BGP routing table information for VRF INTERNET
Router identifier 172.26.159.40, local AS number 62222.4003
Route status codes: s - suppressed, * - valid, > - active, # - not installed, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
 Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

         Network                Next Hop            Metric  LocPref Weight  Path
 * >     10.9.41.96/29          172.26.159.6          0       5000    0       62222.4002 ?

```

**Help:** execute the command "show ip bgp"

**Prompt:**
- arista_eos>
- arista_eos#

### show processes top once

**Output:**
```
top - 18:53:50 up 3 days,  1:06,  2 users,  load average: 0.15, 0.08, 0.09
Tasks: 202 total,   1 running, 201 sleeping,   0 stopped,   0 zombie
%Cpu(s):  2.8 us,  0.7 sy,  0.0 ni, 96.3 id,  0.0 wa,  0.2 hi,  0.0 si,  0.0 st
KiB Mem:   2014520 total,  1970928 used,    43592 free,   171340 buffers
 KiB Swap:        0 total,        0 used,        0 free,  1156836 cached

  PID USER      PR  NI  VIRT  RES  SHR S  %CPU %MEM    TIME+  COMMAND
    1 root      20   0  8608 5920 4376 S   0.0  0.3   0:12.51 systemd
    2 root      20   0     0    0    0 S   0.0  0.0   0:00.01 kthreadd
    3 root      20   0     0    0    0 S   0.0  0.0   0:04.69 ksoftirqd/0
    5 root       0 -20     0    0    0 S   0.0  0.0   0:00.00 kworker/0:0H
    6 root      20   0     0    0    0 S   0.0  0.0   0:00.00 kworker/u2:0
    7 root      20   0     0    0    0 S   0.0  0.0   0:02.74 rcu_preempt
    8 root      20   0     0    0    0 S   0.0  0.0   0:00.00 rcu_sched
    9 root      20   0     0    0    0 S   0.0  0.0   0:00.00 rcu_bh
 2634 root      20   0  451m 136m 108m S   0.0  6.9  13:28.08 Etba
 2635 root      20   0  430m  15m    4 S   0.0  0.8   0:00.00 netnsd-session
```

**Help:** execute the command "show processes top once"

**Prompt:**
- arista_eos>
- arista_eos#

### show module

**Output:**
```
Module  Ports Card Type                Model          Serial No.
------- ----- ------------------------ -------------- -----------
1       3     DCS-7500-SUP2 Supervisor DCS-7500-SUP2  XX16380393
3       144   36-port QSFP100 Linecard 7500R-36CQ-LC  XX16340219
4       144   36-port QSFP100 Linecard 7500R-36CQ-LC  XX16364164
5       144   36-port QSFP100 Linecard 7500R-36CQ-LC  XX16364166
6       144   36-port QSFP100 Linecard 7500R-36CQ-LC  XX16351233
7       144   36-port QSFP100 Linecard 7500R2-36CQ-LC XX17341299
Fabric1 0     DCS-7508R Fabric         7508R-FM       XX16472732
Fabric2 0     DCS-7508R Fabric         7508R-FM       XX16472587
Fabric3 0     DCS-7508R Fabric         7508R-FM       XX16320292
Fabric4 0     DCS-7508R Fabric         7508R-FM       XX16320357
 Fabric5 0     DCS-7508R Fabric         7508R-FM       XX16320439
Fabric6 0     DCS-7508R Fabric         7508R-FM       XX16320585

Module  MAC addresses                         Hw    Sw
------- ------------------------------------- ----- -------
1       44:4c:a8:e6:17:5e - 44:4c:a8:e6:17:5f 14.20 4.19.5M
3       44:4c:a8:e2:d0:28 - 44:4c:a8:e2:d0:b7 13.00
4       44:4c:a8:ee:a9:2c - 44:4c:a8:ee:a9:bb 13.00
5       44:4c:a8:ee:97:2c - 44:4c:a8:ee:97:bb 13.00
6       44:4c:a8:ee:2f:1c - 44:4c:a8:ee:2f:ab 13.00
7       28:99:3a:a4:01:58 - 28:99:3a:a4:01:e7 12.01
Fabric1                                       12.03
Fabric2                                       12.03
Fabric3                                       12.03
Fabric4                                       12.03
Fabric5                                       12.03
Fabric6                                       12.03

Module  Status Uptime
------- ------ ----------------
1       Active
3       Ok     74 days, 0:25:22
4       Ok     74 days, 0:25:22
5       Ok     74 days, 0:25:22
6       Ok     74 days, 0:25:22
7       Ok     74 days, 0:25:22
Fabric1 Ok     74 days, 0:25:22
Fabric2 Ok     74 days, 0:25:22
Fabric3 Ok     74 days, 0:25:22
 Fabric4 Ok     74 days, 0:25:22
Fabric5 Ok     74 days, 0:25:22
Fabric6 Ok     74 days, 0:25:22
```

**Help:** execute the command "show module"

**Prompt:**
- arista_eos>
- arista_eos#

### show interfaces

**Output:**
```
ceos1#show  interface

Ethernet1 is up, line protocol is up (connected)
  Hardware is Ethernet, address is aac1.ab3b.1c7a (bia aac1.ab3b.1c7a)
  Description: "Test interface Et1"
  Internet address is 10.0.0.1/30
  Broadcast address is 255.255.255.255
  IPv6 link-local address is fe80::a8c1:abff:fe3b:1c7a/64
  No IPv6 global unicast address is assigned
  IP MTU 1500 bytes (default), BW 1000000 kbit
  Full-duplex, 1Gb/s, auto negotiation: off, uni-link: n/a
  Up 21 minutes, 40 seconds
  Loopback Mode : None
  2 link status changes since last clear
  Last clearing of "show interface" counters never
  5 minutes input rate 0 bps (0.0% with framing overhead), 0 packets/sec
  5 minutes output rate 0 bps (0.0% with framing overhead), 0 packets/sec
     5280 packets input, 381190 bytes
     Received 1 broadcasts, 273 multicast
     0 runts, 0 giants
     0 input errors, 0 CRC, 0 alignment, 0 symbol, 0 input discards
     0 PAUSE input
     0 packets output, 0 bytes
     Sent 0 broadcasts, 0 multicast
     0 output errors, 0 collisions
     0 late collision, 0 deferred, 0 output discards
     0 PAUSE output
Ethernet2 is up, line protocol is up (connected)
  Hardware is Ethernet, address is aac1.ab31.e593 (bia aac1.ab31.e593)
  Description: "Test int Et2"
  Internet address is 192.168.1.1/30
  Broadcast address is 255.255.255.255
  IPv6 link-local address is fe80::a8c1:abff:fe31:e593/64
  No IPv6 global unicast address is assigned
  IP MTU 1500 bytes (default), BW 1000000 kbit
  Full-duplex, 1Gb/s, auto negotiation: off, uni-link: n/a
  Up 21 minutes, 40 seconds
  Loopback Mode : None
  2 link status changes since last clear
  Last clearing of "show interface" counters never
  5 minutes input rate 0 bps (0.0% with framing overhead), 0 packets/sec
  5 minutes output rate 0 bps (0.0% with framing overhead), 0 packets/sec
     5061 packets input, 362112 bytes
     Received 1 broadcasts, 61 multicast
     0 runts, 0 giants
     0 input errors, 0 CRC, 0 alignment, 0 symbol, 0 input discards
     0 PAUSE input
     0 packets output, 0 bytes
     Sent 0 broadcasts, 0 multicast
     0 output errors, 0 collisions
     0 late collision, 0 deferred, 0 output discards
     0 PAUSE output
Ethernet3 is up, line protocol is up (connected)
  Hardware is Ethernet, address is aac1.ab23.bb13 (bia aac1.ab23.bb13)
  Ethernet MTU 9214 bytes, BW 1000000 kbit
  Full-duplex, 1Gb/s, auto negotiation: off, uni-link: n/a
  Up 21 minutes, 40 seconds
  Loopback Mode : None
  2 link status changes since last clear
  Last clearing of "show interface" counters never
  5 minutes input rate 0 bps (0.0% with framing overhead), 0 packets/sec
  5 minutes output rate 0 bps (0.0% with framing overhead), 0 packets/sec
     900 packets input, 106797 bytes
     Received 0 broadcasts, 900 multicast
     0 runts, 0 giants
     0 input errors, 0 CRC, 0 alignment, 0 symbol, 0 input discards
     0 PAUSE input
     187 packets output, 16634 bytes
     Sent 0 broadcasts, 187 multicast
     0 output errors, 0 collisions
     0 late collision, 0 deferred, 0 output discards
     0 PAUSE output
 Ethernet4 is up, line protocol is up (connected)
  Hardware is Ethernet, address is aac1.abb1.4f2c (bia aac1.abb1.4f2c)
  Ethernet MTU 9214 bytes, BW 1000000 kbit
  Full-duplex, 1Gb/s, auto negotiation: off, uni-link: n/a
  Up 21 minutes, 40 seconds
  Loopback Mode : None
  2 link status changes since last clear
  Last clearing of "show interface" counters never
  5 minutes input rate 0 bps (0.0% with framing overhead), 0 packets/sec
  5 minutes output rate 0 bps (0.0% with framing overhead), 0 packets/sec
     705 packets input, 90157 bytes
     Received 0 broadcasts, 705 multicast
     0 runts, 0 giants
     0 input errors, 0 CRC, 0 alignment, 0 symbol, 0 input discards
     0 PAUSE input
     0 packets output, 0 bytes
     Sent 0 broadcasts, 0 multicast
     0 output errors, 0 collisions
     0 late collision, 0 deferred, 0 output discards
     0 PAUSE output
Loopback0 is up, line protocol is up (connected)
  Hardware is Loopback
  Internet address is 1.1.1.1/32
  Broadcast address is 255.255.255.255
  IP MTU 65535 bytes (default)
  Up 21 minutes, 51 seconds
 Management0 is up, line protocol is up (connected)
  Hardware is Ethernet, address is 001c.7338.71c6 (bia 001c.7338.71c6)
  Internet address is 172.20.20.2/24
  Broadcast address is 255.255.255.255
  IP MTU 1500 bytes (default), BW 1000000 kbit
  Full-duplex, 1Gb/s, auto negotiation: on, uni-link: n/a
  Up 21 minutes, 53 seconds
  Loopback Mode : None
  3 link status changes since last clear
  Last clearing of "show interface" counters never
  5 minutes input rate 426 bps (0.0% with framing overhead), 0 packets/sec
  5 minutes output rate 424 bps (0.0% with framing overhead), 0 packets/sec
     884 packets input, 108713 bytes
     Received 0 broadcasts, 0 multicast
     0 runts, 0 giants
     0 input errors, 0 CRC, 0 alignment, 0 symbol, 47 input discards
     0 PAUSE input
     878 packets output, 127164 bytes
     Sent 0 broadcasts, 0 multicast
     0 output errors, 0 collisions
     0 late collision, 0 deferred, 0 output discards
     0 PAUSE output
Vlan100 is up, line protocol is up (connected)
  Hardware is Vlan, address is 001c.7338.71c7 (bia 001c.7338.71c7)
  Description: VLAN100
  Internet address is 10.100.0.1/24
  Broadcast address is 255.255.255.255
  IPv6 link-local address is fe80::21c:73ff:fe38:71c7/64
  No IPv6 global unicast address is assigned
  IP MTU 1500 bytes (default)
  Up 21 minutes, 56 seconds
Vlan500 is up, line protocol is up (connected)
  Hardware is Vlan, address is 001c.7338.71c7 (bia 001c.7338.71c7)
  Description: VLAN500
  Internet address is 192.168.5.1/24
  Broadcast address is 255.255.255.255
  IPv6 link-local address is fe80::21c:73ff:fe38:71c7/64
  IPv6 global unicast address(es):
    2001:192:168:5::1, subnet is 2001:192:168:5::/64
  IP MTU 1500 bytes (default)
  Up 21 minutes, 56 seconds

```

**Help:** execute the command "show interfaces"

**Prompt:**
- arista_eos>
- arista_eos#

### show pim ipv4 interface

**Output:**
```
Address       Interface             Mode    Neighbor  Hello  DR   DR Address    PktsQed  PktsDropped
                                            Count     Intvl  Pri
192.0.2.1     Ethernet20/1          sparse  1         5      1    192.0.2.2     0        0
192.0.2.3     Port-Channel1.10      sparse  1         30     1    192.0.2.4     28       0
192.0.2.5     Vlan100               sparse  1         30     1    192.0.2.6     0        0
192.0.2.7     Vlan200               sparse  1         30     1    192.0.2.8     0        0
```

**Help:** execute the command "show pim ipv4 interface"

**Prompt:**
- arista_eos>
- arista_eos#

### show port-channel summary

**Output:**
```
Flags                                                            
-------------------------- ----------------------------- ------------------------- 
   a - LACP Active            p - LACP Passive           * - static fallback       
   F - Fallback enabled       f - Fallback configured    ^ - individual fallback   
   U - In Use                 D - Down                                             
   + - In-Sync                - - Out-of-Sync            i - incompatible with agg 
   P - bundled in Po          s - suspended              G - Aggregable            
   I - Individual             S - ShortTimeout           w - wait for agg          

Number of channels in use: 1
Number of aggregators: 1

   Port-Channel       Protocol     Ports                            
 ------------------ --------------- -------------------------------- 
   Po105(D)           LACP(aF*)    Et5(D)                           
   Po106(D)           LACP(aF*)    Et6(D)                           
   Po107(D)           LACP(aF*)    Et7(D)                           
   Po108(D)           LACP(aF*)    Et8(D)                           
   Po109(D)           LACP(aF*)    Et9(D)                           
   Po110(D)           LACP(aF*)    Et10(D)                          
   Po111(D)           LACP(aF*)    Et11(D)                          
   Po112(D)           LACP(aF*)    Et12(D)                          
   Po113(D)           LACP(aF*)    Et13(D)                          
   Po114(D)           LACP(aF*)    Et14(D)                          
   Po115(D)           LACP(aF*)    Et15(D)                          
   Po116(D)           LACP(aF*)    Et16(D)                          
   Po117(D)           LACP(aF*)    Et17(D)                          
   Po118(D)           LACP(aF*)    Et18(D)                          
   Po119(D)           LACP(aF*)    Et19(D)                          
   Po120(D)           LACP(aF*)    Et20(D)                          
   Po121(D)           LACP(aF*)    Et21(D)                          
   Po122(D)           LACP(aF*)    Et22(D)                          
   Po123(D)           LACP(aF*)    Et23(D)                          
   Po124(D)           LACP(aF*)    Et24(D)                          
   Po125(D)           LACP(aF*)    Et25(D)                          
   Po126(D)           LACP(aF*)    Et26(D)                          
   Po127(D)           LACP(aF*)    Et27(D)                          
   Po128(D)           LACP(aF*)    Et28(D)                          
   Po129(D)           LACP(aF*)    Et29(D)                          
   Po130(D)           LACP(aF*)    Et30(D)                          
   Po131(D)           LACP(aF*)    Et31(D)                          
   Po132(D)           LACP(aF*)    Et32(D)                          
   Po133(D)           LACP(aF*)    Et33(D)                          
   Po134(D)           LACP(aF*)    Et34(D)                          
   Po135(D)           LACP(aF*)    Et35(D)                          
   Po136(D)           LACP(aF*)    Et36(D)                          
   Po137(D)           LACP(aF*)    Et37(D)                          
   Po138(D)           LACP(aF*)    Et38(D)                          
   Po139(D)           LACP(aF*)    Et39(D)                          
   Po140(D)           LACP(aF*)    Et40(D)                          
   Po141(D)           LACP(aF*)    Et41(D)                          
   Po142(D)           LACP(aF*)    Et42(D)                          
   Po146(D)           LACP(aF*)    Et43(D) Et44(D) Et45(D) Et46(D)  
                                   Et47(D)                          
   Po2000(U)          LACP(a)      Et54/1(PG+)   
```

**Help:** execute the command "show port-channel summary"

**Prompt:**
- arista_eos>
- arista_eos#

### show interfaces transceiver

**Output:**
```
If device is externally calibrated, only calibrated values are printed.
 N/A: not applicable, Tx: transmit, Rx: receive.
mA: milliamperes, dBm: decibels (milliwatts).
                               Bias      Optical   Optical                
          Temp       Voltage   Current   Tx Power  Rx Power               
Port      (Celsius)  (Volts)   (mA)      (dBm)     (dBm)     Last Update  
-----     ---------  --------  --------  --------  --------  -------------------
Et3/1/1    27.92      3.23      19.94     N/A      -2.39     0:00:06 ago
Et3/17/1   35.61      3.21      36.64    1.51      -0.10     0:00:03 ago
Et3/17/2   35.61      3.21      36.94    -0.20     -0.20     0:00:03 ago
Et3/17/3   35.61      3.21      37.42    1.65      -0.72     0:00:03 ago
Et5/29/1   N/A        N/A       N/A       N/A       N/A      N/A       

```

**Help:** execute the command "show interfaces transceiver"

**Prompt:**
- arista_eos>
- arista_eos#

### show lldp neighbors detail

**Output:**
```
Interface Ethernet1 detected 1 LLDP neighbors:

  Neighbor 2cc2.6081.eaf9/"Ethernet1", age 12 seconds
  Discovered 0:01:11 ago; Last changed 0:01:11 ago
  - Chassis ID type: MAC address (4)
    Chassis ID     : 2cc2.6081.eaf9
  - Port ID type: Interface name (5)
    Port ID     : "Ethernet1"
  - Time To Live: 120 seconds
  - System Name: "spine2.company.com"
  - System Description: "Arista Networks EOS version 4.15.2F running on an Arista Networks vEOS"
  - System Capabilities : Bridge, Router
    Enabled Capabilities: Bridge, Router
  - Management Address Subtype: Ethernet 
    Management Address        : 2cc2.6081.eaf9
    Interface Number Subtype  : Unknown (1)
    Interface Number          : 0
    OID String                : 
  - IEEE802.1 Port VLAN ID: 1
  - IEEE802.1/IEEE802.3 Link Aggregation
    Link Aggregation Status: Capable, Disabled (0x01)
    Port ID                : 0
  - IEEE802.3 Maximum Frame Size: 9236 bytes

Interface Ethernet2 detected 1 LLDP neighbors:

  Neighbor 2cc2.6081.eaf9/"Ethernet2", age 12 seconds
  Discovered 0:01:11 ago; Last changed 0:01:11 ago
  - Chassis ID type: MAC address (4)
    Chassis ID     : 2cc2.6081.eaf9
  - Port ID type: Interface name (5)
    Port ID     : "Ethernet2"
  - Time To Live: 120 seconds
  - System Name: "spine2.company.com"
  - System Description: "Arista Networks EOS version 4.15.2F running on an Arista Networks vEOS"
  - System Capabilities : Bridge, Router
    Enabled Capabilities: Bridge, Router
  - Management Address Subtype: Ethernet 
    Management Address        : 2cc2.6081.eaf9
    Interface Number Subtype  : Unknown (1)
    Interface Number          : 0
    OID String                : 
  - IEEE802.1 Port VLAN ID: 1
  - IEEE802.1/IEEE802.3 Link Aggregation
    Link Aggregation Status: Capable, Disabled (0x01)
    Port ID                : 0
  - IEEE802.3 Maximum Frame Size: 9236 bytes

Interface Ethernet3 detected 1 LLDP neighbors:

  Neighbor 2cc2.6081.eaf9/"Ethernet3", age 12 seconds
  Discovered 0:01:11 ago; Last changed 0:01:11 ago
  - Chassis ID type: MAC address (4)
    Chassis ID     : 2cc2.6081.eaf9
  - Port ID type: Interface name (5)
    Port ID     : "Ethernet3"
  - Time To Live: 120 seconds
  - System Name: "spine2.company.com"
  - System Description: "Arista Networks EOS version 4.15.2F running on an Arista Networks vEOS"
  - System Capabilities : Bridge, Router
    Enabled Capabilities: Bridge, Router
  - Management Address Subtype: Ethernet 
    Management Address        : 2cc2.6081.eaf9
    Interface Number Subtype  : Unknown (1)
    Interface Number          : 0
    OID String                : 
  - IEEE802.1 Port VLAN ID: 1
  - IEEE802.1/IEEE802.3 Link Aggregation
    Link Aggregation Status: Capable, Disabled (0x01)
    Port ID                : 0
  - IEEE802.3 Maximum Frame Size: 9236 bytes
 
Interface Ethernet4 detected 1 LLDP neighbors:

  Neighbor 2cc2.6081.eaf9/"Ethernet4", age 12 seconds
  Discovered 0:01:11 ago; Last changed 0:01:11 ago
  - Chassis ID type: MAC address (4)
    Chassis ID     : 2cc2.6081.eaf9
  - Port ID type: Interface name (5)
    Port ID     : "Ethernet4"
  - Time To Live: 120 seconds
  - System Name: "spine2.company.com"
  - System Description: "Arista Networks EOS version 4.15.2F running on an Arista Networks vEOS"
  - System Capabilities : Bridge, Router
    Enabled Capabilities: Bridge, Router
  - Management Address Subtype: Ethernet 
    Management Address        : 2cc2.6081.eaf9
    Interface Number Subtype  : Unknown (1)
    Interface Number          : 0
    OID String                : 
  - IEEE802.1 Port VLAN ID: 1
  - IEEE802.1/IEEE802.3 Link Aggregation
    Link Aggregation Status: Capable, Disabled (0x01)
    Port ID                : 0
  - IEEE802.3 Maximum Frame Size: 9236 bytes

Interface Ethernet5 detected 0 LLDP neighbors:
 
Interface Ethernet6 detected 0 LLDP neighbors:

Interface Ethernet7 detected 0 LLDP neighbors:

Interface Management1 detected 2 LLDP neighbors:

  Neighbor 0005.8671.4ec0/"fxp0", age 27 seconds
  Discovered 0:02:21 ago; Last changed 0:02:21 ago
  - Chassis ID type: MAC address (4)
    Chassis ID     : 0005.8671.4ec0
  - Port ID type: Interface name (5)
    Port ID     : "fxp0"
  - Time To Live: 120 seconds
  - Port Description: "fxp0"
  - System Name: "vmx1"
  - System Description: "Juniper Networks, Inc. vmx internet router, kernel JUNOS 15.1F4.15, Build date: 2015-12-23 19:22:55 UTC Copyright (c) 1996-2015 Juniper Networks, Inc."
  - System Capabilities : Bridge, Router
    Enabled Capabilities: Bridge, Router
  - Management Address Subtype: IPv4 
    Management Address        : 10.0.0.31
    Interface Number Subtype  : ifIndex (2)
    Interface Number          : 1
    OID String                : 0.1.3.6.1.2.1.31.1.1.1.1.1
  - IEEE802.1/IEEE802.3 Link Aggregation
    Link Aggregation Status: Capable, Disabled (0x01)
    Port ID                : 0
  - IEEE802.3 MAC/PHY Configuration/Status
    Auto-negotiation       : Supported, Disabled
                             10BASE-T (half-duplex)
                             10BASE-T (full-duplex)
                             100BASE-TX (half-duplex)
                             100BASE-TX (full-duplex)
                             1000BASE-X (half-duplex)
                             1000BASE-X (full-duplex)
                             1000BASE-T (full-duplex)
    Operational MAU Type   : Unknown
  - IEEE802.3 Maximum Frame Size: 1514 bytes

  Neighbor 2cc2.6081.eaf9/"Management1", age 17 seconds
  Discovered 0:01:17 ago; Last changed 0:01:17 ago
  - Chassis ID type: MAC address (4)
    Chassis ID     : 2cc2.6081.eaf9
  - Port ID type: Interface name (5)
    Port ID     : "Management1"
  - Time To Live: 120 seconds
  - System Name: "spine2.company.com"
  - System Description: "Arista Networks EOS version 4.15.2F running on an Arista Networks vEOS"
  - System Capabilities : Bridge, Router
    Enabled Capabilities: Bridge, Router
  - Management Address Subtype: Ethernet 
    Management Address        : 2cc2.6081.eaf9
    Interface Number Subtype  : Unknown (1)
    Interface Number          : 0
    OID String                : 
  - IEEE802.1 Port VLAN ID: 0
  - IEEE802.1/IEEE802.3 Link Aggregation
    Link Aggregation Status: Not Capable (0x00)
    Port ID                : 0
  - IEEE802.3 Maximum Frame Size: 1518 bytes

Interface Ethernet8 detected 3 LLDP neighbors:

  Neighbor 0050.56eb.3ef3/Management1, age 4 seconds
  Discovered 34 days, 19:40:42 ago; Last changed 34 days, 19:40:42 ago
    - Chassis ID type: MAC address (4)
      Chassis ID     : 0050.56eb.3ef3
    - Port ID type: Interface name (5)
      Port ID     : "Management1"
    - Time To Live: 120 seconds
    - System Name: "cvx"
    - System Description: "Arista Networks EOS version 4.15.5M running on an Arista Networks CVX"
    - System Capabilities : Bridge, Router
      Enabled Capabilities: Bridge
    - Management Address Subtype: IPv4 (1)
      Management Address        : 172.16.2.141
      Interface Number Subtype  : ifIndex (2)
      Interface Number          : 999001
      OID String                : 
    - IEEE802.1 Port VLAN ID: 0
    - IEEE802.1/IEEE802.3 Link Aggregation
      Link Aggregation Status: Not Capable (0x00)
      Port ID                : 0
    - IEEE802.3 Maximum Frame Size: 1518 bytes

  Neighbor 0050.568b.67c8/Ethernet1, age 29 seconds
  Discovered 34 days, 19:40:24 ago; Last changed 34 days, 19:40:24 ago
    - Chassis ID type: MAC address (4)
      Chassis ID     : 0050.568b.67c8
    - Port ID type: Interface name (5)
      Port ID     : "Ethernet1"
    - Time To Live: 120 seconds
    - System Name: "cvx-client-1"
    - System Description: "Arista Networks EOS version 4.15.5M running on an Arista Networks CVX"
    - System Capabilities : Bridge, Router
      Enabled Capabilities: Bridge
    - Management Address Subtype: IPv4 (1)
      Management Address        : 172.16.2.142
      Interface Number Subtype  : ifIndex (2)
      Interface Number          : 999001
      OID String                : 
    - IEEE802.1 Port VLAN ID: 1
    - IEEE802.1/IEEE802.3 Link Aggregation
      Link Aggregation Status: Capable, Disabled (0x01)
      Port ID                : 0
    - IEEE802.3 Maximum Frame Size: 9236 bytes

  Neighbor 0050.568b.67c8/Management1, age 30 seconds
  Discovered 34 days, 19:40:22 ago; Last changed 34 days, 19:40:22 ago
    - Chassis ID type: MAC address (4)
      Chassis ID     : 0050.568b.67c8
    - Port ID type: Interface name (5)
      Port ID     : "Management1"
    - Time To Live: 120 seconds
    - System Name: "cvx-client-1"
    - System Description: "Arista Networks EOS version 4.15.5M running on an Arista Networks CVX"
    - System Capabilities : Bridge, Router
      Enabled Capabilities: Bridge
    - Management Address Subtype: IPv4 (1)
      Management Address        : 172.16.2.142
      Interface Number Subtype  : ifIndex (2)
      Interface Number          : 999001
      OID String                : 
    - IEEE802.1 Port VLAN ID: 0
    - IEEE802.1/IEEE802.3 Link Aggregation
      Link Aggregation Status: Not Capable (0x00)
      Port ID                : 0
    - IEEE802.3 Maximum Frame Size: 1518 bytes

Interface Ethernet9 detected 1 LLDP neighbors:

  Neighbor 7c0e.cecb.659b/Eth1/23, age 29 seconds
  Discovered 11 days, 1:32:12 ago; Last changed 11 days, 1:32:12 ago
    - Chassis ID type: MAC address (4)
      Chassis ID     : 7c0e.cecb.659b
    - Port ID type: Locally assigned (7)
      Port ID     : "Eth1/23"
    - Time To Live: 120 seconds
    - Port Description: "topology/pod-1/paths-101/pathep-[AVS_Policy_Group]"
    - System Name: "Leaf1.cliqr.com"
    - System Description: "topology/pod-1/node-101"
    - System Capabilities : Bridge, Router
      Enabled Capabilities: Bridge, Router
    - Management Address Subtype: Ethernet (6)
      Management Address        : 7c0e.cecb.659b
      Interface Number Subtype  : ifIndex (2)
      Interface Number          : 83886080
      OID String                : 
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 201):
          01
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 202):
          01
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 203):
          00 00 00 65
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 205):
          00 01
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 206):
          41 43 49 20 46 61 62 72 69 63 31
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 207):
          01 0a 00 00 01 34 61 36 39 62 63 37 61 2d 63 61
          36 64 2d 31 31 65 35 2d 38 39 32 61 2d 38 39 35
          66 31 37 62 38 35 61 39 64 02 0a 00 00 02 37 38
          66 64 30 30 64 32 2d 63 61 37 33 2d 31 31 65 35
          2d 39 34 39 63 2d 38 64 33 35 34 65 39 30 32 31
          38 38 03 0a 00 00 03 38 61 31 65 64 39 32 63 2d
          63 61 36 38 2d 31 31 65 35 2d 61 66 37 66 2d 31
          64 65 39 36 64 38 65 36 64 32 62
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 208):
          0a 00 c8 5f
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 210):
          6e 39 30 30 30 2d 31 31 2e 32 28 32 67 29
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 212):
          53 41 4c 31 38 33 37 30 4e 5a 41
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 214):
          4e 39 4b 2d 43 39 33 39 36 54 58
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 215):
          4c 65 61 66 31
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 216):
          00 00

Interface Ethernet10 detected 1 LLDP neighbors:

  Neighbor 7c0e.cecb.659c/Eth1/24, age 29 seconds
  Discovered 11 days, 1:32:12 ago; Last changed 11 days, 1:32:12 ago
    - Chassis ID type: MAC address (4)
      Chassis ID     : 7c0e.cecb.659c
    - Port ID type: Locally assigned (7)
      Port ID     : "Eth1/24"
    - Time To Live: 120 seconds
    - Port Description: "topology/pod-1/paths-101/pathep-[AVS_Policy_Group]"
    - System Name: "Leaf1.cliqr.com"
    - System Description: "topology/pod-1/node-101"
    - System Capabilities : Bridge, Router
      Enabled Capabilities: Bridge, Router
    - Management Address Subtype: Ethernet (6)
      Management Address        : 7c0e.cecb.659c
      Interface Number Subtype  : ifIndex (2)
      Interface Number          : 83886080
      OID String                : 
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 201):
          01
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 202):
          01
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 203):
          00 00 00 65
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 205):
          00 01
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 206):
          41 43 49 20 46 61 62 72 69 63 31
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 207):
          01 0a 00 00 01 34 61 36 39 62 63 37 61 2d 63 61
          36 64 2d 31 31 65 35 2d 38 39 32 61 2d 38 39 35
          66 31 37 62 38 35 61 39 64 02 0a 00 00 02 37 38
          66 64 30 30 64 32 2d 63 61 37 33 2d 31 31 65 35
          2d 39 34 39 63 2d 38 64 33 35 34 65 39 30 32 31
          38 38 03 0a 00 00 03 38 61 31 65 64 39 32 63 2d
          63 61 36 38 2d 31 31 65 35 2d 61 66 37 66 2d 31
          64 65 39 36 64 38 65 36 64 32 62
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 208):
          0a 00 c8 5f
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 210):
          6e 39 30 30 30 2d 31 31 2e 32 28 32 67 29
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 212):
          53 41 4c 31 38 33 37 30 4e 5a 41
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 214):
          4e 39 4b 2d 43 39 33 39 36 54 58
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 215):
          4c 65 61 66 31
    - Unknown organizationally-defined TLV (OUI 00-01-42, subtype 216):
          00 00

Interface Ethernet11 detected 0 LLDP neighbors:

Interface Ethernet12 detected 0 LLDP neighbors:

Interface Ethernet13 detected 0 LLDP neighbors:

Interface Ethernet14 detected 0 LLDP neighbors:

Interface Ethernet15 detected 0 LLDP neighbors:

Interface Ethernet16 detected 0 LLDP neighbors:

Interface Ethernet17 detected 0 LLDP neighbors:
 
Interface Ethernet18 detected 0 LLDP neighbors:

Interface Ethernet19 detected 0 LLDP neighbors:

Interface Ethernet20 detected 0 LLDP neighbors:

Interface Ethernet21 detected 0 LLDP neighbors:

Interface Ethernet22 detected 0 LLDP neighbors:

Interface Ethernet23 detected 1 LLDP neighbors:

  Neighbor 3c8a.b089.9898/527, age 21 seconds
  Discovered 19 days, 18:20:22 ago; Last changed 19 days, 18:20:22 ago
    - Chassis ID type: MAC address (4)
      Chassis ID     : 3c8a.b089.9898
    - Port ID type: Locally assigned (7)
      Port ID     : "527"
    - Time To Live: 120 seconds
    - Port Description: "ge-1/1/1"
    - System Name: "MX"
    - System Description: "Juniper Networks, Inc. mx5-t internet router, kernel JUNOS 14.2R5.8, Build date: 2015-11-25 01:57:41 UTC Copyright (c) 1996-2015 Juniper Networks, Inc."
    - System Capabilities : Bridge, Router
      Enabled Capabilities: Bridge, Router
    - IEEE802.1/IEEE802.3 Link Aggregation
      Link Aggregation Status: Capable, Disabled (0x01)
      Port ID                : 0
    - IEEE802.3 MAC/PHY Configuration/Status
      Auto-negotiation       : Supported, Enabled
      Advertised Capabilities: Asymmetric and Symmetric PAUSE
                               10BASE-T (half-duplex)
                               10BASE-T (full-duplex)
                               100BASE-TX (half-duplex)
                               100BASE-TX (full-duplex)
                               1000BASE-X (half-duplex)
                               1000BASE-X (full-duplex)
                               1000BASE-T (full-duplex)
      Operational MAU Type   : Unknown (0)
    - IEEE802.3 Maximum Frame Size: 1514 bytes

Interface Ethernet24 detected 0 LLDP neighbors:

Interface Ethernet25 detected 0 LLDP neighbors:

Interface Ethernet26 detected 0 LLDP neighbors:
 
Interface Ethernet27 detected 0 LLDP neighbors:

Interface Ethernet28 detected 0 LLDP neighbors:

Interface Ethernet29 detected 0 LLDP neighbors:

Interface Ethernet30 detected 0 LLDP neighbors:

Interface Ethernet31 detected 0 LLDP neighbors:

Interface Ethernet32 detected 0 LLDP neighbors:

Interface Ethernet33 detected 4 LLDP neighbors:

  Neighbor 0050.560b.66ea/Management1, age 29 seconds
  Discovered 33 days, 23:34:56 ago; Last changed 33 days, 23:34:56 ago
    - Chassis ID type: MAC address (4)
      Chassis ID     : 0050.560b.66ea
    - Port ID type: Interface name (5)
      Port ID     : "Management1"
    - Time To Live: 120 seconds
    - System Name: "cvx-client-2"
    - System Description: "Arista Networks EOS version 4.15.5M running on an Arista Networks CVX"
    - System Capabilities : Bridge, Router
      Enabled Capabilities: Bridge
    - Management Address Subtype: IPv4 (1)
      Management Address        : 172.16.2.143
      Interface Number Subtype  : ifIndex (2)
      Interface Number          : 999001
      OID String                : 
    - IEEE802.1 Port VLAN ID: 0
    - IEEE802.1/IEEE802.3 Link Aggregation
      Link Aggregation Status: Not Capable (0x00)
      Port ID                : 0
    - IEEE802.3 Maximum Frame Size: 1518 bytes

  Neighbor 0050.560b.66ea/Ethernet1, age 29 seconds
  Discovered 33 days, 23:34:56 ago; Last changed 33 days, 23:34:56 ago
    - Chassis ID type: MAC address (4)
      Chassis ID     : 0050.560b.66ea
    - Port ID type: Interface name (5)
      Port ID     : "Ethernet1"
    - Time To Live: 120 seconds
    - System Name: "cvx-client-2"
    - System Description: "Arista Networks EOS version 4.15.5M running on an Arista Networks CVX"
    - System Capabilities : Bridge, Router
      Enabled Capabilities: Bridge
    - Management Address Subtype: IPv4 (1)
      Management Address        : 172.16.2.143
      Interface Number Subtype  : ifIndex (2)
      Interface Number          : 999001
      OID String                : 
    - IEEE802.1 Port VLAN ID: 1
    - IEEE802.1/IEEE802.3 Link Aggregation
      Link Aggregation Status: Capable, Disabled (0x01)
      Port ID                : 0
    - IEEE802.3 Maximum Frame Size: 9236 bytes

  Neighbor 0050.56ac.4cd9/0050.56ac.4cd9, age 29 seconds
  Discovered 33 days, 23:34:56 ago; Last changed 13:58:03 ago
    - Chassis ID type: MAC address (4)
      Chassis ID     : 0050.56ac.4cd9
    - Port ID type: MAC address (3)
      Port ID     : 0050.56ac.4cd9
    - Time To Live: 120 seconds
    - Port Description: "ens192"
    - System Name: "aci-compute"
    - System Description: "Red Hat Enterprise Linux Linux 3.10.0-327.13.1.el7.x86_64 #1 SMP Mon Feb 29 13:22:02 EST 2016 x86_64"
    - System Capabilities : Bridge, WLAN Access Point, Router, Station Only
      Enabled Capabilities: Router, Station Only
    - Management Address Subtype: IPv4 (1)
      Management Address        : 172.16.2.222
      Interface Number Subtype  : ifIndex (2)
      Interface Number          : 2
      OID String                : 
    - Management Address Subtype: IPv6 (2)
      Management Address        : fe80::250:56ff:feac:4cd9
      Interface Number Subtype  : ifIndex (2)
      Interface Number          : 2
      OID String                : 
    - IEEE802.1/IEEE802.3 Link Aggregation
      Link Aggregation Status: Capable, Disabled (0x01)
      Port ID                : 0
    - IEEE802.3 MAC/PHY Configuration/Status
      Auto-negotiation       : Not Supported
      Advertised Capabilities: None
      Operational MAU Type   : 10GBASE-R (33)

  Neighbor 0050.56ac.4e29/0050.56ac.4e29, age 29 seconds
  Discovered 5 days, 19:11:29 ago; Last changed 5 days, 19:01:28 ago
    - Chassis ID type: MAC address (4)
      Chassis ID     : 0050.56ac.4e29
    - Port ID type: MAC address (3)
      Port ID     : 0050.56ac.4e29
    - Time To Live: 120 seconds
    - Port Description: "ens192"
    - System Name: "aci-control"
    - System Description: "Red Hat Enterprise Linux Linux 3.10.0-327.13.1.el7.x86_64 #1 SMP Mon Feb 29 13:22:02 EST 2016 x86_64"
    - System Capabilities : Bridge, WLAN Access Point, Router, Station Only
      Enabled Capabilities: Router, Station Only
    - Management Address Subtype: IPv4 (1)
      Management Address        : 172.16.2.221
      Interface Number Subtype  : ifIndex (2)
      Interface Number          : 2
      OID String                : 
    - Management Address Subtype: IPv6 (2)
      Management Address        : fe80::250:56ff:feac:4e29
      Interface Number Subtype  : ifIndex (2)
      Interface Number          : 2
      OID String                : 
    - IEEE802.1/IEEE802.3 Link Aggregation
      Link Aggregation Status: Capable, Disabled (0x01)
      Port ID                : 0
    - IEEE802.3 MAC/PHY Configuration/Status
      Auto-negotiation       : Not Supported
      Advertised Capabilities: None
      Operational MAU Type   : 10GBASE-R (33)

Interface Ethernet34 detected 0 LLDP neighbors:
 
Interface Ethernet35 detected 0 LLDP neighbors:

Interface Ethernet36 detected 0 LLDP neighbors:

Interface Ethernet37 detected 0 LLDP neighbors:

Interface Ethernet38 detected 0 LLDP neighbors:

Interface Ethernet39 detected 0 LLDP neighbors:

Interface Ethernet40 detected 0 LLDP neighbors:

Interface Ethernet41 detected 0 LLDP neighbors:

Interface Ethernet42 detected 0 LLDP neighbors:
 
Interface Ethernet43 detected 0 LLDP neighbors:

Interface Ethernet44 detected 0 LLDP neighbors:

Interface Ethernet45 detected 0 LLDP neighbors:

Interface Ethernet46 detected 0 LLDP neighbors:

Interface Ethernet47 detected 0 LLDP neighbors:

Interface Ethernet48 detected 0 LLDP neighbors:

Interface Ethernet49/1 detected 1 LLDP neighbors:

  Neighbor 001c.737d.77fb/Ethernet49/1, age 19 seconds
  Discovered 117 days, 19:38:50 ago; Last changed 33 days, 3:31:32 ago
    - Chassis ID type: MAC address (4)
      Chassis ID     : 001c.737d.77fb
    - Port ID type: Interface name (5)
      Port ID     : "Ethernet49/1"
    - Time To Live: 120 seconds
    - Port Description: "" To R4-Arista-L2-SDNLAB -DC1""
    - System Name: "R4-Arista-L3-SDNLAB-SW1"
    - System Description: "Arista Networks EOS version 4.15.0FXA running on an Arista Networks DCS-7050SX-64"
    - System Capabilities : Bridge, Router
      Enabled Capabilities: Bridge, Router
    - Management Address Subtype: IPv4 (1)
      Management Address        : 2.2.2.2
      Interface Number Subtype  : ifIndex (2)
      Interface Number          : 5000000
      OID String                : 
    - IEEE802.1 Port VLAN ID: 1
    - IEEE802.1/IEEE802.3 Link Aggregation
      Link Aggregation Status: Capable, Enabled (0x03)
      Port ID                : 1000010
    - IEEE802.3 Maximum Frame Size: 9236 bytes

Interface Ethernet49/2 detected 0 LLDP neighbors:

Interface Ethernet49/3 detected 0 LLDP neighbors:

Interface Ethernet49/4 detected 0 LLDP neighbors:

Interface Ethernet50/1 detected 0 LLDP neighbors:

Interface Ethernet50/2 detected 0 LLDP neighbors:

Interface Ethernet50/3 detected 0 LLDP neighbors:

Interface Ethernet50/4 detected 0 LLDP neighbors:

Interface Ethernet51/1 detected 1 LLDP neighbors:

  Neighbor 001c.737d.745f/Ethernet49/1, age 28 seconds
  Discovered 117 days, 15:20:04 ago; Last changed 61 days, 23:05:42 ago
    - Chassis ID type: MAC address (4)
      Chassis ID     : 001c.737d.745f
    - Port ID type: Interface name (5)
      Port ID     : "Ethernet49/1"
    - Time To Live: 120 seconds
    - Port Description: ""Connected to DC1-AristaL2SW-R4""
    - System Name: "R4-Arista-L3-SDNLAB-SW2"
    - System Description: "Arista Networks EOS version 4.15.0FXA running on an Arista Networks DCS-7050SX-64"
    - System Capabilities : Bridge, Router
      Enabled Capabilities: Bridge, Router
    - Management Address Subtype: IPv4 (1)
      Management Address        : 172.16.1.3
      Interface Number Subtype  : ifIndex (2)
      Interface Number          : 2000201
      OID String                : 
    - IEEE802.1 Port VLAN ID: 1
    - IEEE802.1/IEEE802.3 Link Aggregation
      Link Aggregation Status: Capable, Enabled (0x03)
      Port ID                : 1000010
    - IEEE802.3 Maximum Frame Size: 9236 bytes

Interface Ethernet51/2 detected 0 LLDP neighbors:

Interface Ethernet51/3 detected 0 LLDP neighbors:

Interface Ethernet51/4 detected 0 LLDP neighbors:

Interface Ethernet52/1 detected 1 LLDP neighbors:

  Neighbor 001c.737d.745f/Ethernet50/1, age 28 seconds
  Discovered 117 days, 18:25:48 ago; Last changed 61 days, 23:03:48 ago
    - Chassis ID type: MAC address (4)
      Chassis ID     : 001c.737d.745f
    - Port ID type: Interface name (5)
      Port ID     : "Ethernet50/1"
    - Time To Live: 120 seconds
    - Port Description: ""Connected to DC1-AristaL2SW-R4""
    - System Name: "R4-Arista-L3-SDNLAB-SW2"
    - System Description: "Arista Networks EOS version 4.15.0FXA running on an Arista Networks DCS-7050SX-64"
    - System Capabilities : Bridge, Router
      Enabled Capabilities: Bridge, Router
    - Management Address Subtype: IPv4 (1)
      Management Address        : 172.16.1.3
      Interface Number Subtype  : ifIndex (2)
      Interface Number          : 2000201
      OID String                : 
    - IEEE802.1 Port VLAN ID: 1
    - IEEE802.1/IEEE802.3 Link Aggregation
      Link Aggregation Status: Capable, Enabled (0x03)
      Port ID                : 1000010
    - IEEE802.3 Maximum Frame Size: 9236 bytes

Interface Ethernet52/2 detected 0 LLDP neighbors:

Interface Ethernet52/3 detected 0 LLDP neighbors:

Interface Ethernet52/4 detected 0 LLDP neighbors:

Interface Management1 detected 1 LLDP neighbors:

  Neighbor 0cca.01c0.e8e1/"Management1", age 2 seconds
  Discovered 1:11:08 ago; Last changed 1:11:08 ago
  - Chassis ID type: MAC address (4)
    Chassis ID     : 0cca.01c0.e8e1
  - Port ID type: Interface name(5)
    Port ID     : "Management1"
  - Time To Live: 120 seconds
  - System Name: "test-host.domain.com"
  - System Capabilities : Bridge, Router
    Enabled Capabilities: Bridge
  - Management Address Subtype: IPv4 
    Management Address        : 172.16.208.5
    Interface Number Subtype  : ifIndex (2)
    Interface Number          : 999001
    OID String                : 
  - IEEE802.1 Port VLAN ID: 0
  - IEEE802.1/IEEE802.3 Link Aggregation
    Link Aggregation Status: Not Capable (0x00)
    Port ID                : 0
  - IEEE802.3 Maximum Frame Size: 1518 bytes
```

**Help:** execute the command "show lldp neighbors detail"

**Prompt:**
- arista_eos>
- arista_eos#

### show snmp community

**Output:**
```
Community name: TEST
Community access: read-only

Community name: TEST_AGAIN
Community access: read-only
Community view: TEST (non-existent)
 
Community name: TEST_ONE_MORE
Community access: read-only
Access list: TEST_ACL (non-existent)

Community name: TEST_ONE_MORE_TIME
Community access: read-write
 IPv6 access list: IPV6_ACL (non-existent)

Community name: public
Community access: read-only

```

**Help:** execute the command "show snmp community"

**Prompt:**
- arista_eos>
- arista_eos#

### show ipv6 bgp summary

**Output:**
```
BGP summary information for VRF default
Router identifier 10.0.65.72, local AS number 64911
Neighbor Status Codes: m - Under maintenance
  Neighbor         V  AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State  PfxRcd PfxAcc
  2001:DB8:ffff::1      4  65292              0         0    0    0   79d05h Active
  2001:DB8:fff1::1     4  64832              0         0    0    0   79d05h Idle(NoIf)
  2001:DB8:fff2::1     4  64833         114056    118481    0    0   79d05h Estab  1      1

```

**Help:** execute the command "show ipv6 bgp summary"

**Prompt:**
- arista_eos>
- arista_eos#

### dir flash

**Output:**
```
Directory of flash:/

       -rwx   591941836            Aug 2  2017  EOS-4.18.3.1F.swi
       -rwx   609823300           Feb 14 02:03  EOS-4.19.5M.swi
       -rwx          29           Aug 23  2017  boot-config
       drwx        4096           Aug 23  2017  debug
       -rwx           0           Apr 15  2017  enable3px
       -rwx          19           Apr 15  2017  enable3px.key
       -rwx          31           Apr 15  2017  kickstart-config
       drwx        4096            Apr 3 10:29  persist
       drwx        4096           Apr 15  2017  schedule
       -rwx       20530           Jan 18 22:46  startup-config
       -rwx          13           Aug 23  2017  zerotouch-config

3519041536 bytes total (1725112320 bytes free)

```

**Help:** execute the command "dir flash"

**Prompt:**
- arista_eos>
- arista_eos#

### show mac security interface

**Output:**
```
Interface       SCI                       Controlled Port      Key in Use          
Ethernet4/15/1  ch:99:3h:69:76:cc::661    True                 changed77f1j42e246kf05b:45   
Ethernet5/13/1  ch:99:3h:69:72:d4::803    True                 changedf1e9j62b5a9keac3:45   
Ethernet5/14/1  ch:99:3h:69:72:d8::807    True                 changeda62bjb9cdadk246e:45   
Ethernet5/16/1  ch:99:3h:69:72:e0::815    True                 changede693j033b28k810e:56   
Ethernet5/17/1  ch:99:3h:69:72:e4::819    True                 changed5778j794bf3k611c:45   
Ethernet5/18/1  ch:99:3h:69:72:e8::823    True                 changed532dj3307f2k610e:45   
Ethernet5/19/1  ch:99:3h:69:72:ec::827    True                 changed046bjdb206eka327:45   
Ethernet5/20/1  ch:99:3h:69:72:f0::831    True                 changedd888jc35359kbd0c:39
```

**Help:** execute the command "show mac security interface"

**Prompt:**
- arista_eos>
- arista_eos#

### show mac address-table

**Output:**
```
          mac Address Table
------------------------------------------------------------------
 
Vlan    mac Address       Type        Ports      Moves   Last Move
----    -----------       ----        -----      -----   ---------
   3    0012.3694.03ec    STATIC      Et7
  55        001c.7313.a3de      DYNAMIC        Et32        1    0:08:16 ago
101    001c.8224.36d7    DYNAMIC     Po2        1       9 days, 15:57:28 ago
102    001c.8220.1319    STATIC      Po1
102    001c.8229.a0f3    DYNAMIC     Po1        1       0:05:05 ago
661    001c.8220.1319    STATIC      Po1
661    001c.822f.6b22    DYNAMIC     Po7        1       0:20:10 ago
3000    001c.8220.1319    STATIC      Po1
3000    0050.56a8.0016    DYNAMIC     Po1        1       0:07:38 ago
3909    001c.8220.1319    STATIC      Po1
3909    001c.822f.6a80    DYNAMIC     Po1        1       0:07:08 ago
3911    001c.8220.1319    STATIC      Po1
3911    001c.8220.40fa    DYNAMIC     Po8        1       1:19:58 ago
3912    001c.822b.033e    DYNAMIC     Et11       1       9 days, 15:57:23 ago
3913    001c.8220.1319    STATIC      Po1
3913    001c.822b.033e    DYNAMIC     Po1        1       0:04:35 ago
3984    001c.8220.178f    DYNAMIC     Et8        1       4 days, 15:07:29 ago
3992    001c.8220.1319    STATIC      Po1
3992    001c.8221.07b9    DYNAMIC     Po6        1       4 days, 15:13:15 ago
Total mac Addresses for this criterion: 24
 
          Multicast mac Address Table
------------------------------------------------------------------
 
Vlan    mac Address       Type        Ports
----    -----------       ----        -----
   4    c867.3057.8423    STATIC      Po10 Po123
  42    5309.3057.8423    STATIC      Po135 Po12 po5
 200    jenn.3057.8423    STATIC      Po66
  47    4242.3057.8423    STATIC      Po135 Po12 po5 eth1/1
Total mac Addresses for this criterion: 1
```

**Help:** execute the command "show mac address-table"

**Prompt:**
- arista_eos>
- arista_eos#

### show mac security mka counters

**Output:**
```
Interface       Rx Success      Rx Failure      Tx Success      Tx Failure     
Ethernet4/13/1  0               0               0               0              
Ethernet4/14/1  0               0               0               0              
Ethernet4/15/1  79688           0               79858           0              
Ethernet4/16/1  0               0               0               0              
Ethernet5/13/1  79788           0               79854           0              
Ethernet5/14/1  79878           0               79853           0              
Ethernet5/15/1  0               0               0               0              
Ethernet5/16/1  64246           0               79850           0              
Ethernet5/17/1  79749           0               79848           0              
Ethernet5/18/1  79756           0               79846           0              
Ethernet5/19/1  79842           0               79845           0              
Ethernet5/20/1  68225           0               68188           0
```

**Help:** execute the command "show mac security mka counters"

**Prompt:**
- arista_eos>
- arista_eos#

### show mac security participants detail

**Output:**
```
Interface: Ethernet4/15/1
    CKN: cd1df125ffbd3027abe6068fcbfdchanged91af15c274998046ca547
      Message ID: changed0975adf202e94acf2
      Elected self: True
      Success: True
      Principal: False
      Default: True
      KeyServer SCI: 28:00:3a:69:06:cc::999
      SAK transmit: False
      LLPN exhaustion: 0
      Distributed key identifier: None
      Live peer list: ['changed0fd8d6b694b42be37f5']
      Potential peer list: []

    CKN: e9cae93c91ef6c62afbb9fffd2fa32380achangede0f6348a8a6e1bb205be4d
      Message ID: changed77f1f42e246ef05b
      Elected self: True
      Success: True
      Principal: True
      Default: False
      KeyServer SCI: 28:1b:22:69:36:cc::333
      SAK transmit: True
      LLPN exhaustion: 0
      Distributed key identifier: changed2577f1f42e246ef05b:46
      Live peer list: ['changed4341200ff8e76821da']
      Potential peer list: []

 Interface: Ethernet5/13/1
    CKN: cd1df125ffbd3027abe6068fcbfd31f0changed58e91af15c274998046ca547
      Message ID: 1860e9c0c1d2b4877fa78b77
      Elected self: True
      Success: True
      Principal: False
      Default: True
      KeyServer SCI: 28:22:1b:69:32:d4::111
      SAK transmit: False
      LLPN exhaustion: 0
      Distributed key identifier: None
      Live peer list: ['2071783e6e9b09640a2eee89']
      Potential peer list: []

    CKN: e9cae93c91ef6c62afbb9fffd2fa323changedd6e0f6348a8a6e1bb205be4d
      Message ID: changedf1e9662b5a94eac3
      Elected self: True
      Success: True
      Principal: True
      Default: False
      KeyServer SCI: 28:11:3a:69:32:d4::111
      SAK transmit: True
      LLPN exhaustion: 0
      Distributed key identifier: dec1a8dchanged5a94eac3:46
      Live peer list: ['changedbe5869ab7cb6fa2c5cb1c']
      Potential peer list: []
```

**Help:** execute the command "show mac security participants detail"

**Prompt:**
- arista_eos>
- arista_eos#

### show ip ospf neighbor

**Output:**
```
Neighbor ID     VRF    Pri   State            Dead Time   Address         Interface
3.3.3.3         default    1   FULL/BDR         00:00:34    10.3.4.3        Ethernet2
2.2.2.2         default    1   FULL             00:00:38    10.2.4.2        Ethernet3

```

**Help:** execute the command "show ip ospf neighbor"

**Prompt:**
- arista_eos>
- arista_eos#

### show reload cause

**Output:**
```
Reload Cause 1:
-------------------
The system rebooted due to a Power Loss

Reload Time:
------------
Reload occurred at Fri Feb 23 14:18:49 2018 UTC.

Recommended Action:
-------------------
No action necessary.

Debugging Information:
----------------------
None available.
```

**Help:** execute the command "show reload cause"

**Prompt:**
- arista_eos>
- arista_eos#

### show ip helper-address

**Output:**
```
DHCP Relay is active
DHCP Relay Option 82 is disabled
DHCPv6 Relay Link-layer Address Option (79) is disabled
DHCP Smart Relay is disabled
Interface: Vlan1
  DHCP Smart Relay is disabled
  DHCP servers: 10.1.0.0
                10.1.0.1
                10.1.0.2
                10.1.0.3
                server.domain
Interface: Vlan2
  DHCP Smart Relay is disabled
  DHCP servers: 10.1.0.4
                server.domain

```

**Help:** execute the command "show ip helper-address"

**Prompt:**
- arista_eos>
- arista_eos#

### show environment temperature

**Output:**
```
System temperature status is: Ok

Supervisor 1:
                                                                 Alert  Critical
                                               Temp    Setpoint  Limit     Limit
Sensor  Description                             (C)         (C)    (C)       (C)
 ------- ----------------------------------- ------- ----------- ------ ---------
1       Digital Temperature Sensor on cpu0     36.0   (65) 63.8     95       105
2       Digital Temperature Sensor on cpu1     36.0   (65) 63.8     95       105
3       Digital Temperature Sensor on cpu2     36.0   (65) 63.8     95       105

Linecard 3:
                                                                 Alert  Critical
                                               Temp    Setpoint  Limit     Limit
Sensor  Description                             (C)         (C)    (C)       (C)
------- ----------------------------------- ------- ----------- ------ ---------
6       Outlet sensor                          50.8   (85) 83.8     95       105
7       Inlet sensor                           59.2   (75) 73.8     90       100
8       Board sensor                           62.0   (95) 93.8    105       110

Linecard 4:
                                                                 Alert  Critical
                                               Temp    Setpoint  Limit     Limit
Sensor  Description                             (C)         (C)    (C)       (C)
------- ----------------------------------- ------- ----------- ------ ---------
5       Outlet sensor                          41.2   (80) 78.8     90       100
6       Inlet sensor                           43.8   (65) 63.8     75        85
7       Board sensor                           49.0   (85) 83.8     95       105
9       Board sensor                           45.0   (85) 83.8     95       105

Linecard 5:
                                                                 Alert  Critical
                                               Temp    Setpoint  Limit     Limit
Sensor  Description                             (C)         (C)    (C)       (C)
------- ----------------------------------- ------- ----------- ------ ---------
5       Outlet sensor                          39.5   (80) 78.8     90       100
6       Inlet sensor                           39.0   (65) 63.8     75        85

Linecard 6:
                                                                 Alert  Critical
                                               Temp    Setpoint  Limit     Limit
Sensor  Description                             (C)         (C)    (C)       (C)
------- ----------------------------------- ------- ----------- ------ ---------
1       Outlet sensor                          32.5   (80) 78.8     90       100
2       Inlet sensor                           29.2   (65) 63.8     70        85

Fabric 1:
                                                                 Alert  Critical
                                               Temp    Setpoint  Limit     Limit
Sensor  Description                             (C)         (C)    (C)       (C)
------- ----------------------------------- ------- ----------- ------ ---------
13      ADT (Fan controller) 1                 32.8   (85) 83.8     95       105
14      Fan side sensor                        32.0   (85) 83.8     95       105
```

**Help:** execute the command "show environment temperature"

**Prompt:**
- arista_eos>
- arista_eos#

### show vlan

**Output:**
```
VLAN  Name                             Status    Ports
----- -------------------------------- --------- -------------------------------
1     default                          active    Et1
10    Test1                            active    Et1, Et2
20    Test2                            suspended
30    VLAN0030                         suspended

```

**Help:** execute the command "show vlan"

**Prompt:**
- arista_eos>
- arista_eos#

### show hostname

**Output:**
```
eos-spine1#show hostname
Hostname: spine1
FQDN:     spine1.company.com

```

**Help:** execute the command "show hostname"

**Prompt:**
- arista_eos>
- arista_eos#

### show ip interface brief

**Output:**
```
Interface              IP Address         Status     Protocol         MTU
Loopback0              1.1.1.1/32         up         up             65535
Management1            unassigned         down       down            1500
Vlan10                 unassigned         down       lowerlayerdown  1500
Ethernet5              10.0.0.1/24        up         up              1500
Port-Channel1          11.11.11.11/24     down       lowerlayerdown  1500


```

**Help:** execute the command "show ip interface brief"

**Prompt:**
- arista_eos>
- arista_eos#

### show vrf

**Output:**
```
Maximum number of vrfs allowed: 1023
   VRF           RD              Protocols       State                     Interfaces
------------- --------------- --------------- ---------------------------- ---------------------------
   red           <not set>       ipv4,ipv6       v4:routing; multicast,    Ethernet10, Ethernet20/1,
                                                 v6:no routing             Loopback0, Vlan100,
                                                                           Vlan200
   blue          1:1             ipv4,ipv6       v4:routing,               Ethernet20/1.10, Loopback1,
                                                 v6:no routing             Port-Channel1.20


```

**Help:** execute the command "show vrf"

**Prompt:**
- arista_eos>
- arista_eos#

### show ip bgp detail

**Output:**
```
BGP routing table information for VRF default
Router identifier 10.103.1.1, local AS number 103
BGP routing table entry for 10.103.1.0/24
 Paths: 2 available
  6333 623566 42669611124 4266644366 4266643244
    10.10.23.2 from 10.10.23.2 (10.10.1.1)
      Origin INCOMPLETE, metric 0, localpref 100, IGP metric 1, weight 0, received 19d16h ago, valid, external, best
      Community: internet 10050:200 10222:10010 3223:0 1000:17044
      Rx SAFI: Unicast
  6333 623566 42669.611124 4266644366 4266643244
    10.10.25.2 from 10.10.25.2 (10.10.1.1)
      Origin INCOMPLETE, metric 0, localpref 100, IGP metric 1, weight 0, received 21:13:51 ago, valid, internal
      Community: 10050:200 10222:10010 3223:0 1000:17055
      Rx SAFI: Unicast
BGP routing table entry for 10.104.1.0/24
 Paths: 1 available
  6333 623566 42669611124 {{432556}}
    10.10.11.2 from 10.10.11.2 (10.10.11.1)
      Origin IGP, metric 0, localpref 200, IGP metric 1, weight 0, received 19:13:51 ago, valid, internal, best
      Community: 10050:300 10222:10010 3223:0 1000:17066
      Extended Community: Route-Target-AS:1234:12
      Rx SAFI: Unicast
BGP routing table entry for 10.105.1.0/24
 Paths: 2 available
  6333 623566 42669611124 {{432556}}
    10.10.11.2 from 10.10.11.2 (10.10.11.1)
      Origin IGP, metric 0, localpref 300, IGP metric 1, weight 0, received 13:43:11 ago, valid, internal, best, atomic-aggregate
      Community: 10050:300 10222:10010 3223:0 1000:17077
      Rx SAFI: Unicast
      4 Contributing routes:
        10.105.1.59/32     Proto: Connected     Origin: IGP          AS Path: Local
        10.105.1.6/32      Proto: Connected     Origin: IGP          AS Path: Local
        10.105.1.29/32     Proto: BGP           Origin: IGP          AS Path: 3245.235
          Community: 999:10 347:234 1240:155
        10.105.1.28/32     Proto: BGP           Origin: IGP          AS Path: 3245.235
          Community: 999:10 347:234 1240:155
  Local (aggregated by 2345223 10.10.11.3)
    10.10.11.3 from 10.10.11.3 (10.10.11.1)
      Origin IGP, metric 0, localpref 200, IGP metric 1, weight 0, received 19:34:12 ago, valid, internal, atomic-aggregate
      Community: 10050:300 10222:10010 3223:0 1000:17088
      Rx SAFI: Unicast
BGP routing table entry for 10.105.100.0
 Paths: 2 available
  6333 623566 42669611124 {{432556}}
    10.10.11.2 from 10.10.11.2 (10.10.11.1)
      Origin IGP, metric 0, localpref 300, IGP metric 1, weight 0, received 13:43:11 ago, valid, internal, best, atomic-aggregate
      Community: 10050:300 10222:10010 3223:0 1000:17077
      Rx SAFI: Unicast
      4 Contributing routes:
        10.105.1.59/32     Proto: Connected     Origin: IGP          AS Path: Local
        10.105.1.6/32      Proto: Connected     Origin: IGP          AS Path: Local
        10.105.1.29/32     Proto: BGP           Origin: IGP          AS Path: 3245.235
          Community: 999:10 347:234 1240:155
        10.105.1.28/32     Proto: BGP           Origin: IGP          AS Path: 3245.235
          Community: 999:10 347:234 1240:155
  Local (aggregated by 2345223 10.10.11.3)
    10.10.11.3 from 10.10.11.3 (10.10.11.1)
      Origin IGP, metric 0, localpref 200, IGP metric 1, weight 0, received 19:34:12 ago, valid, internal, atomic-aggregate
      Community: 10050:300 10222:10010 3223:0 1000:17088
      Rx SAFI: Unicast
BGP routing table entry for 10.106.1.0/24
 Paths: 1 available
  Local
    10.10.12.2 from 10.10.12.2 (10.10.12.1)
      Origin INCOMPLETE, metric 0, localpref 200, IGP metric 1, weight 0, received 19:34:12 ago, valid, external, best
      Community: 10050:300 10222:10010 3223:0 1000:17099
      Rx SAFI: Unicast
 BGP routing table entry for 10.107.1.0/24
 Paths: 1 available
  Local (Received from a RR-client)
    10.10.13.2 from 10.10.13.2 (10.10.13.1)
      Origin IGP, metric 0, localpref 250, IGP metric 1, weight 0, received 19:34:12 ago, valid, internal, best
      Community: no-export
      Rx path id: 0x1
      Rx SAFI: Unicast
BGP routing table information for VRF CLOUD
Router identifier 10.105.1.1, local AS number 105
BGP routing table entry for 10.105.1.0/24
 Paths: 1 available
  6111 6211566 42669611124 4266644366 4266643244
    10.99.1.2 from 10.105.6.2 (10.15.1.1)
      Origin INCOMPLETE, metric 0, localpref 200, IGP metric 1, weight 0, received 13d11h ago, valid, external, best
      Community: internet 10050:200 10222:10010 3223:0 1000:17044
      Rx SAFI: Unicast
BGP routing table entry for 10.106.1.0/24
 Paths: 1 available
  6111 6211566 42669611124 4266644366 4266643244
    10.99.1.3 from 10.105.6.3 (10.15.1.2)
      Origin INCOMPLETE, metric 0, localpref 100, IGP metric 1, weight 0, received 13d11h ago, valid, external, backup
      Community: internet 10050:200 10222:10010 3223:0 1000:17044
      Rx SAFI: Unicast

```

**Help:** execute the command "show ip bgp detail"

**Prompt:**
- arista_eos>
- arista_eos#

### show interfaces status

**Output:**
```
Port Name Status Vlan Duplex Speed Type
Et1 Cust: (SERV-XXXXX disabled 1 auto auto 1000BASE-T
Et47 Cust: (SERV-XXXXX disabled 1 auto auto 1000BASE-T
 Et49 Core: drxx.yul01 notconnect in Po49 full 10G Not Present
Et52 Core: drxx.yul01 connected in Po49 full 10G 10GBASE-SR
Ma1 notconnect routed a-half a-10M 10/100/1000
 Po49 Core: dr01-dr02.y connected trunk full 20G N/A

```

**Help:** execute the command "show interfaces status"

**Prompt:**
- arista_eos>
- arista_eos#

### show isis neighbors

**Output:**
```

Instance  VRF      System Id            Type Interface       SNPA              State Hold time   Circuit Id
1         default  3333.3333.3333       L2   Ethernet2       50:0:0:3:0:3      UP    30          4444.4444.4444.0e
1         default  2222.2222.2222       L2   Ethernet3       50:0:0:2:0:2      UP    30          0F                 

```

**Help:** execute the command "show isis neighbors"

**Prompt:**
- arista_eos>
- arista_eos#

### show ip ospf database

**Output:**
```
            OSPF Router with ID(10.168.103.1) (Process ID 1) (VRF default)
 
                 Router Link States (Area 0.0.0.2)
 
Link ID         ADV Router      Age         Seq#       Checksum Link count
10.168.103.1   10.168.103.1   00:29:08    0x80000031 0x001D5F 1
10.168.104.2   10.168.104.2   00:29:09    0x80000066 0x00A49B 1
 
                 Net Link States (Area 0.0.0.2)
 
Link ID         ADV Router      Age         Seq#       Checksum
10.168.2.1     10.168.103.1   00:29:08    0x80000001 0x00B89D
 
                 Summary Net Link States (Area 0.0.0.2)
 
Link ID         ADV Router      Age         Seq#       Checksum
10.168.0.0     10.168.103.1   00:13:20    0x80000028 0x0008C8
10.168.0.0     10.168.104.2   00:09:16    0x80000054 0x00A2FF
10.168.3.0     10.168.104.2   00:24:16    0x80000004 0x00865F
10.168.3.0     10.168.103.1   00:24:20    0x80000004 0x002FC2
10.168.103.0   10.168.103.1   00:14:20    0x80000028 0x0096D2
10.168.103.0   10.168.104.2   00:13:16    0x80000004 0x00364B
10.168.104.0   10.168.104.2   00:08:16    0x80000055 0x002415
10.168.104.0   10.168.103.1   00:13:20    0x80000028 0x00EF6E

                 Type-5 AS External Link States
 
Link ID         ADV Router      Age         Seq#         Checksum Tag
10.24.238.238   10.26.0.31     678         0x800003d2   0x8acf   0
10.24.238.244   10.26.0.31     678         0x800003d2   0x4e06   0
10.24.238.224   10.26.0.31     678         0x800003d2   0x1751   0

```

**Help:** execute the command "show ip ospf database"

**Prompt:**
- arista_eos>
- arista_eos#

### show boot-config

**Output:**
```
Software image: flash:/EOS-2.2.0.swi
Console speed: (not set)
Aboot password (encrypted): $1$ap1QMbmz$DTqsFYeauuMSa7/Qxbi2l1
```

**Help:** execute the command "show boot-config"

**Prompt:**
- arista_eos>
- arista_eos#

### show bgp evpn summary

**Output:**
```
BGP summary information for VRF default
Router identifier 10.0.250.1, local AS number 65000
Neighbor Status Codes: m - Under maintenance
  Neighbor         V  AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State  PfxRcd PfxAcc
  10.0.250.11      4  65001              8         8    0    0 00:04:09 Estab  0      0
  10.0.250.12      4  65001              8         8    0    0 00:03:54 Estab  0      0
  10.0.250.13      4  65002              8         8    0    0 00:04:08 Estab  0      0
  10.0.250.14      4  65002              8         8    0    0 00:04:09 Estab  0      0
  10.0.250.15      4  65003              8         8    0    0 00:04:07 Estab  0      0
  10.0.250.16      4  65003              9         8    0    0 00:04:12 Estab  0      0
  10.0.250.17      4  65004              8         8    0    0 00:03:57 Estab  0      0
  10.0.250.18      4  65004              8         8    0    0 00:03:57 Estab  0      0

```

**Help:** execute the command "show bgp evpn summary"

**Prompt:**
- arista_eos>
- arista_eos#

### show inventory

**Output:**
```
System information
 DCS-7150S-52-CL 52-port SFP+ 10GigE 1RU + Clock
 02.00 JPE13120702 2013-03-27
System has 2 power supply slots
 Slot Model Serial Number
 ---- ---------------- ----------------
 1 PWR-460AC-F K192KU00241CZ
 2 PWR-460AC-F K192L200751CZ
System has 4 fan modules
 Module Number of Fans Model Serial Number
 ------- --------------- ---------------- ----------------
 1 1 FAN-7000-F N/A
 2 1 FAN-7000-F N/A
 3 1 FAN-7000-F N/A
 4 1 FAN-7000-F N/A
System has 53 ports
 Type Count
 ---------------- ----
 Management 1
 Switched 52
System has 52 transceiver slots
 Port Manufacturer Model Serial Number Rev
 ---- ---------------- ---------------- ---------------- ----
 1 Arista Networks SFP-10G-SR XCW1225FD753 0002
 2 Arista Networks SFP-10G-SR XCW1225FD753 0002
 51 Arista Networks SFP-10G-SR XCW1225FD753 0002
 52 Arista Networks SFP-10G-SR XCW1225FD753 0002
```

**Help:** execute the command "show inventory"

**Prompt:**
- arista_eos>
- arista_eos#

### show interfaces transceiver detail

**Output:**
```
mA: milliamperes, dBm: decibels (milliwatts), NA or N/A: not applicable.
 ++ : high alarm, +  : high warning, -  : low warning, -- : low alarm.
A2D readouts (if they differ), are reported in parentheses.
The threshold values are calibrated.
                         High Alarm  High Warn   Low Alarm   Low Warn    
           Temperature   Threshold   Threshold   Threshold   Threshold   
Port       (Celsius)     (Celsius)   (Celsius)   (Celsius)   (Celsius)   
-------    ------------  ----------  ----------  ----------  ----------  
Et6/1      27.48         80.00       75.00       -5.00       0.00        
Et6/2      27.48         80.00       75.00       -5.00       0.00        
Et6/3      27.48         80.00       75.00       -5.00       0.00        
Et6/4      27.48         80.00       75.00       -5.00       0.00           
                         High Alarm  High Warn   Low Alarm   Low Warn    
           Voltage       Threshold   Threshold   Threshold   Threshold   
Port       (Volts)       (Volts)     (Volts)     (Volts)     (Volts)     
-------    ------------  ----------  ----------  ----------  ----------  
Et6/1      3.30          3.60        3.50        3.00        3.10        
Et6/2      3.30          3.60        3.50        3.00        3.10        
Et6/3      3.30          3.60        3.50        3.00        3.10        
Et6/4      3.30          3.60        3.50        3.00        3.10            
                         High Alarm  High Warn   Low Alarm   Low Warn    
           Current       Threshold   Threshold   Threshold   Threshold   
Port       (mA)          (mA)        (mA)        (mA)        (mA)        
-------    ------------  ----------  ----------  ----------  ----------  
Et29/1     21.90         38.30       37.35       0.00        0.00        
Et29/2     21.90         38.30       37.35       0.00        0.00        
Et29/3     21.90         38.30       37.35       0.00        0.00        
Et29/4     21.90         38.30       37.35       0.00        0.00             
                         High Alarm  High Warn   Low Alarm   Low Warn    
           Tx Power      Threshold   Threshold   Threshold   Threshold   
Port       (dBm)         (dBm)       (dBm)       (dBm)       (dBm)       
-------    ------------  ----------  ----------  ----------  ----------  
Et6/1      -2.39         4.40        3.40        -9.60       -8.60       
Et6/2      -2.33         4.40        3.40        -9.60       -8.60       
Et6/3      -0.78         4.40        3.40        -9.60       -8.60       
Et6/4      -0.93         4.40        3.40        -9.60       -8.60               
                         High Alarm  High Warn   Low Alarm   Low Warn    
           Rx Power      Threshold   Threshold   Threshold   Threshold   
Port       (dBm)         (dBm)       (dBm)       (dBm)       (dBm)       
-------    ------------  ----------  ----------  ----------  ----------  
Et6/1      -0.90         4.40        3.40        -11.50      -10.50      
Et6/2      -0.94         4.40        3.40        -11.50      -10.50      
Et6/3      -1.00         4.40        3.40        -11.50      -10.50      
Et6/4      -0.83         4.40        3.40        -11.50      -10.50      
Et7/1      -1.15         4.40        3.40        -11.50      -10.50           

```

**Help:** execute the command "show interfaces transceiver detail"

**Prompt:**
- arista_eos>
- arista_eos#

### bash df -h

**Output:**
```
Filesystem      Size  Used Avail Use% Mounted on
none            4.6G   44M  4.5G   1% /
none            4.6G   44M  4.5G   1% /.overlay
devtmpfs        8.0M     0  8.0M   0% /dev
tmpfs            16G     0   16G   0% /dev/shm
tmpfs            16G  4.4M   16G   1% /run
tmpfs            16G     0   16G   0% /sys/fs/cgroup
tmpfs           4.6G  308K  4.6G   1% /tmp
tmpfs            64M  1.2M   63M   2% /.deltas
tmpfs            16G     0   16G   0% /var/run/netns
tmpfs           3.1G     0  3.1G   0% /var/core
tmpfs           3.1G   93M  3.0G   3% /var/log
tmpfs           1.0G  218M  807M  22% /var/shmem
/dev/sda1       3.3G  1.2G  2.2G  35% /mnt/flash
```

**Help:** execute the command "bash df -h"

**Prompt:**
- arista_eos>
- arista_eos#

### show environment cooling

**Output:**
```
System cooling status is: Ok
Ambient temperature: 22C
Airflow: front-to-back
Fan              Status          Configured Speed     Actual Speed
---------------- --------------- ---------------- ----------------
1/1              Ok                           35%              34%
1/2              Ok                           35%              35%
1/3              Ok                           35%              35%
1/4              Ok                           35%              34%
1/5              Ok                           35%              34%
2/1              Ok                           35%              34%
2/2              Ok                           35%              34%
2/3              Ok                           35%              35%
2/4              Ok                           35%              34%
2/5              Ok                           35%              35%
3/1              Ok                           35%              35%
3/2              Ok                           35%              34%
3/3              Ok                           35%              34%
3/4              Ok                           35%              35%
3/5              Ok                           35%              34%
4/1              Ok                           35%              34%
4/2              Ok                           35%              34%
4/3              Ok                           35%              35%
4/4              Ok                           35%              35%
4/5              Ok                           35%              34%
5/1              Ok                           35%              35%
5/2              Ok                           35%              34%
5/3              Ok                           35%              35%
5/4              Ok                           35%              34%
5/5              Ok                           35%              34%
6/1              Ok                           35%              35%
6/2              Ok                           35%              34%
6/3              Ok                           35%              35%
6/4              Ok                           35%              35%
6/5              Ok                           35%              34%
PowerSupply1/1   Ok                           70%              70%
PowerSupply2/1   Ok                           70%              69%
PowerSupply3/1   Ok                           70%              70%
PowerSupply4/1   Ok                           70%              69%
PowerSupply5     Not Inserted                 N/A              N/A
PowerSupply6/1   Ok                           70%              69%
PowerSupply7/1   Ok                           70%              70%
PowerSupply8     Not Inserted                 N/A              N/A
```

**Help:** execute the command "show environment cooling"

**Prompt:**
- arista_eos>
- arista_eos#

### show interfaces description

**Output:**
```
Interface                      Status         Protocol           Description
Et1                            admin down     down               ThiS iS a TeSt DeScriPtiON
Et2                            up             up                 ThiS iS a TeSt DeScriPtiON
Et3                            up             up                 ThiS iS a TeSt DeScriPtiON
Et4                            up             up                 ThiS iS a TeSt DeScriPtiON
Et5                            admin down     down               ThiS iS a TeSt DeScriPtiON
Et6                            admin down     down               ThiS iS a TeSt DeScriPtiON
Et7                            admin down     down               ThiS iS a TeSt DeScriPtiON
Et8                            admin down     down               ThiS iS a TeSt DeScriPtiON
Et9                            up             up                 ThiS iS a TeSt DeScriPtiON
Et9.999                        down           lowerlayerdown
Et10                           up             up                 ThiS iS a TeSt DeScriPtiON
Et11                           up             up                 ThiS iS a TeSt DeScriPtiON
Et12                           up             up                 ThiS iS a TeSt DeScriPtiON
Et13                           down           notpresent         This IS a TesT DeScrIption
Et14                           down           notpresent
Ma1                            down           down               Management
Po1                            up             up                 MLAG peer link
Po101                          up             up                 ServerRAD
Tu8                            down           unknown
Vl4094                         up             up                 MLAG local int

```

**Help:** execute the command "show interfaces description"

**Prompt:**
- arista_eos>
- arista_eos#

### show ip bgp summary

**Output:**
```
BGP summary information for VRF RED
Router identifier 192.168.1.1, local AS number 645001
Neighbor Status Codes: m - Under maintenance
  Neighbor         V  AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State  PfxRcd PfxAcc
  192.168.1.2      4  65002        1753556   1761743    0    0   40d23h Estab  7      4
BGP summary information for VRF WHITE
Router identifier 192.168.2.1, local AS number 65011
Neighbor Status Codes: m - Under maintenance
  Neighbor         V  AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State  PfxRcd PfxAcc
  192.168.2.2      4  65012        7405942   7406081    0    0  270d13h Estab  7      5
BGP summary information for VRF BLUE
Router identifier 192.168.3.1, local AS number 65021
Neighbor Status Codes: m - Under maintenance
  Neighbor         V  AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State  PfxRcd PfxAcc
  192.168.3.2      4  65022        1171721   1171752    0    0   67d19h Estab  25     25
  192.168.3.3      4  65023          97651     97643    0    0   40d23h Estab  18     18

```

**Help:** execute the command "show ip bgp summary"

**Prompt:**
- arista_eos>
- arista_eos#

### show ip ospf summary

**Output:**
```
OSPF instance 1 with ID 65.87.229.70, VRF default, ASBR
Time since last SPF: 14 s
Max LSAs: 12000, Total LSAs: 6
Type-5 Ext LSAs: 3
ID               Type   Intf   Nbrs (full) RTR LSA NW LSA  SUM LSA ASBR LSA TYPE-7 LSA
0.0.0.10         normal 6      2    (2   ) 3       0       0       0       0
 
OSPF instance 2 with ID 192.168.28.193, VRF mgmtVrf, ASBR
Time since last SPF: 1673 s
Max LSAs: 12000, Total LSAs: 357
Type-5 Ext LSAs: 152
ID               Type   Intf   Nbrs (full) RTR LSA NW LSA  SUM LSA ASBR LSA TYPE-7 LSA
0.0.0.0          normal 2      2    (2   ) 113     92      0       0       0
```

**Help:** execute the command "show ip ospf summary"

**Prompt:**
- arista_eos>
- arista_eos#

### show ip route

**Output:**
```
VRF: default
Codes: C - connected, S - static, K - kernel, 
       O - OSPF, IA - OSPF inter area, E1 - OSPF external type 1,
       E2 - OSPF external type 2, N1 - OSPF NSSA external type 1,
       N2 - OSPF NSSA external type2, B I - iBGP, B E - eBGP,
       R - RIP, I - ISIS, A B - BGP Aggregate, A O - OSPF Summary,
       NG - Nexthop Group Static Route 

Gateway of last resort is not set

 B E    10.1.31.100/32 [200/0] via 192.168.17.5, Ethernet18
 B E    10.1.31.101/32 [200/0] via 192.168.17.5, Ethernet18
 C      10.1.31.102/32 is directly connected, Loopback100
 C      10.1.31.200/32 is directly connected, Loopback10
 B E    10.1.31.254/32 [200/0] via 192.168.17.5, Ethernet18
 C      10.63.255.8/30 is directly connected, Ethernet20
 B E    10.100.22.52/30 [200/0] via 192.168.17.5, Ethernet18
 B E    10.100.22.56/30 [200/0] via 192.168.17.5, Ethernet18
 B E    10.100.233.11/32 [200/0] via 192.168.17.5, Ethernet18
 B E    10.100.233.12/32 [200/0] via 192.168.17.5, Ethernet18
 B E    10.100.233.15/32 [200/0] via 192.168.17.5, Ethernet18
 C      10.100.233.32/32 is directly connected, Loopback0
 B E    10.100.233.34/32 [200/0] via 192.168.38.5, Ethernet21
 B E    10.100.233.50/32 [200/0] via 192.168.17.5, Ethernet18
 B E    10.100.233.64/32 [200/0] via 192.168.17.5, Ethernet18
 B E    10.100.233.66/32 [200/0] via 192.168.17.5, Ethernet18
 B E    10.100.233.67/32 [200/0] via 192.168.17.5, Ethernet18
 B E    10.100.233.68/32 [200/0] via 192.168.17.5, Ethernet18
 B E    10.100.233.192/32 [200/0] via 10.63.255.10, Ethernet20



VRF: RED
Codes: C - connected, S - static, K - kernel, 
       O - OSPF, IA - OSPF inter area, E1 - OSPF external type 1,
       E2 - OSPF external type 2, N1 - OSPF NSSA external type 1,
       N2 - OSPF NSSA external type2, B I - iBGP, B E - eBGP,
       R - RIP, I - ISIS, A B - BGP Aggregate, A O - OSPF Summary,
       NG - Nexthop Group Static Route 

Gateway of last resort is not set

 B E    10.1.31.100/32 [200/0] via 192.168.17.5, Ethernet18
 B E    10.1.31.101/32 [200/0] via 192.168.17.5, Ethernet18
 C      10.1.31.102/32 is directly connected, Loopback100
 C      10.1.31.200/32 is directly connected, Loopback10
 B E    10.1.31.254/32 [200/0] via 192.168.17.5, Ethernet18
 C      10.63.255.8/30 is directly connected, Ethernet20
 B E    10.100.22.52/30 [200/0] via 192.168.17.5, Ethernet18
 B E    10.100.22.56/30 [200/0] via 192.168.17.5, Ethernet18
 B E    10.100.233.11/32 [200/0] via 192.168.17.5, Ethernet18
 B E    10.100.233.12/32 [200/0] via 192.168.17.5, Ethernet18
 B E    10.100.233.15/32 [200/0] via 192.168.17.5, Ethernet18
 C      10.100.233.32/32 is directly connected, Loopback0
 B E    10.100.233.34/32 [200/0] via 192.168.38.5, Ethernet21
 B E    10.100.233.50/32 [200/0] via 192.168.17.5, Ethernet18
 B E    10.100.233.64/32 [200/0] via 192.168.17.5, Ethernet18
 B E    10.100.233.66/32 [200/0] via 192.168.17.5, Ethernet18
 B E    10.100.233.67/32 [200/0] via 192.168.17.5, Ethernet18
 B E    10.100.233.68/32 [200/0] via 192.168.17.5, Ethernet18
 B E    10.100.233.192/32 [200/0] via 10.63.255.10, Ethernet20

```

**Help:** execute the command "show ip route"

**Prompt:**
- arista_eos>
- arista_eos#

### show ip ospf interface brief

**Output:**
```
   Interface    Instance VRF        Area            IP Address         Cost  State      Nbrs
   Lo0          1        default    0.0.0.10        192.0.2.1/32       10    DR         0
   Vl100        1        default    0.0.0.10        192.0.2.1/32       10    DR         0
   Vl200        1        default    0.0.0.10        192.0.2.1/32       10    DR         0
   Et10         1        default    0.0.0.10        192.0.2.1/32       10    DR         0
   Et20/1       1        default    0.0.0.10        192.0.2.1/32       50    P2P        1
   Et20/1.10    2        mgmtVrf    0.0.0.0         192.0.2.1/32       10    P2P        1
   Po1.10       2        mgmtVrf    0.0.0.0         192.0.2.1/32       10    P2P        1
```

**Help:** execute the command "show ip ospf interface brief"

**Prompt:**
- arista_eos>
- arista_eos#

### show mlag

**Output:**
```
MLAG Configuration:
domain-id           :          mlagDomain
local-interface     :            Vlan4094
peer-address        :            10.0.0.2
peer-link           :      Port-Channel10

MLAG Status:
state               :            Inactive
negotiation status  :          Connecting
peer-link status    :      Lowerlayerdown
local-int status    :                  Up
system-id           :   00:00:00:00:00:00

MLAG Ports:
Disabled            :                   0
Configured          :                   0
Inactive            :                   0
Active-partial      :                   0
Active-full         :                   0


```

**Help:** execute the command "show mlag"

**Prompt:**
- arista_eos>
- arista_eos#

### show pim ipv4 neighbor

**Output:**
```
PIM Neighbor Table for default VRF
Neighbor Address  Interface             Uptime    Expires   Mode    Transport
192.0.2.2         Ethernet20/1          02:26:03  00:00:16  sparse  datagram
192.0.2.4         Port-Channel1.10      02:25:25  00:01:25  sparse  datagram
192.0.2.6         Vlan100               02:04:47  00:01:32  sparse  datagram
192.0.2.8         Vlan200               02:04:47  00:01:35  sparse  datagram
```

**Help:** execute the command "show pim ipv4 neighbor"

**Prompt:**
- arista_eos>
- arista_eos#

### show ip arp

**Output:**
```
Address      Age (min) Hardware Addr  Interface
172.25.0.2           0 004c.6211.021e Vlan101, Port-Channel2
172.22.0.1           0 004c.6214.3699 Vlan1000, Port-Channel1
172.22.0.2           0 004c.6219.a0f3 Ethernet1
10.10.1.1          N/A 0002.00ff.0001 Vlan1, not learned

```

**Help:** execute the command "show ip arp"

**Prompt:**
- arista_eos>
- arista_eos#

### show clock

**Output:**
```
Mon Jan 14 18:42:49 2013
timezone is US/Central


```

**Help:** execute the command "show clock"

**Prompt:**
- arista_eos>
- arista_eos#

### show ip access-lists

**Output:**
```
IP Access List TEST_1
        10 permit ip host 10.0.0.1 10.0.0.0/24
 
IP Access List default-control-plane-acl [readonly]
        statistics per-entry
        10 permit icmp any any
        20 permit ip any any tracked
        30 permit udp any any eq bfd ttl eq 255
        50 permit tcp any any eq ssh telnet www snmp bgp https msdp
        60 permit udp any any eq bootps bootpc snmp rip ntp
        70 permit tcp any any range 5900 5910
        
IP Access List test2
        10 permit ip 1.1.1.0/30 any fragments log
        20 permit tcp 111.11.11.0/24 eq www z39-50 10.0.0.0/24 urg ttl eq 30
        
IP Access List test3
        10 permit tcp any range www ups any ack
        20 permit tcp any eq www ups telnet time tunnel uucp vmnet host 10.10.10.10 ack
        30 permit tcp any eq www ups telnet vmnet any log

```

**Help:** execute the command "show ip access-lists"

**Prompt:**
- arista_eos>
- arista_eos#

### show lldp neighbors

**Output:**
```
Last table change time   : 0:00:02 ago
Number of table inserts  : 2
 Number of table deletes  : 0
Number of table drops    : 0
Number of table age-outs : 0

Port       Neighbor Device ID             Neighbor Port ID           TTL
Et1        localhost                      Ethernet1                  120
Et2        localhost                      Ethernet2                  120
Et3/1      tg104.sjc.aristanetworks.com   Ethernet3/2                120
Ma1/1      dc1-rack11-tor1.sjc            1/1                        120

```

**Help:** execute the command "show lldp neighbors"

**Prompt:**
- arista_eos>
- arista_eos#

### show version

**Output:**
```
Arista vEOS
Hardware version:    
Serial number:       
System MAC address:  2803.829a.1347

Software image version: 4.14.7M
Architecture:           i386
Internal build version: 4.14.7M-2384414.4147M
Internal build ID:      92a53fad-f853-42a5-9f57-c3c4ea3c26b3

Uptime:                 1 hour and 5 minutes
Total memory:           2028860 kB
Free memory:            301240 kB

```

**Help:** execute the command "show version"

**Prompt:**
- arista_eos>
- arista_eos#

