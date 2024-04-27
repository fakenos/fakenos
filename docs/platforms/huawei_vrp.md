# huawei_vrp


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
- huawei_vrp>

### display arp brief

**Output:**
```
IP ADDRESS      MAC ADDRESS    EXPIRE(M) TYPE  INTERFACE           VLAN/CEVLAN  
------------------------------------------------------------------------------  
192.168.120.251 60de-4474-9640           I -   Vlanif1                          
192.168.120.1   7054-f5df-9b40 3         D-0   GE0/0/0                1/-       
192.168.120.252 04f9-3895-8300 19        D-0   GE0/0/0                1/-       
------------------------------------------------------------------------------  
Total:3         Dynamic:2       Static:0     Interface:1  

```

**Help:** execute the command "display arp brief"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display ip vpn-instance interface

**Output:**
```
 Total VPN-Instances configured      : 3

 VPN-Instance Name and ID : cftv, 1
  Interface Number : 3 
  Interface list : Vlanif1823, 
                   Vlanif1847, 
                   LoopBack5

 VPN-Instance Name and ID : met, 2
  Interface Number : 5 
  Interface list : 40GE0/0/3, 
                   Vlanif1774, 
                   Vlanif1797, 
                   LoopBack2, 
                   Vlanif1769

 VPN-Instance Name and ID : tel, 3
  Interface Number : 4 
  Interface list : Vlanif755, 
                   Vlanif773, 
                   Vlanif797, 
                   LoopBack1

```

**Help:** execute the command "display ip vpn-instance interface"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display version

**Output:**
```
Huawei Versatile Routing Platform Software
VRP (R) software, Version 8.180 (ATN 910C-B V300R003C10SPC500)
Copyright (C) 2012-2018 Huawei Technologies Co., Ltd.
HUAWEI ATN 910C-B uptime is 358 days, 16 hours, 59 minutes

ATN 910C-B version information:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CXP version information:

CXP (Master) 2  : uptime is 358 days, 16 hours, 58 minutes
  StartupTime   2019/02/24   17:20:13
  SDRAM Memory Size   : 4096M bytes
  FLASH Memory Size   : 64M bytes
  CFCARD Memory Size  : 800M bytes
  CFCARD2 Memory Size : 800M bytes
  ANGMHSTA0211 version information
  PCB         Version : ANG1CXPH REV A
  EPLD        Version : V120
  FPGA1       Version : V110
  PE          Version : 000
  BootROM     Version : 08.84
  BootLoad    Version : 08.84
  Software    Version : Version 8.180 RELEASE 0001
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PWR version information:

PWR5's  version information:
  PCB         Version : ES5MPSD17 REV D

PWR6's  version information:
  PCB         Version : ES5MPSD17 REV D
```

**Help:** execute the command "display version"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display interface description

**Output:**
```
PHY: Physical
*down: administratively down
#down: LBDT down
(l): loopback
 (s): spoofing
(E): E-Trunk down
(b): BFD down
(e): ETHOAM down
(dl): DLDP down
(lb): LBDT block
Interface                     PHY     Protocol Description
GE0/0/1                       up      up       <C4> work - station 1
GE0/0/2                       up      up       <C4> work - station 1
GE0/0/3                       up      up       <C4> work - station 1
GE0/0/4                       up      up       <C4> work - station 1
GE0/0/5                       up      up       <C4> work - station 1
GE0/0/6                       up      up       <C4> work - station 1
GE0/0/7                       up      up       <C4> work - station 1
GE0/0/8                       up      up       <C4> work - station 1
GE0/0/9                       up      up       <C4> work - station 1
GE0/0/10                      up      up       <C4> work - station 1
GE0/0/11                      up      up       <C4> work - station 1
GE0/0/12                      up      up       <C4> work - station 1
GE0/0/13                      up      up       <C4> work - station 1
GE0/0/14                      up      up       <C4> work - station 1
GE0/0/15                      up      up       <C4> work - station 1
GE0/0/16                      down    down     <C4> work - station 1
GE0/0/17                      up      up       <C4> work - station 1
GE0/0/18                      up      up       <C4> work - station 1
GE0/0/19                      down    down     <C4> work - station 1
GE0/0/20                      up      up       <C4> work - station 1
GE0/0/21                      down    down     <C4> work - station 1
GE0/0/22                      up      up       <C4> work - station 1
GE0/0/23                      up      up       <C4> work - station 1
GE0/0/24                      up      up       <C4> work - station 1
GE0/0/25                      *down   down
GE0/0/26                      *down   down
GE0/0/27                      up      up       spine Uplink
GE0/0/28                      up      up       spine Uplink 2
NULL0                         up      up(s)
Vlanif1                       up      up
```

**Help:** execute the command "display interface description"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display interface brief

**Output:**
```
PHY: Physical
*down: administratively down
^down: standby
(l): loopback
 (s): spoofing
(E): E-Trunk down
(b): BFD down
(B): Bit-error-detection down
 (e): ETHOAM down
(d): Dampening Suppressed
InUti/OutUti: input utility/output utility
Interface                   PHY   Protocol  InUti OutUti   inErrors  outErrors
Aux0/0/1                    down  down         0%     0%          0          0
Eth-Trunk2                  up    up           0%  0.38%          0          0
  GigabitEthernet8/1/16     up    up           0%  0.04%          0          0
  GigabitEthernet8/1/17     up    up           0%  1.66%          0          0
  GigabitEthernet8/1/18     up    up           0%  0.01%          0          0
  GigabitEthernet8/1/19     up    up           0%     0%          0          0
  GigabitEthernet8/1/20     up    up           0%  0.47%          0          0
Eth-Trunk3                  up    up           0%     0%          0          0
  GigabitEthernet8/1/21     up    up           0%     0%          0          0
  GigabitEthernet8/1/22     up    up           0%     0%          0          0
  GigabitEthernet8/1/23     up    up        0.01%  0.01%          0          0
Eth-Trunk4                  up    down      0.69% 13.57%       4625          0
  GigabitEthernet15/1/0(10G) up    up        0.69% 14.30%          0          0
  GigabitEthernet16/0/1(10G) up    up        0.71% 12.84%       4625          0
Eth-Trunk4.10               up    up        0.69% 13.57%          0          0
Eth-Trunk5                  up    down      0.01%     0%          0          0
  GigabitEthernet4/0/4(10G) up    up        0.01%     0%          0          0
Eth-Trunk5.100              up    up           0%     0%          0          0

```

**Help:** execute the command "display interface brief"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display port vlan

**Output:**
```
Port                        Link Type    PVID  Trunk VLAN List
-------------------------------------------------------------------------------
GigabitEthernet0/0/1        trunk        1     1 191 212 214 218 224 238
                                               250-255 300-301 303 306 330
                                               332-333 335 350 400 450 999
GigabitEthernet0/0/2        trunk        1     1 191 212 214 218 224 238
                                               250-255 300-301 303 306 330
                                               332-333 335 350 400 450 999
GigabitEthernet0/0/3        trunk        1     1 191 212 214 218 224 238
                                               250-255 300-301 303 306 330
                                               332-333 335 350 400 450 999
GigabitEthernet0/0/4        trunk        1     1 191 212 214 218 224 238
                                               250-255 300-301 303 306 330
                                               332-333 335 350 400 450 999
GigabitEthernet0/0/5        trunk        1     1 191 212 214 218 224 238
                                               250-255 300-301 303 306 330
                                               332-333 335 350 400 450 999
GigabitEthernet0/0/6        trunk        1     1 191 212 214 218 224 238
                                               250-255 300-301 303 306 330
                                               332-333 335 350 400 450 999
GigabitEthernet0/0/7        trunk        1     1 191 212 214 218 224 238
                                               250-255 300-301 303 306 330
                                               332-333 335 350 400 450 999
GigabitEthernet0/0/8        trunk        1     1 191 212 214 218 224 238
                                               250-255 300-301 303 306 330
                                               332-333 335 350 400 450 999
GigabitEthernet0/0/9        trunk        1     1 191 212 214 218 224 238
                                               250-255 300-301 303 306 330
                                               332-333 335 350 400 450 999
GigabitEthernet0/0/10       trunk        1     1 191 212 214 218 224 238
                                               250-255 300-301 303 306 330
                                               332-333 335 350 400 450 999
GigabitEthernet0/0/11       trunk        1     1 191 212 214 218 224 238
                                               250-255 300-301 303 306 330
                                               332-333 335 350 400 450 999
GigabitEthernet0/0/12       trunk        1     1 191 212 214 218 224 238
                                               250-255 300-301 303 306 330
                                               332-333 335 350 400 450 999
GigabitEthernet0/0/13       access       2     -
GigabitEthernet0/0/14       access       2     -
GigabitEthernet0/0/15       hybrid       1     2
GigabitEthernet0/0/16       hybrid       69    2
GigabitEthernet0/0/17       access       160   -
GigabitEthernet0/0/18       access       160   -
GigabitEthernet0/0/19       access       160   -
GigabitEthernet0/0/20       access       160   -
GigabitEthernet0/0/21       access       160   -
GigabitEthernet0/0/22       hybrid       1     2
GigabitEthernet0/0/23       hybrid       1     2
GigabitEthernet0/0/24       hybrid       1     2
GigabitEthernet0/0/25       auto         1     1-4094
GigabitEthernet0/0/26       auto         1     1-4094
GigabitEthernet0/0/27       trunk        1     1-4094
GigabitEthernet0/0/28       trunk        1     1-4094

```

**Help:** execute the command "display port vlan"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display ipv6 neighbors

**Output:**
```
-----------------------------------------------------------------------------
 IPv6 Address : FC00:1::2
Link-layer   : 0025-9e01-020a                     State   : STALE
Interface    : 10GE4/17/6                          Age     : 75
VLAN         : 35                                 CEVLAN  : -
VPN name     : -                                  Is Router: TRUE
Secure FLAG  : UNSECURE                           Nickname  : -

IPv6 Address : FE80::225:9EFF:FE01:20A
Link-layer   : 0025-9e01-020a                     State   : STALE
Interface    : 10GE4/17/6                          Age     : 38
VLAN         : 35                                 CEVLAN  : -
VPN name     : -                                  Is Router: TRUE
Secure FLAG  : UNSECURE                           Nickname  : -

IPv6 Address : FC00:2::1
Link-layer   : 0023-0045-0067                     State   : INCMP
Interface    : 10GE4/17/3                          Age     : -
VLAN         : -                                  CEVLAN  : -
VPN name     : -                                  Is Router: TRUE
Secure FLAG  : SECURE                             Nickname  : -

-----------------------------------------------------------------------------
 Total: 3        Dynamic: 2      Static: 1

```

**Help:** execute the command "display ipv6 neighbors"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display service-set id id

**Output:**
```
  ----------------------------------------------------------------------------
  Service-set ID                   : 1
  Service-Set name                 : Livebox_5ad8__5G
  SSID                             : Livebox_5ad8
  Hide SSID                        : disable
  User isolate                     : disable
  Type                             : service
  Maximum number of user           : 32
  Association timeout(min)         : 5
  Traffic profile name             : traf
  Security profile name            : Security_Livebox_5ad8
  Wlan-bss interface               : Wlan-bss7
  Igmp mode                        : off
  Forward mode                     : direct-forward
  ----------------------------------------------------------------------------

```

**Help:** execute the command "display service-set id id"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display traffic-filter applied-record

**Output:**
```
-----------------------------------------------------------
Interface                   Direction  AppliedRecord       
-----------------------------------------------------------
Vlanif1                     inbound    acl name ACL_Test
Vlanif1                     outbound   ipv6 acl name MyACL_IPv6
Vlanif3                     inbound    acl 3998
Vlanif3                     inbound    ipv6 acl name MyACL_IPv6
Wlan-Bss0                   outbound   IPv4 ACL 4000
Wlan-Bss1                   outbound   IPv4 ACL 4000
-----------------------------------------------------------             
Total:6                                                                         
-----------------------------------------------------------             
Traffic profile             Direction  AppliedRecord                    
-----------------------------------------------------------             
p1                          inbound    IPv4 ACL 3000                         
p2                          outbound   IPv6 ACL 3001                    
-----------------------------------------------------------             
Total:2 

```

**Help:** execute the command "display traffic-filter applied-record"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display acl all

**Output:**
```
 Total quantity of nonempty ACL number is 3 

Basic ACL 2000, 7 rules
Acl's step is 5
 rule 5 permit source 85.14.167.234 0 (94 matches)
 rule 10 permit source 85.14.167.193 0 (26939 matches)
 rule 15 permit source 5.10.130.152 0.0.0.3 (24 matches)
 rule 20 permit source 185.48.254.19 0 
 rule 25 permit source 10.0.0.0 0.255.255.255 
 rule 30 permit source 172.0.0.0 0.15.255.255 
 rule 35 permit source 192.168.0.0 0.0.255.255 

Basic ACL 2500, 1 rule
Acl's step is 5
 rule 35 permit source 192.168.0.0 0.0.255.255 (5431 matches)
 
Advanced ACL 3997, 1 rule
Acl's step is 5
 rule 5 permit ip source 192.165.3.5 0 
 rule 5 description "qsdqsdqsdqsdqsdqsdqs az"

Advanced ACL REGLE_NAT 3998, 3 rules
Acl's step is 5
 rule 5 permit tcp source 85.14.167.234 0 destination 192.214.198.156 0 destination-port eq 8022 (18 matches)
 rule 10 deny tcp destination 192.214.198.156 0 destination-port eq www (8 matches)
 rule 15 deny tcp destination 192.23.26.1 0.0.255.255 destination-port range 50 80 (8 matches)
 rule 20 permit ip (278450 matches)

Advanced ACL qsdqsd 3999, 0 rule
Acl's step is 5

```

**Help:** execute the command "display acl all"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display arp all

**Output:**
```
IP ADDRESS      MAC ADDRESS     EXPIRE(M) TYPE        INTERFACE   VPN-INSTANCE
                                    VLAN/CEVLAN(SIP/DIP)
------------------------------------------------------------------------------
192.168.1.253   b076-1b65-6a40            I -         MEth0/0/1
10.10.10.1      b076-1b65-6a4b            I -         Vlanif10
10.10.10.2      b8d6-f6ff-739b  17        D-0         XGE0/0/1
                                            10/-
10.10.20.1      b076-1b65-6a46            I -         Vlanif20
10.10.20.2      b8d6-f6ff-7396  17        D-0         XGE0/0/1
                                            20/-
------------------------------------------------------------------------------
Total:5         Dynamic:2       Static:0     Interface:3

```

**Help:** execute the command "display arp all"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display ip routing-table verbose

**Output:**
```
Routing Table : Public
	Destinations : 1	Routes : 1

 Destination  : ::1                             PrefixLength : 128
 NextHop      : ::1                             Preference   : 0
 Neighbour    : ::                              ProcessID    : 0
 Label        : NULL                            Protocol     : Direct
 State        : Active NoAdv                    Cost         : 0
 Entry ID     : 2826122436                      EntryFlags   : 0x80010050
 Reference Cnt: 2                               Tag          : 0
 Priority     : high                            Age          : 93545sec
 IndirectID   : 0x0                             
 RelayNextHop : ::                              TunnelID     : 0x0
 Interface    : InLoopBack0                     Flags        : D

```

**Help:** execute the command "display ip routing-table verbose"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display ip vpn-instance

**Output:**
```
 Total VPN-Instances configured      : 1
 Total IPv4 VPN-Instances configured : 1
 Total IPv6 VPN-Instances configured : 1

  VPN-Instance Name               RD                    Address-family
  red                             1:2                   IPv4
  red                             1:2                   IPv6

```

**Help:** execute the command "display ip vpn-instance"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display lldp neighbor

**Output:**
```
XGigabitEthernet0/0/1 has 1 neighbor(s):

Neighbor index :1
Chassis type   :MAC address
Chassis ID     :b8d6-f6ff-7390
Port ID type   :Interface name
Port ID        :XGigabitEthernet0/0/2
Port description    :XGigabitEthernet0/0/2
 System name         :ROUTER2
System description  :Huawei Switch S6730-S24X6Q
 Huawei Versatile Routing Platform Software
VRP (R) software, Version 5.170 (S6730 V200R022C00SPC500)
Copyright (C) 2000-2022 HUAWEI TECH Co., Ltd.
System capabilities supported   :bridge router
System capabilities enabled     :bridge router
Management address type  :ipv4
Management address value :169.254.1.2
OID  :0.6.15.43.6.1.4.1.2011.5.25.41.1.2.1.1.1.
Expired time   :95s

Port VLAN ID(PVID)  :10
VLAN name of VLAN  1:VLAN 0001

Auto-negotiation supported    :Yes
Auto-negotiation enabled      :Yes
OperMau   :speed(1000)/duplex(Full)
 
Power port class            :PD
PSE power supported         :No
PSE power enabled           :No
PSE pairs control ability   :No
Power pairs                 :Unknown
Port power classification   :Unknown

Link aggregation supported:Yes
Link aggregation enabled :No
Aggregation port ID      :0

 Maximum frame Size       :9216

```

**Help:** execute the command "display lldp neighbor"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display nat server

**Output:**
```
  Nat Server Information:
  Interface  : Dialer1
    Global IP/Port     : current-interface/8080 (Real IP : 192.214.198.156)
    Inside IP/Port     : 192.168.1.24/80(www)
    Protocol : 6(tcp)   
    VPN instance-name  : ----                            
    Acl number         : 2600
    Vrrp id            : ----
    Description : ----

    Global IP/Port     : current-interface/8080 (Real IP : 192.214.198.156)
    Inside IP/Port     : 192.168.1.24/80
    Protocol : 17(udp)  
    VPN instance-name  : ----                            
    Acl number         : 2600
    Vrrp id            : ----
    Description : ----

  Interface  : Vlanif300                                                                                                            
    Global IP/Port     : current-interface/0(any) (Real IP : 2.2.2.2)
    Inside IP/Port     : 10.1.1.1/0(any)
    Protocol : 6(tcp)
    VPN instance-name  : ----
    Acl number         : ----
    Vrrp id            : ----
    Description : ----

  Total :    3

```

**Help:** execute the command "display nat server"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display isis peer

**Output:**
```
                          Peer information for ISIS(1)

  System Id     Interface          Circuit Id        State HoldTime Type     PRI
--------------------------------------------------------------------------------
MA-JK4961-01H   Eth-Trunk2         0000000087         Up   25s      L2       --
PAG-JK1401-01H  Eth-Trunk0         0000000146         Up   29s      L2       --

Total Peer(s): 2

```

**Help:** execute the command "display isis peer"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display temperature

**Output:**
```
SlotID2 :
 Base-Board, Unit:C, Slot2
PCB       I2C Addr Chl  Status  Minor Major Fatal Adj_speed Temp
                                               TMin Tmax (C)
---------------------------------------------------------------
LPUF41A   0   0    0    NORMAL  68    76    83    55   65   38
LPUF41A   0   1    0    NORMAL  63    71    78    50   60   36
LPUF41A   0   2    0    NORMAL  69    77    85    56   66   28
LPUF41A   7   175  0    NORMAL  89    94    105   76   86   55
LPUF41A   7   175  1    NORMAL  89    94    105   76   86   37
LPUF41A   7   175  2    NORMAL  89    94    105   76   86   41
EFGF      2   73   0    NORMAL  77    83    92    64   74   30
EFGF      3   73   0    NORMAL  77    83    92    64   74   36

SlotID25 :
 
SlotID26 :

SlotID27 :
 Base-Board, Unit:C, SlotID27
PCB   I2C Addr Chl  Status  Minor Major Fatal Adj_speed Temp
                                              TMin Tmax (C)
-----------------------------------------------------------------
FAN   1   0    0    NORMAL  70    80    95    32   45   25



SlotID31 : No temp sensors.

```

**Help:** execute the command "display temperature"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display sn license

**Output:**
```
 ESN of device: 21500104792SM8504636

```

**Help:** execute the command "display sn license"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display service-set all

**Output:**
```
  ----------------------------------------------------------------------------
  ID      Name                            SSID
  0       Livebox_5ad8                    Livebox_5ad8                     
  1       Livebox_5ad8__5G                Livebox_5ad8                     
  2       Profile_my_guest_wifi           my_guest_wifi                    
  ----------------------------------------------------------------------------
  Total: 3

```

**Help:** execute the command "display service-set all"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display startup

**Output:**
```
MainBoard: 
  Startup system software:                   flash:/AR610-V300R021C00SPC200.cc
  Next startup system software:              flash:/AR610-V300R021C00SPC200.cc
  Backup system software for next startup:   null
  Startup saved-configuration file:          flash:/vrpcfg.zip
  Next startup saved-configuration file:     flash:/vrpcfg2.zip
  Startup license file:                      null
  Next startup license file:                 null
  Startup patch package:                     flash:/AR610_V300R021SPH180.pat
  Next startup patch package:                flash:/AR610_V300R021SPH180.pat
  Startup voice-files:                       null
  Next startup voice-files:                  null

```

**Help:** execute the command "display startup"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display vlan

**Output:**
```
The total number of VLANs is: 3
--------------------------------------------------------------------------------
 U: Up;         D: Down;         TG: Tagged;         UT: Untagged;
MP: Vlan-mapping;               ST: Vlan-stacking;
#: ProtocolTransparent-vlan;    *: Management-vlan;
--------------------------------------------------------------------------------

VID  Type    Ports
--------------------------------------------------------------------------------
1    common  UT:XGE0/0/1(D)     XGE0/0/2(D)     XGE0/0/3(D)     XGE0/0/4(D)
                XGE0/0/5(D)     XGE0/0/6(D)
             TG:40GE0/0/1(D)    40GE0/0/2(D)    40GE0/0/3(D)    40GE0/0/4(D)
                40GE0/0/5(D)    40GE0/0/6(D)
10   common  UT:XGE0/0/7(D)     XGE0/0/8(D)     XGE0/0/9(D)     XGE0/0/10(D)
                XGE0/0/11(D)    XGE0/0/12(D)
20   common  TG:40GE0/0/1(D)    40GE0/0/2(D)    40GE0/0/3(D)    40GE0/0/4(D)
                40GE0/0/5(D)    40GE0/0/6(D)
30   common  UT:XGE0/0/13(D)    XGE0/0/142(D)   XGE0/0/15(D)    XGE0/0/16(D)
                XGE0/0/17(D)    XGE0/0/18(D)
             TG:40GE0/0/1(D)    40GE0/0/2(D)    40GE0/0/3(D)    40GE0/0/4(D)
                40GE0/0/5(D)    40GE0/0/6(D)

VID  Status  Property      MAC-LRN Statistics Description
--------------------------------------------------------------------------------
1    enable  default       enable  disable    VLAN 0001
10   enable  default       enable  disable    VLAN 0010
20   enable  default       enable  disable    VLAN 0020
30   enable  default       enable  disable    VLAN 0030

```

**Help:** execute the command "display vlan"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display interface

**Output:**
```
GigabitEthernet0/0/0 current state : DOWN
Line protocol current state : DOWN
Description:HUAWEI, AR Series, GigabitEthernet0/0/0 Interface
Switch Port, PVID :    1, TPID : 8100(Hex), The Maximum Frame Length is 9596
IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is fc73-fb9e-601c
Last physical up time   : -
Last physical down time : 2022-10-13 09:35:55
Current system time: 2022-10-13 13:12:02
Port Mode: COMMON COPPER
Speed :   10,  Loopback: NONE
Duplex: FULL,  Negotiation: DISABLE
Mdi   : AUTO,  Clock   : -
Last 300 seconds input rate 0 bits/sec, 0 packets/sec
Last 300 seconds output rate 0 bits/sec, 0 packets/sec
Input peak rate 0 bits/sec,Record time: -
Output peak rate 0 bits/sec,Record time: -

Input:  0 packets, 0 bytes
  Unicast:                  0,  Multicast:                   0
  Broadcast:                0,  Jumbo:                       -
  Discard:                  0,  Total Error:                 0

  CRC:                      0,  Giants:                      0
  Jabbers:                  0,  Throttles:                   0
  Runts:                    0,  Symbols:                     0
  Ignoreds:                 0,  Frames:                      0

Output:  0 packets, 0 bytes
  Unicast:                  0,  Multicast:                   0
  Broadcast:                0,  Jumbo:                       -
  Discard:                  0,  Total Error:                 0

  Collisions:               0,  ExcessiveCollisions:         0
  Late Collisions:          0,  Deferreds:                   0

    Input bandwidth utilization threshold : 100.00%
    Output bandwidth utilization threshold: 100.00%
    Input bandwidth utilization  :    0%
    Output bandwidth utilization :    0%

GigabitEthernet0/0/1 current state : DOWN
Line protocol current state : DOWN
Description:HUAWEI, AR Series, GigabitEthernet0/0/1 Interface
 Switch Port, PVID :    2, TPID : 8100(Hex), The Maximum Frame Length is 9596
 IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is fc73-fb9e-601c
 Last physical up time   : -
Last physical down time : 2022-10-13 09:35:55
 Current system time: 2022-10-13 13:12:04
Port Mode: COMMON COPPER
Speed : 1000,  Loopback: NONE
Duplex: FULL,  Negotiation: ENABLE        
Mdi   : AUTO,  Clock   : -
Last 300 seconds input rate 0 bits/sec, 0 packets/sec
Last 300 seconds output rate 0 bits/sec, 0 packets/sec
Input peak rate 0 bits/sec,Record time: -
Output peak rate 0 bits/sec,Record time: -

Input:  0 packets, 0 bytes
  Unicast:                  0,  Multicast:                   0
  Broadcast:                0,  Jumbo:                       -
  Discard:                  0,  Total Error:                 0

  CRC:                      0,  Giants:                      0
  Jabbers:                  0,  Throttles:                   0
  Runts:                    0,  Symbols:                     0
  Ignoreds:                 0,  Frames:                      0

Output:  0 packets, 0 bytes
  Unicast:                  0,  Multicast:                   0
  Broadcast:                0,  Jumbo:                       -
  Discard:                  0,  Total Error:                 0

  Collisions:               0,  ExcessiveCollisions:         0
  Late Collisions:          0,  Deferreds:                   0

    Input bandwidth utilization threshold : 100.00%
    Output bandwidth utilization threshold: 100.00%
    Input bandwidth utilization  :    0%
    Output bandwidth utilization :    0%

GigabitEthernet0/0/2 current state : UP
Line protocol current state : UP
Description:HUAWEI, AR Series, GigabitEthernet0/0/2 Interface
Switch Port, PVID :  100, TPID : 8100(Hex), The Maximum Frame Length is 9596
IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is fc73-fb9e-601c
Last physical up time   : 2022-10-13 09:37:04
Last physical down time : 2022-10-13 09:37:03
 Current system time: 2022-10-13 13:12:05
Port Mode: COMMON COPPER
Speed : 1000,  Loopback: PHY
Duplex: FULL,  Negotiation: ENABLE
Mdi   : AUTO,  Clock   : -
Last 300 seconds input rate 488 bits/sec, 0 packets/sec
Last 300 seconds output rate 488 bits/sec, 0 packets/sec
Input peak rate 592 bits/sec,Record time: 2022-10-13 10:26:22
Output peak rate 592 bits/sec,Record time: 2022-10-13 10:26:22

Input:  6460 packets, 768740 bytes
  Unicast:                  0,  Multicast:                6460
  Broadcast:                0,  Jumbo:                       -
  Discard:                  0,  Total Error:                 0

  CRC:                      0,  Giants:                      0
  Jabbers:                  0,  Throttles:                   0
  Runts:                    0,  Symbols:                     0
  Ignoreds:                 0,  Frames:                      0

Output:  6460 packets, 768740 bytes
  Unicast:                  0,  Multicast:                6460
  Broadcast:                0,  Jumbo:                       -
  Discard:                  0,  Total Error:                 0

  Collisions:               0,  ExcessiveCollisions:         0
  Late Collisions:          0,  Deferreds:                   0

    Input bandwidth utilization threshold : 100.00%
    Output bandwidth utilization threshold: 100.00%
    Input bandwidth utilization  : 0.01%
    Output bandwidth utilization : 0.01%

GigabitEthernet0/0/3 current state : DOWN
Line protocol current state : DOWN
Description:HUAWEI, AR Series, GigabitEthernet0/0/3 Interface
Switch Port, PVID :    1, TPID : 8100(Hex), The Maximum Frame Length is 9596
IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is fc73-fb9e-601c
Last physical up time   : -               
Last physical down time : 2022-10-13 09:35:55
Current system time: 2022-10-13 13:12:06
Port Mode: COMMON COPPER
Speed : 1000,  Loopback: NONE
Duplex: FULL,  Negotiation: ENABLE
Mdi   : AUTO,  Clock   : -
Last 300 seconds input rate 0 bits/sec, 0 packets/sec
Last 300 seconds output rate 0 bits/sec, 0 packets/sec
 Input peak rate 0 bits/sec,Record time: -
Output peak rate 0 bits/sec,Record time: -

Input:  0 packets, 0 bytes
  Unicast:                  0,  Multicast:                   0
  Broadcast:                0,  Jumbo:                       -
  Discard:                  0,  Total Error:                 0

  CRC:                      0,  Giants:                      0
  Jabbers:                  0,  Throttles:                   0
  Runts:                    0,  Symbols:                     0
  Ignoreds:                 0,  Frames:                      0

Output:  0 packets, 0 bytes
  Unicast:                  0,  Multicast:                   0
  Broadcast:                0,  Jumbo:                       -
  Discard:                  0,  Total Error:                 0

  Collisions:               0,  ExcessiveCollisions:         0
  Late Collisions:          0,  Deferreds:                   0

    Input bandwidth utilization threshold : 100.00%
    Output bandwidth utilization threshold: 100.00%
    Input bandwidth utilization  :    0%
    Output bandwidth utilization :    0%

GigabitEthernet0/0/4 current state : UP
Line protocol current state : DOWN
Description:HUAWEI, AR Series, GigabitEthernet0/0/4 Interface
Route Port,The Maximum Transmit Unit is 1500
Internet protocol processing : disabled
IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is fc73-fb9e-601d
Last physical up time   : 2022-10-13 09:37:06
Last physical down time : 2022-10-13 09:35:55
Current system time: 2022-10-13 13:12:07
 Port Mode: AUTO COPPER
Speed : 1000,  Loopback: NONE
Duplex: FULL,  Negotiation: ENABLE
Mdi   : AUTO,  Clock   : -
Last 300 seconds input rate 2112 bits/sec, 3 packets/sec
Last 300 seconds output rate 1904 bits/sec, 2 packets/sec
Input peak rate 19400 bits/sec,Record time: 2022-10-13 12:55:33
Output peak rate 63040 bits/sec,Record time: 2022-10-13 12:55:33

Input:  30464 packets, 2525068 bytes
  Unicast:              21147,  Multicast:                6738
  Broadcast:             2579,  Jumbo:                       -
  Discard:                  0,  Total Error:                 0

  CRC:                      0,  Giants:                      0
  Jabbers:                  0,  Throttles:                   0
  Runts:                    0,  Symbols:                     0
  Ignoreds:                 0,  Frames:                      0

Output:  20762 packets, 2116014 bytes
  Unicast:              20761,  Multicast:                   0
  Broadcast:                1,  Jumbo:                       -
  Discard:                  0,  Total Error:                 0

  Collisions:               0,  ExcessiveCollisions:         0
  Late Collisions:          0,  Deferreds:                   0

    Input bandwidth utilization threshold : 100.00%
    Output bandwidth utilization threshold: 100.00%
    Input bandwidth utilization  : 0.01%
    Output bandwidth utilization : 0.01%
                                          
GigabitEthernet0/0/5 current state : UP
Line protocol current state : DOWN
Description:VirtualPort
Route Port,The Maximum Transmit Unit is 1500
Internet protocol processing : disabled
 IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is fc73-fb9e-601e
 Last physical up time   : 2022-10-13 09:37:05
Last physical down time : 2022-10-13 09:35:55
Current system time: 2022-10-13 13:12:08
Port Mode: COMMON COPPER
 Speed : 1000,  Loopback: NONE
Duplex: FULL,  Negotiation: ENABLE
Mdi   : AUTO,  Clock   : -
Last 300 seconds input rate 36064 bits/sec, 13 packets/sec
 Last 300 seconds output rate 0 bits/sec, 0 packets/sec
Input peak rate 121600 bits/sec,Record time: 2022-10-13 10:50:03
Output peak rate 0 bits/sec,Record time: -

Input:  1832 packets, 619216 bytes
  Unicast:                  0,  Multicast:                   0
  Broadcast:             1832,  Jumbo:                       -
  Discard:                  0,  Total Error:                 0

  CRC:                      0,  Giants:                      0
  Jabbers:                  0,  Throttles:                   0
  Runts:                    0,  Symbols:                     0
  Ignoreds:                 0,  Frames:                      0

Output:  0 packets, 0 bytes
  Unicast:                  0,  Multicast:                   0
  Broadcast:                0,  Jumbo:                       -
  Discard:                  0,  Total Error:                 0

  Collisions:               0,  ExcessiveCollisions:         0
  Late Collisions:          0,  Deferreds:                   0

    Input bandwidth utilization threshold : 100.00%
    Output bandwidth utilization threshold: 100.00%
    Input bandwidth utilization  :    0%
    Output bandwidth utilization :    0%

```

**Help:** execute the command "display interface"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display snmp-agent community read

**Output:**
```
   Community name: %^%#K[&`Jc~_4H-~.>0:m%dK:*7s,{{(3i02`R$>&n}}+56Pb'@]rd}}NT@o4.7RG'8ScPW0=d%O<1oU+7KHS[I%^%#
   Group name: %^%#K[&`Jc~_4H-~.>0:m%dK:*7s,{{(3i02`R$>&n}}+56Pb'@]rd}}NT@o4.7RG'8ScPW0=d%O<1oU+7KHS[I%^%#
   Acl: 2001
   Storage-type: nonVolatile

   Total number is 1

```

**Help:** execute the command "display snmp-agent community read"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### display mac-address

**Output:**
```
-------------------------------------------------------------------------------
 MAC Address    VLAN/VSI/BD                       Learned-From        Type
 -------------------------------------------------------------------------------
 b8d6-f6ff-7390 10/-/-                            XGE0/0/1            dynamic
 b8d6-f6ff-739b 10/-/-                            XGE0/0/1            dynamic
 
-------------------------------------------------------------------------------
 Total items displayed = 2

```

**Help:** execute the command "display mac-address"

**Prompt:**
- huawei_vrp>
- huawei_vrp#

### screen-length 0 temporary

**Output:** None

**Help:** Execute the command screen-length 0 temporary. This automatically generated. Feel free to change it!

**Prompt:**
- huawei_vrp>
- huawei_vrp#

