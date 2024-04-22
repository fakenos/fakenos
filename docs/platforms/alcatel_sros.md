# alcatel_sros


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
- alcatel_sros>

### show router pim interface

**Output:**
```

===============================================================================
 PIM Interfaces ipv4
===============================================================================
Interface                   Adm  Opr  DR Prty         Hello Intvl  Mcast Send
   DR
-------------------------------------------------------------------------------
R1_R2                       Up   Up   1               30           auto
   192.0.2.245
R1_R3                       Up   Up   1               30           auto
   192.0.2.42
R1_R4                       Up   Down 10              30           auto
   N/A
R1_R5                       Up   Down 5               30           auto
   N/A
R1_R6                       Up   Down N/A             30           auto
   N/A
-------------------------------------------------------------------------------
 Interfaces : 5 Tunnel-Interfaces : 0
===============================================================================

```

**Help:** execute the command "show router pim interface"

**Prompt:**
- alcatel_sros>
- alcatel_sros#

### show router interface

**Output:**
```
===============================================================================
 Interface Table (Router: Base)
===============================================================================
Interface-Name                   Adm       Opr(v4/v6)  Mode    Port/SapId
   IP-Address                                                  PfxState
-------------------------------------------------------------------------------
L3-Telecom-IXR01-1               Up        Down/Up     IES     lag-21:300
   2001:4888:2062:357a:645:400:0:2/64                          PREFERRED
   fe80::645:400:0:2/64                                        PREFERRED
L3-Telecom-IXR02-1               Up        Down/Up     IES     lag-22:300
   2001:4888:2062:3591:645:400:0:2/64                          PREFERRED
   fe80::645:400:0:2/64                                        PREFERRED
TO_EDGE_IXR01                    Up        Down/Down   Network n/a
   192.168.28.1/24                                             n/a
   192.168.47.1/24                                             n/a
system                           Up        Up/Up       Network system
   10.115.43.64/32                                             n/a
   2001:4888:2062:3000:645:400:0:1a0/128                       PREFERRED
to-7750-02                       Up        Up/Up       Network 1/1/c4/1:2415
   172.25.214.121/31                                           n/a
   2001:4888:206a:335c:645:400:0:1/64                          PREFERRED
   fe80::c9:ffff:fe00:0/64                                     PREFERRED
to-BTS0415-7750-H1               Up        Down/Down   Network lag-11:4094
   172.25.198.123/31                                           n/a
   2001:4888:206a:335f:645:400:0:1/64                          INACCESSIBLE
   fe80::c9:ffff:fe00:14b/64                                   INACCESSIBLE
-------------------------------------------------------------------------------
 Interfaces : 6
===============================================================================

```

**Help:** execute the command "show router interface"

**Prompt:**
- alcatel_sros>
- alcatel_sros#

### show router mpls interface

**Output:**
```
===============================================================================
 MPLS Interfaces
===============================================================================
Interface                           Port-id           Adm  Opr(V4/V6) TE-
                                                                      metric
-------------------------------------------------------------------------------
system                              system            Up   Up/Down    None
  Admin Groups                      None
  SRLG Groups                       None
TO_IOSXR                            1/1/c4/1          Up   Up/Down    98999
  Admin Groups                      RED
                                    GREEN
  SRLG Groups                       None
TO_R1                               1/1/c1/1          Up   Up/Down    65660
  Admin Groups                      None
  SRLG Groups                       None
TO_R4                               1/1/c2/1          Up   Up/Down    None
  Admin Groups                      None
  SRLG Groups                       PURPLE
                                    WHITE
-------------------------------------------------------------------------------
 Interfaces : 4
===============================================================================
```

**Help:** execute the command "show router mpls interface"

**Prompt:**
- alcatel_sros>
- alcatel_sros#

### show service sdp

**Output:**
```

============================================================================
 Services: Service Destination Points
============================================================================
SdpId  AdmMTU  OprMTU  Far End          Adm  Opr         Del     LSP   Sig
----------------------------------------------------------------------------
1      0       9170    192.168.0.1      Down Down        GRE     n/a   TLDP
31     0       0       10.10.10.1       Up   Down        MPLS    R     TLDP
32     0       0       10.10.10.2       Up   Down        MPLS    R     TLDP
34     0       0       10.10.10.4       Up   Down        MPLS    R     TLDP
38     0       492     10.10.10.8       Up   Down        MPLS    R     TLDP
2000   0       0                        Down Down        GRE     n/a   TLDP
 ----------------------------------------------------------------------------
 Number of SDPs : 6
----------------------------------------------------------------------------
 Legend: R = RSVP, L = LDP, B = BGP, M = MPLS-TP, n/a = Not Applicable
        I = SR-ISIS, O = SR-OSPF, T = SR-TE, F = FPE
============================================================================

```

**Help:** execute the command "show service sdp"

**Prompt:**
- alcatel_sros>
- alcatel_sros#

### show router isis adjacency

**Output:**
```

===============================================================================
 Rtr Base ISIS Instance 0 Adjacency
===============================================================================
 System ID                Usage State Hold Interface                     MT-ID
-------------------------------------------------------------------------------
R2                       L2    Up    27   R1_R2                         0,2
R3                       L2    Up    19   R1_R3                         0,2
 -------------------------------------------------------------------------------
 Adjacencies : 2
===============================================================================

```

**Help:** execute the command "show router isis adjacency"

**Prompt:**
- alcatel_sros>
- alcatel_sros#

### show service sdp-using

**Output:**
```
===============================================================================
 SDP Using
===============================================================================
SvcId      SdpId              Type   Far End              Opr   I.Label E.Label
                                                          State         
-------------------------------------------------------------------------------
200        31:200             Spok   10.10.10.1           Up    524281  524283
200        34:200             Mesh   10.10.10.4           Down  None    None
310        32767:4294967295   BgpAd  10.10.10.1           Up    524278  524280
400        32767:4294967294   BgpAd  10.10.10.1           Up    524277  524279
401        32767:4294967293   BgpAd  10.10.10.1           Up    524276  524278
 -------------------------------------------------------------------------------
 Number of SDPs : 5
-------------------------------------------------------------------------------
===============================================================================

```

**Help:** execute the command "show service sdp-using"

**Prompt:**
- alcatel_sros>
- alcatel_sros#

### show router isis interface

**Output:**
```

===============================================================================
 Rtr Base ISIS Instance 0 Interfaces
===============================================================================
Interface                        Level CircID  Oper State   L1/L2 Metric
-------------------------------------------------------------------------------
system                           L1L2  1       Up           0/0
R1_R2                            L2    18      Up           10/10
R1_R3                            L1    21      Down         10/1000
-------------------------------------------------------------------------------
 Interfaces : 3
===============================================================================

```

**Help:** execute the command "show router isis interface"

**Prompt:**
- alcatel_sros>
- alcatel_sros#

### show router mpls lsp

**Output:**
```
===============================================================================
 MPLS LSPs (Originating)
===============================================================================
 LSP Name                                            Tun     Fastfail  Adm  Opr
  To                                                Id      Config         
-------------------------------------------------------------------------------
TO_IOSXR                                            1       Yes       Up   Up
  10.10.10.8                                                               
TO_R1                                               2       Yes       Up   Up
  10.10.10.1                                                               
TO_R2                                               3       Yes       Up   Dwn
  10.10.10.2                                                               
TO_R4                                               4       Yes       Up   Dwn
  10.10.10.4                                                               
Full-Mesh-10.10.10.8-61441                          61441   Yes       Up   Up
  10.10.10.8                                                               
Full-Mesh-10.10.10.1-65240                          65240   Yes       Up   Up
  10.10.10.1                                                               
-------------------------------------------------------------------------------
 LSPs : 6
===============================================================================

```

**Help:** execute the command "show router mpls lsp"

**Prompt:**
- alcatel_sros>
- alcatel_sros#

### show lag

**Output:**
```

===============================================================================
 Lag Data
===============================================================================
Lag-id         Adm     Opr     Weighted Threshold Up-Count MC Act/Stdby
-------------------------------------------------------------------------------
1              up      up      No       0         2        N/A
2              up      up      No       0         2        N/A
3              up      up      No       0         1        N/A
4              down    down    No       0         0        N/A
5              down    down    No       0         0        N/A
10             down    down    No       0         0        N/A
20             up      down    No       0         0        standby
70             down    down    No       0         0        N/A
80             up      down    No       0         0        N/A
90             down    down    No       0         0        N/A
100            up      up      No       0         1        N/A
101            up      up      No       0         1        N/A
102            up      up      No       0         1        N/A
103            up      up      No       0         1        active
104            up      up      No       0         1        N/A
105            up      up      No       0         1        N/A
106            up      up      No       0         1        N/A
107            up      up      No       0         1        N/A
108            up      up      No       0         1        N/A
109            up      up      No       0         1        N/A
110            up      up      No       0         1        active
111            up      up      No       0         1        N/A
112            up      up      No       0         1        N/A
114            up      up      No       0         1        N/A
115            up      up      No       0         1        N/A
120            up      up      No       0         1        N/A
124            down    down    No       0         0        N/A
140            up      up      No       0         1        N/A
150            down    down    No       0         0        N/A
153            up      up      No       0         1        active
180            down    down    No       0         0        N/A
-------------------------------------------------------------------------------
 Total Lag-ids: 31      Single Chassis: 27       MC Act: 3       MC Stdby: 1
===============================================================================

```

**Help:** execute the command "show lag"

**Prompt:**
- alcatel_sros>
- alcatel_sros#

### show service sap-using

**Output:**
```
===============================================================================
 Service Access Points 
===============================================================================
PortId                          SvcId      Ing.  Ing.    Egr.  Egr.   Adm  Opr
                                           QoS   Fltr    QoS   Fltr        
-------------------------------------------------------------------------------
lag-21:300                      1          11130 none    11140 none   Up   Up
lag-22:300                      1          11130 ip4     11140 none   Up   Up
1/1/c6/1:234                    400        1     none    1     none   Up   Down
lag-21:400                      76415001   10    none    1     none   Up   Up
lag-22:400                      76415002   10    none    1     none   Up   Up
 -------------------------------------------------------------------------------
 Number of SAPs : 5
-------------------------------------------------------------------------------
===============================================================================

```

**Help:** execute the command "show service sap-using"

**Prompt:**
- alcatel_sros>
- alcatel_sros#

### show router ldp interface

**Output:**
```

===============================================================================
 LDP Interfaces
===============================================================================
Interface                         Adm/Opr
 Sub-Interface(s)                  Adm/Opr  Hello Hold  KA    KA    Transport
                                            Fctr  Time  Fctr  Time  Address
-------------------------------------------------------------------------------
R1_R2                             Up/Up
  ipv4                              Up/Up   3     15    3     30    System
R1_R3                             Up/Up
  ipv4                              Up/Up   3     15    3     30    System
  ipv6                              Up/Up   3     15    3     30    System
R1_R4                             Up/Up
  ipv4                              Up/Dwn  3     15    3     30    System
-------------------------------------------------------------------------------
 No. of Interfaces: 3
===============================================================================

```

**Help:** execute the command "show router ldp interface"

**Prompt:**
- alcatel_sros>
- alcatel_sros#

### oam mac-ping

**Output:**
```
Seq Node-id                                                    Path     RTT
----------------------------------------------------------------------------
 [Send request Seq. 1, Size 126]
1   192.0.2.4:sap1/1/2:100                 No FIB on Egress In-Band  0.153ms

```

**Help:** execute the command "oam mac-ping"

**Prompt:**
- alcatel_sros>
- alcatel_sros#

### show service id base

**Output:**
```
===============================================================================
 Service Basic Information
===============================================================================
 Service Id        : 1099                Vpn Id            : 0
Service Type      : VPLS                
Name              : (Not Specified)
Description       : this_is_a_description
Customer Id       : 4                   
 Last Status Change: 10/31/2016 14:44:10 
Last Mgmt Change  : 11/01/2016 11:04:36 
Admin State       : Up                  Oper State        : Down
MTU               : 5000                Def. Mesh VC Id   : 1099
SAP Count         : 1                   SDP Bind Count    : 1
Snd Flush on Fail : Disabled            Host Conn Verify  : Disabled
Propagate MacFlush: Disabled            Per Svc Hashing   : Disabled
Allow IP Intf Bind: Disabled            
Def. Gateway IP   : None                
Def. Gateway MAC  : None                
Temp Flood Time   : Disabled            Temp Flood        : Inactive
Temp Flood Chg Cnt: 0                   
 
-------------------------------------------------------------------------------
 Service Access & Destination Points
-------------------------------------------------------------------------------
Identifier                               Type         AdmMTU  OprMTU  Adm  Opr
-------------------------------------------------------------------------------
sap:1/1/6:100                            q-tag        9212    9212    Up   Down
 sdp:4:1099 M(192.0.2.4)                  Mesh         0       9190    Up   Down
===============================================================================

```

**Help:** execute the command "show service id base"

**Prompt:**
- alcatel_sros>
- alcatel_sros#

### show router bgp summary family

**Output:**
```
[kvanlang@steffi upgrade-support]$ cat ../ntc-templates-test/lib/test-bgp-sum-family.raw
 A:SRHERE01# show router "Base" bgp summary family ipv4
===============================================================================
 BGP Router ID:192.0.2.11   AS:6848        Local AS:65535
===============================================================================
 BGP Admin State         : Up          BGP Oper State              : Up
Total Peer Groups       : 6           Total Peers                 : 150
Total VPN Peer Groups   : 79          Total VPN Peers             : 207
Total BGP Paths         : 407944      Total Path Memory           : 160791243

Total IPv4 Remote Rts   : 1725031     Total IPv4 Rem. Active Rts  : 862201
Total IPv6 Remote Rts   : 0           Total IPv6 Rem. Active Rts  : 0
Total IPv4 Backup Rts   : 0           Total IPv6 Backup Rts       : 0
Total LblIpv4 Rem Rts   : 2844        Total LblIpv4 Rem. Act Rts  : 311
Total LblIpv6 Rem Rts   : 196896      Total LblIpv6 Rem. Act Rts  : 98446
Total LblIpv4 Bkp Rts   : 0           Total LblIpv6 Bkp Rts       : 0
Total Supressed Rts     : 0           Total Hist. Rts             : 0
Total Decay Rts         : 0

 Total VPN-IPv4 Rem. Rts : 93000       Total VPN-IPv4 Rem. Act. Rts: 45689
 Total VPN-IPv6 Rem. Rts : 0           Total VPN-IPv6 Rem. Act. Rts: 0
Total VPN-IPv4 Bkup Rts : 0           Total VPN-IPv6 Bkup Rts     : 0
Total VPN Local Rts     : 1147        Total VPN Supp. Rts         : 0
Total VPN Hist. Rts     : 0           Total VPN Decay Rts         : 0

Total MVPN-IPv4 Rem Rts : 0           Total MVPN-IPv4 Rem Act Rts : 0
Total MVPN-IPv6 Rem Rts : 0           Total MVPN-IPv6 Rem Act Rts : 0
Total MDT-SAFI Rem Rts  : 0           Total MDT-SAFI Rem Act Rts  : 0
Total McIPv4 Remote Rts : 0           Total McIPv4 Rem. Active Rts: 0
Total McIPv6 Remote Rts : 0           Total McIPv6 Rem. Active Rts: 0
Total McVpnIPv4 Rem Rts : 0           Total McVpnIPv4 Rem Act Rts : 0
Total McVpnIPv6 Rem Rts : 0           Total McVpnIPv6 Rem Act Rts : 0

Total EVPN Rem Rts      : 692         Total EVPN Rem Act Rts      : 338
Total L2-VPN Rem. Rts   : 0           Total L2VPN Rem. Act. Rts   : 0
Total MSPW Rem Rts      : 0           Total MSPW Rem Act Rts      : 0
Total RouteTgt Rem Rts  : 1546        Total RouteTgt Rem Act Rts  : 1546
Total FlowIpv4 Rem Rts  : 0           Total FlowIpv4 Rem Act Rts  : 0
 Total FlowIpv6 Rem Rts  : 0           Total FlowIpv6 Rem Act Rts  : 0
Total Link State Rem Rts: 0           Total Link State Rem Act Rts: 0
Total SrPlcyIpv4 Rem Rts: 0           Total SrPlcyIpv4 Rem Act Rts: 0

===============================================================================
 BGP IPv4 Summary
===============================================================================
 Legend : D - Dynamic Neighbor
===============================================================================
Neighbor
                   AS PktRcvd PktSent  InQ OutQ Up/Down   State|Recv/Actv/Sent
-------------------------------------------------------------------------------
192.0.2.118
               42598*  228872  215409    0    0 25d10h18m 2/2/1
192.0.2.110
               42598   271035  249777    0    0 29d11h41m 1/1/1
192.0.2.126
               42598*       0       0    0    0 54d18h43m Connect
192.0.2.254
               42598*       0       0    0    0 36d13h37m Active
192.0.2.103
               65535  390698*  749512    0    0 54d18h40m 862440/627895/373
192.0.2.104
               65535  355316*  749512    0    0 54d18h40m 862439/234172/373
 -------------------------------------------------------------------------------
 * indicates that the corresponding row element may have been truncated.

```

**Help:** execute the command "show router bgp summary family"

**Prompt:**
- alcatel_sros>
- alcatel_sros#

### show system cpu

**Output:**
```
===============================================================================
 CPU Utilization (Sample period: 1 second)
===============================================================================
Name                                   CPU Time       CPU Usage        Capacity
                                         (uSec)                           Usage
-------------------------------------------------------------------------------
BFD                                         189           0.01%           0.01%
BGP                                          20          ~0.00%          ~0.00%
 BGP PE-CE                                     0           0.00%           0.00%
BIER                                          0           0.00%           0.00%
CFLOWD                                       48          ~0.00%          ~0.00%
 Cards & Ports                             2,311           0.23%           0.10%
 DHCP Server                                  11          ~0.00%          ~0.00%
ETH-CFM                                     244           0.02%           0.02%
 HQoS Algorithm                              102           0.01%           0.01%
 HQoS Statistics                             653           0.06%           0.06%
ICC                                         524           0.05%           0.03%
IGMP/MLD                                     78          ~0.00%          ~0.00%
 IMSI Db Appl                                128           0.01%           0.01%
IOM                                      37,866           3.78%           2.15%
 IP Stack                                  3,554           0.35%           0.22%
IS-IS                                       298           0.02%           0.01%
ISA                                       1,093           0.10%           0.03%
LDP                                         433           0.04%           0.02%
Logging                                      15          ~0.00%          ~0.00%
MBUF                                          0           0.00%           0.00%
MCS                                          83          ~0.00%          ~0.00%
MPLS/RSVP                                 1,230           0.12%           0.05%
MSCP                                          0           0.00%           0.00%
MSDP                                          0           0.00%           0.00%
Management                               25,404           2.53%           1.84%
OAM                                       1,759           0.17%           0.05%
OSPF                                        815           0.08%           0.02%
OpenFlow                                     30          ~0.00%          ~0.00%
PIM/L2Mcast                                   0           0.00%           0.00%
PKI                                          24          ~0.00%          ~0.00%
PTP                                           8          ~0.00%          ~0.00%
RIP                                           0           0.00%           0.00%
RTM/Policies                                  0           0.00%           0.00%
Redundancy                                    0           0.00%           0.00%
SIM                                       4,086           0.40%           0.39%
 SNMP Daemon                                   0           0.00%           0.00%
Security                                      0           0.00%           0.00%
Services                                  1,246           0.12%           0.04%
Stats                                         0           0.00%           0.00%
Stats-Extended                                0           0.00%           0.00%
 Subscriber Mgmt                             834           0.08%           0.01%
System                                   52,774           5.27%           2.63%
 Traffic Eng                                   0           0.00%           0.00%
 Tree Sid                                      0           0.00%           0.00%
VRRP                                        227           0.02%           0.01%
 WEB Redirect                                107           0.01%          ~0.00%
-------------------------------------------------------------------------------
Total                                 1,001,337         100.00%                
   Idle                                 865,143          86.39%                
   Usage                                136,194          13.60%                
Busiest Core Utilization                136,194          13.60%                
===============================================================================

```

**Help:** execute the command "show system cpu"

**Prompt:**
- alcatel_sros>
- alcatel_sros#

### show router rsvp interface

**Output:**
```
===============================================================================
 RSVP Interfaces
===============================================================================
Interface                        Total    Active    Total BW  Resv BW   Adm Opr
                                 Sessions Sessions  (Mbps)    (Mbps)        
-------------------------------------------------------------------------------
system                           -        -         -         -         Up  Up
TO_IOSXR                         0        0         10000     0         Dwn Dwn
TO_R1                            0        0         10000     0         Up  Up
TO_R4                            0        0         10000     0         Up  Up
-------------------------------------------------------------------------------
 Interfaces : 4
===============================================================================

```

**Help:** execute the command "show router rsvp interface"

**Prompt:**
- alcatel_sros>
- alcatel_sros#

### show router bgp routes vpn-ipv4

**Output:**
```
===============================================================================
 BGP Router ID:192.0.2.1        AS:65500       Local AS:65500      
===============================================================================
 Legend -
 Status codes  : u - used, s - suppressed, h - history, d - decayed, * - valid
                 l - leaked, x - stale, > - best, b - backup, p - purge
 Origin codes  : i - IGP, e - EGP, ? - incomplete

===============================================================================
 BGP VPN-IPv4 Routes
===============================================================================
Flag  Network                                            LocalPref   MED
      Nexthop (Router)                                   Path-Id     Label
      As-Path                                                        
-------------------------------------------------------------------------------
*>i   65500:11:192.0.2.4/32                              100         None
      10.11.5.5                                          None        262132
      No As-Path                                                      
u*>i  65500:11:192.0.2.14/32                             100         None
      192.0.2.2                                          None        262132
      No As-Path                                                      
-------------------------------------------------------------------------------
 Routes : 2
===============================================================================

```

**Help:** execute the command "show router bgp routes vpn-ipv4"

**Prompt:**
- alcatel_sros>
- alcatel_sros#

### show port

**Output:**
```

===============================================================================
 Ports on Slot 1
===============================================================================
Port          Admin Link Port    Cfg  Oper LAG/ Port Port Port   C/QS/S/XFP/
Id            State      State   MTU  MTU  Bndl Mode Encp Type   MDIMDX
-------------------------------------------------------------------------------
1/1/1         Up    Yes  Up      9212 9212    - hybr dotq xcme   GIGE-SX
1/1/2         Up    Yes  Up      1518 1518    - accs dotq xcme   MDI GIGE-T
1/1/3         Up    Yes  Up      1518 1518    - accs dotq xcme   MDX GIGE-T
1/1/4         Up    Yes  Up      9212 9212    1 netw null xcme   GIGE-SX
1/1/5         Up    Yes  Up      9212 9212    - netw null xcme   GIGE-SX
1/1/6         Up    Yes  Up      9212 9212    - netw null xcme   GIGE-SX
1/1/7         Up    Yes  Up      1518 1518    - accs dotq xcme   MDX GIGE-T
1/1/8         Up    Yes  Up      1514 1514    - accs null xcme   MDX GIGE-T
1/1/9         Up    Yes  Up      9212 9212    - netw null xcme   GIGE-SX
1/1/10        Up    No   Down    1518 1518    - accs dotq xcme   GIGE-SX
1/1/11        Up    No   Down    1518 1518    - accs dotq xcme   GIGE-T
1/1/12        Up    Yes  Up      9000 9000    - accs null xcme   MDX GIGE-T
1/1/13        Up    Yes  Up      1514 1514    - accs null xcme   GIGE-SX
1/1/14        Up    Yes  Up      1514 1514    - accs null xcme   MDI GIGE-T
1/1/15        Up    Yes  Up      9000 9000    - accs null xcme   MDI GIGE-T
1/1/16        Up    Yes  Up      1514 1514    - accs null xcme   GIGE-SX
1/1/17        Up    No   Down    1518 1518    - accs dotq xcme   GIGE-T
1/1/18        Up    Yes  Up      1518 1518    - accs dotq xcme   MDI GIGE-T
1/1/19        Up    Yes  Up      1514 1514    - accs null xcme   MDI GIGE-T
1/1/20        Up    Yes  Up      9212 9212    - hybr dotq xcme   MDX GIGE-T
1/1/21        Up    Yes  Up      1518 1518    - accs dotq xcme   GIGE-SX
1/1/22        Up    Yes  Up      1518 1518    - accs dotq xcme   GIGE-SX
1/1/23        Up    Yes  Up      1518 1518    - accs dotq xcme   MDI GIGE-T
1/1/24        Up    Yes  Up      1518 1518    - accs dotq xcme   MDX GIGE-T
1/2/1         Up    No   Down    1518 1518    - accs dotq xcme   GIGE-SX
1/2/2         Up    Yes  Up      1514 1514    - accs null xcme   MDI GIGE-T
1/2/3         Up    Yes  Up      1514 1514    - accs null xcme   MDI GIGE-T
1/2/4         Up    No   Down    1514 1514    - accs null xcme   GIGE-T
1/2/5         Up    Yes  Up      9212 9212    - hybr dotq xcme   MDX GIGE-T
1/2/6         Up    No   Down    9022 9022    - accs null xcme   GIGE-T
1/2/7         Up    Yes  Up      1514 1514    - accs null xcme   MDX GIGE-T
1/2/8         Up    No   Down    1514 1514    - accs null xcme
1/2/9         Up    No   Down    1518 1518   99 accs dotq xcme   GIGE-SX
1/2/10        Up    Yes  Up      1514 1514    - accs null xcme   MDI GIGE-T
1/2/11        Up    Yes  Up      1514 1514    - accs null xcme   MDI GIGE-T
1/2/12        Up    No   Down    1514 1514    - accs null xcme   GIGE-T
1/2/13        Up    Yes  Up      1514 1514    - accs null xcme   MDX GIGE-T
1/2/14        Up    No   Down    1514 1514    - accs null xcme   GIGE-T
1/2/15        Up    No   Down    1570 1570    - accs dotq xcme   GIGE-T
1/2/16        Up    Yes  Up      9022 9022    - accs null xcme   MDX GIGE-T
1/2/17        Up    Yes  Up      1538 1538    - accs dotq xcme   MDX GIGE-T
1/2/18        Up    No   Down    1514 1514    - accs null xcme   GIGE-T
1/2/19        Up    No   Down    1518 1518    - accs dotq xcme   GIGE-T
1/2/20        Up    No   Down    1514 1514    - accs null xcme   GIGE-T
1/2/21        Up    Yes  Up      1514 1514    - accs null xcme   MDI GIGE-T
1/2/22        Up    Yes  Up      1518 1518    - accs dotq xcme   MDX GIGE-T
1/2/23        Up    Yes  Up      1518 1518    - accs dotq xcme   MDX GIGE-T
1/2/24        Up    Yes  Up      9212 9212    7 netw null xcme   GIGE-SX

===============================================================================
 Ports on Slot A
===============================================================================
Port          Admin Link Port    Cfg  Oper LAG/ Port Port Port   C/QS/S/XFP/
Id            State      State   MTU  MTU  Bndl Mode Encp Type   MDIMDX
-------------------------------------------------------------------------------
A/1           Up    Yes  Up      1514 1514    - netw null faste  MDI
A/4           Up    No   Down    1514 1514    - netw null faste

===============================================================================
 Ports on Slot B
===============================================================================
Port          Admin Link Port    Cfg  Oper LAG/ Port Port Port   C/QS/S/XFP/
Id            State      State   MTU  MTU  Bndl Mode Encp Type   MDIMDX
-------------------------------------------------------------------------------
B/1           Up    No   Down    1514 1514    - netw null faste
B/4           Up    No   Down    1514 1514    - netw null faste


===============================================================================
 Ports on Satellite esat-1
===============================================================================
Port          Admin Link Port    Cfg  Oper LAG/ Port Port Port   C/QS/S/XFP/
Id            State      State   MTU  MTU  Bndl Mode Encp Type   MDIMDX
-------------------------------------------------------------------------------
esat-1/1/1    Up    Yes  Up      1518 1518    5 accs dotq xcme   MDI GIGE-T
esat-1/1/2    Up    Yes  Up      1518 1518    - accs dotq xcme   MDI GIGE-T
esat-1/1/3    Up    Yes  Up      1518 1518    - accs dotq xcme   MDX GIGE-T
esat-1/1/4    Up    Yes  Up      1538 1538    - accs dotq xcme   MDX GIGE-T
esat-1/1/5    Up    Yes  Up      9022 9022    - accs null xcme   MDX GIGE-T
esat-1/1/6    Up    Yes  Up      1514 1514    - accs null xcme   MDI GIGE-T
esat-1/1/7    Up    Yes  Up      9022 9022    - accs null xcme   MDI GIGE-T
esat-1/1/8    Up    No   Down    9022 9022    - accs null xcme   GIGE-T
esat-1/1/9    Down  No   Down    9208 9208    - netw null xcme
esat-1/1/10   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/11   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/12   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/13   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/14   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/15   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/16   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/17   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/18   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/19   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/20   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/21   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/22   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/23   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/24   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/25   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/26   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/27   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/28   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/29   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/30   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/31   Up    No   Down    9208 9208    - netw null xcme
esat-1/1/32   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/33   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/34   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/35   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/36   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/37   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/38   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/39   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/40   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/41   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/42   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/43   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/44   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/45   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/46   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/47   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/48   Down  No   Down    9208 9208    - netw null xcme
esat-1/1/u1   Up    Yes  Up      9212 9212    - accs dotq xgige  10GBASE-LR  *
esat-1/1/u2   Up    No   Down    9212 9212    - accs dotq xgige
esat-1/1/u3   Up    No   Down    9212 9212    - accs dotq xgige
esat-1/1/u4   Up    No   Down    9212 9212    - accs dotq xgige

===============================================================================
 Ports on Satellite esat-2
===============================================================================
Port          Admin Link Port    Cfg  Oper LAG/ Port Port Port   C/QS/S/XFP/
Id            State      State   MTU  MTU  Bndl Mode Encp Type   MDIMDX
-------------------------------------------------------------------------------
esat-2/1/1    Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/2    Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/3    Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/4    Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/5    Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/6    Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/7    Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/8    Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/9    Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/10   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/11   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/12   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/13   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/14   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/15   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/16   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/17   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/18   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/19   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/20   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/21   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/22   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/23   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/24   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/25   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/26   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/27   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/28   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/29   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/30   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/31   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/32   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/33   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/34   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/35   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/36   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/37   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/38   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/39   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/40   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/41   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/42   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/43   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/44   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/45   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/46   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/47   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/48   Down  No   Ghost   9208 9208    - netw null xcme
esat-2/1/u1   Up    No   Ghost   9212 9212    - accs dotq xgige
esat-2/1/u2   Up    No   Ghost   9212 9212    - accs dotq xgige
esat-2/1/u3   Up    No   Ghost   9212 9212    - accs dotq xgige
esat-2/1/u4   Up    No   Ghost   9212 9212    - accs dotq xgige

===============================================================================
 Ports on Slot 10
===============================================================================
Port          Admin Link Port    Cfg  Oper LAG/ Port Port Port   C/QS/S/XFP/
Id            State      State   MTU  MTU  Bndl Mode Encp Type   MDIMDX
-------------------------------------------------------------------------------
10/2/c1       Up         Link Up                          conn   100GBASE-LR4*
10/2/c1/1     Up    Yes  Up      9192 9192   10 accs null cgige
10/2/c2       Up         Link Up                          conn   100GBASE-LR4*
10/2/c2/1     Up    Yes  Up      9192 9192   10 accs null cgige
10/2/c3       Up         Link Up                          conn   100GBASE-LR4*
10/2/c3/1     Up    Yes  Up      9192 9192   10 accs null cgige
10/2/c4       Down       Down                             conn   100GBASE-LR4*
10/2/c5       Down       Down                             conn
10/2/c6       Down       Down                             conn
10/2/c7       Up         Link Up                          conn   100GBASE-LR4*
10/2/c7/1     Up    Yes  Up      9192 9192   15 accs null cgige
10/2/c8       Up         Link Up                          conn   100GBASE-LR4*
10/2/c8/1     Up    Yes  Up      9192 9192   30 accs null cgige
10/2/c9       Down       Down                             conn   100GBASE-LR4*
10/2/c10      Up         Link Up                          conn   100GBASE-LR4*
10/2/c10/1    Up    Yes  Up      9192 9192   24 accs null cgige
10/2/c11      Down       Down                             conn
10/2/c12      Down       Down                             conn
10/2/c13      Up         Link Up                          conn   100GBASE-LR4*
10/2/c13/1    Up    Yes  Up      9192 9192   14 accs null cgige
10/2/c14      Up         Link Up                          conn   100GBASE-LR4*
10/2/c14/1    Up    Yes  Link Up 9192 9192   14 accs null cgige
10/2/c15      Up         Link Up                          conn   100GBASE-LR4*
10/2/c15/1    Down  No   Down    9192 9192    - accs null cgige
10/2/c16      Down       Down                             conn   100GBASE-LR4*
10/2/c17      Down       Down                             conn
10/2/c18      Down       Down                             conn
10/2/c19      Up         Link Up                          conn   100GBASE-LR4*
10/2/c19/1    Up    Yes  Up      9212 9212    7 netw null cgige
10/2/c20      Up         Link Up                          conn   100GBASE-LR4*
10/2/c20/1    Up    Yes  Up      9212 9212    3 netw null cgige
10/2/c21      Up         Link Up                          conn   100GBASE-LR4*
10/2/c21/1    Up    Yes  Up      9212 9212    7 netw null cgige
10/2/c22      Down       Down                             conn
10/2/c23      Down       Down                             conn
10/2/c24      Down       Down                             conn
===============================================================================
 * indicates that the corresponding row element may have been truncated.


```

**Help:** execute the command "show port"

**Prompt:**
- alcatel_sros>
- alcatel_sros#

### show router ospf interface

**Output:**
```
===============================================================================
 Rtr Base OSPFv2 Instance 0 Interfaces
===============================================================================
 If Name               Area Id         Designated Rtr  Bkup Desig Rtr  Adm  Oper
-------------------------------------------------------------------------------
system                0.0.0.0         10.10.10.3      0.0.0.0         Up   DR
TO_IOSXR              0.0.0.0         0.0.0.0         0.0.0.0         Up   PToP
TO_R1                 0.0.0.0         0.0.0.0         0.0.0.0         Up   PToP
TO_R4                 0.0.0.0         0.0.0.0         0.0.0.0         Up   PToP
 -------------------------------------------------------------------------------
 No. of OSPF Interfaces: 4
===============================================================================

```

**Help:** execute the command "show router ospf interface"

**Prompt:**
- alcatel_sros>
- alcatel_sros#

### environment no more

**Output:** None

**Help:** Execute the command environment no more. This automatically generated. Feel free to change it!

**Prompt:**
- alcatel_sros>
- alcatel_sros#

### //environment more false

**Output:** None

**Help:** Execute the command //environment more false. This automatically generated. Feel free to change it!

**Prompt:**
- alcatel_sros>
- alcatel_sros#

