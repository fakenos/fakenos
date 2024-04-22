# brocade_netiron


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
- brocade_netiron>

### show interfaces

**Output:**
```
GigabitEthernet1/1 is up, line protocol is up 
  STP Root Guard is disabled, STP BPDU Guard is disabled
  Hardware is GigabitEthernet, address is 0024.38a5.1c00 (bia 0024.38a5.1c00)
  Configured speed auto, actual 1Gbit, configured duplex fdx, actual fdx
  Member of Control VLAN 4095, 36 L2 VLAN(S) (tagged), port is in tagged mode, port state is Forwarding
  STP configured to ON, Priority is level0, flow control enabled
  Priority force disabled, Drop precedence level 0, Drop precedence force disabled
  dhcp-snooping-trust configured to OFF
  mirror disabled, monitor disabled
  LACP BPDU Forwarding:Disabled 
  LLDP BPDU Forwarding:Disabled 
  Not member of any active trunks
  Not member of any configured trunks
  Port name is ATM1-G0-1
  Port is not enabled to receive all vlan packets for pbr
  MTU 9216 bytes, encapsulation ethernet
  Openflow: Disabled, Openflow Index 1
  Cluster L2 protocol forwarding enabled
  300 second input rate: 235649647 bits/sec, 27522 packets/sec, 24.00% utilization
  300 second output rate: 140641094 bits/sec, 31382 packets/sec, 14.56% utilization
  74818592872 packets input, 72400348503374 bytes, 0 no buffer
  Received 3639493 broadcasts, 2736343 multicasts, 74812217036 unicasts
  0 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 16192705827 giants                                     
  NP received 74819287581 packets, Sent to TM 74819282240 packets
  NP Ingress dropped 5369 packets
  95864830955 packets output, 54017992924883 bytes, 0 underruns
  Transmitted 2406581209 broadcasts, 82143416 multicasts, 93376106330 unicasts
  0 output errors, 0 collisions
  NP transmitted 95865699894 packets, Received from TM 95872239709 packets
GigabitEthernet1/2 is disabled, line protocol is down 
  STP Root Guard is disabled, STP BPDU Guard is disabled
  Hardware is GigabitEthernet, address is 0024.38a5.1c01 (bia 0024.38a5.1c01)
  Configured speed auto, actual unknown, configured duplex fdx, actual unknown
  Member of Control VLAN 4095, VLAN 1 (untagged), port is in untagged mode, port state is Disabled
  STP configured to ON, Priority is level0, flow control enabled
  Priority force disabled, Drop precedence level 0, Drop precedence force disabled
  dhcp-snooping-trust configured to OFF
  mirror disabled, monitor disabled
  LACP BPDU Forwarding:Disabled 
  LLDP BPDU Forwarding:Disabled 
  Not member of any active trunks
  Not member of any configured trunks
  No port name
  Port is not enabled to receive all vlan packets for pbr
  MTU 9216 bytes, encapsulation ethernet
  Openflow: Disabled, Openflow Index 2                            
  Cluster L2 protocol forwarding enabled
  300 second input rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  300 second output rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  0 packets input, 0 bytes, 0 no buffer
  Received 0 broadcasts, 0 multicasts, 0 unicasts
  0 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  NP received 0 packets, Sent to TM 0 packets
  NP Ingress dropped 0 packets
  0 packets output, 0 bytes, 0 underruns
  Transmitted 0 broadcasts, 0 multicasts, 0 unicasts
  0 output errors, 0 collisions
  NP transmitted 0 packets, Received from TM 0 packets
10GigabitEthernet3/4 is up, line protocol is up 
  STP Root Guard is disabled, STP BPDU Guard is disabled
  Hardware is 10GigabitEthernet, address is 0024.38a5.1c00 (bia 0024.38a5.1c63)
  Configured speed 10Gbit, actual 10Gbit, configured duplex fdx, actual fdx
  Member of Control VLAN 4095, 77 L2 VLAN(S) (tagged), port is in tagged mode, port state is Forwarding
  STP configured to ON, Priority is level0, flow control enabled
  Priority force disabled, Drop precedence level 0, Drop precedence force disabled
  dhcp-snooping-trust configured to OFF
  mirror disabled, monitor disabled
  LACP BPDU Forwarding:Disabled 
  LLDP BPDU Forwarding:Disabled 
  Not member of any active trunks
  Not member of any configured trunks
  Port name is OL2.CLMAMO-ten3/0/0
  Port is not enabled to receive all vlan packets for pbr
  MTU 9216 bytes, encapsulation ethernet
  Openflow: Disabled, Openflow Index 100
  Cluster L2 protocol forwarding enabled
  30 second input rate: 300338645 bits/sec, 41100 packets/sec, 3.07% utilization
  30 second output rate: 190540328 bits/sec, 39304 packets/sec, 1.97% utilization
  121863253313 packets input, 99644389312061 bytes, 0 no buffer
  Received 44852728 broadcasts, 9170942 multicasts, 121809229643 unicasts
  0 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 26930828870 giants
  NP received 121864501462 packets, Sent to TM 121862218321 packets
  NP Ingress dropped 5 packets
  145158405355 packets output, 102580338487220 bytes, 0 underruns
  Transmitted 9556629 broadcasts, 65490504 multicasts, 145083358222 unicasts
  0 output errors, 0 collisions
  NP transmitted 145159557118 packets, Received from TM 145218386173 packets
10GigabitEthernet3/5 is up, line protocol is up 
  STP Root Guard is disabled, STP BPDU Guard is disabled
  Hardware is 10GigabitEthernet, address is 0024.38a5.1c00 (bia 0024.38a5.1c64)
  Configured speed 10Gbit, actual 10Gbit, configured duplex fdx, actual fdx
  Member of Control VLAN 4095, 9 L2 VLAN(S) (tagged), port is in tagged mode, port state is Forwarding
  STP configured to ON, Priority is level0, flow control enabled
  Priority force disabled, Drop precedence level 0, Drop precedence force disabled
  dhcp-snooping-trust configured to OFF
  mirror disabled, monitor disabled
  LACP BPDU Forwarding:Disabled 
  LLDP BPDU Forwarding:Disabled 
  Member of active trunk ports 3/5, primary port
  Member of configured trunk ports 3/5, primary port
  Port name is CLMA-STLS 10G-Centurylink
  Port is not enabled to receive all vlan packets for pbr         
  MTU 9216 bytes, encapsulation ethernet
  Openflow: Disabled, Openflow Index 101
  Cluster L2 protocol forwarding enabled
  30 second input rate: 2602741516 bits/sec, 269941 packets/sec, 26.46% utilization
  30 second output rate: 262142094 bits/sec, 111277 packets/sec, 2.79% utilization
  924970842630 packets input, 1088460975408035 bytes, 0 no buffer
  Received 4575649 broadcasts, 102909425 multicasts, 924863357556 unicasts
  0 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 321137547437 giants
  NP received 924979272212 packets, Sent to TM 924677624613 packets
  NP Ingress dropped 213578234 packets
  526574341236 packets output, 159588031939808 bytes, 0 underruns
  Transmitted 121307096 broadcasts, 317528800 multicasts, 526135505340 unicasts
  0 output errors, 0 collisions
  NP transmitted 526580335261 packets, Received from TM 526680374565 packets
10GigabitEthernet3/6 is disabled, line protocol is down 
  STP Root Guard is disabled, STP BPDU Guard is disabled
  Hardware is 10GigabitEthernet, address is 0024.38a5.1c65 (bia 0024.38a5.1c65)
  Configured speed 10Gbit, actual unknown, configured duplex fdx, actual unknown
  Member of Control VLAN 4095, VLAN 1 (untagged), port is in untagged mode, port state is Disabled
  STP configured to ON, Priority is level0, flow control enabled
  Priority force disabled, Drop precedence level 0, Drop precedence force disabled
  dhcp-snooping-trust configured to OFF                           
  mirror disabled, monitor disabled
  LACP BPDU Forwarding:Disabled 
  LLDP BPDU Forwarding:Disabled 
  Not member of any active trunks
  Not member of any configured trunks
  No port name
  Port is not enabled to receive all vlan packets for pbr
  MTU 9216 bytes, encapsulation ethernet
  Openflow: Disabled, Openflow Index 102
  Cluster L2 protocol forwarding enabled
  300 second input rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  300 second output rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  0 packets input, 0 bytes, 0 no buffer
  Received 0 broadcasts, 0 multicasts, 0 unicasts
  0 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  NP received 0 packets, Sent to TM 0 packets
  NP Ingress dropped 0 packets
  0 packets output, 0 bytes, 0 underruns
  Transmitted 0 broadcasts, 0 multicasts, 0 unicasts
  0 output errors, 0 collisions
  NP transmitted 0 packets, Received from TM 0 packets
Ve1395 is up, line protocol is up 
  Type is Vlan (Vlan Id: 1395)
  Hardware is Virtual Ethernet, address is 0024.38a5.1c00 (bia 0024.38a5.1c00)
  Port name is TA5000A.CLMAMOXI-PON-VOICE 
  Vlan id: 1395
  Internet address is 172.24.18.1/24, IP MTU 1500 bytes, encapsulation ethernet
Ve1400 is up, line protocol is down 
  Type is Vlan (Vlan Id: 1400)
  Hardware is Virtual Ethernet, address is 0024.38a5.1c00 (bia 0024.38a5.1c00)
  No port name
  Vlan id: 1400
  Internet address is 0.0.0.0/0, IP MTU 1500 bytes, encapsulation ethernet
Loopback1 is up, line protocol is up 
  Hardware is Loopback
  Port name is MPLS Loopback
  Internet address is 174.34.31.29/32, IP MTU 1500 bytes, encapsulation LOOPBACK
Loopback6 is up, line protocol is up 
  Hardware is Loopback
  No port name
  IP MTU 1500 bytes, encapsulation LOOPBACK
```

**Help:** execute the command "show interfaces"

**Prompt:**
- brocade_netiron>
- brocade_netiron#

### show lldp neighbors detail

**Output:**
```
Total number of LLDP neighbors on all ports: 38
Local port: 1/1
  Neighbor: 0012.f2f0.2377, TTL 101 seconds
    + Chassis ID (MAC address): 0012.f2f0.2360
    + Port ID (MAC address): 0012.f2f0.2377
    + Time to live: 120 seconds
    + System name         : "switch1d.clmamofw"
    + Port description    : "GigabitEthernet24"
    + System capabilities : bridge
      Enabled capabilities: bridge
    + 802.3 MAC/PHY          : auto-negotiation enabled
      Advertised capabilities: 10BaseT-HD, 10BaseT-FD, 100BaseTX-HD,
                               100BaseTX-FD, fdxSPause, fdxBPause,
                               1000BaseT-HD, 1000BaseT-FD
      Operational MAU type   : 1000BaseT-FD
    + Link aggregation: aggregated (aggregated port ifIndex: 0)
    + Maximum frame size: 10240 octets
    + Port VLAN ID: 1
    + Management address (IPv4): 10.255.1.49

Local port: 1/5
  Neighbor: 001b.ed6b.6304, TTL 97 seconds
    + Chassis ID (MAC address): 001b.ed6b.6300
    + Port ID (MAC address): 001b.ed6b.6304                       
    + Time to live: 120 seconds
    + System name         : "switch1e.clmamofw"
    + Port description    : "GigabitEthernet5"
    + System capabilities : bridge
      Enabled capabilities: bridge
    + 802.3 MAC/PHY          : auto-negotiation enabled
      Advertised capabilities: 10BaseT-HD, 10BaseT-FD, 100BaseTX-HD,
                               100BaseTX-FD, fdxSPause, fdxBPause,
                               1000BaseT-HD, 1000BaseT-FD
      Operational MAU type   : 1000BaseT-FD
    + Link aggregation: aggregated (aggregated port ifIndex: 5)
    + Maximum frame size: 10240 octets
    + Port VLAN ID: none
    + Management address (IPv4): 10.255.5.32

Local port: 1/6
  Neighbor: e8e7.32cd.b14e, TTL 114 seconds
    + Chassis ID (MAC address): e8e7.32cd.b9e8
    + Port ID (locally assigned): "3045"
    + Time to live: 120 seconds

Local port: 1/10
  Neighbor: 001b.edae.fe09, TTL 106 seconds                       
    + Chassis ID (MAC address): 001b.edae.fe00
    + Port ID (MAC address): 001b.edae.fe09
    + Time to live: 120 seconds
    + System name         : "fw1.clmamofw"
    + Port description    : "GigabitEthernet1/10"
    + System capabilities : bridge, router
      Enabled capabilities: bridge, router
    + 802.3 MAC/PHY          : auto-negotiation enabled
      Advertised capabilities: 10BaseT-HD, 10BaseT-FD, 100BaseTX-HD,
                               100BaseTX-FD, 1000BaseT-HD, 1000BaseT-FD
      Operational MAU type   : 1000BaseT-FD
    + Link aggregation: aggregated (aggregated port ifIndex: 10)
    + Maximum frame size: 9216 octets
    + Port VLAN ID: none
    + Management address (IPv4): 216.106.21.252

Local port: 1/13
  Neighbor: 0026.f13c.85a9, TTL 102 seconds
    + Chassis ID (MAC address): 0026.f13c.8580
    + Port ID (locally assigned): "23"
    + Time to live: 120 seconds
    + Port description    : "23"
    + System name         : "FEBE1.SOCKET-COU"                    
    + System description  : "ProCurve J9145A 2910al-24G Switch, revision W.14.\
                             72, ROM W.14.06 (/ws/swbuildm/W_titan4_v14_a_qaof\
                             f/code/build/sbm(W_titan4_v14_a_qaoff))"
    + System capabilities : bridge, router
      Enabled capabilities: bridge
    + Management address (IPv4): 192.168.11.1
    + 802.3 MAC/PHY          : auto-negotiation enabled
      Advertised capabilities: 10BaseT-HD, 10BaseT-FD, 100BaseTX-HD,
                               100BaseTX-FD, 1000BaseT-FD
      Operational MAU type   : 1000BaseT-FD
    + 802.3 Power via MDI: PSE port, power not supported

```

**Help:** execute the command "show lldp neighbors detail"

**Prompt:**
- brocade_netiron>
- brocade_netiron#

### show running-config vlan

**Output:**
```
no spanning-tree
!
no dual-mode-default-vlan
!
!
vlan 1 name DEFAULT-VLAN 
 no untagged e 1/1 e 1/4 to 1/8 e 1/12 e 1/17 e 2/1 e 2/4 to 2/8 e 2/12 e 2/15 to 2/17 e 3/1 to 3/5 e 4/1 to 4/4 
!
vlan 2 
 tagged e 1/1 e 1/6 e 1/17 e 2/1 e 2/6 e 2/17 
 router-interface ve 2
 spanning-tree
!
vlan 10 name CLMAMO-RING-1 
 untagged e 1/14 
 tagged e 1/1 e 1/4 e 1/7 e 2/1 e 2/4 e 2/7 e 3/2 e 3/4 e 4/2 e 4/4 
 router-interface ve 10
 metro-ring 10
  ring-interfaces ethe 1/4 ethe 2/4
  enable
!
vlan 11 name CLMAMOXA-JFCYMOXA-RING 
 tagged e 1/5 e 2/5 
!                                                                 
vlan 14 name CLMAMOXA-RING 
 tagged e 1/4 e 1/7 e 2/4 e 2/7 
 metro-ring 14
  ring-interfaces ethe 2/4 ethe 1/4
  enable
!
vlan 22 name KMIZ 
 tagged e 1/8 e 2/8 e 3/2 e 3/4 e 4/2 
!
vlan 60 name CLMA-JFCY-FLTN_Master 
 tagged e 3/1 e 3/3 e 3/5 e 4/1 e 4/3 
 metro-ring 60
  ring-interfaces ethe 3/1 ethe 4/1
  enable
 metro-ring 58
  ring-interfaces ethe 4/1 ethe 3/5
  enable
 !
vlan 94 name HermannHospital_18thSt 
 tagged e 1/12 e 2/12 e 2/15 e 3/1 e 3/3 to 3/4 e 4/1 e 4/3 
!
vlan 100 
 tagged e 3/1 e 3/3 e 4/1 e 4/3                                   
!
vlan 144 name VOIPstate-External 
 tagged e 3/1 e 3/3 e 4/1 e 4/3 
 router-interface ve 144
!
vlan 145 name VOIPstate-Internal 
 tagged e 3/1 e 3/3 e 4/1 e 4/3 
 router-interface ve 145
!
vlan 146 name LabSBC-External 
 tagged e 1/4 e 1/7 e 2/4 e 2/7 
 router-interface ve 146
 !
vlan 149 name SBC-External 
 tagged e 1/4 e 1/7 e 2/4 e 2/7 
 router-interface ve 149
!
vlan 151 name LabSBC-internal 
 tagged e 1/4 e 1/7 e 2/4 e 2/7 
 router-interface ve 151
!
vlan 152 name SBC-Inside 
 tagged e 1/4 e 1/7 e 2/4 e 2/7                                   
 router-interface ve 152
!
 vlan 154 name SocketVoIP-Svr 
 tagged e 1/4 e 1/7 e 2/4 e 2/7 
 router-interface ve 154
!
vlan 156 name VoIP-Signaling 
 untagged e 1/11 e 2/11 
 tagged e 1/6 e 1/17 e 2/6 e 2/17 
 router-interface ve 156
!
vlan 158 name VoIP-Bearer 
 untagged e 1/10 e 2/10 
 router-interface ve 158

```

**Help:** execute the command "show running-config vlan"

**Prompt:**
- brocade_netiron>
- brocade_netiron#

### show lag brief

**Output:**
```
Total number of LAGs	: 12, 100/40g : 0
Total number of deployed LAGs	 : 12, 100/40g : 0
Total number of trunks created	: 12 (116 available), 100/40g : 0 (8 available)
LACP System Priority / ID	:1 / 0024.38a5.5f00
LACP Long timeout	:90, default: 90
LACP Short timeout	:3, default: 3

LAG                Type      Deploy Trunk Primary        Port List
Akamai Uplink     dynamic      Y     11     1/13        e 1/13 e 2/13
CLMAMOFW-FLTNHT   dynamic      Y     7      4/2         e 3/2 e 4/2
LAG5              dynamic      Y     5      3/3         e 3/3 to 3/4
LAG6              dynamic      Y     6      4/3         e 4/3 to 4/4
MLX-1a            dynamic      Y     4      2/2         e 2/2
MLX-CLMAMOXE      dynamic      Y     3      2/1         e 2/1
Switch1e.clmamofw dynamic      Y     10     1/5         e 1/5 e 2/21
fw1-inside        dynamic      Y     12     1/24        e 1/24 e 2/24
fw1-outside       dynamic      Y     13     1/10        e 1/10 e 2/10
speedtest         dynamic      Y     9      2/23        e 1/11 e 2/23
switch1c-MLX-FW   dynamic      Y     2      1/1         e 1/1
videouplink       static       Y     8      2/15        e 1/15 to 1/18 e 2/15 t
                                                        o 2/18

```

**Help:** execute the command "show lag brief"

**Prompt:**
- brocade_netiron>
- brocade_netiron#

### show interfaces brief

**Output:**
```

Port   Link     Port-State   Dupl Speed Trunk Tag Priori MAC            Name           Type              
1/1    Up       Forward      Full 1G    None  Yes level0 0024.38a5.1c00 ATM1-G0-1      default-port      
1/2    Disabled None         None None  None  No  level0 0024.38a5.1c01                default-port      
1/3    Disabled None         None None  None  No  level0 0024.38a5.1c02                default-port      
1/4    Up       Forward      Full 1G    5     Yes level0 0024.38a5.1c00 switch1a.clmamodefault-port      
1/5    Up       LACP-BLOCKED Full 1G    1     Yes level0 0024.38a5.1c00 CLMA-JFCY LAG #default-port      
1/16   Down     None         None None  None  No  level0 0024.38a5.1c00 InstallerDHCP  default-port
      
Port   Link     Port-State   Dupl Speed Trunk Tag Priori MAC            Name           Type              
ve2    Up       N/A          N/A  N/A   None  N/A N/A    0024.38a5.1c00 Main Ethernet Vdefault-port      
ve10   Up       N/A          N/A  N/A   None  N/A N/A    0024.38a5.1c00 Admin VLAN 10  default-port      
ve144  Up       N/A          N/A  N/A   None  N/A N/A    0024.38a5.1c00 VOIPstate-Exterdefault-port      
ve145  Up       N/A          N/A  N/A   None  N/A N/A    0024.38a5.1c00 VOIPstate-Interdefault-port    

Port   Link     Port-State   Dupl Speed Trunk Tag Priori MAC            Name           Type              
lb1    Up       N/A          N/A  N/A   None  N/A N/A    N/A            MPLS Loopback  default-port      
lb6    Up       N/A          N/A  N/A   None  N/A N/A    N/A                           default-port      
```

**Help:** execute the command "show interfaces brief"

**Prompt:**
- brocade_netiron>
- brocade_netiron#

### show topo

**Output:**
```
VLAN 2 - STP instance 0
--------------------------------------------------------------------
 STP Bridge Parameters:

Bridge           Bridge Bridge Bridge Hold  LastTopology Topology
Identifier       MaxAge Hello  FwdDly Time  Change       Change
hex              sec    sec    sec    sec   sec          cnt
8000002438a51c00 20     2      15     1     2456092      8       

RootBridge       RootPath  DesignatedBridge Root  Max Hel Fwd
Identifier       Cost      Identifier       Port  Age lo  Dly
hex                        hex                    sec sec sec
8000002438a51c00 0         8000002438a51c00 Root  20  2   15  

STP Port Parameters:

Port  Prio Path      State      Designat- Designated       Designated
Num   rity Cost                 ed Cost   Root             Bridge
1/1   128  4         FORWARDING 0         8000002438a51c00 8000002438a51c00 
1/6   128  4         FORWARDING 0         8000002438a51c00 8000002438a51c00 
1/17  128  4         FORWARDING 0         8000002438a51c00 8000002438a51c00 
2/1   128  4         FORWARDING 0         8000002438a51c00 8000002438a51c00 
2/6   128  4         FORWARDING 0         8000002438a51c00 8000002438a51c00 
2/17  128  4         FORWARDING 0         8000002438a51c00 8000002438a51c00 
telnet@mlx1.clmamoxa#  
telnet@mlx1.clmamoxa#show topo
Topology Group 10
 Topo HW Index  2
==================
Master VLAN   : 10
L2 Protocol   : MRP
 VPLS VLAN exist : FALSE
Member VLAN   : 146 149 151 to 152 154 200 300 to 303 350 400 453 1280 to 1283 1295 1335 1395 2005 2022 2024 2030 2033 2035 2039 2049 to 2050 2054 2069 to 2070 2086 2091 to 2092 2096 to 2097 2099 to 2100 2129 2184 2188 to 2189 2204 2215 2226 2241 to 2242 2250 2253 2277 2325 to 2326 2340 2342 2349 to 2351 2360 2367 2414 to 2415 2442 2895 3008 3840 4001 
Member Group  : None
Control Ports : e 1/4 e 1/7 e 2/4 e 2/7 
Free Ports :
VLAN: 10  - e 1/1 e 1/14 e 2/1 e 3/2 e 3/4 e 4/2 e 4/4 
VLAN: 200  - e 1/6 e 1/17 e 2/1 e 2/6 e 2/17 
VLAN: 300  - e 1/1 e 1/8 e 1/16 e 2/1 e 2/8 e 2/19 e 3/2 e 4/2 
VLAN: 301  - e 1/1 e 1/8 e 2/1 e 2/8 
VLAN: 302  - e 1/1 e 1/8 e 2/1 e 2/8 
VLAN: 303  - e 1/1 e 1/8 e 2/1 e 2/8 
VLAN: 350  - e 1/1 e 2/1 
VLAN: 400  - e 1/8 e 2/8 e 3/2 e 4/2 
VLAN: 453  - e 2/12 
VLAN: 1282  - e 1/1 
 VLAN: 1335  - e 1/8 e 2/8 e 3/2 e 4/2 
VLAN: 2022  - e 1/12 
VLAN: 2024  - e 3/4 
VLAN: 2030  - e 1/8 e 2/8 e 3/2 e 4/2                             
 VLAN: 2033  - e 3/4 
VLAN: 2035  - e 3/4 
VLAN: 2039  - e 3/4 
VLAN: 2049  - e 3/4 
VLAN: 2050  - e 2/12 e 3/4 
VLAN: 2054  - e 1/8 e 2/8 
VLAN: 2070  - e 3/4 
VLAN: 2086  - e 2/12 e 2/15 
VLAN: 2091  - e 1/8 e 1/12 e 2/8 
VLAN: 2092  - e 2/12 e 2/15 
VLAN: 2097  - e 3/4 
VLAN: 2100  - e 2/12 
 VLAN: 2129  - e 1/8 e 2/8 e 2/12 e 2/15 e 3/2 e 4/2 
VLAN: 2184  - e 1/12 
 VLAN: 2188  - e 2/12 e 2/15 
VLAN: 2189  - e 3/4 
VLAN: 2204  - e 3/4 
VLAN: 2215  - e 3/4 
VLAN: 2226  - e 1/1 e 3/4 
VLAN: 2241  - e 3/4 
VLAN: 2250  - e 3/4 
VLAN: 2253  - e 1/12 
VLAN: 2277  - e 3/4                                               
VLAN: 2326  - e 3/4 
VLAN: 2340  - e 1/12 e 2/12 e 2/16 
VLAN: 2342  - e 1/1 e 1/8 e 2/8 e 2/12 e 2/16 e 3/2 e 3/4 e 4/2 
 VLAN: 2349  - e 3/4 
VLAN: 2350  - e 1/12 
VLAN: 2351  - e 2/12 e 2/15 
 VLAN: 2360  - e 2/12 e 2/16 
VLAN: 2367  - e 1/8 e 1/12 e 2/8 e 2/12 e 2/16 e 3/2 e 4/2 
VLAN: 2414  - e 2/12 
VLAN: 2415  - e 2/12 e 2/15 
VLAN: 2442  - e 2/15 
VLAN: 2895  - e 3/4 
VLAN: 3840  - e 1/8 e 2/8 
VLAN: 4001  - e 1/6 e 1/17 e 2/6 e 2/17 

Topology Group 11
Topo HW Index  65535
 ==================
Master VLAN   : 11
L2 Protocol   : NONE
VPLS VLAN exist : FALSE
Member VLAN   : 201 501 1400 
Member Group  : None                                              
Control Ports : None
Free Ports :
VLAN: 11  - e 1/5 e 2/5 
VLAN: 201  - e 1/5 to 1/6 e 1/17 e 2/5 to 2/6 e 2/17 
 VLAN: 501  - e 1/5 e 2/5 
VLAN: 1400  - e 1/5 e 2/5 
Topology Group 13
Topo HW Index  8
==================
Master VLAN   : 513
L2 Protocol   : MRP
 VPLS VLAN exist : FALSE
Member VLAN   : 94 207 223 to 224 280 to 282 290 310 to 311 320 to 321 330 to 331 340 345 355 360 365 375 380 385 390 401 517 to 518 619 623 999 1290 1345 1355 to 1356 1380 1385 1390 2004 2006 2011 2018 2043 2045 to 2046 2058 to 2059 2063 to 2065 2072 2075 2102 2104 to 2107 2133 2137 2173 2180 to 2181 2190 2195 2197 2199 to 2200 2235 2257 2261 2265 2267 2270 to 2272 2274 2278 2282 2284 to 2287 2293 to 2296 2298 2301 to 2302 2305 to 2306 2314 to 2317 2320 2323 to 2324 2329 2332 2343 to 2345 2352 to 2353 2355 2357 2359 2362 to 2363 2366 2368 to 2369 2372 2374 to 2376 2379 2381 2384 2386 to 2387 2393 2395 2399 to 2401 2403 2408 2412 2416 2418 to 2420 2435 to 2440 2443 to 2446 2449 to 2451 2453 to 2456 2460 2466 to 2470 2472 2475 2483 2571 2575 to 2576 2718 2766 3004 3006 to 3007 
Member Group  : None
Control Ports : e 3/1 e 3/3 e 4/1 e 4/3 
Free Ports :
VLAN: 94  - e 1/12 e 2/12 e 2/15 e 3/4 
VLAN: 223  - e 1/6 e 1/17 e 2/6 e 2/17 
VLAN: 224  - e 1/6 e 1/17 e 2/6 e 2/17 
VLAN: 280  - e 1/1 
VLAN: 281  - e 1/1 
VLAN: 282  - e 1/1 
VLAN: 290  - e 1/1 e 2/1                                          
VLAN: 310  - e 1/1 e 2/1 
VLAN: 311  - e 1/1 e 2/1 
VLAN: 320  - e 1/1 e 2/1 
VLAN: 321  - e 1/1 e 2/1 
VLAN: 330  - e 1/1 e 2/1 
VLAN: 331  - e 1/1 e 2/1 
VLAN: 340  - e 1/1 e 2/1 
VLAN: 345  - e 1/1 e 2/1 
VLAN: 355  - e 1/1 e 2/1 
 VLAN: 360  - e 1/1 e 2/1 
VLAN: 365  - e 1/1 e 2/1 
VLAN: 375  - e 1/1 e 2/1 
VLAN: 380  - e 1/1 e 2/1 
VLAN: 385  - e 1/1 e 2/1 
VLAN: 390  - e 1/1 e 2/1 
VLAN: 1380  - e 1/1 e 2/1 
VLAN: 1390  - e 1/1 e 2/1 
VLAN: 2004  - e 1/8 e 2/8 e 3/4 
VLAN: 2006  - e 2/12 
VLAN: 2011  - e 1/8 e 1/12 e 2/8 e 2/15 e 3/4 
VLAN: 2018  - e 1/12 
VLAN: 2043  - e 1/8 e 2/8 e 3/4 
VLAN: 2045  - e 2/12 e 3/4                                        
VLAN: 2046  - e 1/12 e 3/4 
VLAN: 2058  - e 1/12 
VLAN: 2059  - e 3/4 
VLAN: 2063  - e 3/4 
VLAN: 2064  - e 3/4 
VLAN: 2072  - e 3/4 
VLAN: 2075  - e 1/12 e 2/12 
VLAN: 2102  - e 1/12 
VLAN: 2104  - e 1/12 e 2/12 
VLAN: 2105  - e 1/12 
VLAN: 2106  - e 1/12 
VLAN: 2107  - e 1/12 e 2/12 
VLAN: 2133  - e 1/12 
VLAN: 2137  - e 3/4 
VLAN: 2173  - e 2/12 
VLAN: 2180  - e 1/12 
VLAN: 2181  - e 3/4 
VLAN: 2190  - e 3/4 
VLAN: 2195  - e 3/4 
VLAN: 2197  - e 1/12 
VLAN: 2199  - e 1/8 e 2/8 e 3/4 
VLAN: 2200  - e 1/4 e 1/7 e 2/4 e 2/7 
VLAN: 2235  - e 2/12 e 2/15                                       
VLAN: 2257  - e 3/4 
VLAN: 2261  - e 1/12 e 2/12 e 2/15 
VLAN: 2265  - e 3/4 
 VLAN: 2267  - e 3/4 
VLAN: 2270  - e 1/12 
VLAN: 2271  - e 1/12 
VLAN: 2272  - e 1/12 
VLAN: 2274  - e 1/12 
VLAN: 2278  - e 3/4 
VLAN: 2282  - e 2/12 e 2/15 to 2/16 
VLAN: 2284  - e 2/16 
VLAN: 2286  - e 3/4 
VLAN: 2287  - e 1/12 
VLAN: 2293  - e 3/4 
VLAN: 2294  - e 3/4 
VLAN: 2295  - e 2/12 e 2/16 
VLAN: 2296  - e 3/4 
VLAN: 2298  - e 3/4 
VLAN: 2301  - e 2/12 e 2/16 
VLAN: 2302  - e 1/12 
VLAN: 2306  - e 3/4 
VLAN: 2314  - e 1/12 e 2/12 e 2/16 
VLAN: 2315  - e 1/12 e 2/15                                       
 VLAN: 2316  - e 1/12 
VLAN: 2317  - e 1/12 
VLAN: 2320  - e 3/4 
VLAN: 2323  - e 1/12 
VLAN: 2324  - e 1/12 
VLAN: 2329  - e 1/12 
VLAN: 2332  - e 3/4 
VLAN: 2343  - e 1/12 
VLAN: 2344  - e 1/1 e 2/12 e 2/16 e 3/2 e 3/4 e 4/2 
VLAN: 2345  - e 3/4 
VLAN: 2352  - e 2/12 e 2/16 
VLAN: 2353  - e 1/12 
VLAN: 2355  - e 3/4 
VLAN: 2357  - e 1/12 
VLAN: 2359  - e 1/4 e 1/7 e 1/12 e 2/4 e 2/7 
VLAN: 2362  - e 1/12 e 2/15 
VLAN: 2363  - e 1/4 e 1/7 e 2/4 e 2/7 
VLAN: 2366  - e 1/4 e 1/7 e 2/4 e 2/7 e 3/4 
VLAN: 2368  - e 2/12 e 2/16 
VLAN: 2369  - e 1/4 e 1/7 e 2/4 e 2/7 e 2/12 e 2/16 e 3/4 
VLAN: 2372  - e 2/12 e 2/16 
VLAN: 2374  - e 1/8 e 2/8 e 2/12 e 2/16 e 3/2 e 4/2 
 VLAN: 2375  - e 2/12 e 2/15                                       
VLAN: 2376  - e 1/12 
VLAN: 2379  - e 1/12 
VLAN: 2381  - e 1/12 
VLAN: 2384  - e 1/12 e 2/12 e 2/16 
VLAN: 2386  - e 1/12 e 2/12 
VLAN: 2387  - e 2/12 e 2/15 e 3/4 
VLAN: 2393  - e 2/12 e 2/16 
VLAN: 2395  - e 2/12 e 2/16 
VLAN: 2399  - e 2/12 
VLAN: 2400  - e 2/12 e 2/16 
VLAN: 2401  - e 2/12 e 2/16 
VLAN: 2403  - e 2/12 
VLAN: 2412  - e 2/12 
VLAN: 2416  - e 2/12 
VLAN: 2418  - e 2/12 
VLAN: 2419  - e 2/12 
VLAN: 2420  - e 2/12 
VLAN: 2435  - e 1/12 e 2/12 
VLAN: 2436  - e 1/12 
VLAN: 2437  - e 2/12 
VLAN: 2438  - e 1/12 e 2/12 
VLAN: 2439  - e 1/12 e 2/12 
VLAN: 2440  - e 1/12 e 2/12 e 3/4                                 
VLAN: 2443  - e 2/15 
VLAN: 2444  - e 2/15 e 3/4 
VLAN: 2445  - e 2/12 e 2/15 
VLAN: 2446  - e 2/16 e 3/4 
VLAN: 2449  - e 2/12 e 3/4 
VLAN: 2450  - e 2/15 
VLAN: 2451  - e 2/15 
VLAN: 2453  - e 2/16 
VLAN: 2454  - e 2/15 
VLAN: 2455  - e 2/16 
VLAN: 2456  - e 2/15 
VLAN: 2460  - e 2/15 
VLAN: 2466  - e 1/12 
VLAN: 2467  - e 1/12 
 VLAN: 2468  - e 2/16 
VLAN: 2469  - e 3/4 
VLAN: 2470  - e 3/4 
VLAN: 2472  - e 3/4 
VLAN: 2475  - e 3/4 
VLAN: 2483  - e 3/4 
VLAN: 2571  - e 3/4 
VLAN: 2575  - e 1/12 
VLAN: 2576  - e 3/4                                               
VLAN: 2718  - e 1/12 
VLAN: 2766  - e 3/4 
VLAN: 3004  - e 1/8 e 2/8 e 2/16 e 3/4 
VLAN: 3006  - e 3/4 
VLAN: 3007  - e 1/12 e 2/12 e 3/4 

Topology Group 14
Topo HW Index  3
==================
Master VLAN   : 14
L2 Protocol   : MRP
VPLS VLAN exist : FALSE
Member VLAN   : 370 1370 2025 2031 2057 2134 2138 2210 2256 2263 2356 2404 2506 2896 
Member Group  : None
Control Ports : e 1/4 e 1/7 e 2/4 e 2/7 
Free Ports :
Topology Group 60
Topo HW Index  7
==================
Master VLAN   : 60
L2 Protocol   : MRP
VPLS VLAN exist : FALSE
Member VLAN   : 2371                                              
Member Group  : None
Control Ports : e 3/1 e 3/3 e 3/5 e 4/1 e 4/3 
Free Ports :
VLAN: 2371  - e 1/4 e 1/7 e 2/4 e 2/7 

Topology Group 170
Topo HW Index  4
==================
Master VLAN   : 170
L2 Protocol   : MRP
VPLS VLAN exist : FALSE
Member VLAN   : 144 to 145 220 454 2040 2191 2422 2459 
Member Group  : None
Control Ports : e 3/1 e 3/3 e 4/1 e 4/3 
Free Ports :

```

**Help:** execute the command "show topo"

**Prompt:**
- brocade_netiron>
- brocade_netiron#

### show monitor actual

**Output:**
```
Monitored Port 1/10
  Input traffic mirrored to:  1/13
  Output traffic mirrored to:  1/13
Monitored Port 1/11
  Input traffic mirrored to:  1/13
  Output traffic mirrored to:  1/13
Monitored Port 2/10
  Input traffic mirrored to:  1/13
  Output traffic mirrored to:  1/13
Monitored Port 2/11
  Input traffic mirrored to:  1/13
  Output traffic mirrored to:  1/13

```

**Help:** execute the command "show monitor actual"

**Prompt:**
- brocade_netiron>
- brocade_netiron#

### show span

**Output:**
```

VLAN 2 - STP instance 0
--------------------------------------------------------------------
 STP Bridge Parameters:

Bridge           Bridge Bridge Bridge Hold  LastTopology Topology
Identifier       MaxAge Hello  FwdDly Time  Change       Change
hex              sec    sec    sec    sec   sec          cnt
8000002438a51c00 20     2      15     1     2456092      8       

RootBridge       RootPath  DesignatedBridge Root  Max Hel Fwd
Identifier       Cost      Identifier       Port  Age lo  Dly
hex                        hex                    sec sec sec
8000002438a51c00 0         8000002438a51c00 Root  20  2   15  

STP Port Parameters:

Port  Prio Path      State      Designat- Designated       Designated
Num   rity Cost                 ed Cost   Root             Bridge
1/1   128  4         FORWARDING 0         8000002438a51c00 8000002438a51c00 
1/6   128  4         FORWARDING 0         8000002438a51c00 8000002438a51c00 
1/17  128  4         FORWARDING 0         8000002438a51c00 8000002438a51c00 
2/1   128  4         FORWARDING 0         8000002438a51c00 8000002438a51c00 
2/6   128  4         FORWARDING 0         8000002438a51c00 8000002438a51c00 
2/17  128  4         FORWARDING 0         8000002438a51c00 8000002438a51c00 
```

**Help:** execute the command "show span"

**Prompt:**
- brocade_netiron>
- brocade_netiron#

### show metro

**Output:**
```

Metro Ring 10 - VLAN Type REGULAR
==============
Ring       State      Ring       Master     Topo       Hello      Prefwing
id                    role       vlan       group      time(ms)   time(ms)
10         enabled    member     10         10         100        300

Ring interfaces Interface role  Interface state interface type 
ethernet 1/1    primary         forwarding      regular        
ethernet 2/1    secondary       forwarding      regular        

RHPs sent       RHPs rcvd       TC rcvd    TC sent    State changes
10              0               126        0          30

Metro Ring 14 - VLAN Type REGULAR
==============
Ring       State      Ring       Master     Topo       Hello      Prefwing
id                    role       vlan       group      time(ms)   time(ms)
14         enabled    member     14         14         100        300

Ring interfaces Interface role  Interface state interface type 
ethernet 1/1    primary         forwarding      regular        
ethernet 2/2    secondary       forwarding      regular        
                                                                  
RHPs sent       RHPs rcvd       TC rcvd    TC sent    State changes
0               0               0          0          0

Metro Ring 215 - VLAN Type REGULAR - CLMAMOFW-Backbone
==============
Ring       State      Ring       Master     Topo       Hello      Prefwing
id                    role       vlan       group      time(ms)   time(ms)
215        enabled    master     215        215        100        300

Ring interfaces Interface role  Interface state interface type 
ethernet 4/3    primary         forwarding      regular        
ethernet 3/3    secondary       blocking        regular        
 
RHPs sent       RHPs rcvd       TC rcvd    TC sent    State changes
18288470        18195932        0          259        148

Metro Ring 13 - VLAN Type REGULAR - CLMAXA-FW-Telecom
==============
Ring       State      Ring       Master     Topo       Hello      Prefwing
id                    role       vlan       group      time(ms)   time(ms)
13         enabled    member     513        13         100        300

Ring interfaces Interface role  Interface state interface type    
ethernet 3/3    primary         forwarding      regular        
ethernet 4/3    secondary       forwarding      regular        

RHPs sent       RHPs rcvd       TC rcvd    TC sent    State changes
4               0               16         0          33

Metro Ring 171 - VLAN Type REGULAR - CLMA-KSCY-STLS-10G-C
==============
Ring       State      Ring       Master     Topo       Hello      Prefwing
id                    role       vlan       group      time(ms)   time(ms)
171        enabled    member     170        170        100        300

Ring interfaces Interface role  Interface state interface type 
ethernet 3/3    primary         forwarding      regular        
ethernet 4/3    secondary       forwarding      regular        

RHPs sent       RHPs rcvd       TC rcvd    TC sent    State changes
4               0               22         0          33

Metro Ring 175 - VLAN Type REGULAR - CLMAMO10G-to-FW
==============
Ring       State      Ring       Master     Topo       Hello      Prefwing
id                    role       vlan       group      time(ms)   time(ms)
175        enabled    member     175        175        100        300

Ring interfaces Interface role  Interface state interface type 
ethernet 3/3    primary         forwarding      regular        
ethernet 4/3    secondary       forwarding      regular        

RHPs sent       RHPs rcvd       TC rcvd    TC sent    State changes
4               0               20         0          33

Metro Ring 176 - VLAN Type REGULAR - FW-to-CLMAMO10G
==============
Ring       State      Ring       Master     Topo       Hello      Prefwing
id                    role       vlan       group      time(ms)   time(ms)
176        enabled    member     175        175        100        300

Ring interfaces Interface role  Interface state interface type 
ethernet 1/1    primary         forwarding      regular        
ethernet 2/2    secondary       forwarding      regular        

RHPs sent       RHPs rcvd       TC rcvd    TC sent    State changes
0               0               3          0          0

Metro Ring 60 - VLAN Type REGULAR                                 
==============
Ring       State      Ring       Master     Topo       Hello      Prefwing
id                    role       vlan       group      time(ms)   time(ms)
60         enabled    member     60         60         100        300

Ring interfaces Interface role  Interface state interface type 
ethernet 3/3    primary         forwarding      tunnel         
ethernet 4/3    secondary       forwarding      tunnel         

RHPs sent       RHPs rcvd       TC rcvd    TC sent    State changes
0               0               9          0          33

Metro Ring 61 - VLAN Type REGULAR
==============
Ring       State      Ring       Master     Topo       Hello      Prefwing
id                    role       vlan       group      time(ms)   time(ms)
61         enabled    member     60         60         100        300

Ring interfaces Interface role  Interface state interface type 
ethernet 4/3    primary         forwarding      tunnel         
ethernet 4/2    secondary       forwarding      regular        
 
RHPs sent       RHPs rcvd       TC rcvd    TC sent    State changes
0               0               42         0          12

Metro Ring 63 - VLAN Type REGULAR
==============
Ring       State      Ring       Master     Topo       Hello      Prefwing
id                    role       vlan       group      time(ms)   time(ms)
63         enabled    member     62         62         100        300

Ring interfaces Interface role  Interface state interface type 
ethernet 4/3    primary         forwarding      regular        
ethernet 4/2    secondary       forwarding      regular        

RHPs sent       RHPs rcvd       TC rcvd    TC sent    State changes
0               0               122        0          12

Metro Ring 58 - VLAN Type REGULAR
==============
Ring       State      Ring       Master     Topo       Hello      Prefwing
id                    role       vlan       group      time(ms)   time(ms)
58         enabled    member     60         60         100        300

Ring interfaces Interface role  Interface state interface type 
ethernet 4/3    primary         forwarding      regular           
ethernet 3/3    secondary       forwarding      regular        

RHPs sent       RHPs rcvd       TC rcvd    TC sent    State changes
7               0               0          0          33

```

**Help:** execute the command "show metro"

**Prompt:**
- brocade_netiron>
- brocade_netiron#

### show running-config interface

**Output:**
```
interface ve 2801
 ip address 10.92.176.219/29
 ip address 10.92.191.67/26
 ip address 10.201.214.35/28
 ip address 10.231.184.211/28
 ip address 10.251.229.83/28
 ip helper-address 10.0.113.10
 ip helper-address 10.0.113.20
 ipv6 address 2001:2aaf:14:8::3/120
 ipv6 nd suppress-ra
 disable
 ip vrrp-extended auth-type simple-text-auth VLAN2801
 ip vrrp-extended vrid 1
  backup priority 90 track-priority 50
  ip-address 10.92.176.217
  advertise backup
  dead-interval 12
  hello-interval 4
  track-port ethernet 1/1
  activate
 ip vrrp-extended vrid 2
  backup priority 90 track-priority 50
  ip-address 10.251.229.81
  advertise backup
  dead-interval 12
  hello-interval 4
  track-port ethernet 1/1
  activate
 ip vrrp-extended vrid 3
  backup priority 90 track-priority 50
  ip-address 10.231.184.209
  advertise backup
  dead-interval 12
  hello-interval 4
  track-port ethernet 1/1
  activate
 ip vrrp-extended vrid 4
  backup priority 90 track-priority 50
  ip-address 10.201.214.33
  advertise backup
  dead-interval 12
  hello-interval 4
  track-port ethernet 1/1
  activate
 ip vrrp-extended vrid 5
  backup priority 90 track-priority 50
  ip-address 10.92.191.65
  advertise backup
  dead-interval 12
  hello-interval 4
  track-port ethernet 1/1
  activate
 ipv6 vrrp-extended vrid 6
  backup priority 90 track-priority 50
  ipv6-address 2001:2aaf:14:8::1
  advertise backup
  hello-interval 4
  track-port ethernet 1/1
  activate
!
interface ve 2802

```

**Help:** execute the command "show running-config interface"

**Prompt:**
- brocade_netiron>
- brocade_netiron#

### skip-page-display

**Output:** None

**Help:** Execute the command skip-page-display. This automatically generated. Feel free to change it!

**Prompt:**
- brocade_netiron>
- brocade_netiron#

