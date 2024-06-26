# cisco_xr


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
- cisco_xr>

### show interfaces summary

**Output:**
```
Interface Type          Total    UP       Down     Admin Down
--------------          -----    --       ----     ----------
ALL TYPES               81       51       0        30
--------------
IFT_ETHERBUNDLE         11       11       0        0
IFT_HUNDREDGE           26       2        0        24
IFT_LOOPBACK            1        1        0        0
IFT_ETHERNET            2        0        0        2
IFT_NULL                1        1        0        0
IFT_TENGETHERNET        40       36       0        4


```

**Help:** execute the command "show interfaces summary"

**Prompt:**
- cisco_xr>
- cisco_xr#

### admin show vm

**Output:**
```
Wed Mar 14 10:04:35.018 UTC

Location: 0/0
Id                Status        IP Address       HB Sent/Recv
-------------------------------------------------------------
sysadmin          running       192.0.4.1        NA/NA
default-sdr       running       192.0.4.3        293478/293478

Location: 0/1
Id                Status        IP Address       HB Sent/Recv
-------------------------------------------------------------
sysadmin          running       192.0.8.1        NA/NA
default-sdr       running       192.0.8.3        293478/293478

Location: 0/2
Id                Status        IP Address       HB Sent/Recv
-------------------------------------------------------------
sysadmin          running       192.0.12.1       NA/NA
default-sdr       running       192.0.12.3       293478/293478

Location: 0/3
Id                Status        IP Address       HB Sent/Recv
-------------------------------------------------------------
sysadmin          running       192.0.16.1       NA/NA
default-sdr       running       192.0.16.3       293478/293478

Location: 0/4
Id                Status        IP Address       HB Sent/Recv
-------------------------------------------------------------
sysadmin          running       192.0.20.1       NA/NA
default-sdr       running       192.0.20.3       293478/293478

Location: 0/FC0
Id                Status        IP Address       HB Sent/Recv
-------------------------------------------------------------
sysadmin          running       192.0.84.1       NA/NA

Location: 0/FC1
Id                Status        IP Address       HB Sent/Recv
-------------------------------------------------------------
sysadmin          running       192.0.88.1       NA/NA

Location: 0/FC2
Id                Status        IP Address       HB Sent/Recv
-------------------------------------------------------------
sysadmin          running       192.0.92.1       NA/NA

Location: 0/FC3
Id                Status        IP Address       HB Sent/Recv
-------------------------------------------------------------
sysadmin          running       192.0.96.1       NA/NA

Location: 0/FC4
Id                Status        IP Address       HB Sent/Recv
-------------------------------------------------------------
sysadmin          running       192.0.100.1      NA/NA

Location: 0/FC5
Id                Status        IP Address       HB Sent/Recv
-------------------------------------------------------------
sysadmin          running       192.0.104.1      NA/NA

Location: 0/RP0
Id                Status        IP Address       HB Sent/Recv
-------------------------------------------------------------
sysadmin          running       192.0.108.1      NA/NA
default-sdr       running       192.0.108.4      5869560/5869560

Location: 0/SC0
Id                Status        IP Address       HB Sent/Recv
-------------------------------------------------------------
sysadmin          running       192.0.116.1      NA/NA

Location: 0/SC1
Id                Status        IP Address       HB Sent/Recv
-------------------------------------------------------------
sysadmin          running       192.0.120.1      NA/NA
```

**Help:** execute the command "admin show vm"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show interfaces

**Output:**
```
Mon Mar 20 17:31:48.208 EDT
Loopback5 is up, line protocol is up
  Interface state transitions: 1
  Hardware is Loopback interface(s)
  Description: $DCI ~Loopback for OSPF/LDP/BGP/TE
  Internet address is 192.168.169.21/32
  MTU 1500 bytes, BW 0 Kbit
     reliability Unknown, txload Unknown, rxload Unknown
  Encapsulation Loopback,  loopback not set,
  Last link flapped 6w1d
  Last input Unknown, output Unknown
  Last clearing of "show interface" counters Unknown
  Input/output data rate is disabled.

Null0 is up, line protocol is up
  Interface state transitions: 1
  Hardware is Null interface
  Internet address is Unknown
  MTU 1500 bytes, BW 0 Kbit
     reliability 255/255, txload Unknown, rxload Unknown
  Encapsulation Null,  loopback not set,
  Last link flapped 6w1d
  Last input never, output never
  Last clearing of "show interface" counters never
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 total input drops
     0 drops for unrecognized upper-level protocol
     Received 0 broadcast packets, 0 multicast packets
     0 packets output, 0 bytes, 0 total output drops
     Output 0 broadcast packets, 0 multicast packets

tunnel-te300 is up, line protocol is up
  Interface state transitions: 7
  Hardware is Tunnel-TE
  Description: $DCI TE Tunnel For REPLICATION to P-YB19-C95
  Internet address is 192.168.169.21/32
  MTU 1500 bytes, BW 0 Kbit
     reliability 255/255, txload Unknown, rxload Unknown
  Encapsulation TUNNEL,  loopback not set,
  Last link flapped 3w2d
  Last input never, output 00:00:00
  Last clearing of "show interface" counters never
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 2000 bits/sec, 1 packets/sec
     0 packets input, 0 bytes, 0 total input drops
     0 drops for unrecognized upper-level protocol
     Received 0 broadcast packets, 0 multicast packets
     1960425 packets output, 674297494 bytes, 0 total output drops
     Output 0 broadcast packets, 0 multicast packets

MgmtEth0/RSP0/CPU0/1 is administratively down, line protocol is administratively down
  Interface state transitions: 0
  Hardware is Management Ethernet, address is 5087.8966.5329 (bia 5087.8966.5329)
  Description: $DCI
  Internet address is Unknown
  MTU 1514 bytes, BW 0 Kbit
     reliability 255/255, txload Unknown, rxload Unknown
  Encapsulation ARPA,
  Duplex unknown, 0Kb/s, THD, link type is autonegotiation
  output flow control is off, input flow control is off
  loopback not set,
  Last input never, output never
  Last clearing of "show interface" counters never
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 total input drops
     0 drops for unrecognized upper-level protocol
     Received 0 broadcast packets, 0 multicast packets
              0 runts, 0 giants, 0 throttles, 0 parity
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     0 packets output, 0 bytes, 0 total output drops
     Output 0 broadcast packets, 0 multicast packets
     0 output errors, 0 underruns, 0 applique, 0 resets
     0 output buffer failures, 0 output buffers swapped out
     0 carrier transitions

MgmtEth0/RSP1/CPU0/0 is up, line protocol is up
  Interface state transitions: 1
  Hardware is Management Ethernet, address is f09e.6340.1420 (bia f09e.6340.1420)
  Description: Management Interface
  Internet address is 10.253.3.18/25
  MTU 1514 bytes, BW 1000000 Kbit (Max: 1000000 Kbit)
     reliability 255/255, txload 0/255, rxload 0/255
  Encapsulation ARPA,
  Full-duplex, 1000Mb/s, THD, link type is autonegotiation
  output flow control is off, input flow control is off
  loopback not set,
  Last link flapped 6w1d
  ARP type ARPA, ARP timeout 04:00:00
  Last input 00:00:11, output 00:00:41
  Last clearing of "show interface" counters never
  5 minute input rate 22000 bits/sec, 10 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     43738403 packets input, 12696681984 bytes, 0 total input drops
     2022343 drops for unrecognized upper-level protocol
     Received 194184 broadcast packets, 5015358 multicast packets
              0 runts, 0 giants, 0 throttles, 0 parity
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     121976 packets output, 18613909 bytes, 0 total output drops
     Output 2 broadcast packets, 62985 multicast packets
     0 output errors, 0 underruns, 0 applique, 0 resets
     0 output buffer failures, 0 output buffers swapped out
     1 carrier transitions

FortyGigE0/0/0/0 is up, line protocol is up
  Interface state transitions: 1
  Dampening enabled: penalty 0, not suppressed
    half-life:        1        reuse:             750
    suppress:         2000     max-suppress-time: 4
    restart-penalty:  0
  Hardware is FortyGigE, address is 5087.895f.81a0 (bia 5087.895f.81a0)
  Layer 1 Transport Mode is LAN
  Description: $DCI ~QTS Richmond DCI @CRDC %P-CRDC-C98 +Fort0/0/0/0 !CRIT
  Internet address is 192.168.166.9/30
  MTU 9216 bytes, BW 40000000 Kbit (Max: 40000000 Kbit)
     reliability 255/255, txload 0/255, rxload 0/255
  Encapsulation ARPA,
  Full-duplex, 40000Mb/s, link type is force-up
  output flow control is off, input flow control is off
  Carrier delay (up) is 9000 msec, Carrier delay (down) is 50 msec
  loopback not set,
  Last link flapped 6w1d
  ARP type ARPA, ARP timeout 04:00:00
  Last input 00:00:00, output 00:00:00
  Last clearing of "show interface" counters never
  30 second input rate 62000 bits/sec, 128 packets/sec
  30 second output rate 62000 bits/sec, 128 packets/sec
     478575583 packets input, 29095652278 bytes, 392 total input drops
     0 drops for unrecognized upper-level protocol
     Received 1 broadcast packets, 1675582 multicast packets
              0 runts, 0 giants, 0 throttles, 0 parity
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     478514791 packets output, 29002406808 bytes, 0 total output drops
     Output 2 broadcast packets, 1677091 multicast packets
     0 output errors, 0 underruns, 0 applique, 0 resets
     0 output buffer failures, 0 output buffers swapped out
     1 carrier transitions

TenGigE0/3/0/0 is up, line protocol is up
  Interface state transitions: 1
  Hardware is TenGigE, address is 5087.8964.53b0 (bia 5087.8964.53b0)
  Layer 1 Transport Mode is LAN
  Description: $DCI ~QTS Richmond Prod @CRDC %Z-CRDC-Dcc001 +Te5/1 !CRIT
  Internet address is 192.168.166.65/30
  MTU 9216 bytes, BW 10000000 Kbit (Max: 10000000 Kbit)
     reliability 255/255, txload 0/255, rxload 3/255
  Encapsulation ARPA,
  Full-duplex, 10000Mb/s, link type is force-up
  output flow control is off, input flow control is off
  Carrier delay (up) is 10 msec
  loopback not set,
  Last link flapped 6w1d
  ARP type ARPA, ARP timeout 04:00:00
  Last input 00:00:00, output 00:00:00
  Last clearing of "show interface" counters never
  30 second input rate 134379000 bits/sec, 26671 packets/sec
  30 second output rate 285000 bits/sec, 257 packets/sec
     74732197285 packets input, 48622921819223 bytes, 5 total input drops
     0 drops for unrecognized upper-level protocol
     Received 2 broadcast packets, 70041 multicast packets
              0 runts, 0 giants, 0 throttles, 0 parity
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     2222908838 packets output, 856734632077 bytes, 0 total output drops
     Output 1 broadcast packets, 63014 multicast packets
     0 output errors, 0 underruns, 0 applique, 0 resets
     0 output buffer failures, 0 output buffers swapped out
     1 carrier transitions

TenGigE0/3/0/4 is administratively down, line protocol is administratively down
  Interface state transitions: 0
  Hardware is TenGigE, address is 5087.8964.53b4 (bia 5087.8964.53b4)
  Layer 1 Transport Mode is LAN
  Internet address is Unknown
  MTU 1514 bytes, BW 10000000 Kbit (Max: 10000000 Kbit)
     reliability 255/255, txload 0/255, rxload 0/255
  Encapsulation ARPA,
  Full-duplex, 10000Mb/s, link type is force-up
  output flow control is off, input flow control is off
  Carrier delay (up) is 10 msec
  loopback not set,
  Last input never, output never
  Last clearing of "show interface" counters never
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 total input drops
     0 drops for unrecognized upper-level protocol
     Received 0 broadcast packets, 0 multicast packets
              0 runts, 0 giants, 0 throttles, 0 parity
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     0 packets output, 0 bytes, 0 total output drops
     Output 0 broadcast packets, 0 multicast packets
     0 output errors, 0 underruns, 0 applique, 0 resets
     0 output buffer failures, 0 output buffers swapped out
     0 carrier transitions

Bundle-Ether123456 is up, line protocol is up
  Interface state transitions: 1
  Hardware is Aggregated Ethernet interface(s), address is aaaa.bbbb.cccc
  Description: Bundle_example
  Internet address is Unknown
  MTU 1514 bytes, BW 10000000 Kbit (Max: 10000000 Kbit)
     reliability 255/255, txload 0/255, rxload 0/255
  Encapsulation ARPA,
  Full-duplex, 10000Mb/s
  loopback not set,
  Last link flapped 3w1d
    No. of members in this bundle: 1
      TenGigE0/3/0/4             Full-duplex  10000Mb/s    Active
  Last input 00:00:00, output 00:00:00
  Last clearing of "show interface" counters never
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 total input drops
     0 drops for unrecognized upper-level protocol
     Received 0 broadcast packets, 0 multicast packets
              0 runts, 0 giants, 0 throttles, 0 parity
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     0 packets output, 0 bytes, 0 total output drops
     Output 0 broadcast packets, 0 multicast packets
     0 output errors, 0 underruns, 0 applique, 0 resets
     0 output buffer failures, 0 output buffers swapped out
     0 carrier transitions

GigabitEthernet0/0/0/12.456 is administratively down, line protocol is administratively down
  Interface state transitions: 0
  Hardware is VLAN sub-interface(s), address is 5000.0002.000d
  Description: qsqsd svsdvxcvsdv
  Internet address is 192.168.5.1/24
  MTU 1518 bytes, BW 1000000 Kbit (Max: 1000000 Kbit)
     reliability 255/255, txload 0/255, rxload 0/255
  Encapsulation 802.1Q Virtual LAN, VLAN Id 456,  loopback not set,
  Last input never, output never
  Last clearing of "show interface" counters never
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 total input drops
     0 drops for unrecognized upper-level protocol
     Received 0 broadcast packets, 0 multicast packets
     0 packets output, 0 bytes, 0 total output drops
     Output 0 broadcast packets, 0 multicast packets

```

**Help:** execute the command "show interfaces"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show pim ipv4 interface

**Output:**
```

Wed Jul 27 17:18:38.018 CST

PIM interfaces in VRF default
Address               Interface                     PIM  Nbr   Hello  DR    DR
                                                         Count Intvl  Prior

192.0.2.1             BVI10                         on   11    30     1     192.0.2.2
192.0.2.1             Bundle-Ether10                on   2     30     1     192.0.2.2
192.0.2.1             Bundle-Ether10.10             on   2     30     1     192.0.2.2
192.0.2.1             Bundle-Ether10.20             on   2     30     1     192.0.2.2
192.0.2.1             Bundle-Ether10.30             on   2     30     1     192.0.2.2
```

**Help:** execute the command "show pim ipv4 interface"

**Prompt:**
- cisco_xr>
- cisco_xr#

### admin show environment fan

**Output:**
```
Sat Mar 10 14:03:31.155 UTC
===============================================================================
                        Fan speed (rpm)
Location   FRU Type           FAN_0   FAN_1   FAN_2   FAN_3   FAN_4   FAN_5   
                                  FAN_6   FAN_7   FAN_8   FAN_9  FAN_10  FAN_11
-------------------------------------------------------------------------------
0/FT0      NC55-5516-FAN       6192    3870    6214    3859    6257    3857   
                                   6420    4029    6390    3938    6467    4066   
0/FT1      NC55-5516-FAN       6360    3970    6143    3824    6033    3750   
                                   6279    3859    6060    3721    6375    3964   
0/FT2      NC55-5516-FAN       6545    4014    6474    3994    6000    3752   
                                   6375    4002    5921    3698    6308    3915   

0/PM0      NC55-PWR-3KW-AC     8021    8537   

0/PM1      NC55-PWR-3KW-AC     8064    8387   

0/PM2      NC55-PWR-3KW-AC     8064    8473   

0/PM3      NC55-PWR-3KW-AC     7978    8537   

0/PM4      NC55-PWR-3KW-AC     8064    8473   

0/PM5      NC55-PWR-3KW-AC     8086    8451   

0/PM6      NC55-PWR-3KW-AC     8086    8537   

0/PM7      NC55-PWR-3KW-AC     7978    8473   

0/PM8      NC55-PWR-3KW-AC     8000    8516   

0/PM9      NC55-PWR-3KW-AC     8021    8516 
  
```

**Help:** execute the command "admin show environment fan"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show bgp

**Output:**
```
Wed Jun 20 18:46:11.356 BST
BGP router identifier 84.38.34.56, local AS number 65444
BGP generic scan interval 60 secs
Non-stop routing is enabled
 BGP table state: Active
Table ID: 0xe0000000   RD version: 111676729
BGP main routing table version 111676729
BGP NSR Initial initsync version 5 (Reached)
 BGP NSR/ISSU Sync-Group versions 111676729/0
BGP scan interval 60 secs

 Status codes: s suppressed, d damped, h history, * valid, > best
              i - internal, r RIB-failure, S stale, N Nexthop-discard
Origin codes: i - IGP, e - EGP, ? - incomplete
   Network            Next Hop            Metric LocPrf Weight Path
*> 111.111.111.111/32 112.112.112.112 4294967295 4294967295  65535 1000 1000 1000 i
*>i                   113.113.113.113 4294967295 4294967295  65535 1000 1000 1000 i
*>                    114.114.114.114          5          5  65535 1000 1000 1000 i
*>i                   2.2.2.2         4294967295 4294967295  65535 1000 1000 1000 i
*>                    3.3.3.3                                65535 1000 1000 1000 i
*>                    4.4.4.4                  5             65535 1000 1000 1000 i
*>                    5.5.5.5                             5  65535 1000 1000 1000 i
*>                    6.6.6.6                                1 5 1000 1000 1000 i
*>                    7.7.7.7                                1 i
*> 113.113.113.113/32 114.114.114.114          5      5      5 1000 1000 1000 i
*> 115.115.115.115/32 116.116.116.116                        5 1000 i
*> 117.117.117.117/32 118.118.118.118                        5 i
*> 0.0.0.0/0          2.2.2.2         4294967295 4294967295  65535 1000 1000 1000 i
*> 3.3.3.3/32         4.4.4.4                  5      5      5 1000 1000 1000 i
 *> 5.5.5.5/32         6.6.6.6                                5 1000 1000 1000 i
*> 7.7.7.7/32         8.8.8.8                                5 1000 1000 1000 i
*> 9.9.9.9/32         0.0.0.0                                5 i
*>                    1.1.1.1         4294967295 4294967295  65535 1000 1000 1000 i
*>                    2.2.2.2                  5          5  5 1000 1000 1000 i
*>                    3.3.3.3                                5 1000 1000 1000 i
*>                    4.4.4.4                             5  5 1000 1000 1000 i
*>                    5.5.5.5                  5             5 1000 1000 1000 i
*>                    6.6.6.6                  5          5  5 i
*>                    7.7.7.7                                5 i

```

**Help:** execute the command "show bgp"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show dhcp ipv4 proxy binding

**Output:**
```

                                           Lease
 MAC Address      IP Address      State    Remaining       Interface          VRF      Sublabel
--------------  --------------  ---------  ---------  -------------------  ---------  ----------
2cb0.5d00.000a  10.248.159.182  BOUND      8691       BE1.201              default    0x11664
20d5.bf00.000b  10.48.93.39     BOUND      10315      BE1.1530             cust-a 0x1853b
a4b1.e900.000c  10.200.185.166 BOUND      10617      BE1.1502             default    0x1cf76
3091.8f00.000d  10.200.185.165 DELETING   N/A        BE1.1526             default    0x10606
0006.1900.000e  10.184.88.53    OFFER_SENT 27         BE1.1534             cust-b 0xa98d
0026.f200.000f  10.200.185.170 BOUND      10794      BE1.1546             default    0x1bb34
0006.1900.0010  10.184.88.24    OFFER_SENT 54         BE1.1535             cust-b 0x44d0
0002.9b00.0011  10.48.90.0      BOUND      10796      BE1.1543             cust-a 0x1c5cc

```

**Help:** execute the command "show dhcp ipv4 proxy binding"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show configuration commit list

**Output:**
```
SNo. Label/ID    User      Line                Client      Time Stamp
 ~~~~ ~~~~~~~~    ~~~~      ~~~~                ~~~~~~      ~~~~~~~~~~
1    1000000093  fred      vty0:node0_RSP0_CP  CLI         Tue Jun  7 14:42:19 2016
2    1000000092  john      vty0:node0_RSP0_CP  CLI         Tue Jun  7 14:40:05 2016
3    1000000091  john      vty0:node0_RSP0_CP  CLI         Tue Jun  7 14:33:52 2016
4    1000000090  john      vty0:node0_RSP0_CP  CLI         Tue Jun  7 14:33:05 2016
5    1000000089  fred      vty0:node0_RSP0_CP  CLI         Tue Jun  7 14:31:39 2016
6    1000000088  patrick   vty1:node0_RSP0_CP  Rollback    Tue Jun  7 14:29:12 2016
7    1000000087  john      vty1:node0_RSP0_CP  CLI         Fri Jun  3 14:33:27 2016
8    1000000086  admin     vty0:node0_RSP0_CP  CLI         Wed May 25 13:43:18 2016
9    1000000085  admin     vty0:node0_RSP0_CP  CLI         Fri May 20 10:06:01 2016
10   1000000084  admin     vty0:node0_RSP0_CP  CLI         Wed May 11 13:32:10 2016
11   1000000083  patrick   vty0:node0_RSP0_CP  CLI         Tue May 10 14:18:59 2016

```

**Help:** execute the command "show configuration commit list"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show lldp neighbors detail

**Output:**
```
Tue Jan 16 13:49:50.315 AEST
Capability codes:
        (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
        (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other

------------------------------------------------
 Local Interface: FourHundredGigE0/0/0/0
Chassis id: 6c03.b5aa.bbcc
Port id: Fou1/0/22
Port Description: uplink:router1:FH0/0/0/0
System Name: router-400.router.com
 
System Description:
Cisco IOS Software [Cupertino], Catalyst L3 Switch Software (CAT9K_IOSXE), Version 17.9.3, RELEASE SOFTWARE (fc6)
Technical Support: http://www.cisco.com/techsupport
 Copyright (c) 1986-2023 by Cisco Systems, Inc.
Compiled Tue 14-Mar-23 18:26 by mcpre

Time remaining: 90 seconds
Hold Time: 120 seconds
Age: 732802 seconds
System Capabilities: B,R
Enabled Capabilities: B,R
Management Addresses:
  IPv4 address: 172.1.1.79
  IPv6 address: 2407:abcd:0:aaaa::0000

Peer MAC Address: 6c:03:b5:aa:bb:cc


------------------------------------------------
 Local Interface: FourHundredGigE0/0/0/28
Chassis id: d0dc.2cdd.aabc
Port id: FourHundredGigE0/0/0/28
Port Description: uplink:router1::FH0/0/0/28
System Name: router2.com

System Description:
7.9.2, 8000

Time remaining: 98 seconds
Hold Time: 120 seconds
Age: 729378 seconds
System Capabilities: R
 Enabled Capabilities: R
Management Addresses:
  IPv4 address: 172.1.1.64
  IPv6 address: 2407:abcd::aaab::0000

Peer MAC Address: d0:dc:2c:aa:bb:cc
 

------------------------------------------------
Local Interface: FourHundredGigE0/0/0/29
 Chassis id: d0dc.abcd.dcba
Port id: FourHundredGigE0/0/0/29
Port Description: uplink:router1:FH0/0/0/29
System Name: router66.router.com

System Description:
 7.9.2, 8000

Time remaining: 100 seconds
Hold Time: 120 seconds
Age: 729313 seconds
System Capabilities: R
Enabled Capabilities: R
Management Addresses:
  IPv4 address: 172.1.1.66
  IPv6 address: 2407:abcd:0:aaac::0000

Peer MAC Address: d0:dc:2c:aa:bb:cd


------------------------------------------------
 Local Interface: HundredGigE0/0/0/30
Chassis id: 247e.32bb.0000
Port id: Eth1/4
 Port Description: router1:Hun1/0/30
System Name: otter-buffy

System Description:
 Cisco NX-OS(tm) n7700, Software (n7700-s2-dk9), Version 8.4(3), RELEASE SOFTWARE Copyright (c) 2002-2020 by Cisco Systems, Inc. Compiled 9/4/2020 23:00:00

 Time remaining: 117 seconds
Hold Time: 120 seconds
Age: 732508 seconds
System Capabilities: B,R
Enabled Capabilities: B,R
Management Addresses:
  IPv4 address: 172.1.1.158

Peer MAC Address: 24:7e:12:aa:bb:cc


------------------------------------------------
 Local Interface: HundredGigE0/0/0/31
Chassis id: 2cab.ebe1.ffff
Port id: Eth2/4
 Port Description: uplink:router1:Hun1/0/31
System Name: onyx.mgmt.com

System Description:
Cisco NX-OS(tm) n7700, Software (n7700-s2-dk9), Version 8.4(3), RELEASE SOFTWARE Copyright (c) 2002-2020 by Cisco Systems, Inc. Compiled 9/4/2020 23:00:00

Time remaining: 104 seconds
Hold Time: 120 seconds
Age: 732462 seconds
System Capabilities: B,R
Enabled Capabilities: B,R
Management Addresses:
  IPv4 address: 172.1.1.158

Peer MAC Address: 2c:ab:eb:aa:bb:cc


Total entries displayed: 5
```

**Help:** execute the command "show lldp neighbors detail"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show rsvp neighbors

**Output:**
```
Global Neighbor: 10.100.100.120
  Interface Neighbor   Interface   
  -------------------- ------------
  10.100.100.141       FortyGigE0/0/1/0
  10.100.100.145       FortyGigE0/1/1/0

```

**Help:** execute the command "show rsvp neighbors"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show arp

**Output:**
```

Mon Oct 17 02:44:29.814 UTC

-------------------------------------------------------------------------------
0/0/CPU0
-------------------------------------------------------------------------------
Address         Age        Hardware Addr   State      Type  Interface
192.0.2.1       01:31:14   ca01.1d8b.0008  Dynamic    ARPA  GigabitEthernet0/0/0/0
192.0.2.2       01:46:18   ca02.1d99.0008  Dynamic    ARPA  GigabitEthernet0/0/0/0
192.0.2.3       01:46:16   ca03.1da7.0008  Dynamic    ARPA  GigabitEthernet0/0/0/0
192.0.2.4       01:46:15   ca04.1db5.0008  Dynamic    ARPA  GigabitEthernet0/0/0/0
192.0.2.5       01:46:13   ca05.1dc3.0008  Dynamic    ARPA  GigabitEthernet0/0/0/0
192.0.2.10      -          0c99.6869.0003  Interface  ARPA  GigabitEthernet0/0/0/0
192.0.2.11      01:43:41   0ca1.f3ee.0ba0  Dynamic    ARPA  GigabitEthernet0/0/0/0

-------------------------------------------------------------------------------
0/RP0/CPU0
-------------------------------------------------------------------------------
Address         Age        Hardware Addr   State      Type  Interface
192.168.57.1    00:00:02   5254.004e.1156  Dynamic    ARPA  MgmtEth0/RP0/CPU0/0
192.168.57.10   -          0c99.6869.0000  Interface  ARPA  MgmtEth0/RP0/CPU0/0
```

**Help:** execute the command "show arp"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show controllers HundredGigabitEthernet

**Output:**
```
Thu Dec 21 06:15:50.979 UTC
Operational data for interface HundredGigE0/0/0/0:

State:
    Administrative state: enabled
    Operational state: Up
    LED state: Green On

Phy:
    Media type: Active optical cable
    Optics:
        Vendor: AOI             
        Part number: AQPA9N09ADLN0778
        Serial number: 04517A10025     
        Wavelength: 850 nm
    Digital Optical Monitoring:
        Transceiver Temp: 17.070 C
        Transceiver Voltage: 3.447 V

        Alarms key: (H) Alarm high, (h) Warning high
                    (L) Alarm low, (l) Warning low
           Wavelength    Tx Power          Rx Power      Laser Bias
        00     n/a     0.1   1.0205     -1.8   0.6627     5.450 
        00     n/a     -0.1   0.9775     -1.1   0.7788     5.240 
        00     n/a     0.3   1.0617     -1.2   0.7626     5.240 
        00     n/a     -0.3   0.9281     -2.1   0.6213     5.240 
        DOM alarms:
            No alarms

        Alarm                     Alarm    Warning   Warning    Alarm
        Thresholds                High      High       Low       Low
                                 -------   -------   -------   -------
        Transceiver Temp (C):     80.000     0.000     0.000    -5.000
        Transceiver Voltage (V):   3.600     0.000     0.000     3.000
        Laser Bias (mA):             n/a       n/a       n/a       n/a
        Transmit Power (mW):       2.754     0.000     0.000     0.091
        Transmit Power (dBm):      4.400      -inf      -inf   -10.410
        Receive Power (mW):        2.754     0.000     0.000     0.058
        Receive Power (dBm):       4.400      -inf      -inf   -12.366
    Statistics:
        FEC:
            Corrected Codeword Count: 0
            Uncorrected Codeword Count: 0

MAC address information:
    Operational address: 008a.9658.f904
    Burnt-in address: 008a.9658.f000

Autonegotiation disabled.

Operational values:
    Speed: 100Gbps
    Duplex: Full Duplex
    Flowcontrol: None
    Loopback: None (or external)
    MTU: 9114
    MRU: 9114
    Forward error correction: Disabled
          
          
Operational data for interface HundredGigE0/0/0/1:
          
State:    
    Administrative state: enabled
    Operational state: Up
    LED state: Green On
          
Phy:      
    Media type: Active optical cable
    Optics:
        Vendor: Ligent Photonics
        Part number: DQF8503-4C13    
        Serial number: S516CBD0371     
        Wavelength: 850 nm
    Digital Optical Monitoring:
        Transceiver Temp: 18.000 C
        Transceiver Voltage: 3.338 V
          
        Alarms key: (H) Alarm high, (h) Warning high
                    (L) Alarm low, (l) Warning low
           Wavelength    Tx Power          Rx Power      Laser Bias
        Lane  (nm)    (dBm)    (mW)     (dBm)     (mW)      (mA)
        --   -----   ------   ------    ------   ------    ------
        00     n/a     -40.0   0.0001     -0.6   0.8658     5.930 
        00     n/a     -40.0   0.0001     -0.6   0.8796     5.940 
        00     n/a     -40.0   0.0001     -0.6   0.8742     5.932 
        00     n/a     -40.0   0.0001     -0.7   0.8572     5.940 
          
        DOM alarms:
            No alarms

        Alarm                     Alarm    Warning   Warning    Alarm
        Thresholds                High      High       Low       Low
                                 -------   -------   -------   -------
        Transceiver Temp (C):     80.000     0.000     0.000    -10.000
        Transceiver Voltage (V):   3.600     0.000     0.000     3.000
        Laser Bias (mA):             n/a       n/a       n/a       n/a
        Transmit Power (mW):       1.949     0.000     0.000     0.087
        Transmit Power (dBm):      2.898      -inf      -inf   -10.605
        Receive Power (mW):        2.754     0.000     0.000     0.051
        Receive Power (dBm):       4.400      -inf      -inf   -12.924
    Statistics:
        FEC:
            Corrected Codeword Count: 0
            Uncorrected Codeword Count: 0

MAC address information:
    Operational address: 008a.9661.d904
    Burnt-in address: 008a.9661.d004

Autonegotiation disabled.

Operational values:
    Speed: 100Gbps
    Duplex: Full Duplex
    Flowcontrol: None
    Loopback: None (or external)
    MTU: 9114
    MRU: 9114
    Forward error correction: Disabled
```

**Help:** execute the command "show controllers HundredGigabitEthernet"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show controllers fabric fia errors ingress location

**Output:**
```
********** FIA-0 **********
Category: in_error-0
                             To Xbar Uc Crc-0                       11
                             To Xbar Uc Crc-1                       22
                             To Xbar Uc Crc-2                       33
                             To Xbar Uc Crc-3                       44
                             To Xbar Mc Crc-0                       55
                             To Xbar Mc Crc-1                       66
                             To Xbar Mc Crc-2                       77
                             To Xbar Mc Crc-3                        0
                          nb pa read data err                    12334
                                pa header err                        0
                                 pa crc16 err                        0
                                 pa crc32 err                        0
                                 pa to tf err                    99999
                         ab overflow req lost                        0
                                 ni bad crc32                        0
                             ni crc32 corrupt                        0

 ********** FIA-1 **********
Category: in_error-1
                             To Xbar Uc Crc-0                        0
                             To Xbar Uc Crc-1                        0
                             To Xbar Uc Crc-2                        0
                             To Xbar Uc Crc-3                        0
                             To Xbar Mc Crc-0                        0
                             To Xbar Mc Crc-1                        0
                             To Xbar Mc Crc-2                        0
                             To Xbar Mc Crc-3                        0
                          nb pa read data err                        0
                                pa header err                        0
                                 pa crc16 err                        0
                                 pa crc32 err                        0
                                 pa to tf err                        0
                         ab overflow req lost                        0
                                 ni bad crc32                        0
                             ni crc32 corrupt                 11111111

 ********** FIA-2 **********
Category: in_error-2
                             To Xbar Uc Crc-0                        0
                             To Xbar Uc Crc-1                        0
                             To Xbar Uc Crc-2                        0
                             To Xbar Uc Crc-3                        0
                             To Xbar Mc Crc-0                        0
                             To Xbar Mc Crc-1                        0
                             To Xbar Mc Crc-2                        0
                             To Xbar Mc Crc-3                        0
                          nb pa read data err                        0
                                pa header err                        0
                                 pa crc16 err                        0
                                 pa crc32 err                        0
                                 pa to tf err                        0
                         ab overflow req lost                        0
                                 ni bad crc32                        0
                             ni crc32 corrupt                        0

 ********** FIA-3 **********
Category: in_error-3
                             To Xbar Uc Crc-0                        0
                             To Xbar Uc Crc-1                        0
                             To Xbar Uc Crc-2                        0
                             To Xbar Uc Crc-3                        0
                             To Xbar Mc Crc-0                        0
                             To Xbar Mc Crc-1                        0
                             To Xbar Mc Crc-2                        0
                             To Xbar Mc Crc-3                        0
                          nb pa read data err                        0
                                pa header err                        0
                                 pa crc16 err                        0
                                 pa crc32 err                        0
                                 pa to tf err                        0
                         ab overflow req lost                        0
                                 ni bad crc32                        0
                             ni crc32 corrupt                        0

```

**Help:** execute the command "show controllers fabric fia errors ingress location"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show mpls ldp neighbor brief

**Output:**
```
Tue Mar  7 14:35:15.185 EST

Peer               GR  NSR  Up Time     Discovery   Addresses     Labels    
                                        ipv4  ipv6  ipv4  ipv6  ipv4   ipv6 
-----------------  --  ---  ----------  ----------  ----------  ------------
10.100.100.120:0   Y   Y    4w2d        3     0     10    0     56     0    
10.100.100.119:0   Y   Y    4w2d        3     0     10    0     56     0    
10.100.100.121:0   Y   N/A  4w2d        3     0     8     0     57     0    


```

**Help:** execute the command "show mpls ldp neighbor brief"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show controllers fabric fia drops egress location

**Output:**
```
********** FIA-0 **********
Category: eg_drop-0
                           From Xbar Uc Crc-0                       11
                           From Xbar Uc Crc-1                       22
                           From Xbar Uc Crc-2                       33
                           From Xbar Uc Crc-3                       44
                           From Xbar Uc Drp-0                       55
                           From Xbar Uc Drp-1                       66
                           From Xbar Uc Drp-2                       77
                           From Xbar Uc Drp-3                       88
                           From Xbar Mc Crc-0                        0
                           From Xbar Mc Crc-1                        1
                           From Xbar Mc Crc-2                        2
                           From Xbar Mc Crc-3                        3
                           From Xbar Mc Drp-0                        4
                           From Xbar Mc Drp-1                        5
                           From Xbar Mc Drp-2                        6
                           From Xbar Mc Drp-3                        7
       Uc dq pkt-len-crc/RO-seq/len error drp                        8
                 Uc eq pkt-len-crc/lookup-drp                   999999
                                Mc rf crc drp                        0
                  Mc vl0 src0 buffer full drp                        0
                  Mc vl1 src0 buffer full drp                        0
                  Mc vl2 src0 buffer full drp                        0
                  Mc vl3 src0 buffer full drp                        0
                  Mc vl0 src1 buffer full drp                        0
                  Mc vl1 src1 buffer full drp                        0
                  Mc vl2 src1 buffer full drp                        0
                  Mc vl3 src1 buffer full drp                        0

 ********** FIA-1 **********
Category: eg_drop-1
                           From Xbar Uc Crc-0                        0
                           From Xbar Uc Crc-1                        0
                           From Xbar Uc Crc-2                        0
                           From Xbar Uc Crc-3                        0
                           From Xbar Uc Drp-0                        0
                           From Xbar Uc Drp-1                        0
                           From Xbar Uc Drp-2                        0
                           From Xbar Uc Drp-3                        0
                           From Xbar Mc Crc-0                        0
                           From Xbar Mc Crc-1                        0
                           From Xbar Mc Crc-2                        0
                           From Xbar Mc Crc-3                        0
                           From Xbar Mc Drp-0                        0
                           From Xbar Mc Drp-1                        0
                           From Xbar Mc Drp-2                        0
                           From Xbar Mc Drp-3                        0
       Uc dq pkt-len-crc/RO-seq/len error drp                        0
                 Uc eq pkt-len-crc/lookup-drp                        0
                                Mc rf crc drp                        0
                  Mc vl0 src0 buffer full drp                        0
                  Mc vl1 src0 buffer full drp                        0
                  Mc vl2 src0 buffer full drp                        0
                  Mc vl3 src0 buffer full drp                        0
                  Mc vl0 src1 buffer full drp                        0
                  Mc vl1 src1 buffer full drp                        0
                  Mc vl2 src1 buffer full drp                        0
                  Mc vl3 src1 buffer full drp                        0

 ********** FIA-2 **********
Category: eg_drop-2
                           From Xbar Uc Crc-0                        0
                           From Xbar Uc Crc-1                        0
                           From Xbar Uc Crc-2                        0
                           From Xbar Uc Crc-3                        0
                           From Xbar Uc Drp-0                        0
                           From Xbar Uc Drp-1                        0
                           From Xbar Uc Drp-2                        0
                           From Xbar Uc Drp-3                        0
                           From Xbar Mc Crc-0                        0
                           From Xbar Mc Crc-1                        0
                           From Xbar Mc Crc-2                        0
                           From Xbar Mc Crc-3                        0
                           From Xbar Mc Drp-0                        0
                           From Xbar Mc Drp-1                        0
                           From Xbar Mc Drp-2                        0
                           From Xbar Mc Drp-3                        0
       Uc dq pkt-len-crc/RO-seq/len error drp                        0
                 Uc eq pkt-len-crc/lookup-drp                        0
                                Mc rf crc drp                        0
                  Mc vl0 src0 buffer full drp                        0
                  Mc vl1 src0 buffer full drp                        0
                  Mc vl2 src0 buffer full drp                        0
                  Mc vl3 src0 buffer full drp                        0
                  Mc vl0 src1 buffer full drp                        0
                  Mc vl1 src1 buffer full drp                        0
                  Mc vl2 src1 buffer full drp                        0
                  Mc vl3 src1 buffer full drp                        0

 ********** FIA-3 **********
Category: eg_drop-3
                           From Xbar Uc Crc-0                        0
                           From Xbar Uc Crc-1                        0
                           From Xbar Uc Crc-2                        0
                           From Xbar Uc Crc-3                        0
                           From Xbar Uc Drp-0                        0
                           From Xbar Uc Drp-1                        0
                           From Xbar Uc Drp-2                        0
                           From Xbar Uc Drp-3                        0
                           From Xbar Mc Crc-0                        0
                           From Xbar Mc Crc-1                        0
                           From Xbar Mc Crc-2                        0
                           From Xbar Mc Crc-3                        0
                           From Xbar Mc Drp-0                        0
                           From Xbar Mc Drp-1                        0
                           From Xbar Mc Drp-2                        0
                           From Xbar Mc Drp-3                        0
       Uc dq pkt-len-crc/RO-seq/len error drp                        0
                 Uc eq pkt-len-crc/lookup-drp                        0
                                Mc rf crc drp                        0
                  Mc vl0 src0 buffer full drp                        0
                  Mc vl1 src0 buffer full drp                        0
                  Mc vl2 src0 buffer full drp                        0
                  Mc vl3 src0 buffer full drp                        0
                  Mc vl0 src1 buffer full drp                        0
                  Mc vl1 src1 buffer full drp                        0
                  Mc vl2 src1 buffer full drp                        0
                  Mc vl3 src1 buffer full drp                        0

```

**Help:** execute the command "show controllers fabric fia drops egress location"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show cef drops location

**Output:**
```
CEF Drop Statistics
Node: 0/RSP0/CPU0
  Unresolved drops     packets :              11
  Unsupported drops    packets :              22
  Null0 drops          packets :              33
  No route drops       packets :              44
  No Adjacency drops   packets :              55
  Checksum error drops packets :              66
  RPF drops            packets :              77
  RPF suppressed drops packets :               0
  RP destined drops    packets :               0
  Discard drops        packets :               0
  GRE lookup drops     packets :               0
  GRE processing drops packets :               0
  LISP punt drops      packets :          999999
  LISP encap err drops packets :               0
  LISP decap err drops packets :               0
Node: 0/RSP1/CPU0
  Unresolved drops     packets :               0
  Unsupported drops    packets :               0
  Null0 drops          packets :               0
  No route drops       packets :              79
  No Adjacency drops   packets :               0
  Checksum error drops packets :               0
  RPF drops            packets :               0
  RPF suppressed drops packets :               0
  RP destined drops    packets :               0
  Discard drops        packets :               0
  GRE lookup drops     packets :               0
  GRE processing drops packets :               0
  LISP punt drops      packets :               0
  LISP encap err drops packets :               0
  LISP decap err drops packets :               0
Node: 0/0/CPU0
  Unresolved drops     packets :               0
  Unsupported drops    packets :               0
  Null0 drops          packets :               0
  No route drops       packets :               0
  No Adjacency drops   packets :               0
  Checksum error drops packets :               0
  RPF drops            packets :               0
  RPF suppressed drops packets :               0
  RP destined drops    packets :               0
  Discard drops        packets :              97
  GRE lookup drops     packets :               0
  GRE processing drops packets :               0
  LISP punt drops      packets :               0
  LISP encap err drops packets :               0
  LISP decap err drops packets :               0
Node: 0/7/CPU0
  Unresolved drops     packets :               0
  Unsupported drops    packets :               0
  Null0 drops          packets :               0
  No route drops       packets :               9
  No Adjacency drops   packets :               0
  Checksum error drops packets :               0
  RPF drops            packets :               0
  RPF suppressed drops packets :               0
  RP destined drops    packets :               0
  Discard drops        packets :             106
  GRE lookup drops     packets :               0
  GRE processing drops packets :               0
  LISP punt drops      packets :               0
  LISP encap err drops packets :               0
  LISP decap err drops packets :               0

```

**Help:** execute the command "show cef drops location"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show bgp vrf all ipv4 unicast summary

**Output:**
```
Tue Mar 21 09:08:19.039 EDT

VRF: DR
-------
BGP VRF DR, state: Active
 BGP Route Distinguisher: 10.1.1.1:5
VRF ID: 0x60000002
BGP router identifier 10.1.1.1, local AS number 15005
Non-stop routing is enabled
BGP table state: Active
Table ID: 0xe0000011   RD version: 184934
BGP main routing table version 31259922
BGP NSR Initial initsync version 17 (Reached)
BGP NSR/ISSU Sync-Group versions 31259922/0

BGP is operating in STANDALONE mode.


Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
Speaker        31259922   31259922   31259922   31259922    31259922    31259922
 

VRF: PROD
---------
BGP VRF PROD, state: Active
BGP Route Distinguisher: 10.1.1.1:3
VRF ID: 0x60000003
BGP router identifier 10.1.1.1, local AS number 15005
Non-stop routing is enabled
BGP table state: Active
Table ID: 0xe0000012   RD version: 31259922
BGP main routing table version 31259922
BGP NSR Initial initsync version 17 (Reached)
BGP NSR/ISSU Sync-Group versions 31259922/0
 
BGP is operating in STANDALONE mode.


Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
Speaker        31259922   31259922   31259922   31259922    31259922    31259922

Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
10.10.10.10       0 65370   83403   96226 31259922    0    0     6w2d      34543

VRF: REPL
 ---------
BGP VRF REPL, state: Active
BGP Route Distinguisher: 10.1.1.1:1
 VRF ID: 0x60000004
BGP router identifier 10.1.1.1, local AS number 15005
 Non-stop routing is enabled
BGP table state: Active
Table ID: 0xe0000013   RD version: 31259922
BGP main routing table version 31259922
BGP NSR Initial initsync version 17 (Reached)
BGP NSR/ISSU Sync-Group versions 31259922/0
 
BGP is operating in STANDALONE mode.


Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
Speaker        31259922   31259922   31259922   31259922    31259922    31259922

Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
172.16.16.10   0 65320   63970   64069 31259922    0    0     6w2d          1


VRF: EXTRANET
 -------------
BGP VRF EXTRANET, state: Active
BGP Route Distinguisher: 10.1.1.1:7
 VRF ID: 0x60000005
BGP router identifier 10.1.1.1, local AS number 15005
 Non-stop routing is enabled
BGP table state: Active
Table ID: 0xe0000014   RD version: 31162685
BGP main routing table version 31259922
BGP NSR Initial initsync version 17 (Reached)
BGP NSR/ISSU Sync-Group versions 31259922/0
 
BGP is operating in STANDALONE mode.


Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
Speaker        31259922   31259922   31259922   31259922    31259922    31259922


VRF: EXTRANET2
--------------
 BGP VRF EXTRANET2, state: Active
BGP Route Distinguisher: 10.1.1.1:8
VRF ID: 0x60000007
BGP router identifier 10.1.1.1, local AS number 15005
Non-stop routing is enabled
BGP table state: Active
Table ID: 0xe0000016   RD version: 31259922
BGP main routing table version 31259922
BGP NSR Initial initsync version 17 (Reached)
BGP NSR/ISSU Sync-Group versions 31259922/0

BGP is operating in STANDALONE mode.


Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
Speaker        31259922   31259922   31259922   31259922    31259922    31259922


VRF: vrf-test
-------------
BGP VRF vrf-test, state: Active
BGP Route Distinguisher: 65000:42
VRF ID: 0x60000003
 BGP router identifier 0.0.0.0, local AS number 65000
Non-stop routing is enabled
 BGP table state: Active
Table ID: 0xe0000012   RD version: 0
BGP main routing table version 1
BGP NSR Initial initsync version 0 (Not Reached)
BGP NSR/ISSU Sync-Group versions 0/0

BGP is operating in STANDALONE mode.


Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
Speaker               1          1          0          0           1           0

```

**Help:** execute the command "show bgp vrf all ipv4 unicast summary"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show bgp neighbors

**Output:**
```
Sun Nov 11 05:46:16.280 GMT

BGP neighbor is 192.168.100.1
 Remote AS 65001, local AS 65001, internal link
 Description: RouteReflector_1
 Remote router ID 192.168.100.1
  BGP state = Established, up for 2w3d
  NSR State: NSR Ready
  Last read 00:00:00, Last read before reset 2w3d
  Hold time is 90, keepalive interval is 30 seconds
  Configured hold time: 180, keepalive: 60, min acceptable hold time: 3
  Last write 00:00:24, attempted 19, written 19
  Second last write 00:00:54, attempted 19, written 19
  Last write before reset 2w3d, attempted 19, written 19
  Second last write before reset 2w3d, attempted 19, written 19
  Last write pulse rcvd  Nov 11 05:46:16.954 last full not set pulse count 6904115
  Last write pulse rcvd before reset 2w3d
  Socket not armed for io, armed for read, armed for write
  Last write thread event before reset 2w3d, second last 2w3d
  Last KA expiry before reset 2w3d, second last 2w3d
  Last KA error before reset 00:00:00, KA not sent 00:00:00
  Last KA start before reset 2w3d, second last 2w3d
  Precedence: internet
  Non-stop routing is enabled
  Multi-protocol capability received
  Neighbor capabilities:
    Route refresh: advertised (old + new) and received (old + new)
    4-byte AS: advertised and received
    Address family IPv4 Unicast: advertised and received
  Received 15716463 messages, 0 notifications, 0 in queue
  Sent 66285 messages, 0 notifications, 0 in queue
  Minimum time between advertisement runs is 0 secs

 For Address Family: IPv4 Unicast
  BGP neighbor version 56362493
  Update group: 0.4 Filter-group: 0.1  No Refresh request being processed
  NEXT_HOP is always this router
  Route refresh request: received 0, sent 0
  847583 accepted prefixes, 794705 are bestpaths
  Cumulative no. of prefixes denied: 0. 
  Prefix advertised 170, suppressed 0, withdrawn 19
  Maximum prefixes allowed 1048576
  Threshold for warning message 75%, restart interval 0 min
  AIGP is enabled
  An EoR was not received during read-only mode
  Last ack version 56362493, Last synced ack version 56362493
  Outstanding version objects: current 0, max 3
  Additional-paths operation: None

  Connections established 2; dropped 1
  Local host: 10.0.0.1, Local port: 179
  Foreign host: 192.168.100.1, Foreign port: 13617
  Last reset 2w3d, due to Peer closing down the session
  Peer reset reason: Remote closed the session (No error)

BGP neighbor is 192.168.100.2
 Remote AS 65001, local AS 65001, internal link
 Description: RouteReflector_2
 Remote router ID 192.168.100.2
  BGP state = Established, up for 2w3d
  NSR State: NSR Ready
  Last read 00:00:00, Last read before reset 2w3d
  Hold time is 90, keepalive interval is 30 seconds
  Configured hold time: 180, keepalive: 60, min acceptable hold time: 3
  Last write 00:00:24, attempted 19, written 19
  Second last write 00:00:54, attempted 19, written 19
  Last write before reset 2w3d, attempted 19, written 19
  Second last write before reset 2w3d, attempted 19, written 19
  Last write pulse rcvd  Nov 11 05:46:16.740 last full not set pulse count 6728170
  Last write pulse rcvd before reset 2w3d
  Socket not armed for io, armed for read, armed for write
  Last write thread event before reset 2w3d, second last 2w3d
  Last KA expiry before reset 2w3d, second last 2w3d
  Last KA error before reset 00:00:00, KA not sent 00:00:00
  Last KA start before reset 2w3d, second last 2w3d
  Precedence: internet
  Non-stop routing is enabled
  Multi-protocol capability received
  Neighbor capabilities:
    Route refresh: advertised (old + new) and received (old + new)
    4-byte AS: advertised and received
    Address family IPv4 Unicast: advertised and received
  Received 15922796 messages, 0 notifications, 0 in queue
  Sent 66281 messages, 0 notifications, 0 in queue
  Minimum time between advertisement runs is 0 secs

 For Address Family: IPv4 Unicast
  BGP neighbor version 56362493
  Update group: 0.4 Filter-group: 0.1  No Refresh request being processed
  NEXT_HOP is always this router
  Route refresh request: received 0, sent 0
  847585 accepted prefixes, 52523 are bestpaths
  Cumulative no. of prefixes denied: 0. 
  Prefix advertised 170, suppressed 0, withdrawn 19
  Maximum prefixes allowed 1048576
  Threshold for warning message 75%, restart interval 0 min
  AIGP is enabled
  An EoR was not received during read-only mode
  Last ack version 56362493, Last synced ack version 56362493
  Outstanding version objects: current 0, max 3
  Additional-paths operation: None

  Connections established 2; dropped 1
  Local host: 10.0.0.1, Local port: 179
  Foreign host: 192.168.100.2, Foreign port: 15445
  Last reset 2w3d, due to Peer closing down the session
  Peer reset reason: Remote closed the session (No error)
 
BGP neighbor is 192.168.0.1
 Remote AS 65001, local AS 65001, internal link
 Description: VPN_RouteReflector_1
 Remote router ID 192.168.0.1
  BGP state = Established, up for 2w4d
  NSR State: NSR Ready
  Last read 00:00:00, Last read before reset 2w4d
  Hold time is 90, keepalive interval is 30 seconds
  Configured hold time: 180, keepalive: 60, min acceptable hold time: 3
  Last write 00:00:25, attempted 19, written 19
  Second last write 00:00:55, attempted 19, written 19
  Last write before reset 2w4d, attempted 19, written 19
  Second last write before reset 2w4d, attempted 19, written 19
  Last write pulse rcvd  Nov 11 05:46:17.108 last full not set pulse count 11339768
  Last write pulse rcvd before reset 2w4d
  Socket not armed for io, armed for read, armed for write
  Last write thread event before reset 2w4d, second last 2w4d
  Last KA expiry before reset 2w4d, second last 2w4d
  Last KA error before reset 00:00:00, KA not sent 00:00:00
  Last KA start before reset 2w4d, second last 2w4d
  Precedence: internet
  Non-stop routing is enabled
  Multi-protocol capability received
  Neighbor capabilities:
    Route refresh: advertised (old + new) and received (old + new)
    4-byte AS: advertised and received
    Address family VPNv4 Unicast: advertised and received
    Address family VPNv6 Unicast: advertised and received
    Address family IPv4 MDT: advertised and received
  Received 44909621 messages, 2 notifications, 0 in queue
  Sent 66491 messages, 1 notifications, 0 in queue
  Minimum time between advertisement runs is 0 secs

 For Address Family: VPNv4 Unicast
  BGP neighbor version 1735091
  Update group: 0.2 Filter-group: 0.1  No Refresh request being processed
  Route refresh request: received 0, sent 0
  4713 accepted prefixes, 4443 are bestpaths
  Cumulative no. of prefixes denied: 387634. 
    No policy: 0, Failed RT match: 146231116
    By ORF policy: 0, By policy: 0
  Prefix advertised 889, suppressed 0, withdrawn 6
  Maximum prefixes allowed 2097152
  Threshold for warning message 75%, restart interval 0 min
  AIGP is enabled
  An EoR was not received during read-only mode
  Last ack version 1735091, Last synced ack version 1735091
  Outstanding version objects: current 0, max 5
  Additional-paths operation: None

 For Address Family: VPNv6 Unicast
  BGP neighbor version 1
  Update group: 0.2 Filter-group: 0.1  No Refresh request being processed
  Route refresh request: received 0, sent 0
  0 accepted prefixes, 0 are bestpaths
  Cumulative no. of prefixes denied: 0. 
  Prefix advertised 0, suppressed 0, withdrawn 0
  Maximum prefixes allowed 1048576
  Threshold for warning message 75%, restart interval 0 min
  AIGP is enabled
  An EoR was not received during read-only mode
  Last ack version 1, Last synced ack version 1
  Outstanding version objects: current 0, max 0
  Additional-paths operation: None

 For Address Family: IPv4 MDT
  BGP neighbor version 77
  Update group: 0.2 Filter-group: 0.2  No Refresh request being processed
  Route refresh request: received 0, sent 0
  0 accepted prefixes, 0 are bestpaths
  Cumulative no. of prefixes denied: 0. 
  Prefix advertised 0, suppressed 0, withdrawn 0
  Maximum prefixes allowed 131072
  Threshold for warning message 75%, restart interval 0 min
  AIGP is enabled
  An EoR was not received during read-only mode
  Last ack version 77, Last synced ack version 77
  Outstanding version objects: current 0, max 0
  Additional-paths operation: None

  Connections established 3; dropped 2
  Local host: 10.0.0.1, Local port: 45510
  Foreign host: 192.168.0.1, Foreign port: 179
  Last reset 2w4d, due to BGP Notification received: peer unconfigured
  Time since last notification sent to neighbor: 3w2d
  Error Code: peer in wrong AS
  Notification data sent:
    00001B47
  Time since last notification received from neighbor: 2w4d
  Error Code: peer unconfigured
  Notification data received:
    None

BGP neighbor is 192.168.0.2
 Remote AS 65001, local AS 65001, internal link
 Description: VPN_RouteReflector_2
 Remote router ID 192.168.0.2
  BGP state = Established, up for 3w2d
  NSR State: NSR Ready
  Last read 00:00:00, Last read before reset 00:00:00
  Hold time is 90, keepalive interval is 30 seconds
  Configured hold time: 180, keepalive: 60, min acceptable hold time: 3
  Last write 00:00:25, attempted 19, written 19
  Second last write 00:00:55, attempted 19, written 19
  Last write before reset 00:00:00, attempted 0, written 0
  Second last write before reset 00:00:00, attempted 0, written 0
  Last write pulse rcvd  Nov 11 05:46:16.890 last full not set pulse count 21237051
  Last write pulse rcvd before reset 00:00:00
  Socket not armed for io, armed for read, armed for write
  Last write thread event before reset 00:00:00, second last 00:00:00
  Last KA expiry before reset 00:00:00, second last 00:00:00
  Last KA error before reset 00:00:00, KA not sent 00:00:00
  Last KA start before reset 00:00:00, second last 00:00:00
  Precedence: internet
  Non-stop routing is enabled
  Multi-protocol capability received
  Neighbor capabilities:
    Route refresh: advertised (old + new) and received (old + new)
    4-byte AS: advertised and received
    Address family VPNv4 Unicast: advertised and received
    Address family VPNv6 Unicast: advertised and received
    Address family IPv4 MDT: advertised and received
  Received 45322792 messages, 0 notifications, 0 in queue
  Sent 66498 messages, 1 notifications, 0 in queue
  Minimum time between advertisement runs is 0 secs

 For Address Family: VPNv4 Unicast
  BGP neighbor version 1735091
  Update group: 0.2 Filter-group: 0.1  No Refresh request being processed
  Route refresh request: received 0, sent 0
  4710 accepted prefixes, 66 are bestpaths
  Cumulative no. of prefixes denied: 500233. 
    No policy: 0, Failed RT match: 185868387
    By ORF policy: 0, By policy: 0
  Prefix advertised 5803, suppressed 0, withdrawn 9
  Maximum prefixes allowed 2097152
  Threshold for warning message 75%, restart interval 0 min
  AIGP is enabled
  An EoR was not received during read-only mode
  Last ack version 1735091, Last synced ack version 1735091
  Outstanding version objects: current 0, max 5
  Additional-paths operation: None

 For Address Family: VPNv6 Unicast
  BGP neighbor version 1
  Update group: 0.2 Filter-group: 0.1  No Refresh request being processed
  Route refresh request: received 0, sent 0
  0 accepted prefixes, 0 are bestpaths
  Cumulative no. of prefixes denied: 0. 
  Prefix advertised 0, suppressed 0, withdrawn 0
  Maximum prefixes allowed 1048576
  Threshold for warning message 75%, restart interval 0 min
  AIGP is enabled
  An EoR was not received during read-only mode
  Last ack version 1, Last synced ack version 1
  Outstanding version objects: current 0, max 0
  Additional-paths operation: None

 For Address Family: IPv4 MDT
  BGP neighbor version 77
  Update group: 0.2 Filter-group: 0.2  No Refresh request being processed
  Route refresh request: received 0, sent 0
  0 accepted prefixes, 0 are bestpaths
  Cumulative no. of prefixes denied: 0. 
  Prefix advertised 0, suppressed 0, withdrawn 0
  Maximum prefixes allowed 131072
  Threshold for warning message 75%, restart interval 0 min
  AIGP is enabled
  An EoR was not received during read-only mode
  Last ack version 77, Last synced ack version 77
  Outstanding version objects: current 0, max 0
  Additional-paths operation: None

  Connections established 1; dropped 0
  Local host: 10.0.0.1, Local port: 35134
  Foreign host: 192.168.0.2, Foreign port: 179
  Last reset 3w2d, due to BGP Notification sent: peer in wrong AS
  Time since last notification sent to neighbor: 3w2d
  Error Code: peer in wrong AS
  Notification data sent:
    00001B47

 BGP neighbor is 10.0.0.42
 Remote AS 65001, local AS 65001, internal link
 Description: iBGP_Neighbor
 Remote router ID 0.0.0.0
 Cluster ID 10.0.0.1
  BGP state = OpenSent
  NSR State: None
  Last read 00:00:00, Last read before reset 2w3d
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time: 180, keepalive: 60, min acceptable hold time: 3
  Last write 00:00:34, attempted 61, written 61
  Second last write 00:02:10, attempted 61, written 61
  Last write before reset 2w3d, attempted 25102, written 0
  Second last write before reset 2w3d, attempted 25102, written 0
  Last write pulse rcvd  Nov 11 05:45:42.941 last full Oct 24 12:47:49.569 pulse count 2351991
  Last write pulse rcvd before reset 2w3d
  Socket not armed for io, armed for read, armed for write
  Last write thread event before reset 2w3d, second last 2w3d
  Last KA expiry before reset 2w3d, second last 00:00:00
  Last KA error before reset 00:00:00, KA not sent 00:00:00
  Last KA start before reset 2w3d, second last 2w3d
  Precedence: internet
  Non-stop routing is enabled
  Multi-protocol capability received
  Received 7580 messages, 0 notifications, 0 in queue
  Sent 4595111 messages, 2 notifications, 0 in queue
  Minimum time between advertisement runs is 0 secs

 For Address Family: IPv4 Unicast
  BGP neighbor version 0
  Update group: 0.1 Filter-group: 0.0  No Refresh request being processed
  Route-Reflector Client
  Route refresh request: received 0, sent 0
  Policy for incoming advertisements is DENY-ALL
  Policy for outgoing advertisements is PASS-ALL
  0 accepted prefixes, 0 are bestpaths
  Cumulative no. of prefixes denied: 0. 
  Prefix advertised 0, suppressed 0, withdrawn 0
  Maximum prefixes allowed 1048576
  Threshold for warning message 75%, restart interval 0 min
  AIGP is enabled
  An EoR was not received during read-only mode
  Last ack version 0, Last synced ack version 0
  Outstanding version objects: current 0, max 178
  Additional-paths operation: None

 For Address Family: IPv6 Unicast
  BGP neighbor version 0
  Update group: 0.1 Filter-group: 0.0  No Refresh request being processed
  Route-Reflector Client
  Route refresh request: received 0, sent 0
  Policy for incoming advertisements is DENY-ALL
  Policy for outgoing advertisements is PASS-ALL
  0 accepted prefixes, 0 are bestpaths
  Cumulative no. of prefixes denied: 0. 
  Prefix advertised 0, suppressed 0, withdrawn 0
  Maximum prefixes allowed 524288
  Threshold for warning message 75%, restart interval 0 min
  AIGP is enabled
  An EoR was not received during read-only mode
  Last ack version 0, Last synced ack version 0
  Outstanding version objects: current 0, max 175
  Additional-paths operation: None

  Connections established 1; dropped 1
  Local host: 10.0.0.1, Local port: 59248
  Foreign host: 10.0.0.42, Foreign port: 179
  Last reset 00:00:52, due to Peer closing down the session
  Peer reset reason: Remote closed the session (Connection timed out)
  Time since last notification sent to neighbor: 2w3d
  Error Code: hold time expired
  Notification data sent:
    None

BGP neighbor is 10.0.0.124
 Remote AS 65012, local AS 65001, external link
 Remote router ID 10.1.2.3
  BGP state = Established, up for 3w1d
  NSR State: NSR Ready
  Last read 00:00:48, Last read before reset 00:00:00
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time: 180, keepalive: 60, min acceptable hold time: 3
  Last write 00:00:27, attempted 19, written 19
  Second last write 00:01:27, attempted 19, written 19
  Last write before reset 00:00:00, attempted 0, written 0
  Second last write before reset 00:00:00, attempted 0, written 0
  Last write pulse rcvd  Nov 11 05:45:50.059 last full not set pulse count 67869
  Last write pulse rcvd before reset 00:00:00
  Socket not armed for io, armed for read, armed for write
  Last write thread event before reset 00:00:00, second last 00:00:00
  Last KA expiry before reset 00:00:00, second last 00:00:00
  Last KA error before reset 00:00:00, KA not sent 00:00:00
  Last KA start before reset 00:00:00, second last 00:00:00
  Precedence: internet
  Non-stop routing is enabled
  Enforcing first AS is enabled
  Multi-protocol capability received
  Neighbor capabilities:
    Route refresh: advertised (old + new) and received (old + new)
    4-byte AS: advertised and received
    Address family IPv4 Unicast: advertised and received
  Received 34482 messages, 0 notifications, 0 in queue
  Sent 33035 messages, 0 notifications, 0 in queue
  Minimum time between advertisement runs is 30 secs

 For Address Family: IPv4 Unicast
  BGP neighbor version 56362493
  Update group: 0.3 Filter-group: 0.3  No Refresh request being processed
  Route refresh request: received 0, sent 0
  Policy for incoming advertisements is eBGP-IN
  Policy for outgoing advertisements is DENY-ALL
  5836 accepted prefixes, 5836 are bestpaths
  Cumulative no. of prefixes denied: 0. 
  Prefix advertised 0, suppressed 0, withdrawn 0
  Maximum prefixes allowed 1048576
  Threshold for warning message 75%, restart interval 0 min
  An EoR was not received during read-only mode
  Last ack version 56362493, Last synced ack version 56362493
  Outstanding version objects: current 0, max 0
  Additional-paths operation: None

  Connections established 1; dropped 0
  Local host: 10.0.0.1, Local port: 37554
  Foreign host: 10.0.0.124, Foreign port: 179
  Last reset 3w1d, due to User clear requested (CEASE notification sent - administrative reset)
  Time since last notification sent to neighbor: 3w1d
  Error Code: administrative reset
  Notification data sent:
    None
  External BGP neighbor may be up to 20 hops away.

BGP neighbor is 1:1:1::1
 Remote AS 65001, local AS 65001, internal link
 Description: rs01.lsan01-ca
 Remote router ID 192.168.100.1
  BGP state = Established, up for 2w3d
  NSR State: NSR Ready
  Last read 00:00:06, Last read before reset 2w3d
  Hold time is 90, keepalive interval is 30 seconds
  Configured hold time: 180, keepalive: 60, min acceptable hold time: 3
  Last write 00:00:09, attempted 19, written 19
  Second last write 00:00:39, attempted 19, written 19
  Last write before reset 2w3d, attempted 19, written 19
  Second last write before reset 2w3d, attempted 19, written 19
  Last write pulse rcvd  Nov 11 05:46:10.750 last full not set pulse count 2477012
  Last write pulse rcvd before reset 2w3d
  Socket not armed for io, armed for read, armed for write
  Last write thread event before reset 2w3d, second last 2w3d
  Last KA expiry before reset 2w3d, second last 2w3d
  Last KA error before reset 00:00:00, KA not sent 00:00:00
  Last KA start before reset 2w3d, second last 2w3d
  Precedence: internet
  Non-stop routing is enabled
  Multi-protocol capability received
  Neighbor capabilities:
    Route refresh: advertised (old + new) and received (old + new)
    4-byte AS: advertised and received
    Address family IPv6 Unicast: advertised and received
  Received 3931360 messages, 0 notifications, 0 in queue
  Sent 66256 messages, 0 notifications, 0 in queue
  Minimum time between advertisement runs is 0 secs

 For Address Family: IPv6 Unicast
  BGP neighbor version 18781601
  Update group: 0.3 Filter-group: 0.1  No Refresh request being processed
  NEXT_HOP is always this router
  Route refresh request: received 0, sent 0
  59216 accepted prefixes, 35229 are bestpaths
  Cumulative no. of prefixes denied: 0. 
  Prefix advertised 1, suppressed 0, withdrawn 0
  Maximum prefixes allowed 524288
  Threshold for warning message 75%, restart interval 0 min
  AIGP is enabled
  An EoR was not received during read-only mode
  Last ack version 18781601, Last synced ack version 18781601
  Outstanding version objects: current 0, max 1
  Additional-paths operation: None

  Connections established 2; dropped 1
  Local host: 100::42, Local port: 179
  Foreign host: 1:1:1::1, Foreign port: 13730
  Last reset 2w3d, due to Peer closing down the session
  Peer reset reason: Remote closed the session (No error)
 
BGP neighbor is 1:1:34::242
 Remote AS 65001, local AS 65001, internal link
 Description: RouteReflector_2
 Remote router ID 192.168.100.2
  BGP state = Established, up for 2w3d
  NSR State: NSR Ready
  Last read 00:00:06, Last read before reset 2w3d
  Hold time is 90, keepalive interval is 30 seconds
  Configured hold time: 180, keepalive: 60, min acceptable hold time: 3
  Last write 00:00:11, attempted 19, written 19
  Second last write 00:00:41, attempted 19, written 19
  Last write before reset 2w3d, attempted 19, written 19
  Second last write before reset 2w3d, attempted 19, written 19
  Last write pulse rcvd  Nov 11 05:46:10.703 last full not set pulse count 2515631
  Last write pulse rcvd before reset 2w3d
  Socket not armed for io, armed for read, armed for write
  Last write thread event before reset 2w3d, second last 2w3d
  Last KA expiry before reset 2w3d, second last 2w3d
  Last KA error before reset 00:00:00, KA not sent 00:00:00
  Last KA start before reset 2w3d, second last 2w3d
  Precedence: internet
  Non-stop routing is enabled
  Multi-protocol capability received
  Neighbor capabilities:
    Route refresh: advertised (old + new) and received (old + new)
    4-byte AS: advertised and received
    Address family IPv6 Unicast: advertised and received
  Received 3944185 messages, 0 notifications, 0 in queue
  Sent 66258 messages, 0 notifications, 0 in queue
  Minimum time between advertisement runs is 0 secs

 For Address Family: IPv6 Unicast
  BGP neighbor version 18781601
  Update group: 0.3 Filter-group: 0.1  No Refresh request being processed
  NEXT_HOP is always this router
  Route refresh request: received 0, sent 0
  59216 accepted prefixes, 23987 are bestpaths
  Cumulative no. of prefixes denied: 0. 
  Prefix advertised 1, suppressed 0, withdrawn 0
  Maximum prefixes allowed 524288
  Threshold for warning message 75%, restart interval 0 min
  AIGP is enabled
  An EoR was not received during read-only mode
  Last ack version 18781601, Last synced ack version 18781601
  Outstanding version objects: current 0, max 1
  Additional-paths operation: None

  Connections established 2; dropped 1
  Local host: 100::42, Local port: 179
  Foreign host: 1:1:34::242, Foreign port: 44455
  Last reset 2w3d, due to Peer closing down the session
  Peer reset reason: Remote closed the session (No error)

```

**Help:** execute the command "show bgp neighbors"

**Prompt:**
- cisco_xr>
- cisco_xr#

### admin show inventory

**Output:**
```
Name: Rack 0 Descr: ASR-9010 Chassis
PID: ASR-9010 VID: V01 SN: FOX0000X0XX
 
Name: 0/0 Descr: 24X10G/1G Service Edge Optimized LC
PID: A9K-24X10GE-1G-SE VID: V05 SN: FOC0000XXXX

Name: 0/7 Descr: ASR 9000 8-port 100GE FLEXE SE linecard
PID: A9K-8HG-FLEX-SE VID: V02 SN: FOC0000XXXX

```

**Help:** execute the command "admin show inventory"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show controllers fabric fia errors egress location

**Output:**
```
********** FIA-0 **********
Category: eg_error-0
                             To Spaui Error-0                        1
                             To Spaui Error-1                       22
                       RL over/under flow cnt                       33

 ********** FIA-1 **********
 Category: eg_error-1
                             To Spaui Error-0                     9999
                             To Spaui Error-1                   123333
                       RL over/under flow cnt                        1

 ********** FIA-2 **********
Category: eg_error-2
                             To Spaui Error-0                        0
                             To Spaui Error-1                        0
                       RL over/under flow cnt                        0

 ********** FIA-3 **********
Category: eg_error-3
                             To Spaui Error-0                        0
                             To Spaui Error-1                        0
                       RL over/under flow cnt                        0

```

**Help:** execute the command "show controllers fabric fia errors egress location"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show drops np all

**Output:**
```
Node: 0/0/CPU0:
----------------------------------------------------------------
 
NP 0 Drops:
----------------------------------------------------------------
RSV_DROP_ING_BFD                                             3               
RSV_DROP_MPLS_TXADJ_NO_MATCH                                 148             
RSV_DROP_MPLS_LEAF_NO_MATCH                                  34              
MODIFY_PUNT_REASON_MISS_DROP                                 2               
PARSE_EGR_INJ_PKT_TYP_UNKNOWN                                4329            
PARSE_DROP_IN_UIDB_TCAM_MISS                                 388             
PARSE_DROP_IN_UIDB_DOWN                                      14              
PARSE_DROP_IPV4_DISABLED                                     106             
----------------------------------------------------------------
 
NP 1 Drops:
----------------------------------------------------------------
RSV_DROP_IPV4_NRLDI_NOT_LOCAL                                3472            
MODIFY_PUNT_REASON_MISS_DROP                                 2               
PARSE_DROP_IN_UIDB_TCAM_MISS                                 384             
----------------------------------------------------------------
 
NP 2 Drops:
----------------------------------------------------------------
MODIFY_PUNT_REASON_MISS_DROP                                 2               
----------------------------------------------------------------

NP 3 Drops:
----------------------------------------------------------------
MODIFY_PUNT_REASON_MISS_DROP                                 3               
----------------------------------------------------------------

NP 4 Drops:
----------------------------------------------------------------
MODIFY_PUNT_REASON_MISS_DROP                                 4               
----------------------------------------------------------------

NP 5 Drops:
----------------------------------------------------------------
MODIFY_PUNT_REASON_MISS_DROP                                 3               
----------------------------------------------------------------

NP 6 Drops:
----------------------------------------------------------------
MODIFY_PUNT_REASON_MISS_DROP                                 3               
----------------------------------------------------------------

NP 7 Drops:
----------------------------------------------------------------
MODIFY_PUNT_REASON_MISS_DROP                                 3               
----------------------------------------------------------------

		 Node: 0/7/CPU0:
----------------------------------------------------------------
 
NP 0 Drops:
----------------------------------------------------------------
RSV_DROP_ING_BFD                                             256             
RSV_DROP_EGR_UIDB_DOWN                                       1               
RSV_DROP_MPLS_TXADJ_NO_MATCH                                 36              
RSV_DROP_MPLS_LEAF_NO_MATCH                                  124             
RSV_DROP_NHINDEX                                             1               
MDF_RPF_FAIL_DROP                                            146019781       
MDF_PUNT_POLICE_DROP                                         362             
MODIFY_PUNT_REASON_MISS_DROP                                 3               
PUNT_NO_MATCH_EXCD                                           362             
DROP_FRM_FRM_ERR_XAUI6                                       1               
PARSE_DROP_IN_UIDB_DOWN                                      27              
PARSE_DROP_IPV4_DISABLED                                     163             
----------------------------------------------------------------
 
NP 1 Drops:
----------------------------------------------------------------
MODIFY_PUNT_REASON_MISS_DROP                                 4               
----------------------------------------------------------------

NP 2 Drops:
----------------------------------------------------------------
MODIFY_PUNT_REASON_MISS_DROP                                 3               
----------------------------------------------------------------

NP 3 Drops:
----------------------------------------------------------------
MODIFY_PUNT_REASON_MISS_DROP                                 4               
----------------------------------------------------------------

NP 4 Drops:
----------------------------------------------------------------
MODIFY_PUNT_REASON_MISS_DROP                                 3               
----------------------------------------------------------------

NP 5 Drops:
----------------------------------------------------------------
MODIFY_PUNT_REASON_MISS_DROP                                 3               
----------------------------------------------------------------

NP 6 Drops:
----------------------------------------------------------------
MODIFY_PUNT_REASON_MISS_DROP                                 4               
----------------------------------------------------------------

NP 7 Drops:
----------------------------------------------------------------
MODIFY_PUNT_REASON_MISS_DROP                                 4               
----------------------------------------------------------------

```

**Help:** execute the command "show drops np all"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show ospf vrf all neighbor

**Output:**
```

Wed Jul 27 17:18:33.921 CST

* Indicates MADJ interface
# Indicates Neighbor awaiting BFD session up

Neighbors for OSPF 1, VRF red

Neighbor ID     Pri   State           Dead Time   Address         Interface
192.0.2.1       0     FULL/  -        00:00:39    192.0.2.2       Bundle-Ether10.10
    Neighbor is up for 5w0d
192.0.2.3       1     FULL/DR         00:00:39    192.0.2.4       TenGigE0/0/0/10.10
    Neighbor is up for 35w1d

Total neighbor count: 2


* Indicates MADJ interface
# Indicates Neighbor awaiting BFD session up

Neighbors for OSPF 1, VRF green

Neighbor ID     Pri   State           Dead Time   Address         Interface
192.0.2.5       0     FULL/  -        00:00:34    192.0.2.6       Bundle-Ether10.20
    Neighbor is up for 6d16h
192.0.2.7       1     FULL/DR         00:00:38    192.0.2.8       TenGigE0/0/0/10.20
    Neighbor is up for 35w1d

Total neighbor count: 2


* Indicates MADJ interface
# Indicates Neighbor awaiting BFD session up

Neighbors for OSPF 1, VRF blue

Neighbor ID     Pri   State           Dead Time   Address         Interface
192.0.2.9       1     FULL/BDR        00:00:39    192.0.2.10      Bundle-Ether10.30
    Neighbor is up for 35w1d
192.0.2.11      1     FULL/BDR        00:00:39    192.0.2.12      GigabitEthernet100/0/0/0
    Neighbor is up for 35w1d

Total neighbor count: 2

```

**Help:** execute the command "show ospf vrf all neighbor"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show hsrp

**Output:**
```
Fri May 17 20:29:32.108 UTC

IPv4 Groups:

                       P indicates configured to preempt.

                       |

Interface     Grp Pri P State   Active addr     Standby addr   Group addr

Gi0/0/0/1         1 110 P Active local           10.1.1.3       10.1.1.1

IPv6 Groups:

                       P indicates configured to preempt.

                       |

Interface     Grp Pri P State   Active addr     Standby addr   Group addr

```

**Help:** execute the command "show hsrp"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show controllers hundredgige all

**Output:**
```
Operational data for interface HundredGigE0/0/0/0:

State:
    Administrative state: enabled
    Operational state: Up
    LED state: Green On

Phy:
    Media type: MMF fiber over 10 lane optics (short reach)
    Optics:
        Vendor: CISCO           
        Part number: 800-41495-01    
        Serial number: FBN19122017

MAC address information:
    Operational address: 54a2.741c.3b29
    Burnt-in address: 54a2.741c.3b29
    No unicast addresses in filter
    Operating in multicast promiscuous mode

Autonegotiation disabled.

Operational values:
    Speed: 100Gbps
    Duplex: Full Duplex
    Flowcontrol: None
    Loopback: None (or external)
    MTU: 9216
    MRU: 9216
    Inter-packet gap: standard (12)
    BER monitoring:
        Signal Degrade: 10e-6 (no-alarm)
        Signal Fail: 10e-4 (report-alarm)
 

Operational data for interface HundredGigE0/0/0/1:

State:
    Administrative state: enabled
    Operational state: Up
    LED state: Green On

Phy:
    Media type: MMF fiber over 10 lane optics (short reach)
    Optics:
        Vendor: CISCO           
        Part number: 800-41495-01    
        Serial number: FBN19092109

MAC address information:
    Operational address: 54a2.741c.3b2a
    Burnt-in address: 54a2.741c.3b2a
    No unicast addresses in filter
    Operating in multicast promiscuous mode

Autonegotiation disabled.

Operational values:
    Speed: 100Gbps
    Duplex: Full Duplex
    Flowcontrol: None
    Loopback: None (or external)
    MTU: 9216
    MRU: 9216
    Inter-packet gap: standard (12)
    BER monitoring:
        Signal Degrade: 10e-6 (no-alarm)
        Signal Fail: 10e-4 (report-alarm)
 

Operational data for interface HundredGigE0/0/0/2:

State:
    Administrative state: enabled
    Operational state: Up
    LED state: Green On

Phy:
    Media type: MMF fiber over 10 lane optics (short reach)
    Optics:
        Vendor: CISCO           
        Part number: 800-41495-01    
        Serial number: FBN19122019

MAC address information:
    Operational address: 54a2.741c.3b2b
    Burnt-in address: 54a2.741c.3b2b
    No unicast addresses in filter
    Operating in multicast promiscuous mode

Autonegotiation disabled.

Operational values:
    Speed: 100Gbps
    Duplex: Full Duplex
    Flowcontrol: None
    Loopback: None (or external)
    MTU: 9216
    MRU: 9216
    Inter-packet gap: standard (12)
    BER monitoring:
        Signal Degrade: 10e-6 (no-alarm)
        Signal Fail: 10e-4 (report-alarm)
 

Operational data for interface HundredGigE0/0/0/3:

State:
    Administrative state: disabled
    Operational state: Down (Reason: Link loss or low light, no loopback)
    LED state: Yellow On

Phy:
    Media type: MMF fiber over 10 lane optics (short reach)
    Optics:
        Vendor: CISCO           
        Part number: 800-41495-01    
        Serial number: FBN19122030
 
MAC address information:
    Operational address: 54a2.741c.3b2c
    Burnt-in address: 54a2.741c.3b2c
    No unicast addresses in filter
    Operating in multicast promiscuous mode

Autonegotiation disabled.

Operational values:
    Speed: 100Gbps
    Duplex: Full Duplex
    Flowcontrol: None
    Loopback: None (or external)
    MTU: 1514
    MRU: 1514
    Inter-packet gap: standard (12)
    BER monitoring:
        Signal Degrade: 10e-6 (no-alarm)
        Signal Fail: 10e-4 (report-alarm)


Operational data for interface HundredGigE0/4/0/0:

State:
    Administrative state: enabled
    Operational state: Up
    LED state: Green On

Phy:
    Media type: MMF fiber over 10 lane optics (short reach)
    Optics:
        Vendor: CISCO           
        Part number: 800-41495-01    
        Serial number: FBN19092110

MAC address information:
    Operational address: 54a2.741c.3c5d
    Burnt-in address: 54a2.741c.3c5d
    No unicast addresses in filter
    Operating in multicast promiscuous mode

Autonegotiation disabled.

Operational values:
    Speed: 100Gbps
    Duplex: Full Duplex
    Flowcontrol: None
    Loopback: None (or external)
    MTU: 9216
    MRU: 9216
    Inter-packet gap: standard (12)
    BER monitoring:
        Signal Degrade: 10e-6 (no-alarm)
        Signal Fail: 10e-4 (report-alarm)


Operational data for interface HundredGigE0/4/0/1:

State:
    Administrative state: enabled
    Operational state: Up
    LED state: Green On

Phy:
    Media type: MMF fiber over 10 lane optics (short reach)
    Optics:
        Vendor: CISCO           
        Part number: 800-41495-01    
        Serial number: FBN19092111

MAC address information:
    Operational address: 54a2.741c.3c5e
    Burnt-in address: 54a2.741c.3c5e
    No unicast addresses in filter
    Operating in multicast promiscuous mode

Autonegotiation disabled.

Operational values:
    Speed: 100Gbps
    Duplex: Full Duplex
    Flowcontrol: None
    Loopback: None (or external)
    MTU: 9216
    MRU: 9216
    Inter-packet gap: standard (12)
    BER monitoring:
        Signal Degrade: 10e-6 (no-alarm)
        Signal Fail: 10e-4 (report-alarm)


Operational data for interface HundredGigE0/4/0/2:

State:
    Administrative state: enabled
    Operational state: Up
    LED state: Green On

Phy:
    Media type: MMF fiber over 10 lane optics (short reach)
    Optics:
        Vendor: CISCO           
        Part number: 800-41495-01    
        Serial number: FBN19122025

MAC address information:
    Operational address: 54a2.741c.3c5f
    Burnt-in address: 54a2.741c.3c5f
    No unicast addresses in filter
    Operating in multicast promiscuous mode

Autonegotiation disabled.

Operational values:
    Speed: 100Gbps
    Duplex: Full Duplex
    Flowcontrol: None
    Loopback: None (or external)
    MTU: 9216
    MRU: 9216
    Inter-packet gap: standard (12)
    BER monitoring:
        Signal Degrade: 10e-6 (no-alarm)
        Signal Fail: 10e-4 (report-alarm)


Operational data for interface HundredGigE0/4/0/3:

State:
    Administrative state: disabled
    Operational state: Down (Reason: Link loss or low light, no loopback)
    LED state: Yellow On

Phy:
    Media type: MMF fiber over 10 lane optics (short reach)
    Optics:
        Vendor: CISCO           
        Part number: 800-41495-01    
        Serial number: FBN19122022

MAC address information:
    Operational address: 54a2.741c.3c60
    Burnt-in address: 54a2.741c.3c60
    No unicast addresses in filter
    Operating in multicast promiscuous mode

Autonegotiation disabled.

Operational values:
    Speed: 100Gbps
    Duplex: Full Duplex
    Flowcontrol: None
    Loopback: None (or external)
    MTU: 1514
    MRU: 1514
    Inter-packet gap: standard (12)
    BER monitoring:
        Signal Degrade: 10e-6 (no-alarm)
        Signal Fail: 10e-4 (report-alarm)
 

Management information for interface HundredGigE0/0/0/0:

Port number: 0
Bay number: 0
Interface handle: 0x10800a0

Config:
    Auto-negotiation: Configuration not supported (Off)
    Carrier delay (up): 9000 ms
    Carrier delay (down): 50 ms
    Speed: Configuration not supported (100Gbps)
    Duplex: Configuration not supported (Full Duplex)
    Flow Control: Not configured (None)
    IPG: Configuration not supported (standard (12))
    Loopback: Not configured (None)
    MTU: 9216 bytes
    Bandwidth: Not configured
    BER-SD Threshold: Not configured (10e-6)
    BER-SD Report: Not configured (Disabled)
    BER-SF Threshold: Not configured (10e-4)
    BER-SF Report: Not configured (Enabled)
    BER-SF Signal Remote Failure: Not configured (Disabled)
 
Driver constraints:
    Min MTU: 64 bytes
    Max MTU: 9600 bytes
    Max speed: 100Gbps
    Interface type: HundredGigE
    Management interface: No
    Promiscuous mode: Yes
    Default carrier delay up (auto-neg on): 0 ms
    Default carrier delay down (auto-neg on): 0 ms
    Default carrier delay up (auto-neg off): 0 ms
    Default carrier delay down (auto-neg off): 0 ms
    Allowed config mask: 0xe6b
    BER:
        SD (min - max): (10e-3 - 10e-12)
        SD default: 10e-6
        SF (min - max): (10e-4 - 10e-12)
        SF default: 10e-4

Cached driver state:
    MTU: 9216 bytes
    Burnt-in MAC address: 54a2.741c.3b29

Operational carrier delay:
    Carrier delay (up): 9000 ms
    Carrier delay (down): 50 ms

Not a member of a bundle interface.

Satellite uplink settings:
    Not in satellite uplink (ICL) mode.

Port FSM state:
    Port is enabled, link is up

Complete FSM state:
    Admin up
    Client admin up
    Client admin tx not disabled
    Port enabled
    Port tx enabled
    Hardware link up
IDB interface state information:
    IDB client admin up
    IDB client tx admin up
    IDB error disable not set

0 Unicast MAC Addresses:

0 Multicast MAC Addresses:


Management information for interface HundredGigE0/0/0/1:

Port number: 1
Bay number: 0
Interface handle: 0x10800c0

Config:
    Auto-negotiation: Configuration not supported (Off)
    Carrier delay (up): 9000 ms
    Carrier delay (down): 50 ms
    Speed: Configuration not supported (100Gbps)
    Duplex: Configuration not supported (Full Duplex)
    Flow Control: Not configured (None)
    IPG: Configuration not supported (standard (12))
    Loopback: Not configured (None)
    MTU: 9216 bytes
    Bandwidth: Not configured
    BER-SD Threshold: Not configured (10e-6)
    BER-SD Report: Not configured (Disabled)
    BER-SF Threshold: Not configured (10e-4)
    BER-SF Report: Not configured (Enabled)
    BER-SF Signal Remote Failure: Not configured (Disabled)

Driver constraints:
    Min MTU: 64 bytes
    Max MTU: 9600 bytes
    Max speed: 100Gbps
    Interface type: HundredGigE
    Management interface: No
    Promiscuous mode: Yes
    Default carrier delay up (auto-neg on): 0 ms
    Default carrier delay down (auto-neg on): 0 ms
    Default carrier delay up (auto-neg off): 0 ms
    Default carrier delay down (auto-neg off): 0 ms
    Allowed config mask: 0xe6b
    BER:
        SD (min - max): (10e-3 - 10e-12)
        SD default: 10e-6
        SF (min - max): (10e-4 - 10e-12)
        SF default: 10e-4

Cached driver state:
    MTU: 9216 bytes
    Burnt-in MAC address: 54a2.741c.3b2a

Operational carrier delay:
    Carrier delay (up): 9000 ms
    Carrier delay (down): 50 ms

Not a member of a bundle interface.

 Satellite uplink settings:
    Not in satellite uplink (ICL) mode.

Port FSM state:
    Port is enabled, link is up

Complete FSM state:
    Admin up
    Client admin up
    Client admin tx not disabled
    Port enabled
    Port tx enabled
    Hardware link up
IDB interface state information:
    IDB client admin up
    IDB client tx admin up
    IDB error disable not set

0 Unicast MAC Addresses:

0 Multicast MAC Addresses:


Management information for interface HundredGigE0/0/0/2:

Port number: 2
Bay number: 0
Interface handle: 0x10800e0

Config:
    Auto-negotiation: Configuration not supported (Off)
    Carrier delay (up): 9000 ms
    Carrier delay (down): 50 ms
    Speed: Configuration not supported (100Gbps)
    Duplex: Configuration not supported (Full Duplex)
    Flow Control: Not configured (None)
    IPG: Configuration not supported (standard (12))
    Loopback: Not configured (None)
    MTU: 9216 bytes
    Bandwidth: Not configured
    BER-SD Threshold: Not configured (10e-6)
    BER-SD Report: Not configured (Disabled)
    BER-SF Threshold: Not configured (10e-4)
    BER-SF Report: Not configured (Enabled)
    BER-SF Signal Remote Failure: Not configured (Disabled)

Driver constraints:
    Min MTU: 64 bytes
    Max MTU: 9600 bytes
    Max speed: 100Gbps
    Interface type: HundredGigE
    Management interface: No
    Promiscuous mode: Yes
    Default carrier delay up (auto-neg on): 0 ms
    Default carrier delay down (auto-neg on): 0 ms
    Default carrier delay up (auto-neg off): 0 ms
    Default carrier delay down (auto-neg off): 0 ms
    Allowed config mask: 0xe6b
    BER:
        SD (min - max): (10e-3 - 10e-12)
        SD default: 10e-6
        SF (min - max): (10e-4 - 10e-12)
        SF default: 10e-4

Cached driver state:
    MTU: 9216 bytes
    Burnt-in MAC address: 54a2.741c.3b2b

Operational carrier delay:
    Carrier delay (up): 9000 ms
    Carrier delay (down): 50 ms

Not a member of a bundle interface.

 Satellite uplink settings:
    Not in satellite uplink (ICL) mode.

Port FSM state:
    Port is enabled, link is up

Complete FSM state:
    Admin up
    Client admin up
    Client admin tx not disabled
    Port enabled
    Port tx enabled
    Hardware link up
IDB interface state information:
    IDB client admin up
    IDB client tx admin up
    IDB error disable not set

0 Unicast MAC Addresses:

0 Multicast MAC Addresses:


Management information for interface HundredGigE0/0/0/3:

Port number: 3
Bay number: 0
Interface handle: 0x1080100

Config:
    Auto-negotiation: Configuration not supported (Off)
    Carrier delay (up): Not configured
    Carrier delay (down): Not configured
    Speed: Configuration not supported (100Gbps)
    Duplex: Configuration not supported (Full Duplex)
    Flow Control: Not configured (None)
    IPG: Configuration not supported (standard (12))
    Loopback: Not configured (None)
    MTU: Not configured
    Bandwidth: Not configured
    BER-SD Threshold: Not configured (10e-6)
    BER-SD Report: Not configured (Disabled)
    BER-SF Threshold: Not configured (10e-4)
    BER-SF Report: Not configured (Enabled)
    BER-SF Signal Remote Failure: Not configured (Disabled)

Driver constraints:
    Min MTU: 64 bytes
    Max MTU: 9600 bytes
    Max speed: 100Gbps
    Interface type: HundredGigE
    Management interface: No
    Promiscuous mode: Yes
    Default carrier delay up (auto-neg on): 0 ms
    Default carrier delay down (auto-neg on): 0 ms
    Default carrier delay up (auto-neg off): 0 ms
    Default carrier delay down (auto-neg off): 0 ms
    Allowed config mask: 0xe6b
    BER:
        SD (min - max): (10e-3 - 10e-12)
        SD default: 10e-6
        SF (min - max): (10e-4 - 10e-12)
        SF default: 10e-4

Cached driver state:
    MTU: 1514 bytes
    Burnt-in MAC address: 54a2.741c.3b2c

Operational carrier delay:
    Carrier delay (up): 0 ms
    Carrier delay (down): 0 ms
 
Not a member of a bundle interface.

Satellite uplink settings:
    Not in satellite uplink (ICL) mode.

Port FSM state:
    Port is disabled, due to an admin down condition.

Complete FSM state:
    Admin down
    Client admin up
    Client admin tx not disabled
    Port disabled
    Port tx disabled
    Hardware link down
IDB interface state information:
    IDB client admin up
    IDB client tx admin up
    IDB error disable not set

0 Unicast MAC Addresses:

0 Multicast MAC Addresses:


Management information for interface HundredGigE0/4/0/0:

Port number: 0
Bay number: 0
Interface handle: 0x14800a0

Config:
    Auto-negotiation: Configuration not supported (Off)
    Carrier delay (up): 9000 ms
    Carrier delay (down): 50 ms
    Speed: Configuration not supported (100Gbps)
    Duplex: Configuration not supported (Full Duplex)
    Flow Control: Not configured (None)
    IPG: Configuration not supported (standard (12))
    Loopback: Not configured (None)
    MTU: 9216 bytes
    Bandwidth: Not configured
    BER-SD Threshold: Not configured (10e-6)
    BER-SD Report: Not configured (Disabled)
    BER-SF Threshold: Not configured (10e-4)
    BER-SF Report: Not configured (Enabled)
    BER-SF Signal Remote Failure: Not configured (Disabled)

Driver constraints:
    Min MTU: 64 bytes
    Max MTU: 9600 bytes
    Max speed: 100Gbps
    Interface type: HundredGigE
    Management interface: No
    Promiscuous mode: Yes
    Default carrier delay up (auto-neg on): 0 ms
    Default carrier delay down (auto-neg on): 0 ms
    Default carrier delay up (auto-neg off): 0 ms
    Default carrier delay down (auto-neg off): 0 ms
    Allowed config mask: 0xe6b
    BER:
        SD (min - max): (10e-3 - 10e-12)
        SD default: 10e-6
        SF (min - max): (10e-4 - 10e-12)
        SF default: 10e-4

Cached driver state:
    MTU: 9216 bytes
    Burnt-in MAC address: 54a2.741c.3c5d

Operational carrier delay:
    Carrier delay (up): 9000 ms
    Carrier delay (down): 50 ms

Not a member of a bundle interface.

Satellite uplink settings:
    Not in satellite uplink (ICL) mode.

Port FSM state:
    Port is enabled, link is up

Complete FSM state:
    Admin up
    Client admin up
    Client admin tx not disabled
    Port enabled
    Port tx enabled
    Hardware link up
IDB interface state information:
    IDB client admin up
    IDB client tx admin up
    IDB error disable not set

0 Unicast MAC Addresses:

0 Multicast MAC Addresses:


Management information for interface HundredGigE0/4/0/1:
 
Port number: 1
Bay number: 0
Interface handle: 0x14800c0

Config:
    Auto-negotiation: Configuration not supported (Off)
    Carrier delay (up): 9000 ms
    Carrier delay (down): 50 ms
    Speed: Configuration not supported (100Gbps)
    Duplex: Configuration not supported (Full Duplex)
    Flow Control: Not configured (None)
    IPG: Configuration not supported (standard (12))
    Loopback: Not configured (None)
    MTU: 9216 bytes
    Bandwidth: Not configured
    BER-SD Threshold: Not configured (10e-6)
    BER-SD Report: Not configured (Disabled)
    BER-SF Threshold: Not configured (10e-4)
    BER-SF Report: Not configured (Enabled)
    BER-SF Signal Remote Failure: Not configured (Disabled)

Driver constraints:
    Min MTU: 64 bytes
    Max MTU: 9600 bytes
    Max speed: 100Gbps
    Interface type: HundredGigE
    Management interface: No
    Promiscuous mode: Yes
    Default carrier delay up (auto-neg on): 0 ms
    Default carrier delay down (auto-neg on): 0 ms
    Default carrier delay up (auto-neg off): 0 ms
    Default carrier delay down (auto-neg off): 0 ms
    Allowed config mask: 0xe6b
    BER:
        SD (min - max): (10e-3 - 10e-12)
        SD default: 10e-6
        SF (min - max): (10e-4 - 10e-12)
        SF default: 10e-4

Cached driver state:
    MTU: 9216 bytes
    Burnt-in MAC address: 54a2.741c.3c5e

Operational carrier delay:
    Carrier delay (up): 9000 ms
    Carrier delay (down): 50 ms

Not a member of a bundle interface.

Satellite uplink settings:
    Not in satellite uplink (ICL) mode.

Port FSM state:
    Port is enabled, link is up

Complete FSM state:
    Admin up
    Client admin up
    Client admin tx not disabled
    Port enabled
    Port tx enabled
    Hardware link up
IDB interface state information:
    IDB client admin up
    IDB client tx admin up
    IDB error disable not set

0 Unicast MAC Addresses:

0 Multicast MAC Addresses:


Management information for interface HundredGigE0/4/0/2:
 
Port number: 2
Bay number: 0
Interface handle: 0x14800e0

Config:
    Auto-negotiation: Configuration not supported (Off)
    Carrier delay (up): 9000 ms
    Carrier delay (down): 50 ms
    Speed: Configuration not supported (100Gbps)
    Duplex: Configuration not supported (Full Duplex)
    Flow Control: Not configured (None)
    IPG: Configuration not supported (standard (12))
    Loopback: Not configured (None)
    MTU: 9216 bytes
    Bandwidth: Not configured
    BER-SD Threshold: Not configured (10e-6)
    BER-SD Report: Not configured (Disabled)
    BER-SF Threshold: Not configured (10e-4)
    BER-SF Report: Not configured (Enabled)
    BER-SF Signal Remote Failure: Not configured (Disabled)

Driver constraints:
    Min MTU: 64 bytes
    Max MTU: 9600 bytes
    Max speed: 100Gbps
    Interface type: HundredGigE
    Management interface: No
    Promiscuous mode: Yes
    Default carrier delay up (auto-neg on): 0 ms
    Default carrier delay down (auto-neg on): 0 ms
    Default carrier delay up (auto-neg off): 0 ms
    Default carrier delay down (auto-neg off): 0 ms
    Allowed config mask: 0xe6b
    BER:
        SD (min - max): (10e-3 - 10e-12)
        SD default: 10e-6
        SF (min - max): (10e-4 - 10e-12)
        SF default: 10e-4

Cached driver state:
    MTU: 9216 bytes
    Burnt-in MAC address: 54a2.741c.3c5f

Operational carrier delay:
    Carrier delay (up): 9000 ms
    Carrier delay (down): 50 ms

Not a member of a bundle interface.

Satellite uplink settings:
    Not in satellite uplink (ICL) mode.

Port FSM state:
    Port is enabled, link is up

Complete FSM state:
    Admin up
    Client admin up
    Client admin tx not disabled
    Port enabled
    Port tx enabled
    Hardware link up
IDB interface state information:
    IDB client admin up
    IDB client tx admin up
    IDB error disable not set

0 Unicast MAC Addresses:

0 Multicast MAC Addresses:


Management information for interface HundredGigE0/4/0/3:
 
Port number: 3
Bay number: 0
Interface handle: 0x1480100

Config:
    Auto-negotiation: Configuration not supported (Off)
    Carrier delay (up): Not configured
    Carrier delay (down): Not configured
    Speed: Configuration not supported (100Gbps)
    Duplex: Configuration not supported (Full Duplex)
    Flow Control: Not configured (None)
    IPG: Configuration not supported (standard (12))
    Loopback: Not configured (None)
    MTU: Not configured
    Bandwidth: Not configured
    BER-SD Threshold: Not configured (10e-6)
    BER-SD Report: Not configured (Disabled)
    BER-SF Threshold: Not configured (10e-4)
    BER-SF Report: Not configured (Enabled)
    BER-SF Signal Remote Failure: Not configured (Disabled)

Driver constraints:
    Min MTU: 64 bytes
    Max MTU: 9600 bytes
    Max speed: 100Gbps
    Interface type: HundredGigE
    Management interface: No
    Promiscuous mode: Yes
    Default carrier delay up (auto-neg on): 0 ms
    Default carrier delay down (auto-neg on): 0 ms
    Default carrier delay up (auto-neg off): 0 ms
    Default carrier delay down (auto-neg off): 0 ms
    Allowed config mask: 0xe6b
    BER:
        SD (min - max): (10e-3 - 10e-12)
        SD default: 10e-6
        SF (min - max): (10e-4 - 10e-12)
        SF default: 10e-4

Cached driver state:
    MTU: 1514 bytes
    Burnt-in MAC address: 54a2.741c.3c60

Operational carrier delay:
    Carrier delay (up): 0 ms
    Carrier delay (down): 0 ms
 
Not a member of a bundle interface.

Satellite uplink settings:
    Not in satellite uplink (ICL) mode.

Port FSM state:
    Port is disabled, due to an admin down condition.

Complete FSM state:
    Admin down
    Client admin up
    Client admin tx not disabled
    Port disabled
    Port tx disabled
    Hardware link down
IDB interface state information:
    IDB client admin up
    IDB client tx admin up
    IDB error disable not set

0 Unicast MAC Addresses:

0 Multicast MAC Addresses:



Operational address: 54a2.741c.3b29
 Burnt-in address: 54a2.741c.3b29
Administrative state: Up
Operational state: Up

0 HSRP/VRRP MAC addresses

VLAN Ethertype: 0x8100
QinQ Ethertype: 0x88a8
MTP  Ethertype: 0x88e7

2 VLAN UIDB entries
VLAN1   VLAN2      Packet Type Flags      UIDB Result Flags
   0        0          VLAN                  1 VLAN
   0        0               ARPA             1 ARPA



Operational address: 54a2.741c.3b2a
Burnt-in address: 54a2.741c.3b2a
Administrative state: Up
Operational state: Up

0 HSRP/VRRP MAC addresses

VLAN Ethertype: 0x8100
 QinQ Ethertype: 0x88a8
MTP  Ethertype: 0x88e7

2 VLAN UIDB entries
VLAN1   VLAN2      Packet Type Flags      UIDB Result Flags
   0        0          VLAN                  2 VLAN
   0        0               ARPA             2 ARPA



Operational address: 54a2.741c.3b2b
Burnt-in address: 54a2.741c.3b2b
Administrative state: Up
Operational state: Up

0 HSRP/VRRP MAC addresses

VLAN Ethertype: 0x8100
QinQ Ethertype: 0x88a8
MTP  Ethertype: 0x88e7

2 VLAN UIDB entries
VLAN1   VLAN2      Packet Type Flags      UIDB Result Flags
   0        0          VLAN                  1 VLAN
   0        0               ARPA             1 ARPA



Operational address: 54a2.741c.3b2c
 Burnt-in address: 54a2.741c.3b2c
Administrative state: Forced Local fault
 Operational state: Local fault

0 HSRP/VRRP MAC addresses

VLAN Ethertype: 0x8100
QinQ Ethertype: 0x88a8
MTP  Ethertype: 0x88e7

2 VLAN UIDB entries
VLAN1   VLAN2      Packet Type Flags      UIDB Result Flags
   0        0          VLAN                  2 VLAN
   0        0               ARPA             2 ARPA



Operational address: 54a2.741c.3c5d
Burnt-in address: 54a2.741c.3c5d
Administrative state: Up
Operational state: Up

0 HSRP/VRRP MAC addresses

VLAN Ethertype: 0x8100
QinQ Ethertype: 0x88a8
MTP  Ethertype: 0x88e7

2 VLAN UIDB entries
VLAN1   VLAN2      Packet Type Flags      UIDB Result Flags
   0        0          VLAN                  1 VLAN
   0        0               ARPA             1 ARPA



Operational address: 54a2.741c.3c5e
 Burnt-in address: 54a2.741c.3c5e
Administrative state: Up
Operational state: Up

0 HSRP/VRRP MAC addresses

VLAN Ethertype: 0x8100
QinQ Ethertype: 0x88a8
MTP  Ethertype: 0x88e7

2 VLAN UIDB entries
VLAN1   VLAN2      Packet Type Flags      UIDB Result Flags
   0        0          VLAN                  2 VLAN
   0        0               ARPA             2 ARPA



Operational address: 54a2.741c.3c5f
Burnt-in address: 54a2.741c.3c5f
Administrative state: Up
Operational state: Up

0 HSRP/VRRP MAC addresses

VLAN Ethertype: 0x8100
 QinQ Ethertype: 0x88a8
MTP  Ethertype: 0x88e7

2 VLAN UIDB entries
VLAN1   VLAN2      Packet Type Flags      UIDB Result Flags
   0        0          VLAN                  1 VLAN
   0        0               ARPA             1 ARPA



Operational address: 54a2.741c.3c60
Burnt-in address: 54a2.741c.3c60
Administrative state: Forced Local fault
Operational state: Local fault

0 HSRP/VRRP MAC addresses

VLAN Ethertype: 0x8100
QinQ Ethertype: 0x88a8
MTP  Ethertype: 0x88e7

2 VLAN UIDB entries
VLAN1   VLAN2      Packet Type Flags      UIDB Result Flags
   0        0          VLAN                  2 VLAN
   0        0               ARPA             2 ARPA


PLIM type 0x28 ports=4
PLIM shared mem: hw_init 0x1 ctx version 0x1
Port 0 t100 inst 0 otn_cfg 0 t100 otn 0
    cpak init flag 0x66666666 
    cpak pending oir count 0 
    optics info valid 1
    optics type 0x83
    xcvr   type 0xf7
    xcvr   str 100GBASE-SR10
Maximum CPAK power class supported: 3
 Maximum CPAK power consumption supported: 8000 mW

PLIM type 0x28 ports=4
 PLIM shared mem: hw_init 0x1 ctx version 0x1
Port 1 t100 inst 1 otn_cfg 0 t100 otn 0
    cpak init flag 0x66666666 
    cpak pending oir count 0 
    optics info valid 1
    optics type 0x83
    xcvr   type 0xf7
    xcvr   str 100GBASE-SR10
 Maximum CPAK power class supported: 3
Maximum CPAK power consumption supported: 8000 mW

PLIM type 0x28 ports=4
PLIM shared mem: hw_init 0x1 ctx version 0x1
Port 2 t100 inst 2 otn_cfg 0 t100 otn 0
    cpak init flag 0x66666666 
    cpak pending oir count 0 
    optics info valid 1
    optics type 0x83
    xcvr   type 0xf7
    xcvr   str 100GBASE-SR10
Maximum CPAK power class supported: 3
Maximum CPAK power consumption supported: 8000 mW

PLIM type 0x28 ports=4
PLIM shared mem: hw_init 0x1 ctx version 0x1
Port 3 t100 inst 3 otn_cfg 0 t100 otn 0
    cpak init flag 0x66666666 
    cpak pending oir count 0 
    optics info valid 1
    optics type 0x83
    xcvr   type 0xf7
    xcvr   str 100GBASE-SR10
Maximum CPAK power class supported: 3
Maximum CPAK power consumption supported: 8000 mW

PLIM type 0x28 ports=4
PLIM shared mem: hw_init 0x1 ctx version 0x1
Port 0 t100 inst 0 otn_cfg 0 t100 otn 0
    cpak init flag 0x66666666 
    cpak pending oir count 0 
    optics info valid 1
    optics type 0x83
    xcvr   type 0xf7
    xcvr   str 100GBASE-SR10
 Maximum CPAK power class supported: 3
Maximum CPAK power consumption supported: 8000 mW

PLIM type 0x28 ports=4
PLIM shared mem: hw_init 0x1 ctx version 0x1
Port 1 t100 inst 1 otn_cfg 0 t100 otn 0
    cpak init flag 0x66666666 
    cpak pending oir count 0 
    optics info valid 1
    optics type 0x83
    xcvr   type 0xf7
    xcvr   str 100GBASE-SR10
Maximum CPAK power class supported: 3
Maximum CPAK power consumption supported: 8000 mW

PLIM type 0x28 ports=4
PLIM shared mem: hw_init 0x1 ctx version 0x1
Port 2 t100 inst 2 otn_cfg 0 t100 otn 0
    cpak init flag 0x66666666 
    cpak pending oir count 0 
    optics info valid 1
    optics type 0x83
    xcvr   type 0xf7
    xcvr   str 100GBASE-SR10
Maximum CPAK power class supported: 3
Maximum CPAK power consumption supported: 8000 mW

PLIM type 0x28 ports=4
PLIM shared mem: hw_init 0x1 ctx version 0x1
Port 3 t100 inst 3 otn_cfg 0 t100 otn 0
    cpak init flag 0x66666666 
    cpak pending oir count 0 
    optics info valid 1
    optics type 0x83
    xcvr   type 0xf7
    xcvr   str 100GBASE-SR10
 Maximum CPAK power class supported: 3
Maximum CPAK power consumption supported: 8000 mW


PCS
  Previous PCS Status: 
    PCS Rx Link Status was UP
    PCS Rx Link was Block Locked
    PCS BER (Sync Header Error) Counts: 0
    PCS BER (BIP) Counts: 0
    PCS BER (BIP) 1 second count: 0 (BER < 10e-9)
    PCS SD-BER Alarm was OFF
    PCS SF-BER Alarm was OFF
  Current PCS Status: 
    PCS Rx Link Status is UP
    PCS Rx Link is Block Locked
    PCS BER (Sync Header Error) Counts: 0
    PCS BER (BIP) Counts: 0
    PCS BER (BIP) 1 second count: 0 (BER < 10e-9)
    PCS SD-BER Alarm is OFF
    PCS SF-BER Alarm is OFF

PCS detailed information:

  RX Service Interface Lane Sync Header Lock Status:

    Lane 0 : Locked
    Lane 1 : Locked
    Lane 2 : Locked
    Lane 3 : Locked
    Lane 4 : Locked
    Lane 5 : Locked
    Lane 6 : Locked
    Lane 7 : Locked
    Lane 8 : Locked
    Lane 9 : Locked

  Mapping of Service Interface Lane and RX PCS Lane:

    Rx Service Interface Lane 0  = PCS Lane 0
    Rx Service Interface Lane 1  = PCS Lane 1
    Rx Service Interface Lane 2  = PCS Lane 2
    Rx Service Interface Lane 3  = PCS Lane 3
    Rx Service Interface Lane 4  = PCS Lane 4
    Rx Service Interface Lane 5  = PCS Lane 5
    Rx Service Interface Lane 6  = PCS Lane 6
    Rx Service Interface Lane 7  = PCS Lane 7
    Rx Service Interface Lane 8  = PCS Lane 8
    Rx Service Interface Lane 9  = PCS Lane 9

  PCS Lane BIP Error Counters:

             Even sublane     Odd sublane
    Lane 0 : 0                0               
    Lane 1 : 0                0               
    Lane 2 : 0                0               
    Lane 3 : 0                0               
    Lane 4 : 0                0               
    Lane 5 : 0                0               
    Lane 6 : 0                0               
    Lane 7 : 0                0               
    Lane 8 : 0                0               
    Lane 9 : 0                0               

  Total PCS Lane BIP Error Count          : 0
  Total PCS Lane Sync Header Error Count  : 0
  Total PCS Lane Bad 64/66 Code Count     : 0
 
 General Info:
=================


PMA/PMD:
========
  Previous Alarm Status:
      PMA/PMD Rx Link is Up.
      LR4 Ability
      SR10 Ability
  Current Alarm Status:
      PMA/PMD Rx Link is Up.
      LR4 Ability
      SR10 Ability

CPAK section:
=============

Quack check: PASSED
 
CPAK General Information:

  Module Identifier:         CPAK_10x10G
  Ethernet Application Code: 100GBASE-SR10
  Module State:              Ready
  Power Class:               1
  Maximum Power Consumption: 4600 mW

CPAK Vendor Information:

  Vendor Name:         CISCO           
  Vendor PN:           800-41495-01    
  Vendor SN:           FBN19122017     
  Vendor OUI:          0x0-0x0-0xc
  Lot Code:            
  DATE CODE(YYYY/MM/DD): 2015/03/20
  CPAK MSA Hardware Version:   11.0
  CPAK MSA MDIO Version:       9.0
  Vendor Hardware Version:    0.5
  Vendor Firmware Version:    2.3

CPAK UDI Information:

  UDI Compliant: Yes
  Cisco PID: CPAK-100G-SR10  
  Cisco VID: V01 

CPAK Cisco Information:

  Vendor Name: CISCO           
  Cisco PN   : 800-41495-01  Rev B0  
  Cisco SN   : FBN19122017

CPAK Detail Information:

  Number of lanes supported: 

    Number of network lanes: 10
    Number of host lanes   : 10

  Time required by module: 

    Maximum high-power-up time:   1 s
    Maximum high-power-down time:   1 s
    Maximum tx-turn-on time   :   1 s

    Maximum tx-turn-off time    : 254 ms

  Module general control: 

    Soft reset asserted     : No
    Soft low power asserted : No
    Soft tx disable asserted: No
    Soft program control 3 asserted: No
    Soft program control 2 asserted: No
    Soft program control 1 asserted: No
    Soft global alarm test asserted: No

    Tx disable pin asserted: No
    Low power pin asserted : No
    Program control 3 pin asserted: No
    Program control 2 pin asserted: No
    Program control 1 pin asserted: No

  Module Analog A/D value: 

    Power supply voltage : 3.3040 V
    Temperature          : 27.8658 degC

  Network lane A/D value: 

    Lane 0 Tx power: 0.5442 mW ( -2.6 dBm)
    Lane 1 Tx power: 0.5721 mW ( -2.4 dBm)
    Lane 2 Tx power: 0.5250 mW ( -2.8 dBm)
    Lane 3 Tx power: 0.5631 mW ( -2.5 dBm)
    Lane 4 Tx power: 0.5583 mW ( -2.5 dBm)
    Lane 5 Tx power: 0.6094 mW ( -2.2 dBm)
    Lane 6 Tx power: 0.5844 mW ( -2.3 dBm)
    Lane 7 Tx power: 0.5921 mW ( -2.3 dBm)
    Lane 8 Tx power: 0.5863 mW ( -2.3 dBm)
    Lane 9 Tx power: 0.6094 mW ( -2.2 dBm)

    Lane 0 Rx power: 0.5664 mW ( -2.5 dBm)
    Lane 1 Rx power: 0.5791 mW ( -2.4 dBm)
    Lane 2 Rx power: 0.5990 mW ( -2.2 dBm)
    Lane 3 Rx power: 0.5472 mW ( -2.6 dBm)
    Lane 4 Rx power: 0.4529 mW ( -3.4 dBm)
    Lane 5 Rx power: 0.5097 mW ( -2.9 dBm)
    Lane 6 Rx power: 0.5001 mW ( -3.0 dBm)
    Lane 7 Rx power: 0.4642 mW ( -3.3 dBm)
    Lane 8 Rx power: 0.5543 mW ( -2.6 dBm)
    Lane 9 Rx power: 0.5132 mW ( -2.9 dBm)

    Total Tx power : 5.7443 mW (  7.6 dBm)
    Total Rx power : 5.2861 mW (  7.2 dBm)



PCS
  Previous PCS Status: 
    PCS Rx Link Status was UP
    PCS Rx Link was Block Locked
    PCS BER (Sync Header Error) Counts: 0
    PCS BER (BIP) Counts: 0
    PCS BER (BIP) 1 second count: 0 (BER < 10e-9)
    PCS SD-BER Alarm was OFF
    PCS SF-BER Alarm was OFF
  Current PCS Status: 
    PCS Rx Link Status is UP
    PCS Rx Link is Block Locked
    PCS BER (Sync Header Error) Counts: 0
    PCS BER (BIP) Counts: 0
    PCS BER (BIP) 1 second count: 0 (BER < 10e-9)
    PCS SD-BER Alarm is OFF
    PCS SF-BER Alarm is OFF

PCS detailed information:

  RX Service Interface Lane Sync Header Lock Status:

    Lane 0 : Locked
    Lane 1 : Locked
    Lane 2 : Locked
    Lane 3 : Locked
    Lane 4 : Locked
    Lane 5 : Locked
    Lane 6 : Locked
    Lane 7 : Locked
    Lane 8 : Locked
    Lane 9 : Locked

  Mapping of Service Interface Lane and RX PCS Lane:

    Rx Service Interface Lane 0  = PCS Lane 0
    Rx Service Interface Lane 1  = PCS Lane 1
    Rx Service Interface Lane 2  = PCS Lane 2
    Rx Service Interface Lane 3  = PCS Lane 3
    Rx Service Interface Lane 4  = PCS Lane 4
    Rx Service Interface Lane 5  = PCS Lane 5
    Rx Service Interface Lane 6  = PCS Lane 6
    Rx Service Interface Lane 7  = PCS Lane 7
    Rx Service Interface Lane 8  = PCS Lane 8
    Rx Service Interface Lane 9  = PCS Lane 9

  PCS Lane BIP Error Counters:

             Even sublane     Odd sublane
    Lane 0 : 0                0               
    Lane 1 : 0                0               
    Lane 2 : 0                0               
    Lane 3 : 0                0               
    Lane 4 : 0                0               
    Lane 5 : 0                0               
    Lane 6 : 0                0               
    Lane 7 : 0                0               
    Lane 8 : 0                0               
    Lane 9 : 0                0               

  Total PCS Lane BIP Error Count          : 0
  Total PCS Lane Sync Header Error Count  : 0
  Total PCS Lane Bad 64/66 Code Count     : 0

 General Info:
=================


PMA/PMD:
========
  Previous Alarm Status:
      PMA/PMD Rx Link is Up.
      LR4 Ability
      SR10 Ability
  Current Alarm Status:
      PMA/PMD Rx Link is Up.
      LR4 Ability
      SR10 Ability

CPAK section:
=============
 
Quack check: PASSED

CPAK General Information:

  Module Identifier:         CPAK_10x10G
  Ethernet Application Code: 100GBASE-SR10
  Module State:              Ready
  Power Class:               1
  Maximum Power Consumption: 4600 mW

CPAK Vendor Information:

  Vendor Name:         CISCO           
  Vendor PN:           800-41495-01    
  Vendor SN:           FBN19092109     
  Vendor OUI:          0x0-0x0-0xc
  Lot Code:            
  DATE CODE(YYYY/MM/DD): 2015/03/05
  CPAK MSA Hardware Version:   11.0
  CPAK MSA MDIO Version:       9.0
  Vendor Hardware Version:    0.5
  Vendor Firmware Version:    2.3

CPAK UDI Information:

  UDI Compliant: Yes
  Cisco PID: CPAK-100G-SR10  
  Cisco VID: V01 

CPAK Cisco Information:

  Vendor Name: CISCO           
  Cisco PN   : 800-41495-01  Rev B0  
  Cisco SN   : FBN19092109
 
CPAK Detail Information:

  Number of lanes supported: 

    Number of network lanes: 10
    Number of host lanes   : 10

  Time required by module: 

    Maximum high-power-up time:   1 s
    Maximum high-power-down time:   1 s
    Maximum tx-turn-on time   :   1 s

    Maximum tx-turn-off time    : 254 ms

  Module general control: 

    Soft reset asserted     : No
    Soft low power asserted : No
    Soft tx disable asserted: No
    Soft program control 3 asserted: No
    Soft program control 2 asserted: No
    Soft program control 1 asserted: No
    Soft global alarm test asserted: No

    Tx disable pin asserted: No
    Low power pin asserted : No
    Program control 3 pin asserted: No
    Program control 2 pin asserted: No
    Program control 1 pin asserted: No

  Module Analog A/D value: 

    Power supply voltage : 3.2551 V
    Temperature          : 27.4290 degC

  Network lane A/D value: 

    Lane 0 Tx power: 0.5207 mW ( -2.8 dBm)
    Lane 1 Tx power: 0.4755 mW ( -3.2 dBm)
    Lane 2 Tx power: 0.4845 mW ( -3.1 dBm)
    Lane 3 Tx power: 0.4681 mW ( -3.3 dBm)
    Lane 4 Tx power: 0.4810 mW ( -3.2 dBm)
    Lane 5 Tx power: 0.4938 mW ( -3.1 dBm)
    Lane 6 Tx power: 0.5083 mW ( -2.9 dBm)
    Lane 7 Tx power: 0.4852 mW ( -3.1 dBm)
    Lane 8 Tx power: 0.5055 mW ( -3.0 dBm)
    Lane 9 Tx power: 0.4843 mW ( -3.1 dBm)

    Lane 0 Rx power: 0.5521 mW ( -2.6 dBm)
    Lane 1 Rx power: 0.6011 mW ( -2.2 dBm)
    Lane 2 Rx power: 0.6191 mW ( -2.1 dBm)
    Lane 3 Rx power: 0.5469 mW ( -2.6 dBm)
    Lane 4 Rx power: 0.6021 mW ( -2.2 dBm)
    Lane 5 Rx power: 0.5577 mW ( -2.5 dBm)
    Lane 6 Rx power: 0.5638 mW ( -2.5 dBm)
    Lane 7 Rx power: 0.5897 mW ( -2.3 dBm)
    Lane 8 Rx power: 0.6259 mW ( -2.0 dBm)
    Lane 9 Rx power: 0.6124 mW ( -2.1 dBm)

    Total Tx power : 4.9069 mW (  6.9 dBm)
    Total Rx power : 5.8708 mW (  7.7 dBm)



PCS
  Previous PCS Status: 
    PCS Rx Link Status was UP
    PCS Rx Link was Block Locked
    PCS BER (Sync Header Error) Counts: 0
    PCS BER (BIP) Counts: 0
    PCS BER (BIP) 1 second count: 0 (BER < 10e-9)
    PCS SD-BER Alarm was OFF
    PCS SF-BER Alarm was OFF
  Current PCS Status: 
    PCS Rx Link Status is UP
    PCS Rx Link is Block Locked
    PCS BER (Sync Header Error) Counts: 0
    PCS BER (BIP) Counts: 0
    PCS BER (BIP) 1 second count: 0 (BER < 10e-9)
    PCS SD-BER Alarm is OFF
    PCS SF-BER Alarm is OFF

PCS detailed information:

  RX Service Interface Lane Sync Header Lock Status:

    Lane 0 : Locked
    Lane 1 : Locked
    Lane 2 : Locked
    Lane 3 : Locked
    Lane 4 : Locked
    Lane 5 : Locked
    Lane 6 : Locked
    Lane 7 : Locked
    Lane 8 : Locked
    Lane 9 : Locked

  Mapping of Service Interface Lane and RX PCS Lane:

    Rx Service Interface Lane 0  = PCS Lane 0
    Rx Service Interface Lane 1  = PCS Lane 1
    Rx Service Interface Lane 2  = PCS Lane 2
    Rx Service Interface Lane 3  = PCS Lane 3
    Rx Service Interface Lane 4  = PCS Lane 4
    Rx Service Interface Lane 5  = PCS Lane 5
    Rx Service Interface Lane 6  = PCS Lane 6
    Rx Service Interface Lane 7  = PCS Lane 7
    Rx Service Interface Lane 8  = PCS Lane 8
    Rx Service Interface Lane 9  = PCS Lane 9

  PCS Lane BIP Error Counters:

             Even sublane     Odd sublane
    Lane 0 : 0                0               
    Lane 1 : 0                0               
    Lane 2 : 0                0               
    Lane 3 : 0                0               
    Lane 4 : 0                0               
    Lane 5 : 0                0               
    Lane 6 : 0                0               
    Lane 7 : 0                0               
    Lane 8 : 0                0               
    Lane 9 : 0                0               

  Total PCS Lane BIP Error Count          : 0
  Total PCS Lane Sync Header Error Count  : 0
  Total PCS Lane Bad 64/66 Code Count     : 0
 
 General Info:
=================


PMA/PMD:
========
  Previous Alarm Status:
      PMA/PMD Rx Link is Up.
      LR4 Ability
      SR10 Ability
  Current Alarm Status:
      PMA/PMD Rx Link is Up.
      LR4 Ability
      SR10 Ability

CPAK section:
=============

Quack check: PASSED
 
CPAK General Information:

  Module Identifier:         CPAK_10x10G
  Ethernet Application Code: 100GBASE-SR10
  Module State:              Ready
  Power Class:               1
  Maximum Power Consumption: 4600 mW

CPAK Vendor Information:

  Vendor Name:         CISCO           
  Vendor PN:           800-41495-01    
  Vendor SN:           FBN19122019     
  Vendor OUI:          0x0-0x0-0xc
  Lot Code:            
  DATE CODE(YYYY/MM/DD): 2015/03/19
  CPAK MSA Hardware Version:   11.0
  CPAK MSA MDIO Version:       9.0
  Vendor Hardware Version:    0.5
  Vendor Firmware Version:    2.3

CPAK UDI Information:

  UDI Compliant: Yes
  Cisco PID: CPAK-100G-SR10  
  Cisco VID: V01 

CPAK Cisco Information:

  Vendor Name: CISCO           
  Cisco PN   : 800-41495-01  Rev B0  
  Cisco SN   : FBN19122019

CPAK Detail Information:

  Number of lanes supported: 

    Number of network lanes: 10
    Number of host lanes   : 10

  Time required by module: 

    Maximum high-power-up time:   1 s
    Maximum high-power-down time:   1 s
    Maximum tx-turn-on time   :   1 s

    Maximum tx-turn-off time    : 254 ms

  Module general control: 

    Soft reset asserted     : No
    Soft low power asserted : No
    Soft tx disable asserted: No
    Soft program control 3 asserted: No
    Soft program control 2 asserted: No
    Soft program control 1 asserted: No
    Soft global alarm test asserted: No

    Tx disable pin asserted: No
    Low power pin asserted : No
    Program control 3 pin asserted: No
    Program control 2 pin asserted: No
    Program control 1 pin asserted: No

  Module Analog A/D value: 

    Power supply voltage : 3.2710 V
    Temperature          : 25.8268 degC

  Network lane A/D value: 

    Lane 0 Tx power: 0.5377 mW ( -2.7 dBm)
    Lane 1 Tx power: 0.5012 mW ( -3.0 dBm)
    Lane 2 Tx power: 0.5002 mW ( -3.0 dBm)
    Lane 3 Tx power: 0.4702 mW ( -3.3 dBm)
    Lane 4 Tx power: 0.5248 mW ( -2.8 dBm)
    Lane 5 Tx power: 0.4907 mW ( -3.1 dBm)
    Lane 6 Tx power: 0.5127 mW ( -2.9 dBm)
    Lane 7 Tx power: 0.4805 mW ( -3.2 dBm)
    Lane 8 Tx power: 0.5319 mW ( -2.7 dBm)
    Lane 9 Tx power: 0.5024 mW ( -3.0 dBm)

    Lane 0 Rx power: 0.4787 mW ( -3.2 dBm)
    Lane 1 Rx power: 0.5329 mW ( -2.7 dBm)
    Lane 2 Rx power: 0.5327 mW ( -2.7 dBm)
    Lane 3 Rx power: 0.5148 mW ( -2.9 dBm)
    Lane 4 Rx power: 0.4681 mW ( -3.3 dBm)
    Lane 5 Rx power: 0.4620 mW ( -3.4 dBm)
    Lane 6 Rx power: 0.5199 mW ( -2.8 dBm)
    Lane 7 Rx power: 0.4814 mW ( -3.2 dBm)
    Lane 8 Rx power: 0.4989 mW ( -3.0 dBm)
    Lane 9 Rx power: 0.4836 mW ( -3.2 dBm)

    Total Tx power : 5.0523 mW (  7.0 dBm)
    Total Rx power : 4.9730 mW (  7.0 dBm)



PCS
  Previous PCS Status: 
    PCS Rx Link Status was DOWN
    PCS Rx Link was NOT Block Locked
    PCS BER (Sync Header Error) Counts: 0
    PCS BER (BIP) Counts: 0
    PCS BER (BIP) 1 second count: 0 (BER < 10e-9)
    PCS SD-BER Alarm was OFF
    PCS SF-BER Alarm was OFF
  Current PCS Status: 
    PCS Rx Link Status is DOWN
    PCS Rx Link is NOT Block Locked
    PCS BER (Sync Header Error) Counts: 0
    PCS BER (BIP) Counts: 0
    PCS BER (BIP) 1 second count: 0 (BER < 10e-9)
    PCS SD-BER Alarm is OFF
    PCS SF-BER Alarm is OFF

 PCS detailed information:

  RX Service Interface Lane Sync Header Lock Status:

    Lane 0 : Not Locked
    Lane 1 : Not Locked
    Lane 2 : Not Locked
    Lane 3 : Not Locked
    Lane 4 : Not Locked
    Lane 5 : Not Locked
    Lane 6 : Not Locked
    Lane 7 : Not Locked
    Lane 8 : Not Locked
    Lane 9 : Not Locked

  Mapping of Service Interface Lane and RX PCS Lane:

    Rx Service Interface Lane 0  = PCS Lane 0
    Rx Service Interface Lane 1  = PCS Lane 1
    Rx Service Interface Lane 2  = PCS Lane 2
    Rx Service Interface Lane 3  = PCS Lane 3
    Rx Service Interface Lane 4  = PCS Lane 4
    Rx Service Interface Lane 5  = PCS Lane 5
    Rx Service Interface Lane 6  = PCS Lane 6
    Rx Service Interface Lane 7  = PCS Lane 7
    Rx Service Interface Lane 8  = PCS Lane 8
    Rx Service Interface Lane 9  = PCS Lane 9

  PCS Lane BIP Error Counters:

             Even sublane     Odd sublane
    Lane 0 : 0                0               
    Lane 1 : 0                0               
    Lane 2 : 0                0               
    Lane 3 : 0                0               
    Lane 4 : 0                0               
    Lane 5 : 0                0               
    Lane 6 : 0                0               
    Lane 7 : 0                0               
    Lane 8 : 0                0               
    Lane 9 : 0                0               

  Total PCS Lane BIP Error Count          : 0
  Total PCS Lane Sync Header Error Count  : 0
  Total PCS Lane Bad 64/66 Code Count     : 0

 General Info:
=================


PMA/PMD:
========
  Previous Alarm Status:
      PMA/PMD Rx Link is Down.
      PMA/PMD Local Fault
      LR4 Ability
      SR10 Ability
      Rx Local Fault
  Current Alarm Status:
      PMA/PMD Rx Link is Down.
      PMA/PMD Local Fault
      LR4 Ability
      SR10 Ability
      Rx Local Fault

CPAK section:
 =============

Quack check: PASSED

CPAK General Information:

  Module Identifier:         CPAK_10x10G
  Ethernet Application Code: 100GBASE-SR10
  Module State:              TX Off
  Power Class:               1
  Maximum Power Consumption: 4600 mW

CPAK Vendor Information:

  Vendor Name:         CISCO           
  Vendor PN:           800-41495-01    
  Vendor SN:           FBN19122030     
  Vendor OUI:          0x0-0x0-0xc
  Lot Code:            
  DATE CODE(YYYY/MM/DD): 2015/03/19
  CPAK MSA Hardware Version:   11.0
  CPAK MSA MDIO Version:       9.0
  Vendor Hardware Version:    0.5
  Vendor Firmware Version:    2.3

CPAK UDI Information:

  UDI Compliant: Yes
  Cisco PID: CPAK-100G-SR10  
  Cisco VID: V01 

CPAK Cisco Information:

  Vendor Name: CISCO           
  Cisco PN   : 800-41495-01  Rev B0  
  Cisco SN   : FBN19122030

CPAK Detail Information:

  Number of lanes supported: 

    Number of network lanes: 10
    Number of host lanes   : 10

  Time required by module: 

    Maximum high-power-up time:   1 s
    Maximum high-power-down time:   1 s
    Maximum tx-turn-on time   :   1 s

    Maximum tx-turn-off time    : 254 ms

  Module general control: 

    Soft reset asserted     : No
    Soft low power asserted : No
    Soft tx disable asserted: Yes
    Soft program control 3 asserted: No
    Soft program control 2 asserted: No
    Soft program control 1 asserted: No
    Soft global alarm test asserted: No

    Tx disable pin asserted: No
    Low power pin asserted : No
    Program control 3 pin asserted: No
    Program control 2 pin asserted: No
    Program control 1 pin asserted: No

  Module Analog A/D value: 

    Power supply voltage : 3.2954 V
    Temperature          : 21.1521 degC

  Network lane A/D value: 

    Lane 0 Tx power: 0.0000 mW (-40.0 dBm)
    Lane 1 Tx power: 0.0000 mW (-40.0 dBm)
    Lane 2 Tx power: 0.0000 mW (-40.0 dBm)
    Lane 3 Tx power: 0.0000 mW (-40.0 dBm)
    Lane 4 Tx power: 0.0000 mW (-40.0 dBm)
    Lane 5 Tx power: 0.0000 mW (-40.0 dBm)
    Lane 6 Tx power: 0.0000 mW (-40.0 dBm)
    Lane 7 Tx power: 0.0000 mW (-40.0 dBm)
    Lane 8 Tx power: 0.0000 mW (-40.0 dBm)
    Lane 9 Tx power: 0.0000 mW (-40.0 dBm)

    Lane 0 Rx power: 0.0000 mW (-40.0 dBm)
    Lane 1 Rx power: 0.0000 mW (-40.0 dBm)
    Lane 2 Rx power: 0.0000 mW (-40.0 dBm)
    Lane 3 Rx power: 0.0000 mW (-40.0 dBm)
    Lane 4 Rx power: 0.0000 mW (-40.0 dBm)
    Lane 5 Rx power: 0.0000 mW (-40.0 dBm)
    Lane 6 Rx power: 0.0000 mW (-40.0 dBm)
    Lane 7 Rx power: 0.0000 mW (-40.0 dBm)
    Lane 8 Rx power: 0.0000 mW (-40.0 dBm)
    Lane 9 Rx power: 0.0000 mW (-40.0 dBm)

    Total Tx power : 0.0000 mW (-40.0 dBm)
    Total Rx power : 0.0000 mW (-40.0 dBm)



PCS
  Previous PCS Status: 
    PCS Rx Link Status was UP
    PCS Rx Link was Block Locked
    PCS BER (Sync Header Error) Counts: 0
    PCS BER (BIP) Counts: 0
    PCS BER (BIP) 1 second count: 0 (BER < 10e-9)
    PCS SD-BER Alarm was OFF
    PCS SF-BER Alarm was OFF
  Current PCS Status: 
    PCS Rx Link Status is UP
    PCS Rx Link is Block Locked
    PCS BER (Sync Header Error) Counts: 0
    PCS BER (BIP) Counts: 0
    PCS BER (BIP) 1 second count: 0 (BER < 10e-9)
    PCS SD-BER Alarm is OFF
    PCS SF-BER Alarm is OFF

PCS detailed information:

  RX Service Interface Lane Sync Header Lock Status:

    Lane 0 : Locked
    Lane 1 : Locked
    Lane 2 : Locked
    Lane 3 : Locked
    Lane 4 : Locked
    Lane 5 : Locked
    Lane 6 : Locked
    Lane 7 : Locked
    Lane 8 : Locked
    Lane 9 : Locked

  Mapping of Service Interface Lane and RX PCS Lane:

    Rx Service Interface Lane 0  = PCS Lane 0
    Rx Service Interface Lane 1  = PCS Lane 1
    Rx Service Interface Lane 2  = PCS Lane 2
    Rx Service Interface Lane 3  = PCS Lane 3
    Rx Service Interface Lane 4  = PCS Lane 4
    Rx Service Interface Lane 5  = PCS Lane 5
    Rx Service Interface Lane 6  = PCS Lane 6
    Rx Service Interface Lane 7  = PCS Lane 7
    Rx Service Interface Lane 8  = PCS Lane 8
    Rx Service Interface Lane 9  = PCS Lane 9

  PCS Lane BIP Error Counters:

             Even sublane     Odd sublane
    Lane 0 : 0                0               
    Lane 1 : 0                0               
    Lane 2 : 0                0               
    Lane 3 : 0                0               
    Lane 4 : 0                0               
    Lane 5 : 0                0               
    Lane 6 : 0                0               
    Lane 7 : 0                0               
    Lane 8 : 0                0               
    Lane 9 : 0                0               

  Total PCS Lane BIP Error Count          : 0
  Total PCS Lane Sync Header Error Count  : 0
  Total PCS Lane Bad 64/66 Code Count     : 0

 General Info:
=================


PMA/PMD:
========
  Previous Alarm Status:
      PMA/PMD Rx Link is Up.
      LR4 Ability
      SR10 Ability
  Current Alarm Status:
      PMA/PMD Rx Link is Up.
      LR4 Ability
      SR10 Ability

CPAK section:
=============

Quack check: PASSED

CPAK General Information:

  Module Identifier:         CPAK_10x10G
  Ethernet Application Code: 100GBASE-SR10
  Module State:              Ready
  Power Class:               1
  Maximum Power Consumption: 4600 mW

CPAK Vendor Information:

  Vendor Name:         CISCO           
  Vendor PN:           800-41495-01    
  Vendor SN:           FBN19092110     
  Vendor OUI:          0x0-0x0-0xc
  Lot Code:            
  DATE CODE(YYYY/MM/DD): 2015/03/05
  CPAK MSA Hardware Version:   11.0
  CPAK MSA MDIO Version:       9.0
  Vendor Hardware Version:    0.5
  Vendor Firmware Version:    2.3

CPAK UDI Information:

  UDI Compliant: Yes
  Cisco PID: CPAK-100G-SR10  
  Cisco VID: V01 

CPAK Cisco Information:

  Vendor Name: CISCO           
  Cisco PN   : 800-41495-01  Rev B0  
  Cisco SN   : FBN19092110
 
CPAK Detail Information:

  Number of lanes supported: 

    Number of network lanes: 10
    Number of host lanes   : 10

  Time required by module: 

    Maximum high-power-up time:   1 s
    Maximum high-power-down time:   1 s
    Maximum tx-turn-on time   :   1 s

    Maximum tx-turn-off time    : 254 ms

  Module general control: 

    Soft reset asserted     : No
    Soft low power asserted : No
    Soft tx disable asserted: No
    Soft program control 3 asserted: No
    Soft program control 2 asserted: No
    Soft program control 1 asserted: No
    Soft global alarm test asserted: No

    Tx disable pin asserted: No
    Low power pin asserted : No
    Program control 3 pin asserted: No
    Program control 2 pin asserted: No
    Program control 1 pin asserted: No

  Module Analog A/D value: 

    Power supply voltage : 3.2991 V
    Temperature          : 27.4602 degC

  Network lane A/D value: 

    Lane 0 Tx power: 0.5472 mW ( -2.6 dBm)
    Lane 1 Tx power: 0.5253 mW ( -2.8 dBm)
    Lane 2 Tx power: 0.5102 mW ( -2.9 dBm)
    Lane 3 Tx power: 0.5327 mW ( -2.7 dBm)
    Lane 4 Tx power: 0.4866 mW ( -3.1 dBm)
    Lane 5 Tx power: 0.5129 mW ( -2.9 dBm)
    Lane 6 Tx power: 0.5129 mW ( -2.9 dBm)
    Lane 7 Tx power: 0.5416 mW ( -2.7 dBm)
    Lane 8 Tx power: 0.5111 mW ( -2.9 dBm)
    Lane 9 Tx power: 0.5343 mW ( -2.7 dBm)

    Lane 0 Rx power: 0.5251 mW ( -2.8 dBm)
    Lane 1 Rx power: 0.5345 mW ( -2.7 dBm)
    Lane 2 Rx power: 0.5865 mW ( -2.3 dBm)
    Lane 3 Rx power: 0.4876 mW ( -3.1 dBm)
    Lane 4 Rx power: 0.4308 mW ( -3.7 dBm)
    Lane 5 Rx power: 0.5249 mW ( -2.8 dBm)
    Lane 6 Rx power: 0.5047 mW ( -3.0 dBm)
    Lane 7 Rx power: 0.4419 mW ( -3.5 dBm)
    Lane 8 Rx power: 0.5576 mW ( -2.5 dBm)
    Lane 9 Rx power: 0.4585 mW ( -3.4 dBm)

    Total Tx power : 5.2148 mW (  7.2 dBm)
    Total Rx power : 5.0521 mW (  7.0 dBm)



PCS
  Previous PCS Status: 
    PCS Rx Link Status was UP
    PCS Rx Link was Block Locked
    PCS BER (Sync Header Error) Counts: 0
    PCS BER (BIP) Counts: 0
    PCS BER (BIP) 1 second count: 0 (BER < 10e-9)
    PCS SD-BER Alarm was OFF
    PCS SF-BER Alarm was OFF
  Current PCS Status: 
    PCS Rx Link Status is UP
    PCS Rx Link is Block Locked
    PCS BER (Sync Header Error) Counts: 0
    PCS BER (BIP) Counts: 0
    PCS BER (BIP) 1 second count: 0 (BER < 10e-9)
    PCS SD-BER Alarm is OFF
    PCS SF-BER Alarm is OFF

PCS detailed information:

  RX Service Interface Lane Sync Header Lock Status:

    Lane 0 : Locked
    Lane 1 : Locked
    Lane 2 : Locked
    Lane 3 : Locked
    Lane 4 : Locked
    Lane 5 : Locked
    Lane 6 : Locked
    Lane 7 : Locked
    Lane 8 : Locked
    Lane 9 : Locked

  Mapping of Service Interface Lane and RX PCS Lane:

    Rx Service Interface Lane 0  = PCS Lane 0
    Rx Service Interface Lane 1  = PCS Lane 1
    Rx Service Interface Lane 2  = PCS Lane 2
    Rx Service Interface Lane 3  = PCS Lane 3
    Rx Service Interface Lane 4  = PCS Lane 4
    Rx Service Interface Lane 5  = PCS Lane 5
    Rx Service Interface Lane 6  = PCS Lane 6
    Rx Service Interface Lane 7  = PCS Lane 7
    Rx Service Interface Lane 8  = PCS Lane 8
    Rx Service Interface Lane 9  = PCS Lane 9

  PCS Lane BIP Error Counters:

             Even sublane     Odd sublane
    Lane 0 : 0                0               
    Lane 1 : 0                0               
    Lane 2 : 0                0               
    Lane 3 : 0                0               
    Lane 4 : 0                0               
    Lane 5 : 0                0               
    Lane 6 : 0                0               
    Lane 7 : 0                0               
    Lane 8 : 0                0               
    Lane 9 : 0                0               

  Total PCS Lane BIP Error Count          : 0
  Total PCS Lane Sync Header Error Count  : 0
  Total PCS Lane Bad 64/66 Code Count     : 0
 
 General Info:
=================


PMA/PMD:
========
  Previous Alarm Status:
      PMA/PMD Rx Link is Up.
      LR4 Ability
      SR10 Ability
  Current Alarm Status:
      PMA/PMD Rx Link is Up.
      LR4 Ability
      SR10 Ability

CPAK section:
=============

Quack check: PASSED
 
CPAK General Information:

  Module Identifier:         CPAK_10x10G
  Ethernet Application Code: 100GBASE-SR10
  Module State:              Ready
  Power Class:               1
  Maximum Power Consumption: 4600 mW

CPAK Vendor Information:

  Vendor Name:         CISCO           
  Vendor PN:           800-41495-01    
  Vendor SN:           FBN19092111     
  Vendor OUI:          0x0-0x0-0xc
  Lot Code:            
  DATE CODE(YYYY/MM/DD): 2015/03/05
  CPAK MSA Hardware Version:   11.0
  CPAK MSA MDIO Version:       9.0
  Vendor Hardware Version:    0.5
  Vendor Firmware Version:    2.3

CPAK UDI Information:

  UDI Compliant: Yes
  Cisco PID: CPAK-100G-SR10  
  Cisco VID: V01 

CPAK Cisco Information:

  Vendor Name: CISCO           
  Cisco PN   : 800-41495-01  Rev B0  
  Cisco SN   : FBN19092111

CPAK Detail Information:

  Number of lanes supported: 

    Number of network lanes: 10
    Number of host lanes   : 10

  Time required by module: 

    Maximum high-power-up time:   1 s
    Maximum high-power-down time:   1 s
    Maximum tx-turn-on time   :   1 s

    Maximum tx-turn-off time    : 254 ms

  Module general control: 

    Soft reset asserted     : No
    Soft low power asserted : No
    Soft tx disable asserted: No
    Soft program control 3 asserted: No
    Soft program control 2 asserted: No
    Soft program control 1 asserted: No
    Soft global alarm test asserted: No

    Tx disable pin asserted: No
    Low power pin asserted : No
    Program control 3 pin asserted: No
    Program control 2 pin asserted: No
    Program control 1 pin asserted: No

  Module Analog A/D value: 

    Power supply voltage : 3.2942 V
    Temperature          : 25.8307 degC

  Network lane A/D value: 

    Lane 0 Tx power: 0.5391 mW ( -2.7 dBm)
    Lane 1 Tx power: 0.4846 mW ( -3.1 dBm)
    Lane 2 Tx power: 0.5342 mW ( -2.7 dBm)
    Lane 3 Tx power: 0.5034 mW ( -3.0 dBm)
    Lane 4 Tx power: 0.5094 mW ( -2.9 dBm)
    Lane 5 Tx power: 0.4753 mW ( -3.2 dBm)
    Lane 6 Tx power: 0.5212 mW ( -2.8 dBm)
    Lane 7 Tx power: 0.4953 mW ( -3.1 dBm)
    Lane 8 Tx power: 0.5488 mW ( -2.6 dBm)
    Lane 9 Tx power: 0.4941 mW ( -3.1 dBm)

    Lane 0 Rx power: 0.5597 mW ( -2.5 dBm)
    Lane 1 Rx power: 0.5674 mW ( -2.5 dBm)
    Lane 2 Rx power: 0.5755 mW ( -2.4 dBm)
    Lane 3 Rx power: 0.5692 mW ( -2.4 dBm)
    Lane 4 Rx power: 0.6046 mW ( -2.2 dBm)
    Lane 5 Rx power: 0.5960 mW ( -2.2 dBm)
    Lane 6 Rx power: 0.6081 mW ( -2.2 dBm)
    Lane 7 Rx power: 0.5935 mW ( -2.3 dBm)
    Lane 8 Rx power: 0.6121 mW ( -2.1 dBm)
    Lane 9 Rx power: 0.5941 mW ( -2.3 dBm)

    Total Tx power : 5.1054 mW (  7.1 dBm)
    Total Rx power : 5.8802 mW (  7.7 dBm)



PCS
  Previous PCS Status: 
    PCS Rx Link Status was UP
    PCS Rx Link was Block Locked
    PCS BER (Sync Header Error) Counts: 0
    PCS BER (BIP) Counts: 0
    PCS BER (BIP) 1 second count: 0 (BER < 10e-9)
    PCS SD-BER Alarm was OFF
    PCS SF-BER Alarm was OFF
  Current PCS Status: 
    PCS Rx Link Status is UP
    PCS Rx Link is Block Locked
    PCS BER (Sync Header Error) Counts: 0
    PCS BER (BIP) Counts: 0
    PCS BER (BIP) 1 second count: 0 (BER < 10e-9)
    PCS SD-BER Alarm is OFF
    PCS SF-BER Alarm is OFF

PCS detailed information:

  RX Service Interface Lane Sync Header Lock Status:

    Lane 0 : Locked
    Lane 1 : Locked
    Lane 2 : Locked
    Lane 3 : Locked
    Lane 4 : Locked
    Lane 5 : Locked
    Lane 6 : Locked
    Lane 7 : Locked
    Lane 8 : Locked
    Lane 9 : Locked

  Mapping of Service Interface Lane and RX PCS Lane:

    Rx Service Interface Lane 0  = PCS Lane 0
    Rx Service Interface Lane 1  = PCS Lane 1
    Rx Service Interface Lane 2  = PCS Lane 2
    Rx Service Interface Lane 3  = PCS Lane 3
    Rx Service Interface Lane 4  = PCS Lane 4
    Rx Service Interface Lane 5  = PCS Lane 5
    Rx Service Interface Lane 6  = PCS Lane 6
    Rx Service Interface Lane 7  = PCS Lane 7
    Rx Service Interface Lane 8  = PCS Lane 8
    Rx Service Interface Lane 9  = PCS Lane 9

  PCS Lane BIP Error Counters:

             Even sublane     Odd sublane
    Lane 0 : 0                0               
    Lane 1 : 0                0               
    Lane 2 : 0                0               
    Lane 3 : 0                0               
    Lane 4 : 0                0               
    Lane 5 : 0                0               
    Lane 6 : 0                0               
    Lane 7 : 0                0               
    Lane 8 : 0                0               
    Lane 9 : 0                0               

  Total PCS Lane BIP Error Count          : 0
  Total PCS Lane Sync Header Error Count  : 0
  Total PCS Lane Bad 64/66 Code Count     : 0

 General Info:
=================


PMA/PMD:
========
  Previous Alarm Status:
      PMA/PMD Rx Link is Up.
      LR4 Ability
      SR10 Ability
  Current Alarm Status:
      PMA/PMD Rx Link is Up.
      LR4 Ability
      SR10 Ability

CPAK section:
=============
 
Quack check: PASSED

CPAK General Information:

  Module Identifier:         CPAK_10x10G
  Ethernet Application Code: 100GBASE-SR10
  Module State:              Ready
  Power Class:               1
  Maximum Power Consumption: 4600 mW

CPAK Vendor Information:

  Vendor Name:         CISCO           
  Vendor PN:           800-41495-01    
  Vendor SN:           FBN19122025     
  Vendor OUI:          0x0-0x0-0xc
  Lot Code:            
  DATE CODE(YYYY/MM/DD): 2015/03/19
  CPAK MSA Hardware Version:   11.0
  CPAK MSA MDIO Version:       9.0
  Vendor Hardware Version:    0.5
  Vendor Firmware Version:    2.3

CPAK UDI Information:

  UDI Compliant: Yes
  Cisco PID: CPAK-100G-SR10  
  Cisco VID: V01 

CPAK Cisco Information:

  Vendor Name: CISCO           
  Cisco PN   : 800-41495-01  Rev B0  
  Cisco SN   : FBN19122025
 
CPAK Detail Information:

  Number of lanes supported: 

    Number of network lanes: 10
    Number of host lanes   : 10

  Time required by module: 

    Maximum high-power-up time:   1 s
    Maximum high-power-down time:   1 s
    Maximum tx-turn-on time   :   1 s

    Maximum tx-turn-off time    : 254 ms

  Module general control: 

    Soft reset asserted     : No
    Soft low power asserted : No
    Soft tx disable asserted: No
    Soft program control 3 asserted: No
    Soft program control 2 asserted: No
    Soft program control 1 asserted: No
    Soft global alarm test asserted: No

    Tx disable pin asserted: No
    Low power pin asserted : No
    Program control 3 pin asserted: No
    Program control 2 pin asserted: No
    Program control 1 pin asserted: No

  Module Analog A/D value: 

    Power supply voltage : 3.3028 V
    Temperature          : 25.4212 degC

  Network lane A/D value: 

    Lane 0 Tx power: 0.5831 mW ( -2.3 dBm)
    Lane 1 Tx power: 0.5871 mW ( -2.3 dBm)
    Lane 2 Tx power: 0.5774 mW ( -2.4 dBm)
    Lane 3 Tx power: 0.6008 mW ( -2.2 dBm)
    Lane 4 Tx power: 0.5457 mW ( -2.6 dBm)
    Lane 5 Tx power: 0.5611 mW ( -2.5 dBm)
    Lane 6 Tx power: 0.5296 mW ( -2.8 dBm)
    Lane 7 Tx power: 0.5524 mW ( -2.6 dBm)
    Lane 8 Tx power: 0.5542 mW ( -2.6 dBm)
    Lane 9 Tx power: 0.5349 mW ( -2.7 dBm)

    Lane 0 Rx power: 0.4432 mW ( -3.5 dBm)
    Lane 1 Rx power: 0.6225 mW ( -2.1 dBm)
    Lane 2 Rx power: 0.6431 mW ( -1.9 dBm)
    Lane 3 Rx power: 0.6172 mW ( -2.1 dBm)
    Lane 4 Rx power: 0.4315 mW ( -3.7 dBm)
    Lane 5 Rx power: 0.5563 mW ( -2.5 dBm)
    Lane 6 Rx power: 0.5017 mW ( -3.0 dBm)
    Lane 7 Rx power: 0.4878 mW ( -3.1 dBm)
    Lane 8 Rx power: 0.5729 mW ( -2.4 dBm)
    Lane 9 Rx power: 0.5421 mW ( -2.7 dBm)

    Total Tx power : 5.6263 mW (  7.5 dBm)
    Total Rx power : 5.4183 mW (  7.3 dBm)



PCS
  Previous PCS Status: 
    PCS Rx Link Status was DOWN
    PCS Rx Link was NOT Block Locked
    PCS BER (Sync Header Error) Counts: 0
    PCS BER (BIP) Counts: 0
    PCS BER (BIP) 1 second count: 0 (BER < 10e-9)
    PCS SD-BER Alarm was OFF
    PCS SF-BER Alarm was OFF
  Current PCS Status: 
    PCS Rx Link Status is DOWN
    PCS Rx Link is NOT Block Locked
    PCS BER (Sync Header Error) Counts: 0
    PCS BER (BIP) Counts: 0
    PCS BER (BIP) 1 second count: 0 (BER < 10e-9)
    PCS SD-BER Alarm is OFF
    PCS SF-BER Alarm is OFF

PCS detailed information:

  RX Service Interface Lane Sync Header Lock Status:

    Lane 0 : Not Locked
    Lane 1 : Not Locked
    Lane 2 : Not Locked
    Lane 3 : Not Locked
    Lane 4 : Not Locked
    Lane 5 : Not Locked
    Lane 6 : Not Locked
    Lane 7 : Not Locked
    Lane 8 : Not Locked
    Lane 9 : Not Locked

  Mapping of Service Interface Lane and RX PCS Lane:

    Rx Service Interface Lane 0  = PCS Lane 0
    Rx Service Interface Lane 1  = PCS Lane 1
    Rx Service Interface Lane 2  = PCS Lane 2
    Rx Service Interface Lane 3  = PCS Lane 3
    Rx Service Interface Lane 4  = PCS Lane 4
    Rx Service Interface Lane 5  = PCS Lane 5
    Rx Service Interface Lane 6  = PCS Lane 6
    Rx Service Interface Lane 7  = PCS Lane 7
    Rx Service Interface Lane 8  = PCS Lane 8
    Rx Service Interface Lane 9  = PCS Lane 9

  PCS Lane BIP Error Counters:

             Even sublane     Odd sublane
    Lane 0 : 0                0               
    Lane 1 : 0                0               
    Lane 2 : 0                0               
    Lane 3 : 0                0               
    Lane 4 : 0                0               
    Lane 5 : 0                0               
    Lane 6 : 0                0               
    Lane 7 : 0                0               
    Lane 8 : 0                0               
    Lane 9 : 0                0               

  Total PCS Lane BIP Error Count          : 0
  Total PCS Lane Sync Header Error Count  : 0
  Total PCS Lane Bad 64/66 Code Count     : 0

 General Info:
=================


PMA/PMD:
========
  Previous Alarm Status:
      PMA/PMD Rx Link is Down.
      PMA/PMD Local Fault
      LR4 Ability
      SR10 Ability
      Rx Local Fault
  Current Alarm Status:
      PMA/PMD Rx Link is Down.
      PMA/PMD Local Fault
      LR4 Ability
      SR10 Ability
      Rx Local Fault

CPAK section:
=============

Quack check: PASSED

CPAK General Information:

  Module Identifier:         CPAK_10x10G
  Ethernet Application Code: 100GBASE-SR10
  Module State:              TX Off
  Power Class:               1
  Maximum Power Consumption: 4600 mW

CPAK Vendor Information:

  Vendor Name:         CISCO           
  Vendor PN:           800-41495-01    
  Vendor SN:           FBN19122022     
  Vendor OUI:          0x0-0x0-0xc
  Lot Code:            
  DATE CODE(YYYY/MM/DD): 2015/03/19
  CPAK MSA Hardware Version:   11.0
  CPAK MSA MDIO Version:       9.0
  Vendor Hardware Version:    0.5
  Vendor Firmware Version:    2.3

CPAK UDI Information:

  UDI Compliant: Yes
  Cisco PID: CPAK-100G-SR10  
  Cisco VID: V01 

CPAK Cisco Information:

  Vendor Name: CISCO           
  Cisco PN   : 800-41495-01  Rev B0  
  Cisco SN   : FBN19122022

CPAK Detail Information:

  Number of lanes supported: 

    Number of network lanes: 10
    Number of host lanes   : 10

  Time required by module: 

    Maximum high-power-up time:   1 s
    Maximum high-power-down time:   1 s
    Maximum tx-turn-on time   :   1 s

    Maximum tx-turn-off time    : 254 ms

  Module general control: 

    Soft reset asserted     : No
    Soft low power asserted : No
    Soft tx disable asserted: Yes
    Soft program control 3 asserted: No
    Soft program control 2 asserted: No
    Soft program control 1 asserted: No
    Soft global alarm test asserted: No

    Tx disable pin asserted: No
    Low power pin asserted : No
    Program control 3 pin asserted: No
    Program control 2 pin asserted: No
    Program control 1 pin asserted: No

  Module Analog A/D value: 

    Power supply voltage : 3.2832 V
    Temperature          : 21.2223 degC

  Network lane A/D value: 

    Lane 0 Tx power: 0.0000 mW (-40.0 dBm)
    Lane 1 Tx power: 0.0000 mW (-40.0 dBm)
    Lane 2 Tx power: 0.0000 mW (-40.0 dBm)
    Lane 3 Tx power: 0.0000 mW (-40.0 dBm)
    Lane 4 Tx power: 0.0000 mW (-40.0 dBm)
    Lane 5 Tx power: 0.0000 mW (-40.0 dBm)
    Lane 6 Tx power: 0.0000 mW (-40.0 dBm)
    Lane 7 Tx power: 0.0000 mW (-40.0 dBm)
    Lane 8 Tx power: 0.0000 mW (-40.0 dBm)
    Lane 9 Tx power: 0.0000 mW (-40.0 dBm)

    Lane 0 Rx power: 0.0000 mW (-40.0 dBm)
    Lane 1 Rx power: 0.0000 mW (-40.0 dBm)
    Lane 2 Rx power: 0.0000 mW (-40.0 dBm)
    Lane 3 Rx power: 0.0000 mW (-40.0 dBm)
    Lane 4 Rx power: 0.0000 mW (-40.0 dBm)
    Lane 5 Rx power: 0.0000 mW (-40.0 dBm)
    Lane 6 Rx power: 0.0000 mW (-40.0 dBm)
    Lane 7 Rx power: 0.0000 mW (-40.0 dBm)
    Lane 8 Rx power: 0.0000 mW (-40.0 dBm)
    Lane 9 Rx power: 0.0000 mW (-40.0 dBm)

    Total Tx power : 0.0000 mW (-40.0 dBm)
    Total Rx power : 0.0000 mW (-40.0 dBm)


No XGXS present

No XGXS present

 No XGXS present

No XGXS present

No XGXS present

No XGXS present

 No XGXS present

No XGXS present

Regs Info
OTN Controller 0 common register:
 
TOP_MPIF Block : 
---------------------------
Addr     Name                            Value
0x00002  GLOBAL_CFG                      0x0051
0x00004  SCRATCH_PAD1                    0x001e
0x00005  SCRATCH_PAD2                    0x2800
0x00009  GPIO_CONTROL                    0x0000

SDS_COMMON Block : BANK B
---------------------------
Addr     Name                            Value
0x0241f  RXLOCKD0_INTSTATUS 3            0x0008
0x02445  RXLOCKD1_INTSTATUS 3            0x0008
0x0246b  RXLOCKD2_INTSTATUS 3            0x0008
0x02491  RXLOCKD3_INTSTATUS 3            0x0008
0x024b9  TXLOCKD0_INTSTATUS 3            0x0008
0x0281f  RXLOCKD0_INTSTATUS 4            0x0008
0x02845  RXLOCKD1_INTSTATUS 4            0x0008
0x0286b  RXLOCKD2_INTSTATUS 4            0x0008
0x02891  RXLOCKD3_INTSTATUS 4            0x004d
0x028b9  TXLOCKD0_INTSTATUS 4            0x0008

SDS_COMMON Block : BANK C
---------------------------
Addr     Name                            Value
0x0301f  RXLOCKD0_INTSTATUS 6            0x0049
0x03045  RXLOCKD1_INTSTATUS 6            0x0049
0x0306b  RXLOCKD2_INTSTATUS 6            0x0049
0x03091  RXLOCKD3_INTSTATUS 6            0x0049
0x030b9  TXLOCKD0_INTSTATUS 6            0x0049
0x0341f  RXLOCKD0_INTSTATUS 7            0x0049
0x03445  RXLOCKD1_INTSTATUS 7            0x0049
0x0346b  RXLOCKD2_INTSTATUS 7            0x0049
0x03491  RXLOCKD3_INTSTATUS 7            0x0049
0x034b9  TXLOCKD0_INTSTATUS 7            0x0049

ILKN_CORE Block : 
---------------------------
Addr     Name                            Value
0x19d6b  RX_INTERLAKEN_STATUS0           0x0049
0x19d6c  RX_INTERLAKEN_SYNCED1           0x0049
0x19d6d  RX_INTERLAKEN_SYNCED0           0x0049
0x19d66  RX_OOBFC_RX_LANE_STATUS1        0x0049
0x19d67  RX_OOBFC_RX_LANE_STATUS0        0x0049
0x19d62  TX_INTERLAKEN_STATUS1           0x0049
0x19d63  TX_INTERLAKEN_STATUS0           0x0049

Port/0 register:

SDS_COMMON Block : line
---------------------------
Addr     Name                            Value
0x0181f  RXLOCKD0_INTSTATUS 0            0x0049
0x01845  RXLOCKD1_INTSTATUS 0            0x0049
0x0186b  RXLOCKD2_INTSTATUS 0            0x0049
0x01891  RXLOCKD3_INTSTATUS 0            0x0049
0x018b9  TXLOCKD0_INTSTATUS 0            0x0049

CPAK Registers:
 ================

NVR 1 Registers:

(Reg 0x8000=0x01) (Reg 0x8001=0x21) (Reg 0x8002=0x09) (Reg 0x8003=0x03) 
(Reg 0x8004=0x00) (Reg 0x8005=0x00) (Reg 0x8006=0x00) (Reg 0x8007=0x00) 
(Reg 0x8008=0x1e) (Reg 0x8009=0xaa) (Reg 0x800a=0x4a) (Reg 0x800b=0x38) 
(Reg 0x800c=0x38) (Reg 0x800d=0x00) (Reg 0x800e=0x0a) (Reg 0x800f=0x00) 
(Reg 0x8010=0x0a) (Reg 0x8011=0x01) (Reg 0x8012=0x83) (Reg 0x8013=0x40) 
(Reg 0x8014=0x86) (Reg 0x8015=0x60) (Reg 0x8016=0x00) (Reg 0x8017=0x00) 
 (Reg 0x8018=0x00) (Reg 0x8019=0x04) (Reg 0x801a=0x40) (Reg 0x801b=0x50) 
(Reg 0x801c=0x26) (Reg 0x801d=0x17) (Reg 0x801e=0x14) (Reg 0x801f=0x46) 
(Reg 0x8020=0x00) (Reg 0x8021=0x43) (Reg 0x8022=0x49) (Reg 0x8023=0x53) 
(Reg 0x8024=0x43) (Reg 0x8025=0x4f) (Reg 0x8026=0x20) (Reg 0x8027=0x20) 
(Reg 0x8028=0x20) (Reg 0x8029=0x20) (Reg 0x802a=0x20) (Reg 0x802b=0x20) 
(Reg 0x802c=0x20) (Reg 0x802d=0x20) (Reg 0x802e=0x20) (Reg 0x802f=0x20) 
(Reg 0x8030=0x20) (Reg 0x8031=0x00) (Reg 0x8032=0x00) (Reg 0x8033=0x0c) 
(Reg 0x8034=0x38) (Reg 0x8035=0x30) (Reg 0x8036=0x30) (Reg 0x8037=0x2d) 
(Reg 0x8038=0x34) (Reg 0x8039=0x31) (Reg 0x803a=0x34) (Reg 0x803b=0x39) 
(Reg 0x803c=0x35) (Reg 0x803d=0x2d) (Reg 0x803e=0x30) (Reg 0x803f=0x31) 
 (Reg 0x8040=0x20) (Reg 0x8041=0x20) (Reg 0x8042=0x20) (Reg 0x8043=0x20) 
(Reg 0x8044=0x46) (Reg 0x8045=0x42) (Reg 0x8046=0x4e) (Reg 0x8047=0x31) 
(Reg 0x8048=0x39) (Reg 0x8049=0x31) (Reg 0x804a=0x32) (Reg 0x804b=0x32) 
(Reg 0x804c=0x30) (Reg 0x804d=0x31) (Reg 0x804e=0x37) (Reg 0x804f=0x20) 
(Reg 0x8050=0x20) (Reg 0x8051=0x20) (Reg 0x8052=0x20) (Reg 0x8053=0x20) 
(Reg 0x8054=0x32) (Reg 0x8055=0x30) (Reg 0x8056=0x31) (Reg 0x8057=0x35) 
(Reg 0x8058=0x30) (Reg 0x8059=0x33) (Reg 0x805a=0x32) (Reg 0x805b=0x30) 
(Reg 0x805c=0x00) (Reg 0x805d=0x00) (Reg 0x805e=0x57) (Reg 0x805f=0x4f) 
(Reg 0x8060=0x54) (Reg 0x8061=0x52) (Reg 0x8062=0x43) (Reg 0x8063=0x35) 
(Reg 0x8064=0x50) (Reg 0x8065=0x42) (Reg 0x8066=0x41) (Reg 0x8067=0x41) 
 (Reg 0x8068=0x6e) (Reg 0x8069=0x5a) (Reg 0x806a=0x00) (Reg 0x806b=0x05) 
(Reg 0x806c=0x02) (Reg 0x806d=0x03) (Reg 0x806e=0x0c) (Reg 0x806f=0x03) 
(Reg 0x8070=0x0f) (Reg 0x8071=0x20) (Reg 0x8072=0x01) (Reg 0x8073=0x01) 
(Reg 0x8074=0x08) (Reg 0x8075=0x00) (Reg 0x8076=0xfe) (Reg 0x8077=0x01) 
(Reg 0x8078=0x00) (Reg 0x8079=0x00) (Reg 0x807a=0x00) (Reg 0x807b=0x02) 
(Reg 0x807c=0x03) (Reg 0x807d=0x00) (Reg 0x807e=0x00) (Reg 0x807f=0xe0) 

NVR 2 Registers:

(Reg 0x8080=0x4b) (Reg 0x8081=0x00) (Reg 0x8082=0x46) (Reg 0x8083=0x00) 
(Reg 0x8084=0x00) (Reg 0x8085=0x00) (Reg 0x8086=0xfb) (Reg 0x8087=0x00) 
(Reg 0x8088=0x8a) (Reg 0x8089=0x00) (Reg 0x808a=0x87) (Reg 0x808b=0x5a) 
(Reg 0x808c=0x7a) (Reg 0x808d=0x76) (Reg 0x808e=0x77) (Reg 0x808f=0xe2) 
(Reg 0x8090=0x00) (Reg 0x8091=0x00) (Reg 0x8092=0x00) (Reg 0x8093=0x00) 
(Reg 0x8094=0x00) (Reg 0x8095=0x00) (Reg 0x8096=0x00) (Reg 0x8097=0x00) 
(Reg 0x8098=0x00) (Reg 0x8099=0x00) (Reg 0x809a=0x00) (Reg 0x809b=0x00) 
 (Reg 0x809c=0x00) (Reg 0x809d=0x00) (Reg 0x809e=0x00) (Reg 0x809f=0x00) 
(Reg 0x80a0=0x00) (Reg 0x80a1=0x00) (Reg 0x80a2=0x00) (Reg 0x80a3=0x00) 
(Reg 0x80a4=0x00) (Reg 0x80a5=0x00) (Reg 0x80a6=0x00) (Reg 0x80a7=0x00) 
(Reg 0x80a8=0x13) (Reg 0x80a9=0x88) (Reg 0x80aa=0x11) (Reg 0x80ab=0x94) 
(Reg 0x80ac=0x05) (Reg 0x80ad=0xdc) (Reg 0x80ae=0x03) (Reg 0x80af=0xe8) 
(Reg 0x80b0=0x45) (Reg 0x80b1=0x76) (Reg 0x80b2=0x22) (Reg 0x80b3=0xd0) 
(Reg 0x80b4=0x06) (Reg 0x80b5=0xc9) (Reg 0x80b6=0x03) (Reg 0x80b7=0x66) 
(Reg 0x80b8=0x5a) (Reg 0x80b9=0x00) (Reg 0x80ba=0x55) (Reg 0x80bb=0x00) 
(Reg 0x80bc=0x00) (Reg 0x80bd=0x00) (Reg 0x80be=0xfb) (Reg 0x80bf=0x00) 
(Reg 0x80c0=0x88) (Reg 0x80c1=0x71) (Reg 0x80c2=0x43) (Reg 0x80c3=0xe2) 
 (Reg 0x80c4=0x04) (Reg 0x80c5=0x62) (Reg 0x80c6=0x02) (Reg 0x80c7=0x32) 
(Reg 0x80c8=0x00) (Reg 0x80c9=0x00) (Reg 0x80ca=0x00) (Reg 0x80cb=0x00) 
(Reg 0x80cc=0x00) (Reg 0x80cd=0x00) (Reg 0x80ce=0x00) (Reg 0x80cf=0x00) 
(Reg 0x80d0=0x00) (Reg 0x80d1=0x00) (Reg 0x80d2=0x00) (Reg 0x80d3=0x00) 
(Reg 0x80d4=0x00) (Reg 0x80d5=0x00) (Reg 0x80d6=0x00) (Reg 0x80d7=0x00) 
(Reg 0x80d8=0x00) (Reg 0x80d9=0x00) (Reg 0x80da=0x00) (Reg 0x80db=0x00) 
(Reg 0x80dc=0x00) (Reg 0x80dd=0x00) (Reg 0x80de=0x00) (Reg 0x80df=0x00) 
(Reg 0x80e0=0x00) (Reg 0x80e1=0x00) (Reg 0x80e2=0x00) (Reg 0x80e3=0x00) 
(Reg 0x80e4=0x00) (Reg 0x80e5=0x00) (Reg 0x80e6=0x00) (Reg 0x80e7=0x00) 
(Reg 0x80e8=0x00) (Reg 0x80e9=0x00) (Reg 0x80ea=0x00) (Reg 0x80eb=0x00) 
 (Reg 0x80ec=0x00) (Reg 0x80ed=0x00) (Reg 0x80ee=0x00) (Reg 0x80ef=0x00) 
(Reg 0x80f0=0x00) (Reg 0x80f1=0x00) (Reg 0x80f2=0x00) (Reg 0x80f3=0x00) 
(Reg 0x80f4=0x00) (Reg 0x80f5=0x00) (Reg 0x80f6=0x00) (Reg 0x80f7=0x00) 
(Reg 0x80f8=0x00) (Reg 0x80f9=0x00) (Reg 0x80fa=0x00) (Reg 0x80fb=0x00) 
(Reg 0x80fc=0x00) (Reg 0x80fd=0x00) (Reg 0x80fe=0x00) (Reg 0x80ff=0x93) 

NVR 3 Registers:

(Reg 0x8100=0x00) (Reg 0x8101=0x00) (Reg 0x8102=0x00) (Reg 0x8103=0x00) 
(Reg 0x8104=0x00) (Reg 0x8105=0x00) (Reg 0x8106=0x00) (Reg 0x8107=0x00) 
(Reg 0x8108=0x00) (Reg 0x8109=0x00) (Reg 0x810a=0x00) (Reg 0x810b=0x00) 
(Reg 0x810c=0x00) (Reg 0x810d=0x00) (Reg 0x810e=0x00) (Reg 0x810f=0x00) 
(Reg 0x8110=0x00) (Reg 0x8111=0x00) (Reg 0x8112=0x00) (Reg 0x8113=0x00) 
(Reg 0x8114=0x00) (Reg 0x8115=0x00) (Reg 0x8116=0x00) (Reg 0x8117=0x00) 
(Reg 0x8118=0x00) (Reg 0x8119=0x00) (Reg 0x811a=0x00) (Reg 0x811b=0x00) 
(Reg 0x811c=0x00) (Reg 0x811d=0x00) (Reg 0x811e=0x00) (Reg 0x811f=0x00) 
 (Reg 0x8120=0x00) (Reg 0x8121=0x00) (Reg 0x8122=0x00) (Reg 0x8123=0x00) 
(Reg 0x8124=0x00) (Reg 0x8125=0x00) (Reg 0x8126=0x00) (Reg 0x8127=0x00) 
(Reg 0x8128=0x00) (Reg 0x8129=0x00) (Reg 0x812a=0x00) (Reg 0x812b=0x00) 
(Reg 0x812c=0x00) (Reg 0x812d=0x00) (Reg 0x812e=0x00) (Reg 0x812f=0x00) 
(Reg 0x8130=0x00) (Reg 0x8131=0x00) (Reg 0x8132=0x00) (Reg 0x8133=0x00) 
(Reg 0x8134=0x00) (Reg 0x8135=0x00) (Reg 0x8136=0x00) (Reg 0x8137=0x00) 
(Reg 0x8138=0x00) (Reg 0x8139=0x00) (Reg 0x813a=0x00) (Reg 0x813b=0x00) 
(Reg 0x813c=0x00) (Reg 0x813d=0x00) (Reg 0x813e=0x00) (Reg 0x813f=0x00) 
(Reg 0x8140=0x00) (Reg 0x8141=0x00) (Reg 0x8142=0x00) (Reg 0x8143=0x00) 
(Reg 0x8144=0x00) (Reg 0x8145=0x00) (Reg 0x8146=0x00) (Reg 0x8147=0x00) 
 (Reg 0x8148=0x00) (Reg 0x8149=0x00) (Reg 0x814a=0x00) (Reg 0x814b=0x00) 
(Reg 0x814c=0x00) (Reg 0x814d=0x00) (Reg 0x814e=0x00) (Reg 0x814f=0x00) 
(Reg 0x8150=0x00) (Reg 0x8151=0x00) (Reg 0x8152=0x00) (Reg 0x8153=0x00) 
(Reg 0x8154=0x00) (Reg 0x8155=0x00) (Reg 0x8156=0x00) (Reg 0x8157=0x00) 
(Reg 0x8158=0x00) (Reg 0x8159=0x00) (Reg 0x815a=0x00) (Reg 0x815b=0x00) 
(Reg 0x815c=0x00) (Reg 0x815d=0x00) (Reg 0x815e=0x00) (Reg 0x815f=0x00) 
(Reg 0x8160=0x00) (Reg 0x8161=0x00) (Reg 0x8162=0x00) (Reg 0x8163=0x00) 
(Reg 0x8164=0x00) (Reg 0x8165=0x00) (Reg 0x8166=0x00) (Reg 0x8167=0x00) 
(Reg 0x8168=0x00) (Reg 0x8169=0x00) (Reg 0x816a=0x00) (Reg 0x816b=0x00) 
(Reg 0x816c=0x00) (Reg 0x816d=0x00) (Reg 0x816e=0x00) (Reg 0x816f=0x00) 
 (Reg 0x8170=0x00) (Reg 0x8171=0x00) (Reg 0x8172=0x00) (Reg 0x8173=0x00) 
(Reg 0x8174=0x00) (Reg 0x8175=0x00) (Reg 0x8176=0x00) (Reg 0x8177=0x00) 
(Reg 0x8178=0x00) (Reg 0x8179=0x00) (Reg 0x817a=0x00) (Reg 0x817b=0x00) 
(Reg 0x817c=0x00) (Reg 0x817d=0x00) (Reg 0x817e=0x00) (Reg 0x817f=0x00) 

NVR 4 Registers:

(Reg 0x8180=0x00) 

VR 1 Registers:

(Reg 0xa000=0x0000) (Reg 0xa001=0x1234) (Reg 0xa002=0x0000) (Reg 0xa003=0x0000) 
(Reg 0xa004=0x0000) (Reg 0xa005=0x0000) (Reg 0xa006=0x0000) (Reg 0xa007=0x0000) 
(Reg 0xa008=0x0000) (Reg 0xa009=0x0000) (Reg 0xa00a=0x0000) (Reg 0xa00b=0x0000) 
(Reg 0xa00c=0x0000) (Reg 0xa00d=0x0000) (Reg 0xa00e=0x0000) (Reg 0xa00f=0x0000) 
(Reg 0xa010=0x0000) (Reg 0xa011=0x0200) (Reg 0xa012=0x0200) (Reg 0xa013=0x0000) 
(Reg 0xa014=0x0000) (Reg 0xa015=0x0000) (Reg 0xa016=0x0020) (Reg 0xa017=0x0000) 
(Reg 0xa018=0x0000) (Reg 0xa019=0x0000) (Reg 0xa01a=0x0000) (Reg 0xa01b=0x0000) 
(Reg 0xa01c=0x8000) (Reg 0xa01d=0x0002) (Reg 0xa01e=0x0000) (Reg 0xa01f=0x0000) 
(Reg 0xa020=0x0000) (Reg 0xa021=0x0000) (Reg 0xa022=0x0000) (Reg 0xa023=0x0000) 
(Reg 0xa024=0x0000) (Reg 0xa025=0x0000) (Reg 0xa026=0x0000) (Reg 0xa027=0x0000) 
(Reg 0xa028=0x006a) (Reg 0xa029=0xa7f8) (Reg 0xa02a=0x0062) (Reg 0xa02b=0x0ff0) 
(Reg 0xa02c=0x00f0) (Reg 0xa02d=0x0000) (Reg 0xa02e=0x0000) (Reg 0xa02f=0x1bde) 
(Reg 0xa030=0x8110) (Reg 0xa031=0x0000) (Reg 0xa032=0x65bb) (Reg 0xa033=0x30b2) 
(Reg 0xa034=0x0000) (Reg 0xa035=0x0000) (Reg 0xa036=0x0000) (Reg 0xa037=0x0000) 
(Reg 0xa038=0x0000) (Reg 0xa039=0x0000) (Reg 0xa03a=0x0000) 

NETWORK LANE VR 1 Registers:

(Reg 0xa200=0x0000) (Reg 0xa201=0x0000) (Reg 0xa202=0x0000) (Reg 0xa203=0x0000) 
(Reg 0xa204=0x0000) (Reg 0xa205=0x0000) (Reg 0xa206=0x0000) (Reg 0xa207=0x0000) 
(Reg 0xa208=0x0000) (Reg 0xa209=0x0000) (Reg 0xa20a=0x0000) (Reg 0xa20b=0x0000) 
(Reg 0xa20c=0x0000) (Reg 0xa20d=0x0000) (Reg 0xa20e=0x0000) (Reg 0xa20f=0x0000) 
(Reg 0xa210=0x0000) (Reg 0xa211=0x0000) (Reg 0xa212=0x0000) (Reg 0xa213=0x0000) 
(Reg 0xa214=0x0000) (Reg 0xa215=0x0000) (Reg 0xa216=0x0000) (Reg 0xa217=0x0000) 
(Reg 0xa218=0x0000) (Reg 0xa219=0x0000) (Reg 0xa21a=0x0000) (Reg 0xa21b=0x0000) 
(Reg 0xa21c=0x0000) (Reg 0xa21d=0x0000) (Reg 0xa21e=0x0000) (Reg 0xa21f=0x0000) 
(Reg 0xa220=0x0000) (Reg 0xa221=0x0000) (Reg 0xa222=0x0000) (Reg 0xa223=0x0000) 
(Reg 0xa224=0x0000) (Reg 0xa225=0x0000) (Reg 0xa226=0x0000) (Reg 0xa227=0x0000) 
(Reg 0xa228=0x0000) (Reg 0xa229=0x0000) (Reg 0xa22a=0x0000) (Reg 0xa22b=0x0000) 
(Reg 0xa22c=0x0000) (Reg 0xa22d=0x0000) (Reg 0xa22e=0x0000) (Reg 0xa22f=0x0000) 
(Reg 0xa230=0x0000) (Reg 0xa231=0x0000) (Reg 0xa232=0x0000) (Reg 0xa233=0x0000) 
(Reg 0xa234=0x0000) (Reg 0xa235=0x0000) (Reg 0xa236=0x0000) (Reg 0xa237=0x0000) 
(Reg 0xa238=0x0000) (Reg 0xa239=0x0000) (Reg 0xa23a=0x0000) (Reg 0xa23b=0x0000) 
(Reg 0xa23c=0x0000) (Reg 0xa23d=0x0000) (Reg 0xa23e=0x0000) (Reg 0xa23f=0x0000) 
(Reg 0xa240=0xffff) (Reg 0xa241=0xffff) (Reg 0xa242=0xffff) (Reg 0xa243=0xffff) 
(Reg 0xa244=0xffff) (Reg 0xa245=0xffff) (Reg 0xa246=0xffff) (Reg 0xa247=0xffff) 
(Reg 0xa248=0xffff) (Reg 0xa249=0xffff) (Reg 0xa24a=0x0000) (Reg 0xa24b=0x0000) 
(Reg 0xa24c=0x0000) (Reg 0xa24d=0x0000) (Reg 0xa24e=0x0000) (Reg 0xa24f=0x0000) 
(Reg 0xa250=0xe0dc) (Reg 0xa251=0xe0dc) (Reg 0xa252=0xe0dc) (Reg 0xa253=0xe0dc) 
(Reg 0xa254=0xe0dc) (Reg 0xa255=0xe0dc) (Reg 0xa256=0xe0dc) (Reg 0xa257=0xe0dc) 
(Reg 0xa258=0xe0dc) (Reg 0xa259=0xe0dc) (Reg 0xa25a=0x0000) (Reg 0xa25b=0x0000) 
(Reg 0xa25c=0x0000) (Reg 0xa25d=0x0000) (Reg 0xa25e=0x0000) (Reg 0xa25f=0x0000) 
(Reg 0xa260=0x0000) 

NETWORK LANE VR 2 Registers:

(Reg 0xa280=0x0000) (Reg 0xa281=0x0000) (Reg 0xa282=0x0000) (Reg 0xa283=0x0000) 
(Reg 0xa284=0x0000) (Reg 0xa285=0x0000) (Reg 0xa286=0x0000) (Reg 0xa287=0x0000) 
(Reg 0xa288=0x0000) (Reg 0xa289=0x0000) (Reg 0xa28a=0x0000) (Reg 0xa28b=0x0000) 
(Reg 0xa28c=0x0000) (Reg 0xa28d=0x0000) (Reg 0xa28e=0x0000) (Reg 0xa28f=0x0000) 
(Reg 0xa290=0x0000) (Reg 0xa291=0x0000) (Reg 0xa292=0x0000) (Reg 0xa293=0x0000) 
(Reg 0xa294=0x0000) (Reg 0xa295=0x0000) (Reg 0xa296=0x0000) (Reg 0xa297=0x0000) 
(Reg 0xa298=0x0000) (Reg 0xa299=0x0000) (Reg 0xa29a=0x0000) (Reg 0xa29b=0x0000) 
(Reg 0xa29c=0x0000) (Reg 0xa29d=0x0000) (Reg 0xa29e=0x0000) (Reg 0xa29f=0x0000) 
(Reg 0xa2a0=0x0bc3) (Reg 0xa2a1=0x0c10) (Reg 0xa2a2=0x0bb5) (Reg 0xa2a3=0x0bdc) 
(Reg 0xa2a4=0x0b8f) (Reg 0xa2a5=0x0bd9) (Reg 0xa2a6=0x0bf8) (Reg 0xa2a7=0x0b76) 
(Reg 0xa2a8=0x0bd9) (Reg 0xa2a9=0x0b0d) (Reg 0xa2aa=0x0000) (Reg 0xa2ab=0x0000) 
(Reg 0xa2ac=0x0000) (Reg 0xa2ad=0x0000) (Reg 0xa2ae=0x0000) (Reg 0xa2af=0x0000) 
(Reg 0xa2b0=0x1543) (Reg 0xa2b1=0x165c) (Reg 0xa2b2=0x1494) (Reg 0xa2b3=0x15fb) 
(Reg 0xa2b4=0x15c2) (Reg 0xa2b5=0x17c5) (Reg 0xa2b6=0x16d2) (Reg 0xa2b7=0x1728) 
(Reg 0xa2b8=0x16cf) (Reg 0xa2b9=0x17ce) (Reg 0xa2ba=0x0000) (Reg 0xa2bb=0x0000) 
(Reg 0xa2bc=0x0000) (Reg 0xa2bd=0x0000) (Reg 0xa2be=0x0000) (Reg 0xa2bf=0x0000) 
(Reg 0xa2c0=0x22de) (Reg 0xa2c1=0x22de) (Reg 0xa2c2=0x22de) (Reg 0xa2c3=0x22de) 
(Reg 0xa2c4=0x22de) (Reg 0xa2c5=0x22de) (Reg 0xa2c6=0x22de) (Reg 0xa2c7=0x22de) 
(Reg 0xa2c8=0x22de) (Reg 0xa2c9=0x22de) (Reg 0xa2ca=0x0000) (Reg 0xa2cb=0x0000) 
(Reg 0xa2cc=0x0000) (Reg 0xa2cd=0x0000) (Reg 0xa2ce=0x0000) (Reg 0xa2cf=0x0000) 
(Reg 0xa2d0=0x1615) (Reg 0xa2d1=0x1698) (Reg 0xa2d2=0x175d) (Reg 0xa2d3=0x1565) 
(Reg 0xa2d4=0x11b1) (Reg 0xa2d5=0x13e9) (Reg 0xa2d6=0x138e) (Reg 0xa2d7=0x1228) 
(Reg 0xa2d8=0x15c1) (Reg 0xa2d9=0x140c) (Reg 0xa2da=0x0000) (Reg 0xa2db=0x0000) 
(Reg 0xa2dc=0x0000) (Reg 0xa2dd=0x0000) (Reg 0xa2de=0x0000) (Reg 0xa2df=0x0000) 
(Reg 0xa2e0=0x0000) 

HOST LANE VR 1 Registers:

(Reg 0xa400=0x0000) (Reg 0xa401=0x0000) (Reg 0xa402=0x0000) (Reg 0xa403=0x0000) 
(Reg 0xa404=0x0000) (Reg 0xa405=0x0000) (Reg 0xa406=0x0000) (Reg 0xa407=0x0000) 
(Reg 0xa408=0x0000) (Reg 0xa409=0x0000) (Reg 0xa40a=0x0000) (Reg 0xa40b=0x0000) 
(Reg 0xa40c=0x0000) (Reg 0xa40d=0x0000) (Reg 0xa40e=0x0000) (Reg 0xa40f=0x0000) 
(Reg 0xa410=0x0000) (Reg 0xa411=0x0000) (Reg 0xa412=0x0000) (Reg 0xa413=0x0000) 
(Reg 0xa414=0x0000) (Reg 0xa415=0x0000) (Reg 0xa416=0x0000) (Reg 0xa417=0x0000) 
(Reg 0xa418=0x0000) (Reg 0xa419=0x0000) (Reg 0xa41a=0x0000) (Reg 0xa41b=0x0000) 
(Reg 0xa41c=0x0000) (Reg 0xa41d=0x0000) (Reg 0xa41e=0x0000) (Reg 0xa41f=0x0000) 
(Reg 0xa420=0x0001) (Reg 0xa421=0x0001) (Reg 0xa422=0x0001) (Reg 0xa423=0x0001) 
(Reg 0xa424=0x0001) (Reg 0xa425=0x0001) (Reg 0xa426=0x0001) (Reg 0xa427=0x0001) 
(Reg 0xa428=0x0001) (Reg 0xa429=0x0001) (Reg 0xa42a=0x0000) (Reg 0xa42b=0x0000) 
(Reg 0xa42c=0x0000) (Reg 0xa42d=0x0000) (Reg 0xa42e=0x0000) (Reg 0xa42f=0x0000) 
(Reg 0xa430=0x0000) (Reg 0xa431=0x0000) (Reg 0xa432=0x0000) (Reg 0xa433=0x0000) 
(Reg 0xa434=0x0000) (Reg 0xa435=0x0000) (Reg 0xa436=0x0000) (Reg 0xa437=0x0000) 
(Reg 0xa438=0x0000) (Reg 0xa439=0x0000) (Reg 0xa43a=0x0000) (Reg 0xa43b=0x0000) 
(Reg 0xa43c=0x0000) (Reg 0xa43d=0x0000) (Reg 0xa43e=0x0000) (Reg 0xa43f=0x0000) 
(Reg 0xa440=0x0007) (Reg 0xa441=0x0007) (Reg 0xa442=0x0007) (Reg 0xa443=0x0007) 
(Reg 0xa444=0x0007) (Reg 0xa445=0x0007) (Reg 0xa446=0x0007) (Reg 0xa447=0x0007) 
(Reg 0xa448=0x0007) (Reg 0xa449=0x0007) (Reg 0xa44a=0x0000) (Reg 0xa44b=0x0000) 
(Reg 0xa44c=0x0000) (Reg 0xa44d=0x0000) (Reg 0xa44e=0x0000) (Reg 0xa44f=0x0000) 
(Reg 0xa450=0x0000) 

Regs Info
OTN Controller 1 common register:

TOP_MPIF Block : 
---------------------------
Addr     Name                            Value
0x00002  GLOBAL_CFG                      0x0051
0x00004  SCRATCH_PAD1                    0x00ef
0x00005  SCRATCH_PAD2                    0x8d00
0x00009  GPIO_CONTROL                    0x0000
 
SDS_COMMON Block : BANK B
---------------------------
Addr     Name                            Value
0x0241f  RXLOCKD0_INTSTATUS 3            0x0008
0x02445  RXLOCKD1_INTSTATUS 3            0x0000
0x0246b  RXLOCKD2_INTSTATUS 3            0x0008
0x02491  RXLOCKD3_INTSTATUS 3            0x0008
0x024b9  TXLOCKD0_INTSTATUS 3            0x0008
0x0281f  RXLOCKD0_INTSTATUS 4            0x0000
0x02845  RXLOCKD1_INTSTATUS 4            0x0008
0x0286b  RXLOCKD2_INTSTATUS 4            0x0008
0x02891  RXLOCKD3_INTSTATUS 4            0x0000
0x028b9  TXLOCKD0_INTSTATUS 4            0x0008

SDS_COMMON Block : BANK C
---------------------------
Addr     Name                            Value
0x0301f  RXLOCKD0_INTSTATUS 6            0x0049
0x03045  RXLOCKD1_INTSTATUS 6            0x0049
0x0306b  RXLOCKD2_INTSTATUS 6            0x0049
0x03091  RXLOCKD3_INTSTATUS 6            0x0049
0x030b9  TXLOCKD0_INTSTATUS 6            0x0049
0x0341f  RXLOCKD0_INTSTATUS 7            0x0049
0x03445  RXLOCKD1_INTSTATUS 7            0x0049
0x0346b  RXLOCKD2_INTSTATUS 7            0x0049
0x03491  RXLOCKD3_INTSTATUS 7            0x0049
0x034b9  TXLOCKD0_INTSTATUS 7            0x0049

ILKN_CORE Block : 
---------------------------
Addr     Name                            Value
0x19d6b  RX_INTERLAKEN_STATUS0           0x0049
0x19d6c  RX_INTERLAKEN_SYNCED1           0x0049
0x19d6d  RX_INTERLAKEN_SYNCED0           0x0049
0x19d66  RX_OOBFC_RX_LANE_STATUS1        0x0049
0x19d67  RX_OOBFC_RX_LANE_STATUS0        0x0049
0x19d62  TX_INTERLAKEN_STATUS1           0x0049
0x19d63  TX_INTERLAKEN_STATUS0           0x0049

Port/1 register:

SDS_COMMON Block : line
---------------------------
Addr     Name                            Value
0x0181f  RXLOCKD0_INTSTATUS 0            0x0049
0x01845  RXLOCKD1_INTSTATUS 0            0x0049
0x0186b  RXLOCKD2_INTSTATUS 0            0x0049
0x01891  RXLOCKD3_INTSTATUS 0            0x0049
0x018b9  TXLOCKD0_INTSTATUS 0            0x0049

CPAK Registers:
================
 
NVR 1 Registers:

(Reg 0x8000=0x01) (Reg 0x8001=0x21) (Reg 0x8002=0x09) (Reg 0x8003=0x03) 
(Reg 0x8004=0x00) (Reg 0x8005=0x00) (Reg 0x8006=0x00) (Reg 0x8007=0x00) 
(Reg 0x8008=0x1e) (Reg 0x8009=0xaa) (Reg 0x800a=0x4a) (Reg 0x800b=0x38) 
(Reg 0x800c=0x38) (Reg 0x800d=0x00) (Reg 0x800e=0x0a) (Reg 0x800f=0x00) 
 (Reg 0x8010=0x0a) (Reg 0x8011=0x01) (Reg 0x8012=0x83) (Reg 0x8013=0x40) 
(Reg 0x8014=0x86) (Reg 0x8015=0x60) (Reg 0x8016=0x00) (Reg 0x8017=0x00) 
(Reg 0x8018=0x00) (Reg 0x8019=0x04) (Reg 0x801a=0x40) (Reg 0x801b=0x50) 
(Reg 0x801c=0x26) (Reg 0x801d=0x17) (Reg 0x801e=0x14) (Reg 0x801f=0x46) 
(Reg 0x8020=0x00) (Reg 0x8021=0x43) (Reg 0x8022=0x49) (Reg 0x8023=0x53) 
(Reg 0x8024=0x43) (Reg 0x8025=0x4f) (Reg 0x8026=0x20) (Reg 0x8027=0x20) 
(Reg 0x8028=0x20) (Reg 0x8029=0x20) (Reg 0x802a=0x20) (Reg 0x802b=0x20) 
(Reg 0x802c=0x20) (Reg 0x802d=0x20) (Reg 0x802e=0x20) (Reg 0x802f=0x20) 
(Reg 0x8030=0x20) (Reg 0x8031=0x00) (Reg 0x8032=0x00) (Reg 0x8033=0x0c) 
(Reg 0x8034=0x38) (Reg 0x8035=0x30) (Reg 0x8036=0x30) (Reg 0x8037=0x2d) 
 (Reg 0x8038=0x34) (Reg 0x8039=0x31) (Reg 0x803a=0x34) (Reg 0x803b=0x39) 
(Reg 0x803c=0x35) (Reg 0x803d=0x2d) (Reg 0x803e=0x30) (Reg 0x803f=0x31) 
(Reg 0x8040=0x20) (Reg 0x8041=0x20) (Reg 0x8042=0x20) (Reg 0x8043=0x20) 
(Reg 0x8044=0x46) (Reg 0x8045=0x42) (Reg 0x8046=0x4e) (Reg 0x8047=0x31) 
(Reg 0x8048=0x39) (Reg 0x8049=0x30) (Reg 0x804a=0x39) (Reg 0x804b=0x32) 
(Reg 0x804c=0x31) (Reg 0x804d=0x30) (Reg 0x804e=0x39) (Reg 0x804f=0x20) 
(Reg 0x8050=0x20) (Reg 0x8051=0x20) (Reg 0x8052=0x20) (Reg 0x8053=0x20) 
(Reg 0x8054=0x32) (Reg 0x8055=0x30) (Reg 0x8056=0x31) (Reg 0x8057=0x35) 
(Reg 0x8058=0x30) (Reg 0x8059=0x33) (Reg 0x805a=0x30) (Reg 0x805b=0x35) 
(Reg 0x805c=0x00) (Reg 0x805d=0x00) (Reg 0x805e=0x57) (Reg 0x805f=0x4f) 
 (Reg 0x8060=0x54) (Reg 0x8061=0x52) (Reg 0x8062=0x43) (Reg 0x8063=0x35) 
(Reg 0x8064=0x50) (Reg 0x8065=0x42) (Reg 0x8066=0x41) (Reg 0x8067=0x41) 
(Reg 0x8068=0x6e) (Reg 0x8069=0x5a) (Reg 0x806a=0x00) (Reg 0x806b=0x05) 
(Reg 0x806c=0x02) (Reg 0x806d=0x03) (Reg 0x806e=0x0c) (Reg 0x806f=0x03) 
(Reg 0x8070=0x0f) (Reg 0x8071=0x20) (Reg 0x8072=0x01) (Reg 0x8073=0x01) 
(Reg 0x8074=0x08) (Reg 0x8075=0x00) (Reg 0x8076=0xfe) (Reg 0x8077=0x01) 
(Reg 0x8078=0x00) (Reg 0x8079=0x00) (Reg 0x807a=0x00) (Reg 0x807b=0x02) 
(Reg 0x807c=0x03) (Reg 0x807d=0x00) (Reg 0x807e=0x00) (Reg 0x807f=0xeb) 

NVR 2 Registers:

(Reg 0x8080=0x4b) (Reg 0x8081=0x00) (Reg 0x8082=0x46) (Reg 0x8083=0x00) 
(Reg 0x8084=0x00) (Reg 0x8085=0x00) (Reg 0x8086=0xfb) (Reg 0x8087=0x00) 
(Reg 0x8088=0x8a) (Reg 0x8089=0x00) (Reg 0x808a=0x87) (Reg 0x808b=0x5a) 
(Reg 0x808c=0x7a) (Reg 0x808d=0x76) (Reg 0x808e=0x77) (Reg 0x808f=0xe2) 
(Reg 0x8090=0x00) (Reg 0x8091=0x00) (Reg 0x8092=0x00) (Reg 0x8093=0x00) 
 (Reg 0x8094=0x00) (Reg 0x8095=0x00) (Reg 0x8096=0x00) (Reg 0x8097=0x00) 
(Reg 0x8098=0x00) (Reg 0x8099=0x00) (Reg 0x809a=0x00) (Reg 0x809b=0x00) 
(Reg 0x809c=0x00) (Reg 0x809d=0x00) (Reg 0x809e=0x00) (Reg 0x809f=0x00) 
(Reg 0x80a0=0x00) (Reg 0x80a1=0x00) (Reg 0x80a2=0x00) (Reg 0x80a3=0x00) 
(Reg 0x80a4=0x00) (Reg 0x80a5=0x00) (Reg 0x80a6=0x00) (Reg 0x80a7=0x00) 
(Reg 0x80a8=0x13) (Reg 0x80a9=0x88) (Reg 0x80aa=0x11) (Reg 0x80ab=0x94) 
(Reg 0x80ac=0x05) (Reg 0x80ad=0xdc) (Reg 0x80ae=0x03) (Reg 0x80af=0xe8) 
(Reg 0x80b0=0x45) (Reg 0x80b1=0x76) (Reg 0x80b2=0x22) (Reg 0x80b3=0xd0) 
(Reg 0x80b4=0x06) (Reg 0x80b5=0xc9) (Reg 0x80b6=0x03) (Reg 0x80b7=0x66) 
(Reg 0x80b8=0x5a) (Reg 0x80b9=0x00) (Reg 0x80ba=0x55) (Reg 0x80bb=0x00) 
 (Reg 0x80bc=0x00) (Reg 0x80bd=0x00) (Reg 0x80be=0xfb) (Reg 0x80bf=0x00) 
(Reg 0x80c0=0x88) (Reg 0x80c1=0x71) (Reg 0x80c2=0x43) (Reg 0x80c3=0xe2) 
(Reg 0x80c4=0x04) (Reg 0x80c5=0x62) (Reg 0x80c6=0x02) (Reg 0x80c7=0x32) 
(Reg 0x80c8=0x00) (Reg 0x80c9=0x00) (Reg 0x80ca=0x00) (Reg 0x80cb=0x00) 
(Reg 0x80cc=0x00) (Reg 0x80cd=0x00) (Reg 0x80ce=0x00) (Reg 0x80cf=0x00) 
(Reg 0x80d0=0x00) (Reg 0x80d1=0x00) (Reg 0x80d2=0x00) (Reg 0x80d3=0x00) 
(Reg 0x80d4=0x00) (Reg 0x80d5=0x00) (Reg 0x80d6=0x00) (Reg 0x80d7=0x00) 
(Reg 0x80d8=0x00) (Reg 0x80d9=0x00) (Reg 0x80da=0x00) (Reg 0x80db=0x00) 
(Reg 0x80dc=0x00) (Reg 0x80dd=0x00) (Reg 0x80de=0x00) (Reg 0x80df=0x00) 
(Reg 0x80e0=0x00) (Reg 0x80e1=0x00) (Reg 0x80e2=0x00) (Reg 0x80e3=0x00) 
 (Reg 0x80e4=0x00) (Reg 0x80e5=0x00) (Reg 0x80e6=0x00) (Reg 0x80e7=0x00) 
(Reg 0x80e8=0x00) (Reg 0x80e9=0x00) (Reg 0x80ea=0x00) (Reg 0x80eb=0x00) 
(Reg 0x80ec=0x00) (Reg 0x80ed=0x00) (Reg 0x80ee=0x00) (Reg 0x80ef=0x00) 
(Reg 0x80f0=0x00) (Reg 0x80f1=0x00) (Reg 0x80f2=0x00) (Reg 0x80f3=0x00) 
(Reg 0x80f4=0x00) (Reg 0x80f5=0x00) (Reg 0x80f6=0x00) (Reg 0x80f7=0x00) 
(Reg 0x80f8=0x00) (Reg 0x80f9=0x00) (Reg 0x80fa=0x00) (Reg 0x80fb=0x00) 
(Reg 0x80fc=0x00) (Reg 0x80fd=0x00) (Reg 0x80fe=0x00) (Reg 0x80ff=0x93) 

NVR 3 Registers:

(Reg 0x8100=0x00) (Reg 0x8101=0x00) (Reg 0x8102=0x00) (Reg 0x8103=0x00) 
(Reg 0x8104=0x00) (Reg 0x8105=0x00) (Reg 0x8106=0x00) (Reg 0x8107=0x00) 
(Reg 0x8108=0x00) (Reg 0x8109=0x00) (Reg 0x810a=0x00) (Reg 0x810b=0x00) 
(Reg 0x810c=0x00) (Reg 0x810d=0x00) (Reg 0x810e=0x00) (Reg 0x810f=0x00) 
(Reg 0x8110=0x00) (Reg 0x8111=0x00) (Reg 0x8112=0x00) (Reg 0x8113=0x00) 
(Reg 0x8114=0x00) (Reg 0x8115=0x00) (Reg 0x8116=0x00) (Reg 0x8117=0x00) 
 (Reg 0x8118=0x00) (Reg 0x8119=0x00) (Reg 0x811a=0x00) (Reg 0x811b=0x00) 
(Reg 0x811c=0x00) (Reg 0x811d=0x00) (Reg 0x811e=0x00) (Reg 0x811f=0x00) 
(Reg 0x8120=0x00) (Reg 0x8121=0x00) (Reg 0x8122=0x00) (Reg 0x8123=0x00) 
(Reg 0x8124=0x00) (Reg 0x8125=0x00) (Reg 0x8126=0x00) (Reg 0x8127=0x00) 
(Reg 0x8128=0x00) (Reg 0x8129=0x00) (Reg 0x812a=0x00) (Reg 0x812b=0x00) 
(Reg 0x812c=0x00) (Reg 0x812d=0x00) (Reg 0x812e=0x00) (Reg 0x812f=0x00) 
(Reg 0x8130=0x00) (Reg 0x8131=0x00) (Reg 0x8132=0x00) (Reg 0x8133=0x00) 
(Reg 0x8134=0x00) (Reg 0x8135=0x00) (Reg 0x8136=0x00) (Reg 0x8137=0x00) 
(Reg 0x8138=0x00) (Reg 0x8139=0x00) (Reg 0x813a=0x00) (Reg 0x813b=0x00) 
(Reg 0x813c=0x00) (Reg 0x813d=0x00) (Reg 0x813e=0x00) (Reg 0x813f=0x00) 
 (Reg 0x8140=0x00) (Reg 0x8141=0x00) (Reg 0x8142=0x00) (Reg 0x8143=0x00) 
(Reg 0x8144=0x00) (Reg 0x8145=0x00) (Reg 0x8146=0x00) (Reg 0x8147=0x00) 
(Reg 0x8148=0x00) (Reg 0x8149=0x00) (Reg 0x814a=0x00) (Reg 0x814b=0x00) 
(Reg 0x814c=0x00) (Reg 0x814d=0x00) (Reg 0x814e=0x00) (Reg 0x814f=0x00) 
(Reg 0x8150=0x00) (Reg 0x8151=0x00) (Reg 0x8152=0x00) (Reg 0x8153=0x00) 
(Reg 0x8154=0x00) (Reg 0x8155=0x00) (Reg 0x8156=0x00) (Reg 0x8157=0x00) 
(Reg 0x8158=0x00) (Reg 0x8159=0x00) (Reg 0x815a=0x00) (Reg 0x815b=0x00) 
(Reg 0x815c=0x00) (Reg 0x815d=0x00) (Reg 0x815e=0x00) (Reg 0x815f=0x00) 
(Reg 0x8160=0x00) (Reg 0x8161=0x00) (Reg 0x8162=0x00) (Reg 0x8163=0x00) 
(Reg 0x8164=0x00) (Reg 0x8165=0x00) (Reg 0x8166=0x00) (Reg 0x8167=0x00) 
 (Reg 0x8168=0x00) (Reg 0x8169=0x00) (Reg 0x816a=0x00) (Reg 0x816b=0x00) 
(Reg 0x816c=0x00) (Reg 0x816d=0x00) (Reg 0x816e=0x00) (Reg 0x816f=0x00) 
(Reg 0x8170=0x00) (Reg 0x8171=0x00) (Reg 0x8172=0x00) (Reg 0x8173=0x00) 
(Reg 0x8174=0x00) (Reg 0x8175=0x00) (Reg 0x8176=0x00) (Reg 0x8177=0x00) 
(Reg 0x8178=0x00) (Reg 0x8179=0x00) (Reg 0x817a=0x00) (Reg 0x817b=0x00) 
(Reg 0x817c=0x00) (Reg 0x817d=0x00) (Reg 0x817e=0x00) (Reg 0x817f=0x00) 

NVR 4 Registers:

(Reg 0x8180=0x00) 

 VR 1 Registers:

(Reg 0xa000=0x0000) (Reg 0xa001=0x1234) (Reg 0xa002=0x0000) (Reg 0xa003=0x0000) 
(Reg 0xa004=0x0000) (Reg 0xa005=0x0000) (Reg 0xa006=0x0000) (Reg 0xa007=0x0000) 
(Reg 0xa008=0x0000) (Reg 0xa009=0x0000) (Reg 0xa00a=0x0000) (Reg 0xa00b=0x0000) 
(Reg 0xa00c=0x0000) (Reg 0xa00d=0x0000) (Reg 0xa00e=0x0000) (Reg 0xa00f=0x0000) 
(Reg 0xa010=0x0000) (Reg 0xa011=0x0200) (Reg 0xa012=0x0200) (Reg 0xa013=0x0000) 
(Reg 0xa014=0x0000) (Reg 0xa015=0x0000) (Reg 0xa016=0x0020) (Reg 0xa017=0x0000) 
(Reg 0xa018=0xb180) (Reg 0xa019=0x03ff) (Reg 0xa01a=0x01ff) (Reg 0xa01b=0x0000) 
(Reg 0xa01c=0x8000) (Reg 0xa01d=0x0002) (Reg 0xa01e=0x0000) (Reg 0xa01f=0x0000) 
(Reg 0xa020=0x0000) (Reg 0xa021=0x8000) (Reg 0xa022=0x003f) (Reg 0xa023=0x0080) 
(Reg 0xa024=0x0000) (Reg 0xa025=0x0000) (Reg 0xa026=0x0000) (Reg 0xa027=0x0000) 
(Reg 0xa028=0x006a) (Reg 0xa029=0xa7f8) (Reg 0xa02a=0x0062) (Reg 0xa02b=0x0ff0) 
(Reg 0xa02c=0x00f0) (Reg 0xa02d=0x0000) (Reg 0xa02e=0x0000) (Reg 0xa02f=0x1b6e) 
(Reg 0xa030=0x800f) (Reg 0xa031=0x0000) (Reg 0xa032=0x6511) (Reg 0xa033=0x301f) 
(Reg 0xa034=0x0000) (Reg 0xa035=0x0000) (Reg 0xa036=0x0000) (Reg 0xa037=0x0000) 
(Reg 0xa038=0x0000) (Reg 0xa039=0x0000) (Reg 0xa03a=0x0000) 

NETWORK LANE VR 1 Registers:

(Reg 0xa200=0x0000) (Reg 0xa201=0x0000) (Reg 0xa202=0x0000) (Reg 0xa203=0x0000) 
(Reg 0xa204=0x0000) (Reg 0xa205=0x0000) (Reg 0xa206=0x0000) (Reg 0xa207=0x0000) 
(Reg 0xa208=0x0000) (Reg 0xa209=0x0000) (Reg 0xa20a=0x0000) (Reg 0xa20b=0x0000) 
(Reg 0xa20c=0x0000) (Reg 0xa20d=0x0000) (Reg 0xa20e=0x0000) (Reg 0xa20f=0x0000) 
(Reg 0xa210=0x0000) (Reg 0xa211=0x0000) (Reg 0xa212=0x0000) (Reg 0xa213=0x0000) 
(Reg 0xa214=0x0000) (Reg 0xa215=0x0000) (Reg 0xa216=0x0000) (Reg 0xa217=0x0000) 
(Reg 0xa218=0x0000) (Reg 0xa219=0x0000) (Reg 0xa21a=0x0000) (Reg 0xa21b=0x0000) 
(Reg 0xa21c=0x0000) (Reg 0xa21d=0x0000) (Reg 0xa21e=0x0000) (Reg 0xa21f=0x0000) 
(Reg 0xa220=0x3300) (Reg 0xa221=0x3300) (Reg 0xa222=0x3300) (Reg 0xa223=0x3300) 
(Reg 0xa224=0x3300) (Reg 0xa225=0x3300) (Reg 0xa226=0x3300) (Reg 0xa227=0x3300) 
(Reg 0xa228=0x3300) (Reg 0xa229=0x3300) (Reg 0xa22a=0x0000) (Reg 0xa22b=0x0000) 
(Reg 0xa22c=0x0000) (Reg 0xa22d=0x0000) (Reg 0xa22e=0x0000) (Reg 0xa22f=0x0000) 
(Reg 0xa230=0x0080) (Reg 0xa231=0x0080) (Reg 0xa232=0x0080) (Reg 0xa233=0x0080) 
(Reg 0xa234=0x0080) (Reg 0xa235=0x0080) (Reg 0xa236=0x0080) (Reg 0xa237=0x0080) 
(Reg 0xa238=0x0080) (Reg 0xa239=0x0000) (Reg 0xa23a=0x0000) (Reg 0xa23b=0x0000) 
(Reg 0xa23c=0x0000) (Reg 0xa23d=0x0000) (Reg 0xa23e=0x0000) (Reg 0xa23f=0x0000) 
(Reg 0xa240=0xffff) (Reg 0xa241=0xffff) (Reg 0xa242=0xffff) (Reg 0xa243=0xffff) 
(Reg 0xa244=0xffff) (Reg 0xa245=0xffff) (Reg 0xa246=0xffff) (Reg 0xa247=0xffff) 
(Reg 0xa248=0xffff) (Reg 0xa249=0xffff) (Reg 0xa24a=0x0000) (Reg 0xa24b=0x0000) 
(Reg 0xa24c=0x0000) (Reg 0xa24d=0x0000) (Reg 0xa24e=0x0000) (Reg 0xa24f=0x0000) 
(Reg 0xa250=0xe0dc) (Reg 0xa251=0xe0dc) (Reg 0xa252=0xe0dc) (Reg 0xa253=0xe0dc) 
(Reg 0xa254=0xe0dc) (Reg 0xa255=0xe0dc) (Reg 0xa256=0xe0dc) (Reg 0xa257=0xe0dc) 
(Reg 0xa258=0xe0dc) (Reg 0xa259=0xe0dc) (Reg 0xa25a=0x0000) (Reg 0xa25b=0x0000) 
(Reg 0xa25c=0x0000) (Reg 0xa25d=0x0000) (Reg 0xa25e=0x0000) (Reg 0xa25f=0x0000) 
(Reg 0xa260=0x0000) 

NETWORK LANE VR 2 Registers:

(Reg 0xa280=0x0000) (Reg 0xa281=0x0000) (Reg 0xa282=0x0000) (Reg 0xa283=0x0000) 
(Reg 0xa284=0x0000) (Reg 0xa285=0x0000) (Reg 0xa286=0x0000) (Reg 0xa287=0x0000) 
(Reg 0xa288=0x0000) (Reg 0xa289=0x0000) (Reg 0xa28a=0x0000) (Reg 0xa28b=0x0000) 
(Reg 0xa28c=0x0000) (Reg 0xa28d=0x0000) (Reg 0xa28e=0x0000) (Reg 0xa28f=0x0000) 
(Reg 0xa290=0x0000) (Reg 0xa291=0x0000) (Reg 0xa292=0x0000) (Reg 0xa293=0x0000) 
(Reg 0xa294=0x0000) (Reg 0xa295=0x0000) (Reg 0xa296=0x0000) (Reg 0xa297=0x0000) 
(Reg 0xa298=0x0000) (Reg 0xa299=0x0000) (Reg 0xa29a=0x0000) (Reg 0xa29b=0x0000) 
(Reg 0xa29c=0x0000) (Reg 0xa29d=0x0000) (Reg 0xa29e=0x0000) (Reg 0xa29f=0x0000) 
(Reg 0xa2a0=0x0b75) (Reg 0xa2a1=0x0b6e) (Reg 0xa2a2=0x0ba9) (Reg 0xa2a3=0x0ba7) 
(Reg 0xa2a4=0x0bdd) (Reg 0xa2a5=0x0b37) (Reg 0xa2a6=0x0bdd) (Reg 0xa2a7=0x0b87) 
(Reg 0xa2a8=0x0b90) (Reg 0xa2a9=0x0b62) (Reg 0xa2aa=0x0000) (Reg 0xa2ab=0x0000) 
(Reg 0xa2ac=0x0000) (Reg 0xa2ad=0x0000) (Reg 0xa2ae=0x0000) (Reg 0xa2af=0x0000) 
(Reg 0xa2b0=0x1466) (Reg 0xa2b1=0x1293) (Reg 0xa2b2=0x12f1) (Reg 0xa2b3=0x1244) 
(Reg 0xa2b4=0x12d5) (Reg 0xa2b5=0x134f) (Reg 0xa2b6=0x13de) (Reg 0xa2b7=0x12f5) 
(Reg 0xa2b8=0x13c4) (Reg 0xa2b9=0x12f0) (Reg 0xa2ba=0x0000) (Reg 0xa2bb=0x0000) 
(Reg 0xa2bc=0x0000) (Reg 0xa2bd=0x0000) (Reg 0xa2be=0x0000) (Reg 0xa2bf=0x0000) 
(Reg 0xa2c0=0x226e) (Reg 0xa2c1=0x226e) (Reg 0xa2c2=0x226e) (Reg 0xa2c3=0x226e) 
(Reg 0xa2c4=0x226e) (Reg 0xa2c5=0x226e) (Reg 0xa2c6=0x226e) (Reg 0xa2c7=0x226e) 
(Reg 0xa2c8=0x226e) (Reg 0xa2c9=0x226e) (Reg 0xa2ca=0x0000) (Reg 0xa2cb=0x0000) 
(Reg 0xa2cc=0x0000) (Reg 0xa2cd=0x0000) (Reg 0xa2ce=0x0000) (Reg 0xa2cf=0x0000) 
(Reg 0xa2d0=0x1589) (Reg 0xa2d1=0x1782) (Reg 0xa2d2=0x182f) (Reg 0xa2d3=0x155a) 
(Reg 0xa2d4=0x1776) (Reg 0xa2d5=0x15c9) (Reg 0xa2d6=0x15fe) (Reg 0xa2d7=0x1714) 
(Reg 0xa2d8=0x1873) (Reg 0xa2d9=0x17e9) (Reg 0xa2da=0x0000) (Reg 0xa2db=0x0000) 
(Reg 0xa2dc=0x0000) (Reg 0xa2dd=0x0000) (Reg 0xa2de=0x0000) (Reg 0xa2df=0x0000) 
(Reg 0xa2e0=0x0000) 

HOST LANE VR 1 Registers:

 (Reg 0xa400=0x0000) (Reg 0xa401=0x0000) (Reg 0xa402=0x0000) (Reg 0xa403=0x0000) 
(Reg 0xa404=0x0000) (Reg 0xa405=0x0000) (Reg 0xa406=0x0000) (Reg 0xa407=0x0000) 
(Reg 0xa408=0x0000) (Reg 0xa409=0x0000) (Reg 0xa40a=0x0000) (Reg 0xa40b=0x0000) 
(Reg 0xa40c=0x0000) (Reg 0xa40d=0x0000) (Reg 0xa40e=0x0000) (Reg 0xa40f=0x0000) 
(Reg 0xa410=0x0000) (Reg 0xa411=0x0000) (Reg 0xa412=0x0000) (Reg 0xa413=0x0000) 
(Reg 0xa414=0x0000) (Reg 0xa415=0x0000) (Reg 0xa416=0x0000) (Reg 0xa417=0x0000) 
(Reg 0xa418=0x0000) (Reg 0xa419=0x0000) (Reg 0xa41a=0x0000) (Reg 0xa41b=0x0000) 
(Reg 0xa41c=0x0000) (Reg 0xa41d=0x0000) (Reg 0xa41e=0x0000) (Reg 0xa41f=0x0000) 
(Reg 0xa420=0x0001) (Reg 0xa421=0x0001) (Reg 0xa422=0x0001) (Reg 0xa423=0x0001) 
(Reg 0xa424=0x0001) (Reg 0xa425=0x0001) (Reg 0xa426=0x0001) (Reg 0xa427=0x0001) 
(Reg 0xa428=0x0001) (Reg 0xa429=0x0001) (Reg 0xa42a=0x0000) (Reg 0xa42b=0x0000) 
(Reg 0xa42c=0x0000) (Reg 0xa42d=0x0000) (Reg 0xa42e=0x0000) (Reg 0xa42f=0x0000) 
(Reg 0xa430=0x0000) (Reg 0xa431=0x0000) (Reg 0xa432=0x0000) (Reg 0xa433=0x0000) 
(Reg 0xa434=0x0000) (Reg 0xa435=0x0000) (Reg 0xa436=0x0000) (Reg 0xa437=0x0000) 
(Reg 0xa438=0x0000) (Reg 0xa439=0x0000) (Reg 0xa43a=0x0000) (Reg 0xa43b=0x0000) 
(Reg 0xa43c=0x0000) (Reg 0xa43d=0x0000) (Reg 0xa43e=0x0000) (Reg 0xa43f=0x0000) 
(Reg 0xa440=0x0007) (Reg 0xa441=0x0007) (Reg 0xa442=0x0007) (Reg 0xa443=0x0007) 
(Reg 0xa444=0x0007) (Reg 0xa445=0x0007) (Reg 0xa446=0x0007) (Reg 0xa447=0x0007) 
(Reg 0xa448=0x0007) (Reg 0xa449=0x0007) (Reg 0xa44a=0x0000) (Reg 0xa44b=0x0000) 
(Reg 0xa44c=0x0000) (Reg 0xa44d=0x0000) (Reg 0xa44e=0x0000) (Reg 0xa44f=0x0000) 
(Reg 0xa450=0x0000) 

Regs Info
OTN Controller 2 common register:

TOP_MPIF Block : 
---------------------------
Addr     Name                            Value
0x00002  GLOBAL_CFG                      0x0051
0x00004  SCRATCH_PAD1                    0x00fb
0x00005  SCRATCH_PAD2                    0xae00
0x00009  GPIO_CONTROL                    0x0000

SDS_COMMON Block : BANK B
---------------------------
Addr     Name                            Value
0x0241f  RXLOCKD0_INTSTATUS 3            0x0008
0x02445  RXLOCKD1_INTSTATUS 3            0x0008
0x0246b  RXLOCKD2_INTSTATUS 3            0x0008
0x02491  RXLOCKD3_INTSTATUS 3            0x0008
0x024b9  TXLOCKD0_INTSTATUS 3            0x0008
0x0281f  RXLOCKD0_INTSTATUS 4            0x0000
0x02845  RXLOCKD1_INTSTATUS 4            0x0008
0x0286b  RXLOCKD2_INTSTATUS 4            0x0008
0x02891  RXLOCKD3_INTSTATUS 4            0x0018
0x028b9  TXLOCKD0_INTSTATUS 4            0x000d

SDS_COMMON Block : BANK C
---------------------------
Addr     Name                            Value
0x0301f  RXLOCKD0_INTSTATUS 6            0x0049
0x03045  RXLOCKD1_INTSTATUS 6            0x0049
0x0306b  RXLOCKD2_INTSTATUS 6            0x0049
0x03091  RXLOCKD3_INTSTATUS 6            0x0049
0x030b9  TXLOCKD0_INTSTATUS 6            0x0049
0x0341f  RXLOCKD0_INTSTATUS 7            0x0049
0x03445  RXLOCKD1_INTSTATUS 7            0x0049
0x0346b  RXLOCKD2_INTSTATUS 7            0x0049
0x03491  RXLOCKD3_INTSTATUS 7            0x0049
0x034b9  TXLOCKD0_INTSTATUS 7            0x0049

ILKN_CORE Block : 
---------------------------
Addr     Name                            Value
0x19d6b  RX_INTERLAKEN_STATUS0           0x0049
0x19d6c  RX_INTERLAKEN_SYNCED1           0x0049
0x19d6d  RX_INTERLAKEN_SYNCED0           0x0049
0x19d66  RX_OOBFC_RX_LANE_STATUS1        0x0049
0x19d67  RX_OOBFC_RX_LANE_STATUS0        0x0049
0x19d62  TX_INTERLAKEN_STATUS1           0x0049
0x19d63  TX_INTERLAKEN_STATUS0           0x0049

Port/2 register:

SDS_COMMON Block : line
---------------------------
Addr     Name                            Value
0x0181f  RXLOCKD0_INTSTATUS 0            0x0049
0x01845  RXLOCKD1_INTSTATUS 0            0x0049
0x0186b  RXLOCKD2_INTSTATUS 0            0x0049
0x01891  RXLOCKD3_INTSTATUS 0            0x0049
0x018b9  TXLOCKD0_INTSTATUS 0            0x0049

CPAK Registers:
 ================

NVR 1 Registers:

(Reg 0x8000=0x01) (Reg 0x8001=0x21) (Reg 0x8002=0x09) (Reg 0x8003=0x03) 
(Reg 0x8004=0x00) (Reg 0x8005=0x00) (Reg 0x8006=0x00) (Reg 0x8007=0x00) 
(Reg 0x8008=0x1e) (Reg 0x8009=0xaa) (Reg 0x800a=0x4a) (Reg 0x800b=0x38) 
(Reg 0x800c=0x38) (Reg 0x800d=0x00) (Reg 0x800e=0x0a) (Reg 0x800f=0x00) 
(Reg 0x8010=0x0a) (Reg 0x8011=0x01) (Reg 0x8012=0x83) (Reg 0x8013=0x40) 
(Reg 0x8014=0x86) (Reg 0x8015=0x60) (Reg 0x8016=0x00) (Reg 0x8017=0x00) 
 (Reg 0x8018=0x00) (Reg 0x8019=0x04) (Reg 0x801a=0x40) (Reg 0x801b=0x50) 
(Reg 0x801c=0x26) (Reg 0x801d=0x17) (Reg 0x801e=0x14) (Reg 0x801f=0x46) 
(Reg 0x8020=0x00) (Reg 0x8021=0x43) (Reg 0x8022=0x49) (Reg 0x8023=0x53) 
(Reg 0x8024=0x43) (Reg 0x8025=0x4f) (Reg 0x8026=0x20) (Reg 0x8027=0x20) 
(Reg 0x8028=0x20) (Reg 0x8029=0x20) (Reg 0x802a=0x20) (Reg 0x802b=0x20) 
(Reg 0x802c=0x20) (Reg 0x802d=0x20) (Reg 0x802e=0x20) (Reg 0x802f=0x20) 
(Reg 0x8030=0x20) (Reg 0x8031=0x00) (Reg 0x8032=0x00) (Reg 0x8033=0x0c) 
(Reg 0x8034=0x38) (Reg 0x8035=0x30) (Reg 0x8036=0x30) (Reg 0x8037=0x2d) 
(Reg 0x8038=0x34) (Reg 0x8039=0x31) (Reg 0x803a=0x34) (Reg 0x803b=0x39) 
(Reg 0x803c=0x35) (Reg 0x803d=0x2d) (Reg 0x803e=0x30) (Reg 0x803f=0x31) 
 (Reg 0x8040=0x20) (Reg 0x8041=0x20) (Reg 0x8042=0x20) (Reg 0x8043=0x20) 
(Reg 0x8044=0x46) (Reg 0x8045=0x42) (Reg 0x8046=0x4e) (Reg 0x8047=0x31) 
(Reg 0x8048=0x39) (Reg 0x8049=0x31) (Reg 0x804a=0x32) (Reg 0x804b=0x32) 
(Reg 0x804c=0x30) (Reg 0x804d=0x31) (Reg 0x804e=0x39) (Reg 0x804f=0x20) 
(Reg 0x8050=0x20) (Reg 0x8051=0x20) (Reg 0x8052=0x20) (Reg 0x8053=0x20) 
(Reg 0x8054=0x32) (Reg 0x8055=0x30) (Reg 0x8056=0x31) (Reg 0x8057=0x35) 
(Reg 0x8058=0x30) (Reg 0x8059=0x33) (Reg 0x805a=0x31) (Reg 0x805b=0x39) 
(Reg 0x805c=0x00) (Reg 0x805d=0x00) (Reg 0x805e=0x57) (Reg 0x805f=0x4f) 
(Reg 0x8060=0x54) (Reg 0x8061=0x52) (Reg 0x8062=0x43) (Reg 0x8063=0x35) 
(Reg 0x8064=0x50) (Reg 0x8065=0x42) (Reg 0x8066=0x41) (Reg 0x8067=0x41) 
 (Reg 0x8068=0x6e) (Reg 0x8069=0x5a) (Reg 0x806a=0x00) (Reg 0x806b=0x05) 
(Reg 0x806c=0x02) (Reg 0x806d=0x03) (Reg 0x806e=0x0c) (Reg 0x806f=0x03) 
(Reg 0x8070=0x0f) (Reg 0x8071=0x20) (Reg 0x8072=0x01) (Reg 0x8073=0x01) 
(Reg 0x8074=0x08) (Reg 0x8075=0x00) (Reg 0x8076=0xfe) (Reg 0x8077=0x01) 
(Reg 0x8078=0x00) (Reg 0x8079=0x00) (Reg 0x807a=0x00) (Reg 0x807b=0x02) 
(Reg 0x807c=0x03) (Reg 0x807d=0x00) (Reg 0x807e=0x00) (Reg 0x807f=0xea) 

NVR 2 Registers:

(Reg 0x8080=0x4b) (Reg 0x8081=0x00) (Reg 0x8082=0x46) (Reg 0x8083=0x00) 
(Reg 0x8084=0x00) (Reg 0x8085=0x00) (Reg 0x8086=0xfb) (Reg 0x8087=0x00) 
(Reg 0x8088=0x8a) (Reg 0x8089=0x00) (Reg 0x808a=0x87) (Reg 0x808b=0x5a) 
(Reg 0x808c=0x7a) (Reg 0x808d=0x76) (Reg 0x808e=0x77) (Reg 0x808f=0xe2) 
(Reg 0x8090=0x00) (Reg 0x8091=0x00) (Reg 0x8092=0x00) (Reg 0x8093=0x00) 
(Reg 0x8094=0x00) (Reg 0x8095=0x00) (Reg 0x8096=0x00) (Reg 0x8097=0x00) 
(Reg 0x8098=0x00) (Reg 0x8099=0x00) (Reg 0x809a=0x00) (Reg 0x809b=0x00) 
 (Reg 0x809c=0x00) (Reg 0x809d=0x00) (Reg 0x809e=0x00) (Reg 0x809f=0x00) 
(Reg 0x80a0=0x00) (Reg 0x80a1=0x00) (Reg 0x80a2=0x00) (Reg 0x80a3=0x00) 
(Reg 0x80a4=0x00) (Reg 0x80a5=0x00) (Reg 0x80a6=0x00) (Reg 0x80a7=0x00) 
(Reg 0x80a8=0x13) (Reg 0x80a9=0x88) (Reg 0x80aa=0x11) (Reg 0x80ab=0x94) 
(Reg 0x80ac=0x05) (Reg 0x80ad=0xdc) (Reg 0x80ae=0x03) (Reg 0x80af=0xe8) 
(Reg 0x80b0=0x45) (Reg 0x80b1=0x76) (Reg 0x80b2=0x22) (Reg 0x80b3=0xd0) 
(Reg 0x80b4=0x06) (Reg 0x80b5=0xc9) (Reg 0x80b6=0x03) (Reg 0x80b7=0x66) 
(Reg 0x80b8=0x5a) (Reg 0x80b9=0x00) (Reg 0x80ba=0x55) (Reg 0x80bb=0x00) 
(Reg 0x80bc=0x00) (Reg 0x80bd=0x00) (Reg 0x80be=0xfb) (Reg 0x80bf=0x00) 
(Reg 0x80c0=0x88) (Reg 0x80c1=0x71) (Reg 0x80c2=0x43) (Reg 0x80c3=0xe2) 
 (Reg 0x80c4=0x04) (Reg 0x80c5=0x62) (Reg 0x80c6=0x02) (Reg 0x80c7=0x32) 
(Reg 0x80c8=0x00) (Reg 0x80c9=0x00) (Reg 0x80ca=0x00) (Reg 0x80cb=0x00) 
(Reg 0x80cc=0x00) (Reg 0x80cd=0x00) (Reg 0x80ce=0x00) (Reg 0x80cf=0x00) 
(Reg 0x80d0=0x00) (Reg 0x80d1=0x00) (Reg 0x80d2=0x00) (Reg 0x80d3=0x00) 
(Reg 0x80d4=0x00) (Reg 0x80d5=0x00) (Reg 0x80d6=0x00) (Reg 0x80d7=0x00) 
(Reg 0x80d8=0x00) (Reg 0x80d9=0x00) (Reg 0x80da=0x00) (Reg 0x80db=0x00) 
(Reg 0x80dc=0x00) (Reg 0x80dd=0x00) (Reg 0x80de=0x00) (Reg 0x80df=0x00) 
(Reg 0x80e0=0x00) (Reg 0x80e1=0x00) (Reg 0x80e2=0x00) (Reg 0x80e3=0x00) 
(Reg 0x80e4=0x00) (Reg 0x80e5=0x00) (Reg 0x80e6=0x00) (Reg 0x80e7=0x00) 
(Reg 0x80e8=0x00) (Reg 0x80e9=0x00) (Reg 0x80ea=0x00) (Reg 0x80eb=0x00) 
 (Reg 0x80ec=0x00) (Reg 0x80ed=0x00) (Reg 0x80ee=0x00) (Reg 0x80ef=0x00) 
(Reg 0x80f0=0x00) (Reg 0x80f1=0x00) (Reg 0x80f2=0x00) (Reg 0x80f3=0x00) 
(Reg 0x80f4=0x00) (Reg 0x80f5=0x00) (Reg 0x80f6=0x00) (Reg 0x80f7=0x00) 
(Reg 0x80f8=0x00) (Reg 0x80f9=0x00) (Reg 0x80fa=0x00) (Reg 0x80fb=0x00) 
(Reg 0x80fc=0x00) (Reg 0x80fd=0x00) (Reg 0x80fe=0x00) (Reg 0x80ff=0x93) 

NVR 3 Registers:

(Reg 0x8100=0x00) (Reg 0x8101=0x00) (Reg 0x8102=0x00) (Reg 0x8103=0x00) 
(Reg 0x8104=0x00) (Reg 0x8105=0x00) (Reg 0x8106=0x00) (Reg 0x8107=0x00) 
(Reg 0x8108=0x00) (Reg 0x8109=0x00) (Reg 0x810a=0x00) (Reg 0x810b=0x00) 
(Reg 0x810c=0x00) (Reg 0x810d=0x00) (Reg 0x810e=0x00) (Reg 0x810f=0x00) 
(Reg 0x8110=0x00) (Reg 0x8111=0x00) (Reg 0x8112=0x00) (Reg 0x8113=0x00) 
(Reg 0x8114=0x00) (Reg 0x8115=0x00) (Reg 0x8116=0x00) (Reg 0x8117=0x00) 
(Reg 0x8118=0x00) (Reg 0x8119=0x00) (Reg 0x811a=0x00) (Reg 0x811b=0x00) 
(Reg 0x811c=0x00) (Reg 0x811d=0x00) (Reg 0x811e=0x00) (Reg 0x811f=0x00) 
 (Reg 0x8120=0x00) (Reg 0x8121=0x00) (Reg 0x8122=0x00) (Reg 0x8123=0x00) 
(Reg 0x8124=0x00) (Reg 0x8125=0x00) (Reg 0x8126=0x00) (Reg 0x8127=0x00) 
(Reg 0x8128=0x00) (Reg 0x8129=0x00) (Reg 0x812a=0x00) (Reg 0x812b=0x00) 
(Reg 0x812c=0x00) (Reg 0x812d=0x00) (Reg 0x812e=0x00) (Reg 0x812f=0x00) 
(Reg 0x8130=0x00) (Reg 0x8131=0x00) (Reg 0x8132=0x00) (Reg 0x8133=0x00) 
(Reg 0x8134=0x00) (Reg 0x8135=0x00) (Reg 0x8136=0x00) (Reg 0x8137=0x00) 
(Reg 0x8138=0x00) (Reg 0x8139=0x00) (Reg 0x813a=0x00) (Reg 0x813b=0x00) 
(Reg 0x813c=0x00) (Reg 0x813d=0x00) (Reg 0x813e=0x00) (Reg 0x813f=0x00) 
(Reg 0x8140=0x00) (Reg 0x8141=0x00) (Reg 0x8142=0x00) (Reg 0x8143=0x00) 
(Reg 0x8144=0x00) (Reg 0x8145=0x00) (Reg 0x8146=0x00) (Reg 0x8147=0x00) 
 (Reg 0x8148=0x00) (Reg 0x8149=0x00) (Reg 0x814a=0x00) (Reg 0x814b=0x00) 
(Reg 0x814c=0x00) (Reg 0x814d=0x00) (Reg 0x814e=0x00) (Reg 0x814f=0x00) 
(Reg 0x8150=0x00) (Reg 0x8151=0x00) (Reg 0x8152=0x00) (Reg 0x8153=0x00) 
(Reg 0x8154=0x00) (Reg 0x8155=0x00) (Reg 0x8156=0x00) (Reg 0x8157=0x00) 
(Reg 0x8158=0x00) (Reg 0x8159=0x00) (Reg 0x815a=0x00) (Reg 0x815b=0x00) 
(Reg 0x815c=0x00) (Reg 0x815d=0x00) (Reg 0x815e=0x00) (Reg 0x815f=0x00) 
(Reg 0x8160=0x00) (Reg 0x8161=0x00) (Reg 0x8162=0x00) (Reg 0x8163=0x00) 
(Reg 0x8164=0x00) (Reg 0x8165=0x00) (Reg 0x8166=0x00) (Reg 0x8167=0x00) 
(Reg 0x8168=0x00) (Reg 0x8169=0x00) (Reg 0x816a=0x00) (Reg 0x816b=0x00) 
(Reg 0x816c=0x00) (Reg 0x816d=0x00) (Reg 0x816e=0x00) (Reg 0x816f=0x00) 
 (Reg 0x8170=0x00) (Reg 0x8171=0x00) (Reg 0x8172=0x00) (Reg 0x8173=0x00) 
(Reg 0x8174=0x00) (Reg 0x8175=0x00) (Reg 0x8176=0x00) (Reg 0x8177=0x00) 
(Reg 0x8178=0x00) (Reg 0x8179=0x00) (Reg 0x817a=0x00) (Reg 0x817b=0x00) 
(Reg 0x817c=0x00) (Reg 0x817d=0x00) (Reg 0x817e=0x00) (Reg 0x817f=0x00) 

NVR 4 Registers:

(Reg 0x8180=0x00) 

VR 1 Registers:

(Reg 0xa000=0x0000) (Reg 0xa001=0x1234) (Reg 0xa002=0x0000) (Reg 0xa003=0x0000) 
(Reg 0xa004=0x0000) (Reg 0xa005=0x0000) (Reg 0xa006=0x0000) (Reg 0xa007=0x0000) 
(Reg 0xa008=0x0000) (Reg 0xa009=0x0000) (Reg 0xa00a=0x0000) (Reg 0xa00b=0x0000) 
(Reg 0xa00c=0x0000) (Reg 0xa00d=0x0000) (Reg 0xa00e=0x0000) (Reg 0xa00f=0x0000) 
(Reg 0xa010=0x0000) (Reg 0xa011=0x0200) (Reg 0xa012=0x0200) (Reg 0xa013=0x0000) 
(Reg 0xa014=0x0000) (Reg 0xa015=0x0000) (Reg 0xa016=0x0020) (Reg 0xa017=0x0000) 
(Reg 0xa018=0xb180) (Reg 0xa019=0x03ff) (Reg 0xa01a=0x03ff) (Reg 0xa01b=0x0000) 
(Reg 0xa01c=0x8000) (Reg 0xa01d=0x0002) (Reg 0xa01e=0x0000) (Reg 0xa01f=0x0000) 
(Reg 0xa020=0x0000) (Reg 0xa021=0x8000) (Reg 0xa022=0x003f) (Reg 0xa023=0x0020) 
(Reg 0xa024=0x0000) (Reg 0xa025=0x0000) (Reg 0xa026=0x0000) (Reg 0xa027=0x0000) 
(Reg 0xa028=0x006a) (Reg 0xa029=0xa7f8) (Reg 0xa02a=0x0062) (Reg 0xa02b=0x0ff0) 
(Reg 0xa02c=0x00f0) (Reg 0xa02d=0x0000) (Reg 0xa02e=0x0000) (Reg 0xa02f=0x19d4) 
(Reg 0xa030=0x801c) (Reg 0xa031=0x0000) (Reg 0xa032=0x6572) (Reg 0xa033=0x2cd5) 
(Reg 0xa034=0x0000) (Reg 0xa035=0x0000) (Reg 0xa036=0x0000) (Reg 0xa037=0x0000) 
(Reg 0xa038=0x0000) (Reg 0xa039=0x0000) (Reg 0xa03a=0x0000) 

NETWORK LANE VR 1 Registers:

(Reg 0xa200=0x0000) (Reg 0xa201=0x0000) (Reg 0xa202=0x0000) (Reg 0xa203=0x0000) 
(Reg 0xa204=0x0000) (Reg 0xa205=0x0000) (Reg 0xa206=0x0000) (Reg 0xa207=0x0000) 
(Reg 0xa208=0x0000) (Reg 0xa209=0x0000) (Reg 0xa20a=0x0000) (Reg 0xa20b=0x0000) 
(Reg 0xa20c=0x0000) (Reg 0xa20d=0x0000) (Reg 0xa20e=0x0000) (Reg 0xa20f=0x0000) 
(Reg 0xa210=0x0000) (Reg 0xa211=0x0000) (Reg 0xa212=0x0000) (Reg 0xa213=0x0000) 
(Reg 0xa214=0x0000) (Reg 0xa215=0x0000) (Reg 0xa216=0x0000) (Reg 0xa217=0x0000) 
(Reg 0xa218=0x0000) (Reg 0xa219=0x0000) (Reg 0xa21a=0x0000) (Reg 0xa21b=0x0000) 
(Reg 0xa21c=0x0000) (Reg 0xa21d=0x0000) (Reg 0xa21e=0x0000) (Reg 0xa21f=0x0000) 
(Reg 0xa220=0x0003) (Reg 0xa221=0x0003) (Reg 0xa222=0x0003) (Reg 0xa223=0x0003) 
(Reg 0xa224=0x0003) (Reg 0xa225=0x0003) (Reg 0xa226=0x0003) (Reg 0xa227=0x0003) 
(Reg 0xa228=0x0003) (Reg 0xa229=0x0003) (Reg 0xa22a=0x0000) (Reg 0xa22b=0x0000) 
(Reg 0xa22c=0x0000) (Reg 0xa22d=0x0000) (Reg 0xa22e=0x0000) (Reg 0xa22f=0x0000) 
(Reg 0xa230=0x0010) (Reg 0xa231=0x0010) (Reg 0xa232=0x0010) (Reg 0xa233=0x0010) 
(Reg 0xa234=0x0010) (Reg 0xa235=0x0010) (Reg 0xa236=0x0010) (Reg 0xa237=0x0010) 
(Reg 0xa238=0x0010) (Reg 0xa239=0x0010) (Reg 0xa23a=0x0000) (Reg 0xa23b=0x0000) 
(Reg 0xa23c=0x0000) (Reg 0xa23d=0x0000) (Reg 0xa23e=0x0000) (Reg 0xa23f=0x0000) 
(Reg 0xa240=0xffff) (Reg 0xa241=0xffff) (Reg 0xa242=0xffff) (Reg 0xa243=0xffff) 
(Reg 0xa244=0xffff) (Reg 0xa245=0xffff) (Reg 0xa246=0xffff) (Reg 0xa247=0xffff) 
(Reg 0xa248=0xffff) (Reg 0xa249=0xffff) (Reg 0xa24a=0x0000) (Reg 0xa24b=0x0000) 
(Reg 0xa24c=0x0000) (Reg 0xa24d=0x0000) (Reg 0xa24e=0x0000) (Reg 0xa24f=0x0000) 
(Reg 0xa250=0xe0dc) (Reg 0xa251=0xe0dc) (Reg 0xa252=0xe0dc) (Reg 0xa253=0xe0dc) 
(Reg 0xa254=0xe0dc) (Reg 0xa255=0xe0dc) (Reg 0xa256=0xe0dc) (Reg 0xa257=0xe0dc) 
(Reg 0xa258=0xe0dc) (Reg 0xa259=0xe0dc) (Reg 0xa25a=0x0000) (Reg 0xa25b=0x0000) 
(Reg 0xa25c=0x0000) (Reg 0xa25d=0x0000) (Reg 0xa25e=0x0000) (Reg 0xa25f=0x0000) 
(Reg 0xa260=0x0000) 

NETWORK LANE VR 2 Registers:

(Reg 0xa280=0x0000) (Reg 0xa281=0x0000) (Reg 0xa282=0x0000) (Reg 0xa283=0x0000) 
(Reg 0xa284=0x0000) (Reg 0xa285=0x0000) (Reg 0xa286=0x0000) (Reg 0xa287=0x0000) 
(Reg 0xa288=0x0000) (Reg 0xa289=0x0000) (Reg 0xa28a=0x0000) (Reg 0xa28b=0x0000) 
(Reg 0xa28c=0x0000) (Reg 0xa28d=0x0000) (Reg 0xa28e=0x0000) (Reg 0xa28f=0x0000) 
(Reg 0xa290=0x0000) (Reg 0xa291=0x0000) (Reg 0xa292=0x0000) (Reg 0xa293=0x0000) 
(Reg 0xa294=0x0000) (Reg 0xa295=0x0000) (Reg 0xa296=0x0000) (Reg 0xa297=0x0000) 
(Reg 0xa298=0x0000) (Reg 0xa299=0x0000) (Reg 0xa29a=0x0000) (Reg 0xa29b=0x0000) 
(Reg 0xa29c=0x0000) (Reg 0xa29d=0x0000) (Reg 0xa29e=0x0000) (Reg 0xa29f=0x0000) 
(Reg 0xa2a0=0x0b21) (Reg 0xa2a1=0x0b2a) (Reg 0xa2a2=0x0b14) (Reg 0xa2a3=0x0b6a) 
(Reg 0xa2a4=0x0b74) (Reg 0xa2a5=0x0b48) (Reg 0xa2a6=0x0b97) (Reg 0xa2a7=0x0b1d) 
(Reg 0xa2a8=0x0b4b) (Reg 0xa2a9=0x0b75) (Reg 0xa2aa=0x0000) (Reg 0xa2ab=0x0000) 
(Reg 0xa2ac=0x0000) (Reg 0xa2ad=0x0000) (Reg 0xa2ae=0x0000) (Reg 0xa2af=0x0000) 
(Reg 0xa2b0=0x1510) (Reg 0xa2b1=0x138d) (Reg 0xa2b2=0x1391) (Reg 0xa2b3=0x125d) 
(Reg 0xa2b4=0x147c) (Reg 0xa2b5=0x132b) (Reg 0xa2b6=0x1405) (Reg 0xa2b7=0x12bc) 
(Reg 0xa2b8=0x14b9) (Reg 0xa2b9=0x13a0) (Reg 0xa2ba=0x0000) (Reg 0xa2bb=0x0000) 
(Reg 0xa2bc=0x0000) (Reg 0xa2bd=0x0000) (Reg 0xa2be=0x0000) (Reg 0xa2bf=0x0000) 
(Reg 0xa2c0=0x20d4) (Reg 0xa2c1=0x20d4) (Reg 0xa2c2=0x20d4) (Reg 0xa2c3=0x20d4) 
(Reg 0xa2c4=0x20d4) (Reg 0xa2c5=0x20d4) (Reg 0xa2c6=0x20d4) (Reg 0xa2c7=0x20d4) 
(Reg 0xa2c8=0x20d4) (Reg 0xa2c9=0x20d4) (Reg 0xa2ca=0x0000) (Reg 0xa2cb=0x0000) 
(Reg 0xa2cc=0x0000) (Reg 0xa2cd=0x0000) (Reg 0xa2ce=0x0000) (Reg 0xa2cf=0x0000) 
(Reg 0xa2d0=0x12b6) (Reg 0xa2d1=0x14e5) (Reg 0xa2d2=0x14d2) (Reg 0xa2d3=0x1423) 
(Reg 0xa2d4=0x1255) (Reg 0xa2d5=0x1213) (Reg 0xa2d6=0x144f) (Reg 0xa2d7=0x12c4) 
(Reg 0xa2d8=0x1384) (Reg 0xa2d9=0x12eb) (Reg 0xa2da=0x0000) (Reg 0xa2db=0x0000) 
(Reg 0xa2dc=0x0000) (Reg 0xa2dd=0x0000) (Reg 0xa2de=0x0000) (Reg 0xa2df=0x0000) 
(Reg 0xa2e0=0x0000) 

HOST LANE VR 1 Registers:

(Reg 0xa400=0x0000) (Reg 0xa401=0x0000) (Reg 0xa402=0x0000) (Reg 0xa403=0x0000) 
(Reg 0xa404=0x0000) (Reg 0xa405=0x0000) (Reg 0xa406=0x0000) (Reg 0xa407=0x0000) 
(Reg 0xa408=0x0000) (Reg 0xa409=0x0000) (Reg 0xa40a=0x0000) (Reg 0xa40b=0x0000) 
(Reg 0xa40c=0x0000) (Reg 0xa40d=0x0000) (Reg 0xa40e=0x0000) (Reg 0xa40f=0x0000) 
(Reg 0xa410=0x0000) (Reg 0xa411=0x0000) (Reg 0xa412=0x0000) (Reg 0xa413=0x0000) 
(Reg 0xa414=0x0000) (Reg 0xa415=0x0000) (Reg 0xa416=0x0000) (Reg 0xa417=0x0000) 
(Reg 0xa418=0x0000) (Reg 0xa419=0x0000) (Reg 0xa41a=0x0000) (Reg 0xa41b=0x0000) 
(Reg 0xa41c=0x0000) (Reg 0xa41d=0x0000) (Reg 0xa41e=0x0000) (Reg 0xa41f=0x0000) 
(Reg 0xa420=0x0001) (Reg 0xa421=0x0001) (Reg 0xa422=0x0001) (Reg 0xa423=0x0001) 
(Reg 0xa424=0x0001) (Reg 0xa425=0x0001) (Reg 0xa426=0x0001) (Reg 0xa427=0x0001) 
(Reg 0xa428=0x0001) (Reg 0xa429=0x0001) (Reg 0xa42a=0x0000) (Reg 0xa42b=0x0000) 
(Reg 0xa42c=0x0000) (Reg 0xa42d=0x0000) (Reg 0xa42e=0x0000) (Reg 0xa42f=0x0000) 
(Reg 0xa430=0x0000) (Reg 0xa431=0x0000) (Reg 0xa432=0x0000) (Reg 0xa433=0x0000) 
(Reg 0xa434=0x0000) (Reg 0xa435=0x0000) (Reg 0xa436=0x0000) (Reg 0xa437=0x0000) 
(Reg 0xa438=0x0000) (Reg 0xa439=0x0000) (Reg 0xa43a=0x0000) (Reg 0xa43b=0x0000) 
(Reg 0xa43c=0x0000) (Reg 0xa43d=0x0000) (Reg 0xa43e=0x0000) (Reg 0xa43f=0x0000) 
(Reg 0xa440=0x0007) (Reg 0xa441=0x0007) (Reg 0xa442=0x0007) (Reg 0xa443=0x0007) 
(Reg 0xa444=0x0007) (Reg 0xa445=0x0007) (Reg 0xa446=0x0007) (Reg 0xa447=0x0007) 
(Reg 0xa448=0x0007) (Reg 0xa449=0x0007) (Reg 0xa44a=0x0000) (Reg 0xa44b=0x0000) 
(Reg 0xa44c=0x0000) (Reg 0xa44d=0x0000) (Reg 0xa44e=0x0000) (Reg 0xa44f=0x0000) 
(Reg 0xa450=0x0000) 

Regs Info
OTN Controller 3 common register:

TOP_MPIF Block : 
---------------------------
Addr     Name                            Value
0x00002  GLOBAL_CFG                      0x0051
0x00004  SCRATCH_PAD1                    0x000a
0x00005  SCRATCH_PAD2                    0x9500
0x00009  GPIO_CONTROL                    0x0000
 
SDS_COMMON Block : BANK B
---------------------------
Addr     Name                            Value
0x0241f  RXLOCKD0_INTSTATUS 3            0x0008
0x02445  RXLOCKD1_INTSTATUS 3            0x005e
0x0246b  RXLOCKD2_INTSTATUS 3            0x0004
0x02491  RXLOCKD3_INTSTATUS 3            0x0010
0x024b9  TXLOCKD0_INTSTATUS 3            0x000c
0x0281f  RXLOCKD0_INTSTATUS 4            0x0005
0x02845  RXLOCKD1_INTSTATUS 4            0x0069
0x0286b  RXLOCKD2_INTSTATUS 4            0x0018
0x02891  RXLOCKD3_INTSTATUS 4            0x0018
0x028b9  TXLOCKD0_INTSTATUS 4            0x0008

SDS_COMMON Block : BANK C
---------------------------
Addr     Name                            Value
0x0301f  RXLOCKD0_INTSTATUS 6            0x0049
0x03045  RXLOCKD1_INTSTATUS 6            0x0049
0x0306b  RXLOCKD2_INTSTATUS 6            0x0049
0x03091  RXLOCKD3_INTSTATUS 6            0x0049
0x030b9  TXLOCKD0_INTSTATUS 6            0x0049
0x0341f  RXLOCKD0_INTSTATUS 7            0x0049
0x03445  RXLOCKD1_INTSTATUS 7            0x0049
0x0346b  RXLOCKD2_INTSTATUS 7            0x0049
0x03491  RXLOCKD3_INTSTATUS 7            0x0049
0x034b9  TXLOCKD0_INTSTATUS 7            0x0049

ILKN_CORE Block : 
---------------------------
Addr     Name                            Value
0x19d6b  RX_INTERLAKEN_STATUS0           0x0049
0x19d6c  RX_INTERLAKEN_SYNCED1           0x0049
0x19d6d  RX_INTERLAKEN_SYNCED0           0x0049
0x19d66  RX_OOBFC_RX_LANE_STATUS1        0x0049
0x19d67  RX_OOBFC_RX_LANE_STATUS0        0x0049
0x19d62  TX_INTERLAKEN_STATUS1           0x0049
0x19d63  TX_INTERLAKEN_STATUS0           0x0049

Port/3 register:

SDS_COMMON Block : line
---------------------------
Addr     Name                            Value
0x0181f  RXLOCKD0_INTSTATUS 0            0x0008
0x01845  RXLOCKD1_INTSTATUS 0            0x0001
0x0186b  RXLOCKD2_INTSTATUS 0            0x0009
0x01891  RXLOCKD3_INTSTATUS 0            0x0001
0x018b9  TXLOCKD0_INTSTATUS 0            0x0049

CPAK Registers:
================
 
NVR 1 Registers:

(Reg 0x8000=0x01) (Reg 0x8001=0x21) (Reg 0x8002=0x09) (Reg 0x8003=0x03) 
(Reg 0x8004=0x00) (Reg 0x8005=0x00) (Reg 0x8006=0x00) (Reg 0x8007=0x00) 
(Reg 0x8008=0x1e) (Reg 0x8009=0xaa) (Reg 0x800a=0x4a) (Reg 0x800b=0x38) 
(Reg 0x800c=0x38) (Reg 0x800d=0x00) (Reg 0x800e=0x0a) (Reg 0x800f=0x00) 
 (Reg 0x8010=0x0a) (Reg 0x8011=0x01) (Reg 0x8012=0x83) (Reg 0x8013=0x40) 
(Reg 0x8014=0x86) (Reg 0x8015=0x60) (Reg 0x8016=0x00) (Reg 0x8017=0x00) 
(Reg 0x8018=0x00) (Reg 0x8019=0x04) (Reg 0x801a=0x40) (Reg 0x801b=0x50) 
(Reg 0x801c=0x26) (Reg 0x801d=0x17) (Reg 0x801e=0x14) (Reg 0x801f=0x46) 
(Reg 0x8020=0x00) (Reg 0x8021=0x43) (Reg 0x8022=0x49) (Reg 0x8023=0x53) 
(Reg 0x8024=0x43) (Reg 0x8025=0x4f) (Reg 0x8026=0x20) (Reg 0x8027=0x20) 
(Reg 0x8028=0x20) (Reg 0x8029=0x20) (Reg 0x802a=0x20) (Reg 0x802b=0x20) 
(Reg 0x802c=0x20) (Reg 0x802d=0x20) (Reg 0x802e=0x20) (Reg 0x802f=0x20) 
(Reg 0x8030=0x20) (Reg 0x8031=0x00) (Reg 0x8032=0x00) (Reg 0x8033=0x0c) 
(Reg 0x8034=0x38) (Reg 0x8035=0x30) (Reg 0x8036=0x30) (Reg 0x8037=0x2d) 
 (Reg 0x8038=0x34) (Reg 0x8039=0x31) (Reg 0x803a=0x34) (Reg 0x803b=0x39) 
(Reg 0x803c=0x35) (Reg 0x803d=0x2d) (Reg 0x803e=0x30) (Reg 0x803f=0x31) 
(Reg 0x8040=0x20) (Reg 0x8041=0x20) (Reg 0x8042=0x20) (Reg 0x8043=0x20) 
(Reg 0x8044=0x46) (Reg 0x8045=0x42) (Reg 0x8046=0x4e) (Reg 0x8047=0x31) 
(Reg 0x8048=0x39) (Reg 0x8049=0x31) (Reg 0x804a=0x32) (Reg 0x804b=0x32) 
(Reg 0x804c=0x30) (Reg 0x804d=0x33) (Reg 0x804e=0x30) (Reg 0x804f=0x20) 
(Reg 0x8050=0x20) (Reg 0x8051=0x20) (Reg 0x8052=0x20) (Reg 0x8053=0x20) 
(Reg 0x8054=0x32) (Reg 0x8055=0x30) (Reg 0x8056=0x31) (Reg 0x8057=0x35) 
(Reg 0x8058=0x30) (Reg 0x8059=0x33) (Reg 0x805a=0x31) (Reg 0x805b=0x39) 
(Reg 0x805c=0x00) (Reg 0x805d=0x00) (Reg 0x805e=0x57) (Reg 0x805f=0x4f) 
 (Reg 0x8060=0x54) (Reg 0x8061=0x52) (Reg 0x8062=0x43) (Reg 0x8063=0x35) 
(Reg 0x8064=0x50) (Reg 0x8065=0x42) (Reg 0x8066=0x41) (Reg 0x8067=0x41) 
(Reg 0x8068=0x6e) (Reg 0x8069=0x5a) (Reg 0x806a=0x00) (Reg 0x806b=0x05) 
(Reg 0x806c=0x02) (Reg 0x806d=0x03) (Reg 0x806e=0x0c) (Reg 0x806f=0x03) 
(Reg 0x8070=0x0f) (Reg 0x8071=0x20) (Reg 0x8072=0x01) (Reg 0x8073=0x01) 
(Reg 0x8074=0x08) (Reg 0x8075=0x00) (Reg 0x8076=0xfe) (Reg 0x8077=0x01) 
(Reg 0x8078=0x00) (Reg 0x8079=0x00) (Reg 0x807a=0x00) (Reg 0x807b=0x02) 
(Reg 0x807c=0x03) (Reg 0x807d=0x00) (Reg 0x807e=0x00) (Reg 0x807f=0xe3) 

NVR 2 Registers:

(Reg 0x8080=0x4b) (Reg 0x8081=0x00) (Reg 0x8082=0x46) (Reg 0x8083=0x00) 
(Reg 0x8084=0x00) (Reg 0x8085=0x00) (Reg 0x8086=0xfb) (Reg 0x8087=0x00) 
(Reg 0x8088=0x8a) (Reg 0x8089=0x00) (Reg 0x808a=0x87) (Reg 0x808b=0x5a) 
(Reg 0x808c=0x7a) (Reg 0x808d=0x76) (Reg 0x808e=0x77) (Reg 0x808f=0xe2) 
(Reg 0x8090=0x00) (Reg 0x8091=0x00) (Reg 0x8092=0x00) (Reg 0x8093=0x00) 
 (Reg 0x8094=0x00) (Reg 0x8095=0x00) (Reg 0x8096=0x00) (Reg 0x8097=0x00) 
(Reg 0x8098=0x00) (Reg 0x8099=0x00) (Reg 0x809a=0x00) (Reg 0x809b=0x00) 
(Reg 0x809c=0x00) (Reg 0x809d=0x00) (Reg 0x809e=0x00) (Reg 0x809f=0x00) 
(Reg 0x80a0=0x00) (Reg 0x80a1=0x00) (Reg 0x80a2=0x00) (Reg 0x80a3=0x00) 
(Reg 0x80a4=0x00) (Reg 0x80a5=0x00) (Reg 0x80a6=0x00) (Reg 0x80a7=0x00) 
(Reg 0x80a8=0x13) (Reg 0x80a9=0x88) (Reg 0x80aa=0x11) (Reg 0x80ab=0x94) 
(Reg 0x80ac=0x05) (Reg 0x80ad=0xdc) (Reg 0x80ae=0x03) (Reg 0x80af=0xe8) 
(Reg 0x80b0=0x45) (Reg 0x80b1=0x76) (Reg 0x80b2=0x22) (Reg 0x80b3=0xd0) 
(Reg 0x80b4=0x06) (Reg 0x80b5=0xc9) (Reg 0x80b6=0x03) (Reg 0x80b7=0x66) 
(Reg 0x80b8=0x5a) (Reg 0x80b9=0x00) (Reg 0x80ba=0x55) (Reg 0x80bb=0x00) 
 (Reg 0x80bc=0x00) (Reg 0x80bd=0x00) (Reg 0x80be=0xfb) (Reg 0x80bf=0x00) 
(Reg 0x80c0=0x88) (Reg 0x80c1=0x71) (Reg 0x80c2=0x43) (Reg 0x80c3=0xe2) 
(Reg 0x80c4=0x04) (Reg 0x80c5=0x62) (Reg 0x80c6=0x02) (Reg 0x80c7=0x32) 
(Reg 0x80c8=0x00) (Reg 0x80c9=0x00) (Reg 0x80ca=0x00) (Reg 0x80cb=0x00) 
(Reg 0x80cc=0x00) (Reg 0x80cd=0x00) (Reg 0x80ce=0x00) (Reg 0x80cf=0x00) 
(Reg 0x80d0=0x00) (Reg 0x80d1=0x00) (Reg 0x80d2=0x00) (Reg 0x80d3=0x00) 
(Reg 0x80d4=0x00) (Reg 0x80d5=0x00) (Reg 0x80d6=0x00) (Reg 0x80d7=0x00) 
(Reg 0x80d8=0x00) (Reg 0x80d9=0x00) (Reg 0x80da=0x00) (Reg 0x80db=0x00) 
(Reg 0x80dc=0x00) (Reg 0x80dd=0x00) (Reg 0x80de=0x00) (Reg 0x80df=0x00) 
(Reg 0x80e0=0x00) (Reg 0x80e1=0x00) (Reg 0x80e2=0x00) (Reg 0x80e3=0x00) 
 (Reg 0x80e4=0x00) (Reg 0x80e5=0x00) (Reg 0x80e6=0x00) (Reg 0x80e7=0x00) 
(Reg 0x80e8=0x00) (Reg 0x80e9=0x00) (Reg 0x80ea=0x00) (Reg 0x80eb=0x00) 
(Reg 0x80ec=0x00) (Reg 0x80ed=0x00) (Reg 0x80ee=0x00) (Reg 0x80ef=0x00) 
(Reg 0x80f0=0x00) (Reg 0x80f1=0x00) (Reg 0x80f2=0x00) (Reg 0x80f3=0x00) 
(Reg 0x80f4=0x00) (Reg 0x80f5=0x00) (Reg 0x80f6=0x00) (Reg 0x80f7=0x00) 
(Reg 0x80f8=0x00) (Reg 0x80f9=0x00) (Reg 0x80fa=0x00) (Reg 0x80fb=0x00) 
(Reg 0x80fc=0x00) (Reg 0x80fd=0x00) (Reg 0x80fe=0x00) (Reg 0x80ff=0x93) 

NVR 3 Registers:

(Reg 0x8100=0x00) (Reg 0x8101=0x00) (Reg 0x8102=0x00) (Reg 0x8103=0x00) 
(Reg 0x8104=0x00) (Reg 0x8105=0x00) (Reg 0x8106=0x00) (Reg 0x8107=0x00) 
(Reg 0x8108=0x00) (Reg 0x8109=0x00) (Reg 0x810a=0x00) (Reg 0x810b=0x00) 
(Reg 0x810c=0x00) (Reg 0x810d=0x00) (Reg 0x810e=0x00) (Reg 0x810f=0x00) 
(Reg 0x8110=0x00) (Reg 0x8111=0x00) (Reg 0x8112=0x00) (Reg 0x8113=0x00) 
(Reg 0x8114=0x00) (Reg 0x8115=0x00) (Reg 0x8116=0x00) (Reg 0x8117=0x00) 
 (Reg 0x8118=0x00) (Reg 0x8119=0x00) (Reg 0x811a=0x00) (Reg 0x811b=0x00) 
(Reg 0x811c=0x00) (Reg 0x811d=0x00) (Reg 0x811e=0x00) (Reg 0x811f=0x00) 
(Reg 0x8120=0x00) (Reg 0x8121=0x00) (Reg 0x8122=0x00) (Reg 0x8123=0x00) 
(Reg 0x8124=0x00) (Reg 0x8125=0x00) (Reg 0x8126=0x00) (Reg 0x8127=0x00) 
(Reg 0x8128=0x00) (Reg 0x8129=0x00) (Reg 0x812a=0x00) (Reg 0x812b=0x00) 
(Reg 0x812c=0x00) (Reg 0x812d=0x00) (Reg 0x812e=0x00) (Reg 0x812f=0x00) 
(Reg 0x8130=0x00) (Reg 0x8131=0x00) (Reg 0x8132=0x00) (Reg 0x8133=0x00) 
(Reg 0x8134=0x00) (Reg 0x8135=0x00) (Reg 0x8136=0x00) (Reg 0x8137=0x00) 
(Reg 0x8138=0x00) (Reg 0x8139=0x00) (Reg 0x813a=0x00) (Reg 0x813b=0x00) 
(Reg 0x813c=0x00) (Reg 0x813d=0x00) (Reg 0x813e=0x00) (Reg 0x813f=0x00) 
 (Reg 0x8140=0x00) (Reg 0x8141=0x00) (Reg 0x8142=0x00) (Reg 0x8143=0x00) 
(Reg 0x8144=0x00) (Reg 0x8145=0x00) (Reg 0x8146=0x00) (Reg 0x8147=0x00) 
(Reg 0x8148=0x00) (Reg 0x8149=0x00) (Reg 0x814a=0x00) (Reg 0x814b=0x00) 
(Reg 0x814c=0x00) (Reg 0x814d=0x00) (Reg 0x814e=0x00) (Reg 0x814f=0x00) 
(Reg 0x8150=0x00) (Reg 0x8151=0x00) (Reg 0x8152=0x00) (Reg 0x8153=0x00) 
(Reg 0x8154=0x00) (Reg 0x8155=0x00) (Reg 0x8156=0x00) (Reg 0x8157=0x00) 
(Reg 0x8158=0x00) (Reg 0x8159=0x00) (Reg 0x815a=0x00) (Reg 0x815b=0x00) 
(Reg 0x815c=0x00) (Reg 0x815d=0x00) (Reg 0x815e=0x00) (Reg 0x815f=0x00) 
(Reg 0x8160=0x00) (Reg 0x8161=0x00) (Reg 0x8162=0x00) (Reg 0x8163=0x00) 
(Reg 0x8164=0x00) (Reg 0x8165=0x00) (Reg 0x8166=0x00) (Reg 0x8167=0x00) 
 (Reg 0x8168=0x00) (Reg 0x8169=0x00) (Reg 0x816a=0x00) (Reg 0x816b=0x00) 
(Reg 0x816c=0x00) (Reg 0x816d=0x00) (Reg 0x816e=0x00) (Reg 0x816f=0x00) 
(Reg 0x8170=0x00) (Reg 0x8171=0x00) (Reg 0x8172=0x00) (Reg 0x8173=0x00) 
(Reg 0x8174=0x00) (Reg 0x8175=0x00) (Reg 0x8176=0x00) (Reg 0x8177=0x00) 
(Reg 0x8178=0x00) (Reg 0x8179=0x00) (Reg 0x817a=0x00) (Reg 0x817b=0x00) 
(Reg 0x817c=0x00) (Reg 0x817d=0x00) (Reg 0x817e=0x00) (Reg 0x817f=0x00) 

NVR 4 Registers:

(Reg 0x8180=0x00) 

 VR 1 Registers:

(Reg 0xa000=0x0000) (Reg 0xa001=0x1234) (Reg 0xa002=0x0000) (Reg 0xa003=0x0000) 
(Reg 0xa004=0x0000) (Reg 0xa005=0x0000) (Reg 0xa006=0x0000) (Reg 0xa007=0x0000) 
(Reg 0xa008=0x0000) (Reg 0xa009=0x0000) (Reg 0xa00a=0x0000) (Reg 0xa00b=0x0000) 
(Reg 0xa00c=0x0000) (Reg 0xa00d=0x0000) (Reg 0xa00e=0x0000) (Reg 0xa00f=0x0000) 
(Reg 0xa010=0x2000) (Reg 0xa011=0x0200) (Reg 0xa012=0x0200) (Reg 0xa013=0x0000) 
(Reg 0xa014=0x0000) (Reg 0xa015=0x0000) (Reg 0xa016=0x0008) (Reg 0xa017=0x0000) 
(Reg 0xa018=0xb180) (Reg 0xa019=0x03ff) (Reg 0xa01a=0x03ff) (Reg 0xa01b=0x0000) 
(Reg 0xa01c=0x8000) (Reg 0xa01d=0x0022) (Reg 0xa01e=0x0000) (Reg 0xa01f=0x0000) 
(Reg 0xa020=0x0000) (Reg 0xa021=0x8000) (Reg 0xa022=0x000f) (Reg 0xa023=0x0020) 
(Reg 0xa024=0x0000) (Reg 0xa025=0x0000) (Reg 0xa026=0x0000) (Reg 0xa027=0x0000) 
(Reg 0xa028=0x006a) (Reg 0xa029=0xa7f8) (Reg 0xa02a=0x0062) (Reg 0xa02b=0x0ff0) 
(Reg 0xa02c=0x00f0) (Reg 0xa02d=0x0000) (Reg 0xa02e=0x0000) (Reg 0xa02f=0x1527) 
(Reg 0xa030=0x80d3) (Reg 0xa031=0x0000) (Reg 0xa032=0x6572) (Reg 0xa033=0x3069) 
(Reg 0xa034=0x0000) (Reg 0xa035=0x0000) (Reg 0xa036=0x0000) (Reg 0xa037=0x0000) 
(Reg 0xa038=0x0000) (Reg 0xa039=0x0000) (Reg 0xa03a=0x0000) 

NETWORK LANE VR 1 Registers:

(Reg 0xa200=0x0003) (Reg 0xa201=0x0003) (Reg 0xa202=0x0003) (Reg 0xa203=0x0003) 
(Reg 0xa204=0x0003) (Reg 0xa205=0x0003) (Reg 0xa206=0x0003) (Reg 0xa207=0x0003) 
(Reg 0xa208=0x0003) (Reg 0xa209=0x0003) (Reg 0xa20a=0x0000) (Reg 0xa20b=0x0000) 
(Reg 0xa20c=0x0000) (Reg 0xa20d=0x0000) (Reg 0xa20e=0x0000) (Reg 0xa20f=0x0000) 
(Reg 0xa210=0x0010) (Reg 0xa211=0x0010) (Reg 0xa212=0x0010) (Reg 0xa213=0x0010) 
(Reg 0xa214=0x0010) (Reg 0xa215=0x0010) (Reg 0xa216=0x0010) (Reg 0xa217=0x0010) 
(Reg 0xa218=0x0010) (Reg 0xa219=0x0010) (Reg 0xa21a=0x0000) (Reg 0xa21b=0x0000) 
(Reg 0xa21c=0x0000) (Reg 0xa21d=0x0000) (Reg 0xa21e=0x0000) (Reg 0xa21f=0x0000) 
(Reg 0xa220=0x0003) (Reg 0xa221=0x0003) (Reg 0xa222=0x0003) (Reg 0xa223=0x0003) 
(Reg 0xa224=0x0003) (Reg 0xa225=0x0003) (Reg 0xa226=0x0003) (Reg 0xa227=0x0003) 
(Reg 0xa228=0x0003) (Reg 0xa229=0x0003) (Reg 0xa22a=0x0000) (Reg 0xa22b=0x0000) 
(Reg 0xa22c=0x0000) (Reg 0xa22d=0x0000) (Reg 0xa22e=0x0000) (Reg 0xa22f=0x0000) 
(Reg 0xa230=0x0010) (Reg 0xa231=0x0010) (Reg 0xa232=0x0010) (Reg 0xa233=0x0010) 
(Reg 0xa234=0x0010) (Reg 0xa235=0x0010) (Reg 0xa236=0x0010) (Reg 0xa237=0x0010) 
(Reg 0xa238=0x0010) (Reg 0xa239=0x0010) (Reg 0xa23a=0x0000) (Reg 0xa23b=0x0000) 
(Reg 0xa23c=0x0000) (Reg 0xa23d=0x0000) (Reg 0xa23e=0x0000) (Reg 0xa23f=0x0000) 
(Reg 0xa240=0xffff) (Reg 0xa241=0xffff) (Reg 0xa242=0xffff) (Reg 0xa243=0xffff) 
(Reg 0xa244=0xffff) (Reg 0xa245=0xffff) (Reg 0xa246=0xffff) (Reg 0xa247=0xffff) 
(Reg 0xa248=0xffff) (Reg 0xa249=0xffff) (Reg 0xa24a=0x0000) (Reg 0xa24b=0x0000) 
(Reg 0xa24c=0x0000) (Reg 0xa24d=0x0000) (Reg 0xa24e=0x0000) (Reg 0xa24f=0x0000) 
(Reg 0xa250=0xe0dc) (Reg 0xa251=0xe0dc) (Reg 0xa252=0xe0dc) (Reg 0xa253=0xe0dc) 
(Reg 0xa254=0xe0dc) (Reg 0xa255=0xe0dc) (Reg 0xa256=0xe0dc) (Reg 0xa257=0xe0dc) 
(Reg 0xa258=0xe0dc) (Reg 0xa259=0xe0dc) (Reg 0xa25a=0x0000) (Reg 0xa25b=0x0000) 
(Reg 0xa25c=0x0000) (Reg 0xa25d=0x0000) (Reg 0xa25e=0x0000) (Reg 0xa25f=0x0000) 
(Reg 0xa260=0x0000) 

NETWORK LANE VR 2 Registers:

(Reg 0xa280=0x0000) (Reg 0xa281=0x0000) (Reg 0xa282=0x0000) (Reg 0xa283=0x0000) 
(Reg 0xa284=0x0000) (Reg 0xa285=0x0000) (Reg 0xa286=0x0000) (Reg 0xa287=0x0000) 
(Reg 0xa288=0x0000) (Reg 0xa289=0x0000) (Reg 0xa28a=0x0000) (Reg 0xa28b=0x0000) 
(Reg 0xa28c=0x0000) (Reg 0xa28d=0x0000) (Reg 0xa28e=0x0000) (Reg 0xa28f=0x0000) 
(Reg 0xa290=0x0000) (Reg 0xa291=0x0000) (Reg 0xa292=0x0000) (Reg 0xa293=0x0000) 
(Reg 0xa294=0x0000) (Reg 0xa295=0x0000) (Reg 0xa296=0x0000) (Reg 0xa297=0x0000) 
(Reg 0xa298=0x0000) (Reg 0xa299=0x0000) (Reg 0xa29a=0x0000) (Reg 0xa29b=0x0000) 
(Reg 0xa29c=0x0000) (Reg 0xa29d=0x0000) (Reg 0xa29e=0x0000) (Reg 0xa29f=0x0000) 
(Reg 0xa2a0=0x0000) (Reg 0xa2a1=0x0000) (Reg 0xa2a2=0x0000) (Reg 0xa2a3=0x0000) 
(Reg 0xa2a4=0x0000) (Reg 0xa2a5=0x0000) (Reg 0xa2a6=0x0000) (Reg 0xa2a7=0x0000) 
(Reg 0xa2a8=0x0000) (Reg 0xa2a9=0x0000) (Reg 0xa2aa=0x0000) (Reg 0xa2ab=0x0000) 
(Reg 0xa2ac=0x0000) (Reg 0xa2ad=0x0000) (Reg 0xa2ae=0x0000) (Reg 0xa2af=0x0000) 
(Reg 0xa2b0=0x0000) (Reg 0xa2b1=0x0000) (Reg 0xa2b2=0x0000) (Reg 0xa2b3=0x0000) 
(Reg 0xa2b4=0x0000) (Reg 0xa2b5=0x0000) (Reg 0xa2b6=0x0000) (Reg 0xa2b7=0x0000) 
(Reg 0xa2b8=0x0000) (Reg 0xa2b9=0x0000) (Reg 0xa2ba=0x0000) (Reg 0xa2bb=0x0000) 
(Reg 0xa2bc=0x0000) (Reg 0xa2bd=0x0000) (Reg 0xa2be=0x0000) (Reg 0xa2bf=0x0000) 
(Reg 0xa2c0=0x1c27) (Reg 0xa2c1=0x1c27) (Reg 0xa2c2=0x1c27) (Reg 0xa2c3=0x1c27) 
(Reg 0xa2c4=0x1c27) (Reg 0xa2c5=0x1c27) (Reg 0xa2c6=0x1c27) (Reg 0xa2c7=0x1c27) 
(Reg 0xa2c8=0x1c27) (Reg 0xa2c9=0x1c27) (Reg 0xa2ca=0x0000) (Reg 0xa2cb=0x0000) 
(Reg 0xa2cc=0x0000) (Reg 0xa2cd=0x0000) (Reg 0xa2ce=0x0000) (Reg 0xa2cf=0x0000) 
(Reg 0xa2d0=0x0000) (Reg 0xa2d1=0x0000) (Reg 0xa2d2=0x0000) (Reg 0xa2d3=0x0000) 
(Reg 0xa2d4=0x0000) (Reg 0xa2d5=0x0000) (Reg 0xa2d6=0x0000) (Reg 0xa2d7=0x0000) 
(Reg 0xa2d8=0x0000) (Reg 0xa2d9=0x0000) (Reg 0xa2da=0x0000) (Reg 0xa2db=0x0000) 
(Reg 0xa2dc=0x0000) (Reg 0xa2dd=0x0000) (Reg 0xa2de=0x0000) (Reg 0xa2df=0x0000) 
(Reg 0xa2e0=0x0000) 

HOST LANE VR 1 Registers:

 (Reg 0xa400=0x0000) (Reg 0xa401=0x0000) (Reg 0xa402=0x0000) (Reg 0xa403=0x0000) 
(Reg 0xa404=0x0000) (Reg 0xa405=0x0000) (Reg 0xa406=0x0000) (Reg 0xa407=0x0000) 
(Reg 0xa408=0x0000) (Reg 0xa409=0x0000) (Reg 0xa40a=0x0000) (Reg 0xa40b=0x0000) 
(Reg 0xa40c=0x0000) (Reg 0xa40d=0x0000) (Reg 0xa40e=0x0000) (Reg 0xa40f=0x0000) 
(Reg 0xa410=0x0000) (Reg 0xa411=0x0000) (Reg 0xa412=0x0000) (Reg 0xa413=0x0000) 
(Reg 0xa414=0x0000) (Reg 0xa415=0x0000) (Reg 0xa416=0x0000) (Reg 0xa417=0x0000) 
(Reg 0xa418=0x0000) (Reg 0xa419=0x0000) (Reg 0xa41a=0x0000) (Reg 0xa41b=0x0000) 
(Reg 0xa41c=0x0000) (Reg 0xa41d=0x0000) (Reg 0xa41e=0x0000) (Reg 0xa41f=0x0000) 
(Reg 0xa420=0x0001) (Reg 0xa421=0x0001) (Reg 0xa422=0x0001) (Reg 0xa423=0x0001) 
(Reg 0xa424=0x0001) (Reg 0xa425=0x0001) (Reg 0xa426=0x0001) (Reg 0xa427=0x0001) 
(Reg 0xa428=0x0001) (Reg 0xa429=0x0001) (Reg 0xa42a=0x0000) (Reg 0xa42b=0x0000) 
(Reg 0xa42c=0x0000) (Reg 0xa42d=0x0000) (Reg 0xa42e=0x0000) (Reg 0xa42f=0x0000) 
(Reg 0xa430=0x0000) (Reg 0xa431=0x0000) (Reg 0xa432=0x0000) (Reg 0xa433=0x0000) 
(Reg 0xa434=0x0000) (Reg 0xa435=0x0000) (Reg 0xa436=0x0000) (Reg 0xa437=0x0000) 
(Reg 0xa438=0x0000) (Reg 0xa439=0x0000) (Reg 0xa43a=0x0000) (Reg 0xa43b=0x0000) 
(Reg 0xa43c=0x0000) (Reg 0xa43d=0x0000) (Reg 0xa43e=0x0000) (Reg 0xa43f=0x0000) 
(Reg 0xa440=0x0007) (Reg 0xa441=0x0007) (Reg 0xa442=0x0007) (Reg 0xa443=0x0007) 
(Reg 0xa444=0x0007) (Reg 0xa445=0x0007) (Reg 0xa446=0x0007) (Reg 0xa447=0x0007) 
(Reg 0xa448=0x0007) (Reg 0xa449=0x0007) (Reg 0xa44a=0x0000) (Reg 0xa44b=0x0000) 
(Reg 0xa44c=0x0000) (Reg 0xa44d=0x0000) (Reg 0xa44e=0x0000) (Reg 0xa44f=0x0000) 
(Reg 0xa450=0x0000) 

Regs Info
OTN Controller 0 common register:

TOP_MPIF Block : 
---------------------------
Addr     Name                            Value
0x00002  GLOBAL_CFG                      0x0051
0x00004  SCRATCH_PAD1                    0x001e
0x00005  SCRATCH_PAD2                    0x5f00
0x00009  GPIO_CONTROL                    0x0000

SDS_COMMON Block : BANK B
---------------------------
Addr     Name                            Value
0x0241f  RXLOCKD0_INTSTATUS 3            0x0000
0x02445  RXLOCKD1_INTSTATUS 3            0x0008
0x0246b  RXLOCKD2_INTSTATUS 3            0x0008
0x02491  RXLOCKD3_INTSTATUS 3            0x0018
0x024b9  TXLOCKD0_INTSTATUS 3            0x0008
0x0281f  RXLOCKD0_INTSTATUS 4            0x0008
0x02845  RXLOCKD1_INTSTATUS 4            0x0024
0x0286b  RXLOCKD2_INTSTATUS 4            0x0008
0x02891  RXLOCKD3_INTSTATUS 4            0x0018
0x028b9  TXLOCKD0_INTSTATUS 4            0x0008

SDS_COMMON Block : BANK C
---------------------------
Addr     Name                            Value
0x0301f  RXLOCKD0_INTSTATUS 6            0x0049
0x03045  RXLOCKD1_INTSTATUS 6            0x0049
0x0306b  RXLOCKD2_INTSTATUS 6            0x0049
0x03091  RXLOCKD3_INTSTATUS 6            0x0049
0x030b9  TXLOCKD0_INTSTATUS 6            0x0049
0x0341f  RXLOCKD0_INTSTATUS 7            0x0049
0x03445  RXLOCKD1_INTSTATUS 7            0x0049
0x0346b  RXLOCKD2_INTSTATUS 7            0x0049
0x03491  RXLOCKD3_INTSTATUS 7            0x0049
0x034b9  TXLOCKD0_INTSTATUS 7            0x0049

ILKN_CORE Block : 
---------------------------
Addr     Name                            Value
0x19d6b  RX_INTERLAKEN_STATUS0           0x0049
0x19d6c  RX_INTERLAKEN_SYNCED1           0x0049
0x19d6d  RX_INTERLAKEN_SYNCED0           0x0049
0x19d66  RX_OOBFC_RX_LANE_STATUS1        0x0049
0x19d67  RX_OOBFC_RX_LANE_STATUS0        0x0049
0x19d62  TX_INTERLAKEN_STATUS1           0x0049
0x19d63  TX_INTERLAKEN_STATUS0           0x0049

Port/0 register:

SDS_COMMON Block : line
---------------------------
Addr     Name                            Value
0x0181f  RXLOCKD0_INTSTATUS 0            0x0049
0x01845  RXLOCKD1_INTSTATUS 0            0x0049
0x0186b  RXLOCKD2_INTSTATUS 0            0x0049
0x01891  RXLOCKD3_INTSTATUS 0            0x0049
0x018b9  TXLOCKD0_INTSTATUS 0            0x0049

CPAK Registers:
 ================

NVR 1 Registers:

(Reg 0x8000=0x01) (Reg 0x8001=0x21) (Reg 0x8002=0x09) (Reg 0x8003=0x03) 
(Reg 0x8004=0x00) (Reg 0x8005=0x00) (Reg 0x8006=0x00) (Reg 0x8007=0x00) 
(Reg 0x8008=0x1e) (Reg 0x8009=0xaa) (Reg 0x800a=0x4a) (Reg 0x800b=0x38) 
(Reg 0x800c=0x38) (Reg 0x800d=0x00) (Reg 0x800e=0x0a) (Reg 0x800f=0x00) 
(Reg 0x8010=0x0a) (Reg 0x8011=0x01) (Reg 0x8012=0x83) (Reg 0x8013=0x40) 
(Reg 0x8014=0x86) (Reg 0x8015=0x60) (Reg 0x8016=0x00) (Reg 0x8017=0x00) 
 (Reg 0x8018=0x00) (Reg 0x8019=0x04) (Reg 0x801a=0x40) (Reg 0x801b=0x50) 
(Reg 0x801c=0x26) (Reg 0x801d=0x17) (Reg 0x801e=0x14) (Reg 0x801f=0x46) 
(Reg 0x8020=0x00) (Reg 0x8021=0x43) (Reg 0x8022=0x49) (Reg 0x8023=0x53) 
(Reg 0x8024=0x43) (Reg 0x8025=0x4f) (Reg 0x8026=0x20) (Reg 0x8027=0x20) 
(Reg 0x8028=0x20) (Reg 0x8029=0x20) (Reg 0x802a=0x20) (Reg 0x802b=0x20) 
(Reg 0x802c=0x20) (Reg 0x802d=0x20) (Reg 0x802e=0x20) (Reg 0x802f=0x20) 
(Reg 0x8030=0x20) (Reg 0x8031=0x00) (Reg 0x8032=0x00) (Reg 0x8033=0x0c) 
(Reg 0x8034=0x38) (Reg 0x8035=0x30) (Reg 0x8036=0x30) (Reg 0x8037=0x2d) 
(Reg 0x8038=0x34) (Reg 0x8039=0x31) (Reg 0x803a=0x34) (Reg 0x803b=0x39) 
(Reg 0x803c=0x35) (Reg 0x803d=0x2d) (Reg 0x803e=0x30) (Reg 0x803f=0x31) 
 (Reg 0x8040=0x20) (Reg 0x8041=0x20) (Reg 0x8042=0x20) (Reg 0x8043=0x20) 
(Reg 0x8044=0x46) (Reg 0x8045=0x42) (Reg 0x8046=0x4e) (Reg 0x8047=0x31) 
(Reg 0x8048=0x39) (Reg 0x8049=0x30) (Reg 0x804a=0x39) (Reg 0x804b=0x32) 
(Reg 0x804c=0x31) (Reg 0x804d=0x31) (Reg 0x804e=0x30) (Reg 0x804f=0x20) 
(Reg 0x8050=0x20) (Reg 0x8051=0x20) (Reg 0x8052=0x20) (Reg 0x8053=0x20) 
(Reg 0x8054=0x32) (Reg 0x8055=0x30) (Reg 0x8056=0x31) (Reg 0x8057=0x35) 
(Reg 0x8058=0x30) (Reg 0x8059=0x33) (Reg 0x805a=0x30) (Reg 0x805b=0x35) 
(Reg 0x805c=0x00) (Reg 0x805d=0x00) (Reg 0x805e=0x57) (Reg 0x805f=0x4f) 
(Reg 0x8060=0x54) (Reg 0x8061=0x52) (Reg 0x8062=0x43) (Reg 0x8063=0x35) 
(Reg 0x8064=0x50) (Reg 0x8065=0x42) (Reg 0x8066=0x41) (Reg 0x8067=0x41) 
 (Reg 0x8068=0x6e) (Reg 0x8069=0x5a) (Reg 0x806a=0x00) (Reg 0x806b=0x05) 
(Reg 0x806c=0x02) (Reg 0x806d=0x03) (Reg 0x806e=0x0c) (Reg 0x806f=0x03) 
(Reg 0x8070=0x0f) (Reg 0x8071=0x20) (Reg 0x8072=0x01) (Reg 0x8073=0x01) 
(Reg 0x8074=0x08) (Reg 0x8075=0x00) (Reg 0x8076=0xfe) (Reg 0x8077=0x01) 
(Reg 0x8078=0x00) (Reg 0x8079=0x00) (Reg 0x807a=0x00) (Reg 0x807b=0x02) 
(Reg 0x807c=0x03) (Reg 0x807d=0x00) (Reg 0x807e=0x00) (Reg 0x807f=0xe3) 

NVR 2 Registers:

(Reg 0x8080=0x4b) (Reg 0x8081=0x00) (Reg 0x8082=0x46) (Reg 0x8083=0x00) 
(Reg 0x8084=0x00) (Reg 0x8085=0x00) (Reg 0x8086=0xfb) (Reg 0x8087=0x00) 
(Reg 0x8088=0x8a) (Reg 0x8089=0x00) (Reg 0x808a=0x87) (Reg 0x808b=0x5a) 
(Reg 0x808c=0x7a) (Reg 0x808d=0x76) (Reg 0x808e=0x77) (Reg 0x808f=0xe2) 
(Reg 0x8090=0x00) (Reg 0x8091=0x00) (Reg 0x8092=0x00) (Reg 0x8093=0x00) 
(Reg 0x8094=0x00) (Reg 0x8095=0x00) (Reg 0x8096=0x00) (Reg 0x8097=0x00) 
(Reg 0x8098=0x00) (Reg 0x8099=0x00) (Reg 0x809a=0x00) (Reg 0x809b=0x00) 
 (Reg 0x809c=0x00) (Reg 0x809d=0x00) (Reg 0x809e=0x00) (Reg 0x809f=0x00) 
(Reg 0x80a0=0x00) (Reg 0x80a1=0x00) (Reg 0x80a2=0x00) (Reg 0x80a3=0x00) 
(Reg 0x80a4=0x00) (Reg 0x80a5=0x00) (Reg 0x80a6=0x00) (Reg 0x80a7=0x00) 
(Reg 0x80a8=0x13) (Reg 0x80a9=0x88) (Reg 0x80aa=0x11) (Reg 0x80ab=0x94) 
(Reg 0x80ac=0x05) (Reg 0x80ad=0xdc) (Reg 0x80ae=0x03) (Reg 0x80af=0xe8) 
(Reg 0x80b0=0x45) (Reg 0x80b1=0x76) (Reg 0x80b2=0x22) (Reg 0x80b3=0xd0) 
(Reg 0x80b4=0x06) (Reg 0x80b5=0xc9) (Reg 0x80b6=0x03) (Reg 0x80b7=0x66) 
(Reg 0x80b8=0x5a) (Reg 0x80b9=0x00) (Reg 0x80ba=0x55) (Reg 0x80bb=0x00) 
(Reg 0x80bc=0x00) (Reg 0x80bd=0x00) (Reg 0x80be=0xfb) (Reg 0x80bf=0x00) 
(Reg 0x80c0=0x88) (Reg 0x80c1=0x71) (Reg 0x80c2=0x43) (Reg 0x80c3=0xe2) 
 (Reg 0x80c4=0x04) (Reg 0x80c5=0x62) (Reg 0x80c6=0x02) (Reg 0x80c7=0x32) 
(Reg 0x80c8=0x00) (Reg 0x80c9=0x00) (Reg 0x80ca=0x00) (Reg 0x80cb=0x00) 
(Reg 0x80cc=0x00) (Reg 0x80cd=0x00) (Reg 0x80ce=0x00) (Reg 0x80cf=0x00) 
(Reg 0x80d0=0x00) (Reg 0x80d1=0x00) (Reg 0x80d2=0x00) (Reg 0x80d3=0x00) 
(Reg 0x80d4=0x00) (Reg 0x80d5=0x00) (Reg 0x80d6=0x00) (Reg 0x80d7=0x00) 
(Reg 0x80d8=0x00) (Reg 0x80d9=0x00) (Reg 0x80da=0x00) (Reg 0x80db=0x00) 
(Reg 0x80dc=0x00) (Reg 0x80dd=0x00) (Reg 0x80de=0x00) (Reg 0x80df=0x00) 
(Reg 0x80e0=0x00) (Reg 0x80e1=0x00) (Reg 0x80e2=0x00) (Reg 0x80e3=0x00) 
(Reg 0x80e4=0x00) (Reg 0x80e5=0x00) (Reg 0x80e6=0x00) (Reg 0x80e7=0x00) 
(Reg 0x80e8=0x00) (Reg 0x80e9=0x00) (Reg 0x80ea=0x00) (Reg 0x80eb=0x00) 
 (Reg 0x80ec=0x00) (Reg 0x80ed=0x00) (Reg 0x80ee=0x00) (Reg 0x80ef=0x00) 
(Reg 0x80f0=0x00) (Reg 0x80f1=0x00) (Reg 0x80f2=0x00) (Reg 0x80f3=0x00) 
(Reg 0x80f4=0x00) (Reg 0x80f5=0x00) (Reg 0x80f6=0x00) (Reg 0x80f7=0x00) 
(Reg 0x80f8=0x00) (Reg 0x80f9=0x00) (Reg 0x80fa=0x00) (Reg 0x80fb=0x00) 
(Reg 0x80fc=0x00) (Reg 0x80fd=0x00) (Reg 0x80fe=0x00) (Reg 0x80ff=0x93) 

NVR 3 Registers:

(Reg 0x8100=0x00) (Reg 0x8101=0x00) (Reg 0x8102=0x00) (Reg 0x8103=0x00) 
(Reg 0x8104=0x00) (Reg 0x8105=0x00) (Reg 0x8106=0x00) (Reg 0x8107=0x00) 
(Reg 0x8108=0x00) (Reg 0x8109=0x00) (Reg 0x810a=0x00) (Reg 0x810b=0x00) 
(Reg 0x810c=0x00) (Reg 0x810d=0x00) (Reg 0x810e=0x00) (Reg 0x810f=0x00) 
(Reg 0x8110=0x00) (Reg 0x8111=0x00) (Reg 0x8112=0x00) (Reg 0x8113=0x00) 
(Reg 0x8114=0x00) (Reg 0x8115=0x00) (Reg 0x8116=0x00) (Reg 0x8117=0x00) 
(Reg 0x8118=0x00) (Reg 0x8119=0x00) (Reg 0x811a=0x00) (Reg 0x811b=0x00) 
(Reg 0x811c=0x00) (Reg 0x811d=0x00) (Reg 0x811e=0x00) (Reg 0x811f=0x00) 
 (Reg 0x8120=0x00) (Reg 0x8121=0x00) (Reg 0x8122=0x00) (Reg 0x8123=0x00) 
(Reg 0x8124=0x00) (Reg 0x8125=0x00) (Reg 0x8126=0x00) (Reg 0x8127=0x00) 
(Reg 0x8128=0x00) (Reg 0x8129=0x00) (Reg 0x812a=0x00) (Reg 0x812b=0x00) 
(Reg 0x812c=0x00) (Reg 0x812d=0x00) (Reg 0x812e=0x00) (Reg 0x812f=0x00) 
(Reg 0x8130=0x00) (Reg 0x8131=0x00) (Reg 0x8132=0x00) (Reg 0x8133=0x00) 
(Reg 0x8134=0x00) (Reg 0x8135=0x00) (Reg 0x8136=0x00) (Reg 0x8137=0x00) 
(Reg 0x8138=0x00) (Reg 0x8139=0x00) (Reg 0x813a=0x00) (Reg 0x813b=0x00) 
(Reg 0x813c=0x00) (Reg 0x813d=0x00) (Reg 0x813e=0x00) (Reg 0x813f=0x00) 
(Reg 0x8140=0x00) (Reg 0x8141=0x00) (Reg 0x8142=0x00) (Reg 0x8143=0x00) 
(Reg 0x8144=0x00) (Reg 0x8145=0x00) (Reg 0x8146=0x00) (Reg 0x8147=0x00) 
 (Reg 0x8148=0x00) (Reg 0x8149=0x00) (Reg 0x814a=0x00) (Reg 0x814b=0x00) 
(Reg 0x814c=0x00) (Reg 0x814d=0x00) (Reg 0x814e=0x00) (Reg 0x814f=0x00) 
(Reg 0x8150=0x00) (Reg 0x8151=0x00) (Reg 0x8152=0x00) (Reg 0x8153=0x00) 
(Reg 0x8154=0x00) (Reg 0x8155=0x00) (Reg 0x8156=0x00) (Reg 0x8157=0x00) 
(Reg 0x8158=0x00) (Reg 0x8159=0x00) (Reg 0x815a=0x00) (Reg 0x815b=0x00) 
(Reg 0x815c=0x00) (Reg 0x815d=0x00) (Reg 0x815e=0x00) (Reg 0x815f=0x00) 
(Reg 0x8160=0x00) (Reg 0x8161=0x00) (Reg 0x8162=0x00) (Reg 0x8163=0x00) 
(Reg 0x8164=0x00) (Reg 0x8165=0x00) (Reg 0x8166=0x00) (Reg 0x8167=0x00) 
(Reg 0x8168=0x00) (Reg 0x8169=0x00) (Reg 0x816a=0x00) (Reg 0x816b=0x00) 
(Reg 0x816c=0x00) (Reg 0x816d=0x00) (Reg 0x816e=0x00) (Reg 0x816f=0x00) 
 (Reg 0x8170=0x00) (Reg 0x8171=0x00) (Reg 0x8172=0x00) (Reg 0x8173=0x00) 
(Reg 0x8174=0x00) (Reg 0x8175=0x00) (Reg 0x8176=0x00) (Reg 0x8177=0x00) 
(Reg 0x8178=0x00) (Reg 0x8179=0x00) (Reg 0x817a=0x00) (Reg 0x817b=0x00) 
(Reg 0x817c=0x00) (Reg 0x817d=0x00) (Reg 0x817e=0x00) (Reg 0x817f=0x00) 

NVR 4 Registers:

(Reg 0x8180=0x00) 

VR 1 Registers:

(Reg 0xa000=0x0000) (Reg 0xa001=0x1234) (Reg 0xa002=0x0000) (Reg 0xa003=0x0000) 
(Reg 0xa004=0x0000) (Reg 0xa005=0x0000) (Reg 0xa006=0x0000) (Reg 0xa007=0x0000) 
(Reg 0xa008=0x0000) (Reg 0xa009=0x0000) (Reg 0xa00a=0x0000) (Reg 0xa00b=0x0000) 
(Reg 0xa00c=0x0000) (Reg 0xa00d=0x0000) (Reg 0xa00e=0x0000) (Reg 0xa00f=0x0000) 
(Reg 0xa010=0x0000) (Reg 0xa011=0x0200) (Reg 0xa012=0x0200) (Reg 0xa013=0x0000) 
(Reg 0xa014=0x0000) (Reg 0xa015=0x0000) (Reg 0xa016=0x0020) (Reg 0xa017=0x0000) 
(Reg 0xa018=0xb180) (Reg 0xa019=0x03ff) (Reg 0xa01a=0x03ff) (Reg 0xa01b=0x0000) 
(Reg 0xa01c=0x8000) (Reg 0xa01d=0x0002) (Reg 0xa01e=0x0000) (Reg 0xa01f=0x0000) 
(Reg 0xa020=0x0000) (Reg 0xa021=0x8000) (Reg 0xa022=0x003f) (Reg 0xa023=0x0020) 
(Reg 0xa024=0x0000) (Reg 0xa025=0x0000) (Reg 0xa026=0x0000) (Reg 0xa027=0x0000) 
(Reg 0xa028=0x006a) (Reg 0xa029=0xa7f8) (Reg 0xa02a=0x0062) (Reg 0xa02b=0x0ff0) 
(Reg 0xa02c=0x00f0) (Reg 0xa02d=0x0000) (Reg 0xa02e=0x0000) (Reg 0xa02f=0x1b76) 
(Reg 0xa030=0x80df) (Reg 0xa031=0x0000) (Reg 0xa032=0x671e) (Reg 0xa033=0x3069) 
(Reg 0xa034=0x0000) (Reg 0xa035=0x0000) (Reg 0xa036=0x0000) (Reg 0xa037=0x0000) 
(Reg 0xa038=0x0000) (Reg 0xa039=0x0000) (Reg 0xa03a=0x0000) 

NETWORK LANE VR 1 Registers:

(Reg 0xa200=0x0000) (Reg 0xa201=0x0000) (Reg 0xa202=0x0000) (Reg 0xa203=0x0000) 
(Reg 0xa204=0x0000) (Reg 0xa205=0x0000) (Reg 0xa206=0x0000) (Reg 0xa207=0x0000) 
(Reg 0xa208=0x0000) (Reg 0xa209=0x0000) (Reg 0xa20a=0x0000) (Reg 0xa20b=0x0000) 
(Reg 0xa20c=0x0000) (Reg 0xa20d=0x0000) (Reg 0xa20e=0x0000) (Reg 0xa20f=0x0000) 
(Reg 0xa210=0x0000) (Reg 0xa211=0x0000) (Reg 0xa212=0x0000) (Reg 0xa213=0x0000) 
(Reg 0xa214=0x0000) (Reg 0xa215=0x0000) (Reg 0xa216=0x0000) (Reg 0xa217=0x0000) 
(Reg 0xa218=0x0000) (Reg 0xa219=0x0000) (Reg 0xa21a=0x0000) (Reg 0xa21b=0x0000) 
(Reg 0xa21c=0x0000) (Reg 0xa21d=0x0000) (Reg 0xa21e=0x0000) (Reg 0xa21f=0x0000) 
(Reg 0xa220=0x0003) (Reg 0xa221=0x0003) (Reg 0xa222=0x0003) (Reg 0xa223=0x0003) 
(Reg 0xa224=0x0003) (Reg 0xa225=0x0003) (Reg 0xa226=0x0003) (Reg 0xa227=0x0003) 
(Reg 0xa228=0x0003) (Reg 0xa229=0x0003) (Reg 0xa22a=0x0000) (Reg 0xa22b=0x0000) 
(Reg 0xa22c=0x0000) (Reg 0xa22d=0x0000) (Reg 0xa22e=0x0000) (Reg 0xa22f=0x0000) 
(Reg 0xa230=0x0010) (Reg 0xa231=0x0010) (Reg 0xa232=0x0010) (Reg 0xa233=0x0010) 
(Reg 0xa234=0x0010) (Reg 0xa235=0x0010) (Reg 0xa236=0x0010) (Reg 0xa237=0x0010) 
(Reg 0xa238=0x0010) (Reg 0xa239=0x0010) (Reg 0xa23a=0x0000) (Reg 0xa23b=0x0000) 
(Reg 0xa23c=0x0000) (Reg 0xa23d=0x0000) (Reg 0xa23e=0x0000) (Reg 0xa23f=0x0000) 
(Reg 0xa240=0xffff) (Reg 0xa241=0xffff) (Reg 0xa242=0xffff) (Reg 0xa243=0xffff) 
(Reg 0xa244=0xffff) (Reg 0xa245=0xffff) (Reg 0xa246=0xffff) (Reg 0xa247=0xffff) 
(Reg 0xa248=0xffff) (Reg 0xa249=0xffff) (Reg 0xa24a=0x0000) (Reg 0xa24b=0x0000) 
(Reg 0xa24c=0x0000) (Reg 0xa24d=0x0000) (Reg 0xa24e=0x0000) (Reg 0xa24f=0x0000) 
(Reg 0xa250=0xe0dc) (Reg 0xa251=0xe0dc) (Reg 0xa252=0xe0dc) (Reg 0xa253=0xe0dc) 
(Reg 0xa254=0xe0dc) (Reg 0xa255=0xe0dc) (Reg 0xa256=0xe0dc) (Reg 0xa257=0xe0dc) 
(Reg 0xa258=0xe0dc) (Reg 0xa259=0xe0dc) (Reg 0xa25a=0x0000) (Reg 0xa25b=0x0000) 
(Reg 0xa25c=0x0000) (Reg 0xa25d=0x0000) (Reg 0xa25e=0x0000) (Reg 0xa25f=0x0000) 
(Reg 0xa260=0x0000) 

NETWORK LANE VR 2 Registers:

(Reg 0xa280=0x0000) (Reg 0xa281=0x0000) (Reg 0xa282=0x0000) (Reg 0xa283=0x0000) 
(Reg 0xa284=0x0000) (Reg 0xa285=0x0000) (Reg 0xa286=0x0000) (Reg 0xa287=0x0000) 
(Reg 0xa288=0x0000) (Reg 0xa289=0x0000) (Reg 0xa28a=0x0000) (Reg 0xa28b=0x0000) 
(Reg 0xa28c=0x0000) (Reg 0xa28d=0x0000) (Reg 0xa28e=0x0000) (Reg 0xa28f=0x0000) 
(Reg 0xa290=0x0000) (Reg 0xa291=0x0000) (Reg 0xa292=0x0000) (Reg 0xa293=0x0000) 
(Reg 0xa294=0x0000) (Reg 0xa295=0x0000) (Reg 0xa296=0x0000) (Reg 0xa297=0x0000) 
(Reg 0xa298=0x0000) (Reg 0xa299=0x0000) (Reg 0xa29a=0x0000) (Reg 0xa29b=0x0000) 
(Reg 0xa29c=0x0000) (Reg 0xa29d=0x0000) (Reg 0xa29e=0x0000) (Reg 0xa29f=0x0000) 
(Reg 0xa2a0=0x0b3f) (Reg 0xa2a1=0x0b68) (Reg 0xa2a2=0x0b6b) (Reg 0xa2a3=0x0b52) 
(Reg 0xa2a4=0x0b95) (Reg 0xa2a5=0x0ad8) (Reg 0xa2a6=0x0b44) (Reg 0xa2a7=0x0afa) 
(Reg 0xa2a8=0x0b15) (Reg 0xa2a9=0x0b81) (Reg 0xa2aa=0x0000) (Reg 0xa2ab=0x0000) 
(Reg 0xa2ac=0x0000) (Reg 0xa2ad=0x0000) (Reg 0xa2ae=0x0000) (Reg 0xa2af=0x0000) 
(Reg 0xa2b0=0x1580) (Reg 0xa2b1=0x1486) (Reg 0xa2b2=0x13e6) (Reg 0xa2b3=0x14d1) 
(Reg 0xa2b4=0x12fb) (Reg 0xa2b5=0x1410) (Reg 0xa2b6=0x140b) (Reg 0xa2b7=0x1525) 
(Reg 0xa2b8=0x1402) (Reg 0xa2b9=0x14e4) (Reg 0xa2ba=0x0000) (Reg 0xa2bb=0x0000) 
(Reg 0xa2bc=0x0000) (Reg 0xa2bd=0x0000) (Reg 0xa2be=0x0000) (Reg 0xa2bf=0x0000) 
(Reg 0xa2c0=0x2276) (Reg 0xa2c1=0x2276) (Reg 0xa2c2=0x2276) (Reg 0xa2c3=0x2276) 
(Reg 0xa2c4=0x2276) (Reg 0xa2c5=0x2276) (Reg 0xa2c6=0x2276) (Reg 0xa2c7=0x2276) 
(Reg 0xa2c8=0x2276) (Reg 0xa2c9=0x2276) (Reg 0xa2ca=0x0000) (Reg 0xa2cb=0x0000) 
(Reg 0xa2cc=0x0000) (Reg 0xa2cd=0x0000) (Reg 0xa2ce=0x0000) (Reg 0xa2cf=0x0000) 
(Reg 0xa2d0=0x1483) (Reg 0xa2d1=0x14e1) (Reg 0xa2d2=0x16f2) (Reg 0xa2d3=0x12f7) 
(Reg 0xa2d4=0x10b7) (Reg 0xa2d5=0x148c) (Reg 0xa2d6=0x13b7) (Reg 0xa2d7=0x1143) 
(Reg 0xa2d8=0x15ea) (Reg 0xa2d9=0x11ee) (Reg 0xa2da=0x0000) (Reg 0xa2db=0x0000) 
(Reg 0xa2dc=0x0000) (Reg 0xa2dd=0x0000) (Reg 0xa2de=0x0000) (Reg 0xa2df=0x0000) 
(Reg 0xa2e0=0x0000) 

HOST LANE VR 1 Registers:

(Reg 0xa400=0x0000) (Reg 0xa401=0x0000) (Reg 0xa402=0x0000) (Reg 0xa403=0x0000) 
(Reg 0xa404=0x0000) (Reg 0xa405=0x0000) (Reg 0xa406=0x0000) (Reg 0xa407=0x0000) 
(Reg 0xa408=0x0000) (Reg 0xa409=0x0000) (Reg 0xa40a=0x0000) (Reg 0xa40b=0x0000) 
(Reg 0xa40c=0x0000) (Reg 0xa40d=0x0000) (Reg 0xa40e=0x0000) (Reg 0xa40f=0x0000) 
(Reg 0xa410=0x0000) (Reg 0xa411=0x0000) (Reg 0xa412=0x0000) (Reg 0xa413=0x0000) 
(Reg 0xa414=0x0000) (Reg 0xa415=0x0000) (Reg 0xa416=0x0000) (Reg 0xa417=0x0000) 
(Reg 0xa418=0x0000) (Reg 0xa419=0x0000) (Reg 0xa41a=0x0000) (Reg 0xa41b=0x0000) 
(Reg 0xa41c=0x0000) (Reg 0xa41d=0x0000) (Reg 0xa41e=0x0000) (Reg 0xa41f=0x0000) 
(Reg 0xa420=0x0001) (Reg 0xa421=0x0001) (Reg 0xa422=0x0001) (Reg 0xa423=0x0001) 
(Reg 0xa424=0x0001) (Reg 0xa425=0x0001) (Reg 0xa426=0x0001) (Reg 0xa427=0x0001) 
(Reg 0xa428=0x0001) (Reg 0xa429=0x0001) (Reg 0xa42a=0x0000) (Reg 0xa42b=0x0000) 
(Reg 0xa42c=0x0000) (Reg 0xa42d=0x0000) (Reg 0xa42e=0x0000) (Reg 0xa42f=0x0000) 
(Reg 0xa430=0x0000) (Reg 0xa431=0x0000) (Reg 0xa432=0x0000) (Reg 0xa433=0x0000) 
(Reg 0xa434=0x0000) (Reg 0xa435=0x0000) (Reg 0xa436=0x0000) (Reg 0xa437=0x0000) 
(Reg 0xa438=0x0000) (Reg 0xa439=0x0000) (Reg 0xa43a=0x0000) (Reg 0xa43b=0x0000) 
(Reg 0xa43c=0x0000) (Reg 0xa43d=0x0000) (Reg 0xa43e=0x0000) (Reg 0xa43f=0x0000) 
(Reg 0xa440=0x0007) (Reg 0xa441=0x0007) (Reg 0xa442=0x0007) (Reg 0xa443=0x0007) 
(Reg 0xa444=0x0007) (Reg 0xa445=0x0007) (Reg 0xa446=0x0007) (Reg 0xa447=0x0007) 
(Reg 0xa448=0x0007) (Reg 0xa449=0x0007) (Reg 0xa44a=0x0000) (Reg 0xa44b=0x0000) 
(Reg 0xa44c=0x0000) (Reg 0xa44d=0x0000) (Reg 0xa44e=0x0000) (Reg 0xa44f=0x0000) 
(Reg 0xa450=0x0000) 

Regs Info
OTN Controller 1 common register:

TOP_MPIF Block : 
---------------------------
Addr     Name                            Value
0x00002  GLOBAL_CFG                      0x0051
0x00004  SCRATCH_PAD1                    0x00ef
0x00005  SCRATCH_PAD2                    0xc400
0x00009  GPIO_CONTROL                    0x0000
 
SDS_COMMON Block : BANK B
---------------------------
Addr     Name                            Value
0x0241f  RXLOCKD0_INTSTATUS 3            0x0018
0x02445  RXLOCKD1_INTSTATUS 3            0x0008
0x0246b  RXLOCKD2_INTSTATUS 3            0x001c
0x02491  RXLOCKD3_INTSTATUS 3            0x0000
0x024b9  TXLOCKD0_INTSTATUS 3            0x000c
0x0281f  RXLOCKD0_INTSTATUS 4            0x0008
0x02845  RXLOCKD1_INTSTATUS 4            0x0008
0x0286b  RXLOCKD2_INTSTATUS 4            0x0008
0x02891  RXLOCKD3_INTSTATUS 4            0x000c
0x028b9  TXLOCKD0_INTSTATUS 4            0x0009

SDS_COMMON Block : BANK C
---------------------------
Addr     Name                            Value
0x0301f  RXLOCKD0_INTSTATUS 6            0x0049
0x03045  RXLOCKD1_INTSTATUS 6            0x0049
0x0306b  RXLOCKD2_INTSTATUS 6            0x0049
0x03091  RXLOCKD3_INTSTATUS 6            0x0049
0x030b9  TXLOCKD0_INTSTATUS 6            0x0049
0x0341f  RXLOCKD0_INTSTATUS 7            0x0049
0x03445  RXLOCKD1_INTSTATUS 7            0x0049
0x0346b  RXLOCKD2_INTSTATUS 7            0x0049
0x03491  RXLOCKD3_INTSTATUS 7            0x0049
0x034b9  TXLOCKD0_INTSTATUS 7            0x0049

ILKN_CORE Block : 
---------------------------
Addr     Name                            Value
0x19d6b  RX_INTERLAKEN_STATUS0           0x0049
0x19d6c  RX_INTERLAKEN_SYNCED1           0x0049
0x19d6d  RX_INTERLAKEN_SYNCED0           0x0049
0x19d66  RX_OOBFC_RX_LANE_STATUS1        0x0049
0x19d67  RX_OOBFC_RX_LANE_STATUS0        0x0049
0x19d62  TX_INTERLAKEN_STATUS1           0x0049
0x19d63  TX_INTERLAKEN_STATUS0           0x0049

Port/1 register:

SDS_COMMON Block : line
---------------------------
Addr     Name                            Value
0x0181f  RXLOCKD0_INTSTATUS 0            0x0049
0x01845  RXLOCKD1_INTSTATUS 0            0x0049
0x0186b  RXLOCKD2_INTSTATUS 0            0x0049
0x01891  RXLOCKD3_INTSTATUS 0            0x0049
0x018b9  TXLOCKD0_INTSTATUS 0            0x0049

CPAK Registers:
================
 
NVR 1 Registers:

(Reg 0x8000=0x01) (Reg 0x8001=0x21) (Reg 0x8002=0x09) (Reg 0x8003=0x03) 
(Reg 0x8004=0x00) (Reg 0x8005=0x00) (Reg 0x8006=0x00) (Reg 0x8007=0x00) 
(Reg 0x8008=0x1e) (Reg 0x8009=0xaa) (Reg 0x800a=0x4a) (Reg 0x800b=0x38) 
(Reg 0x800c=0x38) (Reg 0x800d=0x00) (Reg 0x800e=0x0a) (Reg 0x800f=0x00) 
 (Reg 0x8010=0x0a) (Reg 0x8011=0x01) (Reg 0x8012=0x83) (Reg 0x8013=0x40) 
(Reg 0x8014=0x86) (Reg 0x8015=0x60) (Reg 0x8016=0x00) (Reg 0x8017=0x00) 
(Reg 0x8018=0x00) (Reg 0x8019=0x04) (Reg 0x801a=0x40) (Reg 0x801b=0x50) 
(Reg 0x801c=0x26) (Reg 0x801d=0x17) (Reg 0x801e=0x14) (Reg 0x801f=0x46) 
(Reg 0x8020=0x00) (Reg 0x8021=0x43) (Reg 0x8022=0x49) (Reg 0x8023=0x53) 
(Reg 0x8024=0x43) (Reg 0x8025=0x4f) (Reg 0x8026=0x20) (Reg 0x8027=0x20) 
(Reg 0x8028=0x20) (Reg 0x8029=0x20) (Reg 0x802a=0x20) (Reg 0x802b=0x20) 
(Reg 0x802c=0x20) (Reg 0x802d=0x20) (Reg 0x802e=0x20) (Reg 0x802f=0x20) 
(Reg 0x8030=0x20) (Reg 0x8031=0x00) (Reg 0x8032=0x00) (Reg 0x8033=0x0c) 
(Reg 0x8034=0x38) (Reg 0x8035=0x30) (Reg 0x8036=0x30) (Reg 0x8037=0x2d) 
 (Reg 0x8038=0x34) (Reg 0x8039=0x31) (Reg 0x803a=0x34) (Reg 0x803b=0x39) 
(Reg 0x803c=0x35) (Reg 0x803d=0x2d) (Reg 0x803e=0x30) (Reg 0x803f=0x31) 
(Reg 0x8040=0x20) (Reg 0x8041=0x20) (Reg 0x8042=0x20) (Reg 0x8043=0x20) 
(Reg 0x8044=0x46) (Reg 0x8045=0x42) (Reg 0x8046=0x4e) (Reg 0x8047=0x31) 
(Reg 0x8048=0x39) (Reg 0x8049=0x30) (Reg 0x804a=0x39) (Reg 0x804b=0x32) 
(Reg 0x804c=0x31) (Reg 0x804d=0x31) (Reg 0x804e=0x31) (Reg 0x804f=0x20) 
(Reg 0x8050=0x20) (Reg 0x8051=0x20) (Reg 0x8052=0x20) (Reg 0x8053=0x20) 
(Reg 0x8054=0x32) (Reg 0x8055=0x30) (Reg 0x8056=0x31) (Reg 0x8057=0x35) 
(Reg 0x8058=0x30) (Reg 0x8059=0x33) (Reg 0x805a=0x30) (Reg 0x805b=0x35) 
(Reg 0x805c=0x00) (Reg 0x805d=0x00) (Reg 0x805e=0x57) (Reg 0x805f=0x4f) 
 (Reg 0x8060=0x54) (Reg 0x8061=0x52) (Reg 0x8062=0x43) (Reg 0x8063=0x35) 
(Reg 0x8064=0x50) (Reg 0x8065=0x42) (Reg 0x8066=0x41) (Reg 0x8067=0x41) 
(Reg 0x8068=0x6e) (Reg 0x8069=0x5a) (Reg 0x806a=0x00) (Reg 0x806b=0x05) 
(Reg 0x806c=0x02) (Reg 0x806d=0x03) (Reg 0x806e=0x0c) (Reg 0x806f=0x03) 
(Reg 0x8070=0x0f) (Reg 0x8071=0x20) (Reg 0x8072=0x01) (Reg 0x8073=0x01) 
(Reg 0x8074=0x08) (Reg 0x8075=0x00) (Reg 0x8076=0xfe) (Reg 0x8077=0x01) 
(Reg 0x8078=0x00) (Reg 0x8079=0x00) (Reg 0x807a=0x00) (Reg 0x807b=0x02) 
(Reg 0x807c=0x03) (Reg 0x807d=0x00) (Reg 0x807e=0x00) (Reg 0x807f=0xe4) 

NVR 2 Registers:

(Reg 0x8080=0x4b) (Reg 0x8081=0x00) (Reg 0x8082=0x46) (Reg 0x8083=0x00) 
(Reg 0x8084=0x00) (Reg 0x8085=0x00) (Reg 0x8086=0xfb) (Reg 0x8087=0x00) 
(Reg 0x8088=0x8a) (Reg 0x8089=0x00) (Reg 0x808a=0x87) (Reg 0x808b=0x5a) 
(Reg 0x808c=0x7a) (Reg 0x808d=0x76) (Reg 0x808e=0x77) (Reg 0x808f=0xe2) 
(Reg 0x8090=0x00) (Reg 0x8091=0x00) (Reg 0x8092=0x00) (Reg 0x8093=0x00) 
 (Reg 0x8094=0x00) (Reg 0x8095=0x00) (Reg 0x8096=0x00) (Reg 0x8097=0x00) 
(Reg 0x8098=0x00) (Reg 0x8099=0x00) (Reg 0x809a=0x00) (Reg 0x809b=0x00) 
(Reg 0x809c=0x00) (Reg 0x809d=0x00) (Reg 0x809e=0x00) (Reg 0x809f=0x00) 
(Reg 0x80a0=0x00) (Reg 0x80a1=0x00) (Reg 0x80a2=0x00) (Reg 0x80a3=0x00) 
(Reg 0x80a4=0x00) (Reg 0x80a5=0x00) (Reg 0x80a6=0x00) (Reg 0x80a7=0x00) 
(Reg 0x80a8=0x13) (Reg 0x80a9=0x88) (Reg 0x80aa=0x11) (Reg 0x80ab=0x94) 
(Reg 0x80ac=0x05) (Reg 0x80ad=0xdc) (Reg 0x80ae=0x03) (Reg 0x80af=0xe8) 
(Reg 0x80b0=0x45) (Reg 0x80b1=0x76) (Reg 0x80b2=0x22) (Reg 0x80b3=0xd0) 
(Reg 0x80b4=0x06) (Reg 0x80b5=0xc9) (Reg 0x80b6=0x03) (Reg 0x80b7=0x66) 
(Reg 0x80b8=0x5a) (Reg 0x80b9=0x00) (Reg 0x80ba=0x55) (Reg 0x80bb=0x00) 
 (Reg 0x80bc=0x00) (Reg 0x80bd=0x00) (Reg 0x80be=0xfb) (Reg 0x80bf=0x00) 
(Reg 0x80c0=0x88) (Reg 0x80c1=0x71) (Reg 0x80c2=0x43) (Reg 0x80c3=0xe2) 
(Reg 0x80c4=0x04) (Reg 0x80c5=0x62) (Reg 0x80c6=0x02) (Reg 0x80c7=0x32) 
(Reg 0x80c8=0x00) (Reg 0x80c9=0x00) (Reg 0x80ca=0x00) (Reg 0x80cb=0x00) 
(Reg 0x80cc=0x00) (Reg 0x80cd=0x00) (Reg 0x80ce=0x00) (Reg 0x80cf=0x00) 
(Reg 0x80d0=0x00) (Reg 0x80d1=0x00) (Reg 0x80d2=0x00) (Reg 0x80d3=0x00) 
(Reg 0x80d4=0x00) (Reg 0x80d5=0x00) (Reg 0x80d6=0x00) (Reg 0x80d7=0x00) 
(Reg 0x80d8=0x00) (Reg 0x80d9=0x00) (Reg 0x80da=0x00) (Reg 0x80db=0x00) 
(Reg 0x80dc=0x00) (Reg 0x80dd=0x00) (Reg 0x80de=0x00) (Reg 0x80df=0x00) 
(Reg 0x80e0=0x00) (Reg 0x80e1=0x00) (Reg 0x80e2=0x00) (Reg 0x80e3=0x00) 
 (Reg 0x80e4=0x00) (Reg 0x80e5=0x00) (Reg 0x80e6=0x00) (Reg 0x80e7=0x00) 
(Reg 0x80e8=0x00) (Reg 0x80e9=0x00) (Reg 0x80ea=0x00) (Reg 0x80eb=0x00) 
(Reg 0x80ec=0x00) (Reg 0x80ed=0x00) (Reg 0x80ee=0x00) (Reg 0x80ef=0x00) 
(Reg 0x80f0=0x00) (Reg 0x80f1=0x00) (Reg 0x80f2=0x00) (Reg 0x80f3=0x00) 
(Reg 0x80f4=0x00) (Reg 0x80f5=0x00) (Reg 0x80f6=0x00) (Reg 0x80f7=0x00) 
(Reg 0x80f8=0x00) (Reg 0x80f9=0x00) (Reg 0x80fa=0x00) (Reg 0x80fb=0x00) 
(Reg 0x80fc=0x00) (Reg 0x80fd=0x00) (Reg 0x80fe=0x00) (Reg 0x80ff=0x93) 

NVR 3 Registers:

(Reg 0x8100=0x00) (Reg 0x8101=0x00) (Reg 0x8102=0x00) (Reg 0x8103=0x00) 
(Reg 0x8104=0x00) (Reg 0x8105=0x00) (Reg 0x8106=0x00) (Reg 0x8107=0x00) 
(Reg 0x8108=0x00) (Reg 0x8109=0x00) (Reg 0x810a=0x00) (Reg 0x810b=0x00) 
(Reg 0x810c=0x00) (Reg 0x810d=0x00) (Reg 0x810e=0x00) (Reg 0x810f=0x00) 
(Reg 0x8110=0x00) (Reg 0x8111=0x00) (Reg 0x8112=0x00) (Reg 0x8113=0x00) 
(Reg 0x8114=0x00) (Reg 0x8115=0x00) (Reg 0x8116=0x00) (Reg 0x8117=0x00) 
 (Reg 0x8118=0x00) (Reg 0x8119=0x00) (Reg 0x811a=0x00) (Reg 0x811b=0x00) 
(Reg 0x811c=0x00) (Reg 0x811d=0x00) (Reg 0x811e=0x00) (Reg 0x811f=0x00) 
(Reg 0x8120=0x00) (Reg 0x8121=0x00) (Reg 0x8122=0x00) (Reg 0x8123=0x00) 
(Reg 0x8124=0x00) (Reg 0x8125=0x00) (Reg 0x8126=0x00) (Reg 0x8127=0x00) 
(Reg 0x8128=0x00) (Reg 0x8129=0x00) (Reg 0x812a=0x00) (Reg 0x812b=0x00) 
(Reg 0x812c=0x00) (Reg 0x812d=0x00) (Reg 0x812e=0x00) (Reg 0x812f=0x00) 
(Reg 0x8130=0x00) (Reg 0x8131=0x00) (Reg 0x8132=0x00) (Reg 0x8133=0x00) 
(Reg 0x8134=0x00) (Reg 0x8135=0x00) (Reg 0x8136=0x00) (Reg 0x8137=0x00) 
(Reg 0x8138=0x00) (Reg 0x8139=0x00) (Reg 0x813a=0x00) (Reg 0x813b=0x00) 
(Reg 0x813c=0x00) (Reg 0x813d=0x00) (Reg 0x813e=0x00) (Reg 0x813f=0x00) 
 (Reg 0x8140=0x00) (Reg 0x8141=0x00) (Reg 0x8142=0x00) (Reg 0x8143=0x00) 
(Reg 0x8144=0x00) (Reg 0x8145=0x00) (Reg 0x8146=0x00) (Reg 0x8147=0x00) 
(Reg 0x8148=0x00) (Reg 0x8149=0x00) (Reg 0x814a=0x00) (Reg 0x814b=0x00) 
(Reg 0x814c=0x00) (Reg 0x814d=0x00) (Reg 0x814e=0x00) (Reg 0x814f=0x00) 
(Reg 0x8150=0x00) (Reg 0x8151=0x00) (Reg 0x8152=0x00) (Reg 0x8153=0x00) 
(Reg 0x8154=0x00) (Reg 0x8155=0x00) (Reg 0x8156=0x00) (Reg 0x8157=0x00) 
(Reg 0x8158=0x00) (Reg 0x8159=0x00) (Reg 0x815a=0x00) (Reg 0x815b=0x00) 
(Reg 0x815c=0x00) (Reg 0x815d=0x00) (Reg 0x815e=0x00) (Reg 0x815f=0x00) 
(Reg 0x8160=0x00) (Reg 0x8161=0x00) (Reg 0x8162=0x00) (Reg 0x8163=0x00) 
(Reg 0x8164=0x00) (Reg 0x8165=0x00) (Reg 0x8166=0x00) (Reg 0x8167=0x00) 
 (Reg 0x8168=0x00) (Reg 0x8169=0x00) (Reg 0x816a=0x00) (Reg 0x816b=0x00) 
(Reg 0x816c=0x00) (Reg 0x816d=0x00) (Reg 0x816e=0x00) (Reg 0x816f=0x00) 
(Reg 0x8170=0x00) (Reg 0x8171=0x00) (Reg 0x8172=0x00) (Reg 0x8173=0x00) 
(Reg 0x8174=0x00) (Reg 0x8175=0x00) (Reg 0x8176=0x00) (Reg 0x8177=0x00) 
(Reg 0x8178=0x00) (Reg 0x8179=0x00) (Reg 0x817a=0x00) (Reg 0x817b=0x00) 
(Reg 0x817c=0x00) (Reg 0x817d=0x00) (Reg 0x817e=0x00) (Reg 0x817f=0x00) 

NVR 4 Registers:

(Reg 0x8180=0x00) 

 VR 1 Registers:

(Reg 0xa000=0x0000) (Reg 0xa001=0x1234) (Reg 0xa002=0x0000) (Reg 0xa003=0x0000) 
(Reg 0xa004=0x0000) (Reg 0xa005=0x0000) (Reg 0xa006=0x0000) (Reg 0xa007=0x0000) 
(Reg 0xa008=0x0000) (Reg 0xa009=0x0000) (Reg 0xa00a=0x0000) (Reg 0xa00b=0x0000) 
(Reg 0xa00c=0x0000) (Reg 0xa00d=0x0000) (Reg 0xa00e=0x0000) (Reg 0xa00f=0x0000) 
(Reg 0xa010=0x0000) (Reg 0xa011=0x0200) (Reg 0xa012=0x0200) (Reg 0xa013=0x0000) 
(Reg 0xa014=0x0000) (Reg 0xa015=0x0000) (Reg 0xa016=0x0020) (Reg 0xa017=0x0000) 
(Reg 0xa018=0xb180) (Reg 0xa019=0x03ff) (Reg 0xa01a=0x03ff) (Reg 0xa01b=0x0000) 
(Reg 0xa01c=0x8000) (Reg 0xa01d=0x0002) (Reg 0xa01e=0x0000) (Reg 0xa01f=0x0000) 
(Reg 0xa020=0x0000) (Reg 0xa021=0x8000) (Reg 0xa022=0x003f) (Reg 0xa023=0x0020) 
(Reg 0xa024=0x0000) (Reg 0xa025=0x0000) (Reg 0xa026=0x0000) (Reg 0xa027=0x0000) 
(Reg 0xa028=0x006a) (Reg 0xa029=0xa7f8) (Reg 0xa02a=0x0062) (Reg 0xa02b=0x0ff0) 
(Reg 0xa02c=0x00f0) (Reg 0xa02d=0x0000) (Reg 0xa02e=0x0000) (Reg 0xa02f=0x19d5) 
(Reg 0xa030=0x80ae) (Reg 0xa031=0x0000) (Reg 0xa032=0x6566) (Reg 0xa033=0x3138) 
(Reg 0xa034=0x0000) (Reg 0xa035=0x0000) (Reg 0xa036=0x0000) (Reg 0xa037=0x0000) 
(Reg 0xa038=0x0000) (Reg 0xa039=0x0000) (Reg 0xa03a=0x0000) 

NETWORK LANE VR 1 Registers:

(Reg 0xa200=0x0000) (Reg 0xa201=0x0000) (Reg 0xa202=0x0000) (Reg 0xa203=0x0000) 
(Reg 0xa204=0x0000) (Reg 0xa205=0x0000) (Reg 0xa206=0x0000) (Reg 0xa207=0x0000) 
(Reg 0xa208=0x0000) (Reg 0xa209=0x0000) (Reg 0xa20a=0x0000) (Reg 0xa20b=0x0000) 
(Reg 0xa20c=0x0000) (Reg 0xa20d=0x0000) (Reg 0xa20e=0x0000) (Reg 0xa20f=0x0000) 
(Reg 0xa210=0x0000) (Reg 0xa211=0x0000) (Reg 0xa212=0x0000) (Reg 0xa213=0x0000) 
(Reg 0xa214=0x0000) (Reg 0xa215=0x0000) (Reg 0xa216=0x0000) (Reg 0xa217=0x0000) 
(Reg 0xa218=0x0000) (Reg 0xa219=0x0000) (Reg 0xa21a=0x0000) (Reg 0xa21b=0x0000) 
(Reg 0xa21c=0x0000) (Reg 0xa21d=0x0000) (Reg 0xa21e=0x0000) (Reg 0xa21f=0x0000) 
(Reg 0xa220=0x0003) (Reg 0xa221=0x0003) (Reg 0xa222=0x0003) (Reg 0xa223=0x0003) 
(Reg 0xa224=0x0003) (Reg 0xa225=0x0003) (Reg 0xa226=0x0003) (Reg 0xa227=0x0003) 
(Reg 0xa228=0x0003) (Reg 0xa229=0x0003) (Reg 0xa22a=0x0000) (Reg 0xa22b=0x0000) 
(Reg 0xa22c=0x0000) (Reg 0xa22d=0x0000) (Reg 0xa22e=0x0000) (Reg 0xa22f=0x0000) 
(Reg 0xa230=0x0010) (Reg 0xa231=0x0010) (Reg 0xa232=0x0010) (Reg 0xa233=0x0010) 
(Reg 0xa234=0x0010) (Reg 0xa235=0x0010) (Reg 0xa236=0x0010) (Reg 0xa237=0x0010) 
(Reg 0xa238=0x0010) (Reg 0xa239=0x0010) (Reg 0xa23a=0x0000) (Reg 0xa23b=0x0000) 
(Reg 0xa23c=0x0000) (Reg 0xa23d=0x0000) (Reg 0xa23e=0x0000) (Reg 0xa23f=0x0000) 
(Reg 0xa240=0xffff) (Reg 0xa241=0xffff) (Reg 0xa242=0xffff) (Reg 0xa243=0xffff) 
(Reg 0xa244=0xffff) (Reg 0xa245=0xffff) (Reg 0xa246=0xffff) (Reg 0xa247=0xffff) 
(Reg 0xa248=0xffff) (Reg 0xa249=0xffff) (Reg 0xa24a=0x0000) (Reg 0xa24b=0x0000) 
(Reg 0xa24c=0x0000) (Reg 0xa24d=0x0000) (Reg 0xa24e=0x0000) (Reg 0xa24f=0x0000) 
(Reg 0xa250=0xe0dc) (Reg 0xa251=0xe0dc) (Reg 0xa252=0xe0dc) (Reg 0xa253=0xe0dc) 
(Reg 0xa254=0xe0dc) (Reg 0xa255=0xe0dc) (Reg 0xa256=0xe0dc) (Reg 0xa257=0xe0dc) 
(Reg 0xa258=0xe0dc) (Reg 0xa259=0xe0dc) (Reg 0xa25a=0x0000) (Reg 0xa25b=0x0000) 
(Reg 0xa25c=0x0000) (Reg 0xa25d=0x0000) (Reg 0xa25e=0x0000) (Reg 0xa25f=0x0000) 
(Reg 0xa260=0x0000) 

NETWORK LANE VR 2 Registers:

(Reg 0xa280=0x0000) (Reg 0xa281=0x0000) (Reg 0xa282=0x0000) (Reg 0xa283=0x0000) 
(Reg 0xa284=0x0000) (Reg 0xa285=0x0000) (Reg 0xa286=0x0000) (Reg 0xa287=0x0000) 
(Reg 0xa288=0x0000) (Reg 0xa289=0x0000) (Reg 0xa28a=0x0000) (Reg 0xa28b=0x0000) 
(Reg 0xa28c=0x0000) (Reg 0xa28d=0x0000) (Reg 0xa28e=0x0000) (Reg 0xa28f=0x0000) 
(Reg 0xa290=0x0000) (Reg 0xa291=0x0000) (Reg 0xa292=0x0000) (Reg 0xa293=0x0000) 
(Reg 0xa294=0x0000) (Reg 0xa295=0x0000) (Reg 0xa296=0x0000) (Reg 0xa297=0x0000) 
(Reg 0xa298=0x0000) (Reg 0xa299=0x0000) (Reg 0xa29a=0x0000) (Reg 0xa29b=0x0000) 
(Reg 0xa29c=0x0000) (Reg 0xa29d=0x0000) (Reg 0xa29e=0x0000) (Reg 0xa29f=0x0000) 
(Reg 0xa2a0=0x0b28) (Reg 0xa2a1=0x0b5a) (Reg 0xa2a2=0x0b36) (Reg 0xa2a3=0x0adb) 
(Reg 0xa2a4=0x0ad2) (Reg 0xa2a5=0x0af8) (Reg 0xa2a6=0x0b1c) (Reg 0xa2a7=0x0ae7) 
(Reg 0xa2a8=0x0a76) (Reg 0xa2a9=0x0b3e) (Reg 0xa2aa=0x0000) (Reg 0xa2ab=0x0000) 
(Reg 0xa2ac=0x0000) (Reg 0xa2ad=0x0000) (Reg 0xa2ae=0x0000) (Reg 0xa2af=0x0000) 
(Reg 0xa2b0=0x1511) (Reg 0xa2b1=0x12e6) (Reg 0xa2b2=0x14d7) (Reg 0xa2b3=0x13b3) 
(Reg 0xa2b4=0x13ed) (Reg 0xa2b5=0x1292) (Reg 0xa2b6=0x1452) (Reg 0xa2b7=0x135a) 
(Reg 0xa2b8=0x157a) (Reg 0xa2b9=0x1339) (Reg 0xa2ba=0x0000) (Reg 0xa2bb=0x0000) 
(Reg 0xa2bc=0x0000) (Reg 0xa2bd=0x0000) (Reg 0xa2be=0x0000) (Reg 0xa2bf=0x0000) 
(Reg 0xa2c0=0x20d5) (Reg 0xa2c1=0x20d5) (Reg 0xa2c2=0x20d5) (Reg 0xa2c3=0x20d5) 
(Reg 0xa2c4=0x20d5) (Reg 0xa2c5=0x20d5) (Reg 0xa2c6=0x20d5) (Reg 0xa2c7=0x20d5) 
(Reg 0xa2c8=0x20d5) (Reg 0xa2c9=0x20d5) (Reg 0xa2ca=0x0000) (Reg 0xa2cb=0x0000) 
(Reg 0xa2cc=0x0000) (Reg 0xa2cd=0x0000) (Reg 0xa2ce=0x0000) (Reg 0xa2cf=0x0000) 
(Reg 0xa2d0=0x15e1) (Reg 0xa2d1=0x1627) (Reg 0xa2d2=0x167e) (Reg 0xa2d3=0x1638) 
(Reg 0xa2d4=0x179e) (Reg 0xa2d5=0x1740) (Reg 0xa2d6=0x17b5) (Reg 0xa2d7=0x172f) 
(Reg 0xa2d8=0x17e9) (Reg 0xa2d9=0x173d) (Reg 0xa2da=0x0000) (Reg 0xa2db=0x0000) 
(Reg 0xa2dc=0x0000) (Reg 0xa2dd=0x0000) (Reg 0xa2de=0x0000) (Reg 0xa2df=0x0000) 
(Reg 0xa2e0=0x0000) 

HOST LANE VR 1 Registers:

 (Reg 0xa400=0x0000) (Reg 0xa401=0x0000) (Reg 0xa402=0x0000) (Reg 0xa403=0x0000) 
(Reg 0xa404=0x0000) (Reg 0xa405=0x0000) (Reg 0xa406=0x0000) (Reg 0xa407=0x0000) 
(Reg 0xa408=0x0000) (Reg 0xa409=0x0000) (Reg 0xa40a=0x0000) (Reg 0xa40b=0x0000) 
(Reg 0xa40c=0x0000) (Reg 0xa40d=0x0000) (Reg 0xa40e=0x0000) (Reg 0xa40f=0x0000) 
(Reg 0xa410=0x0000) (Reg 0xa411=0x0000) (Reg 0xa412=0x0000) (Reg 0xa413=0x0000) 
(Reg 0xa414=0x0000) (Reg 0xa415=0x0000) (Reg 0xa416=0x0000) (Reg 0xa417=0x0000) 
(Reg 0xa418=0x0000) (Reg 0xa419=0x0000) (Reg 0xa41a=0x0000) (Reg 0xa41b=0x0000) 
(Reg 0xa41c=0x0000) (Reg 0xa41d=0x0000) (Reg 0xa41e=0x0000) (Reg 0xa41f=0x0000) 
(Reg 0xa420=0x0001) (Reg 0xa421=0x0001) (Reg 0xa422=0x0001) (Reg 0xa423=0x0001) 
(Reg 0xa424=0x0001) (Reg 0xa425=0x0001) (Reg 0xa426=0x0001) (Reg 0xa427=0x0001) 
(Reg 0xa428=0x0001) (Reg 0xa429=0x0001) (Reg 0xa42a=0x0000) (Reg 0xa42b=0x0000) 
(Reg 0xa42c=0x0000) (Reg 0xa42d=0x0000) (Reg 0xa42e=0x0000) (Reg 0xa42f=0x0000) 
(Reg 0xa430=0x0000) (Reg 0xa431=0x0000) (Reg 0xa432=0x0000) (Reg 0xa433=0x0000) 
(Reg 0xa434=0x0000) (Reg 0xa435=0x0000) (Reg 0xa436=0x0000) (Reg 0xa437=0x0000) 
(Reg 0xa438=0x0000) (Reg 0xa439=0x0000) (Reg 0xa43a=0x0000) (Reg 0xa43b=0x0000) 
(Reg 0xa43c=0x0000) (Reg 0xa43d=0x0000) (Reg 0xa43e=0x0000) (Reg 0xa43f=0x0000) 
(Reg 0xa440=0x0007) (Reg 0xa441=0x0007) (Reg 0xa442=0x0007) (Reg 0xa443=0x0007) 
(Reg 0xa444=0x0007) (Reg 0xa445=0x0007) (Reg 0xa446=0x0007) (Reg 0xa447=0x0007) 
(Reg 0xa448=0x0007) (Reg 0xa449=0x0007) (Reg 0xa44a=0x0000) (Reg 0xa44b=0x0000) 
(Reg 0xa44c=0x0000) (Reg 0xa44d=0x0000) (Reg 0xa44e=0x0000) (Reg 0xa44f=0x0000) 
(Reg 0xa450=0x0000) 

Regs Info
OTN Controller 2 common register:

TOP_MPIF Block : 
---------------------------
Addr     Name                            Value
0x00002  GLOBAL_CFG                      0x0051
0x00004  SCRATCH_PAD1                    0x00fb
0x00005  SCRATCH_PAD2                    0xab00
0x00009  GPIO_CONTROL                    0x0000

SDS_COMMON Block : BANK B
---------------------------
Addr     Name                            Value
0x0241f  RXLOCKD0_INTSTATUS 3            0x0009
0x02445  RXLOCKD1_INTSTATUS 3            0x0008
0x0246b  RXLOCKD2_INTSTATUS 3            0x0049
0x02491  RXLOCKD3_INTSTATUS 3            0x0008
0x024b9  TXLOCKD0_INTSTATUS 3            0x0009
0x0281f  RXLOCKD0_INTSTATUS 4            0x0010
0x02845  RXLOCKD1_INTSTATUS 4            0x0009
0x0286b  RXLOCKD2_INTSTATUS 4            0x000c
0x02891  RXLOCKD3_INTSTATUS 4            0x0012
0x028b9  TXLOCKD0_INTSTATUS 4            0x004d

SDS_COMMON Block : BANK C
---------------------------
Addr     Name                            Value
0x0301f  RXLOCKD0_INTSTATUS 6            0x0049
0x03045  RXLOCKD1_INTSTATUS 6            0x0049
0x0306b  RXLOCKD2_INTSTATUS 6            0x0049
0x03091  RXLOCKD3_INTSTATUS 6            0x0049
0x030b9  TXLOCKD0_INTSTATUS 6            0x0049
0x0341f  RXLOCKD0_INTSTATUS 7            0x0049
0x03445  RXLOCKD1_INTSTATUS 7            0x0049
0x0346b  RXLOCKD2_INTSTATUS 7            0x0049
0x03491  RXLOCKD3_INTSTATUS 7            0x0049
0x034b9  TXLOCKD0_INTSTATUS 7            0x0049

ILKN_CORE Block : 
---------------------------
Addr     Name                            Value
0x19d6b  RX_INTERLAKEN_STATUS0           0x0049
0x19d6c  RX_INTERLAKEN_SYNCED1           0x0049
0x19d6d  RX_INTERLAKEN_SYNCED0           0x0049
0x19d66  RX_OOBFC_RX_LANE_STATUS1        0x0049
0x19d67  RX_OOBFC_RX_LANE_STATUS0        0x0049
0x19d62  TX_INTERLAKEN_STATUS1           0x0049
0x19d63  TX_INTERLAKEN_STATUS0           0x0049

Port/2 register:

SDS_COMMON Block : line
---------------------------
Addr     Name                            Value
0x0181f  RXLOCKD0_INTSTATUS 0            0x0049
0x01845  RXLOCKD1_INTSTATUS 0            0x0049
0x0186b  RXLOCKD2_INTSTATUS 0            0x0049
0x01891  RXLOCKD3_INTSTATUS 0            0x0049
0x018b9  TXLOCKD0_INTSTATUS 0            0x0049

CPAK Registers:
 ================

NVR 1 Registers:

(Reg 0x8000=0x01) (Reg 0x8001=0x21) (Reg 0x8002=0x09) (Reg 0x8003=0x03) 
(Reg 0x8004=0x00) (Reg 0x8005=0x00) (Reg 0x8006=0x00) (Reg 0x8007=0x00) 
(Reg 0x8008=0x1e) (Reg 0x8009=0xaa) (Reg 0x800a=0x4a) (Reg 0x800b=0x38) 
(Reg 0x800c=0x38) (Reg 0x800d=0x00) (Reg 0x800e=0x0a) (Reg 0x800f=0x00) 
(Reg 0x8010=0x0a) (Reg 0x8011=0x01) (Reg 0x8012=0x83) (Reg 0x8013=0x40) 
(Reg 0x8014=0x86) (Reg 0x8015=0x60) (Reg 0x8016=0x00) (Reg 0x8017=0x00) 
 (Reg 0x8018=0x00) (Reg 0x8019=0x04) (Reg 0x801a=0x40) (Reg 0x801b=0x50) 
(Reg 0x801c=0x26) (Reg 0x801d=0x17) (Reg 0x801e=0x14) (Reg 0x801f=0x46) 
(Reg 0x8020=0x00) (Reg 0x8021=0x43) (Reg 0x8022=0x49) (Reg 0x8023=0x53) 
(Reg 0x8024=0x43) (Reg 0x8025=0x4f) (Reg 0x8026=0x20) (Reg 0x8027=0x20) 
(Reg 0x8028=0x20) (Reg 0x8029=0x20) (Reg 0x802a=0x20) (Reg 0x802b=0x20) 
(Reg 0x802c=0x20) (Reg 0x802d=0x20) (Reg 0x802e=0x20) (Reg 0x802f=0x20) 
(Reg 0x8030=0x20) (Reg 0x8031=0x00) (Reg 0x8032=0x00) (Reg 0x8033=0x0c) 
(Reg 0x8034=0x38) (Reg 0x8035=0x30) (Reg 0x8036=0x30) (Reg 0x8037=0x2d) 
(Reg 0x8038=0x34) (Reg 0x8039=0x31) (Reg 0x803a=0x34) (Reg 0x803b=0x39) 
(Reg 0x803c=0x35) (Reg 0x803d=0x2d) (Reg 0x803e=0x30) (Reg 0x803f=0x31) 
 (Reg 0x8040=0x20) (Reg 0x8041=0x20) (Reg 0x8042=0x20) (Reg 0x8043=0x20) 
(Reg 0x8044=0x46) (Reg 0x8045=0x42) (Reg 0x8046=0x4e) (Reg 0x8047=0x31) 
(Reg 0x8048=0x39) (Reg 0x8049=0x31) (Reg 0x804a=0x32) (Reg 0x804b=0x32) 
(Reg 0x804c=0x30) (Reg 0x804d=0x32) (Reg 0x804e=0x35) (Reg 0x804f=0x20) 
(Reg 0x8050=0x20) (Reg 0x8051=0x20) (Reg 0x8052=0x20) (Reg 0x8053=0x20) 
(Reg 0x8054=0x32) (Reg 0x8055=0x30) (Reg 0x8056=0x31) (Reg 0x8057=0x35) 
(Reg 0x8058=0x30) (Reg 0x8059=0x33) (Reg 0x805a=0x31) (Reg 0x805b=0x39) 
(Reg 0x805c=0x00) (Reg 0x805d=0x00) (Reg 0x805e=0x57) (Reg 0x805f=0x4f) 
(Reg 0x8060=0x54) (Reg 0x8061=0x52) (Reg 0x8062=0x43) (Reg 0x8063=0x35) 
(Reg 0x8064=0x50) (Reg 0x8065=0x42) (Reg 0x8066=0x41) (Reg 0x8067=0x41) 
 (Reg 0x8068=0x6e) (Reg 0x8069=0x5a) (Reg 0x806a=0x00) (Reg 0x806b=0x05) 
(Reg 0x806c=0x02) (Reg 0x806d=0x03) (Reg 0x806e=0x0c) (Reg 0x806f=0x03) 
(Reg 0x8070=0x0f) (Reg 0x8071=0x20) (Reg 0x8072=0x01) (Reg 0x8073=0x01) 
(Reg 0x8074=0x08) (Reg 0x8075=0x00) (Reg 0x8076=0xfe) (Reg 0x8077=0x01) 
(Reg 0x8078=0x00) (Reg 0x8079=0x00) (Reg 0x807a=0x00) (Reg 0x807b=0x02) 
(Reg 0x807c=0x03) (Reg 0x807d=0x00) (Reg 0x807e=0x00) (Reg 0x807f=0xe7) 

NVR 2 Registers:

(Reg 0x8080=0x4b) (Reg 0x8081=0x00) (Reg 0x8082=0x46) (Reg 0x8083=0x00) 
(Reg 0x8084=0x00) (Reg 0x8085=0x00) (Reg 0x8086=0xfb) (Reg 0x8087=0x00) 
(Reg 0x8088=0x8a) (Reg 0x8089=0x00) (Reg 0x808a=0x87) (Reg 0x808b=0x5a) 
(Reg 0x808c=0x7a) (Reg 0x808d=0x76) (Reg 0x808e=0x77) (Reg 0x808f=0xe2) 
(Reg 0x8090=0x00) (Reg 0x8091=0x00) (Reg 0x8092=0x00) (Reg 0x8093=0x00) 
(Reg 0x8094=0x00) (Reg 0x8095=0x00) (Reg 0x8096=0x00) (Reg 0x8097=0x00) 
(Reg 0x8098=0x00) (Reg 0x8099=0x00) (Reg 0x809a=0x00) (Reg 0x809b=0x00) 
 (Reg 0x809c=0x00) (Reg 0x809d=0x00) (Reg 0x809e=0x00) (Reg 0x809f=0x00) 
(Reg 0x80a0=0x00) (Reg 0x80a1=0x00) (Reg 0x80a2=0x00) (Reg 0x80a3=0x00) 
(Reg 0x80a4=0x00) (Reg 0x80a5=0x00) (Reg 0x80a6=0x00) (Reg 0x80a7=0x00) 
(Reg 0x80a8=0x13) (Reg 0x80a9=0x88) (Reg 0x80aa=0x11) (Reg 0x80ab=0x94) 
(Reg 0x80ac=0x05) (Reg 0x80ad=0xdc) (Reg 0x80ae=0x03) (Reg 0x80af=0xe8) 
(Reg 0x80b0=0x45) (Reg 0x80b1=0x76) (Reg 0x80b2=0x22) (Reg 0x80b3=0xd0) 
(Reg 0x80b4=0x06) (Reg 0x80b5=0xc9) (Reg 0x80b6=0x03) (Reg 0x80b7=0x66) 
(Reg 0x80b8=0x5a) (Reg 0x80b9=0x00) (Reg 0x80ba=0x55) (Reg 0x80bb=0x00) 
(Reg 0x80bc=0x00) (Reg 0x80bd=0x00) (Reg 0x80be=0xfb) (Reg 0x80bf=0x00) 
(Reg 0x80c0=0x88) (Reg 0x80c1=0x71) (Reg 0x80c2=0x43) (Reg 0x80c3=0xe2) 
 (Reg 0x80c4=0x04) (Reg 0x80c5=0x62) (Reg 0x80c6=0x02) (Reg 0x80c7=0x32) 
(Reg 0x80c8=0x00) (Reg 0x80c9=0x00) (Reg 0x80ca=0x00) (Reg 0x80cb=0x00) 
(Reg 0x80cc=0x00) (Reg 0x80cd=0x00) (Reg 0x80ce=0x00) (Reg 0x80cf=0x00) 
(Reg 0x80d0=0x00) (Reg 0x80d1=0x00) (Reg 0x80d2=0x00) (Reg 0x80d3=0x00) 
(Reg 0x80d4=0x00) (Reg 0x80d5=0x00) (Reg 0x80d6=0x00) (Reg 0x80d7=0x00) 
(Reg 0x80d8=0x00) (Reg 0x80d9=0x00) (Reg 0x80da=0x00) (Reg 0x80db=0x00) 
(Reg 0x80dc=0x00) (Reg 0x80dd=0x00) (Reg 0x80de=0x00) (Reg 0x80df=0x00) 
(Reg 0x80e0=0x00) (Reg 0x80e1=0x00) (Reg 0x80e2=0x00) (Reg 0x80e3=0x00) 
(Reg 0x80e4=0x00) (Reg 0x80e5=0x00) (Reg 0x80e6=0x00) (Reg 0x80e7=0x00) 
(Reg 0x80e8=0x00) (Reg 0x80e9=0x00) (Reg 0x80ea=0x00) (Reg 0x80eb=0x00) 
 (Reg 0x80ec=0x00) (Reg 0x80ed=0x00) (Reg 0x80ee=0x00) (Reg 0x80ef=0x00) 
(Reg 0x80f0=0x00) (Reg 0x80f1=0x00) (Reg 0x80f2=0x00) (Reg 0x80f3=0x00) 
(Reg 0x80f4=0x00) (Reg 0x80f5=0x00) (Reg 0x80f6=0x00) (Reg 0x80f7=0x00) 
(Reg 0x80f8=0x00) (Reg 0x80f9=0x00) (Reg 0x80fa=0x00) (Reg 0x80fb=0x00) 
(Reg 0x80fc=0x00) (Reg 0x80fd=0x00) (Reg 0x80fe=0x00) (Reg 0x80ff=0x93) 

NVR 3 Registers:

(Reg 0x8100=0x00) (Reg 0x8101=0x00) (Reg 0x8102=0x00) (Reg 0x8103=0x00) 
(Reg 0x8104=0x00) (Reg 0x8105=0x00) (Reg 0x8106=0x00) (Reg 0x8107=0x00) 
(Reg 0x8108=0x00) (Reg 0x8109=0x00) (Reg 0x810a=0x00) (Reg 0x810b=0x00) 
(Reg 0x810c=0x00) (Reg 0x810d=0x00) (Reg 0x810e=0x00) (Reg 0x810f=0x00) 
(Reg 0x8110=0x00) (Reg 0x8111=0x00) (Reg 0x8112=0x00) (Reg 0x8113=0x00) 
(Reg 0x8114=0x00) (Reg 0x8115=0x00) (Reg 0x8116=0x00) (Reg 0x8117=0x00) 
(Reg 0x8118=0x00) (Reg 0x8119=0x00) (Reg 0x811a=0x00) (Reg 0x811b=0x00) 
(Reg 0x811c=0x00) (Reg 0x811d=0x00) (Reg 0x811e=0x00) (Reg 0x811f=0x00) 
 (Reg 0x8120=0x00) (Reg 0x8121=0x00) (Reg 0x8122=0x00) (Reg 0x8123=0x00) 
(Reg 0x8124=0x00) (Reg 0x8125=0x00) (Reg 0x8126=0x00) (Reg 0x8127=0x00) 
(Reg 0x8128=0x00) (Reg 0x8129=0x00) (Reg 0x812a=0x00) (Reg 0x812b=0x00) 
(Reg 0x812c=0x00) (Reg 0x812d=0x00) (Reg 0x812e=0x00) (Reg 0x812f=0x00) 
(Reg 0x8130=0x00) (Reg 0x8131=0x00) (Reg 0x8132=0x00) (Reg 0x8133=0x00) 
(Reg 0x8134=0x00) (Reg 0x8135=0x00) (Reg 0x8136=0x00) (Reg 0x8137=0x00) 
(Reg 0x8138=0x00) (Reg 0x8139=0x00) (Reg 0x813a=0x00) (Reg 0x813b=0x00) 
(Reg 0x813c=0x00) (Reg 0x813d=0x00) (Reg 0x813e=0x00) (Reg 0x813f=0x00) 
(Reg 0x8140=0x00) (Reg 0x8141=0x00) (Reg 0x8142=0x00) (Reg 0x8143=0x00) 
(Reg 0x8144=0x00) (Reg 0x8145=0x00) (Reg 0x8146=0x00) (Reg 0x8147=0x00) 
 (Reg 0x8148=0x00) (Reg 0x8149=0x00) (Reg 0x814a=0x00) (Reg 0x814b=0x00) 
(Reg 0x814c=0x00) (Reg 0x814d=0x00) (Reg 0x814e=0x00) (Reg 0x814f=0x00) 
(Reg 0x8150=0x00) (Reg 0x8151=0x00) (Reg 0x8152=0x00) (Reg 0x8153=0x00) 
(Reg 0x8154=0x00) (Reg 0x8155=0x00) (Reg 0x8156=0x00) (Reg 0x8157=0x00) 
(Reg 0x8158=0x00) (Reg 0x8159=0x00) (Reg 0x815a=0x00) (Reg 0x815b=0x00) 
(Reg 0x815c=0x00) (Reg 0x815d=0x00) (Reg 0x815e=0x00) (Reg 0x815f=0x00) 
(Reg 0x8160=0x00) (Reg 0x8161=0x00) (Reg 0x8162=0x00) (Reg 0x8163=0x00) 
(Reg 0x8164=0x00) (Reg 0x8165=0x00) (Reg 0x8166=0x00) (Reg 0x8167=0x00) 
(Reg 0x8168=0x00) (Reg 0x8169=0x00) (Reg 0x816a=0x00) (Reg 0x816b=0x00) 
(Reg 0x816c=0x00) (Reg 0x816d=0x00) (Reg 0x816e=0x00) (Reg 0x816f=0x00) 
 (Reg 0x8170=0x00) (Reg 0x8171=0x00) (Reg 0x8172=0x00) (Reg 0x8173=0x00) 
(Reg 0x8174=0x00) (Reg 0x8175=0x00) (Reg 0x8176=0x00) (Reg 0x8177=0x00) 
(Reg 0x8178=0x00) (Reg 0x8179=0x00) (Reg 0x817a=0x00) (Reg 0x817b=0x00) 
(Reg 0x817c=0x00) (Reg 0x817d=0x00) (Reg 0x817e=0x00) (Reg 0x817f=0x00) 

NVR 4 Registers:

(Reg 0x8180=0x00) 

VR 1 Registers:

(Reg 0xa000=0x0000) (Reg 0xa001=0x1234) (Reg 0xa002=0x0000) (Reg 0xa003=0x0000) 
(Reg 0xa004=0x0000) (Reg 0xa005=0x0000) (Reg 0xa006=0x0000) (Reg 0xa007=0x0000) 
(Reg 0xa008=0x0000) (Reg 0xa009=0x0000) (Reg 0xa00a=0x0000) (Reg 0xa00b=0x0000) 
(Reg 0xa00c=0x0000) (Reg 0xa00d=0x0000) (Reg 0xa00e=0x0000) (Reg 0xa00f=0x0000) 
(Reg 0xa010=0x0000) (Reg 0xa011=0x0200) (Reg 0xa012=0x0200) (Reg 0xa013=0x0000) 
(Reg 0xa014=0x0000) (Reg 0xa015=0x0000) (Reg 0xa016=0x0020) (Reg 0xa017=0x0000) 
(Reg 0xa018=0xb100) (Reg 0xa019=0x03ff) (Reg 0xa01a=0x03ff) (Reg 0xa01b=0x0000) 
(Reg 0xa01c=0x8000) (Reg 0xa01d=0x0002) (Reg 0xa01e=0x0000) (Reg 0xa01f=0x0000) 
(Reg 0xa020=0x0000) (Reg 0xa021=0x0000) (Reg 0xa022=0x0000) (Reg 0xa023=0x0020) 
(Reg 0xa024=0x0000) (Reg 0xa025=0x0000) (Reg 0xa026=0x0000) (Reg 0xa027=0x0000) 
(Reg 0xa028=0x006a) (Reg 0xa029=0xa7f8) (Reg 0xa02a=0x0062) (Reg 0xa02b=0x0ff0) 
(Reg 0xa02c=0x00f0) (Reg 0xa02d=0x0000) (Reg 0xa02e=0x0000) (Reg 0xa02f=0x196c) 
(Reg 0xa030=0x8128) (Reg 0xa031=0x0000) (Reg 0xa032=0x65f9) (Reg 0xa033=0x309a) 
(Reg 0xa034=0x0000) (Reg 0xa035=0x0000) (Reg 0xa036=0x0000) (Reg 0xa037=0x0000) 
(Reg 0xa038=0x0000) (Reg 0xa039=0x0000) (Reg 0xa03a=0x0000) 

NETWORK LANE VR 1 Registers:

(Reg 0xa200=0x0000) (Reg 0xa201=0x0000) (Reg 0xa202=0x0000) (Reg 0xa203=0x0000) 
(Reg 0xa204=0x0000) (Reg 0xa205=0x0000) (Reg 0xa206=0x0000) (Reg 0xa207=0x0000) 
(Reg 0xa208=0x0000) (Reg 0xa209=0x0000) (Reg 0xa20a=0x0000) (Reg 0xa20b=0x0000) 
(Reg 0xa20c=0x0000) (Reg 0xa20d=0x0000) (Reg 0xa20e=0x0000) (Reg 0xa20f=0x0000) 
(Reg 0xa210=0x0000) (Reg 0xa211=0x0000) (Reg 0xa212=0x0000) (Reg 0xa213=0x0000) 
(Reg 0xa214=0x0000) (Reg 0xa215=0x0000) (Reg 0xa216=0x0000) (Reg 0xa217=0x0000) 
(Reg 0xa218=0x0000) (Reg 0xa219=0x0000) (Reg 0xa21a=0x0000) (Reg 0xa21b=0x0000) 
(Reg 0xa21c=0x0000) (Reg 0xa21d=0x0000) (Reg 0xa21e=0x0000) (Reg 0xa21f=0x0000) 
(Reg 0xa220=0x0003) (Reg 0xa221=0x0003) (Reg 0xa222=0x0003) (Reg 0xa223=0x0003) 
(Reg 0xa224=0x0003) (Reg 0xa225=0x0003) (Reg 0xa226=0x0003) (Reg 0xa227=0x0003) 
(Reg 0xa228=0x0003) (Reg 0xa229=0x0003) (Reg 0xa22a=0x0000) (Reg 0xa22b=0x0000) 
(Reg 0xa22c=0x0000) (Reg 0xa22d=0x0000) (Reg 0xa22e=0x0000) (Reg 0xa22f=0x0000) 
(Reg 0xa230=0x0010) (Reg 0xa231=0x0010) (Reg 0xa232=0x0010) (Reg 0xa233=0x0010) 
(Reg 0xa234=0x0010) (Reg 0xa235=0x0010) (Reg 0xa236=0x0010) (Reg 0xa237=0x0010) 
(Reg 0xa238=0x0010) (Reg 0xa239=0x0010) (Reg 0xa23a=0x0000) (Reg 0xa23b=0x0000) 
(Reg 0xa23c=0x0000) (Reg 0xa23d=0x0000) (Reg 0xa23e=0x0000) (Reg 0xa23f=0x0000) 
(Reg 0xa240=0xffff) (Reg 0xa241=0xffff) (Reg 0xa242=0xffff) (Reg 0xa243=0xffff) 
(Reg 0xa244=0xffff) (Reg 0xa245=0xffff) (Reg 0xa246=0xffff) (Reg 0xa247=0xffff) 
(Reg 0xa248=0xffff) (Reg 0xa249=0xffff) (Reg 0xa24a=0x0000) (Reg 0xa24b=0x0000) 
(Reg 0xa24c=0x0000) (Reg 0xa24d=0x0000) (Reg 0xa24e=0x0000) (Reg 0xa24f=0x0000) 
(Reg 0xa250=0xe0dc) (Reg 0xa251=0xe0dc) (Reg 0xa252=0xe0dc) (Reg 0xa253=0xe0dc) 
(Reg 0xa254=0xe0dc) (Reg 0xa255=0xe0dc) (Reg 0xa256=0xe0dc) (Reg 0xa257=0xe0dc) 
(Reg 0xa258=0xe0dc) (Reg 0xa259=0xe0dc) (Reg 0xa25a=0x0000) (Reg 0xa25b=0x0000) 
(Reg 0xa25c=0x0000) (Reg 0xa25d=0x0000) (Reg 0xa25e=0x0000) (Reg 0xa25f=0x0000) 
(Reg 0xa260=0x0000) 

NETWORK LANE VR 2 Registers:

(Reg 0xa280=0x0000) (Reg 0xa281=0x0000) (Reg 0xa282=0x0000) (Reg 0xa283=0x0000) 
(Reg 0xa284=0x0000) (Reg 0xa285=0x0000) (Reg 0xa286=0x0000) (Reg 0xa287=0x0000) 
(Reg 0xa288=0x0000) (Reg 0xa289=0x0000) (Reg 0xa28a=0x0000) (Reg 0xa28b=0x0000) 
(Reg 0xa28c=0x0000) (Reg 0xa28d=0x0000) (Reg 0xa28e=0x0000) (Reg 0xa28f=0x0000) 
(Reg 0xa290=0x0000) (Reg 0xa291=0x0000) (Reg 0xa292=0x0000) (Reg 0xa293=0x0000) 
(Reg 0xa294=0x0000) (Reg 0xa295=0x0000) (Reg 0xa296=0x0000) (Reg 0xa297=0x0000) 
(Reg 0xa298=0x0000) (Reg 0xa299=0x0000) (Reg 0xa29a=0x0000) (Reg 0xa29b=0x0000) 
(Reg 0xa29c=0x0000) (Reg 0xa29d=0x0000) (Reg 0xa29e=0x0000) (Reg 0xa29f=0x0000) 
(Reg 0xa2a0=0x0af4) (Reg 0xa2a1=0x0b0f) (Reg 0xa2a2=0x0b39) (Reg 0xa2a3=0x0ae1) 
(Reg 0xa2a4=0x0b6d) (Reg 0xa2a5=0x0acd) (Reg 0xa2a6=0x0b71) (Reg 0xa2a7=0x0ae2) 
(Reg 0xa2a8=0x0b26) (Reg 0xa2a9=0x0abf) (Reg 0xa2aa=0x0000) (Reg 0xa2ab=0x0000) 
(Reg 0xa2ac=0x0000) (Reg 0xa2ad=0x0000) (Reg 0xa2ae=0x0000) (Reg 0xa2af=0x0000) 
(Reg 0xa2b0=0x16c4) (Reg 0xa2b1=0x16f6) (Reg 0xa2b2=0x167f) (Reg 0xa2b3=0x176c) 
(Reg 0xa2b4=0x154e) (Reg 0xa2b5=0x15e4) (Reg 0xa2b6=0x14ad) (Reg 0xa2b7=0x1592) 
(Reg 0xa2b8=0x159d) (Reg 0xa2b9=0x14e8) (Reg 0xa2ba=0x0000) (Reg 0xa2bb=0x0000) 
(Reg 0xa2bc=0x0000) (Reg 0xa2bd=0x0000) (Reg 0xa2be=0x0000) (Reg 0xa2bf=0x0000) 
(Reg 0xa2c0=0x206c) (Reg 0xa2c1=0x206c) (Reg 0xa2c2=0x206c) (Reg 0xa2c3=0x206c) 
(Reg 0xa2c4=0x206c) (Reg 0xa2c5=0x206c) (Reg 0xa2c6=0x206c) (Reg 0xa2c7=0x206c) 
(Reg 0xa2c8=0x206c) (Reg 0xa2c9=0x206c) (Reg 0xa2ca=0x0000) (Reg 0xa2cb=0x0000) 
(Reg 0xa2cc=0x0000) (Reg 0xa2cd=0x0000) (Reg 0xa2ce=0x0000) (Reg 0xa2cf=0x0000) 
(Reg 0xa2d0=0x1150) (Reg 0xa2d1=0x1851) (Reg 0xa2d2=0x191f) (Reg 0xa2d3=0x181c) 
(Reg 0xa2d4=0x10db) (Reg 0xa2d5=0x15bb) (Reg 0xa2d6=0x1391) (Reg 0xa2d7=0x130e) 
(Reg 0xa2d8=0x1665) (Reg 0xa2d9=0x152d) (Reg 0xa2da=0x0000) (Reg 0xa2db=0x0000) 
(Reg 0xa2dc=0x0000) (Reg 0xa2dd=0x0000) (Reg 0xa2de=0x0000) (Reg 0xa2df=0x0000) 
(Reg 0xa2e0=0x0000) 

HOST LANE VR 1 Registers:

(Reg 0xa400=0x0000) (Reg 0xa401=0x0000) (Reg 0xa402=0x0000) (Reg 0xa403=0x0000) 
(Reg 0xa404=0x0000) (Reg 0xa405=0x0000) (Reg 0xa406=0x0000) (Reg 0xa407=0x0000) 
(Reg 0xa408=0x0000) (Reg 0xa409=0x0000) (Reg 0xa40a=0x0000) (Reg 0xa40b=0x0000) 
(Reg 0xa40c=0x0000) (Reg 0xa40d=0x0000) (Reg 0xa40e=0x0000) (Reg 0xa40f=0x0000) 
(Reg 0xa410=0x0000) (Reg 0xa411=0x0000) (Reg 0xa412=0x0000) (Reg 0xa413=0x0000) 
(Reg 0xa414=0x0000) (Reg 0xa415=0x0000) (Reg 0xa416=0x0000) (Reg 0xa417=0x0000) 
(Reg 0xa418=0x0000) (Reg 0xa419=0x0000) (Reg 0xa41a=0x0000) (Reg 0xa41b=0x0000) 
(Reg 0xa41c=0x0000) (Reg 0xa41d=0x0000) (Reg 0xa41e=0x0000) (Reg 0xa41f=0x0000) 
(Reg 0xa420=0x0001) (Reg 0xa421=0x0001) (Reg 0xa422=0x0001) (Reg 0xa423=0x0001) 
(Reg 0xa424=0x0001) (Reg 0xa425=0x0001) (Reg 0xa426=0x0001) (Reg 0xa427=0x0001) 
(Reg 0xa428=0x0001) (Reg 0xa429=0x0001) (Reg 0xa42a=0x0000) (Reg 0xa42b=0x0000) 
(Reg 0xa42c=0x0000) (Reg 0xa42d=0x0000) (Reg 0xa42e=0x0000) (Reg 0xa42f=0x0000) 
(Reg 0xa430=0x0000) (Reg 0xa431=0x0000) (Reg 0xa432=0x0000) (Reg 0xa433=0x0000) 
(Reg 0xa434=0x0000) (Reg 0xa435=0x0000) (Reg 0xa436=0x0000) (Reg 0xa437=0x0000) 
(Reg 0xa438=0x0000) (Reg 0xa439=0x0000) (Reg 0xa43a=0x0000) (Reg 0xa43b=0x0000) 
(Reg 0xa43c=0x0000) (Reg 0xa43d=0x0000) (Reg 0xa43e=0x0000) (Reg 0xa43f=0x0000) 
(Reg 0xa440=0x0007) (Reg 0xa441=0x0007) (Reg 0xa442=0x0007) (Reg 0xa443=0x0007) 
(Reg 0xa444=0x0007) (Reg 0xa445=0x0007) (Reg 0xa446=0x0007) (Reg 0xa447=0x0007) 
(Reg 0xa448=0x0007) (Reg 0xa449=0x0007) (Reg 0xa44a=0x0000) (Reg 0xa44b=0x0000) 
(Reg 0xa44c=0x0000) (Reg 0xa44d=0x0000) (Reg 0xa44e=0x0000) (Reg 0xa44f=0x0000) 
(Reg 0xa450=0x0000) 

Regs Info
OTN Controller 3 common register:

TOP_MPIF Block : 
---------------------------
Addr     Name                            Value
0x00002  GLOBAL_CFG                      0x0051
0x00004  SCRATCH_PAD1                    0x000a
0x00005  SCRATCH_PAD2                    0xcc00
0x00009  GPIO_CONTROL                    0x0000
 
SDS_COMMON Block : BANK B
---------------------------
Addr     Name                            Value
0x0241f  RXLOCKD0_INTSTATUS 3            0x0028
0x02445  RXLOCKD1_INTSTATUS 3            0x0008
0x0246b  RXLOCKD2_INTSTATUS 3            0x0020
0x02491  RXLOCKD3_INTSTATUS 3            0x0000
0x024b9  TXLOCKD0_INTSTATUS 3            0x000d
0x0281f  RXLOCKD0_INTSTATUS 4            0x0009
0x02845  RXLOCKD1_INTSTATUS 4            0x0018
0x0286b  RXLOCKD2_INTSTATUS 4            0x0008
0x02891  RXLOCKD3_INTSTATUS 4            0x001c
0x028b9  TXLOCKD0_INTSTATUS 4            0x0008

SDS_COMMON Block : BANK C
---------------------------
Addr     Name                            Value
0x0301f  RXLOCKD0_INTSTATUS 6            0x0049
0x03045  RXLOCKD1_INTSTATUS 6            0x0049
0x0306b  RXLOCKD2_INTSTATUS 6            0x0049
0x03091  RXLOCKD3_INTSTATUS 6            0x0049
0x030b9  TXLOCKD0_INTSTATUS 6            0x0049
0x0341f  RXLOCKD0_INTSTATUS 7            0x0049
0x03445  RXLOCKD1_INTSTATUS 7            0x0049
0x0346b  RXLOCKD2_INTSTATUS 7            0x0049
0x03491  RXLOCKD3_INTSTATUS 7            0x0049
0x034b9  TXLOCKD0_INTSTATUS 7            0x0049

ILKN_CORE Block : 
---------------------------
Addr     Name                            Value
0x19d6b  RX_INTERLAKEN_STATUS0           0x0049
0x19d6c  RX_INTERLAKEN_SYNCED1           0x0049
0x19d6d  RX_INTERLAKEN_SYNCED0           0x0049
0x19d66  RX_OOBFC_RX_LANE_STATUS1        0x0049
0x19d67  RX_OOBFC_RX_LANE_STATUS0        0x0049
0x19d62  TX_INTERLAKEN_STATUS1           0x0049
0x19d63  TX_INTERLAKEN_STATUS0           0x0049

Port/3 register:

SDS_COMMON Block : line
---------------------------
Addr     Name                            Value
0x0181f  RXLOCKD0_INTSTATUS 0            0x0001
0x01845  RXLOCKD1_INTSTATUS 0            0x0001
0x0186b  RXLOCKD2_INTSTATUS 0            0x0001
0x01891  RXLOCKD3_INTSTATUS 0            0x0009
0x018b9  TXLOCKD0_INTSTATUS 0            0x0049

CPAK Registers:
================
 
NVR 1 Registers:

(Reg 0x8000=0x01) (Reg 0x8001=0x21) (Reg 0x8002=0x09) (Reg 0x8003=0x03) 
(Reg 0x8004=0x00) (Reg 0x8005=0x00) (Reg 0x8006=0x00) (Reg 0x8007=0x00) 
(Reg 0x8008=0x1e) (Reg 0x8009=0xaa) (Reg 0x800a=0x4a) (Reg 0x800b=0x38) 
(Reg 0x800c=0x38) (Reg 0x800d=0x00) (Reg 0x800e=0x0a) (Reg 0x800f=0x00) 
 (Reg 0x8010=0x0a) (Reg 0x8011=0x01) (Reg 0x8012=0x83) (Reg 0x8013=0x40) 
(Reg 0x8014=0x86) (Reg 0x8015=0x60) (Reg 0x8016=0x00) (Reg 0x8017=0x00) 
(Reg 0x8018=0x00) (Reg 0x8019=0x04) (Reg 0x801a=0x40) (Reg 0x801b=0x50) 
(Reg 0x801c=0x26) (Reg 0x801d=0x17) (Reg 0x801e=0x14) (Reg 0x801f=0x46) 
(Reg 0x8020=0x00) (Reg 0x8021=0x43) (Reg 0x8022=0x49) (Reg 0x8023=0x53) 
(Reg 0x8024=0x43) (Reg 0x8025=0x4f) (Reg 0x8026=0x20) (Reg 0x8027=0x20) 
(Reg 0x8028=0x20) (Reg 0x8029=0x20) (Reg 0x802a=0x20) (Reg 0x802b=0x20) 
(Reg 0x802c=0x20) (Reg 0x802d=0x20) (Reg 0x802e=0x20) (Reg 0x802f=0x20) 
(Reg 0x8030=0x20) (Reg 0x8031=0x00) (Reg 0x8032=0x00) (Reg 0x8033=0x0c) 
(Reg 0x8034=0x38) (Reg 0x8035=0x30) (Reg 0x8036=0x30) (Reg 0x8037=0x2d) 
 (Reg 0x8038=0x34) (Reg 0x8039=0x31) (Reg 0x803a=0x34) (Reg 0x803b=0x39) 
(Reg 0x803c=0x35) (Reg 0x803d=0x2d) (Reg 0x803e=0x30) (Reg 0x803f=0x31) 
(Reg 0x8040=0x20) (Reg 0x8041=0x20) (Reg 0x8042=0x20) (Reg 0x8043=0x20) 
(Reg 0x8044=0x46) (Reg 0x8045=0x42) (Reg 0x8046=0x4e) (Reg 0x8047=0x31) 
(Reg 0x8048=0x39) (Reg 0x8049=0x31) (Reg 0x804a=0x32) (Reg 0x804b=0x32) 
(Reg 0x804c=0x30) (Reg 0x804d=0x32) (Reg 0x804e=0x32) (Reg 0x804f=0x20) 
(Reg 0x8050=0x20) (Reg 0x8051=0x20) (Reg 0x8052=0x20) (Reg 0x8053=0x20) 
(Reg 0x8054=0x32) (Reg 0x8055=0x30) (Reg 0x8056=0x31) (Reg 0x8057=0x35) 
(Reg 0x8058=0x30) (Reg 0x8059=0x33) (Reg 0x805a=0x31) (Reg 0x805b=0x39) 
(Reg 0x805c=0x00) (Reg 0x805d=0x00) (Reg 0x805e=0x57) (Reg 0x805f=0x4f) 
 (Reg 0x8060=0x54) (Reg 0x8061=0x52) (Reg 0x8062=0x43) (Reg 0x8063=0x35) 
(Reg 0x8064=0x50) (Reg 0x8065=0x42) (Reg 0x8066=0x41) (Reg 0x8067=0x41) 
(Reg 0x8068=0x6e) (Reg 0x8069=0x5a) (Reg 0x806a=0x00) (Reg 0x806b=0x05) 
(Reg 0x806c=0x02) (Reg 0x806d=0x03) (Reg 0x806e=0x0c) (Reg 0x806f=0x03) 
(Reg 0x8070=0x0f) (Reg 0x8071=0x20) (Reg 0x8072=0x01) (Reg 0x8073=0x01) 
(Reg 0x8074=0x08) (Reg 0x8075=0x00) (Reg 0x8076=0xfe) (Reg 0x8077=0x01) 
(Reg 0x8078=0x00) (Reg 0x8079=0x00) (Reg 0x807a=0x00) (Reg 0x807b=0x02) 
(Reg 0x807c=0x03) (Reg 0x807d=0x00) (Reg 0x807e=0x00) (Reg 0x807f=0xe4) 

NVR 2 Registers:

(Reg 0x8080=0x4b) (Reg 0x8081=0x00) (Reg 0x8082=0x46) (Reg 0x8083=0x00) 
(Reg 0x8084=0x00) (Reg 0x8085=0x00) (Reg 0x8086=0xfb) (Reg 0x8087=0x00) 
(Reg 0x8088=0x8a) (Reg 0x8089=0x00) (Reg 0x808a=0x87) (Reg 0x808b=0x5a) 
(Reg 0x808c=0x7a) (Reg 0x808d=0x76) (Reg 0x808e=0x77) (Reg 0x808f=0xe2) 
(Reg 0x8090=0x00) (Reg 0x8091=0x00) (Reg 0x8092=0x00) (Reg 0x8093=0x00) 
 (Reg 0x8094=0x00) (Reg 0x8095=0x00) (Reg 0x8096=0x00) (Reg 0x8097=0x00) 
(Reg 0x8098=0x00) (Reg 0x8099=0x00) (Reg 0x809a=0x00) (Reg 0x809b=0x00) 
(Reg 0x809c=0x00) (Reg 0x809d=0x00) (Reg 0x809e=0x00) (Reg 0x809f=0x00) 
(Reg 0x80a0=0x00) (Reg 0x80a1=0x00) (Reg 0x80a2=0x00) (Reg 0x80a3=0x00) 
(Reg 0x80a4=0x00) (Reg 0x80a5=0x00) (Reg 0x80a6=0x00) (Reg 0x80a7=0x00) 
(Reg 0x80a8=0x13) (Reg 0x80a9=0x88) (Reg 0x80aa=0x11) (Reg 0x80ab=0x94) 
(Reg 0x80ac=0x05) (Reg 0x80ad=0xdc) (Reg 0x80ae=0x03) (Reg 0x80af=0xe8) 
(Reg 0x80b0=0x45) (Reg 0x80b1=0x76) (Reg 0x80b2=0x22) (Reg 0x80b3=0xd0) 
(Reg 0x80b4=0x06) (Reg 0x80b5=0xc9) (Reg 0x80b6=0x03) (Reg 0x80b7=0x66) 
(Reg 0x80b8=0x5a) (Reg 0x80b9=0x00) (Reg 0x80ba=0x55) (Reg 0x80bb=0x00) 
 (Reg 0x80bc=0x00) (Reg 0x80bd=0x00) (Reg 0x80be=0xfb) (Reg 0x80bf=0x00) 
(Reg 0x80c0=0x88) (Reg 0x80c1=0x71) (Reg 0x80c2=0x43) (Reg 0x80c3=0xe2) 
(Reg 0x80c4=0x04) (Reg 0x80c5=0x62) (Reg 0x80c6=0x02) (Reg 0x80c7=0x32) 
(Reg 0x80c8=0x00) (Reg 0x80c9=0x00) (Reg 0x80ca=0x00) (Reg 0x80cb=0x00) 
(Reg 0x80cc=0x00) (Reg 0x80cd=0x00) (Reg 0x80ce=0x00) (Reg 0x80cf=0x00) 
(Reg 0x80d0=0x00) (Reg 0x80d1=0x00) (Reg 0x80d2=0x00) (Reg 0x80d3=0x00) 
(Reg 0x80d4=0x00) (Reg 0x80d5=0x00) (Reg 0x80d6=0x00) (Reg 0x80d7=0x00) 
(Reg 0x80d8=0x00) (Reg 0x80d9=0x00) (Reg 0x80da=0x00) (Reg 0x80db=0x00) 
(Reg 0x80dc=0x00) (Reg 0x80dd=0x00) (Reg 0x80de=0x00) (Reg 0x80df=0x00) 
(Reg 0x80e0=0x00) (Reg 0x80e1=0x00) (Reg 0x80e2=0x00) (Reg 0x80e3=0x00) 
 (Reg 0x80e4=0x00) (Reg 0x80e5=0x00) (Reg 0x80e6=0x00) (Reg 0x80e7=0x00) 
(Reg 0x80e8=0x00) (Reg 0x80e9=0x00) (Reg 0x80ea=0x00) (Reg 0x80eb=0x00) 
(Reg 0x80ec=0x00) (Reg 0x80ed=0x00) (Reg 0x80ee=0x00) (Reg 0x80ef=0x00) 
(Reg 0x80f0=0x00) (Reg 0x80f1=0x00) (Reg 0x80f2=0x00) (Reg 0x80f3=0x00) 
(Reg 0x80f4=0x00) (Reg 0x80f5=0x00) (Reg 0x80f6=0x00) (Reg 0x80f7=0x00) 
(Reg 0x80f8=0x00) (Reg 0x80f9=0x00) (Reg 0x80fa=0x00) (Reg 0x80fb=0x00) 
(Reg 0x80fc=0x00) (Reg 0x80fd=0x00) (Reg 0x80fe=0x00) (Reg 0x80ff=0x93) 

NVR 3 Registers:

(Reg 0x8100=0x00) (Reg 0x8101=0x00) (Reg 0x8102=0x00) (Reg 0x8103=0x00) 
(Reg 0x8104=0x00) (Reg 0x8105=0x00) (Reg 0x8106=0x00) (Reg 0x8107=0x00) 
(Reg 0x8108=0x00) (Reg 0x8109=0x00) (Reg 0x810a=0x00) (Reg 0x810b=0x00) 
(Reg 0x810c=0x00) (Reg 0x810d=0x00) (Reg 0x810e=0x00) (Reg 0x810f=0x00) 
(Reg 0x8110=0x00) (Reg 0x8111=0x00) (Reg 0x8112=0x00) (Reg 0x8113=0x00) 
(Reg 0x8114=0x00) (Reg 0x8115=0x00) (Reg 0x8116=0x00) (Reg 0x8117=0x00) 
 (Reg 0x8118=0x00) (Reg 0x8119=0x00) (Reg 0x811a=0x00) (Reg 0x811b=0x00) 
(Reg 0x811c=0x00) (Reg 0x811d=0x00) (Reg 0x811e=0x00) (Reg 0x811f=0x00) 
(Reg 0x8120=0x00) (Reg 0x8121=0x00) (Reg 0x8122=0x00) (Reg 0x8123=0x00) 
(Reg 0x8124=0x00) (Reg 0x8125=0x00) (Reg 0x8126=0x00) (Reg 0x8127=0x00) 
(Reg 0x8128=0x00) (Reg 0x8129=0x00) (Reg 0x812a=0x00) (Reg 0x812b=0x00) 
(Reg 0x812c=0x00) (Reg 0x812d=0x00) (Reg 0x812e=0x00) (Reg 0x812f=0x00) 
(Reg 0x8130=0x00) (Reg 0x8131=0x00) (Reg 0x8132=0x00) (Reg 0x8133=0x00) 
(Reg 0x8134=0x00) (Reg 0x8135=0x00) (Reg 0x8136=0x00) (Reg 0x8137=0x00) 
(Reg 0x8138=0x00) (Reg 0x8139=0x00) (Reg 0x813a=0x00) (Reg 0x813b=0x00) 
(Reg 0x813c=0x00) (Reg 0x813d=0x00) (Reg 0x813e=0x00) (Reg 0x813f=0x00) 
 (Reg 0x8140=0x00) (Reg 0x8141=0x00) (Reg 0x8142=0x00) (Reg 0x8143=0x00) 
(Reg 0x8144=0x00) (Reg 0x8145=0x00) (Reg 0x8146=0x00) (Reg 0x8147=0x00) 
(Reg 0x8148=0x00) (Reg 0x8149=0x00) (Reg 0x814a=0x00) (Reg 0x814b=0x00) 
(Reg 0x814c=0x00) (Reg 0x814d=0x00) (Reg 0x814e=0x00) (Reg 0x814f=0x00) 
(Reg 0x8150=0x00) (Reg 0x8151=0x00) (Reg 0x8152=0x00) (Reg 0x8153=0x00) 
(Reg 0x8154=0x00) (Reg 0x8155=0x00) (Reg 0x8156=0x00) (Reg 0x8157=0x00) 
(Reg 0x8158=0x00) (Reg 0x8159=0x00) (Reg 0x815a=0x00) (Reg 0x815b=0x00) 
(Reg 0x815c=0x00) (Reg 0x815d=0x00) (Reg 0x815e=0x00) (Reg 0x815f=0x00) 
(Reg 0x8160=0x00) (Reg 0x8161=0x00) (Reg 0x8162=0x00) (Reg 0x8163=0x00) 
(Reg 0x8164=0x00) (Reg 0x8165=0x00) (Reg 0x8166=0x00) (Reg 0x8167=0x00) 
 (Reg 0x8168=0x00) (Reg 0x8169=0x00) (Reg 0x816a=0x00) (Reg 0x816b=0x00) 
(Reg 0x816c=0x00) (Reg 0x816d=0x00) (Reg 0x816e=0x00) (Reg 0x816f=0x00) 
(Reg 0x8170=0x00) (Reg 0x8171=0x00) (Reg 0x8172=0x00) (Reg 0x8173=0x00) 
(Reg 0x8174=0x00) (Reg 0x8175=0x00) (Reg 0x8176=0x00) (Reg 0x8177=0x00) 
(Reg 0x8178=0x00) (Reg 0x8179=0x00) (Reg 0x817a=0x00) (Reg 0x817b=0x00) 
(Reg 0x817c=0x00) (Reg 0x817d=0x00) (Reg 0x817e=0x00) (Reg 0x817f=0x00) 

NVR 4 Registers:

(Reg 0x8180=0x00) 

 VR 1 Registers:

(Reg 0xa000=0x0000) (Reg 0xa001=0x1234) (Reg 0xa002=0x0000) (Reg 0xa003=0x0000) 
(Reg 0xa004=0x0000) (Reg 0xa005=0x0000) (Reg 0xa006=0x0000) (Reg 0xa007=0x0000) 
(Reg 0xa008=0x0000) (Reg 0xa009=0x0000) (Reg 0xa00a=0x0000) (Reg 0xa00b=0x0000) 
(Reg 0xa00c=0x0000) (Reg 0xa00d=0x0000) (Reg 0xa00e=0x0000) (Reg 0xa00f=0x0000) 
(Reg 0xa010=0x2000) (Reg 0xa011=0x0200) (Reg 0xa012=0x0200) (Reg 0xa013=0x0000) 
(Reg 0xa014=0x0000) (Reg 0xa015=0x0000) (Reg 0xa016=0x0008) (Reg 0xa017=0x0000) 
(Reg 0xa018=0xb180) (Reg 0xa019=0x03ff) (Reg 0xa01a=0x03ff) (Reg 0xa01b=0x0000) 
(Reg 0xa01c=0x8000) (Reg 0xa01d=0x0022) (Reg 0xa01e=0x0000) (Reg 0xa01f=0x0000) 
(Reg 0xa020=0x0000) (Reg 0xa021=0x8000) (Reg 0xa022=0x000f) (Reg 0xa023=0x0020) 
(Reg 0xa024=0x0000) (Reg 0xa025=0x0000) (Reg 0xa026=0x0000) (Reg 0xa027=0x0000) 
(Reg 0xa028=0x006a) (Reg 0xa029=0xa7f8) (Reg 0xa02a=0x0062) (Reg 0xa02b=0x0ff0) 
(Reg 0xa02c=0x00f0) (Reg 0xa02d=0x0000) (Reg 0xa02e=0x0000) (Reg 0xa02f=0x1539) 
(Reg 0xa030=0x8040) (Reg 0xa031=0x0000) (Reg 0xa032=0x657e) (Reg 0xa033=0x3069) 
(Reg 0xa034=0x0000) (Reg 0xa035=0x0000) (Reg 0xa036=0x0000) (Reg 0xa037=0x0000) 
(Reg 0xa038=0x0000) (Reg 0xa039=0x0000) (Reg 0xa03a=0x0000) 

NETWORK LANE VR 1 Registers:

(Reg 0xa200=0x0003) (Reg 0xa201=0x0003) (Reg 0xa202=0x0003) (Reg 0xa203=0x0003) 
(Reg 0xa204=0x0003) (Reg 0xa205=0x0003) (Reg 0xa206=0x0003) (Reg 0xa207=0x0003) 
(Reg 0xa208=0x0003) (Reg 0xa209=0x0003) (Reg 0xa20a=0x0000) (Reg 0xa20b=0x0000) 
(Reg 0xa20c=0x0000) (Reg 0xa20d=0x0000) (Reg 0xa20e=0x0000) (Reg 0xa20f=0x0000) 
(Reg 0xa210=0x0010) (Reg 0xa211=0x0010) (Reg 0xa212=0x0010) (Reg 0xa213=0x0010) 
(Reg 0xa214=0x0010) (Reg 0xa215=0x0010) (Reg 0xa216=0x0010) (Reg 0xa217=0x0010) 
(Reg 0xa218=0x0010) (Reg 0xa219=0x0010) (Reg 0xa21a=0x0000) (Reg 0xa21b=0x0000) 
(Reg 0xa21c=0x0000) (Reg 0xa21d=0x0000) (Reg 0xa21e=0x0000) (Reg 0xa21f=0x0000) 
(Reg 0xa220=0x0003) (Reg 0xa221=0x0003) (Reg 0xa222=0x0003) (Reg 0xa223=0x0003) 
(Reg 0xa224=0x0003) (Reg 0xa225=0x0003) (Reg 0xa226=0x0003) (Reg 0xa227=0x0003) 
(Reg 0xa228=0x0003) (Reg 0xa229=0x0003) (Reg 0xa22a=0x0000) (Reg 0xa22b=0x0000) 
(Reg 0xa22c=0x0000) (Reg 0xa22d=0x0000) (Reg 0xa22e=0x0000) (Reg 0xa22f=0x0000) 
(Reg 0xa230=0x0010) (Reg 0xa231=0x0010) (Reg 0xa232=0x0010) (Reg 0xa233=0x0010) 
(Reg 0xa234=0x0010) (Reg 0xa235=0x0010) (Reg 0xa236=0x0010) (Reg 0xa237=0x0010) 
(Reg 0xa238=0x0010) (Reg 0xa239=0x0010) (Reg 0xa23a=0x0000) (Reg 0xa23b=0x0000) 
(Reg 0xa23c=0x0000) (Reg 0xa23d=0x0000) (Reg 0xa23e=0x0000) (Reg 0xa23f=0x0000) 
(Reg 0xa240=0xffff) (Reg 0xa241=0xffff) (Reg 0xa242=0xffff) (Reg 0xa243=0xffff) 
(Reg 0xa244=0xffff) (Reg 0xa245=0xffff) (Reg 0xa246=0xffff) (Reg 0xa247=0xffff) 
(Reg 0xa248=0xffff) (Reg 0xa249=0xffff) (Reg 0xa24a=0x0000) (Reg 0xa24b=0x0000) 
(Reg 0xa24c=0x0000) (Reg 0xa24d=0x0000) (Reg 0xa24e=0x0000) (Reg 0xa24f=0x0000) 
(Reg 0xa250=0xe0dc) (Reg 0xa251=0xe0dc) (Reg 0xa252=0xe0dc) (Reg 0xa253=0xe0dc) 
(Reg 0xa254=0xe0dc) (Reg 0xa255=0xe0dc) (Reg 0xa256=0xe0dc) (Reg 0xa257=0xe0dc) 
(Reg 0xa258=0xe0dc) (Reg 0xa259=0xe0dc) (Reg 0xa25a=0x0000) (Reg 0xa25b=0x0000) 
(Reg 0xa25c=0x0000) (Reg 0xa25d=0x0000) (Reg 0xa25e=0x0000) (Reg 0xa25f=0x0000) 
(Reg 0xa260=0x0000) 

NETWORK LANE VR 2 Registers:

(Reg 0xa280=0x0000) (Reg 0xa281=0x0000) (Reg 0xa282=0x0000) (Reg 0xa283=0x0000) 
(Reg 0xa284=0x0000) (Reg 0xa285=0x0000) (Reg 0xa286=0x0000) (Reg 0xa287=0x0000) 
(Reg 0xa288=0x0000) (Reg 0xa289=0x0000) (Reg 0xa28a=0x0000) (Reg 0xa28b=0x0000) 
(Reg 0xa28c=0x0000) (Reg 0xa28d=0x0000) (Reg 0xa28e=0x0000) (Reg 0xa28f=0x0000) 
(Reg 0xa290=0x0000) (Reg 0xa291=0x0000) (Reg 0xa292=0x0000) (Reg 0xa293=0x0000) 
(Reg 0xa294=0x0000) (Reg 0xa295=0x0000) (Reg 0xa296=0x0000) (Reg 0xa297=0x0000) 
(Reg 0xa298=0x0000) (Reg 0xa299=0x0000) (Reg 0xa29a=0x0000) (Reg 0xa29b=0x0000) 
(Reg 0xa29c=0x0000) (Reg 0xa29d=0x0000) (Reg 0xa29e=0x0000) (Reg 0xa29f=0x0000) 
(Reg 0xa2a0=0x0000) (Reg 0xa2a1=0x0000) (Reg 0xa2a2=0x0000) (Reg 0xa2a3=0x0000) 
(Reg 0xa2a4=0x0000) (Reg 0xa2a5=0x0000) (Reg 0xa2a6=0x0000) (Reg 0xa2a7=0x0000) 
(Reg 0xa2a8=0x0000) (Reg 0xa2a9=0x0000) (Reg 0xa2aa=0x0000) (Reg 0xa2ab=0x0000) 
(Reg 0xa2ac=0x0000) (Reg 0xa2ad=0x0000) (Reg 0xa2ae=0x0000) (Reg 0xa2af=0x0000) 
(Reg 0xa2b0=0x0000) (Reg 0xa2b1=0x0000) (Reg 0xa2b2=0x0000) (Reg 0xa2b3=0x0000) 
(Reg 0xa2b4=0x0000) (Reg 0xa2b5=0x0000) (Reg 0xa2b6=0x0000) (Reg 0xa2b7=0x0000) 
(Reg 0xa2b8=0x0000) (Reg 0xa2b9=0x0000) (Reg 0xa2ba=0x0000) (Reg 0xa2bb=0x0000) 
(Reg 0xa2bc=0x0000) (Reg 0xa2bd=0x0000) (Reg 0xa2be=0x0000) (Reg 0xa2bf=0x0000) 
(Reg 0xa2c0=0x1c39) (Reg 0xa2c1=0x1c39) (Reg 0xa2c2=0x1c39) (Reg 0xa2c3=0x1c39) 
(Reg 0xa2c4=0x1c39) (Reg 0xa2c5=0x1c39) (Reg 0xa2c6=0x1c39) (Reg 0xa2c7=0x1c39) 
(Reg 0xa2c8=0x1c39) (Reg 0xa2c9=0x1c39) (Reg 0xa2ca=0x0000) (Reg 0xa2cb=0x0000) 
(Reg 0xa2cc=0x0000) (Reg 0xa2cd=0x0000) (Reg 0xa2ce=0x0000) (Reg 0xa2cf=0x0000) 
(Reg 0xa2d0=0x0000) (Reg 0xa2d1=0x0000) (Reg 0xa2d2=0x0000) (Reg 0xa2d3=0x0000) 
(Reg 0xa2d4=0x0000) (Reg 0xa2d5=0x0000) (Reg 0xa2d6=0x0000) (Reg 0xa2d7=0x0000) 
(Reg 0xa2d8=0x0000) (Reg 0xa2d9=0x0000) (Reg 0xa2da=0x0000) (Reg 0xa2db=0x0000) 
(Reg 0xa2dc=0x0000) (Reg 0xa2dd=0x0000) (Reg 0xa2de=0x0000) (Reg 0xa2df=0x0000) 
(Reg 0xa2e0=0x0000) 

HOST LANE VR 1 Registers:

 (Reg 0xa400=0x0000) (Reg 0xa401=0x0000) (Reg 0xa402=0x0000) (Reg 0xa403=0x0000) 
(Reg 0xa404=0x0000) (Reg 0xa405=0x0000) (Reg 0xa406=0x0000) (Reg 0xa407=0x0000) 
(Reg 0xa408=0x0000) (Reg 0xa409=0x0000) (Reg 0xa40a=0x0000) (Reg 0xa40b=0x0000) 
(Reg 0xa40c=0x0000) (Reg 0xa40d=0x0000) (Reg 0xa40e=0x0000) (Reg 0xa40f=0x0000) 
(Reg 0xa410=0x0000) (Reg 0xa411=0x0000) (Reg 0xa412=0x0000) (Reg 0xa413=0x0000) 
(Reg 0xa414=0x0000) (Reg 0xa415=0x0000) (Reg 0xa416=0x0000) (Reg 0xa417=0x0000) 
(Reg 0xa418=0x0000) (Reg 0xa419=0x0000) (Reg 0xa41a=0x0000) (Reg 0xa41b=0x0000) 
(Reg 0xa41c=0x0000) (Reg 0xa41d=0x0000) (Reg 0xa41e=0x0000) (Reg 0xa41f=0x0000) 
(Reg 0xa420=0x0001) (Reg 0xa421=0x0001) (Reg 0xa422=0x0001) (Reg 0xa423=0x0001) 
(Reg 0xa424=0x0001) (Reg 0xa425=0x0001) (Reg 0xa426=0x0001) (Reg 0xa427=0x0001) 
(Reg 0xa428=0x0001) (Reg 0xa429=0x0001) (Reg 0xa42a=0x0000) (Reg 0xa42b=0x0000) 
(Reg 0xa42c=0x0000) (Reg 0xa42d=0x0000) (Reg 0xa42e=0x0000) (Reg 0xa42f=0x0000) 
(Reg 0xa430=0x0000) (Reg 0xa431=0x0000) (Reg 0xa432=0x0000) (Reg 0xa433=0x0000) 
(Reg 0xa434=0x0000) (Reg 0xa435=0x0000) (Reg 0xa436=0x0000) (Reg 0xa437=0x0000) 
(Reg 0xa438=0x0000) (Reg 0xa439=0x0000) (Reg 0xa43a=0x0000) (Reg 0xa43b=0x0000) 
(Reg 0xa43c=0x0000) (Reg 0xa43d=0x0000) (Reg 0xa43e=0x0000) (Reg 0xa43f=0x0000) 
(Reg 0xa440=0x0007) (Reg 0xa441=0x0007) (Reg 0xa442=0x0007) (Reg 0xa443=0x0007) 
(Reg 0xa444=0x0007) (Reg 0xa445=0x0007) (Reg 0xa446=0x0007) (Reg 0xa447=0x0007) 
(Reg 0xa448=0x0007) (Reg 0xa449=0x0007) (Reg 0xa44a=0x0000) (Reg 0xa44b=0x0000) 
(Reg 0xa44c=0x0000) (Reg 0xa44d=0x0000) (Reg 0xa44e=0x0000) (Reg 0xa44f=0x0000) 
(Reg 0xa450=0x0000) 

```

**Help:** execute the command "show controllers hundredgige all"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show bgp instance all summary

**Output:**
```

Wed Jul 27 17:18:35.642 CST

BGP instance 0: 'default'
=========================
 BGP router identifier 192.0.2.1, local AS number 65533
BGP generic scan interval 60 secs
Non-stop routing is enabled
BGP table state: Active
Table ID: 0xe0000000   RD version: 2308648196
BGP main routing table version 2308648196
BGP NSR Initial initsync version 2063371958 (Reached)
BGP NSR/ISSU Sync-Group versions 2308648196/0
BGP scan interval 60 secs

BGP is operating in STANDALONE mode.


Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
Speaker       2308648196  2308648196  2308648196  2308648196  2308648196  2308648196
 
Some configured eBGP neighbors (under default or non-default vrfs)
do not have both inbound and outbound policies configured for IPv4 Unicast
address family. These neighbors will default to sending and/or
receiving no routes and are marked with '!' in the output below.
Use the 'show bgp neighbor <nbr_address>' command for details.

Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
192.0.2.1         0 65533 3687720 44027503 2308648193    0    0     6w0d          4
192.0.2.1         0 65533 2998156       0        0    0    0    1y11w Active
192.0.2.1         0 65533  740185  712198 2308648196    0    0    6d12h          0
192.0.2.1         0 65533   19179   11983 2308648196    0    0 01:57:59         10
192.0.2.1         0 65533 3372692  355977 2308648196    0    0     1w6d          0!
192.0.2.1         0 65533 5765678       0        0    0    0    45w1d Idle!

```

**Help:** execute the command "show bgp instance all summary"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show ipv4 interface

**Output:**
```
Mon Feb 13 17:30:47.464 UTC
MgmtEth0/0/CPU0/0 is Up, ipv4 protocol is Up
  Vrf is default (vrfid 0x60000000)
  Internet address is 172.25.82.44/24
  MTU is 1514 (1500 is available to IP)
  Helper address is not set
  Multicast reserved groups joined: 224.0.0.2 224.0.0.1
  Directed broadcast forwarding is disabled
  Outgoing access list is not set
  Inbound  common access list is not set, access list is not set
  Proxy ARP is disabled
  ICMP redirects are never sent
  ICMP unreachables are always sent
  ICMP mask replies are never sent
  Table Id is 0xe0000000
GigabitEthernet0/0/0/0 is Shutdown, ipv4 protocol is Down
  Vrf is default (vrfid 0x60000000)
  Internet protocol processing disabled

```

**Help:** execute the command "show ipv4 interface"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show ip interface brief

**Output:**
```
Interface                      IP-Address      Status          Protocol Vrf-Name
GigabitEthernet0/0/1/18        unassigned      Shutdown        Down     default
GigabitEthernet0/0/1/19        unassigned      Up              Up       default
GigabitEthernet0/0/1/19.2003   10.79.255.0     Up              Up       WAG:OOB
TenGigE0/0/2/0                 unassigned      Up              Up       default
TenGigE0/0/2/0.2396            10.79.255.96    Up              Up       WAG:123
TenGigE0/0/2/0.2397            10.79.255.80    Up              Up       WAG:ABC

```

**Help:** execute the command "show ip interface brief"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show isis neighbors

**Output:**
```
Tue Jan  3 14:57:35.234 UTC

IS-IS 1 neighbors:
System Id      Interface        SNPA           State Holdtime Type IETF-NSF
CSR2           Gi0/0/0/1        5000.0002.0001 Up    23       L1L2 Capable
vMX1           Gi0/0/0/1        0005.8671.9202 Up    18       L1L2 Capable
vMX1           Gi0/0/0/3        *PtoP*         Up    25       L1L2 Capable
vEOS4          Gi0/0/0/2        5000.0003.3766 Up    8        L2   Unable

Total neighbor count: 4

```

**Help:** execute the command "show isis neighbors"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show bfd sessions

**Output:**
```
Interface           Dest Addr           Local det time(int*mult)      State     
                                    Echo             Async   H/W   NPU     
------------------- --------------- ---------------- ---------------- ----------
Fo0/0/1/0           10.100.100.141  45ms(15ms*3)     6s(2s*3)         UP        
                                                             No    n/a            
Fo0/0/0/0           10.100.100.19   45ms(15ms*3)     6s(2s*3)         UP        
                                                             No    n/a            
Fo0/0/0/1           10.100.100.125  45ms(15ms*3)     6s(2s*3)         UP        
                                                             No    n/a            
Fo0/1/0/0           10.100.100.113  45ms(15ms*3)     6s(2s*3)         UP        
                                                             No    n/a            
Fo0/1/1/0           10.100.100.145  45ms(15ms*3)     6s(2s*3)         UP        
                                                             No    n/a            
Fo0/2/1/1           10.100.100.129  45ms(15ms*3)     6s(2s*3)         UP        
                                                             No    n/a            

```

**Help:** execute the command "show bfd sessions"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show interface brief

**Output:**
```

               Intf       Intf        LineP              Encap  MTU        BW
               Name       State       State               Type (byte)    (Kbps)
--------------------------------------------------------------------------------
                Lo5          up          up           Loopback  1500          0
               Lo10          up          up           Loopback  1500          0
               Lo20          up          up           Loopback  1500          0
               Lo21          up          up           Loopback  1500          0
               Lo30          up          up           Loopback  1500          0
                Nu0          up          up               Null  1500          0
              tt300          up          up             TUNNEL  1500          0
              tt301          up          up             TUNNEL  1500          0
              tt302          up          up             TUNNEL  1500          0
              tt303          up          up             TUNNEL  1500          0
              tt304          up          up             TUNNEL  1500          0
              tt305          up          up             TUNNEL  1500          0
              tt306          up          up             TUNNEL  1500          0
              tt307          up          up             TUNNEL  1500          0
              tt404          up          up             TUNNEL  1500          0
              tt405          up          up             TUNNEL  1500          0
              tt406          up          up             TUNNEL  1500          0
              tt407          up          up             TUNNEL  1500          0
              tt408          up          up             TUNNEL  1500          0
              tt409          up          up             TUNNEL  1500          0
              tt410          up          up             TUNNEL  1500          0
              tt411          up          up             TUNNEL  1500          0
              tt412          up          up             TUNNEL  1500          0
              tt413          up          up             TUNNEL  1500          0
              tt414          up          up             TUNNEL  1500          0
              tt415          up          up             TUNNEL  1500          0
              tt416          up          up             TUNNEL  1500          0
              tt417          up          up             TUNNEL  1500          0
              tt418          up          up             TUNNEL  1500          0
              tt419          up          up             TUNNEL  1500          0
    Mg0/RSP0/CPU0/0          up          up               ARPA  1514    1000000
    Mg0/RSP0/CPU0/1  admin-down  admin-down               ARPA  1514          0
    Mg0/RSP1/CPU0/0          up          up               ARPA  1514    1000000
    Mg0/RSP1/CPU0/1  admin-down  admin-down               ARPA  1514          0
          Fo0/0/0/0          up          up               ARPA  9216   40000000
          Fo0/0/0/1          up          up               ARPA  9216   40000000
          Fo0/0/1/0          up          up               ARPA  9216   40000000
          Fo0/0/1/1          up          up               ARPA  9216   40000000
          Fo0/1/0/0          up          up               ARPA  9216   40000000
          Fo0/1/0/1          up          up               ARPA  9216   40000000
          Fo0/1/1/0          up          up               ARPA  9216   40000000
          Fo0/1/1/1          up          up               ARPA  9216   40000000
          Fo0/2/0/0          up          up               ARPA  9216   40000000
          Fo0/2/0/1          up          up               ARPA  9216   40000000
          Fo0/2/1/0          up          up               ARPA  9216   40000000
          Fo0/2/1/1          up          up               ARPA  9216   40000000
          Te0/3/0/0          up          up               ARPA  9216   10000000
          Te0/3/0/1          up          up               ARPA  1514   10000000
          Te0/3/0/2          up          up               ARPA  1514   10000000
          Te0/3/0/3          up          up               ARPA  1514   10000000
          Te0/3/0/4  admin-down  admin-down               ARPA  1514   10000000
          Te0/3/0/5  admin-down  admin-down               ARPA  1514   10000000
          Te0/3/0/6  admin-down  admin-down               ARPA  1514   10000000
          Te0/3/0/7  admin-down  admin-down               ARPA  1514   10000000
          Te0/3/0/8  admin-down  admin-down               ARPA  1514   10000000
          Te0/3/0/9  admin-down  admin-down               ARPA  1514   10000000
         Te0/3/0/10  admin-down  admin-down               ARPA  9216   10000000
         Te0/3/0/11          up          up               ARPA  9216   10000000
         Te0/3/0/12  admin-down  admin-down               ARPA  1514   10000000
         Te0/3/0/13  admin-down  admin-down               ARPA  1514   10000000
         Te0/3/0/14  admin-down  admin-down               ARPA  1514   10000000
         Te0/3/0/15  admin-down  admin-down               ARPA  1514   10000000
         Te0/3/0/16  admin-down  admin-down               ARPA  1514   10000000
         Te0/3/0/17  admin-down  admin-down               ARPA  1514   10000000
         Te0/3/0/18  admin-down  admin-down               ARPA  1514   10000000
         Te0/3/0/19  admin-down  admin-down               ARPA  1514   10000000
         Te0/3/0/20  admin-down  admin-down               ARPA  1514   10000000
         Te0/3/0/21  admin-down  admin-down               ARPA  1514   10000000
         Te0/3/0/22  admin-down  admin-down               ARPA  1514   10000000
         Te0/3/0/23  admin-down  admin-down               ARPA  1514   10000000
          Te0/4/0/0          up          up               ARPA  9216   10000000
          Te0/4/0/1          up          up               ARPA  1514   10000000
          Te0/4/0/2          up          up               ARPA  1514   10000000
          Te0/4/0/3          up          up               ARPA  1514   10000000
          Te0/4/0/4  admin-down  admin-down               ARPA  1514   10000000
          Te0/4/0/5  admin-down  admin-down               ARPA  1514   10000000
          Te0/4/0/6  admin-down  admin-down               ARPA  1514   10000000
          Te0/4/0/7  admin-down  admin-down               ARPA  1514   10000000
          Te0/4/0/8  admin-down  admin-down               ARPA  1514   10000000
          Te0/4/0/9  admin-down  admin-down               ARPA  1514   10000000
         Te0/4/0/10  admin-down  admin-down               ARPA  9216   10000000
         Te0/4/0/11          up          up               ARPA  9216   10000000
         Te0/4/0/12  admin-down  admin-down               ARPA  1514   10000000
         Te0/4/0/13  admin-down  admin-down               ARPA  1514   10000000
         Te0/4/0/14  admin-down  admin-down               ARPA  1514   10000000
         Te0/4/0/15  admin-down  admin-down               ARPA  1514   10000000
         Te0/4/0/16  admin-down  admin-down               ARPA  1514   10000000
         Te0/4/0/17  admin-down  admin-down               ARPA  1514   10000000
         Te0/4/0/18  admin-down  admin-down               ARPA  1514   10000000
         Te0/4/0/19  admin-down  admin-down               ARPA  1514   10000000
         Te0/4/0/20  admin-down  admin-down               ARPA  1514   10000000
         Te0/4/0/21  admin-down  admin-down               ARPA  1514   10000000
         Te0/4/0/22  admin-down  admin-down               ARPA  1514   10000000
         Te0/4/0/23  admin-down  admin-down               ARPA  1514   10000000
          Fo0/6/0/0          up          up               ARPA  9216   40000000
          Fo0/6/0/1  admin-down  admin-down               ARPA  1514   40000000
          Fo0/6/1/0  admin-down  admin-down               ARPA  1514   40000000
          Fo0/6/1/1  admin-down  admin-down               ARPA  1514   40000000
          Fo0/7/0/0        down        down               ARPA  9216   40000000
          Fo0/7/0/1  admin-down  admin-down               ARPA  1514   40000000
          Fo0/7/1/0  admin-down  admin-down               ARPA  1514   40000000
          Fo0/7/1/1  admin-down  admin-down               ARPA  1514   40000000
```

**Help:** execute the command "show interface brief"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show ipv6 neighbors

**Output:**
```
Fri Oct 11 02:35:25.149 UTC
IPv6 Address                              Age Link-layer Addr State Interface            Location
2001:db8:ffff::12:2                      110  0c07.a11a.b801 REACH Gi0/0/0/0            0/0/CPU0       
fe80::e07:a1ff:fe1a:b801                 99   0c07.a11a.b801 REACH Gi0/0/0/0            0/0/CPU0       
[Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/0            0/0/CPU0       
[Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/1            0/0/CPU0       
[Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/2            0/0/CPU0       
2001:db8:1000:beef::1                    105  ca01.0ff1.0008 REACH Gi0/0/0/3            0/0/CPU0       
2001:db8:1000:beef::2                    108  ca02.0fff.0008 REACH Gi0/0/0/3            0/0/CPU0       
2001:db8:1000:beef::3                    105  ca03.100d.0008 REACH Gi0/0/0/3            0/0/CPU0       
fe80::c801:fff:fef1:8                    89   ca01.0ff1.0008 REACH Gi0/0/0/3            0/0/CPU0       
fe80::c802:fff:feff:8                    105  ca02.0fff.0008 REACH Gi0/0/0/3            0/0/CPU0       
fe80::c803:10ff:fe0d:8                   91   ca03.100d.0008 REACH Gi0/0/0/3            0/0/CPU0       
[Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/3            0/0/CPU0       

```

**Help:** execute the command "show ipv6 neighbors"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show install active

**Output:**
```
Mon Feb 28 23:36:31.563 CET
Label : 7.3.2

Node 0/RP0/CPU0 [RP]
  Boot Partition: xr_lv38
  Active Packages: 18
        ncs5500-xr-7.3.2 version=7.3.2 [Boot image]
        ncs5500-mcast-3.0.0.0-r732
        ncs5500-dpa-3.0.0.1-r732.CSCwa07903
        ncs5500-mpls-2.1.0.0-r732
        ncs5500-os-6.0.0.1-r732.CSCvq20498
        ncs5500-k9sec-3.2.0.0-r732
        ncs5500-os-support-4.0.0.2-r732.CSCvz72160
        ncs5500-eigrp-1.0.0.0-r732
        ncs5500-iosxr-fwding-4.1.0.1-r732.CSCwa34439
        ncs5500-li-1.0.0.0-r732
        ncs5500-parser-3.0.0.1-r732.CSCwa44780
        ncs5500-dpa-fwding-4.1.0.3-r732.CSCwa01375
        ncs5500-mgbl-3.0.0.0-r732
        ncs5500-isis-2.1.0.0-r732
        ncs5500-bgp-2.0.0.1-r732.CSCvz94897
        ncs5500-mpls-te-rsvp-3.1.0.0-r732
        ncs5500-infra-5.0.0.5-r732.CSCvu13993
        ncs5500-ospf-3.0.0.0-r732

Node 0/RP1/CPU0 [RP]
  Boot Partition: xr_lv38
  Active Packages: 18
        ncs5500-xr-7.3.2 version=7.3.2 [Boot image]
        ncs5500-mcast-3.0.0.0-r732
        ncs5500-dpa-3.0.0.3-r732.CSCvz54050
        ncs5500-mpls-2.1.0.0-r732
        ncs5500-os-6.0.0.1-r732.CSCvq20498
        ncs5500-k9sec-3.2.0.0-r732
        ncs5500-eigrp-1.0.0.0-r732
        ncs5500-os-support-4.0.0.5-r732.CSCwa01498
        ncs5500-iosxr-fwding-4.1.0.1-r732.CSCwa34439
        ncs5500-li-1.0.0.0-r732
        ncs5500-parser-3.0.0.1-r732.CSCwa44780
        ncs5500-dpa-fwding-4.1.0.3-r732.CSCwa01375
        ncs5500-mgbl-3.0.0.0-r732
        ncs5500-isis-2.1.0.0-r732
        ncs5500-bgp-2.0.0.1-r732.CSCvz94897
        ncs5500-mpls-te-rsvp-3.1.0.0-r732
        ncs5500-infra-5.0.0.5-r732.CSCvu13993
        ncs5500-ospf-3.0.0.0-r732

Node 0/0/CPU0 [LC]
  Boot Partition: xr_lv0
  Active Packages: 18
        ncs5500-xr-7.3.2 version=7.3.2 [Boot image]
        ncs5500-eigrp-1.0.0.0-r732
        ncs5500-k9sec-3.2.0.0-r732
        ncs5500-mpls-2.1.0.0-r732
        ncs5500-li-1.0.0.0-r732
        ncs5500-mgbl-3.0.0.0-r732
        ncs5500-mpls-te-rsvp-3.1.0.0-r732
        ncs5500-isis-2.1.0.0-r732
        ncs5500-ospf-3.0.0.0-r732
        ncs5500-mcast-3.0.0.0-r732
        ncs5500-bgp-2.0.0.1-r732.CSCvz94897
        ncs5500-iosxr-fwding-4.1.0.1-r732.CSCwa34439
        ncs5500-os-6.0.0.1-r732.CSCvq20498
        ncs5500-os-support-4.0.0.5-r732.CSCwa01498
        ncs5500-dpa-3.0.0.5-r732.CSCwa05129
        ncs5500-parser-3.0.0.1-r732.CSCwa44780
        ncs5500-infra-5.0.0.5-r732.CSCvu13993
        ncs5500-dpa-fwding-4.1.0.3-r732.CSCwa01375

Node 0/1/CPU0 [LC]
  Boot Partition: xr_lv38
  Active Packages: 18
        ncs5500-xr-7.3.2 version=7.3.2 [Boot image]
        ncs5500-dpa-3.0.0.5-r732.CSCwa05129
        ncs5500-mcast-3.0.0.0-r732
        ncs5500-mpls-2.1.0.0-r732
        ncs5500-os-6.0.0.1-r732.CSCvq20498
        ncs5500-k9sec-3.2.0.0-r732
        ncs5500-eigrp-1.0.0.0-r732
        ncs5500-os-support-4.0.0.5-r732.CSCwa01498
        ncs5500-iosxr-fwding-4.1.0.1-r732.CSCwa34439
        ncs5500-dpa-fwding-4.1.0.1-r732.CSCwa03269
        ncs5500-li-1.0.0.0-r732
        ncs5500-parser-3.0.0.1-r732.CSCwa44780
        ncs5500-mgbl-3.0.0.0-r732
        ncs5500-isis-2.1.0.0-r732
        ncs5500-bgp-2.0.0.1-r732.CSCvz94897
        ncs5500-mpls-te-rsvp-3.1.0.0-r732
        ncs5500-infra-5.0.0.5-r732.CSCvu13993
        ncs5500-ospf-3.0.0.0-r732

```

**Help:** execute the command "show install active"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show redundancy summary

**Output:**
```
Tue Mar  7 14:33:54.330 EST
  Active/Primary   Standby/Backup
  --------------   --------------
  0/RSP0/CPU0(A)   0/RSP1/CPU0(S) (Node Ready, NSR: Ready)
  0/RSP0/CPU0(P)   0/RSP1/CPU0(B) (Proc Group Ready, NSR: Ready)

```

**Help:** execute the command "show redundancy summary"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show pim ipv4 group-map

**Output:**
```

Wed Jul 27 17:18:36.472 CST

IP PIM Group Mapping Table
(* indicates group mappings being used)
(+ indicates BSR group mappings active in MRIB)
 
Group Range         Proto Client   Groups RP address      Info

224.0.1.1/32*       DM    perm     0      0.0.0.0
224.0.1.2/32*       DM    perm     1      0.0.0.0
224.0.0.0/24*       NO    perm     0      0.0.0.0
232.0.0.0/8*        SSM   config   40     0.0.0.0
224.0.0.0/4*        SM    static   7      0.0.0.0         RPF: Null,0.0.0.0
```

**Help:** execute the command "show pim ipv4 group-map"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show cdp neighbors detail

**Output:**
```
-------------------------
Device ID: nyc-dc-dcm005.ntc.com
SysName :
Entry address(es):
  IPv4 address: 10.100.1.54
Platform: cisco WS-C4948E,  Capabilities: Router Switch IGMP
Interface: MgmtEth0/RSP0/CPU0/0
Port ID (outgoing port): GigabitEthernet1/9
Holdtime : 134 sec

Version :
Cisco IOS Software, Catalyst 4500 L3 Switch Software (cat4500e-ENTSERVICESK9-M), Version 15.0(2)SG10, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
 Copyright (c) 1986-2015 by Cisco Systems, Inc.
Compiled Tue 07-Apr-15 10:40 by prod_rel_team

advertisement version: 2
Native VLAN: 103
Duplex: full
 
-------------------------
Device ID: nyc-dc-dcm006.ntc.com
SysName :
Entry address(es):
  IPv4 address: 10.100.1.55
Platform: cisco WS-C4948E,  Capabilities: Router Switch IGMP
Interface: MgmtEth0/RSP1/CPU0/0
Port ID (outgoing port): GigabitEthernet1/9
Holdtime : 160 sec

Version :
Cisco IOS Software, Catalyst 4500 L3 Switch Software (cat4500e-ENTSERVICESK9-M), Version 15.0(2)SG10, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2015 by Cisco Systems, Inc.
Compiled Tue 07-Apr-15 10:40 by prod_rel_team
 
advertisement version: 2
Native VLAN: 103
Duplex: full

-------------------------
 Device ID: nyc-dc-c90.ntc.com
SysName : nyc-dc-c90.ntc.com
Entry address(es):
  IPv4 address: 10.100.100.141
Platform: cisco CRS,  Capabilities: Router Switch IGMP
Interface: FortyGigE0/0/1/0
Port ID (outgoing port): FortyGigE0/0/0/2
 Holdtime : 155 sec

Version :
Cisco IOS XR Software, Version 5.1.2[Default]
 Copyright (c) 2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full

-------------------------
Device ID: nyc-dc-d02.ntc.com(FXS182XXXXX)
 SysName : nyc-dc-d02
Entry address(es):
  IPv4 address: 10.100.100.162
Platform: N77-C7706,  Capabilities: Router Switch
Interface: FortyGigE0/0/1/1
Port ID (outgoing port): Ethernet6/1
Holdtime : 126 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 6.2(12)

advertisement version: 2
Duplex: full

-------------------------
Device ID: nyc-dc-c97
SysName : nyc-dc-c97
 Entry address(es):
  IPv4 address: 10.100.100.19
Platform: cisco ASR9K Series,  Capabilities: Router
Interface: FortyGigE0/0/0/0
Port ID (outgoing port): FortyGigE0/0/0/0
Holdtime : 170 sec

Version :
Cisco IOS XR Software, Version 5.3.4[Default]
Copyright (c) 2016 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full

-------------------------
Device ID: nyc-dc-c91.ntc.com
 SysName : nyc-dc-c91.ntc.com
Entry address(es):
  IPv4 address: 10.100.100.125
 Platform: cisco CRS,  Capabilities: Router
Interface: FortyGigE0/0/0/1
Port ID (outgoing port): FortyGigE0/0/0/2
Holdtime : 122 sec

Version :
Cisco IOS XR Software, Version 5.1.2[Default]
Copyright (c) 2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full

-------------------------
 Device ID: nyc-dc-c97
SysName : nyc-dc-c97
Entry address(es):
  IPv4 address: 10.100.100.113
Platform: cisco ASR9K Series,  Capabilities: Router
Interface: FortyGigE0/1/0/0
Port ID (outgoing port): FortyGigE0/1/0/0
Holdtime : 132 sec

Version :
Cisco IOS XR Software, Version 5.3.4[Default]
Copyright (c) 2016 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full

-------------------------
 Device ID: nyc-dc-d03.ntc.com(FXS182XXXXX)
SysName : nyc-dc-d03
Entry address(es):
  IPv4 address: 10.100.100.190
Platform: N77-C7706,  Capabilities: Router Switch
Interface: FortyGigE0/1/0/1
Port ID (outgoing port): Ethernet6/1
 Holdtime : 144 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 6.2(12)

advertisement version: 2
Duplex: full

-------------------------
 Device ID: nyc-dc-c90.ntc.com
SysName : nyc-dc-c90.ntc.com
Entry address(es):
  IPv4 address: 10.100.100.145
Platform: cisco CRS,  Capabilities: Router
 Interface: FortyGigE0/1/1/0
Port ID (outgoing port): FortyGigE0/4/0/2
Holdtime : 174 sec

Version :
Cisco IOS XR Software, Version 5.1.2[Default]
Copyright (c) 2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full

 -------------------------
Device ID: nyc-dc-z50a.ntc.com(JAF18XXXXX)
SysName : nyc-dc-z50a
Entry address(es):
  IPv4 address: 10.100.100.116
Platform: N77-C7710,  Capabilities: Router Switch
Interface: FortyGigE0/1/1/1
Port ID (outgoing port): Ethernet4/3
Holdtime : 153 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 6.2(12)

advertisement version: 2
Duplex: full

-------------------------
Device ID: nyc-dc-d04.ntc.com(FXS18XXXXXX)
 SysName : nyc-dc-d04
Entry address(es):
  IPv4 address: 10.100.100.194
Platform: N77-C7706,  Capabilities: Router Switch
Interface: FortyGigE0/2/1/0
Port ID (outgoing port): Ethernet6/1
Holdtime : 155 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 6.2(12)

advertisement version: 2
Duplex: full

-------------------------
Device ID: nyc-dc-c91.ntc.com
SysName : nyc-dc-c91.ntc.com
Entry address(es):
  IPv4 address: 10.100.100.129
Platform: cisco CRS,  Capabilities: Router
Interface: FortyGigE0/2/1/1
Port ID (outgoing port): FortyGigE0/4/0/2
Holdtime : 130 sec

Version :
Cisco IOS XR Software, Version 5.1.2[Default]
Copyright (c) 2015 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full

-------------------------
Device ID: nyc-dc-d01.ntc.com(FXS182XXXXX)
 SysName : nyc-dc-d01
Entry address(es):
  IPv4 address: 10.100.100.158
Platform: N77-C7706,  Capabilities: Router Switch
Interface: FortyGigE0/2/0/0
Port ID (outgoing port): Ethernet6/1
Holdtime : 128 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 6.2(12)

advertisement version: 2
Duplex: full

-------------------------
Device ID: nyc-dc-z50b.ntc.com(JAF181XXXXX)
 SysName : nyc-dc-z50b
Entry address(es):
  IPv4 address: 10.100.100.111
 Platform: N77-C7710,  Capabilities: Router Switch
Interface: FortyGigE0/2/0/1
 Port ID (outgoing port): Ethernet4/3
Holdtime : 158 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 6.2(12)

advertisement version: 2
Duplex: full

-------------------------
Device ID: nyc-dc-dcc001.ntc.com
 SysName :
Entry address(es):
  IPv4 address: 10.100.100.174
Platform: cisco WS-C4510R+E,  Capabilities: Router Switch IGMP
Interface: TenGigE0/3/0/0
 Port ID (outgoing port): TenGigabitEthernet6/1
Holdtime : 142 sec

Version :
Cisco IOS Software, Catalyst 4500 L3 Switch  Software (cat4500e-UNIVERSALK9-M), Version 15.2(2)E3, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
 Copyright (c) 1986-2015 by Cisco Systems, Inc.
Compiled Wed 26-Aug-15 06:05 by prod_rel_team

advertisement version: 2
Duplex: full

-------------------------
 Device ID: nyc-dc-d57
SysName : nyc-dc-d57
Entry address(es):
  IPv4 address: 10.100.100.115
Platform: cisco ASR9K Series,  Capabilities: Router
Interface: TenGigE0/3/0/1
Port ID (outgoing port): TenGigE0/2/0/0
Holdtime : 150 sec
 
Version :
Cisco IOS XR Software, Version 4.3.2[Default]
Copyright (c) 2013 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full

-------------------------
 Device ID: nyc-dc-d40b.ntc.com(JAF182XXXXX)
SysName : nyc-dc-d40b
Entry address(es):
  IPv4 address: 10.100.100.114
Platform: N77-C7710,  Capabilities: Router Switch
Interface: TenGigE0/3/0/2
Port ID (outgoing port): Ethernet4/1
Holdtime : 171 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 6.2(12)

advertisement version: 2
Duplex: full

-------------------------
 Device ID: nyc-dc-d80.ntc.com(FOC184XXXXX)
SysName : nyc-dc-d80
Entry address(es):
  IPv4 address: 10.100.100.117
Platform: N5K-C56128P,  Capabilities: Router Switch IGMP
Interface: TenGigE0/3/0/3
Port ID (outgoing port): Ethernet2/1
 Holdtime : 140 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 7.0(7)N1(1)

advertisement version: 2
Duplex: full

-------------------------
 Device ID: nyc-dc-dcc002.ntc.com
SysName :
Entry address(es):
  IPv4 address: 10.100.100.178
Platform: cisco WS-C4510R+E,  Capabilities: Router Switch IGMP
 Interface: TenGigE0/4/0/0
Port ID (outgoing port): TenGigabitEthernet6/1
 Holdtime : 147 sec

Version :
Cisco IOS Software, Catalyst 4500 L3 Switch  Software (cat4500e-UNIVERSALK9-M), Version 15.2(2)E3, RELEASE SOFTWARE (fc3)
 Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2015 by Cisco Systems, Inc.
Compiled Wed 26-Aug-15 06:05 by prod_rel_team

advertisement version: 2
Duplex: full

-------------------------
Device ID: nyc-dc-d57
 SysName : nyc-dc-d57
Entry address(es):
  IPv4 address: 10.100.100.115
Platform: cisco ASR9K Series,  Capabilities: Router
Interface: TenGigE0/4/0/1
Port ID (outgoing port): TenGigE1/2/0/0
Holdtime : 120 sec

Version :
Cisco IOS XR Software, Version 4.3.2[Default]
Copyright (c) 2013 by Cisco Systems, Inc.
 
advertisement version: 2
Duplex: full

-------------------------
Device ID: nyc-dc-d40a.ntc.com(JAF182XXXXX)
SysName : nyc-dc-d40a
Entry address(es):
  IPv4 address: 10.100.100.113
Platform: N77-C7710,  Capabilities: Router Switch
Interface: TenGigE0/4/0/2
Port ID (outgoing port): Ethernet4/1
Holdtime : 171 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 6.2(12)

advertisement version: 2
Duplex: full

-------------------------
 Device ID: nyc-dc-d81.ntc.com(FOC182XXXXX)
SysName : nyc-dc-d81
Entry address(es):
  IPv4 address: 10.100.100.118
Platform: N5K-C56128P,  Capabilities: Router Switch IGMP
Interface: TenGigE0/4/0/3
Port ID (outgoing port): Ethernet1/1
 Holdtime : 141 sec

Version :
Cisco Nexus Operating System (NX-OS) Software, Version 7.0(7)N1(1)

advertisement version: 2
Duplex: full

-------------------------
 Device ID: nyc-dc-c97
SysName : nyc-dc-c97
Entry address(es):
  IPv4 address: 192.168.169.21
Platform: cisco ASR9K Series,  Capabilities: Router
Interface: FortyGigE0/6/0/0
Port ID (outgoing port): FortyGigE0/6/0/0
Holdtime : 163 sec

Version :
Cisco IOS XR Software, Version 5.3.4[Default]
Copyright (c) 2016 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full

-------------------------
 Device ID: nyc-dc-c97
SysName : nyc-dc-c97
Entry address(es):
  IPv4 address: 192.168.169.21
Platform: cisco ASR9K Series,  Capabilities: Router
Interface: FortyGigE0/6/0/0
Port ID (outgoing port): FortyGigE0/7/0/0
Holdtime : 140 sec

Version :
Cisco IOS XR Software, Version 5.3.4[Default]
Copyright (c) 2016 by Cisco Systems, Inc.

advertisement version: 2
Duplex: full


```

**Help:** execute the command "show cdp neighbors detail"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show asic-errors all location

**Output:**
```
************************************************************
*                  Fia ASIC Error Summary                  *
************************************************************
Instance            : 0
Number of nodes     : 22
SBE error count     : 33
 MBE error count     : 44
Parity error count  : 55
CRC error count     : 99999
 Generic error count : 0
Reset error count   : 0
--------------------
Instance            : 1
Number of nodes     : 0
SBE error count     : 23
MBE error count     : 0
Parity error count  : 0
CRC error count     : 0
Generic error count : 0
Reset error count   : 0
--------------------
Instance            : 2
Number of nodes     : 0
SBE error count     : 0
MBE error count     : 0
Parity error count  : 0
CRC error count     : 0
Generic error count : 0
Reset error count   : 0
--------------------
Instance            : 3
 Number of nodes     : 0
SBE error count     : 0
MBE error count     : 0
 Parity error count  : 0
CRC error count     : 0
Generic error count : 0
 Reset error count   : 0
--------------------

************************************************************
*                Prm_np ASIC Error Summary                 *
************************************************************
Instance            : 0
Number of nodes     : 0
SBE error count     : 0
 MBE error count     : 0
Parity error count  : 0
CRC error count     : 0
 Generic error count : 0
Reset error count   : 0
--------------------
Instance            : 1
Number of nodes     : 0
SBE error count     : 0
MBE error count     : 0
Parity error count  : 0
CRC error count     : 0
Generic error count : 0
Reset error count   : 0
--------------------
Instance            : 2
Number of nodes     : 0
SBE error count     : 0
MBE error count     : 0
Parity error count  : 0
CRC error count     : 0
Generic error count : 0
Reset error count   : 0
--------------------
Instance            : 3
 Number of nodes     : 0
SBE error count     : 0
MBE error count     : 0
 Parity error count  : 0
CRC error count     : 0
Generic error count : 0
 Reset error count   : 0
--------------------
Instance            : 4
Number of nodes     : 0
SBE error count     : 0
MBE error count     : 0
Parity error count  : 0
CRC error count     : 0
Generic error count : 0
Reset error count   : 0
--------------------
Instance            : 5
Number of nodes     : 0
SBE error count     : 0
MBE error count     : 0
Parity error count  : 0
CRC error count     : 0
Generic error count : 0
Reset error count   : 0
--------------------
Instance            : 6
Number of nodes     : 0
SBE error count     : 0
MBE error count     : 0
Parity error count  : 0
CRC error count     : 0
Generic error count : 0
Reset error count   : 0
--------------------
Instance            : 7
Number of nodes     : 0
SBE error count     : 0
MBE error count     : 0
Parity error count  : 0
CRC error count     : 0
Generic error count : 0
Reset error count   : 0
--------------------

```

**Help:** execute the command "show asic-errors all location"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show inventory

**Output:**
```
Tue Jan 16 13:30:53.501 AEST

NAME: "Rack 0", DESCR: "Cisco 8200 2RU 32x400G QSFP56-DD w/IOS XR HBM MACsec"
PID: 8202-32FH-M       , VID: V03, SN: FLM27ABCDEF

NAME: "0/RP0/CPU0", DESCR: "Cisco 8200 2RU 32x400G QSFP56-DD w/IOS XR HBM MACsec"
PID: 8202-32FH-M       , VID: V03, SN: FLM27ZBCDEF

 NAME: "FourHundredGigE0/0/0/0", DESCR: "Cisco QSFPDD 400G LR4 Pluggable Optics Module"
PID: QDD-400G-LR4-S    , VID: V01 , SN: INL26ABCAUG

NAME: "FourHundredGigE0/0/0/28", DESCR: "Cisco QSFPDD 400G LR4 Pluggable Optics Module"
PID: QDD-400G-LR4-S    , VID: V01 , SN: INL2ABCDEFG

NAME: "FourHundredGigE0/0/0/29", DESCR: "Cisco QSFPDD 400G LR4 Pluggable Optics Module"
PID: QDD-400G-LR4-S    , VID: V01 , SN: INL261ABCDE

NAME: "HundredGigE0/0/0/30", DESCR: "Non-Cisco QSFP28 100G CWDM4 MSA WITH FEC Pluggable Optics Module"
PID: Q.161HG.2.C       , VID: 01, SN: F78AAB5

NAME: "HundredGigE0/0/0/31", DESCR: "Non-Cisco QSFP28 100G CWDM4 MSA WITH FEC Pluggable Optics Module"
PID: Q.161HG.2.C       , VID: 01, SN: F78AAB6

NAME: "0/FB0", DESCR: "Cisco 8000 Series Fan Controller Board on 8202-32FH-M"
PID: 8202-32FH-M[FB]   , VID: N/A, SN: FLM2ZABCDEF

NAME: "0/FT0", DESCR: "Cisco Fixed Routers V3 Fan with Port-side Air Intake"
PID: FAN-PI-V3         , VID: V01, SN: DCH27ABCDEF

NAME: "0/FT1", DESCR: "Cisco Fixed Routers V3 Fan with Port-side Air Intake"
PID: FAN-PI-V3         , VID: V01, SN: DCH27BBCDEF

NAME: "0/FT2", DESCR: " Cisco Fixed Routers V3 Fan with Port-side Air Intake"
PID: FAN-PI-V3         , VID: V01, SN: DCH27CBCDEF

NAME: "0/FT3", DESCR: "Cisco Fixed Routers V3 Fan with Port-side Air Intake"
PID: FAN-PI-V3         , VID: V01, SN: DCH27DBCDEF
 
NAME: "0/PM0", DESCR: "2000W AC Power Module with Port-side Air Intake"
PID: PSU2KW-ACPI       , VID: V01 , SN: POG27DBCDEF

NAME: "0/PM1", DESCR: "2000W AC Power Module with Port-side Air Intake"
PID: PSU2KW-ACPI       , VID: V01 , SN: POG27ABCDEF

```

**Help:** execute the command "show inventory"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show controller fabric plane all

**Output:**
```
Sun Feb  25 06:32:34.404 UTC

Plane Admin Plane    up->dn  up->mcast
Id    State State    counter   counter
--------------------------------------
0     UP    UP             0         0
1     UP    UP             0         0
2     UP    DN             0         0
3     UP    UP             0         0
4     UP    UP             0         0
5     UP    UP             0         0
```

**Help:** execute the command "show controller fabric plane all"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show vrf all detail

**Output:**
```

Wed Jul 27 17:18:32.001 CST

VRF red; RD not set; VPN ID not set
 VRF mode: Regular
Description not set
Address family IPV4 Unicast
  No import VPN route-target communities
  No export VPN route-target communities
  No import route policy
  No export route policy
Address family IPV6 Unicast
  No import VPN route-target communities
  No export VPN route-target communities
  No import route policy
  No export route policy

VRF blue; RD not set; VPN ID not set
VRF mode: Regular
Description not set
Interfaces:
  BVI10
 Address family IPV4 Unicast
  No import VPN route-target communities
  No export VPN route-target communities
  No import route policy
  No export route policy
Address family IPV6 Unicast
  No import VPN route-target communities
  No export VPN route-target communities
  No import route policy
  No export route policy

VRF green; RD not set; VPN ID not set
VRF mode: Regular
Description not set
Interfaces:
  GigabitEthernet200/0/0/1
  GigabitEthernet200/0/0/2
  GigabitEthernet300/0/0/1
  GigabitEthernet300/0/0/2
  TenGigE0/0/0/10.10
  Bundle-Ether10.10
  Bundle-Ether10.20
  Bundle-Ether20.10
  Bundle-Ether20.20
  Bundle-Ether30.10
  Bundle-Ether40.10
  Bundle-Ether50.10
  Loopback0
 Address family IPV4 Unicast
  No import VPN route-target communities
  No export VPN route-target communities
  No import route policy
  No export route policy
Address family IPV6 Unicast
  No import VPN route-target communities
  No export VPN route-target communities
  No import route policy
  No export route policy

VRF purple; RD not set; VPN ID not set
VRF mode: Regular
 Description not set
Interfaces:
  Loopback1
  Bundle-Ether10.10
  Bundle-Ether10.20
  Bundle-Ether10.30
  GigabitEthernet100/0/0/10.10
  GigabitEthernet100/0/0/10.20
  GigabitEthernet200/0/0/20.10
  GigabitEthernet200/0/0/20.20
  GigabitEthernet300/0/0/30.10
  GigabitEthernet300/0/0/30.20
  TenGigE0/0/0/10.10
  TenGigE0/2/0/20.10
  TenGigE0/2/0/20.20
Address family IPV4 Unicast
  No import VPN route-target communities
  No export VPN route-target communities
  No import route policy
  No export route policy
Address family IPV6 Unicast
  No import VPN route-target communities
  No export VPN route-target communities
  No import route policy
  No export route policy

VRF brown; RD not set; VPN ID not set
VRF mode: Regular
Description not set
Interfaces:
  GigabitEthernet100/0/0/10
  GigabitEthernet300/0/0/20
  Bundle-Ether10.10
  Bundle-Ether10.20
Address family IPV4 Unicast
  No import VPN route-target communities
  No export VPN route-target communities
  No import route policy
  No export route policy
Address family IPV6 Unicast
  No import VPN route-target communities
  No export VPN route-target communities
  No import route policy
  No export route policy

VRF vrf-test; RD not set; VPN ID not set
VRF mode: Regular
Description this is a description
 Address family IPV4 Unicast
  Import VPN route-target communities:
    RT:65000:42
  Export VPN route-target communities:
    RT:65000:43
  No import route policy
  No export route policy
Address family IPV6 Unicast
  No import VPN route-target communities
  No export VPN route-target communities
  No import route policy
  No export route policy

```

**Help:** execute the command "show vrf all detail"

**Prompt:**
- cisco_xr>
- cisco_xr#

### admin show platform

**Output:**
```
Tue Mar  7 14:29:29.338 EST
Node            Type                      State            Config State
-----------------------------------------------------------------------------
0/RSP0/CPU0     A9K-RSP440-TR(Active)     IOS XR RUN       PWR,NSHUT,MON
0/RSP1/CPU0     A9K-RSP440-TR(Standby)    IOS XR RUN       PWR,NSHUT,MON
0/FT0/SP        ASR-9010-FAN-V2           READY            
0/FT1/SP        ASR-9010-FAN-V2           READY            
0/0/0           A9K-MPA-2X40GE            OK               PWR,NSHUT,MON

```

**Help:** execute the command "admin show platform"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show platform summary location all

**Output:**
```

Wed Jul 27 17:18:08.328 CST
-------------------------------------------------------------------------------
     Platform Node : 0/RP0/CPU0 (slot 0)
               PID : ASR-9900-RP-SE
         Card Type : ASR 9900 Route Processor for Service Edge
            VID/SN : V02 / XXXXXXXXXXX
        Oper State : IOS XR RUN
        Last Reset : User Initiated reload                                                  Process: reload
                   : Wed Jul 31 07:07:56 2019
     Configuration : Power is enabled
		     Bootup enabled.
		     Monitoring enabled
        Rommon Ver : Version 5.15
        IOS SW Ver : 5.3.2
        Main Power : Power state Enabled. Estimate power 380 Watts of power required.
            Faults : N/A
-------------------------------------------------------------------------------
     Platform Node : 0/RP1/CPU0 (slot 1)
               PID : ASR-9900-RP-SE
         Card Type : ASR 9900 Route Processor for Service Edge
            VID/SN : V02 / XXXXXXXXXXX
        Oper State : IOS XR RUN
        Last Reset : dSC node reload is required by install operation                       Process: instdir
                   : Wed Jan 27 20:49:21 2016
     Configuration : Power is enabled
		     Bootup enabled.
		     Monitoring enabled
        Rommon Ver : Version 5.15
        IOS SW Ver : 5.3.2
        Main Power : Power state Enabled. Estimate power 380 Watts of power required.
            Faults : N/A
-------------------------------------------------------------------------------
     Platform Node : 0/0/CPU0 (slot 2)
               PID : A9K-24X10GE-TR
         Card Type : 24-port 10GE, Packet Transport Optimized LC
            VID/SN : V10 / XXXXXXXXXXX
        Oper State : IOS XR RUN
        Last Reset : N/A
                   : N/A
     Configuration : Power is enabled
		     Bootup enabled.
		     Monitoring enabled
        Rommon Ver : Version 3.2(20150713:063058)
        IOS SW Ver : 5.3.2
        Main Power : Power state Enabled. Estimate power 850 Watts of power required.
            Faults : N/A
-------------------------------------------------------------------------------
     Platform Node : 0/1/CPU0 (slot 3)
               PID : A9K-24X10GE-TR
         Card Type : 24-port 10GE, Packet Transport Optimized LC
            VID/SN : V07 / XXXXXXXXXXX
        Oper State : IOS XR RUN
        Last Reset : N/A
                   : N/A
     Configuration : Power is enabled
		     Bootup enabled.
		     Monitoring enabled
        Rommon Ver : Version 3.3(20150930:043930)
        IOS SW Ver : 5.3.2
        Main Power : Power state Enabled. Estimate power 850 Watts of power required.
            Faults : N/A
-------------------------------------------------------------------------------
     Platform Node : 0/2/CPU0 (slot 4)
               PID : A9K-24X10GE-TR
         Card Type : 24-port 10GE, Packet Transport Optimized LC
            VID/SN : V07 / XXXXXXXXXXX
        Oper State : IOS XR RUN
        Last Reset : N/A
                   : N/A
     Configuration : Power is enabled
		     Bootup enabled.
		     Monitoring enabled
        Rommon Ver : Version 3.3(20150930:043930)
        IOS SW Ver : 5.3.2
        Main Power : Power state Enabled. Estimate power 850 Watts of power required.
            Faults : N/A
-------------------------------------------------------------------------------
```

**Help:** execute the command "show platform summary location all"

**Prompt:**
- cisco_xr>
- cisco_xr#

### admin show environment power

**Output:**
```
Fri Jan 17 14:45:54.414 EST
================================================================================
 CHASSIS LEVEL POWER INFO: 0
================================================================================
   Total output power capacity (Group 0 + Group 1) :    6000W +    6000W
   Total output power required                     :    2493W
   Total power input                               :    1334W
   Total power output                              :    1246W

Power Group 0: 
================================================================================
   Power       Supply      --------Input-------   ----Output----    Status
   Module      Type        Volts A/B   Amps A/B   Volts     Amps    
================================================================================
   0/PM0       3kW-DC      54.0/54.0   3.3/ 3.5    12.1     27.0    Failed 
   0/PM1       3kW-DC      54.0/54.0   3.0/ 2.9    12.1     25.8    OK 

 Total of Power Group 0:       686W/  ( 6.3/ 6.4)A     639W/ 52.8A

Power Group 1: 
================================================================================
   Power       Supply      --------Input-------   ----Output----    Status
   Module      Type        Volts A/B   Amps A/B   Volts     Amps    
================================================================================
   0/PM2       3kW-DC      54.0/54.0   2.7/ 2.9    12.1     23.8    OK 
   0/PM3       3kW-DC      54.0/54.0   3.1/ 3.3    12.1     26.4    OK 

 Total of Power Group 1:       648W/  ( 5.8/ 6.2)A     607W/ 50.2A

================================================================================
   Location     Card Type            Power       Power       Status
                                     Allocated   Used
                                     Watts       Watts
================================================================================
   0/0          NC55-36X100G           902         504       ON 
   0/1                 -                25           -       RESERVED 
   0/2                 -                25           -       RESERVED 
   0/3                 -                25           -       RESERVED 
   0/RP0        NC55-RP                 90          37       ON 
   0/RP1        NC55-RP                 90          28       ON 
   0/FC0        NC55-5504-FC           124          89       ON 
   0/FC1        NC55-5504-FC           124          90       ON 
   0/FC2        NC55-5504-FC           124          88       ON 
   0/FC3        NC55-5504-FC           124          88       ON 
   0/FC4        NC55-5504-FC           124          87       ON 
   0/FC5        NC55-5504-FC           124          88       ON 
   0/FT0        NC55-5504-FAN          174          20       ON 
   0/FT1        NC55-5504-FAN          174          19       ON 
   0/FT2        NC55-5504-FAN          174          21       ON 
   0/SC0        NC55-SC                 35          17       ON 
   0/SC1        NC55-SC                 35          15       ON 

```

**Help:** execute the command "admin show environment power"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show pim neighbor

**Output:**
```
Tue Mar  7 14:37:03.743 EST

PIM neighbors in VRF default
Flag: B - Bidir capable, P - Proxy capable, DR - Designated Router,
      E - ECMP Redirect capable
      * indicates the neighbor created for this router

 Neighbor Address             Interface              Uptime    Expires  DR pri   Flags

10.100.100.129               FortyGigE0/2/1/1       4w2d      00:01:41 1      B P
10.100.100.130*              FortyGigE0/2/1/1       4w2d      00:01:25 1 (DR) B E
10.100.100.125               FortyGigE0/0/0/1       4w2d      00:01:27 1      B P


```

**Help:** execute the command "show pim neighbor"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show controllers all phy

**Output:**
```
PHY data for interface: TenGigE0/0/0/0

SFP EEPROM  port: 0
        Xcvr Type: SFP
        Xcvr Code: SFP-10G-SR
        Encoding: 64B66B
        Bit Rate: 10300 Mbps
        Link Reach 50u fiber: 80 meter
        Link Reach 62.5u fiber: 20 meter
        Vendor Name: CISCO-FINISAR
        Vendor OUI: 00.90.65
        Vendor Part Number: FTLX8571D3BCL-C2 (rev.: A   )
        Laser wavelength: 850 nm (fraction: 0.00 nm)
        Optional SFP Signal: Tx_Disable, Tx_Fault, LOS
        Vendor Serial Number: FNS17231KXG
        Date Code (yy/mm/dd): 13/06/06  lot code:
        Diagnostic Monitoring: DOM, Int. Cal.,
        Enhanced Options: Alarm/Warning Flags
 
MSA Data
0x0000: 03 04 07 10 00 00 00 00 : 00 00 00 06 67 00 00 00
0x0010: 08 02 00 1e 43 49 53 43 : 4f 2d 46 49 4e 49 53 41
0x0020: 52 20 20 20 00 00 90 65 : 46 54 4c 58 38 35 37 31
0x0030: 44 33 42 43 4c 2d 43 32 : 41 20 20 20 03 52 00 a5
0x0040: 00 1a 00 00 46 4e 53 31 : 37 32 33 31 4b 58 47 20
 0x0050: 20 20 20 20 31 33 30 36 : 30 36 20 20 68 80 03 e4
0x0060: 00 00 02 12 74 eb 9c 1e : 89 59 e6 a8 3c 20 cb 2a
0x0070: b0 0d ca 00 00 00 00 00 : 00 00 00 00 f5 ca 74 5e

        Thresholds:                    Alarm High         Warning High          Warning Low            Alarm Low
              Temperature:            +75.000 C             +70.000 C              +0.000 C              -5.000 C
                  Voltage:           3.630 Volt            3.465 Volt            3.135 Volt            2.970 Volt
                     Bias:         11.800 mAmps          10.800 mAmps           5.000 mAmps           4.000 mAmps
           Transmit Power:  1.47910 mW (1.69998 dBm)   0.74130 mW (-1.30006 dBm)   0.18620 mW (-7.30020 dBm)   0.07410 mW (-11.30182 dBm)
            Receive Power:  1.58490 mW (2.00002 dBm)   0.79430 mW (-1.00015 dBm)   0.10230 mW (-9.90124 dBm)   0.04070 mW (-13.90406 dBm)
        Temperature: 28.461
        Voltage: 3.244 Volt
        Tx Bias: 0.116 mAmps
        Tx Power:  0.02730 mW (-15.63837 dBm)
        Rx Power:  0.000 mW (<-40.00 dBm)
        Oper. Status/Control: Tx Disabled, LOS,
EEPROM Memory (A2 lower)
 0x0100: 4b 00 fb 00 46 00 00 00 : 8d cc 74 04 87 5a 7a 76
0x0110: 17 0c 07 d0 15 18 09 c4 : 39 c7 02 e5 1c f5 07 46
0x0120: 3d e9 01 97 1f 07 03 ff : 00 00 00 00 00 00 00 00
0x0130: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 00 00
0x0140: 00 00 00 00 3f 80 00 00 : 00 00 00 00 01 00 00 00
0x0150: 01 00 00 00 01 00 00 00 : 01 00 00 00 00 00 00 10
0x0160: 1c 76 7e b9 00 3a 01 11 : 00 00 00 00 00 00 82 00
0x0170: 05 40 00 00 05 40 00 00 : ff ff ff ff ff ff ff 01

        CLEI Code: COUIA8NCAA
        Part Number: 10-2415-03 (ver.: V03 )
        Temp/Alarm/Power Flags: COM, commercial 0C to 70C
        Minimum Temperature: 0
        Maximum Temperature: 70
        Calibration Constants:
        Product Id: SFP-10G-SR
EEPROM Memory (A2 upper)
0x0180: 43 4f 55 49 41 38 4e 43 : 41 41 31 30 2d 32 34 31
0x0190: 35 2d 30 33 56 30 33 20 : 01 00 46 00 00 00 00 c6
0x01a0: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 00 00
0x01b0: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 aa aa
 0x01c0: 53 46 50 2d 31 30 47 2d : 53 52 20 20 20 20 20 20
0x01d0: 20 20 20 20 32 33 00 00 : 00 00 00 00 00 00 00 35
0x01e0: 15 1a 20 24 2a 30 20 30 : 00 00 00 00 00 00 00 00
0x01f0: 00 00 00 00 00 1d 00 00 : ff ff ff ff 00 00 00 00



PHY data for interface: TenGigE0/0/0/1

SFP EEPROM  port: 1
        Xcvr Type: SFP
        Xcvr Code: SFP-10G-LR
        Encoding: 64B66B
        Bit Rate: 10300 Mbps
        Link Reach 9u fiber (Km): 10000 meter
        Link Reach 9u fiber (100m): 10000 meter
        Vendor Name: CISCO-SUMITOMO
        Vendor OUI: 00.00.5f
        Vendor Part Number: SPP5200LR-C6     (rev.: B   )
        Laser wavelength: 1310 nm (fraction: 0.00 nm)
        Optional SFP Signal: Tx_Disable, Tx_Fault, LOS
        Vendor Serial Number: SPC1719093J
        Date Code (yy/mm/dd): 13/05/11  lot code: 1C
        Diagnostic Monitoring: DOM, Int. Cal.,
        Enhanced Options: SW RX LOS Mon., SW TX Fault Mon, SW TX Disable, Alarm/Warning Flags

MSA Data
0x0000: 03 04 07 20 00 00 00 00 : 00 00 00 06 67 00 0a 64
0x0010: 00 00 00 00 43 49 53 43 : 4f 2d 53 55 4d 49 54 4f
0x0020: 4d 4f 20 20 00 00 00 5f : 53 50 50 35 32 30 30 4c
0x0030: 52 2d 43 36 20 20 20 20 : 42 20 20 20 05 1e 00 06
0x0040: 00 1a 00 00 53 50 43 31 : 37 31 39 30 39 33 4a 20
0x0050: 20 20 20 20 31 33 30 35 : 31 31 31 43 68 f0 03 52
0x0060: 00 00 0b 1c ba 98 43 64 : 6a 97 d8 6c ea 86 b2 df
0x0070: cc 46 fd 00 00 00 00 00 : 00 00 00 00 3e ac 79 a3

        Thresholds:                    Alarm High         Warning High          Warning Low            Alarm Low
              Temperature:            +75.000 C             +70.000 C              +0.000 C              -5.000 C
                  Voltage:           3.630 Volt            3.465 Volt            3.135 Volt            2.970 Volt
                     Bias:         90.000 mAmps          84.000 mAmps          24.000 mAmps          20.000 mAmps
           Transmit Power:  2.23870 mW (3.49996 dBm)   1.12200 mW (0.49993 dBm)   0.15140 mW (-8.19874 dBm)   0.06030 mW (-12.19683 dBm)
            Receive Power:  2.23870 mW (3.49996 dBm)   1.12200 mW (0.49993 dBm)   0.03630 mW (-14.40093 dBm)   0.01450 mW (-18.38632 dBm)
        Temperature: 25.629
        Voltage: 3.318 Volt
        Tx Bias: 0.000 mAmps
        Tx Power:  0.000 mW (<-40.00 dBm)
        Rx Power:  0.000 mW (<-40.00 dBm)
        Oper. Status/Control: Tx Disabled, LOS,
EEPROM Memory (A2 lower)
0x0100: 4b 00 fb 00 46 00 00 00 : 8d cc 74 04 87 5a 7a 76
0x0110: af c8 27 10 a4 10 2e e0 : 57 73 02 5b 2b d4 05 ea
0x0120: 57 73 00 91 2b d4 01 6b : 00 00 00 00 00 00 00 00
0x0130: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 00 00
0x0140: 00 00 00 00 3f 80 00 00 : 00 00 00 00 01 00 00 00
0x0150: 01 00 00 00 01 00 00 00 : 01 00 00 00 00 00 00 3c
0x0160: 19 a1 81 98 00 00 00 00 : 00 00 00 00 00 00 82 00
 0x0170: 00 40 00 00 00 40 00 00 : 00 00 00 00 00 00 00 01

        CLEI Code: COUIA75CAA
        Part Number: 10-2457-02 (ver.: V02 )
        Temp/Alarm/Power Flags: COM, commercial 0C to 70C
        Minimum Temperature: 0
        Maximum Temperature: 70
        Calibration Constants: LBC Scale, Temperature, Laser bias current, Output power,
        Product Id: SFP-10G-LR
EEPROM Memory (A2 upper)
0x0180: 43 4f 55 49 41 37 35 43 : 41 41 31 30 2d 32 34 35
0x0190: 37 2d 30 32 56 30 32 20 : 01 00 46 00 00 00 00 b0
0x01a0: 00 00 00 00 00 00 00 00 : 00 00 8c dd 94 00 ac a5
0x01b0: d6 cd 00 00 1e 00 59 2d : 12 88 0f 3e 00 00 aa aa
0x01c0: 53 46 50 2d 31 30 47 2d : 4c 52 20 20 20 20 20 20
0x01d0: 20 20 20 20 32 33 00 00 : 00 00 00 00 00 00 00 2e
0x01e0: 20 26 2b 30 33 36 2b 36 : 00 00 00 00 00 00 00 00
0x01f0: 00 00 00 00 00 6b 00 00 : ff ff ff ff 00 00 00 00



PHY data for interface: TenGigE0/0/0/2

SFP EEPROM  port: 2
        Xcvr Type: SFP
        Xcvr Code: DWDM-SFP10G-58.98
        Encoding: 64B66B
        Bit Rate: 11100 Mbps
        Link Reach 9u fiber (Km): 80000 meter
        Vendor Name: CISCO-FUJITSU
        Vendor OUI: 00.00.0e
        Vendor Part Number: FIM35060/201W23  (rev.: 0002)
        Laser wavelength: 1558 nm (fraction: 0.098 nm)
        Optional SFP Signal: Tx_Disable, Tx_Fault, LOS
        Vendor Serial Number: FLJ1736K039
        Date Code (yy/mm/dd): 13/09/03  lot code: 01
        Diagnostic Monitoring: DOM, Int. Cal.,
        Enhanced Options: SW RX LOS Mon., SW TX Fault Mon, SW TX Disable, Alarm/Warning Flags

MSA Data
0x0000: 03 04 07 00 00 00 00 00 : 00 00 00 06 6f 00 50 00
0x0010: 00 00 00 00 43 49 53 43 : 4f 2d 46 55 4a 49 54 53
0x0020: 55 20 20 20 00 00 00 0e : 46 49 4d 33 35 30 36 30
0x0030: 2f 32 30 31 57 32 33 20 : 30 30 30 32 06 16 62 c1
0x0040: 05 1a 00 00 46 4c 4a 31 : 37 33 36 4b 30 33 39 20
0x0050: 20 20 20 20 31 33 30 39 : 30 33 30 31 68 f0 04 40
0x0060: a3 00 15 3b 48 6e 9c da : f4 7b 3c 89 41 c2 1e d5
 0x0070: aa f3 88 00 00 00 00 00 : 00 00 00 00 49 75 e7 e7

        Thresholds:                    Alarm High         Warning High          Warning Low            Alarm Low
              Temperature:            +75.000 C             +70.000 C              +0.000 C              -5.000 C
                  Voltage:           3.630 Volt            3.465 Volt            3.135 Volt            2.970 Volt
                     Bias:        105.000 mAmps          98.000 mAmps          42.000 mAmps          35.000 mAmps
           Transmit Power:  3.98100 mW (5.99992 dBm)   1.99520 mW (2.99986 dBm)   0.79430 mW (-1.00015 dBm)   0.31620 mW (-5.00038 dBm)
            Receive Power:  0.50120 mW (-2.99989 dBm)   0.19950 mW (-7.00057 dBm)   0.00200 mW (-26.98970 dBm)   0.00080 mW (-30.96910 dBm)
        Temperature: 36.656
        Voltage: 3.250 Volt
        Tx Bias: 79.936 mAmps
        Tx Power:  1.38250 mW (1.40665 dBm)
        Rx Power:  0.01520 mW (-18.18156 dBm)
        Oper. Status/Control:
 EEPROM Memory (A2 lower)
0x0100: 4b 00 fb 00 46 00 00 00 : 8d cc 74 04 87 5a 7a 76
0x0110: cd 14 44 5c bf 68 52 08 : 9b 82 0c 5a 4d f0 1f 07
0x0120: 13 94 00 08 07 cb 00 14 : 00 00 00 00 00 00 00 00
0x0130: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 00 00
0x0140: 00 00 00 00 00 00 00 01 : 00 00 00 00 00 01 00 00
0x0150: 00 01 00 00 00 01 00 00 : 00 01 00 00 00 00 00 b0
0x0160: 24 a8 7e f8 9c 20 36 01 : 00 98 00 00 00 00 00 00
0x0170: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 00 02

        CLEI Code: IPU3AZ6CAA
        Part Number: 10-2750-01 (ver.: V01 )
        Temp/Alarm/Power Flags: COM, commercial 0C to 70C
        Minimum Temperature: 0
        Maximum Temperature: 70
        Calibration Constants: LBC Scale, Temperature, Laser bias current, Output power,
        Product Id: DWDM-SFP10G-58.98
EEPROM Memory (A2 upper)
 0x0180: 49 50 55 33 41 5a 36 43 : 41 41 31 30 2d 32 37 35
0x0190: 30 2d 30 31 56 30 31 20 : 01 00 46 00 00 00 00 bf
0x01a0: 00 00 00 00 00 00 00 00 : 00 00 63 aa 64 00 64 ca
0x01b0: 66 43 00 00 1c 02 9d 51 : 37 07 0f a1 00 00 aa aa
0x01c0: 44 57 44 4d 2d 53 46 50 : 31 30 47 2d 35 38 2e 39
0x01d0: 38 20 20 20 33 32 00 00 : 00 00 00 00 00 00 00 e8
0x01e0: 0b 0d 1a 21 27 34 1a 34 : 00 00 00 00 00 00 00 00
0x01f0: 00 00 00 00 00 fc 00 00 : ff ff ff ff 00 00 00 00



PHY data for interface: TenGigE0/0/0/3

SFP EEPROM  port: 3
        Xcvr Type: SFP
        Xcvr Code: SFP-10G-SR
        Encoding: 64B66B
        Bit Rate: 10300 Mbps
        Link Reach 50u fiber: 80 meter
        Link Reach 62.5u fiber: 20 meter
        Vendor Name: CISCO-JDSU
        Vendor OUI: 00.01.9c
        Vendor Part Number: PLRXPL-SC-S43-CS (rev.: 1   )
        Laser wavelength: 850 nm (fraction: 0.00 nm)
        Optional SFP Signal: Tx_Disable, Tx_Fault, LOS
        Vendor Serial Number: JUR1833GV1F
        Date Code (yy/mm/dd): 14/08/16  lot code:
        Diagnostic Monitoring: DOM, Int. Cal.,
        Enhanced Options: SW RX LOS Mon., SW TX Fault Mon, SW TX Disable, Alarm/Warning Flags

MSA Data
0x0000: 03 04 07 10 00 00 00 00 : 00 00 00 06 67 00 00 00
0x0010: 08 02 00 1e 43 49 53 43 : 4f 2d 4a 44 53 55 20 20
0x0020: 20 20 20 20 00 00 01 9c : 50 4c 52 58 50 4c 2d 53
0x0030: 43 2d 53 34 33 2d 43 53 : 31 20 20 20 03 52 00 19
0x0040: 00 1a 00 00 4a 55 52 31 : 38 33 33 47 56 31 46 20
0x0050: 20 20 20 20 31 34 30 38 : 31 36 20 20 68 f0 03 5d
0x0060: 00 00 08 93 24 b6 53 74 : 94 4c 09 f7 05 38 f0 78
0x0070: 12 90 2a 00 00 00 00 00 : 00 00 00 00 8a 25 00 f8

        Thresholds:                    Alarm High         Warning High          Warning Low            Alarm Low
              Temperature:            +75.000 C             +70.000 C              +0.000 C              -5.000 C
                  Voltage:           3.630 Volt            3.465 Volt            3.135 Volt            2.970 Volt
                     Bias:         10.000 mAmps           8.500 mAmps           3.000 mAmps           2.600 mAmps
           Transmit Power:  1.47910 mW (1.69998 dBm)   0.74130 mW (-1.30006 dBm)   0.18620 mW (-7.30020 dBm)   0.07410 mW (-11.30182 dBm)
            Receive Power:  1.58490 mW (2.00002 dBm)   0.79430 mW (-1.00015 dBm)   0.10230 mW (-9.90124 dBm)   0.04070 mW (-13.90406 dBm)
        Temperature: 32.988
        Voltage: 3.291 Volt
        Tx Bias: 7.250 mAmps
        Tx Power:  0.56550 mW (-2.47567 dBm)
        Rx Power:  0.42270 mW (-3.73968 dBm)
        Oper. Status/Control:
 EEPROM Memory (A2 lower)
0x0100: 4b 00 fb 00 46 00 00 00 : 8d cc 74 04 87 5a 7a 76
0x0110: 13 88 05 14 10 9a 05 dc : 39 c7 02 e5 1c f5 07 46
0x0120: 3d e9 01 97 1f 07 03 ff : 00 00 00 00 00 00 00 00
0x0130: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 00 00
0x0140: 00 00 00 00 3f 80 00 00 : 00 00 00 00 01 00 00 00
0x0150: 01 00 00 00 01 00 00 00 : 01 00 00 00 00 00 00 5b
0x0160: 20 fd 80 8e 0e 29 16 17 : 10 83 00 00 00 00 00 00
0x0170: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 00 01

        CLEI Code: COUIA8NCAA
        Part Number: 10-2415-03 (ver.: V03 )
        Temp/Alarm/Power Flags: COM, commercial 0C to 70C
        Minimum Temperature: 0
        Maximum Temperature: 70
        Calibration Constants: LBC Scale, Temperature, Laser bias current, Output power,
        Product Id: SFP-10G-SR
EEPROM Memory (A2 upper)
0x0180: 43 4f 55 49 41 38 4e 43 : 41 41 31 30 2d 32 34 31
0x0190: 35 2d 30 33 56 30 33 20 : 01 00 46 00 00 00 00 c6
0x01a0: 00 00 00 00 00 00 00 00 : 00 00 61 06 64 00 6d d7
0x01b0: 7c 2b 00 00 16 00 0c 6c : 16 45 0f ae 00 00 aa aa
 0x01c0: 53 46 50 2d 31 30 47 2d : 53 52 20 20 20 20 20 20
0x01d0: 20 20 20 20 34 31 00 00 : 00 00 00 00 00 00 00 35
0x01e0: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 00 00
0x01f0: 00 00 00 00 00 00 00 00 : ff ff ff ff 00 00 00 00



PHY data for interface: TenGigE0/0/0/4

SFP EEPROM  port: 4
        Xcvr Type: SFP
        Xcvr Code: SFP-10G-SR
        Encoding: 64B66B
        Bit Rate: 10300 Mbps
        Link Reach 50u fiber: 80 meter
        Link Reach 62.5u fiber: 20 meter
        Vendor Name: CISCO-FINISAR
        Vendor OUI: 00.90.65
        Vendor Part Number: FTLX8571D3BCL-C2 (rev.: A   )
        Laser wavelength: 850 nm (fraction: 0.00 nm)
        Optional SFP Signal: Tx_Disable, Tx_Fault, LOS
        Vendor Serial Number: FNS17231KZU
        Date Code (yy/mm/dd): 13/06/06  lot code:
        Diagnostic Monitoring: DOM, Int. Cal.,
        Enhanced Options: Alarm/Warning Flags
 
MSA Data
0x0000: 03 04 07 10 00 00 00 00 : 00 00 00 06 67 00 00 00
0x0010: 08 02 00 1e 43 49 53 43 : 4f 2d 46 49 4e 49 53 41
0x0020: 52 20 20 20 00 00 90 65 : 46 54 4c 58 38 35 37 31
0x0030: 44 33 42 43 4c 2d 43 32 : 41 20 20 20 03 52 00 a5
0x0040: 00 1a 00 00 46 4e 53 31 : 37 32 33 31 4b 5a 55 20
 0x0050: 20 20 20 20 31 33 30 36 : 30 36 20 20 68 80 03 f4
0x0060: 00 00 02 61 e7 86 6e be : 16 35 ef 18 50 08 c7 78
0x0070: 28 bc 3c 00 00 00 00 00 : 00 00 00 00 e5 04 00 95

        Thresholds:                    Alarm High         Warning High          Warning Low            Alarm Low
              Temperature:            +75.000 C             +70.000 C              +0.000 C              -5.000 C
                  Voltage:           3.630 Volt            3.465 Volt            3.135 Volt            2.970 Volt
                     Bias:         11.800 mAmps          10.800 mAmps           5.000 mAmps           4.000 mAmps
           Transmit Power:  1.47910 mW (1.69998 dBm)   0.74130 mW (-1.30006 dBm)   0.18620 mW (-7.30020 dBm)   0.07410 mW (-11.30182 dBm)
            Receive Power:  1.58490 mW (2.00002 dBm)   0.79430 mW (-1.00015 dBm)   0.10230 mW (-9.90124 dBm)   0.04070 mW (-13.90406 dBm)
        Temperature: 32.152
        Voltage: 3.264 Volt
        Tx Bias: 7.904 mAmps
        Tx Power:  0.59180 mW (-2.27825 dBm)
        Rx Power:  0.45310 mW (-3.43806 dBm)
        Oper. Status/Control:
EEPROM Memory (A2 lower)
0x0100: 4b 00 fb 00 46 00 00 00 : 8d cc 74 04 87 5a 7a 76
0x0110: 17 0c 07 d0 15 18 09 c4 : 39 c7 02 e5 1c f5 07 46
0x0120: 3d e9 01 97 1f 07 03 ff : 00 00 00 00 00 00 00 00
0x0130: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 00 00
0x0140: 00 00 00 00 3f 80 00 00 : 00 00 00 00 01 00 00 00
0x0150: 01 00 00 00 01 00 00 00 : 01 00 00 00 00 00 00 10
0x0160: 20 27 7f 83 0f 70 17 1e : 11 b3 00 00 00 00 00 00
0x0170: 00 00 00 00 00 00 00 00 : ff ff ff ff ff ff ff 01

        CLEI Code: COUIA8NCAA
        Part Number: 10-2415-03 (ver.: V03 )
        Temp/Alarm/Power Flags: COM, commercial 0C to 70C
        Minimum Temperature: 0
        Maximum Temperature: 70
        Calibration Constants:
        Product Id: SFP-10G-SR
EEPROM Memory (A2 upper)
0x0180: 43 4f 55 49 41 38 4e 43 : 41 41 31 30 2d 32 34 31
0x0190: 35 2d 30 33 56 30 33 20 : 01 00 46 00 00 00 00 c6
0x01a0: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 00 00
 0x01b0: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 aa aa
0x01c0: 53 46 50 2d 31 30 47 2d : 53 52 20 20 20 20 20 20
0x01d0: 20 20 20 20 32 33 00 00 : 00 00 00 00 00 00 00 35
0x01e0: 15 1a 20 24 2a 30 20 30 : 00 00 00 00 00 00 00 00
0x01f0: 00 00 00 00 00 1d 00 00 : ff ff ff ff 00 00 00 00



PHY data for interface: TenGigE0/0/0/5

SFP EEPROM  port: 5
        Xcvr Type: SFP
        Xcvr Code: SFP-10G-SR
        Encoding: 64B66B
        Bit Rate: 10300 Mbps
        Link Reach 50u fiber: 80 meter
        Link Reach 62.5u fiber: 20 meter
        Vendor Name: CISCO-FINISAR
        Vendor OUI: 00.90.65
        Vendor Part Number: FTLX8571D3BCL-C2 (rev.: A   )
        Laser wavelength: 850 nm (fraction: 0.00 nm)
        Optional SFP Signal: Tx_Disable, Tx_Fault, LOS
        Vendor Serial Number: FNS17231KZ7
        Date Code (yy/mm/dd): 13/06/06  lot code:
        Diagnostic Monitoring: DOM, Int. Cal.,
        Enhanced Options: Alarm/Warning Flags

MSA Data
0x0000: 03 04 07 10 00 00 00 00 : 00 00 00 06 67 00 00 00
0x0010: 08 02 00 1e 43 49 53 43 : 4f 2d 46 49 4e 49 53 41
0x0020: 52 20 20 20 00 00 90 65 : 46 54 4c 58 38 35 37 31
 0x0030: 44 33 42 43 4c 2d 43 32 : 41 20 20 20 03 52 00 a5
0x0040: 00 1a 00 00 46 4e 53 31 : 37 32 33 31 4b 5a 37 20
0x0050: 20 20 20 20 31 33 30 36 : 30 36 20 20 68 80 03 d6
0x0060: 00 00 02 6d 9a 90 34 05 : 5a 2b de b4 22 a8 95 6b
0x0070: 4c b4 d5 00 00 00 00 00 : 00 00 00 00 b6 4c a5 80

        Thresholds:                    Alarm High         Warning High          Warning Low            Alarm Low
              Temperature:            +75.000 C             +70.000 C              +0.000 C              -5.000 C
                  Voltage:           3.630 Volt            3.465 Volt            3.135 Volt            2.970 Volt
                     Bias:         11.800 mAmps          10.800 mAmps           5.000 mAmps           4.000 mAmps
           Transmit Power:  1.47910 mW (1.69998 dBm)   0.74130 mW (-1.30006 dBm)   0.18620 mW (-7.30020 dBm)   0.07410 mW (-11.30182 dBm)
            Receive Power:  1.58490 mW (2.00002 dBm)   0.79430 mW (-1.00015 dBm)   0.10230 mW (-9.90124 dBm)   0.04070 mW (-13.90406 dBm)
        Temperature: 30.563
        Voltage: 3.258 Volt
        Tx Bias: 7.876 mAmps
        Tx Power:  0.64740 mW (-1.88827 dBm)
        Rx Power:  0.56550 mW (-2.47567 dBm)
        Oper. Status/Control:
 EEPROM Memory (A2 lower)
0x0100: 4b 00 fb 00 46 00 00 00 : 8d cc 74 04 87 5a 7a 76
0x0110: 17 0c 07 d0 15 18 09 c4 : 39 c7 02 e5 1c f5 07 46
0x0120: 3d e9 01 97 1f 07 03 ff : 00 00 00 00 00 00 00 00
0x0130: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 00 00
0x0140: 00 00 00 00 3f 80 00 00 : 00 00 00 00 01 00 00 00
0x0150: 01 00 00 00 01 00 00 00 : 01 00 00 00 00 00 00 10
0x0160: 1e 90 7f 45 0f 62 19 4a : 16 17 00 00 00 00 00 00
0x0170: 00 00 00 00 00 00 00 00 : ff ff ff ff ff ff ff 01

        CLEI Code: COUIA8NCAA
        Part Number: 10-2415-03 (ver.: V03 )
        Temp/Alarm/Power Flags: COM, commercial 0C to 70C
        Minimum Temperature: 0
        Maximum Temperature: 70
        Calibration Constants:
        Product Id: SFP-10G-SR
EEPROM Memory (A2 upper)
0x0180: 43 4f 55 49 41 38 4e 43 : 41 41 31 30 2d 32 34 31
0x0190: 35 2d 30 33 56 30 33 20 : 01 00 46 00 00 00 00 c6
0x01a0: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 00 00
0x01b0: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 aa aa
0x01c0: 53 46 50 2d 31 30 47 2d : 53 52 20 20 20 20 20 20
 0x01d0: 20 20 20 20 32 33 00 00 : 00 00 00 00 00 00 00 35
0x01e0: 15 1a 20 24 2a 30 20 30 : 00 00 00 00 00 00 00 00
0x01f0: 00 00 00 00 00 1d 00 00 : ff ff ff ff 00 00 00 00



PHY data for interface: TenGigE0/0/0/6

SFP EEPROM  port: 6
        Xcvr Type: SFP
        Xcvr Code: SFP-10G-SR
        Encoding: 64B66B
        Bit Rate: 10300 Mbps
        Link Reach 50u fiber: 80 meter
        Link Reach 62.5u fiber: 20 meter
        Vendor Name: CISCO-FINISAR
        Vendor OUI: 00.90.65
        Vendor Part Number: FTLX8571D3BCL-C2 (rev.: A   )
        Laser wavelength: 850 nm (fraction: 0.00 nm)
        Optional SFP Signal: Tx_Disable, Tx_Fault, LOS
        Vendor Serial Number: FNS17231KYN
        Date Code (yy/mm/dd): 13/06/06  lot code:
        Diagnostic Monitoring: DOM, Int. Cal.,
        Enhanced Options: Alarm/Warning Flags
 
MSA Data
0x0000: 03 04 07 10 00 00 00 00 : 00 00 00 06 67 00 00 00
0x0010: 08 02 00 1e 43 49 53 43 : 4f 2d 46 49 4e 49 53 41
0x0020: 52 20 20 20 00 00 90 65 : 46 54 4c 58 38 35 37 31
0x0030: 44 33 42 43 4c 2d 43 32 : 41 20 20 20 03 52 00 a5
0x0040: 00 1a 00 00 46 4e 53 31 : 37 32 33 31 4b 59 4e 20
 0x0050: 20 20 20 20 31 33 30 36 : 30 36 20 20 68 80 03 ec
0x0060: 00 00 02 b1 f4 73 e5 c3 : 5c aa e2 5c 9c fe 1c 95
0x0070: 91 98 47 00 00 00 00 00 : 00 00 00 00 ab 24 53 3c

        Thresholds:                    Alarm High         Warning High          Warning Low            Alarm Low
              Temperature:            +75.000 C             +70.000 C              +0.000 C              -5.000 C
                  Voltage:           3.630 Volt            3.465 Volt            3.135 Volt            2.970 Volt
                     Bias:         11.800 mAmps          10.800 mAmps           5.000 mAmps           4.000 mAmps
           Transmit Power:  1.47910 mW (1.69998 dBm)   0.74130 mW (-1.30006 dBm)   0.18620 mW (-7.30020 dBm)   0.07410 mW (-11.30182 dBm)
            Receive Power:  1.58490 mW (2.00002 dBm)   0.79430 mW (-1.00015 dBm)   0.10230 mW (-9.90124 dBm)   0.04070 mW (-13.90406 dBm)
        Temperature: 34.293
        Voltage: 3.240 Volt
        Tx Bias: 7.846 mAmps
        Tx Power:  0.61560 mW (-2.10701 dBm)
        Rx Power:  0.62050 mW (-2.07258 dBm)
        Oper. Status/Control:
EEPROM Memory (A2 lower)
0x0100: 4b 00 fb 00 46 00 00 00 : 8d cc 74 04 87 5a 7a 76
0x0110: 17 0c 07 d0 15 18 09 c4 : 39 c7 02 e5 1c f5 07 46
0x0120: 3d e9 01 97 1f 07 03 ff : 00 00 00 00 00 00 00 00
0x0130: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 00 00
0x0140: 00 00 00 00 3f 80 00 00 : 00 00 00 00 01 00 00 00
0x0150: 01 00 00 00 01 00 00 00 : 01 00 00 00 00 00 00 10
0x0160: 22 4b 7e 8e 0f 53 18 0c : 18 3d 00 00 00 00 00 00
0x0170: 00 00 00 00 00 00 00 00 : ff ff ff ff ff ff ff 01

        CLEI Code: COUIA8NCAA
        Part Number: 10-2415-03 (ver.: V03 )
        Temp/Alarm/Power Flags: COM, commercial 0C to 70C
        Minimum Temperature: 0
        Maximum Temperature: 70
        Calibration Constants:
        Product Id: SFP-10G-SR
EEPROM Memory (A2 upper)
0x0180: 43 4f 55 49 41 38 4e 43 : 41 41 31 30 2d 32 34 31
0x0190: 35 2d 30 33 56 30 33 20 : 01 00 46 00 00 00 00 c6
0x01a0: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 00 00
 0x01b0: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 aa aa
0x01c0: 53 46 50 2d 31 30 47 2d : 53 52 20 20 20 20 20 20
0x01d0: 20 20 20 20 32 33 00 00 : 00 00 00 00 00 00 00 35
0x01e0: 15 1a 20 24 2a 30 20 30 : 00 00 00 00 00 00 00 00
0x01f0: 00 00 00 00 00 1d 00 00 : ff ff ff ff 00 00 00 00



PHY data for interface: TenGigE0/0/0/7

SFP EEPROM  port: 7
        Xcvr Type: SFP
        Xcvr Code: SFP-10G-SR
        Encoding: 64B66B
        Bit Rate: 10300 Mbps
        Link Reach 50u fiber: 80 meter
        Link Reach 62.5u fiber: 20 meter
        Vendor Name: CISCO-FINISAR
        Vendor OUI: 00.90.65
        Vendor Part Number: FTLX8571D3BCL-C2 (rev.: A   )
        Laser wavelength: 850 nm (fraction: 0.00 nm)
        Optional SFP Signal: Tx_Disable, Tx_Fault, LOS
        Vendor Serial Number: FNS17231KYF
        Date Code (yy/mm/dd): 13/06/06  lot code:
        Diagnostic Monitoring: DOM, Int. Cal.,
        Enhanced Options: Alarm/Warning Flags

MSA Data
0x0000: 03 04 07 10 00 00 00 00 : 00 00 00 06 67 00 00 00
0x0010: 08 02 00 1e 43 49 53 43 : 4f 2d 46 49 4e 49 53 41
0x0020: 52 20 20 20 00 00 90 65 : 46 54 4c 58 38 35 37 31
 0x0030: 44 33 42 43 4c 2d 43 32 : 41 20 20 20 03 52 00 a5
0x0040: 00 1a 00 00 46 4e 53 31 : 37 32 33 31 4b 59 46 20
0x0050: 20 20 20 20 31 33 30 36 : 30 36 20 20 68 80 03 e4
0x0060: 00 00 02 92 fe 63 74 2e : 97 52 42 36 a9 62 00 68
0x0070: 2e 2a 5f 00 00 00 00 00 : 00 00 00 00 8b 7d 0c 6e

        Thresholds:                    Alarm High         Warning High          Warning Low            Alarm Low
              Temperature:            +75.000 C             +70.000 C              +0.000 C              -5.000 C
                  Voltage:           3.630 Volt            3.465 Volt            3.135 Volt            2.970 Volt
                     Bias:         11.800 mAmps          10.800 mAmps           5.000 mAmps           4.000 mAmps
           Transmit Power:  1.47910 mW (1.69998 dBm)   0.74130 mW (-1.30006 dBm)   0.18620 mW (-7.30020 dBm)   0.07410 mW (-11.30182 dBm)
            Receive Power:  1.58490 mW (2.00002 dBm)   0.79430 mW (-1.00015 dBm)   0.10230 mW (-9.90124 dBm)   0.04070 mW (-13.90406 dBm)
        Temperature: 34.387
        Voltage: 3.278 Volt
        Tx Bias: 0.152 mAmps
        Tx Power:  0.05760 mW (-12.39578 dBm)
        Rx Power:  0.000 mW (<-40.00 dBm)
        Oper. Status/Control: Tx Disabled, LOS,
EEPROM Memory (A2 lower)
0x0100: 4b 00 fb 00 46 00 00 00 : 8d cc 74 04 87 5a 7a 76
0x0110: 17 0c 07 d0 15 18 09 c4 : 39 c7 02 e5 1c f5 07 46
0x0120: 3d e9 01 97 1f 07 03 ff : 00 00 00 00 00 00 00 00
0x0130: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 00 00
0x0140: 00 00 00 00 3f 80 00 00 : 00 00 00 00 01 00 00 00
0x0150: 01 00 00 00 01 00 00 00 : 01 00 00 00 00 00 00 10
0x0160: 22 63 80 09 00 4c 02 40 : 00 00 00 00 00 00 82 00
 0x0170: 05 40 00 00 05 40 00 00 : ff ff ff ff ff ff ff 01

        CLEI Code: COUIA8NCAA
        Part Number: 10-2415-03 (ver.: V03 )
        Temp/Alarm/Power Flags: COM, commercial 0C to 70C
        Minimum Temperature: 0
        Maximum Temperature: 70
        Calibration Constants:
        Product Id: SFP-10G-SR
 EEPROM Memory (A2 upper)
0x0180: 43 4f 55 49 41 38 4e 43 : 41 41 31 30 2d 32 34 31
0x0190: 35 2d 30 33 56 30 33 20 : 01 00 46 00 00 00 00 c6
0x01a0: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 00 00
0x01b0: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 aa aa
0x01c0: 53 46 50 2d 31 30 47 2d : 53 52 20 20 20 20 20 20
0x01d0: 20 20 20 20 32 33 00 00 : 00 00 00 00 00 00 00 35
0x01e0: 15 1a 20 24 2a 30 20 30 : 00 00 00 00 00 00 00 00
0x01f0: 00 00 00 00 00 1d 00 00 : ff ff ff ff 00 00 00 00



PHY data for interface: TenGigE0/0/0/8
 
SFP EEPROM  port: 8
        Xcvr Type: SFP
        Xcvr Code: SFP-10G-SR
        Encoding: 64B66B
        Bit Rate: 10300 Mbps
        Link Reach 50u fiber: 80 meter
        Link Reach 62.5u fiber: 20 meter
        Vendor Name: CISCO-FINISAR
        Vendor OUI: 00.90.65
        Vendor Part Number: FTLX8571D3BCL-C2 (rev.: A   )
        Laser wavelength: 850 nm (fraction: 0.00 nm)
        Optional SFP Signal: Tx_Disable, Tx_Fault, LOS
        Vendor Serial Number: FNS17231KZG
        Date Code (yy/mm/dd): 13/06/06  lot code:
        Diagnostic Monitoring: DOM, Int. Cal.,
        Enhanced Options: Alarm/Warning Flags

MSA Data
0x0000: 03 04 07 10 00 00 00 00 : 00 00 00 06 67 00 00 00
 0x0010: 08 02 00 1e 43 49 53 43 : 4f 2d 46 49 4e 49 53 41
0x0020: 52 20 20 20 00 00 90 65 : 46 54 4c 58 38 35 37 31
0x0030: 44 33 42 43 4c 2d 43 32 : 41 20 20 20 03 52 00 a5
0x0040: 00 1a 00 00 46 4e 53 31 : 37 32 33 31 4b 5a 47 20
0x0050: 20 20 20 20 31 33 30 36 : 30 36 20 20 68 80 03 e6
0x0060: 00 00 02 3e c6 30 bb 72 : 52 c4 39 8f 04 21 07 b0
0x0070: cc 72 75 00 00 00 00 00 : 00 00 00 00 60 af 93 d2

        Thresholds:                    Alarm High         Warning High          Warning Low            Alarm Low
              Temperature:            +75.000 C             +70.000 C              +0.000 C              -5.000 C
                  Voltage:           3.630 Volt            3.465 Volt            3.135 Volt            2.970 Volt
                     Bias:         11.800 mAmps          10.800 mAmps           5.000 mAmps           4.000 mAmps
           Transmit Power:  1.47910 mW (1.69998 dBm)   0.74130 mW (-1.30006 dBm)   0.18620 mW (-7.30020 dBm)   0.07410 mW (-11.30182 dBm)
            Receive Power:  1.58490 mW (2.00002 dBm)   0.79430 mW (-1.00015 dBm)   0.10230 mW (-9.90124 dBm)   0.04070 mW (-13.90406 dBm)
        Temperature: 33.723
        Voltage: 3.277 Volt
        Tx Bias: 0.000 mAmps
        Tx Power:  0.00530 mW (-22.75724 dBm)
        Rx Power:  0.000 mW (<-40.00 dBm)
        Oper. Status/Control: Tx Disabled, LOS,
 EEPROM Memory (A2 lower)
0x0100: 4b 00 fb 00 46 00 00 00 : 8d cc 74 04 87 5a 7a 76
0x0110: 17 0c 07 d0 15 18 09 c4 : 39 c7 02 e5 1c f5 07 46
0x0120: 3d e9 01 97 1f 07 03 ff : 00 00 00 00 00 00 00 00
0x0130: 00 00 00 00 00 00 00 00 : 00 00 00 00 00 00 00 00
0x0140: 00 00 00 00 3f 80 00 00 : 00 00 00 00 01 00 00 00
0x0150: 01 00 00 00 01 00 00 00 : 01 00 00 00 00 00 00 10
0x0160: 21 b9 80 02 00 00 00 35 : 00 00 00 00 00 00 82 00
0x0170: 05 40 00 00 05 40 00 00 : ff ff ff ff ff ff ff 01

```

**Help:** execute the command "show controllers all phy"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show ospf vrf all interface brief

**Output:**
```

Wed Jul 27 17:18:34.807 CST

* Indicates MADJ interface, (P) Indicates fast detect hold down state

Interfaces for OSPF 1, VRF red

Interface          PID   Area            IP Address/Mask    Cost  State Nbrs F/C
BE1.10             1     0               192.0.2.1/30       1     DR    1/1
Te0/0/0/10.10      1     0               192.0.2.1/30       1     BDR   1/1


Interfaces for OSPF 1, VRF green

BE1.20             1     0               192.0.2.1/30       1000  P2P   0/0
Gi300/0/0/0.10     1     0               192.0.2.1/30       1     DR    0/0


Interfaces for OSPF 1, VRF blue

BE1.30             1     0               192.0.2.1/30       1     DR    1/1
Gi300/0/0/0        1     0               192.0.2.1/30       1     DR    0/0

```

**Help:** execute the command "show ospf vrf all interface brief"

**Prompt:**
- cisco_xr>
- cisco_xr#

### admin show controller fabric health

**Output:**
```
Sat Feb 24 18:07:38.753 UTC

Fabric System Health
---------------------
 Flags: T - Total,      U - Up,         A - Admin Down 
       L - LCC,        M - Mcast Down, Y - Yes        
       F - FCC,        D - Down,       N - No or Not Ok
       V - Valid,     

Collaborator Process State:
------------------------------
    FSDB Aggregator: OK
    +-----------+--+
    |Rack id    | 0|
    +-----------+--+
    |FSDB status|Ok|
    +-----------+--+

    +------------+-----+-----+-----+-----+-----+-----+
    |FC Location |0/FC0|0/FC1|0/FC2|0/FC3|0/FC4|0/FC5|
    +------------+-----+-----+-----+-----+-----+-----+
    |SFE status  |  Ok |  Ok |  Ok |  Ok |  Ok |  Ok |
    +------------+-----+-----+-----+-----+-----+-----+
 
Router Health:
-----------------

    Rack    Planes  SFE Asics      Fia Asics     
    T/L/F   U/M/D/A T/U/D          T/U/D         
    ------------------------------------------------------
    1/1/0   5/0/1/0 36/30/6        36/36/0        

    Plane Admin Plane    Racks    Data      
    id    state state    in issue drop/error
    -----------------------------------------------------------
    0     UP    UP       0        No        
    1     UP    UP       0        No        
    2     UP    DN       1        No        
    3     UP    UP       0        No        
    4     UP    UP       0        No        
    5     UP    UP       0        No        
    -----------------------------------------------------------
 
Rack Health:
-------------
    Rack:  0, Type: LCC

    SFE Asics  FIA Asics   Planes   Valid  
    T/U/D      T/U/D       U/M/D    fab ids
    ------------------------------------------------
    36/30/6    36/36/0     5/0/1      72

    Plane Plane    SFE Asics    Fab ids  
    id    state    T/U/D        Reachable
    --------------------------------------
    0     UP       6/6/0        72    
    1     UP       6/6/0        72    
    2     DN       6/0/6        0     
    3     UP       6/6/0        72    
    4     UP       6/6/0        72    
    5     UP       6/6/0        72    
    --------------------------------------

```

**Help:** execute the command "admin show controller fabric health"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show lpts pifib hardware police location

**Output:**
```
-------------------------------------------------------------
                Node 0/3/CPU0:
-------------------------------------------------------------
 Burst = 100ms for all flow types
-------------------------------------------------------------
FlowType               Policer Type    Cur. Rate  Def. Rate  Accepted             Dropped              TOS Value
---------------------- ------- ------- ---------- ---------- -------------------- -------------------- ----------
unconfigured-default   100     Static  2500       2500       0                    0                    01234567
L2TPv2-fragment        185     Static  10000      10000      0                    0                    01234567
Fragment               101     Static  2500       2500       0                    0                    01234567
OSPF-mc-known          102     Static  2000       2000       387624               0                    01234567
OSPF-mc-default        103     Static  1500       1500       0                    0                    01234567
OSPF-uc-known          104     Static  2000       2000       20                   0                    01234567
OSPF-uc-default        105     Static  1000       1000       0                    0                    01234567
ISIS-known             143     Static  2000       2000       0                    0                    01234567
ISIS-default           144     Static  1500       1500       0                    0                    01234567
BFD-known              150     Static  9600       9600       0                    0                    01234567
BFD-default            160     Static  45340      9600       0                    0                    01234567
BFD-MP-known           178     Static  11520      11520      0                    0                    01234567
BFD-MP-0               179     Static  128        128        0                    0                    01234567
BFD-BLB-known          183     Static  11520      11520      0                    0                    01234567
BFD-BLB-0              184     Static  128        128        0                    0                    01234567
BFD-SP-0               182     Static  512        512        0                    0                    01234567
BGP-known              106     Static  2500       2500       51911                0                    01234567
BGP-cfg-peer           107     Static  2000       2000       0                    0                    01234567
BGP-default            108     Static  1500       1500       7                    0                    01234567
PIM-mcast-default      109     Static  2000       2000       0                    0                    01234567
PIM-mcast-known        176     Static  2000       2000       0                    0                    01234567
PIM-ucast              110     Static  1500       1500       0                    0                    01234567
IGMP                   111     Static  3000       3000       0                    0                    01234567
ICMP-local             112     Static  1500       1500       19                   0                    01234567
ICMP-app               152     Static  1500       1500       0                    0                    01234567
ICMP-control           140     Static  1000       1000       0                    0                    01234567
ICMP-default           153     Static  1500       1500       35                   0                    01234567
ICMP-app-default       152     Static  1500       1500       0                    0                    01234567
LDP-TCP-known          113     Static  2500       2500       127939               0                    01234567
LDP-TCP-cfg-peer       114     Static  2000       2000       0                    0                    01234567
LDP-TCP-default        115     Static  1500       1500       0                    0                    01234567
LDP-UDP                116     Static  2000       2000       726952               0                    01234567
All-routers            117     Static  1000       1000       0                    0                    01234567
LMP-TCP-known          168     Static  2500       2500       0                    0                    01234567
LMP-TCP-cfg-peer       169     Static  2000       2000       0                    0                    01234567
LMP-TCP-default        170     Static  1500       1500       0                    0                    01234567
LMP-UDP                171     Static  2000       2000       0                    0                    01234567
RSVP-UDP               118     Static  2000       2000       0                    0                    01234567
RSVP-default           154     Static  500        500        0                    0                    01234567
RSVP-known             177     Static  7000       7000       0                    0                    01234567
IKE                    119     Static  100        100        0                    0                    01234567
IPSEC-known            120     Static  400        400        0                    0                    01234567
IPSEC-default          121     Static  100        100        0                    0                    01234567
MSDP-known             122     Static  300        300        0                    0                    01234567
MSDP-cfg-peer          123     Static  200        200        0                    0                    01234567
MSDP-default           124     Static  100        100        0                    0                    01234567
SNMP                   125     Static  300        300        0                    0                    01234567
SSH-known              127     Static  300        300        0                    0                    01234567
SSH-default            128     Static  200        200        0                    0                    01234567
HTTP-known             129     Static  400        400        0                    0                    01234567
HTTP-default           130     Static  200        200        0                    0                    01234567
SHTTP-known            161     Static  400        400        0                    0                    01234567
IFIB_FT_SHTTP_DEFAULT  162     Static  200        200        0                    0                    01234567
TELNET-known           131     Static  200        200        0                    0                    01234567
TELNET-default         132     Static  200        200        0                    0                    01234567
CSS-known              133     Static  200        200        0                    0                    01234567
CSS-default            134     Static  200        200        0                    0                    01234567
RSH-known              135     Static  200        200        0                    0                    01234567
RSH-default            136     Static  200        200        0                    0                    01234567
UDP-known              137     Static  2500       2500       0                    0                    01234567
UDP-listen             138     Static  2500       2500       0                    0                    01234567
UDP-cfg-peer           155     Static  2500       2500       0                    0                    01234567
UDP-default            163     Static  3500       3500       0                    0                    01234567
TCP-known              156     Static  2500       2500       0                    0                    01234567
TCP-listen             157     Static  2500       2500       0                    0                    01234567
TCP-cfg-peer           158     Static  2000       2000       0                    0                    01234567
TCP-default            164     Static  2000       2000       573                  0                    01234567
Mcast-known            159     Static  2500       2500       0                    0                    01234567
Mcast-default          165     Static  2000       2000       0                    0                    01234567
Raw-listen             166     Static  2500       2500       0                    0                    01234567
Raw-default            167     Static  2500       2500       0                    0                    01234567
Ip-Sla                 139     Static  1000       1000       0                    0                    01234567
EIGRP                  145     Static  1500       1500       0                    0                    01234567
RIP                    146     Static  1500       1500       0                    0                    01234567
L2TPv3                 141     Static  400        400        0                    0                    01234567
PCEP                   142     Static  200        200        0                    0                    01234567
GRE                    147     Static  10000      10000      0                    0                    01234567
VRRP                   148     Static  1000       1000       0                    0                    01234567
HSRP                   149     Static  400        400        0                    0                    01234567
MPLS-oam               151     Static  250        250        0                    0                    01234567
L2TPv2-default         172     Static  2000       2000       0                    0                    01234567
L2TPv2-known           181     Static  2500       2500       0                    0                    01234567
DNS                    173     Static  2000       2000       0                    0                    01234567
RADIUS                 174     Static  2000       2000       0                    0                    01234567
TACACS                 175     Static  2000       2000       0                    0                    01234567
NTP-default            126     Static  200        200        0                    0                    01234567
NTP-known              180     Static  200        200        0                    0                    01234567
AMT                    186     Static  4000       4000       0                    0                    01234567
MIPv6                  188     Static  0          0          0                    0                    01234567
SDAC-TCP               187     Static  5000       5000       0                    0                    01234567
ONEPK                  189     Static  0          0          0                    0                    01234567

------------------------
statistics:
 Packets accepted by deleted entries: 7
Packets dropped by deleted entries: 0
Run out of statistics counter errors: 0
Statistics last cleared: Sat Aug 25 18:56:24 2700

```

**Help:** execute the command "show lpts pifib hardware police location"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show ip bgp summary

**Output:**
```
Mon Dec 18 11:13:26.959 UTC
BGP router identifier 30.67.35.78, local AS number 64200
BGP generic scan interval 60 secs
Non-stop routing is enabled
 BGP table state: Active
Table ID: 0xe0000000   RD version: 94623
BGP main routing table version 94623
BGP NSR Initial initsync version 2 (Reached)
 BGP NSR/ISSU Sync-Group versions 0/0
BGP scan interval 60 secs

BGP is operating in STANDALONE mode.


Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
Speaker           94623      94623      94623      94623       94623           0

Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
10.10.17.161      0 64924   36190   64731        0    0    0 00:00:00 Idle
10.10.128.240     0 64727   68750   70941        0    0    0    2d14h Active
10.10.132.240     0 64727   74112   76220    94623    0    0     7w2d         82
10.10.140.240     0 64727   72363   74575    94623    0    0    4d10h         82
```

**Help:** execute the command "show ip bgp summary"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show ospf neighbor

**Output:**
```
Mon Jan  2 16:12:20.544 UTC

* Indicates MADJ interface
# Indicates Neighbor awaiting BFD session up

Neighbors for OSPF 1

Neighbor ID     Pri   State           Dead Time   Address         Interface
1.1.1.1         128   FULL/DR         00:00:39    10.1.2.1        GigabitEthernet0/0/0/1
    Neighbor is up for 01:03:05
2.2.2.2         1     FULL/BDR        00:00:36    10.1.2.2        GigabitEthernet0/0/0/1
    Neighbor is up for 01:02:57
4.4.4.4         1     FULL/DR         00:00:31    10.3.4.4        GigabitEthernet0/0/0/2
    Neighbor is up for 01:04:39
1.1.1.1         128   FULL/  -        00:00:31    10.1.3.1        GigabitEthernet0/0/0/3
    Neighbor is up for 1w2d

 Total neighbor count: 4

```

**Help:** execute the command "show ospf neighbor"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show controllers fabric fia drops ingress location

**Output:**
```
********** FIA-0 **********
Category: in_drop-0
                            From Spaui Drop-0                       11
                                  accpt tbl-0                       22
                                    ctl len-0                       33
                                  short pkt-0                       44
                                max pkt len-0                       55
                                min pkt len-0                       66
                            From Spaui Drop-1                       77
                                  accpt tbl-1                       88
                                    ctl len-1                       99
                                  short pkt-1                        0
                                max pkt len-1                       12
                                min pkt len-1                       13
                                     Tail drp                        4
                                      Vqi drp                        1
                           Header parsing drp                        2
                                 pw to ni drp                        3
                               ni from pw drp                        4
                                  sp0 crc err                       12
                                sp0 bad align                        5
                                 sp0 bad code                        1
                               sp0 align fail                        3
                                 sp0 prot err                        1
                                  sp1 crc err                        1
                                sp1 bad align                        0
                                 sp1 bad code                        0
                               sp1 align fail                        3
                                 sp1 prot err                        0

 ********** FIA-1 **********
Category: in_drop-1
                            From Spaui Drop-0                        0
                                  accpt tbl-0                        0
                                    ctl len-0                        0
                                  short pkt-0                        0
                                max pkt len-0                        0
                                min pkt len-0                        0
                            From Spaui Drop-1                        0
                                  accpt tbl-1                        0
                                    ctl len-1                        0
                                  short pkt-1                        0
                                max pkt len-1                        0
                                min pkt len-1                        0
                                     Tail drp                        0
                                      Vqi drp                        0
                           Header parsing drp                        0
                                 pw to ni drp                        0
                               ni from pw drp                        0
                                  sp0 crc err                        8
                                sp0 bad align                        0
                                 sp0 bad code                        5
                               sp0 align fail                        3
                                 sp0 prot err                        1
                                  sp1 crc err                       12
                                sp1 bad align                        0
                                 sp1 bad code                        8
                               sp1 align fail                        3
                                 sp1 prot err                        0

 ********** FIA-2 **********
 Category: in_drop-2
                            From Spaui Drop-0                        0
                                  accpt tbl-0                        0
                                    ctl len-0                        0
                                  short pkt-0                        0
                                max pkt len-0                        0
                                min pkt len-0                        0
                            From Spaui Drop-1                        0
                                  accpt tbl-1                        0
                                    ctl len-1                        0
                                  short pkt-1                        0
                                max pkt len-1                        0
                                min pkt len-1                        0
                                     Tail drp                        0
                                      Vqi drp                        0
                           Header parsing drp                        0
                                 pw to ni drp                        0
                               ni from pw drp                        0
                                  sp0 crc err                       12
                                sp0 bad align                        0
                                 sp0 bad code                        6
                               sp0 align fail                        3
                                 sp0 prot err                        1
                                  sp1 crc err                        1
                                sp1 bad align                        0
                                 sp1 bad code                        0
                               sp1 align fail                        3
                                 sp1 prot err                        0

 ********** FIA-3 **********
Category: in_drop-3
                            From Spaui Drop-0                        0
                                  accpt tbl-0                        0
                                    ctl len-0                        0
                                  short pkt-0                        0
                                max pkt len-0                        0
                                min pkt len-0                        0
                            From Spaui Drop-1                        0
                                  accpt tbl-1                        0
                                    ctl len-1                        0
                                  short pkt-1                        0
                                max pkt len-1                        0
                                min pkt len-1                        0
                                     Tail drp                        0
                                      Vqi drp                        0
                           Header parsing drp                        0
                                 pw to ni drp                        0
                               ni from pw drp                        0
                                  sp0 crc err                        2
                                sp0 bad align                        0
                                 sp0 bad code                        0
                               sp0 align fail                        3
                                 sp0 prot err                        0
                                  sp1 crc err                        3
                                sp1 bad align                        0
                                 sp1 bad code                        0
                               sp1 align fail                        3
                                 sp1 prot err                        0

```

**Help:** execute the command "show controllers fabric fia drops ingress location"

**Prompt:**
- cisco_xr>
- cisco_xr#

### dir

**Output:**
```
Tue Jan 16 17:08:43.028 AEST

Directory of /var/xr/scratch
74 drwxrwxrwx. 2  4096 Dec  6 19:39 resmon_debug
22 -rw-rw-rw-. 1  2464 Jan  7 19:34 status_file
 11 drwx------. 2 16384 Nov 15 14:44 lost+found
13 drwxr-xr-x. 3  4096 Jan  7 19:32 shutdown
23 drwxrwxrwx. 3  4096 Nov 15 14:59 syslog-hm
68 drwxrwxrwx. 3  4096 Dec  5 22:00 asic-err-logs-backup
41 drwxr-xr-x. 3  4096 Nov 15 15:01 pam
15 lrwxrwxrwx. 1    12 Nov 15 14:58 config -> /misc/config
14 -rw-r--r--. 1   936 Jan  7 19:32 envoke_log
28 drwxrwxrwx. 2  4096 Jan  7 19:33 crypto
 12 drwxr-xr-x. 3  4096 Dec 11 00:53 core
17 drwxrwxrwx. 2  4096 Nov 15 14:58 npu_drvr_cfg
55 drwxr-xr-x. 2  4096 Dec  5 22:46 nvgen_traces
38 -rw-------. 1   444 Nov 15 15:23 .bash_history
25 drwxrwxrwx. 9  4096 Jan  7 19:34 ztp
 19 drwx---r-x. 2  4096 Nov 15 14:58 clihistory

3365348 kbytes total (3163632 kbytes free)
```

**Help:** execute the command "dir"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show ipv4 vrf all interface brief

**Output:**
```

Wed Jul 27 17:18:32.918 CST

Interface                      IP-Address      Status          Protocol Vrf-Name
BVI10                          192.0.2.1       Up              Up       red
BVI20                          192.0.2.1       Shutdown        Down     red
BVI30                          192.0.2.1       Down            Down     red
Bundle-Ether1                  192.0.2.1       Up              Up       **brown
Bundle-Ether1.10               192.0.2.1       Up              Up       green
Bundle-Ether1.20               192.0.2.1       Up              Up       blue
Bundle-Ether1.30               192.0.2.1       Up              Up       blue
Bundle-Ether2                  192.0.2.1       Up              Up       **brown
Bundle-Ether3                  192.0.2.1       Up              Up       **brown
Loopback0                      192.0.2.1       Up              Up       purple
Loopback1                      192.0.2.1       Up              Up       green
GigabitEthernet100/0/0/0       192.0.2.1       Up              Up       blue
GigabitEthernet200/0/0/0.10    192.0.2.1       Up              Up       purple
GigabitEthernet200/0/0/0.20    192.0.2.1       Up              Up       purple
GigabitEthernet200/0/0/0.30    192.0.2.1       Down            Down     purple
TenGigE0/1/0/0                 192.0.2.1       Up              Up       green
TenGigE0/2/0/0.10              192.0.2.1       Up              Up       green

```

**Help:** execute the command "show ipv4 vrf all interface brief"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show ip route

**Output:**
```
Mon Jan 29 19:00:32.892 UTC
VRF: example555


Codes: C - connected, S - static, R - RIP, B - BGP, (>) - Diversion path
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
       U - per-user static route, o - ODR, L - local, G  - DAGR, l - LISP
       A - access/subscriber, a - Application route
       M - mobile route, r - RPL, (!) - FRR Backup path

Gateway of last resort is 172.16.1.1 to network 0.0.0.0

S*   0.0.0.0/0 [1/0] via 172.16.1.1, 04:43:54
O    1.1.1.1/32 [110/0] via 10.1.1.9, 04:43:27, GigabitEthernet0/0/0/0 (!)
                [110/9164] via 10.1.1.34, 04:43:27, GigabitEthernet0/0/0/3
O    1.1.1.3/32 [110/0] via 10.1.1.9, 04:43:21, GigabitEthernet0/0/0/0 (!)
                [110/6564] via 10.1.1.34, 04:43:21, GigabitEthernet0/0/0/3
O    1.1.2.1/32 [110/0] via 10.1.1.9, 04:43:40, GigabitEthernet0/0/0/0 (!)
                [110/9163] via 10.1.1.34, 04:43:40, GigabitEthernet0/0/0/3
O    1.1.2.3/32 [110/0] via 10.1.1.9, 04:43:40, GigabitEthernet0/0/0/0 (!)
                [110/6563] via 10.1.1.34, 04:43:40, GigabitEthernet0/0/0/3
O    1.1.2.5/32 [110/0] via 10.1.1.9, 04:43:40, GigabitEthernet0/0/0/0 (!)
                [110/639] via 10.1.1.34, 04:43:40, GigabitEthernet0/0/0/3
L    1.1.2.6/32 is directly connected, 04:43:54, Loopback0
O    10.1.0.0/30 [110/0] via 10.1.1.9, 04:43:40, GigabitEthernet0/0/0/0 (!)
                 [110/9163] via 10.1.1.34, 04:43:40, GigabitEthernet0/0/0/3
O    10.1.0.8/30 [110/0] via 10.1.1.9, 04:43:40, GigabitEthernet0/0/0/0 (!)
                 [110/6563] via 10.1.1.34, 04:43:40, GigabitEthernet0/0/0/3
O    10.1.1.0/30 [110/0] via 10.1.1.9, 04:43:40, GigabitEthernet0/0/0/0 (!)
                 [110/11762] via 10.1.1.34, 04:43:40, GigabitEthernet0/0/0/3
C    10.1.1.4/30 is directly connected, 04:43:54, GigabitEthernet0/0/0/1
L    10.1.1.6/32 is directly connected, 04:43:54, GigabitEthernet0/0/0/1
C    10.1.1.8/30 is directly connected, 04:43:54, GigabitEthernet0/0/0/0
L    10.1.1.10/32 is directly connected, 04:43:54, GigabitEthernet0/0/0/0
O    10.1.1.12/30 [110/0] via 10.1.1.9, 04:43:40, GigabitEthernet0/0/0/0 (!)
                  [110/9162] via 10.1.1.34, 04:43:40, GigabitEthernet0/0/0/3
O    10.1.1.20/30 [110/0] via 10.1.1.9, 04:43:41, GigabitEthernet0/0/0/0 (!)
                  [110/6562] via 10.1.1.34, 04:43:41, GigabitEthernet0/0/0/3
O    10.1.1.24/30 [110/0] via 10.1.1.9, 04:43:40, GigabitEthernet0/0/0/0 (!)
                  [110/709] via 10.1.1.34, 04:43:40, GigabitEthernet0/0/0/3
C    10.1.1.28/30 is directly connected, 04:43:54, GigabitEthernet0/0/0/2
L    10.1.1.30/32 is directly connected, 04:43:54, GigabitEthernet0/0/0/2
C    10.1.1.32/30 is directly connected, 04:43:54, GigabitEthernet0/0/0/3
L    10.1.1.33/32 is directly connected, 04:43:54, GigabitEthernet0/0/0/3
C    172.16.1.0/24 is directly connected, 04:43:54, MgmtEth0/0/CPU0/0
L    172.16.1.120/32 is directly connected, 04:43:54, MgmtEth0/0/CPU0/0

VRF: VRF10


Codes: C - connected, S - static, R - RIP, B - BGP, (>) - Diversion path
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
       U - per-user static route, o - ODR, L - local, G  - DAGR, l - LISP
       A - access/subscriber, a - Application route
       M - mobile route, r - RPL, (!) - FRR Backup path

Gateway of last resort is not set

L    10.1.0.10/32 is directly connected, 1w1d, Loopback44
B    10.1.0.15/32 [200/0] via 10.1.0.15 (nexthop in vrf default), 3w1d
B    10.1.0.20/32 [200/0] via 10.1.0.20 (nexthop in vrf default), 3w1d

VRF: ThirdExample


Codes: C - connected, S - static, R - RIP, B - BGP, (>) - Diversion path
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
       U - per-user static route, o - ODR, L - local, G  - DAGR, l - LISP
       A - access/subscriber, a - Application route
       M - mobile route, r - RPL, (!) - FRR Backup path
 
Gateway of last resort is not set

O    10.7.1.0/29 [110/110] via 10.2.2.3, 1w5d, GigabitEthernet0/0/0/0
                 [110/110] via 10.2.2.4, 1w5d, GigabitEthernet0/0/0/0
O    10.2.0.0/24 [110/110] via 10.2.2.3, 1w5d, GigabitEthernet0/0/0/0
                 [110/110] via 10.2.2.4, 1w5d, GigabitEthernet0/0/0/0
O    10.2.1.0/29 [110/110] via 10.2.2.3, 1w5d, GigabitEthernet0/0/0/0
                 [110/110] via 10.2.2.4, 1w5d, GigabitEthernet0/0/0/0
C    10.2.2.0/29 is directly connected, 1w5d, GigabitEthernet0/0/0/0
L    10.2.2.1/32 is directly connected, 1w5d, GigabitEthernet0/0/0/0
O E1 10.2.10.2/32 [110/110] via 10.2.2.3, 1w5d, GigabitEthernet0/0/0/0
                  [110/110] via 10.2.2.4, 1w5d, GigabitEthernet0/0/0/0
B    10.3.0.0/24 [200/110] via 10.1.0.25 (nexthop in vrf default), 1w5d
B    10.3.1.0/29 [200/0] via 10.1.0.25 (nexthop in vrf default), 1w5d


VRF: customerA


% No matching routes found


```

**Help:** execute the command "show ip route"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show pim ipv4 neighbor

**Output:**
```

Wed Jul 27 17:18:37.203 CST

PIM neighbors in VRF default
Flag: B - Bidir capable, P - Proxy capable, DR - Designated Router,
      E - ECMP Redirect capable
      * indicates the neighbor created for this router

 Neighbor Address             Interface              Uptime    Expires  DR pri   Flags

192.0.2.1*                   Bundle-Ether10.10      1d09h     00:01:29 1      B E
192.0.2.2                    Bundle-Ether10.20      02:26:23  00:01:26 1 (DR)
192.0.2.3                    BVI10                  2y51w     00:01:27 2 (DR) B
192.0.2.4                    BVI10                  2y51w     00:01:24 0
192.0.2.5                    BVI10                  45w1d     00:01:19 1      P
192.0.2.6*                   BVI10                  2y51w     00:01:25 1      B
```

**Help:** execute the command "show pim ipv4 neighbor"

**Prompt:**
- cisco_xr>
- cisco_xr#

### ping

**Output:**
```
Fri Dec 22 17:30:39.512 BRA
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.191.129.114, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms

```

**Help:** execute the command "ping"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show processes cpu

**Output:**
```
Thu Mar 23 17:16:01.625 EDT

CPU utilization for one minute: 5%; five minutes: 3%; fifteen minutes: 3%

PID    1Min    5Min    15Min Process
1        0%      0%       0% kernel
8195     0%      0%       0% dllmgr
12290    0%      0%       0% wd-critical-mon
12295    0%      0%       0% pkgfs
12296    0%      0%       0% devc-ser8250
12297    0%      0%       0% devc-pty
12298    0%      0%       0% devc-conaux
12299    0%      0%       0% pkgfs
12300    0%      0%       0% ksh
16397    0%      0%       0% pipe
16399    0%      0%       0% mqueue
16400    0%      0%       0% mq
16403    0%      0%       0% shmwin_svr
20500    0%      0%       0% inflator
24594    0%      0%       0% pciesvr
36878    0%      0%       0% nvram
36881    0%      0%       0% mediasvr
36885    0%      0%       0% dumper
36886    0%      0%       0% redfs_svr
36887    0%      0%       0% obflmgr
36888    0%      0%       0% devb-ahci
36889    0%      0%       0% syslogd_helper
36890    0%      0%       0% ahci-mon
36891    0%      0%       0% syslog_dev
36892    0%      0%       0% umass-enum
36893    0%      0%       0% i2c_ctrl_rsp
36895    0%      0%       0% zl30160_server
36896    0%      0%       0% laguna
36898    0%      0%       0% vkg_dmac_svr
49158    0%      0%       0% ge_dmac_svr
49187    0%      0%       0% spp
49188    0%      0%       0% qad_server
49189    0%      0%       0% packet
49190    0%      0%       0% cluster_clm_procmon
49191    2%      2%       2% eth_server
94241    0%      0%       0% attachd
94248    0%      0%       0% qnet
94250    0%      0%       0% mbi-hello
94255    0%      0%       0% insthelper
94256    0%      0%       0% ce_switch
94257    0%      0%       0% attach_server
94258    0%      0%       0% zenjf
94259    0%      0%       0% dao_tmp
102430   0%      0%       0% io-usb
102445   0%      0%       0% devb-umass
102455   0%      0%       0% devb-umass
151593   0%      0%       0% sysmgr
159748   0%      0%       0% correlatord
159749   0%      0%       0% syslogd
159787   0%      0%       0% dsc
159788   0%      0%       0% qsm
159796   0%      0%       0% dsc-clue
159797   0%      0%       0% chkpt_proxy
159798   0%      0%       0% aipc_proxy
159801   0%      0%       0% ltrace_server
159802   0%      0%       0% ltrace_sync
159803   0%      0%       0% obfl_pd_driver
159805   0%      0%       0% sds
159807   0%      0%       0% sld
163902   0%      0%       0% sysmgr
163908   0%      0%       0% top_procs
180289   0%      0%       0% wdsysmon
180291   0%      0%       0% sc_reddrv
184386   0%      0%       0% rmf_svr
213048   0%      0%       0% sysdb_svr_admin
213052   0%      0%       0% sysdb_svr_local
213056   0%      0%       0% enf_broker
213061   0%      0%       0% instdir
213062   0%      0%       0% alphadisplay
213063   0%      0%       0% lrd
213064   0%      0%       0% pwr_mgmt
213065   0%      0%       0% eem_ed_sysmgr
213066   0%      0%       0% meminfo_svr
213067   0%      0%       0% fab_si
213068   0%      0%       0% showd_server
213069   0%      0%       0% sysmgr_show_proc_all_edm
213070   0%      0%       0% dumper_config
213071   0%      0%       0% obfl_config
213074   0%      0%       0% canb-server
217169   1%      1%       1% gsp
217171   0%      0%       0% psm
217172   0%      0%       0% shelfmgr
217173   0%      0%       0% cfg_helper
217174   0%      0%       0% aipc_cleaner
217175   0%      0%       0% bfd_verifier
217176   0%      0%       0% fcd_admin_config
217177   0%      0%       0% mgid_prgm
217178   0%      0%       0% obfl_agent-rp
217179   0%      0%       0% rdsfs_svr
217180   0%      0%       0% tftp_server
217181   0%      0%       0% nrssvr_global
217182   0%      0%       0% pfm_node_rp
217183   0%      0%       0% sysdb_mc
217184   0%      0%       0% bpe
217185   0%      0%       0% cluster_dlm_rp
217186   0%      0%       0% fab_vqi_alloc
217187   0%      0%       0% firmware_manager
217188   0%      0%       0% sysbkup_svr
217189   0%      0%       0% bundlemgr_checker
217190   0%      0%       0% fabmgr
217191   0%      0%       0% licmgr
217192   0%      0%       0% cfgmgr-rp
217193   0%      0%       0% licagent
217194   0%      0%       0% plat_lic_agent
217195   0%      0%       0% plat_license_udi_mgr
217196   0%      0%       0% fiarsp
217197   0%      0%       0% invmgr
217198   0%      0%       0% m_shelfmgr
217199   0%      0%       0% parser_server
217200   0%      0%       0% fab_arb
217201   0%      0%       0% fab_xbar
217203   0%      0%       0% nvgen_server
217204   0%      0%       0% rem_proxy
217206   0%      0%       0% timezone_config
217207   0%      0%       0% cerrno_server
217208   0%      0%       0% locald_DSC
217209   0%      0%       0% online_diag_global
217210   0%      0%       0% online_diag_rsp
217211   0%      0%       0% online_diag_svr
217212   0%      0%       0% envmon
217213   0%      0%       0% fab_license_config
217216   0%      0%       0% config_admin_verify
217218   0%      0%       0% laguna_fpd_agent
217219   0%      0%       0% sam_server
217220   0%      0%       0% spm_server
217221   0%      0%       0% wd-stat-publisher
233552   0%      0%       0% sysdb_shared_data_nc
233586   0%      0%       0% sysdb_shared_nc
233589   0%      0%       0% sysdb_shared_sc
233601   0%      0%       0% debug_d_admin
233606   0%      0%       0% prm_verifier
233607   0%      0%       0% vkg_fib_verifier
233608   0%      0%       0% nrssvr
233609   0%      0%       0% lda_wildchild_config_verifier
233610   0%      0%       0% subdb_svr
233611   0%      0%       0% syncctrl
237694   0%      0%       0% ifmgr
237708   0%      0%       0% netio
237709   0%      0%       0% placed
237710   0%      0%       0% ema_server
237711   0%      0%       0% ifindex_server
237712   0%      0%       0% lpts_pa
237713   0%      0%       0% alarm-logger
237714   0%      0%       0% ether_ctrl_mgmt
241791   0%      0%       0% fwd_driver_partner
241812   0%      0%       0% mempool_edm
241813   0%      0%       0% ncd
241814   0%      0%       0% nd_partner
241815   0%      0%       0% nsr_fo
241816   0%      0%       0% nsr_ping_reply
241817   0%      0%       0% nto_misc_shprocmem_edm
245907   0%      0%       0% rmf_cli_edm
245914   0%      0%       0% rsi_agent
245915   0%      0%       0% rsi_master
245916   0%      0%       0% mpls_io_ea
245917   0%      0%       0% aib
245918   0%      0%       0% bundlemgr_adj
245919   0%      0%       0% statsd_server
245920   0%      0%       0% ipv4_arm
245921   0%      0%       0% ipv6_arm
245922   0%      0%       0% ipv4_acl_mgr
245923   0%      0%       0% ipv6_acl_daemon
245924   0%      0%       0% mgid_server
245925   0%      0%       0% ipv4_mfwd_partner
245926   0%      0%       0% ipv6_mfwd_partner
245927   0%      0%       0% pifibm_server_rp
245928   0%      0%       0% ipv4_io
245929   0%      0%       0% ipv4_ma
245930   0%      0%       0% ipv6_nd
245931   0%      0%       0% policymgr_rp
245932   0%      0%       0% fib_mgr
245933   0%      0%       0% ipv6_ea
245934   0%      0%       0% ipv6_io
245935   0%      0%       0% nve_mgr
245936   0%      0%       0% procfind
245937   0%      0%       0% ipv6_ma
245938   0%      0%       0% mpls_lsd
245939   0%      0%       0% bgp_policy_reg_agent
245940   0%      0%       0% eigrp_policy_reg_agent
245941   0%      0%       0% bcdl_agent
245942   0%      0%       0% igmp_policy_reg_agent
245943   0%      0%       0% igmpsn_policy_reg_agent
245944   0%      0%       0% isis_policy_reg_agent
245945   0%      0%       0% lisp_xr_policy_reg_agent
245946   0%      0%       0% mldp_policy_reg_agent
245947   0%      0%       0% mldsn_policy_reg_agent
245948   0%      0%       0% ospf_policy_reg_agent
245949   0%      0%       0% ospfv3_policy_reg_agent
245950   0%      0%       0% pim6_policy_reg_agent
245951   0%      0%       0% pim_policy_reg_agent
245952   0%      0%       0% rip_policy_reg_agent
245953   0%      0%       0% cemgbl
245954   0%      0%       0% debug_d
245955   0%      0%       0% ether_ctrl_msg_server
245956   0%      0%       0% fsyncglobal
245957   0%      0%       0% fsyncmgr
245958   0%      0%       0% iedged
245959   0%      0%       0% plat_swc_agent
245960   0%      0%       0% redfs_config
245961   0%      0%       0% tcam_mgr_rp
393420   0%      0%       0% cdm_rs
544814   0%      0%       0% bcdls
544970   0%      0%       0% bcdls
544971   0%      0%       0% ether_caps_partner
544973   0%      0%       0% ether_sock
544974   0%      0%       0% vlan_ea
544975   0%      0%       0% ema_server_sdr
544976   0%      0%       0% accounting_ma
544977   0%      0%       0% daps
544978   0%      0%       0% eint_ma
544979   0%      0%       0% flowtrap
544980   0%      0%       0% ipsub_ma
544981   0%      0%       0% l2fib_mgr
544982   0%      0%       0% l2rib
544983   0%      0%       0% ppp_ma
544984   0%      0%       0% pppoe_ma
544985   0%      0%       0% sconbkup
544986   0%      0%       0% ipv6_assembler
544987   0%      0%       0% mpls_fwd_show_proxy
544988   0%      0%       0% statsd_manager_l
544989   0%      0%       0% mpls_io
544990   0%      0%       0% ntpd
544991   0%      0%       0% nfma
544992   0%      0%       0% session_mon
544994   0%      0%       0% route_proxy
544995   0%      0%       0% clns
544996   0%      0%       0% arp
544997   0%      0%       0% ip_aps
544998   0%      0%       0% raw_ip
544999   0%      0%       0% tcp
545000   0%      0%       0% udp
545001   0%      0%       0% fhrp_output
545002   0%      0%       0% l2snoop
545003   0%      0%       0% pim6_ma
545004   0%      0%       0% pim_ma
545005   0%      0%       0% ip_app
545006   0%      0%       0% cinetd
545007   0%      0%       0% devc-vty
545008   0%      0%       0% bundlemgr_local
545009   0%      0%       0% otn_sync
545010   0%      0%       0% pld_upg_d
545011   0%      0%       0% sits
545012   0%      0%       0% tftp_fs
545013   0%      0%       0% vi_config_replicator
545014   0%      0%       0% x86rmon_fpd_agent
545015   0%      0%       0% eem_server
545016   0%      0%       0% showd_lc
545017   0%      0%       0% bcdls
545018   0%      0%       0% tcl_secure_mode
545019   0%      0%       0% lpts_fm
545021   0%      0%       0% eem_policy_dir
545022   0%      0%       0% ipsec_pp
545023   0%      0%       0% cepki
545024   0%      0%       0% crypto_monitor
545025   0%      0%       0% eem_ed_config
545026   0%      0%       0% eem_ed_counter
545027   0%      0%       0% eem_ed_generic
545028   0%      0%       0% eem_ed_hardware
545029   0%      0%       0% eem_ed_nd
545030   0%      0%       0% eem_ed_none
545031   0%      0%       0% eem_ed_oir
545032   0%      0%       0% eem_ed_stats
545033   0%      0%       0% eem_ed_syslog
545034   0%      0%       0% eem_ed_test
545035   0%      0%       0% eem_ed_timer
545036   0%      0%       0% ipsec_mp
545037   0%      0%       0% object_tracking
545039   0%      0%       0% call_home
545041   0%      0%       0% fs_dev_info
545042   0%      0%       0% http_client
549134   0%      0%       0% lamptest-rp
549139   0%      0%       0% redstatsd
549140   0%      0%       0% atmgcmgr
549141   0%      0%       0% canb_bpid2_upg_agt
549142   0%      0%       0% canb_fan_upg_agt
549143   0%      0%       0% canb_upg_agt
549144   0%      0%       0% cem_class_proc
549145   0%      0%       0% cron
549146   0%      0%       0% crypto_edm
549147   0%      0%       0% eem_ed_wdsysmon_edm
549148   0%      0%       0% es_acl_act_agent
549149   0%      0%       0% fr_edm
549150   0%      0%       0% icpe_sdep
549151   0%      0%       0% imaedm_server
549152   0%      0%       0% ipodwdm
549153   0%      0%       0% ipsec_ha_agent
549154   0%      0%       0% ipv4_acl_act_agent
549155   0%      0%       0% ipv6_acl_cfg_agent
549156   0%      0%       0% lc_fpd_upgrade
549157   0%      0%       0% local_sock
549158   0%      0%       0% macsec_ea
549159   0%      0%       0% mediasvr_edm
549160   0%      0%       0% mpls_vpn_mib
549161   0%      0%       0% netio_debug_partner
549162   0%      0%       0% pcds_daemon
549163   0%      0%       0% pfilter_ma
549164   0%      0%       0% pm_ma
549165   0%      0%       0% pm_server
549166   0%      0%       0% pwrmon_upg_agt
549167   0%      0%       0% redfs_edm
549168   0%      0%       0% service_mgr
549169   0%      0%       0% spio_ea
549170   0%      0%       0% spio_ma
549171   0%      0%       0% ssm_process
549172   0%      0%       0% svi_adj_mgr
549173   0%      0%       0% pm_collector
549175   0%      0%       0% srms
553270   0%      0%       0% snmppingd
553272   0%      0%       0% l2tp_mgr
553273   0%      0%       0% schema_server
553274   0%      0%       0% mpls_ldp
553275   0%      0%       0% rt_check_mgr
553276   0%      0%       0% l2vpn_mgr
553277   0%      0%       0% qos_ma
553278   0%      0%       0% vservice_mgr
553279   0%      0%       0% pbr_ma
553280   0%      0%       0% icpe_satmgr
553281   0%      0%       0% ipv6_rump
553282   0%      0%       0% ethernet_stats_controller_edm
553283   0%      0%       0% ipv4_rump
553284   0%      0%       0% tty_verifyd
553285   0%      0%       0% rcp_fs
553286   0%      0%       0% ftp_fs
553287   0%      0%       0% pim6
553288   0%      0%       0% bfd
553289   0%      0%       0% bundlemgr_distrib
553290   0%      0%       0% ipv6_local
553291   0%      0%       0% auto_ip_ring
553292   0%      0%       0% domain_services
553293   0%      0%       0% ipv4_connected
553294   0%      0%       0% mld
553295   0%      0%       0% eth_gl_cfg
553296   0%      0%       0% pim
553297   0%      0%       0% ipv4_mpa
553298   0%      0%       0% ipv6_connected
553299   0%      0%       0% ipv4_local
553300   0%      0%       0% mrib
553301   0%      0%       0% igmp
553302   0%      0%       0% ipv6_mpa
553303   0%      0%       0% policy_repository
553304   0%      0%       0% mrib6
553305   0%      0%       0% nfmgr
553306   0%      0%       0% ipv6_rib
553307   0%      0%       0% intf_mgbl
553308   0%      0%       0% ipv6_mfwd_ma
553309   0%      0%       0% ipv4_rib
553310   0%      0%       0% ipv4_mfwd_ma
553311   0%      0%       0% statsd_manager_g
553312   0%      0%       0% mpls_static
553313   0%      0%       0% bcdls
553314   0%      0%       0% bcdls
553315   0%      0%       0% bcdl_agent
553316   0%      0%       0% bcdl_agent
553317   0%      0%       0% bcdl_agent
557281   0%      0%       0% cdp_mgr
557414   0%      0%       0% snmpd
557415   0%      0%       0% msdp
557416   0%      0%       0% lspv_server
557417   0%      0%       0% rsvp
557418   0%      0%       0% banner_config
557419   0%      0%       0% ip_expl_paths_daemon
557420   0%      0%       0% ipv4_static
557421   0%      0%       0% mibd_entity
557422   0%      0%       0% mibd_infra
557423   0%      0%       0% mibd_interface
557424   0%      0%       0% mibd_route
557425   0%      0%       0% bpm
557426   0%      0%       0% bgp
557427   0%      0%       0% radiusd
557428   0%      0%       0% tacacsd
557429   0%      0%       0% kc_srvr
557430   0%      0%       0% ip_smiap
557431   0%      0%       0% mpp_srvr
557432   0%      0%       0% ospf_uv
557433   0%      0%       0% ospf
557434   0%      0%       0% ssh_server
557435   0%      0%       0% ssh_conf_verifier
557436   0%      0%       0% te_control
561534   0%      0%       0% loopback_caps_partner
561535   0%      0%       0% cdp
48337148   0%      0%       0% sshd_child_handler
48337168   0%      0%       0% exec
48337277   0%      0%       0% 48337277_unknown
```

**Help:** execute the command "show processes cpu"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show version brief

**Output:**
```

Wed Jul 27 17:17:42.915 CST

Cisco IOS XR Software, Version 5.3.2[Default]
 Copyright (c) 2015 by Cisco Systems, Inc.

ROM: System Bootstrap, Version 5.15(c) 1994-2012 by Cisco Systems,  Inc.

rtr-01 uptime is 2 years, 51 weeks, 5 days, 11 hours, 1 minute
System image file is "disk0:asr9k-os-mbi-5.3.2.sp1-1.0.0/0x100305/mbiasr9k-rsp3.vm"

cisco ASR9K Series (Intel 686 F6M14S4) processor with 12582912K bytes of memory.
Intel 686 F6M14S4 processor at 2130MHz, Revision 2.174
ASR 9912 10 Line Card Slot Chassis with V2 AC PEM

4 Management Ethernet
132 GigabitEthernet/IEEE 802.3 interface(s)
72 TenGigE
72 DWDM controller(s)
72 WANPHY controller(s)
 503k bytes of non-volatile configuration memory.
6111M bytes of hard disk.
 12510192k bytes of disk0: (Sector size 512 bytes).
12510192k bytes of disk1: (Sector size 512 bytes).
```

**Help:** execute the command "show version brief"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show lldp neighbors

**Output:**
```
Mon Jan 29 19:06:33.768 UTC
Capability codes:
        (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
        (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other

Device ID       Local Intf          Hold-time  Capability     Port ID
ASR-OCC-P1      Gi0/0/0/0           120        R               Gi0/0/0/2
ASR-LON-P1      Gi0/0/0/3           120        R               Gi0/0/0/2

Total entries displayed: 2

```

**Help:** execute the command "show lldp neighbors"

**Prompt:**
- cisco_xr>
- cisco_xr#

### show version

**Output:**
```
Cisco IOS XR Software, Version 4.1.0[Default]
Copyright (c) 2010 by Cisco Systems, Inc.

 
ROM: System Bootstrap, Version 2.100(20100129:213223) [CRS-1 ROMMON],  


router uptime is 1 week, 6 days, 4 hours, 22 minutes
 System image file is "bootflash:disk0/hfr-os-mbi-4.1.0/mbihfr-rp.vm"


 cisco CRS-8/S (7457) processor with 4194304K bytes of memory.
7457 processor at 1197Mhz, Revision 1.2


2 Management Ethernet
8 GigabitEthernet
12 SONET/SDH
 12 Packet over SONET/SDH
1 WANPHY controller(s)
1 TenGigE
1019k bytes of non-volatile configuration memory.
38079M bytes of hard disk.
3607592k bytes of disk0: (Sector size 512 bytes).
3607592k bytes of disk1: (Sector size 512 bytes).


Boot device on node 0/1/SP is bootflash:
Package active on node 0/1/SP:
hfr-doc, V 4.1.0[Default], Cisco Systems, at disk0:hfr-doc-4.1.0
    Built on Thu May  6 17:28:51 DST 2010
    By sjc-lds-364 in /auto/ioxbuild6/production/4.1.0.DT_IMAGE/hfr/workspace for pie


iosxr-infra, V 4.1.0[Default], Cisco Systems, at disk0:iosxr-infra-4.1.0
    Built on Thu May  6 15:09:12 DST 2010
    By sjc-lds-364 in /auto/ioxbuild6/production/4.1.0.DT_IMAGE/hfr/workspace for pie

```

**Help:** execute the command "show version"

**Prompt:**
- cisco_xr>
- cisco_xr#

### terminal width 511

**Output:** None

**Help:** Execute the command terminal width 511. This automatically generated. Feel free to change it!

**Prompt:**
- cisco_xr>
- cisco_xr#

### terminal length 0

**Output:** None

**Help:** Execute the command terminal length 0. This automatically generated. Feel free to change it!

**Prompt:**
- cisco_xr>
- cisco_xr#

### terminal width 512

**Output:** None

**Help:** Execute the command terminal width 512. This automatically generated. Feel free to change it!

**Prompt:**
- cisco_xr>
- cisco_xr#

