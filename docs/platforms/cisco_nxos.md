# cisco_nxos


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
- cisco_nxos>

### terminal length 0

**Output:** None

**Help:** set the terminal width to maximum

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### ex

**Output:**
```
True
```

**Help:** exit the terminal

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show l2rib internal permanently-frozen-list

**Output:**
```

Topology    Mac Address    Frozen time
----------- -------------- ---------------------------
190         0050.5699.7898 Sat Jan 27 08:46:01.447 UTC
190         0050.5699.8ec0 Sat Jan 27 08:47:39.818 UTC
190         0050.5699.d709 Sat Jan 27 08:47:49.970 UTC
190         0050.56b5.1419 Sat Jan 27 08:40:15.482 UTC
190         0050.56b5.1bca Sat Jan 27 08:48:00.545 UTC
192         000c.29d4.ee30 Sat Jan 27 08:42:26.149 UTC
192         0012.3fff.e687 Sat Jan 27 08:57:48.481 UTC
192         0050.5699.1684 Sat Jan 27 08:53:13.686 UTC
192         0050.5699.1b56 Sat Jan 27 08:37:59.468 UTC
192         0050.5699.2199 Sat Jan 27 08:53:08.098 UTC
192         0050.5699.249d Sat Jan 27 08:52:44.355 UTC
192         0050.5699.25bf Sat Jan 27 08:45:45.772 UTC
192         0050.5699.27b2 Sat Jan 27 08:49:48.131 UTC
192         0050.5699.3c5a Sat Jan 27 08:49:48.310 UTC
192         0050.5699.410a Sat Jan 27 08:51:56.147 UTC
192         0050.5699.4241 Sat Jan 27 08:52:28.534 UTC
192         0050.5699.449f Sat Jan 27 08:52:50.603 UTC
192         0050.5699.4826 Sat Jan 27 08:55:45.974 UTC
192         0050.5699.4a94 Sat Jan 27 08:56:50.314 UTC
192         0050.5699.4dd2 Sat Jan 27 08:48:56.964 UTC
192         0050.5699.5044 Sat Jan 27 08:55:23.553 UTC
192         0050.5699.50ab Sat Jan 27 08:52:46.601 UTC
192         0050.5699.5705 Sat Jan 27 08:58:09.431 UTC
192         0050.5699.57ec Sat Jan 27 08:51:55.528 UTC
192         0050.5699.6083 Sat Jan 27 08:52:46.851 UTC

```

**Help:** execute the command "show l2rib internal permanently-frozen-list"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show vrf interface

**Output:**
```
Interface                 VRF-Name                        VRF-ID  Site-of-Origin
Vlan6001                  ADMIN                                6  --
Vlan6700                  ADMIN                                6  --
Vlan5302                  AXNET                                7  --
Vlan7202                  AXNET                                7  --
Vlan6302                  AXNET                                7  --
Vlan5301                  MARKING                              4  --
Vlan7201                  MARKING                              4  --
Vlan6301                  MARKING                              4  --
Ethernet1/10              Keepalive                            3  --
Vlan1                     default                              1  --
Vlan100                   default                              1  --
loopback0                 default                              1  --
loopback1                 default                              1  --
Ethernet1/25              default                              1  --
Ethernet1/30              default                              1  --
Ethernet1/17              default                              1  --
Ethernet1/42              default                              1  --
mgmt0                     management                           2  --

```

**Help:** execute the command "show vrf interface"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip bgp

**Output:**
```
Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

   Network            Next Hop            Metric     LocPrf     Weight Path
*>l10.10.0.1/32       0.0.0.0                           100      32768 i
x e10.10.0.2/32       10.10.2.1                                      0 64102 64002 i
*>e                   10.10.1.1                                      0 64101 64002 i
*>e10.10.0.101/32     10.10.1.1                                      0 64101 i
*>e10.10.0.102/32     10.10.2.1                                      0 64102 i
*>e10.10.0.201/32     10.10.2.1                                      0 64102 64201 i
* e                   10.10.1.1                                      0 64101 64201 i
*>e10.10.0.202/32     10.10.2.1                                      0 64102 64202 i
*>l10.10.1.0/30       0.0.0.0                           100      32768 i
* e                   10.10.1.1                                      0 64101 i
x e10.10.1.4/30       10.10.2.1                                      0 64102 64002 i
*>e                   10.10.1.1                                      0 64101 i
*>l10.10.2.0/30       0.0.0.0                           100      32768 i
* e                   10.10.2.1                                      0 64102 i
*>e10.10.2.4/30       10.10.2.1                                      0 64102 i
* e                   10.10.1.1                                      0 64101 64002 i
* e10.10.101.0/30     10.10.2.1                                      0 64102 64201 i
*>e                   10.10.1.1                                      0 64101 i
*>e10.10.101.4/30     10.10.2.1                                      0 64102 i
* e                   10.10.1.1                                      0 64101 64201 i
* e10.10.102.0/30     10.10.2.1                                      0 64102 64202 i
*>e                   10.10.1.1                                      0 64101 i
*>e10.10.102.4/30     10.10.2.1                                      0 64102 i
*>l10.10.150.0/24     0.0.0.0                           100      32768 i
*>l10.10.151.0/24     0.0.0.0                           100      32768 i
*>l10.10.152.0/24     0.0.0.0                           100      32768 i
x e10.10.160.0/24     10.10.2.1                                      0 64102 64002 i
*>e                   10.10.1.1                                      0 64101 64002 i
x e10.10.161.0/24     10.10.2.1                                      0 64102 64002 i
*>e                   10.10.1.1                                      0 64101 64002 i
x e10.10.162.0/24     10.10.2.1                                      0 64102 64002 i
*>e                   10.10.1.1                                      0 64101 64002 i
*>e10.10.201.0/30     10.10.2.1                                      0 64102 64201 i
* e                   10.10.1.1                                      0 64101 64201 i
*>e10.10.202.0/30     10.10.2.1                                      0 64102 64202 i
*>l100.100.100.100/30 0.0.0.0                           100      32768 i
x e100.100.100.104/30 10.10.2.1                                      0 64102 64002 i
*>e                   10.10.1.1                                      0 64101 64002 i
*>e100.100.100.108/30 10.10.2.1                                      0 64102 {{64201 64202}} i
*>e100.100.100.112/30 10.10.2.1                                      0 64102 {{64201 64202}} 64203 i
  l                   0.0.0.0                           100      32768 i

```

**Help:** execute the command "show ip bgp"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show interface description

**Output:**
```

-------------------------------------------------------------------------------
Interface                Description                                            
-------------------------------------------------------------------------------
mgmt0                    --

-------------------------------------------------------------------------------
Port          Type   Speed   Description
-------------------------------------------------------------------------------
Eth4/1        eth    10G     --
Eth4/2        eth    1000    --
Eth4/3        eth    10G     This is a test description
Eth4/4        eth    10G     This is a test description
Eth4/5        eth    10G     This is a test description
Eth4/6        eth    1000    This is a test description
Eth4/7        eth    10G     This is a test description
Eth4/8        eth    1000    This is a test description
Eth4/9        eth    10G     This is a test description
Eth4/10       eth    10G     This is a test description
Eth4/11       eth    10G     This is a test description
Eth4/12       eth    10G     This is a test description
Eth4/13       eth    1000    This is a test description
Eth4/14       eth    10G     --
Eth4/15       eth    10G     This is a test description
Eth4/16       eth    10G     This is a test description
Eth4/17       eth    1000    This is a test description
Eth4/18       eth    10G     This is a test description
Eth4/19       eth    1000    This is a test description
Eth4/20       eth    10G     This is a test description
Eth4/21       eth    10G     This is a test description
Eth4/22       eth    10G     This is a test description
Eth4/23       eth    10G     This is a test description
Eth4/24       eth    10G     This is a test description
Eth6/1        eth    10G     This is a description on line card 6
Eth6/2        eth    10G     This is a description on line card 6
Eth6/3        eth    1000    This is a description on line card 6
Eth6/4        eth    1000    This is a description on line card 6
Eth6/5        eth    10G     This is a description on line card 6
Eth6/6        eth    1000    This is a description on line card 6
Eth6/7        eth    10G     This is a description on line card 6
Eth6/8        eth    10G     This is a description on line card 6
Eth6/9        eth    10G     This is a description on line card 6
Eth6/10       eth    10G     This is a description on line card 6
Eth6/11       eth    10G     This is a description on line card 6
Eth6/12       eth    10G     This is a description on line card 6
Eth6/13       eth    10G     This is a description on line card 6
Eth6/14       eth    10G     This is a description on line card 6
Eth6/15       eth    10G     This is a description on line card 6
Eth6/16       eth    1000    This is a description on line card 6
Eth6/17       eth    10G     This is a description on line card 6
Eth6/18       eth    1000    This is a description on line card 6
Eth6/19       eth    10G     This is a description on line card 6
Eth6/20       eth    10G     This is a description on line card 6
Eth6/21       eth    10G     This is a description on line card 6
Eth6/22       eth    10G     This is a description on line card 6
Eth6/23       eth    10G     This is a description on line card 6
Eth6/24       eth    10G     This is a description on line card 6
Eth6/25       eth    1000    This is a description on line card 6
Eth6/26       eth    1000    This is a description on line card 6
Eth6/27       eth    10G     This is a description on line card 6
Eth6/28       eth    1000    This is a description on line card 6
Eth6/29       eth    10G     This is a description on line card 6
Eth6/30       eth    10G     This is a description on line card 6
Eth6/31       eth    10G     This is a description on line card 6
Eth6/32       eth    10G     This is a description on line card 6
Eth6/33       eth    10G     This is a description on line card 6
Eth6/34       eth    1000    This is a description on line card 6
Eth6/35       eth    10G     This is a description on line card 6
Eth6/36       eth    1000    This is a description on line card 6
Eth6/37       eth    10G     This is a description on line card 6
Eth6/38       eth    10G     This is a description on line card 6
Eth6/39       eth    1000    This is a description on line card 6
Eth6/40       eth    10G     This is a description on line card 6
Eth6/41       eth    10G     This is a description on line card 6
Eth6/42       eth    10G     This is a description on line card 6
Eth6/43       eth    10G     This is a description on line card 6
Eth6/44       eth    10G     This is a description on line card 6
Eth6/45       eth    10G     This is a description on line card 6
Eth6/46       eth    10G     This is a description on line card 6
Eth6/47       eth    10G     This is a description on line card 6
Eth6/48       eth    10G     This is a description on line card 6

-------------------------------------------------------------------------------
Interface                Description                                            
-------------------------------------------------------------------------------
Po10                     This is a portchannel
Po20                     This is a portchannel
Po25                     This is a portchannel
Po300                    This is a portchannel

-------------------------------------------------------------------------------
Interface                Description                                            
-------------------------------------------------------------------------------
Lo0                      This is a loopback
Lo1                      This is a loopback
Lo2                      This is a loopback
Lo20                     --
Lo30                     --
Vlan1                    --
Vlan9                    Nice little VLAN interface here
Vlan10                   Nice little VLAN interface here
Vlan20                   Nice little VLAN interface here
Vlan30                   Nice little VLAN interface here

-------------------------------------------------------------------------------
Port          Type   Speed   Description
-------------------------------------------------------------------------------
Eth100/1/1    eth    1000    This is another description
Eth100/1/2    eth    1000    This is another description
Eth100/1/3    eth    1000    This is another description
Eth100/1/4    eth    1000    This is another description
Eth100/1/5    eth    1000    This is another description
Eth100/1/6    eth    1000    This is another description
Eth100/1/7    eth    1000    This is another description
Eth100/1/8    eth    1000    This is another description
Eth100/1/9    eth    1000    This is another description
Eth100/1/10   eth    1000    This is another description
Eth100/1/11   eth    1000    This is another description
Eth100/1/12   eth    1000    This is another description
Eth100/1/13   eth    1000    This is another description
Eth100/1/14   eth    1000    This is another description
Eth100/1/15   eth    1000    This is another description
Eth100/1/16   eth    1000    This is another description
Eth100/1/17   eth    1000    This is another description
Eth100/1/18   eth    1000    This is another description
Eth100/1/19   eth    1000    This is another description
Eth100/1/20   eth    1000    This is another description
Eth100/1/21   eth    1000    This is another description
Eth100/1/22   eth    1000    This is another description
Eth100/1/23   eth    1000    This is another description
Eth100/1/24   eth    1000    This is another description

```

**Help:** execute the command "show interface description"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show module

**Output:**
```
Mod  Ports  Module-Type                      Model              Status
---  -----  -------------------------------- ------------------ ------------
1    48     1000 Mbps Optical Ethernet Modul N7K-M148GS-11      ok
3    0      Supervisor Module-2                                 powered-up
4    0      Supervisor Module-2              N7K-SUP1           powered-dn
5    0      Supervisor Module-2              N7K-SUP1           active *
6    0      Supervisor Module-2              N7K-SUP1           ha-standby


Mod  Power-Status  Reason 
---  ------------  ---------------------------
4    powered-dn     Configured Power down

Mod  Sw              Hw
---  --------------  ------
3    4.1(3)          0.202   
4    4.1(3)          0.805   

Mod  MAC-Address(es)                         Serial-Num
---  --------------------------------------  ----------
3    00-1b-54-c2-ed-d0 to 00-1b-54-c2-ee-04  JAF1219AGFE
4    00-1b-54-c0-ff-10 to 00-1b-54-c0-ff-18  JAB114000BV

Mod  Online Diag Status
---  ------------------
3    Pass
4    Pass

Xbar Ports  Module-Type                      Model              Status
---  -----  -------------------------------- ------------------ ------------
1    0      Fabric Module 1                  N7K-C7018-FAB-1    ok

Xbar Sw              Hw
---  --------------  ------
1    NA              0.101   

Xbar MAC-Address(es)                         Serial-Num
---  --------------------------------------  ----------
1    NA                                      JAF1225AGHJ

* this terminal session 

```

**Help:** execute the command "show module"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show cts interface brief

**Output:**
```
CTS Information for Interfaces:
--------- -------- ---------- ------------------ -------------
Interface CTS Mode IFC State    SGT Assignment   Propagate SGT 
--------- -------- ---------- ------------------ -------------
Eth4/1    MANUAL   OPEN           0, Not Trusted Disabled 

```

**Help:** execute the command "show cts interface brief"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show switching-mode

**Output:**
```
Configured switching mode: Store and Forward

Module Number     Operational Mode 
     1            Store and Forward
     2            Cut-Through 
```

**Help:** execute the command "show switching-mode"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show vrf detail

**Output:**
```
VRF-Name: HUB, VRF-ID: 9, State: Up
    VPNID: 123:456
    RD: 172.21.111.112:197
    Max Routes: 0  Mid-Threshold: 0
    Table-ID: 0x80000009, AF: IPv6, Fwd-ID: 0x80000009, State: Up
    Table-ID: 0x00000009, AF: IPv4, Fwd-ID: 0x00000009, State: Up

VRF-Name: INSTRUMENTS, VRF-ID: 10, State: Up
    VPNID: 3211:65
    RD: 172.21.111.112:108
    Max Routes: 0  Mid-Threshold: 0
    Table-ID: 0x8000000a, AF: IPv6, Fwd-ID: 0x8000000a, State: Up
    Table-ID: 0x0000000a, AF: IPv4, Fwd-ID: 0x0000000a, State: Up

VRF-Name: LAB, VRF-ID: 11, State: Up
    VPNID: 890:765
    RD: 172.21.123.111:107
    Max Routes: 0  Mid-Threshold: 0
    Table-ID: 0x8000000b, AF: IPv6, Fwd-ID: 0x8000000b, State: Up
    Table-ID: 0x0000000b, AF: IPv4, Fwd-ID: 0x0000000b, State: Up

```

**Help:** execute the command "show vrf detail"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip dhcp snooping statistics

**Output:**
```
---------------------------------------------------------------------- 
Message Type             Rx              Tx           Drops  
---------------------------------------------------------------------- 
Discover                 10              10              10
Offer                    20              20              20
Request                  30              30              30
Ack                      40              40              40
Release                  50              50              50
Decline                  60              60              60
Inform                   70              70              70
Nack                     80              80              80
---------------------------------------------------------------------- 
Total                  5000            5000            5000
---------------------------------------------------------------------- 
DHCP L2 Forwarding:
Total Packets Forwarded                          :       100
Total Packets Received                           :       200
Total Packets Dropped                            :       300
Non DHCP:
Total Packets Received                           :       400
Total Packets Forwarded                          :       500
Total Packets Dropped                            :       600
DROP:
Received on untrusted port                       :       700
Unknown Failure                                  :       800
Source mac validation failed                     :       900
Binding entry validation Failed                  :      1000
Invalid DHCP message type                        :      1100
Interface error                                  :      1200
Tx over trusted port failed                      :      1300
Trust port not configured                        :      1400
 Vlan validation failure                          :      1500
Insertion of option 82 failed                    :      1600
Packet Malformed                                 :      1700
```

**Help:** execute the command "show ip dhcp snooping statistics"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip pim group-range vrf all

**Output:**
```
PIM Group-Range Configuration for VRF "default"
Group-range        Action Mode  RP-address      Shrd-tree-range   Origin
224.0.0.0/8        Accept SSM   -               -                 Local

PIM Group-Range Configuration for VRF "red"
Group-range        Action Mode  RP-address      Shrd-tree-range   Origin
224.0.0.0/8        Accept SSM   -               -                 Local


```

**Help:** execute the command "show ip pim group-range vrf all"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show nve peers

**Output:**
```
Interface Peer-IP                                 State LearnType Uptime   Router-Mac      
--------- --------------------------------------  ----- --------- -------- -----------------
nve1      192.168.111.41                          Up    CP        2y11w    0200.c0a8.5422   
nve1      192.168.111.47                          Up    CP        2y11w    2416.9dd1.4117  
nve1      192.168.111.48                          Up    CP        2y11w    cc7f.76a5.3a77  
nve1      192.168.111.52                          Up    CP        2y11w    2416.9dd1.8137  
nve1      192.168.111.81                          Up    CP        2y11w    0200.c0a8.545b  

```

**Help:** execute the command "show nve peers"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show port-channel summary

**Output:**
```
Flags:  D - Down        P - Up in port-channel (members)
        I - Individual  H - Hot-standby (LACP only)
        s - Suspended   r - Module-removed
        S - Switched    R - Routed
        U - Up (port-channel)
        M - Not in use. Min-links not met
--------------------------------------------------------------------------------
 Group Port-       Type     Protocol  Member Ports
      Channel
--------------------------------------------------------------------------------
1     Po1(RU)     Eth      LACP      Eth1/1(P)    Eth2/1(P)
2     Po2(RU)     Eth      LACP      Eth1/2(P)    Eth2/2(P)
3     Po3(RU)     Eth      LACP      Eth1/3(P)    Eth2/3(P)
4     Po4(RU)     Eth      LACP      Eth1/4(P)    Eth2/4(P)
12    Po12(RU)    Eth      LACP      Eth1/5(P)    Eth2/5(P)
13    Po13(RU)    Eth      LACP      Eth1/6(P)    Eth2/6(P)
14    Po14(RU)    Eth      LACP      Eth1/7(P)    Eth2/7(P)
801   Po801(RU)   Eth      LACP      Eth5/6(P)    Eth6/6(P)
802   Po802(RU)   Eth      LACP      Eth5/7(P)    Eth6/7(P)
803   Po803(RU)   Eth      LACP      Eth15/17(P)  Eth16/17(P)
804   Po804(RU)   Eth      LACP      Eth15/24(P)  Eth16/24(P)
811   Po811(RU)   Eth      LACP      Eth15/8(P)   Eth15/28(P)  Eth16/8(P)
                                     Eth16/28(P)
812   Po812(RU)   Eth      LACP      Eth15/36(P)  Eth16/36(P)  Eth17/8(P)
                                     Eth18/8(P)
813   Po813(RU)   Eth      LACP      Eth15/15(P)  Eth16/15(P)
814   Po814(RU)   Eth      LACP      Eth15/22(P)  Eth16/22(P)
821   Po821(RU)   Eth      LACP      Eth15/30(P)  Eth16/30(P)  Eth17/29(P)
                                     Eth18/29(P)
822   Po822(RU)   Eth      LACP      Eth15/38(P)  Eth16/38(P)  Eth17/30(P)
                                     Eth18/30(P)
823   Po823(RU)   Eth      LACP      Eth3/9(P)    Eth4/9(P)
824   Po824(RU)   Eth      LACP      Eth3/10(P)   Eth4/10(P)
825   Po825(RU)   Eth      LACP      Eth3/3(P)
826   Po826(RU)   Eth      LACP      Eth4/3(P)
827   Po827(RU)   Eth      LACP      Eth5/3(P)
828   Po828(RU)   Eth      LACP      Eth6/3(P)

```

**Help:** execute the command "show port-channel summary"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show environment

**Output:**
```
Power Supply:
Voltage: 50 Volts
Power                              Actual        Total
Supply    Model                    Output     Capacity    Status
                                 (Watts )     (Watts )
-------  -------------------  -----------  -----------  --------------
1        N7K-AC-3KW                 407 W       3000 W     Ok        
2        N7K-AC-3KW                 370 W       3000 W     Ok              


                                  Actual        Power      
Module    Model                     Draw    Allocated    Status
                                 (Watts )     (Watts )     
-------  -------------------  -----------  -----------  --------------
1        N7K-SUP2E                  125 W        265 W    Powered-Up
2        N7K-SUP2E                  125 W        265 W    Powered-Up
3        N7K-M224XP-23L             602 W        795 W    Powered-Up
4        N7K-M202CF-22L             620 W        795 W    Powered-Up
fan1     N7K-C7004-FAN               91 W        450 W    Powered-Up

N/A - Per module power not available


Power Usage Summary:
--------------------
Power Supply redundancy mode (configured)                PS-Redundant
Power Supply redundancy mode (operational)               PS-Redundant

Total Power Capacity (based on configured mode)               9000 W
Total Power of all Inputs (cumulative)                       12000 W
Total Power Output (actual draw)                              1555 W
Total Power Allocated (budget)                                2570 W
Total Power Available for additional modules                  6430 W

Clock:
----------------------------------------------------------
Clock           Model                Hw         Status
----------------------------------------------------------
A               Clock Module         --         NotSupported/None
B               Clock Module         --         NotSupported/None


Fan:
------------------------------------------------------
Fan             Model                Hw         Status
------------------------------------------------------
Fan1(sys_fan1)  N7K-C7004-FAN        1.0        Ok  
Fan_in_PS1      --                   --         Ok             
Fan_in_PS2      --                   --         Ok                      
Fan Zone Speed: Zone 1: 0x7f


Temperature:
--------------------------------------------------------------------
Module   Sensor        MajorThresh   MinorThres   CurTemp     Status
                       (Celsius)     (Celsius)    (Celsius)         
--------------------------------------------------------------------
1        Inlet  (s1)     60              42          25         Ok         
    
1        PMFPGA (s2)     80              60          36         Ok         
    
1        Crossbar(s3)    105             95          41         Ok              
    
2        Inlet  (s1)     60              42          25         Ok         
    
2        PMFPGA (s2)     80              60          35         Ok         
    
2        Crossbar(s3)    105             95          40         Ok            
    
3        MAC0Sn0(s2)     115             105         42         Ok         
    
3        MAC0Sn1(s3)     115             105         43         Ok         
    
3        MAC0-Buf0(s4)   115             105         35         Ok          
    
4        MAC0Sn0(s2)     115             105         35         Ok         
    
4        MAC0Sn1(s3)     115             105         36         Ok         
    
4        MAC0-Buf0(s4)   115             105         46         Ok         

```

**Help:** execute the command "show environment"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show hardware internal bigsur all-ports detail

**Output:**
```

Bigsur port sup1 card-config info:
        if_index           : 0x15010000
        instance index     : 0
        instance slot      : 17
        instance asic      : 0
        asic_eport         : 0
        logical_port       : 0
        front_port         : 0
        state              : va swi hw1 hw2 hwf 
        bigsur eport       : 0
        port_type          : sup-hi(1)
        type               : 5
        fw_instance        : 0
        speed              : 1

Bigsur port sup1 port-client-config info:
        admin_state        : en(1)
        mtu                : 2280
        duplexity          : full(2)
        auto_neg_state     : (on)1
        Fast 1G AN timer is: on
        speed              : 1000
        debounce time      : 100ms
        linkup_debounce time : 0ms
        sat_fabric_mode    : off(0x0)
        port_flow_ctrl     : 0
        class_flow_ctrl7-0 : 0000 0000
        class_flow_ctrl msk: rx 0x0, tx 0x0
Bigsur port sup1 port-oper info:
        link_state         : dn(2)
        oper speed         : 1000
        oper duplexity     : full(2)
        oper port_flow_ctrl: 0
        up count           : 0
        down count         : 0

Bigsur port sup1 miscellaneous info:
        slot               : 17
        mm_inst            : 0
        mm_mode            : SUP
        diag sts           : pass
        mac status polling : 0

Clause 73 AN:
        AN state               : 0 (AN_ST_IDLE)
        AN timer               : 0h
        Link Fail Inhibit timer: 0h
        AN disabled            : 0

MM Port Bring Up state-machine:
        MM port state          : 15 (PORT_ST_ENABLED)
        MM port timer          : 0h

Remote fault disable       : 0
Adaptive tuning disable    : 0
Link recovery disable      : 0
Link bring down disable    : 0
DFE tuning disable         : 0
Force QSFP removal         : 0
Force QSFP insertion       : 0
Force QSFP fiber type      : 0
Force QSFP copper type     : 0
 

SBus addresses:
        Serdes             : 47 (2fh)
        DFE Tune result   :

        FI block lock 0h: f
        FI block lock 1h: f
        FI block lock 2h: f
        FI block lock 3h: f

MAC statistics:
 MAC Statistic                  | Value                             
-------------------------------+-----------------------------------
TX_PKT_SIZE_LT_64              | 0
TX_PKT_SIZE_IS_64              | 0
TX_PKT_SIZE_IS_65_TO_127       | 2823262146
TX_PKT_SIZE_IS_128_TO_255      | 4795287371
TX_PKT_SIZE_IS_256_TO_511      | 117237451
TX_PKT_SIZE_IS_512_TO_1023     | 36844691
TX_PKT_SIZE_IS_1024_TO_1518    | 1414252162
TX_PKT_SIZE_IS_1519_TO_2047    | 79288810
TX_PKT_SIZE_IS_2048_TO_4095    | 0
TX_PKT_SIZE_IS_4095_TO_8191    | 0
TX_PKT_SIZE_IS_8192_TO_9216    | 0
TX_PKT_SIZE_GT_9216            | 0
TX_PKT_TOTAL                   | 13561139927
TX_PKT_OCTETS                  | 4246363557157
TX_PKT_GOOD                    | 13561139369
TX_PKT_UCAST                   | 211
TX_PKT_MCAST                   | 13561139158
TX_PKT_BCAST                   | 0
TX_PKT_VLAN                    | 0
TX_PKT_802.3x_PAUSE            | 0
TX_PKT_PER_PRIORITY_PAUSE      | 0
TX_PKT_FRAME_ERROR             | 558
RX_PKT_SIZE_LT_64              | 0
RX_PKT_SIZE_IS_64              | 0
RX_PKT_SIZE_IS_65_TO_127       | 779403235
RX_PKT_SIZE_IS_128_TO_255      | 247806975
RX_PKT_SIZE_IS_256_TO_511      | 46761364
RX_PKT_SIZE_IS_512_TO_1023     | 650380
RX_PKT_SIZE_IS_1024_TO_1518    | 148887
RX_PKT_SIZE_IS_1519_TO_2047    | 0
RX_PKT_SIZE_IS_2048_TO_4095    | 0
RX_PKT_SIZE_IS_4095_TO_8191    | 0
RX_PKT_SIZE_IS_8192_TO_9216    | 0
RX_PKT_SIZE_GT_9216            | 0
RX_PKT_TOTAL                   | 1074770841
RX_PKT_OCTETS                  | 130446639665
RX_PKT_GOOD                    | 7488
RX_PKT_UCAST                   | 0
RX_PKT_MCAST                   | 7488
RX_PKT_BCAST                   | 0
RX_PKT_VLAN                    | 0
RX_PKT_OVERSIZE                | 0
RX_PKT_TOOLONG                 | 0
RX_PKT_DISCARD                 | 0
RX_PKT_UNDERSIZE               | 0
RX_PKT_FRAGMENT                | 0
RX_PKT_CRC_NOT_STOMPED         | 0
RX_PKT_CRC_STOMPED             | 0
RX_PKT_IN_RANGE_ERR            | 1074763353
RX_PKT_JABBER                  | 0
RX_PKT_802.3x_PAUSE            | 0
RX_PKT_PER_PRIORITY_PAUSE      | 0
TX_PKT_GOOD_OCTETS             | 4246363466864
RX_PKT_GOOD_OCTETS             | 3784988
Done.
 
Bigsur port sup0 card-config info:
        if_index           : 0x15020000
        instance index     : 0
        instance slot      : 17
        instance asic      : 0
        asic_eport         : 1
        logical_port       : 1
        front_port         : 0
        state              : va swi hw1 hw2 hwf 
        bigsur eport       : 1
        port_type          : sup-lo(2)
        type               : 5
        fw_instance        : 1
        speed              : 1

Bigsur port sup0 port-client-config info:
        admin_state        : en(1)
        mtu                : 2280
        duplexity          : full(2)
        auto_neg_state     : (on)1
        Fast 1G AN timer is: on
        speed              : 1000
        debounce time      : 100ms
        linkup_debounce time : 0ms
        sat_fabric_mode    : off(0x0)
        port_flow_ctrl     : 0
        class_flow_ctrl7-0 : 0000 0000
        class_flow_ctrl msk: rx 0x0, tx 0x0
Bigsur port sup0 port-oper info:
        link_state         : dn(2)
        oper speed         : 1000
        oper duplexity     : full(2)
        oper port_flow_ctrl: 0
        up count           : 0
        down count         : 0

Bigsur port sup0 miscellaneous info:
        slot               : 17
        mm_inst            : 1
        mm_mode            : SUP
        diag sts           : pass
        mac status polling : 0

Clause 73 AN:
        AN state               : 0 (AN_ST_IDLE)
        AN timer               : 0h
        Link Fail Inhibit timer: 0h
        AN disabled            : 0

MM Port Bring Up state-machine:
        MM port state          : 15 (PORT_ST_ENABLED)
        MM port timer          : 0h

Remote fault disable       : 0
Adaptive tuning disable    : 0
Link recovery disable      : 0
Link bring down disable    : 0
DFE tuning disable         : 0
Force QSFP removal         : 0
Force QSFP insertion       : 0
Force QSFP fiber type      : 0
Force QSFP copper type     : 0
 

SBus addresses:
        Serdes             : 49 (31h)
        DFE Tune result   :

        FI block lock 0h: f
        FI block lock 1h: f
        FI block lock 2h: f
        FI block lock 3h: f

MAC statistics:
 MAC Statistic                  | Value                             
-------------------------------+-----------------------------------
TX_PKT_SIZE_LT_64              | 0
TX_PKT_SIZE_IS_64              | 0
TX_PKT_SIZE_IS_65_TO_127       | 0
TX_PKT_SIZE_IS_128_TO_255      | 0
TX_PKT_SIZE_IS_256_TO_511      | 0
TX_PKT_SIZE_IS_512_TO_1023     | 0
TX_PKT_SIZE_IS_1024_TO_1518    | 0
TX_PKT_SIZE_IS_1519_TO_2047    | 0
TX_PKT_SIZE_IS_2048_TO_4095    | 0
TX_PKT_SIZE_IS_4095_TO_8191    | 0
TX_PKT_SIZE_IS_8192_TO_9216    | 0
TX_PKT_SIZE_GT_9216            | 0
TX_PKT_TOTAL                   | 0
TX_PKT_OCTETS                  | 0
TX_PKT_GOOD                    | 0
TX_PKT_UCAST                   | 0
TX_PKT_MCAST                   | 0
TX_PKT_BCAST                   | 0
TX_PKT_VLAN                    | 0
TX_PKT_802.3x_PAUSE            | 0
TX_PKT_PER_PRIORITY_PAUSE      | 0
TX_PKT_FRAME_ERROR             | 0
RX_PKT_SIZE_LT_64              | 0
RX_PKT_SIZE_IS_64              | 0
RX_PKT_SIZE_IS_65_TO_127       | 232035201
RX_PKT_SIZE_IS_128_TO_255      | 78530597
RX_PKT_SIZE_IS_256_TO_511      | 49134037
RX_PKT_SIZE_IS_512_TO_1023     | 2680457976
RX_PKT_SIZE_IS_1024_TO_1518    | 150725864
RX_PKT_SIZE_IS_1519_TO_2047    | 69560111
RX_PKT_SIZE_IS_2048_TO_4095    | 0
RX_PKT_SIZE_IS_4095_TO_8191    | 0
RX_PKT_SIZE_IS_8192_TO_9216    | 0
RX_PKT_SIZE_GT_9216            | 0
RX_PKT_TOTAL                   | 3260443786
RX_PKT_OCTETS                  | 2176458795398
RX_PKT_GOOD                    | 64
RX_PKT_UCAST                   | 0
RX_PKT_MCAST                   | 64
RX_PKT_BCAST                   | 0
RX_PKT_VLAN                    | 0
RX_PKT_OVERSIZE                | 0
RX_PKT_TOOLONG                 | 0
RX_PKT_DISCARD                 | 0
RX_PKT_UNDERSIZE               | 0
RX_PKT_FRAGMENT                | 0
RX_PKT_CRC_NOT_STOMPED         | 0
RX_PKT_CRC_STOMPED             | 0
RX_PKT_IN_RANGE_ERR            | 3260443722
RX_PKT_JABBER                  | 0
RX_PKT_802.3x_PAUSE            | 0
RX_PKT_PER_PRIORITY_PAUSE      | 0
TX_PKT_GOOD_OCTETS             | 0
RX_PKT_GOOD_OCTETS             | 5602
Done.

Bigsur port 40gb1/1 card-config info:
        if_index           : 0x1a070000
        instance index     : 1
        instance slot      : 0
        instance asic      : 0
        asic_eport         : 0
        logical_port       : 0
        front_port         : 0
        state              : va swi hw1 hw2 hwf 
        bigsur eport       : 0
        port_type          : 40gbe(12)
        type               : 6
        fw_instance        : 0
        speed              : 5

Bigsur port 40gb1/1 port-client-config info:
        admin_state        : en(1)
        mtu                : 9260
        duplexity          : full(2)
        auto_neg_state     : (off)2
        Fast 1G AN timer is: on
        speed              : 40000
        debounce time      : 100ms
        linkup_debounce time : 0ms
        sat_fabric_mode    : off(0x0)
        port_flow_ctrl     : 0
        class_flow_ctrl7-0 : 0000 0000
        class_flow_ctrl msk: rx 0x0, tx 0x0
Bigsur port 40gb1/1 port-oper info:
        link_state         : up(1)
        oper speed         : 40000
        oper duplexity     : full(2)
        oper port_flow_ctrl: 0
        up count           : 1
        down count         : 0

Bigsur port 40gb1/1 miscellaneous info:
        slot               : 0
        mm_inst            : 0
        mm_mode            : 40G
        diag sts           : pass
        mac status polling : 1

Clause 73 AN:
        AN state               : 0 (AN_ST_IDLE)
        AN timer               : 0h
        Link Fail Inhibit timer: 0h
        AN disabled            : 0

MM Port Bring Up state-machine:
        MM port state          : 15 (PORT_ST_ENABLED)
        MM port timer          : 0h

Remote fault disable       : 0
Adaptive tuning disable    : 0
Link recovery disable      : 0
Link bring down disable    : 0
DFE tuning disable         : 0
Force QSFP removal         : 0
Force QSFP insertion       : 0
Force QSFP fiber type      : 0
Force QSFP copper type     : 0


SBus addresses:
        Serdes lanes 0-3   : 47 (2fh), 49 (31h), 51 (33h), 53 (35h) 
        DFE Tune result   :
                Lane 0:
                <0 0.ln0>:DFE A: 92 0x 0 0-2 1 1 41 -2
                <0 0.ln0>:DFE B: 93 0x 0 0-1 0-1 41  1
                <0 0.ln0> DFE Tune [0x67-B,D]: 98426/33/88226/21/5d005c  0
                Lane 1:
                <0 0.ln1>:DFE A: 98 0x-3 0-4 1 0 30  1
                <0 0.ln1>:DFE B: 97 0x 1 0-5 0 0 30  1
                <0 0.ln1> DFE Tune [0x67-B,D]: 240b0402/1/20b8002/1/610062  0
                Lane 2:
                <0 0.ln2>:DFE A: 90 0x-6 1-3 0 0 31 -1
                <0 0.ln2>:DFE B: 92 0x-6 0-2-1 0 31  0
                <0 0.ln2> DFE Tune [0x67-B,D]: 2b190002/31/2a09c402/20/5c005a  0
                Lane 3:
                <0 0.ln3>:DFE A: 101 0x-9 0-3 1 0 01 -1
                <0 0.ln3>:DFE B: 95 0x-8 0-4 1 0 01 -5
                <0 0.ln3> DFE Tune [0x67-B,D]: 3a090400/31/380b0400/37/5f0065  0

        FI block lock 0h: f
        FI block lock 1h: f
        FI block lock 2h: f
        FI block lock 3h: f

MAC statistics:
MAC Statistic                  | Value                             
-------------------------------+-----------------------------------
TX_PKT_SIZE_LT_64              | 0
TX_PKT_SIZE_IS_64              | 18664463
TX_PKT_SIZE_IS_65_TO_127       | 238330564005
TX_PKT_SIZE_IS_128_TO_255      | 208519091965
TX_PKT_SIZE_IS_256_TO_511      | 52508123590
TX_PKT_SIZE_IS_512_TO_1023     | 31784748589
TX_PKT_SIZE_IS_1024_TO_1518    | 68228288123
TX_PKT_SIZE_IS_1519_TO_2047    | 655538327602
TX_PKT_SIZE_IS_2048_TO_4095    | 12004245922
TX_PKT_SIZE_IS_4095_TO_8191    | 52439440105
TX_PKT_SIZE_IS_8192_TO_9216    | 103249777669
TX_PKT_SIZE_GT_9216            | 0
TX_PKT_TOTAL                   | 1422621272033
TX_PKT_OCTETS                  | 2416042841135777
TX_PKT_GOOD                    | 1422621272034
TX_PKT_UCAST                   | 1422526412248
TX_PKT_MCAST                   | 94859785
TX_PKT_BCAST                   | 1
TX_PKT_VLAN                    | 0
TX_PKT_802.3x_PAUSE            | 0
TX_PKT_PER_PRIORITY_PAUSE      | 0
TX_PKT_FRAME_ERROR             | 0
RX_PKT_SIZE_LT_64              | 0
RX_PKT_SIZE_IS_64              | 13493183
RX_PKT_SIZE_IS_65_TO_127       | 242229594382
RX_PKT_SIZE_IS_128_TO_255      | 170715085186
RX_PKT_SIZE_IS_256_TO_511      | 52962213518
RX_PKT_SIZE_IS_512_TO_1023     | 15954313004
RX_PKT_SIZE_IS_1024_TO_1518    | 154045143557
RX_PKT_SIZE_IS_1519_TO_2047    | 748698164670
RX_PKT_SIZE_IS_2048_TO_4095    | 11890366490
RX_PKT_SIZE_IS_4095_TO_8191    | 55672237707
RX_PKT_SIZE_IS_8192_TO_9216    | 103016468728
RX_PKT_SIZE_GT_9216            | 0
RX_PKT_TOTAL                   | 1555197080425
RX_PKT_OCTETS                  | 2684618846662334
RX_PKT_GOOD                    | 1555196893875
RX_PKT_UCAST                   | 1268271913848
RX_PKT_MCAST                   | 271281819207
RX_PKT_BCAST                   | 15643160820
RX_PKT_VLAN                    | 0
RX_PKT_OVERSIZE                | 0
RX_PKT_TOOLONG                 | 0
RX_PKT_DISCARD                 | 0
RX_PKT_UNDERSIZE               | 0
RX_PKT_FRAGMENT                | 0
RX_PKT_CRC_NOT_STOMPED         | 315
RX_PKT_CRC_STOMPED             | 186235
RX_PKT_IN_RANGE_ERR            | 0
RX_PKT_JABBER                  | 0
RX_PKT_802.3x_PAUSE            | 0
RX_PKT_PER_PRIORITY_PAUSE      | 0
TX_PKT_GOOD_OCTETS             | 2416042841147997
RX_PKT_GOOD_OCTETS             | 2684618748170285


XCVR port info:
Card Config info
        logical_port       : 0
        sfp_ctrl_bigsur    : 0
        sfp_ctrl_port      : 0
        phy_bigsur         : 0
        phy_mdio_addr      : 0
        phy_mdio_master    : 1
        phy_reset_bigsur   : 0
        phy_reset_spio     : 0
        phy_prom_shared    : 0
        Serdes txdata[0]   : 0x0
        Serdes txdata[1]   : 0x0
        Serdes txdata[2]   : 0x0
        Serdes txdata[3]   : 0x0
        phy_pmd_tx[0]      : 0x0
        phy_pmd_tx[1]      : 0x0
        phy_pmd_tx[2]      : 0x0
Dev address info
        pma_pmd_devaddr    : 1
        pcs_devaddr        : 3
        phyxs_devaddr      : 4
        xcvr_devaddr       : 1
Misc info
        phy_present        : 0
        phy_type           : 0
        sfp_acc_type       : 8
        dfe_timer          : 0
        dfe_timer_running  : 0
        init_wait_count    : 0
        do_tx_disable_clr  : 0
        tx_disable_clr_cnt : 0
        qsa_status         : 0
        Connector type     : FIBER
        usb_bus_num        : 1
        usb_dev_num        : 8
        usb_priv           : available
        Reset done         : N
Xcvr flags
        XCVR_FLAG_PRESENT              : Y
        XCVR_FLAG_XCVR_NOT_SFP         : Y
        XCVR_FLAG_10G_CAPABLE          : Y
        XCVR_FLAG_CKSUM_OK             : Y
        XCVR_FLAG_SECURITY_CRC_OK      : Y
        XCVR_FLAG_CISCO_CHK_OK         : N
        XCVR_FLAG_DDM_CAPABLE          : N
        XCVR_FLAG_PMA_PMD_PRESENT      : N
        XCVR_FLAG_PCS_PRESENT          : N
        XCVR_FLAG_PHYXS_PRESENT        : N
        XCVR_FLAG_XCVR_OPERATIONAL     : Y
        XCVR_FLAG_PMA_PMD_LOW_PWR_MODE : N
        XCVR_FLAG_PCS_LOW_PWR_MODE     : N
        XCVR_FLAG_PHYXS_LOW_PWR_MODE   : N
        XCVR_FLAG_LINK_UP              : Y
        XCVR_FLAG_TYPE_FIBER           : Y
        XCVR_FLAG_SPROM_READ_OK        : Y
Link states:HF-HwFailure, ED-ErrDisabled, DB-Debounced, UP and DN-Down

Port 0/0:
State: UP
XCVR insert debounce timer not running
XCVR link debounce timer not running
XCVR linkup debounce timer not running
XCVR presence detect timer running
TX enable signal is off
Debounce timeout: 0.030 seconds

Linkup Debounce timeout: 0.000 seconds

Link up : 941735 usecs after Sun Oct 27 06:14:48 2019
Link dn debounce start : 0 usecs after Thu Jan  1 00:00:00 1970
Link debounce end : 0 usecs after Thu Jan  1 00:00:00 1970

Counters:
  Interrupt cntrs:
  Bit error cntrs:
    Bit Error Rate: 0x0000000000000000 Bit Error Rate(since linkup): 0x00000000
    Error blocks  : 0x0000000000000000 Error blocks(since linkup)  : 0x00000000
  Link cntrs:
    Link up: 0x1 (1)
    Link dn: 0x0 (0)
    Link debounced with link up: 0x0 (0)
    Link debounced with link up since  last enable: 0x0 (0)
Done.

Bigsur port 40gb1/2 card-config info:
        if_index           : 0x1a071000
        instance index     : 1
        instance slot      : 0
        instance asic      : 0
        asic_eport         : 1
        logical_port       : 1
        front_port         : 1
        state              : va swi hw1 hw2 hwf 
        bigsur eport       : 1
        port_type          : 40gbe(12)
        type               : 6
        fw_instance        : 4
        speed              : 5

 Bigsur port 40gb1/2 port-client-config info:
        admin_state        : en(1)
        mtu                : 9260
        duplexity          : full(2)
        auto_neg_state     : (off)2
        Fast 1G AN timer is: on
        speed              : 40000
        debounce time      : 100ms
        linkup_debounce time : 0ms
        sat_fabric_mode    : off(0x0)
        port_flow_ctrl     : 0
        class_flow_ctrl7-0 : 0000 0000
        class_flow_ctrl msk: rx 0x0, tx 0x0
Bigsur port 40gb1/2 port-oper info:
        link_state         : up(1)
        oper speed         : 40000
        oper duplexity     : full(2)
        oper port_flow_ctrl: 0
        up count           : 1
        down count         : 0

Bigsur port 40gb1/2 miscellaneous info:
        slot               : 0
        mm_inst            : 1
        mm_mode            : 40G
        diag sts           : pass
        mac status polling : 1

Clause 73 AN:
        AN state               : 0 (AN_ST_IDLE)
        AN timer               : 0h
        Link Fail Inhibit timer: 0h
        AN disabled            : 0

MM Port Bring Up state-machine:
        MM port state          : 15 (PORT_ST_ENABLED)
        MM port timer          : 0h

Remote fault disable       : 0
Adaptive tuning disable    : 0
 Link recovery disable      : 0
Link bring down disable    : 0
DFE tuning disable         : 0
Force QSFP removal         : 0
Force QSFP insertion       : 0
Force QSFP fiber type      : 0
Force QSFP copper type     : 0


SBus addresses:
        Serdes lanes 0-3   : 55 (37h), 57 (39h), 59 (3bh), 61 (3dh) 
        DFE Tune result   :
                Lane 0:
                <0 0.ln4>:DFE A: 97 0x-3 0-1 0 0 40 -2
                <0 0.ln4>:DFE B: 100 0x-2 0-2 1 0 40 -1
                <0 0.ln4> DFE Tune [0x67-B,D]: 24088006/13/26098406/11/640061  0
                Lane 1:
                <0 0.ln5>:DFE A: 98 0x-6 0-5 1 0 01  0
                <0 0.ln5>:DFE B: 100 0x-8 0-5 1 0 01  1
                <0 0.ln5> DFE Tune [0x67-B,D]: 2a0b8400/20/380b8400/21/640062  0
                Lane 2:
                <0 0.ln6>:DFE A: 95 0x-4 0-2 0 0 41  1
                <0 0.ln6>:DFE B: 90 0x-1 0-3 0-1 41  1
                <0 0.ln6> DFE Tune [0x67-B,D]: 2c098006/21/22090226/21/5a005f  0
                Lane 3:
                <0 0.ln7>:DFE A: 102 0x-9 0-3 2 1 01  0
                <0 0.ln7>:DFE B: 103 0x-b 0 0 0 0 01  0
                <0 0.ln7> DFE Tune [0x67-B,D]: 3a090c20/20/3c000000/20/670066  0

        FI block lock 0h: f
        FI block lock 1h: f
        FI block lock 2h: f
        FI block lock 3h: f

MAC statistics:
MAC Statistic                  | Value                             
-------------------------------+-----------------------------------
TX_PKT_SIZE_LT_64              | 0
TX_PKT_SIZE_IS_64              | 0
TX_PKT_SIZE_IS_65_TO_127       | 221696905275
TX_PKT_SIZE_IS_128_TO_255      | 194761555926
TX_PKT_SIZE_IS_256_TO_511      | 52118735247
TX_PKT_SIZE_IS_512_TO_1023     | 28101578047
TX_PKT_SIZE_IS_1024_TO_1518    | 51755254532
TX_PKT_SIZE_IS_1519_TO_2047    | 708624997790
TX_PKT_SIZE_IS_2048_TO_4095    | 12210800606
TX_PKT_SIZE_IS_4095_TO_8191    | 47301205375
TX_PKT_SIZE_IS_8192_TO_9216    | 101005431860
TX_PKT_SIZE_GT_9216            | 0
TX_PKT_TOTAL                   | 1417576464658
TX_PKT_OCTETS                  | 2423284879830834
TX_PKT_GOOD                    | 1417576464659
TX_PKT_UCAST                   | 1416864425571
TX_PKT_MCAST                   | 388555955
TX_PKT_BCAST                   | 323483133
TX_PKT_VLAN                    | 0
TX_PKT_802.3x_PAUSE            | 0
TX_PKT_PER_PRIORITY_PAUSE      | 0
TX_PKT_FRAME_ERROR             | 0
RX_PKT_SIZE_LT_64              | 0
RX_PKT_SIZE_IS_64              | 13723786
RX_PKT_SIZE_IS_65_TO_127       | 236486911378
RX_PKT_SIZE_IS_128_TO_255      | 181809874494
RX_PKT_SIZE_IS_256_TO_511      | 58190299575
RX_PKT_SIZE_IS_512_TO_1023     | 15742772244
RX_PKT_SIZE_IS_1024_TO_1518    | 94593384424
RX_PKT_SIZE_IS_1519_TO_2047    | 548720562260
RX_PKT_SIZE_IS_2048_TO_4095    | 12264718059
RX_PKT_SIZE_IS_4095_TO_8191    | 54765198272
RX_PKT_SIZE_IS_8192_TO_9216    | 103065149039
RX_PKT_SIZE_GT_9216            | 0
RX_PKT_TOTAL                   | 1305652593531
RX_PKT_OCTETS                  | 2287031513403995
RX_PKT_GOOD                    | 1305652327716
RX_PKT_UCAST                   | 1035478421252
RX_PKT_MCAST                   | 259688831694
RX_PKT_BCAST                   | 10485074770
RX_PKT_VLAN                    | 0
RX_PKT_OVERSIZE                | 0
RX_PKT_TOOLONG                 | 0
RX_PKT_DISCARD                 | 0
RX_PKT_UNDERSIZE               | 0
RX_PKT_FRAGMENT                | 0
RX_PKT_CRC_NOT_STOMPED         | 5
RX_PKT_CRC_STOMPED             | 265810
RX_PKT_IN_RANGE_ERR            | 0
RX_PKT_JABBER                  | 0
RX_PKT_802.3x_PAUSE            | 0
RX_PKT_PER_PRIORITY_PAUSE      | 0
TX_PKT_GOOD_OCTETS             | 2423284879835690
RX_PKT_GOOD_OCTETS             | 2287031285388567
 

XCVR port info:
Card Config info
        logical_port       : 1
        sfp_ctrl_bigsur    : 0
        sfp_ctrl_port      : 1
        phy_bigsur         : 0
        phy_mdio_addr      : 0
        phy_mdio_master    : 1
        phy_reset_bigsur   : 0
        phy_reset_spio     : 0
        phy_prom_shared    : 0
        Serdes txdata[0]   : 0x0
        Serdes txdata[1]   : 0x0
        Serdes txdata[2]   : 0x0
        Serdes txdata[3]   : 0x0
        phy_pmd_tx[0]      : 0x0
        phy_pmd_tx[1]      : 0x0
        phy_pmd_tx[2]      : 0x0
Dev address info
        pma_pmd_devaddr    : 1
        pcs_devaddr        : 3
        phyxs_devaddr      : 4
        xcvr_devaddr       : 1
 Misc info
        phy_present        : 0
        phy_type           : 0
        sfp_acc_type       : 8
        dfe_timer          : 0
        dfe_timer_running  : 0
        init_wait_count    : 0
        do_tx_disable_clr  : 0
        tx_disable_clr_cnt : 0
        qsa_status         : 0
        Connector type     : FIBER
        usb_bus_num        : 1
        usb_dev_num        : 8
        usb_priv           : available
        Reset done         : N
Xcvr flags
        XCVR_FLAG_PRESENT              : Y
        XCVR_FLAG_XCVR_NOT_SFP         : Y
        XCVR_FLAG_10G_CAPABLE          : Y
        XCVR_FLAG_CKSUM_OK             : Y
        XCVR_FLAG_SECURITY_CRC_OK      : Y
        XCVR_FLAG_CISCO_CHK_OK         : N
        XCVR_FLAG_DDM_CAPABLE          : N
        XCVR_FLAG_PMA_PMD_PRESENT      : N
        XCVR_FLAG_PCS_PRESENT          : N
        XCVR_FLAG_PHYXS_PRESENT        : N
        XCVR_FLAG_XCVR_OPERATIONAL     : Y
        XCVR_FLAG_PMA_PMD_LOW_PWR_MODE : N
        XCVR_FLAG_PCS_LOW_PWR_MODE     : N
        XCVR_FLAG_PHYXS_LOW_PWR_MODE   : N
        XCVR_FLAG_LINK_UP              : Y
        XCVR_FLAG_TYPE_FIBER           : Y
        XCVR_FLAG_SPROM_READ_OK        : Y
Link states:HF-HwFailure, ED-ErrDisabled, DB-Debounced, UP and DN-Down

Port 0/1:
State: UP
XCVR insert debounce timer not running
XCVR link debounce timer not running
XCVR linkup debounce timer not running
XCVR presence detect timer running
TX enable signal is on
Debounce timeout: 0.030 seconds

Linkup Debounce timeout: 0.000 seconds
 
Link up : 294003 usecs after Sun Oct 27 06:14:53 2019
Link dn debounce start : 0 usecs after Thu Jan  1 00:00:00 1970
Link debounce end : 0 usecs after Thu Jan  1 00:00:00 1970

Counters:
  Interrupt cntrs:
  Bit error cntrs:
    Bit Error Rate: 0x0000000000000000 Bit Error Rate(since linkup): 0x00000000
    Error blocks  : 0x0000000000000000 Error blocks(since linkup)  : 0x00000000
  Link cntrs:
    Link up: 0x1 (1)
    Link dn: 0x0 (0)
    Link debounced with link up: 0x0 (0)
    Link debounced with link up since  last enable: 0x0 (0)
Done.

```

**Help:** execute the command "show hardware internal bigsur all-ports detail"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show lldp neighbors detail

**Output:**
```
Capability codes:
  (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
  (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other
 Device ID            Local Intf      Hold-time  Capability  Port ID  

Chassis id: 0014.1c57.a48b
Port id: Fa1/0/9
Local Port id: mgmt0
Port Description: FastEthernet1/0/9
System Name: Switch.cisco.com
System Description: Cisco IOS Software, C3750 Software (C3750-IPBASEK9-M), Version 12.2(44)SE2, RELEASE SOFTWARE (fc2)
Copyright (c) 1986-2008 by Cisco Systems, Inc.
Compiled Thu 01-May-08 15:42 by antonino
Time remaining: 91 seconds
System Capabilities: B, R
Enabled Capabilities: B, R
Management Address: 10.30.140.1
Vlan ID: 100


Chassis id: 5087.89a1.d8d6
Port id: Ethernet1/1
Local Port id: Eth1/1
 Port Description: Ethernet1/1
System Name: n9k2.company.com
System Description: Cisco Nexus Operating System (NX-OS) Software 7.0(3)I4(1)
TAC support: http://www.cisco.com/tac
 Copyright (c) 2002-2016, Cisco Systems, Inc. All rights reserved.
Time remaining: 93 seconds
System Capabilities: B, R
Enabled Capabilities: B, R
Management Address: 10.30.140.21
Vlan ID: 1


Chassis id: 5087.89a1.d8d7
Port id: Ethernet1/2
Local Port id: Eth1/2
Port Description: Ethernet1/2
System Name: n9k2.company.com
System Description: Cisco Nexus Operating System (NX-OS) Software 7.0(3)I4(1)
TAC support: http://www.cisco.com/tac
Copyright (c) 2002-2016, Cisco Systems, Inc. All rights reserved.
Time remaining: 93 seconds
System Capabilities: B, R
Enabled Capabilities: B, R
Management Address: 10.30.140.21
 Vlan ID: 1


Chassis id: 547f.eeaf.7818
Port id: Ethernet1/49
Local Port id: Eth2/2
Port Description: Ethernet1/49
System Name: N3K.cisconxapi.com
 System Description: Cisco Nexus Operating System (NX-OS) Software 6.0(2)U4(1)
 TAC support: http://www.cisco.com/tac
Copyright (c) 2002-2014, Cisco Systems, Inc. All rights reserved.
Time remaining: 93 seconds
System Capabilities: B, R
Enabled Capabilities: B, R
Management Address: 10.30.140.30
Vlan ID: 1

Total entries displayed: 4

```

**Help:** execute the command "show lldp neighbors detail"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show interface snmp-ifindex

**Output:**
```

--------------------------------------------------------------------------------
Port             IFMIB Ifindex (hex)
--------------------------------------------------------------------------------
mgmt0           83886080   (0x5000000 )
Eth9/1          440401920  (0x1a400000)
Eth9/2          440406016  (0x1a401000)
Eth9/3          440410112  (0x1a402000)
Eth9/4          440414208  (0x1a403000)
Eth9/4.10       440414218  (0x1a40300a)
Eth9/5/1        960659456  (0x39428000)
Eth9/5/2        960663552  (0x39429000)
Eth9/5/3        960667648  (0x3942a000)
Eth9/5/4        960671744  (0x3942b000)
Eth9/6/1        960700416  (0x39432000)
Eth9/6/2        960704512  (0x39433000)
Eth9/6/3        960708608  (0x39434000)
Eth9/6/4        960712704  (0x39435000)
Eth9/7          440426496  (0x1a406000)
Eth9/8          440430592  (0x1a407000)
Eth9/9          440434688  (0x1a408000)
Eth9/10         440438784  (0x1a409000)
Eth9/11         440442880  (0x1a40a000)
Eth9/12         440446976  (0x1a40b000)
Po1             369098752  (0x16000000)
Lo0             335544320  (0x14000000)
Vlan1           151126017  (0x9020001)
```

**Help:** execute the command "show interface snmp-ifindex"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show license usage

**Output:**
```

Feature                      Ins  Lic   Status Expiry Date Comments
                                 Count
--------------------------------------------------------------------------------
MPLS_PKG                      No    -   Unused             Grace 10D 1H
STORAGE-ENT                   No    -   Unused             Grace 20D 6H
VDC_LICENSES                  No    0   Unused             -
ENTERPRISE_PKG                No    -   Unused             -
FCOE-N7K-F132XP               No    0   Unused             -
FCOE-N7K-F248XP               No    0   Unused             -
ENHANCED_LAYER2_PKG           No    -   Unused             Grace 20D 6H
SCALABLE_SERVICES_PKG         No    -   Unused             -
TRANSPORT_SERVICES_PKG        Yes   -   Unused Never       -
LAN_ADVANCED_SERVICES_PKG     Yes   -   Unused Never       -
LAN_ENTERPRISE_SERVICES_PKG   Yes   -   In use Never       -
--------------------------------------------------------------------------------

```

**Help:** execute the command "show license usage"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip adjacency

**Output:**
```

Flags: # - Adjacencies Throttled for Glean
       G - Adjacencies of vPC peer with G/W bit

IP Adjacency Table for VRF default
Total number of entries: 8
Address         MAC Address     Pref Source     Interface
10.110.100.142  002a.6a11.62c1  50   arp        Vlan1800         G
10.110.100.178  78bc.1af1.ca61  50   arp        Vlan1801
10.110.100.179  002a.6a11.62c1  50   arp        Vlan1801         G
10.100.1.22     002a.6a11.62c1  50   arp        Vlan10           G
10.100.1.24     0040.9d99.f6f6  50   arp        Vlan10
10.100.150.3    0050.5694.bb20  50   arp        Vlan150
10.100.150.5    002a.6a11.62c1  50   arp        Vlan150          G
10.100.150.6    0050.568c.2110  50   arp        Vlan150
```

**Help:** execute the command "show ip adjacency"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show spanning-tree root

**Output:**
```
                                        Root  Hello Max Fwd
Vlan                   Root ID          Cost  Time  Age Dly  Root Port
---------------- -------------------- ------- ----- --- ---  ----------------
VLAN0001             1 1211.a111.1111       0    2   20  10  This bridge is root
VLAN0002            10 1211.a111.1112       3    2   20  10    port-channel10
VLAN0003          1111 1211.a111.1113       1    2   20  10     port-channel1
VLAN0004            11 1211.a111.1114       0    2   20  10  This bridge is root
```

**Help:** execute the command "show spanning-tree root"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show bgp vrf all ipv4 unicast neighbors routes

**Output:**
```
Can't find neighbor 10.1.1.1 in VRF TEST_1

Peer 10.1.1.1 routes for address family IPv4 Unicast:
BGP table version is 401423, Local Router ID is 10.10.10.10
Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup, 2 - best2

   Network            Next Hop            Metric     LocPrf     Weight Path
*>e10.20.20.0/27      10.1.1.1                         5000          0 100 200 i
*>e10.10.202.0/30     10.10.2.1                                      0 64102 64202 i
*>l100.100.100.100/30 0.0.0.0                           100      32768 i
x e100.100.100.104/30 10.10.2.1                                      0 64102 64002 i
*>e                   10.10.1.1                                      0 64101 64002 i
*>e100.100.100.108/30 10.10.2.1                                      0 64102 {{64201 64202}} i
*>e100.100.100.112/30 10.10.2.1                                      0 64102 {{64201 64202}} 64203 i
 *>e100.100.100.114/30 10.10.2.1                                      0 64102 {{64201 64202}} 64203 64500.2345 i
*>e100.100.100.116/30 10.10.2.1                                      0 {{64102 64201 64202}} 64203 64500.2345 i
*>e100.100.100.118/30 10.10.2.1                                      0 64102.444 {{64201 64202}} 64203 64500.2345 i
*>e100.100.100.120/30 10.10.2.1                                      0 {{64102.333 64201 64202}} 64203 64500.2345 i

```

**Help:** execute the command "show bgp vrf all ipv4 unicast neighbors routes"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show vpc

**Output:**
```
Legend:
                (*) - local vPC is down, forwarding via vPC peer-link

vPC domain id                     : 100
Peer status                       : peer link is down
vPC keep-alive status             : Suspended (Destination IP not reachable)
Configuration consistency status  : failed
 Per-vlan consistency status       : success
Configuration inconsistency reason: Consistency Check Not Performed
Type-2 inconsistency reason       : Consistency Check Not Performed
vPC role                          : none established
 Number of vPCs configured         : 0
Peer Gateway                      : Disabled
 Dual-active excluded VLANs        : -
Graceful Consistency Check        : Disabled (due to peer configuration)
Auto-recovery status              : Disabled
 Delay-restore status              : Timer is off.(timeout = 30s)
Delay-restore SVI status          : Timer is off.(timeout = 10s)

vPC Peer-link status
---------------------------------------------------------------------
id   Port   Status Active vlans
--   ----   ------ --------------------------------------------------
1    Po12   down   -
2    Po13   up     10

```

**Help:** execute the command "show vpc"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show access-lists

**Output:**
```
IP access list TEST-ACL
        statistics per-entry
        10 remark established connections
        20 permit tcp any 10.10.10.0/24 established [match=66]
        30 remark Test
        40 permit tcp 1.1.1.1/32 any eq 80 [match=0]
        50 permit tcp 2.2.2.2/32 any eq 443 [match=0]
        60 remark Allow NAT IP
        70 permit tcp 3.3.3.3/32 any eq 80 [match=0]
        80 remark TestRemark
        90 permit tcp 4.4.4.4/32 any eq 443 [match=0]
        100 remark Test Remark
        110 permit tcp 5.5.5.5/32 any eq 80 [match=0]
        120 remark AnotherOne
        130 permit tcp 6.6.6.6/32 any eq 443 [match=0]
        140 remark addTest: contains list should not become name
        150 remark addTest: dont "miss" 'me'

```

**Help:** execute the command "show access-lists"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show mac address-table

**Output:**
```
Legend:
        * - primary entry, G - Gateway MAC, (R) - Routed MAC, O - Overlay MAC
        age - seconds since last seen,+ - primary entry using vPC Peer-Link,
        (T) - True, (F) - False
     VLAN       MAC Address       Type     age    Secure  NTFY     Ports
------------+-----------------+----------+-------+------+------+------------------
G    100      5087.89a1.de75     static     -        F      F    sup-eth1(R)
*    145        000a.000a.000a   static     -        F      F    Drop
*    145        000e.000e.000e   static     -        F      F    Po10


```

**Help:** execute the command "show mac address-table"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show fex id

**Output:**
```
FEX: 102 Description: ATL1-AS3P   state: Online
  FEX version: 7.2(1)N1(1) [Switch version: 7.2(1)N1(1)]
  Extender Serial: SSI16340AR0
  Extender Model: N2K-C2248TP-E-1GE,  Part No: 73-13671-01
  Pinning-mode: static    Max-links: 1
  Fabric port for control traffic: Eth1/31
  FCoE Admin: false
  FCoE Oper: true
  FCoE FEX AA Configured: false
  Fabric interface state:
    Po102 - Interface Up. State: Active
    Eth1/31 - Interface Up. State: Active
    Eth2/15 - Interface Up. State: Active

```

**Help:** execute the command "show fex id"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip pim rp vrf all

**Output:**
```
PIM RP Status Information for VRF "default"
BSR disabled
Auto-RP disabled
BSR RP Candidate policy: None
BSR RP policy: None
Auto-RP Announce policy: None
Auto-RP Discovery policy: None


PIM RP Status Information for VRF "red"
BSR disabled
Auto-RP disabled
BSR RP Candidate policy: None
 BSR RP policy: None
Auto-RP Announce policy: None
Auto-RP Discovery policy: None



```

**Help:** execute the command "show ip pim rp vrf all"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show vdc

**Output:**
```

Switchwide mode is m1 f1 m1xl f2 m2xl f2e f3

vdc_id  vdc_name                          state               mac                 type        lc
------  --------                          -----               ----------          ---------   ------
1       not1.barr1                        active              e4:c7:22:0c:67:c1   Admin       None
2       foo1.bar1.bazz1                   active              e4:c7:22:0c:67:c2   Ethernet    f2e
3       foo2.bar2.bazz2                   active              e4:c7:22:0c:67:c3   Ethernet    f2e

```

**Help:** execute the command "show vdc"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show forwarding adjacency

**Output:**
```
IPv4 adjacency information

next-hop         rewrite info    interface    Origin AS  Peer AS  Neighbor
-------------- --------------- ------------- ---------- --------- --------------
10.111.1.3      cc16.7c1f.9852 Vlan10
10.111.1.4      cc16.7c1f.6900 Vlan10
10.111.1.5      84b8.025a.f786 Vlan10
10.111.1.6      a89d.2121.bc7b Vlan10
10.5.111.213    0050.528c.5b4c Vlan182
10.5.111.221    002a.6312.6ac1 Vlan182
10.111.254.6    002a.6312.6ac1 Vlan254
10.6.140.234    000e.b6b2.ff01 Ethernet1/16
10.6.140.238    54a2.72da.b651 Ethernet1/16
```

**Help:** execute the command "show forwarding adjacency"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip ospf neighbor

**Output:**
```
router1# sh ip ospf neighbors vrf all 
 OSPF Process ID 1111 VRF CUSTVRF1
 Total number of neighbors: 3
 Neighbor ID     Pri State            Up Time  Address         Interface
 10.0.0.1          1 FULL/ -          8w6d     11.11.11.11     Vlan999 
 10.0.0.2          1 FULL/ -          5w6d     22.22.22.22     Po1 
 10.0.0.3          1 FULL/ -          5w6d     44.44.44.44     Po2 
 OSPF Process ID 2222 VRF CUSTVRF2
 Total number of neighbors: 1
 Neighbor ID     Pri State            Up Time  Address         Interface
 10.0.0.4          1 FULL/ -          8w6d     55.55.55.55     Vlan1000 
 OSPF Process ID 3333 VRF CUSTVRF2
 Total number of neighbors: 2
 Neighbor ID     Pri State            Up Time  Address         Interface
 10.0.0.5          1 FULL/ -          7w2d     66.66.66.66     Po3 
 10.0.0.6          1 INIT/DROTHER     -        77.77.77.77     Po4 

```

**Help:** execute the command "show ip ospf neighbor"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip bgp summary vrf

**Output:**
```
BGP summary information for VRF AMB, address family IPv4 Unicast
 
 BGP summary information for VRF AMB, address family IPv6 Unicast
 
BGP summary information for VRF BLU, address family IPv4 Unicast
BGP router identifier 172.16.101.101, local AS number 65161
BGP table version is 2301549, IPv4 Unicast config peers 1, capable peers 1
827 network entries and 1406 paths using 105308 bytes of memory
BGP attribute entries [107/18404], BGP AS path entries [26/272]
 BGP community entries [0/0], BGP clusterlist entries [6/24]
 
Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
10.25.113.1     4 65001 21968368 22451737  2301549    0    0    24w2d 0        
 
BGP summary information for VRF BLU, address family IPv6 Unicast
 
BGP summary information for VRF GRN, address family IPv4 Unicast
 
BGP summary information for VRF GRN, address family IPv6 Unicast
 
BGP summary information for VRF GRY, address family IPv4 Unicast
 
BGP summary information for VRF GRY, address family IPv6 Unicast
 
BGP summary information for VRF NPE, address family IPv4 Unicast
 
BGP summary information for VRF NPE, address family IPv6 Unicast
 
BGP summary information for VRF RED, address family IPv4 Unicast
 
BGP summary information for VRF RED, address family IPv6 Unicast
 
BGP summary information for VRF TRI, address family IPv4 Unicast
BGP router identifier 172.16.101.123, local AS number 65161
BGP table version is 8526, IPv4 Unicast config peers 1, capable peers 1
55 network entries and 102 paths using 9940 bytes of memory
 BGP attribute entries [11/1892], BGP AS path entries [8/80]
BGP community entries [0/0], BGP clusterlist entries [6/24]
 
Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
10.23.1.74      4 65171 3078819 3074406     8526    0    0     2w5d 24    
 
BGP summary information for VRF TRI, address family IPv6 Unicast
 
BGP summary information for VRF default, address family IPv4 Unicast
BGP router identifier 172.16.101.37, local AS number 65161
BGP table version is 14450, IPv4 Unicast config peers 5, capable peers 5
36 network entries and 56 paths using 11184 bytes of memory
BGP attribute entries [24/4128], BGP AS path entries [13/102]
BGP community entries [0/0], BGP clusterlist entries [6/24]
 
Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
172.16.14.2     4 65164 8429603 8531693    14450    0    0    1d08h 2        
172.16.31.1     4 65191 8081582 8260415    14450    0    0     1w0d 2        
172.16.31.17    4 65193 8167842 8348036    14450    0    0     1w0d 2        
172.16.102.2    4 65161 1166456 1165743    14450    0    0     2y0w 28       
172.16.151.2    4 65162 1074723 1073151    14450    0    0     1w1d 18       
 
BGP summary information for VRF default, address family IPv6 Unicast
 
BGP summary information for VRF default, address family VPNv4 Unicast
 
BGP summary information for VRF default, address family VPNv6 Unicast
 
BGP summary information for VRF default, address family IPv4 MVPN
 
BGP summary information for VRF default, address family IPv6 MVPN
 
BGP summary information for VRF default, address family L2VPN EVPN
BGP router identifier 172.16.101.37, local AS number 65161
BGP table version is 63025110, L2VPN EVPN config peers 7, capable peers 7
4630 network entries and 8017 paths using 1210960 bytes of memory
BGP attribute entries [796/136912], BGP AS path entries [31/334]
BGP community entries [0/0], BGP clusterlist entries [6/24]
 
Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
172.23.129.240  4 65191 8081498 8246843 63025110    0    0     1w0d 6        
172.23.133.240  4 65193 8167863 8334538 63025110    0    0     1w0d 6        
172.16.101.33   4 65161 40997672 23273121 63025110    0    0    2y11w 1782     
172.16.101.34   4 65161 40992491 23273008 63025110    0    0    2y11w 1782     
172.16.201.37   4 65162 23261970 26520909 63025110    0    0     1w1d 698      
172.16.201.38   4 65162 23309853 26564632 63025110    0    0     2y2w 698      
172.16.255.42   4 65164 20901792 21346308 63025110    0    0    1d08h 14       
 
Neighbor        T    AS PfxRcd     Type-2     Type-3     Type-4     Type-5   
172.23.129.240  I 65191 6          0          0          0          6        
172.23.133.240  I 65193 6          0          0          0          6        
172.16.101.33   I 65161 1782       1434       14         0          334      
172.16.101.34   I 65161 1782       1434       14         0          334      
172.16.201.37   E 65162 698        481        7          0          210      
172.16.201.38   E 65162 698        481        7          0          210      
172.16.255.42   I 65164 14         0          0          0          14


Value Filldown VRF (\S+)
 Value Filldown ADDRESS_FAMILY (\S+\s\S+)
Value Filldown ROUTER_ID (\d+?\ .\d+?\.\d+?\.\d+?)
Value Filldown LOCAL_AS (\d+)
Value Required BGP_NEIGH (\d+?\.\d+?\.\d+?\.\d+?)
Value BGP_VER (\d)
Value Required NEIGH_AS (\S+)
Value MSG_RCVD (\d+)
Value MSG_SENT (\d+)
Value TBLVER (\d+)
 Value IN_QUEUE (\d+)
Value OUT_QUEUE (\d+)
Value UP_DOWN (\S+)
Value STATE_PFXRCD (\S+?\s+\S+?|\S+?)

```

**Help:** execute the command "show ip bgp summary vrf"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show fex

**Output:**
```

  FEX         FEX           FEX              FEX              Fex
Number    Description      State            Model            Serial
------------------------------------------------------------------------
102      ATL1-AS3P                Online   N2K-C2248TP-E-1GE   SSI16340AR0
103      ATL1-AS5P                Online   N2K-C2248TP-E-1GE   SSI16350CPC
104      ATL1-AS7P                Online   N2K-C2248TP-E-1GE   SSI16340AKE
105      ATL1-AS9P                Online   N2K-C2248TP-E-1GE   SSI16350BJ9
121    ATL1-AS1PR2                Online   N2K-C2248TP-E-1GE   SSI165102M7
122    ATL1-AS3PR2 test           Online   N2K-C2248TP-E-1GE   SSI16460ARS
123    ATL1-AS3PR2 test test      Online   N2K-C2248TP-E-1GE   SSI16460AR1
124    ATL1-AS3PR2  Test          Online   N2K-C2248TP-E-1GE   SSI16460AR2
125    ATL1-AS3PR2 Test  test     Online   N2K-C2248TP-E-1GE   SSI16460AR3


```

**Help:** execute the command "show fex"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show environment temperature

**Output:**
```


Temperature
-------------------------------------------------------------------------
Module  Sensor             MajorThresh   MinorThres   CurTemp     Status
                            (Celsius)     (Celsius)   (Celsius)         
-------------------------------------------------------------------------
1       ASIC                101           95           52          ok          
1       Front-Middle(D1)    62            56           38          ok          
1       Front-Left  (D2)    52            44           33          ok          
1       Back        (D3)    48            42           28          ok

```

**Help:** execute the command "show environment temperature"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show vlan

**Output:**
```

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Po1, Eth1/53, Eth1/54

VLAN Type         Vlan-mode
---- -----        ----------
1    enet         CE

Remote SPAN VLANs
-------------------------------------------------------------------------------

Primary  Secondary  Type             Ports
-------  ---------  ---------------  -------------------------------------------




```

**Help:** execute the command "show vlan"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip dhcp relay address

**Output:**
```
 Interface        Relay Address     VRF Name
 -------------    -------------     --------

 Vlan100           10.40.15.152      my_vrf
 Vlan100           10.40.10.162
 Vlan200           10.40.15.152
 Vlan200           10.40.10.162
 Ethernet1         10.40.15.152
 Ethernet1         10.40.10.162      my_vrf2
 Ethernet1/1       10.40.15.152
 Ethernet1/1       10.40.10.162
 Ethernet1/1.1     10.40.15.152
 Ethernet1/1.1     10.40.10.162
```

**Help:** execute the command "show ip dhcp relay address"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show hostname

**Output:**
```
n9k1 

```

**Help:** execute the command "show hostname"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip interface brief

**Output:**
```
IP Interface Status for VRF "default"(1)
Interface            IP Address      Interface Status

IP Interface Status for VRF "management"(2)
Interface            IP Address      Interface Status
mgmt0                10.205.143.20   protocol-up/link-up/admin-up       

```

**Help:** execute the command "show ip interface brief"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show vrf

**Output:**
```
VRF-Name                           VRF-ID State   Reason
VPC_KEEPALIVE                           3 Up      --
default                                 1 Up      --
VRF1                                    4 Up      --
VRF2                                    7 Up      --
VRF-NAME-3                              8 Up      --
VRF_NAME_4                              5 Up      --
VRFNAME5                                6 Up      --
management                              2 Up      --
```

**Help:** execute the command "show vrf"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip ospf database

**Output:**
```
OSPF Router with ID (50.50.50.50) (Process ID p1)
 
Router Link States (Area 0)
 
Link ID ADV Router Age Seq# Checksum Link Count
40.40.40.40 40.40.40.40 930 0x80000004 0x2ea1 3
50.50.50.50 50.50.50.50 935 0x80000002 0x8b52 1
60.60.60.60 60.60.60.60 943 0x800003c5 0x9854 2
 
Network Link States (Area 0)
 
Link ID ADV Router Age Seq# Checksum
209.165.201.3 60.60.60.60 944 0x80000001 0x7179
 192.0.2.1 50.50.50.50 935 0x80000001 0x516a
 
Summary Network Link States (Area 0)
 
Link ID ADV Router Age Seq# Checksum
209.165.201.1 40.40.40.40 929 0x80000001 0x2498
209.165.201.1 50.50.50.50 928 0x80000001 0x5b2f
209.165.201.1 60.60.60.60 1265 0x800003c3 0xf49b
192.0.2.0 40.40.40.40 943 0x80000001 0x53f3
 192.0.2.0 50.50.50.50 935 0x80000001 0x26f8
192.0.2.0 60.60.60.60 930 0x80000001 0x7b51
```

**Help:** execute the command "show ip ospf database"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show route-map

**Output:**
```
route-map RM-TEST-OUT, permit, sequence 10 
  Match clauses:
    as-path (as-path filter): AS-TEST 
  Set clauses:
route-map RM-BGP-TO-OSPF, deny, sequence 10 
  Match clauses:
    tag: 12345
  Set clauses:
route-map RM-BGP-TO-OSPF, permit, sequence 20 
  Match clauses:
  Set clauses:
route-map RM-ISP1-IN, permit, sequence 1000 
  Match clauses:
  Set clauses:
    local-preference 300
route-map RM-ISP1-OUT, permit, sequence 1000 
  Match clauses:
    as-path (as-path filter): AS-ISP2 
  Set clauses:
route-map RM-ISP1-MAITENANCE, permit, sequence 10 
  Match clauses:
  Set clauses:
    local-preference 50
route-map RM-FW-LP, permit, sequence 10 
  Match clauses:
  Set clauses:
    local-preference 25
route-map RM-FW-MAITENANCE, permit, sequence 10 
  Match clauses:
  Set clauses:
route-map RM-FW-OUTBOUND, permit, sequence 10 
  Match clauses:
    as-path (as-path filter): TEST-AS-FW 
  Set clauses:

route-map RM-X-SIDE-INTERNAL, permit, sequence 10 
  Match clauses:
    ip address prefix-lists: PF-PATH-X-INTERNAL 
  Set clauses:
route-map RM-Z-SIDE-INTERNAL, permit, sequence 10 
  Match clauses:
    ip address prefix-lists: PF-PATH-Z-INTERNAL 
  Set clauses:
 route-map RM-FILTER-IN, permit, sequence 10 
  Match clauses:
    ip address prefix-lists: PL-PERMIT-IN 
  Set clauses:
route-map TEST_THIS, permit, sequence 10 
  Match clauses:
    ip address (access-lists): AL_TEST_TEST 
  Set clauses:
    ip next-hop 2.2.2.2 
route-map RM-N3K1-TO-N3K2, permit, sequence 10 
  Match clauses:
    ip address prefix-lists: PF-N3K1-TO-N3K2 
  Set clauses:
    extcommunity RT:100:1
route-map RM-N3K2-TO-N3K1, permit, sequence 10 
  Match clauses:
    ip address prefix-lists: PF-N3K2-TO-N3K1 
  Set clauses:
    extcommunity RT:200:1
route-map RM-PATH-A-DEFAULT-ROUTE, permit, sequence 10 
  Match clauses:
    ip address prefix-lists: PF-A-DEFAULT-ROUTE 
  Set clauses:

```

**Help:** execute the command "show route-map"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show interface brief

**Output:**
```
--------------------------------------------------------------------------------
Ethernet      VLAN   Type Mode   Status  Reason                   Speed     Port
Interface                                                                   Ch #
--------------------------------------------------------------------------------
Eth1/1        150     eth  access down    Link not connected         auto(D) --
Eth1/2        150     eth  access down    Link not connected         auto(D) --
Eth1/3        150     eth  access down    Link not connected         auto(D) --
Eth1/4        150     eth  access down    Link not connected         auto(D) --
Eth1/5        150     eth  access down    Link not connected         auto(D) --
Eth1/6        150     eth  access down    Link not connected         auto(D) --
Eth1/7        150     eth  access down    Link not connected         auto(D) --
Eth1/8        150     eth  access down    Link not connected         auto(D) --
Eth1/9        150     eth  access down    Link not connected         auto(D) --
Eth1/10       150     eth  access down    Link not connected         auto(D) --
Eth1/11       150     eth  access down    Link not connected         auto(D) --
Eth1/12       150     eth  access down    Link not connected         auto(D) --
Eth1/13       150     eth  access down    Link not connected         auto(D) --
Eth1/14       150     eth  access down    Link not connected         auto(D) --
Eth1/15       150     eth  access down    Link not connected         auto(D) --
Eth1/16       150     eth  access down    Link not connected         auto(D) --
Eth1/17       150     eth  access down    Link not connected         auto(D) --
Eth1/18       150     eth  access down    Link not connected         auto(D) --
Eth1/19       150     eth  access down    Link not connected         auto(D) --
Eth1/20       150     eth  access down    Link not connected         auto(D) --
Eth1/21       150     eth  access down    Link not connected         auto(D) --
Eth1/22       150     eth  access down    Link not connected         auto(D) --
Eth1/23       150     eth  access down    Link not connected         auto(D) --
Eth1/24       150     eth  access down    Link not connected         auto(D) --
Eth1/25       150     eth  access down    Link not connected         auto(D) --
Eth1/26       150     eth  access down    Link not connected         auto(D) --
Eth1/27       150     eth  access down    Link not connected         auto(D) --
Eth1/28       150     eth  access down    Link not connected         auto(D) --
Eth1/29       150     eth  access down    Link not connected         auto(D) --
Eth1/30       150     eth  access down    Link not connected         auto(D) --
Eth1/31       140     eth  access down    Link not connected         auto(D) --
Eth1/32       140     eth  access down    Link not connected         auto(D) --
Eth1/33       140     eth  access down    Link not connected         auto(D) --
Eth1/34       140     eth  access down    Link not connected         auto(D) --
Eth1/35       140     eth  access down    Link not connected         auto(D) --
Eth1/36       140     eth  access down    Link not connected         auto(D) --
Eth1/37       140     eth  access down    Link not connected         auto(D) --
Eth1/38       140     eth  access down    Link not connected         auto(D) --
Eth1/39       140     eth  access down    Link not connected         auto(D) --
Eth1/40       140     eth  access down    Link not connected         auto(D) --
Eth1/41       140     eth  access down    Link not connected         auto(D) --
Eth1/42       140     eth  access down    Link not connected         auto(D) --
Eth1/43       140     eth  access down    Link not connected         auto(D) --
Eth1/44       140     eth  access down    Link not connected         auto(D) --
Eth1/45       140     eth  access down    Link not connected         auto(D) --
Eth1/46       140     eth  access down    Link not connected         auto(D) --
Eth1/47       140     eth  access down    Link not connected         auto(D) --
Eth1/48       140     eth  access down    Link not connected         auto(D) --
Eth1/49       1       eth  trunk  up      none                        10G(D) 1
Eth1/50       1       eth  trunk  down    SFP not inserted            10G(D) 1
Eth1/51       1       eth  access down    SFP not inserted            10G(D) --
Eth1/52       1       eth  access down    SFP not inserted            10G(D) --

--------------------------------------------------------------------------------
 Port-channel VLAN    Type Mode   Status  Reason                    Speed   Protocol
Interface
--------------------------------------------------------------------------------
Po1          1       eth  trunk  up      none                       a-10G(D)  lacp

--------------------------------------------------------------------------------
Port   VRF          Status IP Address                              Speed    MTU
--------------------------------------------------------------------------------
mgmt0  --           down   --                                      --       1500

-------------------------------------------------------------------------------
 Interface Secondary VLAN(Type)                    Status Reason
-------------------------------------------------------------------------------
Vlan1     --                                      down   Administratively down
Vlan142   --                                      up     --
```

**Help:** execute the command "show interface brief"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show interface status

**Output:**
```
--------------------------------------------------------------------------------
Port          Name               Status    Vlan      Duplex  Speed   Type
--------------------------------------------------------------------------------
mgmt0         --                 notconnec routed    auto    auto    --         

--------------------------------------------------------------------------------
Port          Name               Status    Vlan      Duplex  Speed   Type
--------------------------------------------------------------------------------
Eth1/1        --                 connected trunk     full    1000    1000base-T 
Eth1/2        --                 xcvrAbsen 1         auto    auto    --         
Eth1/3        --                 xcvrAbsen 1         auto    auto    --         
Eth1/4        --                 xcvrAbsen 1         auto    auto    --         
Eth1/5        --                 xcvrAbsen 1         auto    auto    --         
Eth1/6        --                 xcvrAbsen 1         auto    auto    --         
Eth1/7        --                 xcvrAbsen 1         auto    auto    --         
Eth1/8        --                 xcvrAbsen 1         auto    auto    --         
Eth1/9        --                 xcvrAbsen 1         auto    auto    --         
Eth1/10       --                 xcvrAbsen 1         auto    auto    --         
Eth1/11       --                 xcvrAbsen 1         auto    auto    --         
Eth1/12       --                 xcvrAbsen 1         auto    auto    --         
Eth1/13       --                 xcvrAbsen 1         auto    auto    --         
Eth1/14       --                 xcvrAbsen 1         auto    auto    --         
Eth1/15       --                 xcvrAbsen 1         auto    auto    --         
Eth1/16       --                 xcvrAbsen 1         auto    auto    --         
Eth1/17       --                 xcvrAbsen 1         auto    auto    --         
Eth1/18       --                 xcvrAbsen 1         auto    auto    --         
Eth1/19       --                 xcvrAbsen 1         auto    auto    --         
Eth1/20       --                 xcvrAbsen 1         auto    auto    --         
Eth1/21       --                 xcvrAbsen 1         auto    auto    --         
Eth1/22       --                 xcvrAbsen 1         auto    auto    --         
Eth1/23       --                 xcvrAbsen 1         auto    auto    --         
Eth1/24       --                 xcvrAbsen 1         auto    auto    --         
Eth1/25       --                 xcvrAbsen 1         auto    auto    --         
Eth1/26       --                 xcvrAbsen 1         auto    auto    --         
Eth1/27       --                 xcvrAbsen 1         auto    auto    --         
Eth1/28       --                 xcvrAbsen 1         auto    auto    --         
Eth1/29       --                 xcvrAbsen 1         auto    auto    --         
Eth1/30       --                 xcvrAbsen 1         auto    auto    --         
Eth1/31       --                 xcvrAbsen 1         auto    auto    --         
Eth1/32       --                 xcvrAbsen 1         auto    auto    --         
Eth1/33       --                 xcvrAbsen 1         auto    auto    --         
Eth1/34       --                 xcvrAbsen 1         auto    auto    --         
Eth1/35       --                 xcvrAbsen 1         auto    auto    --         
Eth1/36       --                 xcvrAbsen 1         auto    auto    --         
Eth1/37       --                 xcvrAbsen 1         auto    auto    --         
Eth1/38       --                 xcvrAbsen 1         auto    auto    --         
Eth1/39       --                 xcvrAbsen 1         auto    auto    --         
Eth1/40       --                 xcvrAbsen 1         auto    auto    --         
Eth1/41       --                 xcvrAbsen 1         auto    auto    --         
Eth1/42       --                 xcvrAbsen 1         auto    auto    --         
Eth1/43       --                 xcvrAbsen 1         auto    auto    --         
Eth1/44       --                 xcvrAbsen 1         auto    auto    --         
Eth1/45       --                 xcvrAbsen 1         auto    auto    --         
Eth1/46       --                 xcvrAbsen 1         auto    auto    --         
Eth1/47       --                 xcvrAbsen 1         auto    auto    --         
Eth1/48       --                 xcvrAbsen 1         auto    auto    --         
Eth1/49       --                 xcvrAbsen 1         auto    auto    --         
Eth1/50       --                 xcvrAbsen 1         auto    auto    --         
Eth1/51       --                 xcvrAbsen 1         auto    auto    --         
Eth1/52       --                 xcvrAbsen 1         auto    auto    --         
Eth1/53       VPC-peer-link !kob xcvrAbsen trunk     auto    auto    --         
Eth1/54       VPC-peer-link !kob xcvrAbsen trunk     auto    auto    --         

```

**Help:** execute the command "show interface status"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip mroutes vrf all

**Output:**
```
IP Multicast Routing Table for VRF "default"

(*, 225.1.0.1/32), uptime: 2w3d, igmp ip pim
  Incoming interface: Ethernet1/1, RPF nbr: 10.1.1.1
  Outgoing interface list: (count: 1)
    Ethernet1/3, uptime: 2w3d, igmp
 

(10.1.13.10/32, 225.1.0.1/32), uptime: 06:33:34, ip mrib pim
  Incoming interface: Ethernet1/1, RPF nbr: 10.1.1.1
  Outgoing interface list: (count: 1)
    Ethernet1/3, uptime: 06:33:34, mrib


(*, 232.0.0.0/8), uptime: 2w3d, pim ip
  Incoming interface: Null, RPF nbr: 0.0.0.0
  Outgoing interface list: (count: 0)

```

**Help:** execute the command "show ip mroutes vrf all"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show cdp neighbors detail

**Output:**
```
----------------------------------------
Device ID:MKT1

Interface address(es): 0
Platform: MikroTik, Capabilities: Router
Interface: Ethernet1/1, Port ID (outgoing port): ether1
Holdtime: 61 sec

Version:
6.47.10 (long-term)
 
Advertisement Version: 1
Local Interface MAC: b1:81:d1:d1:a1:11
Remote Interface MAC: 00:00:00:00:00:00

```

**Help:** execute the command "show cdp neighbors detail"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show feature

**Output:**
```
Feature Name          Instance  State
--------------------  --------  --------
bash-shell             1          enabled
bfd                    1          disabled
bgp                    1          disabled
dhcp                   1          disabled
eigrp                  1          disabled
eigrp                  2          disabled
eigrp                  3          disabled
eigrp                  4          disabled
eigrp                  5          disabled
eigrp                  6          disabled
eigrp                  7          disabled
eigrp                  8          disabled
eigrp                  9          disabled
eigrp                  10         disabled
eigrp                  11         disabled
eigrp                  12         disabled
eigrp                  13         disabled
eigrp                  14         disabled
eigrp                  15         disabled
eigrp                  16         disabled
evmed                  1          disabled
fabric_mcast           1          disabled
hmm                    1          disabled
hsrp_engine            1          enabled
interface-vlan         1          enabled
isis                   1          disabled
isis                   2          disabled
isis                   3          disabled
isis                   4          disabled
isis                   5          disabled
isis                   6          disabled
isis                   7          disabled
isis                   8          disabled
isis                   9          disabled
isis                   10         disabled
isis                   11         disabled
isis                   12         disabled
isis                   13         disabled
isis                   14         disabled
isis                   15         disabled
isis                   16         disabled
itd                    1          disabled
lacp                   1          enabled
ldap                   1          disabled
ldp                    1          disabled
lldp                   1          enabled
mpls_static            1          disabled
msdp                   1          disabled
nat                    1          disabled
ospf                   1          enabled (not-running)
ospf                   2          enabled
ospf                   3          enabled
ospf                   4          enabled (not-running)
ospf                   5          enabled (not-running)
ospf                   6          enabled (not-running)
ospf                   7          enabled (not-running)
ospf                   8          enabled (not-running)
ospf                   9          enabled (not-running)
ospf                   10         enabled (not-running)
ospf                   11         enabled (not-running)
ospf                   12         enabled (not-running)
ospf                   13         enabled (not-running)

```

**Help:** execute the command "show feature"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show hsrp all

**Output:**
```
Vlan100 - Group 100 (HSRP-V2) (IPv4)
  Local state is Active, priority 250 (Cfged 250), may preempt
    Forwarding threshold(for vPC), lower: 1 upper: 250 
  Preemption Delay (Seconds) Reload:120 Minimum:60 Sync:60 
  Hellotime 3 sec, holdtime 10 sec
  Next hello sent in 2.676000 sec(s)
  Virtual IP address is 192.168.100.1 (Cfged)
     Secondary Virtual IP address is 192.168.100.193
  Active router is local
  Standby router is 192.168.100.69 , priority 200 expires in 10.174000 sec(s)
  Authentication MD5, key-string "dr-hsrp"
  Virtual mac address is 0000.0c9f.f384 (Default MAC)
  2 state changes, last state change 1y27w
  IP redundancy name is hsrp-Vlan100-100 (default)
  Secondary VIP(s):
                  192.168.100.193

Vlan200 - Group 200 (HSRP-V2) (IPv4)
  Local state is Active, priority 250 (Cfged 250), may preempt
    Forwarding threshold(for vPC), lower: 1 upper: 250 
  Preemption Delay (Seconds) Reload:120 Minimum:60 Sync:60 
  Hellotime 1 sec, holdtime 3 sec
  Next hello sent in 0.448000 sec(s)
  Virtual IP address is 172.11.4.254 (Cfged)
  Active router is local
  Standby router is 172.11.4.253 , priority 200 expires in 2.551000 sec(s)
  Authentication MD5, key-string "hq-hsrp"
  Virtual mac address is 0000.0c9f.fd48 (Default MAC)
  2 state changes, last state change 1y0w
  IP redundancy name is hsrp-Vlan200-200 (default)

Vlan201 - Group 201 (HSRP-V2) (IPv4)
  Local state is Active, priority 250 (Cfged 250), may preempt
    Forwarding threshold(for vPC), lower: 1 upper: 250 
  Preemption Delay (Seconds) Reload:120 Minimum:60 Sync:60 
  Hellotime 1 sec, holdtime 3 sec
  Next hello sent in 0.484000 sec(s)
  Virtual IP address is 172.11.5.30 (Cfged)
  Active router is local
  Standby router is 172.11.5.29 , priority 200 expires in 2.551000 sec(s)
  Authentication MD5, key-string "hq-hsrp"
  Virtual mac address is 0000.0c9f.fd49 (Default MAC)
  2 state changes, last state change 1y0w
  IP redundancy name is hsrp-Vlan201-201 (default)
 
Vlan210 - Group 210 (HSRP-V2) (IPv4)
  Local state is Active, priority 250 (Cfged 250), may preempt
    Forwarding threshold(for vPC), lower: 1 upper: 250 
  Preemption Delay (Seconds) Reload:120 Minimum:60 Sync:60 
  Hellotime 1 sec, holdtime 3 sec
  Next hello sent in 0.420000 sec(s)
  Virtual IP address is 172.12.9.254 (Cfged)
  Active router is local
  Standby router is 172.12.9.253 , priority 200 expires in 2.873000 sec(s)
  Authentication MD5, key-string "hq-hsrp"
  Virtual mac address is 0000.0c9f.fdb6 (Default MAC)
  2 state changes, last state change 1y0w
  IP redundancy name is hsrp-Vlan210-210 (default)
 
Vlan211 - Group 211 (HSRP-V2) (IPv4)
  Local state is Active, priority 250 (Cfged 250), may preempt
    Forwarding threshold(for vPC), lower: 1 upper: 250 
  Preemption Delay (Seconds) Reload:120 Minimum:60 Sync:60 
  Hellotime 1 sec, holdtime 3 sec
  Next hello sent in 0.695000 sec(s)
  Virtual IP address is 172.12.10.62 (Cfged)
  Active router is local
  Standby router is 172.12.10.61 , priority 200 expires in 2.873000 sec(s)
  Authentication MD5, key-string "hq-hsrp"
  Virtual mac address is 0000.0c9f.fdb7 (Default MAC)
  2 state changes, last state change 1y0w
  IP redundancy name is hsrp-Vlan211-211 (default)
 
Vlan220 - Group 220 (HSRP-V2) (IPv4)
  Local state is Active, priority 250 (Cfged 250), may preempt
    Forwarding threshold(for vPC), lower: 1 upper: 250 
  Preemption Delay (Seconds) Reload:120 Minimum:60 Sync:60 
  Hellotime 1 sec, holdtime 3 sec
  Next hello sent in 0.484000 sec(s)
  Virtual IP address is 172.13.12.254 (Cfged)
  Active router is local
  Standby router is 172.13.12.253 , priority 200 expires in 2.281000 sec(s)
  Authentication MD5, key-string "hq-hsrp"
  Virtual mac address is 0000.0c9f.fe24 (Default MAC)
  2 state changes, last state change 1y0w
  IP redundancy name is hsrp-Vlan220-220 (default)
 
Vlan221 - Group 221 (HSRP-V2) (IPv4)
  Local state is Active, priority 250 (Cfged 250), may preempt
    Forwarding threshold(for vPC), lower: 1 upper: 250 
  Preemption Delay (Seconds) Reload:120 Minimum:60 Sync:60 
  Hellotime 1 sec, holdtime 3 sec
  Next hello sent in 0.614000 sec(s)
  Virtual IP address is 172.13.13.30 (Cfged)
  Active router is local
  Standby router is 172.13.13.29 , priority 200 expires in 2.281000 sec(s)
  Authentication MD5, key-string "hq-hsrp"
  Virtual mac address is 0000.0c9f.fe25 (Default MAC)
  2 state changes, last state change 1y0w
  IP redundancy name is hsrp-Vlan221-221 (default)
 
Vlan300 - Group 300 (HSRP-V2) (IPv4)
  Local state is Active, priority 250 (Cfged 250), may preempt
    Forwarding threshold(for vPC), lower: 1 upper: 250 
  Preemption Delay (Seconds) Reload:120 Minimum:60 Sync:60 
  Hellotime 1 sec, holdtime 3 sec
  Next hello sent in 0.448000 sec(s)
  Virtual IP address is 172.16.0.254 (Cfged)
  Active router is local
  Standby router is 172.16.0.253 , priority 200 expires in 2.551000 sec(s)
  Authentication MD5, key-string "dr-hsrp"
  Virtual mac address is 0000.0c9f.fed8 (Default MAC)
  14 state changes, last state change 1y2w
  IP redundancy name is hsrp-Vlan300-300 (default)
 
Vlan416 - Group 416 (HSRP-V2) (IPv4)
  Local state is Standby, priority 130 (Cfged 130), may preempt
    Forwarding threshold(for vPC), lower: 1 upper: 130 
  Preemption Delay (Seconds) Reload:120 Minimum:60 Sync:60 
  Hellotime 1 sec, holdtime 3 sec
  Next hello sent in 0.231000 sec(s)
  Virtual IP address is 172.17.1.1 (Cfged)
  Active router is 172.17.1.2, priority 150 expires in 0.661000 sec(s)
  Standby router is local 
  Authentication MD5, key-string "core-hsrp"
  Virtual mac address is 0000.0c9f.ff4c (Default MAC)
  105 state changes, last state change 21w5d
  IP redundancy name is hsrp-Vlan416-416 (default)

Vlan417 - Group 417 (HSRP-V2) (IPv4)
  Local state is Standby, priority 130 (Cfged 130), may preempt
    Forwarding threshold(for vPC), lower: 1 upper: 130 
  Preemption Delay (Seconds) Reload:120 Minimum:60 Sync:60 
  Hellotime 1 sec, holdtime 3 sec
  Next hello sent in 0.610000 sec(s)
  Virtual IP address is 172.17.1.17 (Cfged)
  Active router is 172.17.1.18, priority 150 expires in 1.531000 sec(s)
  Standby router is local 
  Authentication MD5, key-string "core-hsrp"
  Virtual mac address is 0000.0c9f.ff4d (Default MAC)
  418 state changes, last state change 21w5d
  IP redundancy name is hsrp-Vlan417-417 (default)

Vlan418 - Group 418 (HSRP-V2) (IPv4)
  Local state is Standby, priority 130 (Cfged 130), may preempt
    Forwarding threshold(for vPC), lower: 1 upper: 130 
  Preemption Delay (Seconds) Reload:120 Minimum:60 Sync:60 
  Hellotime 1 sec, holdtime 3 sec
  Next hello sent in 0.422000 sec(s)
  Virtual IP address is 172.17.1.33 (Cfged)
  Active router is 172.17.1.2, priority 150 expires in 0.081000 sec(s)
  Standby router is local 
  Authentication MD5, key-string "core-hsrp"
  Virtual mac address is 0000.0c9f.ff4e (Default MAC)
  102 state changes, last state change 21w5d
  IP redundancy name is hsrp-Vlan418-418 (default)

Vlan419 - Group 419 (HSRP-V2) (IPv4)
  Local state is Standby, priority 130 (Cfged 130), may preempt
    Forwarding threshold(for vPC), lower: 1 upper: 130 
  Preemption Delay (Seconds) Reload:120 Minimum:60 Sync:60 
  Hellotime 1 sec, holdtime 3 sec
  Next hello sent in 0.886000 sec(s)
  Virtual IP address is 172.17.1.49 (Cfged)
  Active router is 172.17.1.50, priority 150 expires in 2.281000 sec(s)
  Standby router is local 
  Authentication MD5, key-string "core-hsrp"
  Virtual mac address is 0000.0c9f.ff4f (Default MAC)
  448 state changes, last state change 21w5d
  IP redundancy name is hsrp-Vlan419-419 (default)

Vlan420 - Group 420 (HSRP-V2) (IPv4)
  Local state is Standby, priority 130 (Cfged 130), may preempt
    Forwarding threshold(for vPC), lower: 1 upper: 130 
  Preemption Delay (Seconds) Reload:120 Minimum:60 Sync:60 
  Hellotime 1 sec, holdtime 3 sec
  Next hello sent in 0.301000 sec(s)
  Virtual IP address is 172.17.1.65 (Cfged)
  Active router is 172.17.1.66, priority 150 expires in 0.081000 sec(s)
  Standby router is local 
  Authentication MD5, key-string "core-hsrp"
  Virtual mac address is 0000.0c9f.ff50 (Default MAC)
  103 state changes, last state change 21w5d
  IP redundancy name is hsrp-Vlan420-420 (default)

```

**Help:** execute the command "show hsrp all"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show inventory

**Output:**
```
NAME: "Chassis",  DESCR: "Nexus9000 C9396PX Chassis"
PID: N9K-C9396PX         ,  VID: V02 ,  SN: SAL1819S6LU

NAME: "Slot 1",  DESCR: "1/10G SFP+ Ethernet Module"
PID: N9K-C9396PX         ,  VID: V02 ,  SN: SAL1819S6LU
 
NAME: "Slot 2",  DESCR: "40G Ethernet Expansion Module"
PID: N9K-M12PQ           ,  VID: V01 ,  SN: SAL1815QCJE

NAME: "Power Supply 1",  DESCR: "Nexus9000 C9396PX Chassis Power Supply"
PID: N9K-PAC-650W        ,  VID: V01 ,  SN: DCB1809X07E

NAME: "Power Supply 2",  DESCR: "Nexus9000 C9396PX Chassis Power Supply"
PID: N9K-PAC-650W        ,  VID: V01 ,  SN: DCB1809X07H
 
NAME: "Fan 1",  DESCR: "Nexus9000 C9396PX Chassis Fan Module"
PID: N9K-C9300-FAN2      ,  VID: V01 ,  SN: N/A

NAME: "Fan 2",  DESCR: "Nexus9000 C9396PX Chassis Fan Module"
PID: N9K-C9300-FAN2      ,  VID: V01 ,  SN: N/A

NAME: "Fan 3",  DESCR: "Nexus9000 C9396PX Chassis Fan Module"
PID: N9K-C9300-FAN2      ,  VID: V01 ,  SN: N/A

NAME: "Slot 33", DESCR: "Nexus7000 C7009 (9 Slot) Chassis Power Supply"
PID: N7K-AC-6.0KW, VID: V01, SN: DTM141600XT
 
NAME: "Slot 34", DESCR: "Nexus7000 C7009 (9 Slot) Chassis Power Supply"
PID: N7K-AC-6.0KW, VID: V01, SN: DTM1414007T
 
NAME: "Slot 35", DESCR: "Nexus7000 C7009 (9 Slot) Chassis Fan Module"
PID: N7K-C7009-FAN, VID: V00, SN: JAF1433DDEJ

NAME: Ethernet1/46,  DESCR: CISCO-AVAGO
PID: 10Gbase-SR          ,  VID: SFBR-709SMZ-CS1,  SN: AVD42309ABD

NAME: Ethernet1/47,  DESCR: CISCO
PID: 1000base-LH         ,  VID: RTXM191-404-C88,  SN: ACW315000AD
 
NAME: Ethernet1/48,  DESCR: CISCO-AVAGO
PID: 10Gbase-LR          ,  VID: SFCT-739SMZ,  SN: AVD2219K9AO

```

**Help:** execute the command "show inventory"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show interface transceiver details

**Output:**
```
Ethernet3/1
    transceiver is present
    type is 10Gbase-SR
    name is CISCO-FINISAR   
    part number is FTLX8571D3BCL-C2
    revision is A   
    serial number is FNS18510TXL     
    nominal bitrate is 10300 MBit/sec
    Link length supported for 50/125um OM2 fiber is 82 m
    Link length supported for 62.5/125um fiber is 26 m
    Link length supported for 50/125um OM3 fiber is 300 m
    cisco id is --
    cisco extended id number is 4
    cisco part number is 10-2415-03
    cisco product id is SFP-10G-SR          
    cisco vendor id is V03 
    number of lanes 1

           SFP Detail Diagnostics Information (internal calibration)
  ----------------------------------------------------------------------------
                Current              Alarms                  Warnings
                Measurement     High        Low         High          Low
  ----------------------------------------------------------------------------
  Temperature   35.66 C        75.00 C     -5.00 C     70.00 C        0.00 C
  Voltage        3.29 V         3.63 V      2.97 V      3.46 V        3.13 V
  Current           N/A        11.80 mA     4.00 mA    10.80 mA       5.00 mA
  Tx Power     -14.05 dBm --    1.69 dBm  -11.30 dBm   -1.30 dBm     -7.30 dBm
  Rx Power     -30.45 dBm --    2.00 dBm  -13.90 dBm   -1.00 dBm     -9.90 dBm
  Transmit Fault Count = 0
  ----------------------------------------------------------------------------
  Note: ++  high-alarm; +  high-warning; --  low-alarm; -  low-warning

Ethernet3/2
    transceiver is present
    type is 10Gbase-SR
    name is CISCO-FINISAR   
    part number is FTLX8571D3BCL-C2
    revision is A   
    serial number is FNS18510TXV     
    nominal bitrate is 10300 MBit/sec
    Link length supported for 50/125um OM2 fiber is 82 m
    Link length supported for 62.5/125um fiber is 26 m
    Link length supported for 50/125um OM3 fiber is 300 m
    cisco id is --
    cisco extended id number is 4
    cisco part number is 10-2415-03
    cisco product id is SFP-10G-SR          
    cisco vendor id is V03 
    number of lanes 1

           SFP Detail Diagnostics Information (internal calibration)
  ----------------------------------------------------------------------------
                Current              Alarms                  Warnings
                Measurement     High        Low         High          Low
  ----------------------------------------------------------------------------
  Temperature   38.28 C        75.00 C     -5.00 C     70.00 C        0.00 C
  Voltage        3.29 V         3.63 V      2.97 V      3.46 V        3.13 V
  Current        0.43 mA  --   11.80 mA     4.00 mA    10.80 mA       5.00 mA
  Tx Power     -16.19 dBm --    1.69 dBm  -11.30 dBm   -1.30 dBm     -7.30 dBm
  Rx Power     -33.97 dBm --    2.00 dBm  -13.90 dBm   -1.00 dBm     -9.90 dBm
  Transmit Fault Count = 0
  ----------------------------------------------------------------------------
  Note: ++  high-alarm; +  high-warning; --  low-alarm; -  low-warning

Ethernet3/3
    transceiver is present
    type is 10Gbase-SR
    name is CISCO-FINISAR   
    part number is FTLX8571D3BCL-C2
    revision is A   
    serial number is FNS18510TYD     
    nominal bitrate is 10300 MBit/sec
    Link length supported for 50/125um OM2 fiber is 82 m
    Link length supported for 62.5/125um fiber is 26 m
    Link length supported for 50/125um OM3 fiber is 300 m
    cisco id is --
    cisco extended id number is 4
    cisco part number is 10-2415-03
    cisco product id is SFP-10G-SR          
    cisco vendor id is V03 
    number of lanes 1

           SFP Detail Diagnostics Information (internal calibration)
  ----------------------------------------------------------------------------
                Current              Alarms                  Warnings
                Measurement     High        Low         High          Low
  ----------------------------------------------------------------------------
  Temperature   37.07 C        75.00 C     -5.00 C     70.00 C        0.00 C
  Voltage        3.29 V         3.63 V      2.97 V      3.46 V        3.13 V
  Current        0.21 mA  --   11.80 mA     4.00 mA    10.80 mA       5.00 mA
  Tx Power          N/A         1.69 dBm  -11.30 dBm   -1.30 dBm     -7.30 dBm
  Rx Power     -33.97 dBm --    2.00 dBm  -13.90 dBm   -1.00 dBm     -9.90 dBm
  Transmit Fault Count = 0
  ----------------------------------------------------------------------------
  Note: ++  high-alarm; +  high-warning; --  low-alarm; -  low-warning

Ethernet4/1
    transceiver is present
    type is CFP-100G-LR4
    name is CISCO           
    part number is SCF1001L4CNC101 
    revision is 11
    serial number is ECL190200BA     
    nominal bitrate is 129 MBit/sec per channel
    Link length supported for 9/125um fiber is 10 km
    cisco id is --
    cisco extended id number is 85
    cisco part number is 10-2549-02
    cisco product id is CFP-100G-LR4    
    cisco vendor id is V02 
    number of lanes 3

Lane Number:1 Common Diagnostic Information
           SFP Detail Diagnostics Information (internal calibration)
  ----------------------------------------------------------------------------
                Current              Alarms                  Warnings
                Measurement     High        Low         High          Low
  ----------------------------------------------------------------------------
  Temperature   40.44 C        74.00 C     -4.00 C     70.00 C        0.00 C
  Voltage        3.28 V         3.66 V      2.93 V      3.46 V        3.13 V
  ----------------------------------------------------------------------------
  Note: ++  high-alarm; +  high-warning; --  low-alarm; -  low-warning

 Lane Number:2 Network Lane
           SFP Detail Diagnostics Information (internal calibration)
  ----------------------------------------------------------------------------
                Current              Alarms                  Warnings
                Measurement     High        Low         High          Low
  ----------------------------------------------------------------------------
  Tx Power       0.76 dBm       7.49 dBm   -8.30 dBm    4.49 dBm     -4.30 dBm
  Rx Power      -1.77 dBm       7.49 dBm  -14.60 dBm    4.49 dBm    -10.59 dBm
  Transmit Fault Count = 0
  ----------------------------------------------------------------------------
  Note: ++  high-alarm; +  high-warning; --  low-alarm; -  low-warning

 Lane Number:3 Network Lane
           SFP Detail Diagnostics Information (internal calibration)
  ----------------------------------------------------------------------------
                Current              Alarms                  Warnings
                Measurement     High        Low         High          Low
  ----------------------------------------------------------------------------
  Tx Power       0.44 dBm       7.49 dBm   -8.30 dBm    4.49 dBm     -4.30 dBm
  Rx Power      -1.57 dBm       7.49 dBm  -14.60 dBm    4.49 dBm    -10.59 dBm
  Transmit Fault Count = 0
  ----------------------------------------------------------------------------
  Note: ++  high-alarm; +  high-warning; --  low-alarm; -  low-warning

```

**Help:** execute the command "show interface transceiver details"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show interface

**Output:**
```
Vlan1 is down (Administratively down), line protocol is down
  Hardware is EtherSVI, address is  00de.fb01.c9bc
  MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec

Vlan330 is up, line protocol is up
  Hardware is EtherSVI, address is  00de.fb01.c921
  Internet Address is 192.168.1.3/24
  MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec

Vlan336 is up, line protocol is up
  Hardware is EtherSVI, address is  00de.fb01.c933
  Internet Address is 192.168.2.3/24
  MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec

Vlan339 is up, line protocol is up
  Hardware is EtherSVI, address is  00de.fb01.c9ab
  Internet Address is 192.168.3.3/24
  MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec

Vlan300 is up, line protocol is up
  Hardware is EtherSVI, address is  00de.fb01.c9ef
  Internet Address is 192.168.24.1/24
  MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec

Ethernet106/1/1 is down (Link not connected)
  Hardware: 10/100/1000 Ethernet, address: 0000.d200.0000 (bia 0000.d200.0000)
  MTU 1500 bytes, BW 23 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA
  Port mode is access
  auto-duplex, auto-speed
  Beacon is turned off
  Input flow-control is off, output flow-control is on
  Switchport monitor is off 
  EtherType is 0x8100 
  Last link flapped 14week(s) 5day(s)
  Last clearing of "show interface" counters never
  9 interface resets
  30 seconds input rate 0 bits/sec, 0 packets/sec
  30 seconds output rate 0 bits/sec, 0 packets/sec
  Load-Interval #2: 5 minute (300 seconds)
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    18476 unicast packets  506094 multicast packets  362760 broadcast packets
    887330 input packets  70500074 bytes
    2 jumbo packets  0 storm suppression bytes
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    17841 unicast packets  5660600 multicast packets  339717 broadcast packets
    6018158 output packets  711823811 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble 0 output discard
    0 Tx pause

```

**Help:** execute the command "show interface"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip interface

**Output:**
```
IP Interface Status for VRF "default"
Vlan156, Interface status: protocol-down/link-down/admin-up, iod: 2,
  IP address: 155.155.155.1, IP subnet: 155.155.155.0/30 route-preference: 0, tag: 0 
  IP broadcast address: 255.255.255.255
  IP multicast groups locally joined: none
  IP MTU: 1500 bytes (using link MTU)
  IP primary address route-preference: 0, tag: 0
  IP proxy ARP : disabled
  IP Local Proxy ARP : disabled
  IP multicast routing: disabled
  IP icmp redirects: enabled
  IP directed-broadcast: disabled 
  IP Forwarding: disabled 
  IP icmp unreachables (except port): disabled
  IP icmp port-unreachable: enabled
  IP unicast reverse path forwarding: none
  IP load sharing: none 
  IP interface statistics last reset: never
  IP interface software stats: (sent/received/forwarded/originated/consumed)
    Unicast packets    : 0/0/0/0/0
    Unicast bytes      : 0/0/0/0/0
    Multicast packets  : 0/0/0/0/0
    Multicast bytes    : 0/0/0/0/0
    Broadcast packets  : 0/0/0/0/0
    Broadcast bytes    : 0/0/0/0/0
    Labeled packets    : 0/0/0/0/0
    Labeled bytes      : 0/0/0/0/0
Ethernet1/5, Interface status: protocol-down/link-down/admin-up, iod: 15,
  IP address: 10.1.0.1, IP subnet: 10.1.0.0/30 route-preference: 0, tag: 0 
  IP broadcast address: 255.255.255.255
  IP multicast groups locally joined: none
  IP MTU: 1500 bytes (using link MTU)
  IP primary address route-preference: 0, tag: 0
  IP proxy ARP : disabled
  IP Local Proxy ARP : disabled
  IP multicast routing: disabled
  IP icmp redirects: enabled
  IP directed-broadcast: disabled 
  IP Forwarding: disabled 
  IP icmp unreachables (except port): disabled
  IP icmp port-unreachable: enabled
  IP unicast reverse path forwarding: none
  IP load sharing: none 
  IP interface statistics last reset: never
  IP interface software stats: (sent/received/forwarded/originated/consumed)
    Unicast packets    : 0/0/0/0/0
    Unicast bytes      : 0/0/0/0/0
    Multicast packets  : 0/0/0/0/0
    Multicast bytes    : 0/0/0/0/0
    Broadcast packets  : 0/0/0/0/0
    Broadcast bytes    : 0/0/0/0/0
    Labeled packets    : 0/0/0/0/0
    Labeled bytes      : 0/0/0/0/0

```

**Help:** execute the command "show ip interface"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show bgp vrf all ipv4 unicast detail

**Output:**
```
BGP routing table information for VRF TEST_1, address family IPv4 Unicast
 BGP routing table entry for 10.1.1.0/24, version 3446
Paths: (1 available, best #0)
Flags: (0x8000002) (high32 00000000) on xmit-list, is not in urib, is not in HW

  Path type: local, path is invalid(not in urib), no labeled nexthop
  AS-Path: NONE, path locally originated
    0.0.0.0 (metric 0) from 0.0.0.0 (10.0.1.1)
      Origin IGP, MED not set, localpref 100, weight 32768
 

BGP routing table information for VRF default, address family IPv4 Unicast
 BGP routing table entry for 0.0.0.0/0, version 461888
Paths: (2 available, best #1)
Flags: (0x8008001a) (high32 00000000) on xmit-list, is in urib, is best urib route, is in HW

  Advertised path-id 1
  Path type: internal, path is valid, is best path, no labeled nexthop, in rib
  AS-Path: 65111.1233 65111.4566 65111.7899 12345 , path sourced external to AS
    10.2.2.252 (metric 0) from 10.2.2.252 (10.12.2.100)
      Origin IGP, MED not set, localpref 5000, weight 0
      Community: 12345:1111 3000:4444 44444:1111 

  Path type: external, path is valid, not best reason: Local Preference, no labeled nexthop
  AS-Path: 65111.1233 65111.4566 65111.7899 22222 , path sourced external to AS
    10.1.1.226 (metric 0) from 10.1.1.226 (10.9.1.100)
      Origin IGP, MED not set, localpref 4000, weight 0
      Community: 12345:1111 3000:4444 44444:2222

  Path-id 1 advertised to peers:
    172.16.251.13  
BGP routing table entry for 2.22.22.0/27, version 98
Paths: (1 available, best #1)
Flags: (0x8008001a) (high32 00000000) on xmit-list, is in urib, is best urib route, is in HW

  Advertised path-id 1
  Path type: internal, path is valid, is best path, no labeled nexthop, in rib
  AS-Path: 65222.1111 653333 , path sourced external to AS
    10.3.3.252 (metric 0) from 10.3.3.252 (10.9.1.200)
      Origin IGP, MED 100, localpref 5000, weight 0
      Community: 10104:10030 20311:0 41000:11501 

  Path-id 1 advertised to peers:
    10.3.10.123        10.3.9.234        172.16.10.123  
BGP routing table entry for 10.10.10.0/24, version 336212
Paths: (3 available, best #1)
Flags: (0x8008001a) (high32 00000000) on xmit-list, is in urib, is best urib route, is in HW

  Advertised path-id 1
  Path type: internal, path is valid, is best path, no labeled nexthop, in rib
  AS-Path: 65444.3444 65444.100 65444.200 , path sourced external to AS
    10.9.9.252 (metric 0) from 10.9.10.252 (10.16.100.100)
      Origin IGP, MED not set, localpref 5000, weight 0
      Aggregated by 172.16.100.100, aggregator AS 65444.3444
      Community: 100:200 300:400 500:600
      Extcommunity: RT:33333:2222

  Path type: external, path is valid, not best reason: Local Preference, no labeled nexthop
  AS-Path: 65444.3444 65444.100 65444.300 , path sourced external to AS
    10.15.5.214 (metric 0) from 10.15.5.214 (172.16.5.100)
      Origin IGP, MED not set, localpref 4000, weight 0
      Aggregated by 172.16.5.100, aggregator AS 65444.500
      Community: 100:200 300:400 500:700
      Extcommunity: RT:33333:2222

  Path type: external, path is valid, received only, no labeled nexthop
  AS-Path: 65108.50007 65108.51000 65108.53002 , path sourced external to AS
    10.19.9.214 (metric 0) from 10.19.9.214 (172.26.156.121)
      Origin IGP, MED 100, localpref 100, weight 0
      Aggregated by 172.26.156.121, aggregator AS 65108.50007
      Community: 100:200 300:400 500:800
      Extcommunity: RT:33333:2222

  Path-id 1 advertised to peers:
    172.16.251.13  
BGP routing table entry for 10.13.13.0/22, version 450373
Paths: (2 available, best #1)
Flags: (0x8008001a) (high32 00000000) on xmit-list, is in urib, is best urib route, is in HW

  Advertised path-id 1
  Path type: external, path is valid, is best path, no labeled nexthop, in rib
  AS-Path: 65100.30037 65100.30032 2222 2222 , path sourced external to AS
    10.19.19.19 (metric 0) from 10.19.19.19 (172.16.2.2)
      Origin IGP, MED not set, localpref 5000, weight 0
      Aggregated by 10.9.1.90, aggregator AS 64675, atomic-aggregate set
      Community: 10308:10030 30006:0 41000:11501 

  Path type: external, path is valid, received only, no labeled nexthop
  AS-Path: 65100.30037 65100.30032 2222 2222 2222 , path sourced external to AS
    10.19.19.19 (metric 0) from 10.19.19.19 (172.16.2.2)
      Origin IGP, MED not set, localpref 100, weight 0
      Aggregated by 10.9.1.90, aggregator AS 64675, atomic-aggregate set
      Community: 10308:10030 30006:0 41000:11501 

  Path-id 1 advertised to peers:
    10.19.10.253 

```

**Help:** execute the command "show bgp vrf all ipv4 unicast detail"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show interface transceiver

**Output:**
```
Ethernet1/1
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA1
    revision is 01
    serial number is CI1906290051
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 1 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/2
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA2
    revision is 01
    serial number is CI1906290092
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 2 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/3
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA2
    revision is 01
    serial number is CI1906290092
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 2 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/4
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA2
    revision is 01
    serial number is CI1906290092
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 2 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/5
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA2
    revision is 01
    serial number is CI1906290092
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 2 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/6
    transceiver is present
    type is SFP-H10GB-CU1M
    name is OEM
    part number is SFP-H10GB-CU1M
    revision is R
    serial number is CSS11F80668
    nominal bitrate is 10300 MBit/sec
    Link length supported for copper is 1 m
    cisco id is 3
    cisco extended id number is 4

Ethernet1/7
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA2
    revision is 01
    serial number is CI1906290092
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 2 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/8
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA2
    revision is 01
    serial number is CI1906290092
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 2 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/9
    transceiver is present
    type is SFP-H10GB-CU2M
    name is UPNET
    part number is SFP+-10G-DA-2
    revision is A0
    serial number is FO1810250113
    nominal bitrate is 10300 MBit/sec
    Link length supported for copper is 2 m
    cisco id is 3
    cisco extended id number is 4

Ethernet1/10
    transceiver is present
    type is SFP-H10GB-CU2M
    name is UPNET
    part number is SFP+-10G-DA-2
    revision is A0
    serial number is FO1810250145
    nominal bitrate is 10300 MBit/sec
    Link length supported for copper is 2 m
    cisco id is 3
    cisco extended id number is 4

Ethernet1/11
    transceiver is present
    type is SFP-H10GB-CU2M
    name is UPNET
    part number is SFP+-10G-DA-2
    revision is A0
    serial number is FO1810250115
    nominal bitrate is 10300 MBit/sec
    Link length supported for copper is 2 m
    cisco id is 3
    cisco extended id number is 4

Ethernet1/12
    transceiver is present
    type is SFP-H10GB-CU2M
    name is UPNET
    part number is SFP+-10G-DA-2
    revision is A0
    serial number is FO1810250131
    nominal bitrate is 10300 MBit/sec
    Link length supported for copper is 2 m
    cisco id is 3
    cisco extended id number is 4

Ethernet1/13
    transceiver is present
    type is SFP-H10GB-CU2M
    name is UPNET
    part number is SFP+-10G-DA-2
    revision is A0
    serial number is FO1810250138
    nominal bitrate is 10300 MBit/sec
    Link length supported for copper is 2 m
    cisco id is 3
    cisco extended id number is 4

Ethernet1/14
    transceiver is present
    type is SFP-H10GB-CU2M
    name is UPNET
    part number is SFP+-10G-DA-2
    revision is A0
    serial number is FO1810250171
    nominal bitrate is 10300 MBit/sec
    Link length supported for copper is 2 m
    cisco id is 3
    cisco extended id number is 4

Ethernet1/15
    transceiver is present
    type is SFP-H10GB-CU1M
    name is UPNET
    part number is SFP+-10G-DA-1
    revision is A0
    serial number is FO1810250047
    nominal bitrate is 10300 MBit/sec
    Link length supported for copper is 1 m
    cisco id is 3
    cisco extended id number is 4

Ethernet1/16
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA2
    revision is 01
    serial number is CI1906290092
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 2 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/17
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA1
    revision is 01
    serial number is CI1906290049
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 1 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/18
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA1
    revision is 01
    serial number is CI1906290023
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 1 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/19
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA1
    revision is 01
    serial number is CI1906290063
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 1 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/20
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA1
    revision is 01
    serial number is CI1906290033
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 1 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/21
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA2
    revision is 01
    serial number is CI1906290092
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 2 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/22
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA2
    revision is 01
    serial number is CI1906290092
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 2 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/23
    transceiver is present
    type is SFP-H25GB-CU2M
    name is CISCO-UPNET
    part number is SFP28-25G-DA-2m
    revision is 01
    serial number is 7522046139(A)
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 2 m
    cable type is CA-L
    cisco id is 3
    cisco extended id number is 4

Ethernet1/24
    transceiver is present
    type is SFP-H25GB-CU2M
    name is CISCO-UPNET
    part number is SFP28-25G-DA-2m
    revision is 01
    serial number is 7522046129(A)
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 2 m
    cable type is CA-L
    cisco id is 3
    cisco extended id number is 4

Ethernet1/25
    transceiver is not present

Ethernet1/26
    transceiver is present
    type is SFP-H10GB-CU3M
    name is UPNET
    part number is SFP+-10G-DA-3
    revision is A0
    serial number is FO1810250348
    nominal bitrate is 10300 MBit/sec
    Link length supported for copper is 3 m
    cisco id is 3
    cisco extended id number is 4

Ethernet1/27
    transceiver is present
    type is SFP-H10GB-CU3M
    name is UPNET
    part number is SFP+-10G-DA-3
    revision is A0
    serial number is FO1810250259
    nominal bitrate is 10300 MBit/sec
    Link length supported for copper is 3 m
    cisco id is 3
    cisco extended id number is 4

Ethernet1/28
    transceiver is not present

Ethernet1/29
    transceiver is not present

Ethernet1/30
    transceiver is not present

Ethernet1/31
    transceiver is not present

Ethernet1/32
    transceiver is not present

Ethernet1/33
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA2
    revision is 01
    serial number is CI1906290092
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 2 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/34
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA2
    revision is 01
    serial number is CI1906290092
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 2 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/35
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA2
    revision is 01
    serial number is CI1906290092
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 2 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/36
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA2
    revision is 01
    serial number is CI1906290092
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 2 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/37
    transceiver is present
    type is Unknown Type-(unknown)
    name is TAYLE
    part number is GL-CC-SFP-030
    revision is 0000
    serial number is PI#556600002
    nominal bitrate is 10300 MBit/sec
    Link length supported for copper is 3 m
    cisco id is 3
    cisco extended id number is 4

Ethernet1/38
    transceiver is present
    type is SFP-H10GB-CU3M
    name is UPNET
    part number is SFP+-10G-DA-3
    revision is A0
    serial number is FO1810250253
    nominal bitrate is 10300 MBit/sec
    Link length supported for copper is 3 m
    cisco id is 3
    cisco extended id number is 4

Ethernet1/39
    transceiver is present
    type is SFP-H10GB-CU2M
    name is UPNET
    part number is SFP+-10G-DA-2
    revision is A0
    serial number is FO1810250130
    nominal bitrate is 10300 MBit/sec
    Link length supported for copper is 2 m
    cisco id is 3
    cisco extended id number is 4

Ethernet1/40
    transceiver is present
    type is SFP-H10GB-CU2M
    name is UPNET
    part number is SFP+-10G-DA-2
    revision is A0
    serial number is FO1810250123
    nominal bitrate is 10300 MBit/sec
    Link length supported for copper is 2 m
    cisco id is 3
    cisco extended id number is 4

Ethernet1/41
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA2
    revision is 01
    serial number is CI1906290092
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 2 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/42
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA2
    revision is 01
    serial number is CI1906290092
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 2 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/43
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA2
    revision is 01
    serial number is CI1906290092
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 2 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/44
    transceiver is present
    type is SFP-H25GB-Unknown
    name is OEM
    part number is BZ-SFP28-25G-DA2
    revision is 01
    serial number is CI1906290092
    nominal bitrate is 25500 MBit/sec
    Link length supported for copper is 2 m
    cable type is unknown
    cisco id is 3
    cisco extended id number is 4

Ethernet1/45
    transceiver is not present

Ethernet1/46
    transceiver is not present

Ethernet1/47
    transceiver is present
    type is SFP-H10GB-CU3M
    name is UPNET
    part number is SFP+-10G-DA-3
    revision is A0
    serial number is FO1810250320
    nominal bitrate is 10300 MBit/sec
    Link length supported for copper is 3 m
    cisco id is 3
    cisco extended id number is 4

Ethernet1/48
    transceiver is present
    type is SFP-H10GB-CU2M
    name is UPNET
    part number is SFP+-10G-DA-2
    revision is A0
    serial number is FO1810250200
    nominal bitrate is 10300 MBit/sec
    Link length supported for copper is 2 m
    cisco id is 3
    cisco extended id number is 4

Ethernet1/49
    transceiver is present
    type is QSFP-100G-LR4
    name is OEM
    part number is BZ-QSFP28-100G-E
    revision is A 
    serial number is GS2008105001
    nominal bitrate is 25500 MBit/sec
    Link length supported for 9/125um fiber is 40 km
    cisco id is 17
    cisco extended id number is 204

Ethernet1/50
    transceiver is present
    type is QSFP-40G-SR-BD
    name is CISCO-AVAGO
    part number is AFBR-79EBPZ-CS2
    revision is 01
    serial number is AVM2152U54A
    nominal bitrate is 20600 MBit/sec per channel
    Link length supported for 50/125um OM3 fiber is 100 m
    cisco id is 13
    cisco extended id number is 220
    cisco part number is 10-2945-02
    cisco product id is QSFP-40G-SR-BD
    cisco version id is V02

Ethernet1/51
    transceiver is present
    type is QSFP-40G-SR-BD
    name is CISCO-AVAGO
    part number is AFBR-79EBPZ-CS2
    revision is 01
    serial number is AVM1828U4JG
    nominal bitrate is 20600 MBit/sec per channel
    Link length supported for 50/125um OM3 fiber is 100 m
    cisco id is 13
    cisco extended id number is 220
    cisco part number is 10-2945-02
    cisco product id is QSFP-40G-SR-BD
    cisco version id is V02

Ethernet1/52
    transceiver is present
    type is QSFP-40G-SR-BD
    name is UPNET
    part number is WDM QSFP+-40G-SR
    revision is 01
    serial number is 52CI19022808
    nominal bitrate is 20600 MBit/sec per channel
    Link length supported for 50/125um OM3 fiber is 100 m
    cisco id is 13
    cisco extended id number is 220

Ethernet1/53
    transceiver is present
    type is QSFP-40G-SR-BD
    name is CISCO-AVAGO
    part number is AFBR-79EBPZ-CS2
    revision is 01
    serial number is AVM1828U4HW
    nominal bitrate is 20600 MBit/sec per channel
    Link length supported for 50/125um OM3 fiber is 100 m
    cisco id is 13
    cisco extended id number is 220
    cisco part number is 10-2945-02
    cisco product id is QSFP-40G-SR-BD
    cisco version id is V02

Ethernet1/54
    transceiver is present
    type is QSFP-40G-SR-BD
    name is CISCO-AVAGO
    part number is AFBR-79EBPZ-CS2
    revision is 01
    serial number is AVM2152U54D
    nominal bitrate is 20600 MBit/sec per channel
    Link length supported for 50/125um OM3 fiber is 100 m
    cisco id is 13
    cisco extended id number is 220
    cisco part number is 10-2945-02
    cisco product id is QSFP-40G-SR-BD
    cisco version id is V02

Ethernet1/55
    transceiver is present
    type is QSFP-40G-SR-BD
    name is CISCO-AVAGO
    part number is AFBR-79EBPZ-CS2
    revision is 01
    serial number is AVM2152U5BR
    nominal bitrate is 20600 MBit/sec per channel
    Link length supported for 50/125um OM3 fiber is 100 m
    cisco id is 13
    cisco extended id number is 220
    cisco part number is 10-2945-02
    cisco product id is QSFP-40G-SR-BD
    cisco version id is V02

Ethernet1/56
    transceiver is present
    type is QSFP-40G-SR-BD
    name is CISCO-AVAGO
    part number is AFBR-79EBPZ-CS2
    revision is 01
    serial number is AVM2152U54V
    nominal bitrate is 20600 MBit/sec per channel
    Link length supported for 50/125um OM3 fiber is 100 m
    cisco id is 13
    cisco extended id number is 220
    cisco part number is 10-2945-02
    cisco product id is QSFP-40G-SR-BD
    cisco version id is V02

Ethernet1/57
    transceiver is present
    type is QSFP-40G-SR-BD
    name is CISCO-AVAGO
    part number is AFBR-79EBPZ-CS2
    revision is 01
    serial number is AVM2152U0R0
    nominal bitrate is 20600 MBit/sec per channel
    Link length supported for 50/125um OM3 fiber is 100 m
    cisco id is 13
    cisco extended id number is 220
    cisco part number is 10-2945-02
    cisco product id is QSFP-40G-SR-BD
    cisco version id is V02

Ethernet1/58
    transceiver is present
    type is QSFP-40G-SR-BD
    name is CISCO-AVAGO
    part number is AFBR-79EBPZ-CS2
    revision is 01
    serial number is AVM1832U1WK
    nominal bitrate is 20600 MBit/sec per channel
    Link length supported for 50/125um OM3 fiber is 100 m
    cisco id is 13
    cisco extended id number is 220
    cisco part number is 10-2945-02
    cisco product id is QSFP-40G-SR-BD
    cisco version id is V02

Ethernet1/59
    transceiver is present
    type is QSFP-40G-SR-BD
    name is UPNET
    part number is WDM QSFP+-40G-SR
    revision is 01
    serial number is 52CI19022817
    nominal bitrate is 20600 MBit/sec per channel
    Link length supported for 50/125um OM3 fiber is 100 m
    cisco id is 13
    cisco extended id number is 220

Ethernet1/60
    transceiver is present
    type is QSFP-40G-SR-BD
    name is CISCO-AVAGO
    part number is AFBR-79EBPZ-CS2
    revision is 01
    serial number is AVM1829U7HN
    nominal bitrate is 20600 MBit/sec per channel
    Link length supported for 50/125um OM3 fiber is 100 m
    cisco id is 13
    cisco extended id number is 220
    cisco part number is 10-2945-02
    cisco product id is QSFP-40G-SR-BD
    cisco version id is V02
```

**Help:** execute the command "show interface transceiver"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip bgp neighbors

**Output:**
```
BGP neighbor is 136.170.1.201,  remote AS 64826, ibgp link,  Peer index 1
  Inherits peer configuration from peer-template SPINES
  Description: from boo to donkey
  BGP version 4, remote router ID 251.243.49.1076
  BGP state = Established, up for 1d01h
  Using loopback0 as update source for this peer
  TCP MD5 authentication is set (enabled)
  Last read 00:00:13, hold time = 180, keepalive interval is 60 seconds
  Last written 00:00:16, keepalive timer expiry due 00:00:43
  Received 906098 messages, 1 notifications, 0 bytes in queue
  Sent 200932 messages, 1 notifications, 0 bytes in queue
  Connections established 3, dropped 2
  Last reset by us 1d10h, due to holdtimer expired error
  Last reset by peer 1w1d, due to administratively shutdown

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Address family L2VPN EVPN: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast  L2VPN EVPN
  Address families received from peer:
    IPv4 Unicast  L2VPN EVPN
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised received
  Receive IPv6 next hop encoding Capability for AF:
    IPv4 Unicast

  Message statistics:
                              Sent               Rcvd
  Opens:                        24                  3
  Notifications:                 1                  1
  Updates:                    8514             743363
  Keepalives:               192374             162725
  Route Refresh:                13                  0
  Capability:                    6                  6
  Total:                    200932             906098
  Total bytes:             4570033           85316584
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 10317, neighbor version 10317
  226 accepted paths consume 28024 bytes of memory
  5 sent paths
  Nexthop always set to local peering address, 57.84.92.1388
  Third-party Nexthop will not be computed.
  Last End-of-RIB received 00:00:01 after session start

  For address family: L2VPN EVPN
  BGP table version 1123760, neighbor version 1123760
  8458 accepted paths consume 1048792 bytes of memory
  608 sent paths
  Community attribute sent to this neighbor
  Extended community attribute sent to this neighbor
  Third-party Nexthop will not be computed.
  Last End-of-RIB received 00:00:02 after session start

  Local host: 34.83.217.230, Local port: 31643
  Foreign host: 226.176.223.89, Foreign port: 179
  fd = 82

BGP neighbor is 174.8.181.98,  remote AS 64826, ibgp link,  Peer index 2
  Inherits peer configuration from peer-template SPINES
  Description: from foo to baz
  BGP version 4, remote router ID 249.8.88.647
  BGP state = Established, up for 1w0d
  Using loopback0 as update source for this peer
  TCP MD5 authentication is set (enabled)
  Last read 00:00:13, hold time = 180, keepalive interval is 60 seconds
  Last written 00:00:16, keepalive timer expiry due 00:00:43
  Received 860816 messages, 1 notifications, 0 bytes in queue
  Sent 201506 messages, 0 notifications, 0 bytes in queue
  Connections established 2, dropped 1
  Last reset by us 1w0d, due to session closed
  Last reset by peer 1w0d, due to administratively shutdown

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Address family L2VPN EVPN: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast  L2VPN EVPN
  Address families received from peer:
    IPv4 Unicast  L2VPN EVPN
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised received
  Receive IPv6 next hop encoding Capability for AF:
    IPv4 Unicast

  Message statistics:
                              Sent               Rcvd
  Opens:                        10                  2
  Notifications:                 0                  1
  Updates:                    8559             697776
  Keepalives:               192920             163033
  Route Refresh:                13                  0
  Capability:                    4                  4
  Total:                    201506             860816
  Total bytes:             4562658           80515353
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 10317, neighbor version 10317
  225 accepted paths consume 27900 bytes of memory
  5 sent paths
  Nexthop always set to local peering address, 255.60.99.1798
  Third-party Nexthop will not be computed.
  Last End-of-RIB received 0.201056 after session start

  For address family: L2VPN EVPN
  BGP table version 1123760, neighbor version 1123760
  8458 accepted paths consume 1048792 bytes of memory
  608 sent paths
  Community attribute sent to this neighbor
  Extended community attribute sent to this neighbor
  Third-party Nexthop will not be computed.
  Last End-of-RIB received 0.651312 after session start

  Local host: 29.91.80.176, Local port: 179
  Foreign host: 127.145.91.46, Foreign port: 52469
  fd = 84

BGP neighbor is 171.143.203.215,  remote AS 64826, ibgp link,  Peer index 3
  Inherits peer configuration from peer-template SPINES
  Description: from bar to frog
  BGP version 4, remote router ID 80.252.118.818
  BGP state = Established, up for 3d21h
  Using loopback0 as update source for this peer
  TCP MD5 authentication is set (enabled)
  Last read 00:00:13, hold time = 180, keepalive interval is 60 seconds
  Last written 00:00:16, keepalive timer expiry due 00:00:43
  Received 907269 messages, 1 notifications, 0 bytes in queue
  Sent 201494 messages, 0 notifications, 0 bytes in queue
  Connections established 2, dropped 1
  Last reset by us 3d21h, due to session closed
  Last reset by peer 3d23h, due to administratively shutdown

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Address family L2VPN EVPN: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast  L2VPN EVPN
  Address families received from peer:
    IPv4 Unicast  L2VPN EVPN
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised received
  Receive IPv6 next hop encoding Capability for AF:
    IPv4 Unicast

  Message statistics:
                              Sent               Rcvd
  Opens:                        20                  2
  Notifications:                 0                  1
  Updates:                    8558             744278
  Keepalives:               192899             162984
  Route Refresh:                13                  0
  Capability:                    4                  4
  Total:                    201494             907269
  Total bytes:             4562535           84937258
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 10317, neighbor version 10317
  225 accepted paths consume 27900 bytes of memory
  5 sent paths
  Nexthop always set to local peering address, 206.212.210.1498
  Third-party Nexthop will not be computed.
  Last End-of-RIB received 0.707848 after session start

  For address family: L2VPN EVPN
  BGP table version 1123760, neighbor version 1123760
  8458 accepted paths consume 1048792 bytes of memory
  608 sent paths
  Community attribute sent to this neighbor
  Extended community attribute sent to this neighbor
  Third-party Nexthop will not be computed.
  Last End-of-RIB received 00:00:01 after session start

  Local host: 190.125.83.222, Local port: 179
  Foreign host: 231.231.113.66, Foreign port: 22132
  fd = 83

BGP neighbor is 94.210.82.240,  remote AS 64826, ibgp link,  Peer index 4
  Inherits peer configuration from peer-template SPINES
  Description: from baz to monkey
  BGP version 4, remote router ID 237.83.240.109
  BGP state = Established, up for 3d15h
  Using loopback0 as update source for this peer
  TCP MD5 authentication is set (enabled)
  Last read 00:00:13, hold time = 180, keepalive interval is 60 seconds
  Last written 00:00:16, keepalive timer expiry due 00:00:43
  Received 907296 messages, 1 notifications, 0 bytes in queue
  Sent 201441 messages, 0 notifications, 0 bytes in queue
  Connections established 2, dropped 1
  Last reset by us 3d15h, due to session closed
  Last reset by peer 3d18h, due to administratively shutdown

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Address family L2VPN EVPN: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast  L2VPN EVPN
  Address families received from peer:
    IPv4 Unicast  L2VPN EVPN
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised received
  Receive IPv6 next hop encoding Capability for AF:
    IPv4 Unicast

  Message statistics:
                              Sent               Rcvd
  Opens:                        13                  2
  Notifications:                 0                  1
  Updates:                    8566             744351
  Keepalives:               192845             162938
  Route Refresh:                13                  0
  Capability:                    4                  4
  Total:                    201441             907296
  Total bytes:             4562211           84952999
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 10317, neighbor version 10317
  226 accepted paths consume 28024 bytes of memory
  5 sent paths
  Nexthop always set to local peering address, 194.112.107.1118
  Third-party Nexthop will not be computed.
  Last End-of-RIB received 0.609480 after session start

  For address family: L2VPN EVPN
  BGP table version 1123760, neighbor version 1123760
  8458 accepted paths consume 1048792 bytes of memory
  608 sent paths
  Community attribute sent to this neighbor
  Extended community attribute sent to this neighbor
  Third-party Nexthop will not be computed.
  Last End-of-RIB received 00:00:01 after session start

  Local host: 61.84.112.233, Local port: 179
  Foreign host: 221.224.143.168, Foreign port: 21548
  fd = 81

BGP neighbor is 143.128.128.163,  remote AS 64938, ibgp link,  Peer index 1
  Inherits peer configuration from peer-template SPINES
  Description: from foo to foo
  BGP version 4, remote router ID 10.46.0.1
  BGP state = Established, up for 3d15h
  Using loopback0 as update source for this peer
  TCP MD5 authentication is set (enabled)
  Last read 00:00:22, hold time = 180, keepalive interval is 60 seconds
  Last written 00:00:26, keepalive timer expiry due 00:00:33
  Received 5284 messages, 0 notifications, 0 bytes in queue
  Sent 5284 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Address family L2VPN EVPN: received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
    IPv4 Unicast  L2VPN EVPN
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised received
  Receive IPv6 next hop encoding Capability for AF:
    IPv4 Unicast

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                       1                  1
  Keepalives:                 5279               5279
  Route Refresh:                 0                  0
  Capability:                    3                  3
  Total:                      5284               5284
  Total bytes:              100396             100400
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 4, neighbor version 4
  0 accepted paths consume 0 bytes of memory
  0 sent paths
  Community attribute sent to this neighbor
  Extended community attribute sent to this neighbor
  Third-party Nexthop will not be computed.
  Last End-of-RIB received 00:00:01 after session start

  Local host: 144.125.246.17, Local port: 36220
  Foreign host: 72.193.89.91, Foreign port: 179
  fd = 70

 BGP neighbor is 12.26.221.3,  remote AS 64938, ibgp link,  Peer index 2
  Inherits peer configuration from peer-template SPINES
  Description: from donkey to boo
  BGP version 4, remote router ID 10.46.0.2
  BGP state = Established, up for 3d15h
  Using loopback0 as update source for this peer
  TCP MD5 authentication is set (enabled)
  Last read 00:00:35, hold time = 180, keepalive interval is 60 seconds
  Last written 00:00:38, keepalive timer expiry due 00:00:21
  Received 5284 messages, 0 notifications, 0 bytes in queue
  Sent 5284 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Address family L2VPN EVPN: received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
    IPv4 Unicast  L2VPN EVPN
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised received
  Receive IPv6 next hop encoding Capability for AF:
    IPv4 Unicast

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                       1                  1
  Keepalives:                 5279               5279
  Route Refresh:                 0                  0
  Capability:                    3                  3
  Total:                      5284               5284
  Total bytes:              100396             100400
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 4, neighbor version 4
  0 accepted paths consume 0 bytes of memory
  0 sent paths
  Community attribute sent to this neighbor
  Extended community attribute sent to this neighbor
  Third-party Nexthop will not be computed.
  Last End-of-RIB received 00:00:01 after session start

  Local host: 210.219.168.143, Local port: 48355
  Foreign host: 220.134.183.122, Foreign port: 179
  fd = 71

BGP neighbor is 202.77.85.157,  remote AS 64938, ibgp link,  Peer index 3
  Inherits peer configuration from peer-template SPINES
  Description: from donkey to boo
  BGP version 4, remote router ID 0.0.0.0
  BGP state = Idle, down for 3d16h, retry in 00:00:33
  Using loopback0 as update source for this peer
  TCP MD5 authentication is set (disabled)
  Last read never, hold time = 180, keepalive interval is 60 seconds
  Last written never, keepalive timer not running
  Received 0 messages, 0 notifications, 0 bytes in queue
  Sent 0 messages, 0 notifications, 0 bytes in queue
  Connections established 0, dropped 0
  Connection attempts 4248
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Message statistics:
                              Sent               Rcvd
  Opens:                         0                  0
  Notifications:                 0                  0
  Updates:                       0                  0
  Keepalives:                    0                  0
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                         0                  0
  Total bytes:                   0                  0
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 4, neighbor version 0
  0 accepted paths consume 0 bytes of memory
  0 sent paths
  Community attribute sent to this neighbor
  Extended community attribute sent to this neighbor
  Third-party Nexthop will not be computed.

  No established BGP session with peer

BGP neighbor is 47.48.246.179,  remote AS 64938, ibgp link,  Peer index 4
  Inherits peer configuration from peer-template SPINES
  Description: from bar to monkey
  BGP version 4, remote router ID 0.0.0.0
  BGP state = Idle, down for 3d16h, retry in 00:01:19
  Using loopback0 as update source for this peer
  TCP MD5 authentication is set (disabled)
  Last read never, hold time = 180, keepalive interval is 60 seconds
  Last written never, keepalive timer not running
  Received 0 messages, 0 notifications, 0 bytes in queue
  Sent 0 messages, 0 notifications, 0 bytes in queue
  Connections established 0, dropped 0
  Connection attempts 4270
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Message statistics:
                              Sent               Rcvd
  Opens:                         0                  0
  Notifications:                 0                  0
  Updates:                       0                  0
  Keepalives:                    0                  0
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                         0                  0
  Total bytes:                   0                  0
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 4, neighbor version 0
  0 accepted paths consume 0 bytes of memory
  0 sent paths
  Community attribute sent to this neighbor
  Extended community attribute sent to this neighbor
  Third-party Nexthop will not be computed.

  No established BGP session with peer

BGP neighbor is 217.90.29.79,  remote AS 65003, ebgp link,  Peer index 1
  Inherits peer configuration from peer-template MPLS_WanCore
  Description: from bing to bing
  BGP version 4, remote router ID 10.0.0.3
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface Ethernet5/24
  Last read 00:00:02, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1205978 messages, 0 notifications, 0 bytes in queue
  Sent 1413795 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
    IPv4 Unicast
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                  938868             857498
  Keepalives:               474926             348479
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1413795            1205978
  Total bytes:           116954780           99012794
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  51195 accepted paths consume 3071700 bytes of memory
  10303 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Last End-of-RIB received 00:00:06 after session start

  Local host: 148.188.153.56, Local port: 24169
  Foreign host: 22.15.33.118, Foreign port: 179
  fd = 68

BGP neighbor is 167.161.119.185,  remote AS 65003, ebgp link,  Peer index 2
  Inherits peer configuration from peer-template MPLS_WanCore
  Description: from monkey to monkey
  BGP version 4, remote router ID 10.0.0.4
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface Ethernet6/24
  Last read 00:00:02, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1223233 messages, 0 notifications, 0 bytes in queue
  Sent 1412915 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
    IPv4 Unicast
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                  937989             875258
  Keepalives:               474925             347974
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1412915            1223233
  Total bytes:           116855577          101143596
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  51195 accepted paths consume 3071700 bytes of memory
  10303 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Last End-of-RIB received 00:00:06 after session start

  Local host: 77.16.23.163, Local port: 179
  Foreign host: 228.67.65.167, Foreign port: 28699
  fd = 91

BGP neighbor is 129.33.213.49,  remote AS 64991, ebgp link,  Peer index 3
  Inherits peer configuration from peer-template Standard-Leg
  Description: from boo to frog
  BGP version 4, remote router ID 79.194.1.2394
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface port-channel101
  TCP MD5 authentication is enabled
  Last read 00:00:12, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1173611 messages, 0 notifications, 0 bytes in queue
  Sent 1996295 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1534229             633313
  Keepalives:               462065             540297
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1996295            1173611
  Total bytes:           159499836           71640462
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  117 accepted paths consume 7020 bytes of memory
  53329 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 30.251.237.123, Local port: 29517
  Foreign host: 88.181.26.218, Foreign port: 179
  fd = 79

BGP neighbor is 134.81.203.129,  remote AS 64563, ebgp link,  Peer index 4
  Inherits peer configuration from peer-template Standard-Leg
  Description: from baz to boo
  BGP version 4, remote router ID 168.184.251.470
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface port-channel102
  TCP MD5 authentication is enabled
  Last read 00:00:03, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1069823 messages, 0 notifications, 0 bytes in queue
  Sent 1996406 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1534343             529532
  Keepalives:               462062             540290
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1996406            1069823
  Total bytes:           159507685           58482473
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  2 accepted paths consume 120 bytes of memory
  53444 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 27.27.246.137, Local port: 29341
  Foreign host: 121.155.249.169, Foreign port: 179
  fd = 77
 
BGP neighbor is 87.209.8.85,  remote AS 64564, ebgp link,  Peer index 5
  Inherits peer configuration from peer-template Standard-Leg
  Description: from monkey to foo
  BGP version 4, remote router ID 204.223.212.780
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface port-channel103
  TCP MD5 authentication is enabled
  Last read 00:00:05, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1077286 messages, 0 notifications, 0 bytes in queue
  Sent 1995741 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1533678             536991
  Keepalives:               462062             540294
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1995741            1077286
  Total bytes:           159433865           59253810
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  2 accepted paths consume 120 bytes of memory
  53444 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 142.198.83.176, Local port: 29565
  Foreign host: 72.243.246.239, Foreign port: 179
  fd = 82

 BGP neighbor is 232.122.144.131,  remote AS 64520, ebgp link,  Peer index 6
  Inherits peer configuration from peer-template Standard-Leg
  Description: from frog to bing
  BGP version 4, remote router ID 186.211.15.2194
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface port-channel104
  TCP MD5 authentication is enabled
  Last read 00:00:01, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1194123 messages, 0 notifications, 0 bytes in queue
  Sent 1995749 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1533676             653827
  Keepalives:               462072             540295
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1995749            1194123
  Total bytes:           159436316           70997495
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  12 accepted paths consume 720 bytes of memory
  53434 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 83.39.58.145, Local port: 29751
  Foreign host: 249.71.59.33, Foreign port: 179
  fd = 84

 BGP neighbor is 255.6.79.240,  remote AS 64521, ebgp link,  Peer index 7
  Inherits peer configuration from peer-template Standard-Leg
  Description: from baz to bar
  BGP version 4, remote router ID 138.247.170.544
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface port-channel105
  TCP MD5 authentication is enabled
  Last read 00:00:13, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1175530 messages, 0 notifications, 0 bytes in queue
  Sent 1995481 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1533414             635238
  Keepalives:               462066             540291
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1995481            1175530
  Total bytes:           159402410           71901157
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  9 accepted paths consume 540 bytes of memory
  53437 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 159.85.223.154, Local port: 30455
  Foreign host: 88.87.6.2, Foreign port: 179
  fd = 97

BGP neighbor is 135.138.128.239,  remote AS 64522, ebgp link,  Peer index 8
  Inherits peer configuration from peer-template Standard-Leg
  Description: from bing to donkey
  BGP version 4, remote router ID 177.212.30.864
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface port-channel106
  TCP MD5 authentication is enabled
  Last read 00:00:07, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1175577 messages, 0 notifications, 0 bytes in queue
  Sent 1995513 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1533446             635285
  Keepalives:               462066             540291
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1995513            1175577
  Total bytes:           159405036           71887964
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  12 accepted paths consume 720 bytes of memory
  53434 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 115.48.39.12, Local port: 29928
  Foreign host: 187.84.208.112, Foreign port: 179
  fd = 86

 BGP neighbor is 166.177.87.84,  remote AS 64523, ebgp link,  Peer index 9
  Inherits peer configuration from peer-template Standard-Leg
  Description: from boo to monkey
  BGP version 4, remote router ID 11.132.72.134
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface port-channel107
  TCP MD5 authentication is enabled
  Last read 00:00:01, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1087024 messages, 0 notifications, 0 bytes in queue
  Sent 1996708 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1534639             657289
  Keepalives:               462068             429734
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1996708            1087024
  Total bytes:           159546312           71926991
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  10 accepted paths consume 600 bytes of memory
  53436 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 121.14.31.73, Local port: 179
  Foreign host: 22.41.156.160, Foreign port: 59645
  fd = 69

 BGP neighbor is 24.218.246.161,  remote AS 64525, ebgp link,  Peer index 10
  Inherits peer configuration from peer-template Standard-Leg
  Description: from frog to foo
  BGP version 4, remote router ID 23.86.193.565
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface port-channel108
  TCP MD5 authentication is enabled
  Last read 00:00:10, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1216870 messages, 0 notifications, 0 bytes in queue
  Sent 1994773 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1532707             676579
  Keepalives:               462065             540290
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1994773            1216870
  Total bytes:           159325085           76128478
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  3 accepted paths consume 180 bytes of memory
  53443 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 46.95.207.194, Local port: 30808
  Foreign host: 249.173.131.89, Foreign port: 179
  fd = 102
 
BGP neighbor is 88.158.245.249,  remote AS 64524, ebgp link,  Peer index 11
  Inherits peer configuration from peer-template Standard-Leg
  Description: from bing to monkey
  BGP version 4, remote router ID 142.201.248.2474
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface port-channel109
  TCP MD5 authentication is enabled
  Last read 00:00:02, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1214103 messages, 0 notifications, 0 bytes in queue
  Sent 1994815 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1532747             673811
  Keepalives:               462067             540291
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1994815            1214103
  Total bytes:           159330896           75757206
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  1 accepted paths consume 60 bytes of memory
  53445 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 19.33.193.41, Local port: 30630
  Foreign host: 113.114.126.174, Foreign port: 179
  fd = 100

BGP neighbor is 209.58.188.204,  remote AS 65150, ebgp link,  Peer index 12
  Inherits peer configuration from peer-template Standard-Leg
  Description: from monkey to foo
  BGP version 4, remote router ID 38.154.204.99
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface port-channel110
  TCP MD5 authentication is enabled
  Last read 00:00:09, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1185942 messages, 0 notifications, 0 bytes in queue
  Sent 1994538 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1532440             645646
  Keepalives:               462097             540295
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1994538            1185942
  Total bytes:           159307244           72795532
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  247 accepted paths consume 14820 bytes of memory
  53199 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 79.138.5.173, Local port: 30104
  Foreign host: 241.90.87.199, Foreign port: 179
  fd = 90

 BGP neighbor is 168.96.139.211,  remote AS 65510, ebgp link,  Peer index 13
  Inherits peer configuration from peer-template Standard-Leg
  Description: from monkey to baz
  BGP version 4, remote router ID 176.222.95.1033
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface port-channel121
  TCP MD5 authentication is enabled
  Last read 0.912799, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1191434 messages, 0 notifications, 0 bytes in queue
  Sent 1993836 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1531755             651138
  Keepalives:               462080             540295
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1993836            1191434
  Total bytes:           159216507           73439672
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  61 accepted paths consume 3660 bytes of memory
  53385 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 191.131.46.70, Local port: 30959
  Foreign host: 224.44.237.104, Foreign port: 179
  fd = 106

BGP neighbor is 131.243.190.190,  remote AS 65152, ebgp link,  Peer index 14
  Inherits peer configuration from peer-template Standard-Leg
  Description: from bing to bing
  BGP version 4, remote router ID 105.207.18.158
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface port-channel122
  TCP MD5 authentication is enabled
  Last read 00:00:14, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 543643 messages, 0 notifications, 0 bytes in queue
  Sent 1992372 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
    IPv4 Unicast
  Forwarding state preserved by peer for:
    IPv4 Unicast
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised received
  Receive IPv6 next hop encoding Capability for AF:
    IPv4 Unicast

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1529417               4645
  Keepalives:               462954             538997
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1992372             543643
  Total bytes:           204149228           10483590
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  324 accepted paths consume 19440 bytes of memory
  53122 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%
  Last End-of-RIB received 00:00:01 after session start

  Local host: 233.29.157.75, Local port: 179
  Foreign host: 116.246.167.246, Foreign port: 27360
  fd = 85

BGP neighbor is 103.90.75.222,  remote AS 65533, ebgp link,  Peer index 15
  Inherits peer configuration from peer-template Standard-Leg
  Description: from donkey to baz
  BGP version 4, remote router ID 157.132.40.799
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface Ethernet5/2
  TCP MD5 authentication is enabled
  Last read 00:00:08, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1175230 messages, 0 notifications, 0 bytes in queue
  Sent 1996448 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1534379             634933
  Keepalives:               462068             540296
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1996448            1175230
  Total bytes:           159527265           68391959
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  258 accepted paths consume 15480 bytes of memory
  53236 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 159.247.127.30, Local port: 28632
  Foreign host: 27.240.178.84, Foreign port: 179
  fd = 65

BGP neighbor is 122.169.105.222,  remote AS 65532, ebgp link,  Peer index 20
  Inherits peer configuration from peer-template Standard-Leg
  Description: from monkey to baz
  BGP version 4, remote router ID 157.27.199.2391
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface Ethernet5/6
  TCP MD5 authentication is enabled
  Last read 00:00:08, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1190783 messages, 0 notifications, 0 bytes in queue
  Sent 1994786 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1532715             650489
  Keepalives:               462070             540293
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1994786            1190783
  Total bytes:           159321595           69981415
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  265 accepted paths consume 15900 bytes of memory
  53375 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 167.143.174.37, Local port: 29025
  Foreign host: 133.127.112.13, Foreign port: 179
  fd = 70

BGP neighbor is 248.253.184.199,  remote AS 64526, ebgp link,  Peer index 21
  Inherits peer configuration from peer-template Standard-Leg
  Description: from donkey to foo
  BGP version 4, remote router ID 56.221.192.2063
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface port-channel123
  TCP MD5 authentication is enabled
  Last read 00:00:04, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1204718 messages, 0 notifications, 0 bytes in queue
  Sent 1994668 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1532601             664426
  Keepalives:               462066             540291
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1994668            1204718
  Total bytes:           159313024           74725071
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  33 accepted paths consume 1980 bytes of memory
  53413 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 117.70.157.199, Local port: 30297
  Foreign host: 234.33.202.152, Foreign port: 179
  fd = 94

BGP neighbor is 113.9.147.198,  remote AS 64517, ebgp link,  Peer index 22
  Inherits peer configuration from peer-template Standard-Leg
  Description: from boo to bing
  BGP version 4, remote router ID 106.121.225.2254
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface port-channel124
  TCP MD5 authentication is enabled
  Last read 00:00:01, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1058610 messages, 0 notifications, 0 bytes in queue
  Sent 1995134 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1533067             654504
  Keepalives:               462066             404105
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1995134            1058610
  Total bytes:           159354403           71166342
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  7 accepted paths consume 420 bytes of memory
  53439 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 158.80.154.105, Local port: 30528
  Foreign host: 124.68.182.124, Foreign port: 179
  fd = 98

 BGP neighbor is 178.51.35.168,  remote AS 64568, ebgp link,  Peer index 23
  Inherits peer configuration from peer-template Standard-Leg
  Description: from bar to foo
  BGP version 4, remote router ID 0.0.0.0
  BGP state = Shut (Admin), down for 13w2d
  Last read never, hold time = 45, keepalive interval is 15 seconds
  Last written never, keepalive timer not running
  Received 0 messages, 0 notifications, 0 bytes in queue
  Sent 0 messages, 0 notifications, 0 bytes in queue
  Connections established 0, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Message statistics:
                              Sent               Rcvd
  Opens:                         0                  0
  Notifications:                 0                  0
  Updates:                       0                  0
  Keepalives:                    0                  0
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                         0                  0
  Total bytes:                   0                  0
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 0
  0 accepted paths consume 0 bytes of memory
  0 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 30000
  Threshold for warning messages 75%

  No established BGP session with peer
 
BGP neighbor is 212.164.170.242,  remote AS 63000, ebgp link,  Peer index 24
  Inherits peer configuration from peer-template Standard-Leg
  Description: from bing to monkey
  BGP version 4, remote router ID 251.20.97.1225
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface port-channel125
  TCP MD5 authentication is enabled
  Last read 00:00:09, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 818135 messages, 0 notifications, 0 bytes in queue
  Sent 1993594 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1531531             277837
  Keepalives:               462062             540297
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1993594             818135
  Total bytes:           159180954           37605685
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  6 accepted paths consume 360 bytes of memory
  53440 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 42.49.226.128, Local port: 30976
  Foreign host: 187.198.29.137, Foreign port: 179
  fd = 112
 
BGP neighbor is 162.55.172.94,  remote AS 65205, ebgp link,  Peer index 25
  Inherits peer configuration from peer-template Standard-Leg
  Description: from boo to foo
  BGP version 4, remote router ID 229.170.129.1504
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface Ethernet5/1
  TCP MD5 authentication is enabled
  Last read 00:00:09, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 540378 messages, 0 notifications, 0 bytes in queue
  Sent 1993712 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1531655                 85
  Keepalives:               462056             540292
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1993712             540378
  Total bytes:           159219708           10269707
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  54 accepted paths consume 3240 bytes of memory
  53392 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%
  Inbound ip prefix-list configured is DENY_DEFAULT_ALLOW_PCI, handle obtained

  Local host: 99.106.129.169, Local port: 29117
  Foreign host: 130.223.103.98, Foreign port: 179
  fd = 71

BGP neighbor is 117.185.189.71,  remote AS 64519, ebgp link,  Peer index 26
  Inherits peer configuration from peer-template Standard-Leg
  Description: from monkey to donkey
  BGP version 4, remote router ID 172.249.91.510
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface port-channel126
  TCP MD5 authentication is enabled
  Last read 00:00:01, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1036321 messages, 0 notifications, 0 bytes in queue
  Sent 1995243 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1533153             618470
  Keepalives:               462089             417850
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1995243            1036321
  Total bytes:           159372385           64469061
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  94 accepted paths consume 5640 bytes of memory
  53352 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 222.163.71.138, Local port: 179
  Foreign host: 60.17.163.56, Foreign port: 35869
  fd = 78
 
BGP neighbor is 11.17.141.125,  remote AS 64980, ebgp link,  Peer index 27
  Inherits peer configuration from peer-template Standard-Leg
  Description: from baz to frog
  BGP version 4, remote router ID 200.253.227.465
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface port-channel127
  TCP MD5 authentication is enabled
  Last read 0.188752, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 540449 messages, 0 notifications, 0 bytes in queue
  Sent 1993020 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1530946                157
  Keepalives:               462073             540291
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1993020             540449
  Total bytes:           159108645           10275086
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  155 accepted paths consume 9300 bytes of memory
  53292 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 204.196.181.66, Local port: 31129
  Foreign host: 40.101.222.225, Foreign port: 179
  fd = 113

BGP neighbor is 157.89.123.211,  remote AS 65290, ebgp link,  Peer index 28
  Inherits peer configuration from peer-template Standard-Leg
  Description: from foo to bing
  BGP version 4, remote router ID 50.28.84.1680
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface port-channel128
  TCP MD5 authentication is enabled
  Last read 00:00:01, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1100863 messages, 0 notifications, 0 bytes in queue
  Sent 1993261 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1530832             675340
  Keepalives:               462428             425522
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1993261            1100863
  Total bytes:           159185878           74252109
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  358 accepted paths consume 21480 bytes of memory
  53100 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 28.224.141.117, Local port: 179
  Foreign host: 128.255.228.37, Foreign port: 18524
  fd = 74

BGP neighbor is 194.134.175.38,  remote AS 64538, ebgp link,  Peer index 29
  Inherits peer configuration from peer-template Standard-Leg
  Description: from bar to frog
  BGP version 4, remote router ID 165.201.104.1339
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface Ethernet6/11
  TCP MD5 authentication is enabled
  Last read 00:00:04, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1183875 messages, 0 notifications, 0 bytes in queue
  Sent 1994248 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1532184             643578
  Keepalives:               462063             540296
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1994248            1183875
  Total bytes:           159261972           72566814
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  5 accepted paths consume 300 bytes of memory
  53441 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 29.156.12.176, Local port: 30092
  Foreign host: 119.96.208.59, Foreign port: 179
  fd = 87

 BGP neighbor is 187.149.19.88,  remote AS 64539, ebgp link,  Peer index 30
  Inherits peer configuration from peer-template Standard-Leg
  Description: from donkey to boo
  BGP version 4, remote router ID 146.48.5.531
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface Ethernet5/4
  TCP MD5 authentication is enabled
  Last read 00:00:08, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1185640 messages, 0 notifications, 0 bytes in queue
  Sent 1996014 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1533949             645340
  Keepalives:               462064             540299
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1996014            1185640
  Total bytes:           159465944           72747379
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  3 accepted paths consume 180 bytes of memory
  53443 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 26.19.106.90, Local port: 28398
  Foreign host: 195.117.50.146, Foreign port: 179
  fd = 56

BGP neighbor is 16.114.168.33,  remote AS 64542, ebgp link,  Peer index 31
  Inherits peer configuration from peer-template Standard-Leg
  Description: from donkey to donkey
  BGP version 4, remote router ID 22.189.83.416
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface Ethernet3/31
  TCP MD5 authentication is enabled
  Last read 00:00:02, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 540291 messages, 0 notifications, 0 bytes in queue
  Sent 1993570 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1531502                  3
  Keepalives:               462067             540287
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1993570             540291
  Total bytes:           159179177           10265638
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  5 accepted paths consume 300 bytes of memory
  53441 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 220.226.76.231, Local port: 30862
  Foreign host: 186.39.56.0, Foreign port: 179
  fd = 103

 BGP neighbor is 156.0.8.154,  remote AS 64544, ebgp link,  Peer index 32
  Inherits peer configuration from peer-template Standard-Leg
  Description: from foo to boo
  BGP version 4, remote router ID 229.226.243.444
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface Ethernet5/3
  TCP MD5 authentication is enabled
  Last read 00:00:10, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1188699 messages, 0 notifications, 0 bytes in queue
  Sent 1995340 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1533275             648401
  Keepalives:               462064             540297
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1995340            1188699
  Total bytes:           159385318           69708946
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  5 accepted paths consume 300 bytes of memory
  53442 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 99.240.42.174, Local port: 28790
  Foreign host: 235.228.253.157, Foreign port: 179
  fd = 66
 
BGP neighbor is 131.175.74.157,  remote AS 65155, ebgp link,  Peer index 33
  Inherits peer configuration from peer-template Standard-Leg
  Description: from donkey to donkey
  BGP version 4, remote router ID 83.144.35.24
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface Ethernet6/10
  TCP MD5 authentication is enabled
  Last read 00:00:07, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 540296 messages, 0 notifications, 0 bytes in queue
  Sent 1993409 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1531346                  2
  Keepalives:               462062             540293
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1993409             540296
  Total bytes:           159161130           10265672
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  3 accepted paths consume 180 bytes of memory
  53443 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 49.35.116.26, Local port: 30581
  Foreign host: 244.157.125.129, Foreign port: 179
  fd = 99

BGP neighbor is 48.218.155.56,  remote AS 65271, ebgp link,  Peer index 34
  Inherits peer configuration from peer-template Standard-Leg
  Description: from monkey to boo
  BGP version 4, remote router ID 0.0.0.0
  BGP state = Idle, down for 13w2d, retry in 00:00:01
  Last read never, hold time = 45, keepalive interval is 15 seconds
  Last written never, keepalive timer not running
  Received 0 messages, 0 notifications, 0 bytes in queue
  Sent 0 messages, 0 notifications, 0 bytes in queue
  Connections established 0, dropped 0
  Connection attempts 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Message statistics:
                              Sent               Rcvd
  Opens:                         0                  0
  Notifications:                 0                  0
  Updates:                       0                  0
  Keepalives:                    0                  0
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                         0                  0
  Total bytes:                   0                  0
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 0
  0 accepted paths consume 0 bytes of memory
  0 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  No established BGP session with peer

BGP neighbor is 44.153.169.176,  remote AS 65201, ebgp link,  Peer index 35
  Description: from monkey to baz
  BGP version 4, remote router ID 103.50.167.1310
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface Ethernet3/30
  TCP MD5 authentication is enabled
  Last read 00:00:09, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:01, keepalive timer expiry due 00:00:13
  Received 540305 messages, 0 notifications, 0 bytes in queue
  Sent 539741 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                       1                  2
  Keepalives:               539739             540302
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                    539741             540305
  Total bytes:            10255045           10265893
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  21 accepted paths consume 1260 bytes of memory
  0 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Outbound route-map configured is DENY_ALL, handle obtained

  Local host: 168.77.208.187, Local port: 28277
  Foreign host: 192.204.136.39, Foreign port: 179
  fd = 107

BGP neighbor is 255.247.222.27,  remote AS 65160, ebgp link,  Peer index 36
  Inherits peer configuration from peer-template Standard-Leg
  Description: from bar to bing
  BGP version 4, remote router ID 156.95.76.8
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface Ethernet6/4
  TCP MD5 authentication is enabled
  Last read 00:00:06, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 529259 messages, 0 notifications, 0 bytes in queue
  Sent 1994274 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1531827               2683
  Keepalives:               462446             526575
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1994274             529259
  Total bytes:           159358223           10115356
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  6 accepted paths consume 360 bytes of memory
  53440 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 51.154.104.202, Local port: 179
  Foreign host: 49.149.6.165, Foreign port: 18056
  fd = 73

BGP neighbor is 220.157.249.83,  remote AS 65180, ebgp link,  Peer index 37
  Inherits peer configuration from peer-template Standard-Leg
  Description: from frog to donkey
  BGP version 4, remote router ID 60.232.253.146
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface Ethernet6/5
  TCP MD5 authentication is enabled
  Last read 00:00:05, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 527762 messages, 0 notifications, 0 bytes in queue
  Sent 1995367 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1533270                253
  Keepalives:               462096             527508
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1995367             527762
  Total bytes:           159391360           10035035
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  32 accepted paths consume 1920 bytes of memory
  53414 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 16.47.100.156, Local port: 179
  Foreign host: 144.195.50.101, Foreign port: 35983
  fd = 75

BGP neighbor is 244.94.161.162,  remote AS 64546, ebgp link,  Peer index 38
  Inherits peer configuration from peer-template Standard-Leg
  Description: from boo to baz
  BGP version 4, remote router ID 166.201.194.1274
  BGP state = Established, up for 9w4d
  Peer is directly attached, interface Ethernet6/6
  TCP MD5 authentication is enabled
  Last read 00:00:03, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 539893 messages, 0 notifications, 0 bytes in queue
  Sent 2011450 messages, 0 notifications, 0 bytes in queue
  Connections established 2, dropped 1
  Last reset by peer 9w4d, due to duplicate connection request
  Last reset by us never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
    IPv4 Unicast
  Forwarding state preserved by peer for:
    IPv4 Unicast
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         2                  2
  Notifications:                 0                  0
  Updates:                 1549371                  9
  Keepalives:               462077             539882
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   2011450             539893
  Total bytes:           196954641           10258189
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  6 accepted paths consume 360 bytes of memory
  53441 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%
  Last End-of-RIB received 00:00:08 after session start

  Local host: 30.246.241.47, Local port: 15942
  Foreign host: 170.229.101.87, Foreign port: 179
  fd = 88

BGP neighbor is 132.115.163.171,  remote AS 65105, ebgp link,  Peer index 39
  Inherits peer configuration from peer-template Standard-Leg
  Description: from donkey to monkey
  BGP version 4, remote router ID 48.151.81.94
  BGP state = Established, up for 1d06h
  Peer is directly attached, interface port-channel132
  TCP MD5 authentication is enabled
  Last read 00:00:03, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 539821 messages, 0 notifications, 0 bytes in queue
  Sent 2040431 messages, 0 notifications, 0 bytes in queue
  Connections established 4, dropped 3
  Last reset by peer 1d06h, due to duplicate connection request
  Last reset by us never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
    IPv4 Unicast
  Forwarding state preserved by peer for:
    IPv4 Unicast
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         4                  4
  Notifications:                 0                  0
  Updates:                 1578342                 79
  Keepalives:               462085             539738
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   2040431             539821
  Total bytes:           200776152           10260440
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  110 accepted paths consume 6600 bytes of memory
  53336 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%
  Last End-of-RIB received 00:04:56 after session start

  Local host: 214.144.36.241, Local port: 55353
  Foreign host: 160.215.146.14, Foreign port: 179
  fd = 105

BGP neighbor is 32.180.174.240,  remote AS 65282, ebgp link,  Peer index 40
  Inherits peer configuration from peer-template Standard-Leg
  Description: from bing to bar
  BGP version 4, remote router ID 0.0.0.0
  BGP state = Idle, down for 13w2d, retry in 0.963836
  Last read never, hold time = 45, keepalive interval is 15 seconds
  Last written never, keepalive timer not running
  Received 0 messages, 0 notifications, 0 bytes in queue
  Sent 0 messages, 0 notifications, 0 bytes in queue
  Connections established 0, dropped 0
  Connection attempts 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Message statistics:
                              Sent               Rcvd
  Opens:                         0                  0
  Notifications:                 0                  0
  Updates:                       0                  0
  Keepalives:                    0                  0
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                         0                  0
  Total bytes:                   0                  0
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 0
  0 accepted paths consume 0 bytes of memory
  0 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%
  Outbound route-map configured is ALLOW_DEFAULT, handle obtained

  No established BGP session with peer

BGP neighbor is 132.226.58.125,  remote AS 64602, ebgp link,  Peer index 41
  Inherits peer configuration from peer-template Standard-Leg
  Description: from donkey to bing
  BGP version 4, remote router ID 190.57.189.2222
  BGP state = Established, up for 10w5d
  Peer is directly attached, interface Ethernet6/8
  TCP MD5 authentication is enabled
  Last read 00:00:11, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 539956 messages, 0 notifications, 0 bytes in queue
  Sent 2010003 messages, 0 notifications, 0 bytes in queue
  Connections established 2, dropped 1
  Last reset by peer 10w5d, due to duplicate connection request
  Last reset by us never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
    IPv4 Unicast
  Forwarding state preserved by peer for:
    IPv4 Unicast
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised received
  Receive IPv6 next hop encoding Capability for AF:
    IPv4 Unicast

  Message statistics:
                              Sent               Rcvd
  Opens:                         2                  2
  Notifications:                 0                  0
  Updates:                 1547924                223
  Keepalives:               462077             539731
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   2010003             539956
  Total bytes:           206256974           10273374
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  55 accepted paths consume 3300 bytes of memory
  53393 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%
  Last End-of-RIB received 00:01:09 after session start

  Local host: 238.32.93.158, Local port: 65116
  Foreign host: 206.89.69.2, Foreign port: 179
  fd = 89

BGP neighbor is 58.87.110.23,  remote AS 65010, ebgp link,  Peer index 42
  Inherits peer configuration from peer-template Standard-Leg
  Description: from frog to boo
  BGP version 4, remote router ID 250.160.61.644
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface port-channel129
  TCP MD5 authentication is enabled
  Last read 00:00:06, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 752748 messages, 0 notifications, 0 bytes in queue
  Sent 1990872 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1527603             226933
  Keepalives:               463268             525814
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1990872             752748
  Total bytes:           194429206           24196536
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  642 accepted paths consume 38520 bytes of memory
  52804 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%

  Local host: 85.4.162.71, Local port: 179
  Foreign host: 112.221.23.57, Foreign port: 37814
  fd = 76

BGP neighbor is 214.53.165.54,  remote AS 64616, ebgp link,  Peer index 43
  Description: from foo to frog
  BGP version 4, remote router ID 230.88.88.615
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface Ethernet5/14
  TCP MD5 authentication is enabled
  Last read 00:00:10, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 539909 messages, 0 notifications, 0 bytes in queue
  Sent 1997579 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
    IPv4 Unicast
  Forwarding state preserved by peer for:
    IPv4 Unicast
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised received
  Receive IPv6 next hop encoding Capability for AF:
    IPv4 Unicast

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1535502                  3
  Keepalives:               462076             539905
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1997579             539909
  Total bytes:           204495240           10258358
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  11 accepted paths consume 660 bytes of memory
  53435 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Last End-of-RIB received 00:00:01 after session start

  Local host: 51.185.196.36, Local port: 179
  Foreign host: 191.20.54.179, Foreign port: 57737
  fd = 63

BGP neighbor is 237.50.68.158,  remote AS 64617, ebgp link,  Peer index 44
  Inherits peer configuration from peer-template Standard-Leg
  Description: from donkey to frog
  BGP version 4, remote router ID 120.212.28.247
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface Ethernet6/14
  TCP MD5 authentication is enabled
  Last read 00:00:09, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 539888 messages, 0 notifications, 0 bytes in queue
  Sent 1995748 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
    IPv4 Unicast
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised received
  Receive IPv6 next hop encoding Capability for AF:
    IPv4 Unicast

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1533672                  2
  Keepalives:               462075             539885
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1995748             539888
  Total bytes:           204283404           10257892
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  1 accepted paths consume 60 bytes of memory
  53445 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%
  Last End-of-RIB received 00:00:01 after session start

  Local host: 89.132.8.29, Local port: 179
  Foreign host: 255.186.167.183, Foreign port: 17650
  fd = 81

BGP neighbor is 30.151.70.12,  remote AS 64610, ebgp link,  Peer index 45
  Inherits peer configuration from peer-template Standard-Leg
  Description: from foo to baz
  BGP version 4, remote router ID 172.17.111.0
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface port-channel130
  TCP MD5 authentication is enabled
  Last read 00:00:12, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 539995 messages, 0 notifications, 0 bytes in queue
  Sent 1995618 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
    IPv4 Unicast
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised received
  Receive IPv6 next hop encoding Capability for AF:
    IPv4 Unicast

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1533539                 18
  Keepalives:               462078             539976
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1995618             539995
  Total bytes:           204266892           10260620
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  26 accepted paths consume 1560 bytes of memory
  53420 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%
  Last End-of-RIB received 02:20:38 after session start

  Local host: 78.199.207.157, Local port: 179
  Foreign host: 222.28.243.82, Foreign port: 16952
  fd = 83

BGP neighbor is 59.112.207.30,  remote AS 64615, ebgp link,  Peer index 46
  Inherits peer configuration from peer-template Standard-Leg
  Description: from monkey to bing
  BGP version 4, remote router ID 109.134.68.284
  BGP state = Established, up for 10w5d
  Peer is directly attached, interface Ethernet5/15
  TCP MD5 authentication is enabled
  Last read 00:00:03, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 539758 messages, 0 notifications, 0 bytes in queue
  Sent 2025821 messages, 0 notifications, 0 bytes in queue
  Connections established 3, dropped 2
  Last reset by peer 10w5d, due to duplicate connection request
  Last reset by us never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
    IPv4 Unicast
  Forwarding state preserved by peer for:
    IPv4 Unicast
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised received
  Receive IPv6 next hop encoding Capability for AF:
    IPv4 Unicast

  Message statistics:
                              Sent               Rcvd
  Opens:                         3                  3
  Notifications:                 0                  0
  Updates:                 1563738                 15
  Keepalives:               462080             539740
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   2025821             539758
  Total bytes:           208408364           10255802
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  4 accepted paths consume 240 bytes of memory
  53442 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%
  Last End-of-RIB received 00:00:08 after session start

  Local host: 221.66.123.172, Local port: 64966
  Foreign host: 127.176.93.177, Foreign port: 179
  fd = 67

BGP neighbor is 185.174.44.36,  remote AS 64613, ebgp link,  Peer index 47
  Inherits peer configuration from peer-template OOB
  Description: from monkey to bing
  BGP version 4, remote router ID 229.223.33.1724
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface Ethernet6/15
  TCP MD5 authentication is enabled
  Last read 00:00:10, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 578136 messages, 0 notifications, 0 bytes in queue
  Sent 1995615 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr)
  Dynamic capability (old): advertised
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
    IPv4 Unicast
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1533546                  7
  Keepalives:               462068             578128
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1995615             578136
  Total bytes:           194880652           10984839
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  5 accepted paths consume 300 bytes of memory
  53441 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Last End-of-RIB received 0.223700 after session start

  Local host: 209.213.88.120, Local port: 27191
  Foreign host: 166.18.170.15, Foreign port: 179
  fd = 95

BGP neighbor is 73.80.95.69,  remote AS 64623, ebgp link,  Peer index 48
  Inherits peer configuration from peer-template Standard-Leg
  Description: from boo to donkey
  BGP version 4, remote router ID 108.240.226.2090
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface Ethernet5/10
  TCP MD5 authentication is enabled
  Last read 00:00:01, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 539932 messages, 0 notifications, 0 bytes in queue
  Sent 1996998 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
    IPv4 Unicast
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised received
  Receive IPv6 next hop encoding Capability for AF:
    IPv4 Unicast

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1534921                  2
  Keepalives:               462076             539929
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1996998             539932
  Total bytes:           204431633           10258728
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  1 accepted paths consume 60 bytes of memory
  53445 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Maximum prefixes allowed 10000
  Threshold for warning messages 75%
  Last End-of-RIB received 00:00:01 after session start

  Local host: 151.112.219.37, Local port: 179
  Foreign host: 87.38.121.111, Foreign port: 40066
  fd = 61

BGP neighbor is 238.139.143.60,  remote AS 65002, ebgp link,  Peer index 16
  Description: from frog to monkey
  BGP version 4, remote router ID 118.97.21.1872
  BGP state = Established, up for 12w6d
  Peer is directly attached, interface Ethernet6/2
  TCP MD5 authentication is enabled
  Last read 00:00:05, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1465362 messages, 0 notifications, 0 bytes in queue
  Sent 1391904 messages, 0 notifications, 0 bytes in queue
  Connections established 2, dropped 1
  Last reset by us 12w6d, due to other configuration change
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
    IPv4 Unicast
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised received
  Receive IPv6 next hop encoding Capability for AF:
    IPv4 Unicast

  Message statistics:
                              Sent               Rcvd
  Opens:                         2                  2
  Notifications:                 0                  0
  Updates:                  913861            1000017
  Keepalives:               478041             465343
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1391904            1465362
  Total bytes:           113569741          122214139
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  51100 accepted paths consume 3066000 bytes of memory
  46640 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Last End-of-RIB received 00:01:21 after session start

  Local host: 246.236.13.106, Local port: 34610
  Foreign host: 129.148.50.189, Foreign port: 179
  fd = 92

BGP neighbor is 14.39.170.172,  remote AS 65002, ebgp link,  Peer index 17
  Description: from bing to monkey
  BGP version 4, remote router ID 174.189.3.1302
  BGP state = Established, up for 11w4d
  Peer is directly attached, interface Ethernet6/3
  TCP MD5 authentication is enabled
  Last read 00:00:05, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1570618 messages, 0 notifications, 0 bytes in queue
  Sent 1432408 messages, 0 notifications, 0 bytes in queue
  Connections established 7, dropped 6
  Last reset by peer 11w4d, due to duplicate connection request
  Last reset by us 11w5d, due to other configuration change

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
    IPv4 Unicast
  Forwarding state preserved by peer for:
    IPv4 Unicast
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised received
  Receive IPv6 next hop encoding Capability for AF:
    IPv4 Unicast

  Message statistics:
                              Sent               Rcvd
  Opens:                         7                  7
  Notifications:                 0                  0
  Updates:                  955014            1108031
  Keepalives:               477387             462580
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1432408            1570618
  Total bytes:           117957629          140481425
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  51100 accepted paths consume 3066000 bytes of memory
  46640 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  1 paths flushed from peer
  Last End-of-RIB received 00:01:36 after session start

  Local host: 247.176.130.61, Local port: 53574
  Foreign host: 180.138.38.81, Foreign port: 179
  fd = 72

BGP neighbor is 171.175.146.126,  remote AS 65001, ibgp link,  Peer index 18
  Description: from donkey to bing
  BGP version 4, remote router ID 89.143.28.662
  BGP state = Established, up for 11w5d
  Peer is directly attached, interface Ethernet6/1
  TCP MD5 authentication is enabled
  Last read 00:00:05, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1797442 messages, 0 notifications, 0 bytes in queue
  Sent 1795086 messages, 6 notifications, 0 bytes in queue
  Connections established 9, dropped 8
  Last reset by us 11w5d, due to holdtimer expired error
  Last reset by peer 11w5d, due to duplicate connection request

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
    IPv4 Unicast
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised received
  Receive IPv6 next hop encoding Capability for AF:
    IPv4 Unicast

  Message statistics:
                              Sent               Rcvd
  Opens:                         9                  9
  Notifications:                 6                  0
  Updates:                 1321374            1334218
  Keepalives:               473697             463215
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1795086            1797442
  Total bytes:           165732259          169019249
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  52809 accepted paths consume 3168540 bytes of memory
  53204 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Nexthop always set to local peering address, 68.18.216.1745
  Third-party Nexthop will not be computed.
  Last End-of-RIB received 00:01:15 after session start

  Local host: 183.124.152.216, Local port: 179
  Foreign host: 188.93.115.206, Foreign port: 3413
  fd = 80

BGP neighbor is 254.145.7.45,  remote AS 65261, ebgp link,  Peer index 19
  Description: from bing to bar
  BGP version 4, remote router ID 66.94.166.244
  BGP state = Established, up for 13w2d
  Peer is directly attached, interface Ethernet5/8
  TCP MD5 authentication is enabled
  Last read 00:00:05, hold time = 45, keepalive interval is 15 seconds
  Last written 00:00:05, keepalive timer expiry due 00:00:09
  Received 1540339 messages, 0 notifications, 0 bytes in queue
  Sent 1968468 messages, 0 notifications, 0 bytes in queue
  Connections established 1, dropped 0
  Last reset by us never, due to No error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
    IPv4 Unicast
  Forwarding state preserved by peer for:
    IPv4 Unicast
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  1
  Notifications:                 0                  0
  Updates:                 1506061            1067023
  Keepalives:               462406             473315
  Route Refresh:                 0                  0
  Capability:                    0                  0
  Total:                   1968468            1540339
  Total bytes:           191796776          133449716
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 8483941, neighbor version 8483941
  12901 accepted paths consume 774060 bytes of memory
  52922 sent paths
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Last End-of-RIB received 00:00:02 after session start

  Local host: 31.67.203.133, Local port: 179
  Foreign host: 255.45.69.45, Foreign port: 25122
  fd = 60
BGP neighbor is 255.136.173.131,  remote AS 65272, ibgp link,  Peer index 3
  BGP version 4, remote router ID 41.65.243.1412
  BGP state = Established, up for 3w5d
  Using loopback0 as update source for this peer
  Last read 00:00:39, hold time = 180, keepalive interval is 60 seconds
  Last written 00:00:09, keepalive timer expiry due 00:00:50
  Received 57117 messages, 0 notifications, 0 bytes in queue
  Sent 42287 messages, 2 notifications, 0 bytes in queue
  Connections established 3, dropped 2
  Last reset by us 3w5d, due to holdtimer expired error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Address family IPv6 Unicast: advertised received
  Address family L2VPN EVPN: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast  IPv6 Unicast  L2VPN EVPN
  Address families received from peer:
    IPv4 Unicast  IPv6 Unicast  L2VPN EVPN
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised received
  Receive IPv6 next hop encoding Capability for AF:
    IPv4 Unicast

  Message statistics:
                              Sent               Rcvd
  Opens:                         3                  3
  Notifications:                 2                  0
  Updates:                    4200              21260
  Keepalives:                38070              35845
  Route Refresh:                 3                  0
  Capability:                    9                  9
  Total:                     42287              57117
  Total bytes:             1212655            3818154
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 227160, neighbor version 227160
  31 accepted paths consume 3968 bytes of memory
  7 sent paths
  Third-party Nexthop will not be computed.
  Last End-of-RIB received 00:00:47 after session start

  For address family: IPv6 Unicast
  BGP table version 4, neighbor version 4
  0 accepted paths consume 0 bytes of memory
  0 sent paths
  Third-party Nexthop will not be computed.
  Last End-of-RIB received 00:00:01 after session start

  For address family: L2VPN EVPN
  BGP table version 139600, neighbor version 139600
  2159 accepted paths consume 276352 bytes of memory
  601 sent paths
  Community attribute sent to this neighbor
  Extended community attribute sent to this neighbor
  Third-party Nexthop will not be computed.
  Last End-of-RIB received 3w0d after session start

  Local host: 187.113.144.52, Local port: 42267
  Foreign host: 87.39.86.252, Foreign port: 179
  fd = 91
BGP neighbor is 13.187.14.99,  remote AS 65273.435, local AS 4355, ebgp link,  Peer index 3
  Inherits peer configuration from peer-template Standard-Leg
  BGP version 4, remote router ID 88.23.55.122
  BGP state = Established, up for 7w1d
  Using loopback0 as update source for this peer
  Last read 00:00:19, hold time = 180, keepalive interval is 60 seconds
  Last written 00:00:02, keepalive timer expiry due 00:00:20
  Received 41213 messages, 0 notifications, 0 bytes in queue
  Sent 33285 messages, 2 notifications, 0 bytes in queue
  Connections established 3, dropped 2
  Last reset by us 7w1d, due to holdtimer expired error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Address family IPv6 Unicast: advertised received
  Address family L2VPN EVPN: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast  IPv6 Unicast  L2VPN EVPN
  Address families received from peer:
    IPv4 Unicast  IPv6 Unicast  L2VPN EVPN
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised received
  Receive IPv6 next hop encoding Capability for AF:
    IPv4 Unicast

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  6
  Notifications:                 2                  0
  Updates:                    1200                230
  Keepalives:                28020              45845
  Route Refresh:                 3                  0
  Capability:                    9                  9
  Total:                     62481              25117
  Total bytes:             1212221              38154
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 220, neighbor version 227
  31 accepted paths consume 3968 bytes of memory
  7 sent paths
  Third-party Nexthop will not be computed.
  Last End-of-RIB received 00:00:19 after session start

  For address family: IPv6 Unicast
  BGP table version 4, neighbor version 4
  0 accepted paths consume 0 bytes of memory
  0 sent paths
  Third-party Nexthop will not be computed.
  Last End-of-RIB received 00:00:01 after session start

  For address family: L2VPN EVPN
  BGP table version 1496, neighbor version 1496
  21 accepted paths consume 2763 bytes of memory
  61 sent paths
  Community attribute sent to this neighbor
  Extended community attribute sent to this neighbor
  Third-party Nexthop will not be computed.
  Last End-of-RIB received 3w0d after session start

  Local host: 12.22.65.52, Local port: 42267
  Foreign host: 83.26.83.25, Foreign port: 179
  fd = 91
BGP neighbor is 19.13.1.12,  remote AS 65273.3334, local AS 2202, ebgp link,  Peer index 3
  Inherits peer configuration from peer-template Standard-Leg
  Description: TEST
  BGP version 4, remote router ID 11.22.33.44
  BGP state = Established, up for 71w2d
  Neighbor vrf: CLOUD
  Using loopback0 as update source for this peer
  Last read 00:00:19, hold time = 180, keepalive interval is 60 seconds
  Last written 00:00:02, keepalive timer expiry due 00:00:20
  Received 33431221 messages, 0 notifications, 0 bytes in queue
  Sent 33285112 messages, 2 notifications, 0 bytes in queue
  Connections established 3, dropped 2
  Last reset by us 71w2d, due to holdtimer expired error
  Last reset by peer never, due to No error

  Neighbor capabilities:
  Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
  Dynamic capability (old): advertised received
  Route refresh capability (new): advertised received
  Route refresh capability (old): advertised received
  4-Byte AS capability: advertised received
  Address family IPv4 Unicast: advertised received
  Address family IPv6 Unicast: advertised received
  Address family L2VPN EVPN: advertised received
  Graceful Restart capability: advertised received

  Graceful Restart Parameters:
  Address families advertised to peer:
    IPv4 Unicast
  Address families received from peer:
    IPv4 Unicast
  Forwarding state preserved by peer for:
  Restart time advertised to peer: 120 seconds
  Stale time for routes advertised by peer: 300 seconds
  Restart time advertised by peer: 120 seconds
  Extended Next Hop Encoding Capability: advertised received
  Receive IPv6 next hop encoding Capability for AF:
    IPv4 Unicast

  Message statistics:
                              Sent               Rcvd
  Opens:                         1                  6
  Notifications:                 2                  0
  Updates:                  120032               3333
  Keepalives:               342020             111845
  Route Refresh:                 3                  0
  Capability:                    9                  9
  Total:                     62481              25117
  Total bytes:             1212221              38154
  Bytes in queue:                0                  0

  For address family: IPv4 Unicast
  BGP table version 220, neighbor version 227
  31 accepted paths consume 3968 bytes of memory
  7 sent paths
  Third-party Nexthop will not be computed.
  Last End-of-RIB received 00:00:19 after session start

  Local host: 23.55.61.2, Local port: 42267
  Foreign host: 86.11.82.26, Foreign port: 179
  fd = 91

```

**Help:** execute the command "show ip bgp neighbors"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip bgp summary

**Output:**
```
BGP summary information for VRF default, address family IPv4 Multicast
 BGP router identifier 2.2.2.3, local AS number 102
BGP table version is 5, IPv4 Multicast config peers 2, capable peers 0
1 network entries and 1 paths using 104 bytes of memory
BGP attribute entries [1/124], BGP AS path entries [0/0]
BGP community entries [0/0], BGP clusterlist entries [0/0]
Neighbor V AS MsgRcvd MsgSent TblVer InQ OutQ Up/Down State/PfxRcd
10.0.0.100 4 64497 0 0 0 0 0 03:20:10 Idle
192.168.1.3 4 0 0 0 0 0 0 01:51:38 Idle
10.0.0.1        4        65000 2746767 2396274 512185206    0    0 3w0d       558720
10.0.0.2        4        65001 2855873 2409742 512185206    0    0 3w0d       558720
10.0.0.3        4        65002  695143  689871 512185203    0    0 1y10w           0
10.0.0.4        4        65003 1030294 1220041 512185206    0    0 1y50w        1351
10.0.0.5        4        65004 26552304 14931352 512185206    0    0 19w5d      558720
10.0.0.6        4        65005 26532908 14931123 512185206    0    0 19w5d      558720
10.0.0.7        4        65006 12245684 9181569 512185203    0    0 1y10w          82
10.0.0.8        4        65007 12250936 9181571 512185203    0    0 1y10w          82
10.0.0.9        4        65008  222146 14368489 512185203    0    0 22w0d           0
10.0.0.10       4        65009 26930508  942614 512185203    0    0 1y10w     Idle (Admin)
10.0.0.11       4        65010
                               2655204 14931352 512185206   0    0 1w5d      4452

```

**Help:** execute the command "show ip bgp summary"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show configuration session summary

**Output:**
```
Session Manager Database:
--------------------------------------------------------------------
Name                    Session Owner           Creation Time
--------------------------------------------------------------------
ACL-SESSION1            ntc                     02:37:14 UTC Oct 28 2017
ACL-SESS22              ntc                     02:37:55 UTC Oct 28 2017

Number of active configuration sessions = 2


```

**Help:** execute the command "show configuration session summary"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show flogi database

**Output:**
```
SWITCH1# sh flogi database
--------------------------------------------------------------------------------
INTERFACE        VSAN    FCID           PORT NAME               NODE NAME
--------------------------------------------------------------------------------
fc1/33           10    0x000000  aa:bb:cc:dd:ee:ff:00:11 aa:bb:cc:dd:ee:ff:00:00
                           [SAN_PORT_1]
fc1/34           10    0x000000  aa:bb:cc:dd:ee:ff:00:12 aa:bb:cc:dd:ee:ff:00:00
                           [SAN_PORT_2]
fc1/35           10    0x000000  aa:bb:cc:dd:ee:ff:00:13 aa:bb:cc:dd:ee:ff:00:00
                           [SAN_PORT_3]
fc1/36           10    0x000000  aa:bb:cc:dd:ee:ff:00:14 aa:bb:cc:dd:ee:ff:00:00
                           [SAN_PORT_4]
fc1/37           10    0x000000  aa:bb:cc:dd:ee:ff:00:15 bb:bb:cc:dd:ee:ff:00:00
                           [TAPE_1]
fc1/38           10    0x000000  aa:bb:cc:dd:ee:ff:00:16 a0:bb:cc:dd:ee:ff:00:00
                           [TAPE_2]
fc1/41           10    0x000000  aa:bb:cc:dd:ee:ff:00:17 d1:bb:cc:dd:ee:ff:00:00
                           [SERVER_A_PORT_1]
fc1/42           10    0x000000  aa:bb:cc:dd:ee:ff:00:18 d1:bb:cc:dd:ee:ff:00:00
                           [SERVER_A_PORT_2]
fc1/43           10    0x000000  aa:bb:cc:dd:ee:ff:00:19 3a:bb:cc:dd:ee:ff:00:00
                           [SERVER_B_PORT_1]
fc1/44           10    0x000000  aa:bb:cc:dd:ee:ff:00:10 3a:bb:cc:dd:ee:ff:00:00
                           [SERVER_B_PORT_2]
fc1/45           10    0x000000  aa:bb:cc:dd:ee:ff:01:10 da:bb:cc:dd:ee:ff:00:00
fc1/45           10    0x000000  aa:bb:cc:dd:ee:ff:01:11 da:bb:cc:dd:ee:ff:00:01
                           [SERVER_C_PORT_1]
fc1/45           10    0x000000  aa:bb:cc:dd:ee:ff:01:12 da:bb:cc:dd:ee:ff:00:a0
                           [SERVER_D_PORT_1]
fc1/45           10    0x000000  aa:bb:cc:dd:ee:ff:01:13 da:bb:cc:dd:ee:ff:00:f3
                           [SERVER_E_PORT_1]
fc1/45           10    0x000000  aa:bb:cc:dd:ee:ff:01:14 da:bb:cc:dd:ee:ff:00:d7
                           [SERVER_F_PORT_1]
fc1/45           10    0x000000  aa:bb:cc:dd:ee:ff:01:15 da:bb:cc:dd:ee:ff:00:a8
                           [SERVER_G_PORT_1]
fc1/45           10    0x000000  aa:bb:cc:dd:ee:ff:01:16 da:bb:cc:dd:ee:ff:00:c3
                           [SERVER_H_PORT_1]
fc1/45           10    0x000000  aa:bb:cc:dd:ee:ff:01:17 da:bb:cc:dd:ee:ff:00:c8
                           [SERVER_I_PORT_1]
fc1/45           10    0x000000  aa:bb:cc:dd:ee:ff:01:18 da:bb:cc:dd:ee:ff:00:e9
                           [SERVER_J_PORT_1]
fc1/45           10    0x000000  aa:bb:cc:dd:ee:ff:01:19 da:bb:cc:dd:ee:ff:00:e1
                           [SERVER_K_PORT_1]
fc1/46           10    0x000000  aa:bb:cc:dd:ee:ff:02:00 c6:bb:cc:dd:ee:ff:00:11
                           [DEV_SERVER_PORT_1]

 Total number of flogi = 21.

```

**Help:** execute the command "show flogi database"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip community-list

**Output:**
```
Expanded Community List ROUTES_CL1
    1 permit "11111:10000"
Standard Community List ROUTES_CL2
    1 permit 11111:10000
    2 permit 22222:10000
    3 permit 33333:10000
    4 permit 44444:10000 55555:10005 no-export
    5 deny internet

```

**Help:** execute the command "show ip community-list"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show nve vni

**Output:**
```
Codes: CP - Control Plane        DP - Data Plane         
       UC - Unconfigured         SA - Suppress ARP       
       SU - Suppress Unknown Unicast
       Xconn - Crossconnect     
       MS-IR - Multisite Ingress Replication
Interface VNI      Multicast-group   State Mode Type [BD/VRF]      Flags
--------- -------- ----------------- ----- ---- ------------------ -----
nve1      1006    UnicastBGP          Up    CP   L2 [6]             SA   
nve1      1105    UnicastBGP          Up    CP   L2 [1105]          SA  
nve1      2111    UnicastBGP          Up    CP   L2 [111]           SA  
nve1      3098    UnicastBGP          Up    CP   L2 [98]            SA  
nve1      10301 n/a                   Up    CP   L3 [BLU]               
nve1      10302 n/a                   Up    CP   L3 [GRN]               
nve1      10303 n/a                   Up    CP   L3 [AMB]                              
nve1      10306 n/a                   Up    CP   L3 [GRY]               

```

**Help:** execute the command "show nve vni"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip arp detail

**Output:**
```
Flags: * - Adjacencies learnt on non-active FHRP router
       + - Adjacencies synced via CFSoE
       # - Adjacencies Throttled for Glean

IP ARP Table for context default
Total number of entries: 1
Address         Age       MAC Address     Interface        Physical Interface
192.168.56.2    00:17:02  5087.89a1.d8d5  Ethernet1/2      Ethernet1/2
90.10.10.2      00:02:55  000d.ece7.df7c  Vlan900          Ethernet1/12
90.10.10.4      -         000d.ece7.df7d  -                -


```

**Help:** execute the command "show ip arp detail"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### dir

**Output:**
```
Input/output error
       4096    Sep 22 15:27:34 2019  .rpmstore/
       4096    Sep 22 15:27:53 2019  .swtam/
       1982    Sep 22 15:29:22 2019  20190922_052903_poap_7826_init.log
     189080    Sep 22 15:18:11 2019  CpuUsage.Log
 1410981963    Jul 13 10:05:48 2018  aci-n9000-dk9.13.1.2p.bin
 1157861451    Sep 22 15:15:57 2019  auto-s
          0    Sep 22 15:16:00 2019  bios_bootup_scratch_not_cleared
          0    Sep 22 15:27:47 2019  bootflash_sync_list
         53    Sep 22 15:10:02 2019  disk_log.txt
         18    Dec 12 22:32:13 2022  gold_file
        462    Sep 22 15:18:02 2019  libmon.logs
       4096    Sep 22 15:02:17 2019  lost+found/
```

**Help:** execute the command "dir"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip interface vrf all

**Output:**
```
IP Interface Status for VRF "default"
loopback0, Interface status: protocol-up/link-up/admin-up, iod: 50,
Unnumbered interfaces of loopback0: first iod 69
mti19: mti6: mti10: mti4: mti14: mti13: mti7: mti3: mti20: mti17: mti15: mti16: mti18: mti8: mti12: mti11: mti9: 
  IP address: 172.21.128.112, IP subnet: 172.21.128.112/32 route-preference: 0, tag: 0 
  IP broadcast address: 255.255.255.255
  IP multicast groups locally joined: 
      224.0.0.22  224.0.0.2  224.0.0.1  224.0.0.13  
  IP MTU: 1500 bytes (using link MTU)
  IP primary address route-preference: 0, tag: 0
  IP proxy ARP : disabled
  IP Local Proxy ARP : disabled
  IP multicast routing: enabled
  IP icmp redirects: enabled
  IP directed-broadcast: disabled 
  IP Forwarding: disabled 
  IP icmp unreachables (except port): disabled
  IP icmp port-unreachable: enabled
  IP unicast reverse path forwarding: none
  IP load sharing: none 
  IP interface statistics last reset: never
  IP interface software stats: (sent/received/forwarded/originated/consumed)
    Unicast packets    : 0/0/0/2/319819115
    Unicast bytes      : 0/0/0/336/69375531170
    Multicast packets  : 0/0/0/0/0
    Multicast bytes    : 0/0/0/0/0
    Broadcast packets  : 0/0/0/0/0
    Broadcast bytes    : 0/0/0/0/0
    Labeled packets    : 0/0/0/0/0
    Labeled bytes      : 0/0/0/0/0
  WCCP Redirect outbound: disabled
  WCCP Redirect inbound: disabled
  WCCP Redirect exclude: disabled
Vlan3050, Interface status: protocol-up/link-up/admin-up, iod: 11,
  IP address: 10.135.128.2, IP subnet: 10.135.128.0/23 route-preference: 0, tag: 0
  IP address: 10.135.136.2, IP subnet: 10.135.136.0/23 secondary route-preference: 0, tag: 0
  IP broadcast address: 255.255.255.255
  IP multicast groups locally joined:
      224.0.0.102
  IP MTU: 9100 bytes (using link MTU)
  IP primary address route-preference: 0, tag: 0
  IP proxy ARP : disabled
  IP Local Proxy ARP : disabled
  IP multicast routing: disabled
  IP icmp redirects: disabled
  IP directed-broadcast: disabled
  IP Forwarding: disabled
  IP icmp unreachables (except port): disabled
  IP icmp port-unreachable: enabled
  IP unicast reverse path forwarding: none
  IP load sharing: none
  IP interface statistics last reset: never
  IP interface software stats: (sent/received/forwarded/originated/consumed)
    Unicast packets    : 423354/1246554/6/866674/2936084
    Unicast bytes      : 31332247/100739265/564/74949788/237074996
    Multicast packets  : 0/49794479/0/0/17107296
    Multicast bytes    : 0/9247224241/0/0/855364800
    Broadcast packets  : 0/0/0/0/0
    Broadcast bytes    : 0/0/0/0/0
    Labeled packets    : 0/0/0/0/0
    Labeled bytes      : 0/0/0/0/0
  WCCP Redirect outbound: disabled
  WCCP Redirect inbound: disabled
  WCCP Redirect exclude: disabled

IP Interface Status for VRF "MGMT"
mti3, Interface status: protocol-up/link-up/admin-up, iod: 62,
  IP unnumbered interface (loopback0)
  IP broadcast address: 255.255.255.255
  IP multicast groups locally joined:
      224.0.0.13  224.0.0.2  224.0.0.1
  IP MTU: 1500 bytes (using link MTU)
  IP proxy ARP : disabled
  IP Local Proxy ARP : disabled
  IP multicast routing: enabled
  IP icmp redirects: enabled
  IP directed-broadcast: disabled
  IP Forwarding: disabled
  IP icmp unreachables (except port): disabled
  IP icmp port-unreachable: enabled
  IP unicast reverse path forwarding: none
  IP load sharing: none
  IP outbound access list: LD
  IP interface statistics last reset: never
  IP interface software stats: (sent/received/forwarded/originated/consumed)
    Unicast packets    : 0/0/0/0/0
    Unicast bytes      : 0/0/0/0/0
    Multicast packets  : 0/1517585632/0/0/3028204944
    Multicast bytes    : 0/88397434730/0/0/88397450856
    Broadcast packets  : 0/0/0/0/0
    Broadcast bytes    : 0/0/0/0/0
    Labeled packets    : 0/0/0/0/0
    Labeled bytes      : 0/0/0/0/0
  WCCP Redirect outbound: disabled
  WCCP Redirect inbound: disabled
  WCCP Redirect exclude: disabled

```

**Help:** execute the command "show ip interface vrf all"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show cdp neighbors

**Output:**
```
Capability Codes: R - Router, T - Trans-Bridge, B - Source-Route-Bridge
                 S - Switch, H - Host, I - IGMP, r - Repeater,
                 V - VoIP-Phone, D - Remotely-Managed-Device,
                 s - Supports-STP-Dispute


Device-ID             Local Intrfce Hldtme Capability  Platform         Port ID
my-dc1-mgt-sw1(FOC213230KP)
                   mgmt0          138    R S I s   N3K-C3172PQ-XL     Eth1/48       
lx-dc1-server01.mynetwork.com
                   Eth1/1/1       109    H         Linux              eth9          
lx-dc1-server02.mynetwork.com
                   Eth1/1/2       106    H         Linux              eth9          
lx-dc1-server03.mynetwork.com
                   Eth1/1/3       91     H         Linux              eth9          
lx-dc1-server04.mynetwork.com
                   Eth1/1/4       112    H         Linux              eth9          
lx-dc1-server05.mynetwork.com
                   Eth1/2/1       100    H         Linux              eth9

```

**Help:** execute the command "show cdp neighbors"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip route

**Output:**
```
IP Route Table for VRF "default"
'*' denotes best ucast next-hop
'**' denotes best mcast next-hop
'[x/y]' denotes [preference/metric]
'%<string>' in via output denotes VRF <string>

10.138.224.32/28, ubest/mbest: 1/0 time
    *via 222.111.19.38, [1/0], 1w0d, static
     via 172.16.2.37, Vlan22, [110/21], 3w1d, ospf-UNDERLAY, type-1
152.98.240.64/27, ubest/mbest: 1/0 time
    *via 111.222.236.188, [1/0], 8w4d, static
     via 172.16.2.37, Vlan22, [110/21], 3w1d, ospf-UNDERLAY, type-1

IP Route Table for VRF "management"
'*' denotes best ucast next-hop
'**' denotes best mcast next-hop
'[x/y]' denotes [preference/metric]
'%<string>' in via output denotes VRF <string>
 
0.0.0.0/0, ubest/mbest: 1/0 time
    *via 172.16.170.193, [1/0], 1y16w, static

```

**Help:** execute the command "show ip route"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip ospf interface brief

**Output:**
```
 OSPF Process ID BLU1 VRF BLU
 Total number of interface: 1
 Interface               ID     Area            Cost   State    Neighbors Status
 Vlan10                  1      0.0.0.10        10     DR       2         up 
 
 OSPF Process ID DC_UNDERLAY VRF default
 Total number of interface: 6
 Interface               ID     Area            Cost   State    Neighbors Status
 Vlan2                   3      0.0.0.0         100    P2P      1         up 
 Lo1                     1      0.0.0.0         1      LOOPBACK 0         up 
 Lo2                     2      0.0.0.0         1      LOOPBACK 0         up 
 Lo3                     4      0.0.0.0         1      LOOPBACK 0         up 
 Eth1/1                  6      0.0.0.0         1      P2P      1         up 
 Eth1/2                  5      0.0.0.0         1      P2P      1         up 

```

**Help:** execute the command "show ip ospf interface brief"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip msdp summary vrf all

**Output:**
```
MSDP Peer Status Summary for VRF "default"
Local ASN: 64520, originator-id: 10.10.100.10

Number of configured peers:  3
Number of established peers: 3
Number of shutdown peers:    0

Peer            Peer        Connection      Uptime/   Last msg  (S,G)s
Address         ASN         State           Downtime  Received  Received
10.1.2.3        64513       Established     1w4d      0.487184  4195
10.1.2.4        64513       Established     1w4d      0.485689  3763
10.1.2.5        64517       Established     1w4d      0.487786  0

```

**Help:** execute the command "show ip msdp summary vrf all"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip pim neighbor vrf all

**Output:**
```
                                    ^
% Invalid command at '^' marker.

```

**Help:** execute the command "show ip pim neighbor vrf all"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show processes cpu

**Output:**
```
CPU utilization for five seconds: 15%/1%; one minute: 12%; five minutes: 10%
PID    Runtime(ms)  Invoked   uSecs  5Sec    1Min    5Min    TTY  Process
-----  -----------  --------  -----  ------  ------  ------  ---  -----------
    1         6170      1011      6   0.00%   0.00%  0.00%   -    init
 2828           20         6      3   0.00%   0.00%  0.00%   -    portmap
 2866           20         8      2   0.00%   0.00%  0.00%   -    rpc.statd
 2876         3490     12448      0   0.92%   0.34%  0.10%   -    sysmgr
 3383           80         6     13   0.00%   0.00%  0.00%   -    xinetd
 3384           40         5      8   0.00%   0.00%  0.00%   -    tftpd
 3385         1650      6566      0   0.00%   0.01%  0.01%   -    syslogd
 3386          450        51      8   0.00%   0.00%  0.00%   -    sdwrapd
 3387          650        92      7   0.00%   0.00%  0.00%   -    pfm_dummy
 3388         2920      4747      0   0.00%   0.03%  0.03%   -    platform
 3400          150       731      0   0.00%   0.00%  0.00%   -    klogd
 3403          560       863      0   0.00%   0.00%  0.00%   -    vshd
 3404          670      1698      0   0.00%   0.00%  0.00%   -    vpc_config_sync
 3405          270      2214      0   0.00%   0.00%  0.00%   -    smm
 3406          620      1399      0   0.00%   0.00%  0.00%   -    session-mgr
 3407          730      4464      0   0.00%   0.00%  0.00%   -    psshelper
 3408          820      1531      0   0.00%   0.00%  0.00%   -    pixm
 3410          580     19429      0   0.00%   0.03%  0.03%   -    pdsd
```

**Help:** execute the command "show processes cpu"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show forwarding ipv4 route

**Output:**
```
IPv4 routes for table default/base

------------------+------------------+----------------------+-----------------
Prefix            | Next-hop         | Interface            | Labels
------------------+------------------+----------------------+-----------------
0.0.0.0/32           Drop               Null0
127.0.0.0/8          Drop               Null0
255.255.255.255/32   Receive            sup-eth1
0.0.0.0/0            10.100.100.178     Ethernet1/8
                     10.100.100.186     Ethernet1/9
10.0.0.0/16          10.100.100.230     Ethernet1/14
10.0.120.0/24        10.100.100.230     Ethernet1/14
10.0.210.0/24        10.100.100.230     Ethernet1/14
10.0.251.0/24        10.100.100.230     Ethernet1/14
10.1.0.0/16          10.100.100.230     Ethernet1/14
10.2.0.0/16          10.100.100.230     Ethernet1/14
10.5.0.0/16          10.100.100.230     Ethernet1/14
10.6.0.0/16          10.100.100.230     Ethernet1/14
10.7.0.0/16          10.100.100.230     Ethernet1/14
10.8.0.0/16          10.100.100.230     Ethernet1/14
10.12.0.0/16         10.100.100.230     Ethernet1/14
10.13.0.0/16         10.100.100.230     Ethernet1/14
10.14.0.0/16         10.100.100.230     Ethernet1/14
10.27.0.0/16         10.100.100.230     Ethernet1/14
10.29.0.0/16         10.100.100.230     Ethernet1/14
10.30.0.0/16         10.100.100.230     Ethernet1/14
10.31.0.0/16         10.100.100.230     Ethernet1/14
10.32.0.0/16         10.100.100.230     Ethernet1/14
10.33.0.0/16         10.100.100.230     Ethernet1/14
10.34.0.0/16         10.100.100.230     Ethernet1/14
10.36.0.0/16         10.100.100.230     Ethernet1/14
10.38.0.0/16         10.100.100.230     Ethernet1/14
10.39.0.0/16         10.100.100.230     Ethernet1/14
10.40.0.0/16         10.100.100.230     Ethernet1/14
10.42.0.0/16         10.100.100.230     Ethernet1/14
10.43.0.0/16         10.100.100.230     Ethernet1/14
10.44.0.0/16         10.100.100.230     Ethernet1/14
10.46.0.0/16         10.100.100.230     Ethernet1/14
10.48.0.0/16         10.100.100.230     Ethernet1/14
10.49.0.0/16         10.100.100.230     Ethernet1/14
10.50.0.0/16         10.100.100.230     Ethernet1/14
10.51.0.0/16         10.100.100.230     Ethernet1/14
10.52.0.0/16         10.100.100.230     Ethernet1/14
10.53.0.0/16         10.100.100.230     Ethernet1/14
10.54.0.0/16         10.100.100.230     Ethernet1/14
10.55.0.0/16         10.100.100.230     Ethernet1/14
10.57.0.0/16         10.100.100.230     Ethernet1/14
10.62.0.0/16         10.100.100.230     Ethernet1/14
10.63.0.0/16         10.100.100.230     Ethernet1/14
10.64.0.0/16         10.100.100.230     Ethernet1/14
10.66.0.0/16         10.100.100.230     Ethernet1/14
10.67.0.0/16         10.100.100.230     Ethernet1/14
10.69.192.0/19       10.100.100.230     Ethernet1/14
10.69.224.0/19       10.100.100.230     Ethernet1/14
10.70.0.0/16         10.100.100.230     Ethernet1/14
10.70.0.0/24         10.100.100.230     Ethernet1/14
10.70.7.0/24         10.100.100.230     Ethernet1/14
10.70.8.0/24         10.100.100.230     Ethernet1/14
10.70.12.0/24        10.100.100.230     Ethernet1/14
10.70.14.0/24        10.100.100.230     Ethernet1/14
10.70.27.0/24        10.100.100.230     Ethernet1/14
10.70.29.0/24        10.100.100.230     Ethernet1/14
10.70.30.0/24        10.100.100.230     Ethernet1/14
10.70.32.0/24        10.100.100.230     Ethernet1/14
10.70.34.0/24        10.100.100.230     Ethernet1/14
10.70.38.0/24        10.100.100.230     Ethernet1/14
10.70.40.0/24        10.100.100.230     Ethernet1/14
10.70.42.0/24        10.100.100.230     Ethernet1/14
10.70.43.0/24        10.100.100.230     Ethernet1/14
10.70.44.0/24        10.100.100.230     Ethernet1/14
10.70.46.0/24        10.100.100.230     Ethernet1/14
10.70.48.0/24        10.100.100.230     Ethernet1/14
10.70.49.0/24        10.100.100.230     Ethernet1/14
10.70.50.0/24        10.100.100.230     Ethernet1/14
10.70.51.0/24        10.100.100.230     Ethernet1/14
10.70.52.0/24        10.100.100.230     Ethernet1/14
10.70.64.0/24        10.100.100.230     Ethernet1/14
10.70.66.0/24        10.100.100.230     Ethernet1/14
10.70.67.0/24        10.100.100.230     Ethernet1/14
10.70.112.0/24       10.100.100.230     Ethernet1/14
10.71.0.0/16         10.100.100.230     Ethernet1/14
10.72.150.0/24       10.100.100.230     Ethernet1/14
10.72.151.0/24       10.100.100.230     Ethernet1/14
10.73.0.0/16         10.100.100.230     Ethernet1/14
10.74.0.0/16         10.100.100.230     Ethernet1/14
10.75.0.0/16         10.100.100.230     Ethernet1/14
10.76.0.0/16         10.100.100.230     Ethernet1/14
10.77.0.0/16         10.100.100.230     Ethernet1/14
10.78.0.0/16         10.100.100.230     Ethernet1/14
10.79.0.0/16         10.100.100.230     Ethernet1/14
10.80.0.0/16         10.100.100.230     Ethernet1/14
10.82.20.0/24        10.100.100.142     Vlan1800
10.82.21.0/24        10.100.100.142     Vlan1800
10.82.22.0/24        10.100.100.142     Vlan1800
10.82.22.0/26        10.100.100.142     Vlan1800
10.82.22.64/26       10.100.100.142     Vlan1800
10.82.22.80/32       10.100.100.142     Vlan1800
10.82.22.192/26      10.100.100.142     Vlan1800
10.82.22.231/32      10.100.100.142     Vlan1800
10.82.22.240/32      10.100.100.142     Vlan1800
10.82.22.242/32      10.100.100.142     Vlan1800
10.82.22.243/32      10.100.100.142     Vlan1800
10.82.22.244/32      10.100.100.142     Vlan1800
10.82.22.245/32      10.100.100.142     Vlan1800
10.82.23.0/24        10.100.100.142     Vlan1800
10.91.9.0/24         10.100.100.230     Ethernet1/14
10.92.0.0/19         10.100.100.230     Ethernet1/14
10.92.254.0/24       10.100.100.230     Ethernet1/14
10.100.32.0/21       10.100.100.230     Ethernet1/14
10.100.40.0/21       10.100.100.230     Ethernet1/14
10.100.112.0/21      10.100.100.230     Ethernet1/14
10.100.120.0/21      10.100.100.230     Ethernet1/14
10.101.174.0/23      10.100.100.230     Ethernet1/14
10.102.174.0/23      10.100.100.230     Ethernet1/14
10.112.0.0/16        10.100.100.230     Ethernet1/14
10.122.0.0/16        10.100.100.230     Ethernet1/14
10.123.0.0/16        10.100.100.230     Ethernet1/14
*10.128.0.0/17       10.100.100.114     Ethernet1/47
10.130.0.0/16        10.100.100.186     Ethernet1/9
*10.131.0.0/16       10.100.100.114     Ethernet1/47
*10.132.0.0/18       10.100.100.114     Ethernet1/47
*10.132.101.0/24     10.100.100.114     Ethernet1/47
*10.132.102.0/24     10.100.100.114     Ethernet1/47
*10.132.103.0/24     10.100.100.114     Ethernet1/47
*10.132.104.0/24     10.100.100.114     Ethernet1/47
*10.132.150.0/24     10.100.100.114     Ethernet1/47
*10.132.170.0/24     10.100.100.114     Ethernet1/47

```

**Help:** execute the command "show forwarding ipv4 route"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip arp

**Output:**
```

Flags: * - Adjacencies learnt on non-active FHRP router
       + - Adjacencies synced via CFSoE
       # - Adjacencies Throttled for Glean
       D - Static Adjacencies attached to down interface

IP ARP Table for all contexts
Total number of entries: 22
Address         Age       MAC Address     Interface
1.1.1.2         00:00:57  3c60.f40e.f9c3  Ethernet1/41
1.0.11.2        00:01:02  3c60.f40e.f9c4  Ethernet1/47
10.3.1.101      00:06:06  d46d.5031.88b0  mgmt0
10.3.1.102      00:18:18  e0ac.b16b.e940  mgmt0
10.3.1.104      00:17:17  e5ac.b16c.aac8  mgmt0
10.3.1.105      00:13:08  d46d.503c.beb0  mgmt0
10.3.0.20       00:15:11  487b.6bad.7b36  mgmt0
10.3.0.250      00:14:56  0000.0c9f.fa14  mgmt0
10.3.0.251      00:07:08  03c5.a4e8.c342  mgmt0
10.3.0.252      00:14:14  02c5.a4ea.56c2  mgmt0
192.168.10.12   00:00:57  8c60.0012.0012  Vlan10
10.45.69.110    00:09:49  70e4.225a.5e6a  Ethernet1/1.2151
10.45.69.106    00:00:05  d46d.501e.2a92  Ethernet1/2.2151
10.225.19.113   00:00:57  8c60.f40e.f9c3  Vlan2051
10.254.254.113  00:00:57  8b60.f40e.f9c3  Vlan2003
10.225.19.110   00:09:51  7ee4.225a.5e6a  Ethernet1/1.2051
10.225.19.106   00:00:05  a16d.501e.2a92  Ethernet1/2.2051
10.254.254.106  00:00:05  a16d.501e.2a92  Ethernet1/2.2003
10.254.254.110  00:09:50  1ee4.125a.5e6a  Ethernet1/1.2003
10.15.154.110   00:09:50  1ee4.125a.5e6a  Ethernet1/1.2103
10.15.154.106   00:00:06  d46d.301e.2a92  Ethernet1/2.2103
10.215.51.250      -      0000.0c9f.f9d3  Vlan2515
10.5.6.10       00:00:16  INCOMPLETE      Vlan1425
```

**Help:** execute the command "show ip arp"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ip pim interface brief vrf all

**Output:**
```
PIM Interface Status for VRF "default"
Interface            IP Address      PIM DR Address  Neighbor  Border
                                                     Count     Interface
Vlan100              192.0.2.1       192.0.2.2       0         no
Ethernet1/1.10       192.0.2.3       192.0.2.4       1         no

PIM Interface Status for VRF "red"
Interface            IP Address      PIM DR Address  Neighbor  Border
                                                     Count     Interface
Ethernet1/1.20       192.0.2.5       192.0.2.6       1         no


```

**Help:** execute the command "show ip pim interface brief vrf all"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show interfaces switchport

**Output:**
```
Name: Ethernet1/1
  Switchport: Enabled
  Switchport Monitor: Not enabled
  Switchport Isolated : Not enabled
  Switchport Block Multicast: Not enabled
  Switchport Block Unicast: Not enabled
  Operational Mode: access
  Access Mode VLAN: 3 (Vlan not created)
  Trunking Native Mode VLAN: 1 (default)
  Trunking VLANs Allowed: 1-4094
  Voice VLAN: none
  Extended Trust State : not trusted [COS = 0]
  Administrative private-vlan primary host-association: none
  Administrative private-vlan secondary host-association: none
  Administrative private-vlan primary mapping: none
  Administrative private-vlan secondary mapping: none
  Administrative private-vlan trunk native VLAN: none
  Administrative private-vlan trunk encapsulation: dot1q
  Administrative private-vlan trunk normal VLANs: none
  Administrative private-vlan trunk private VLANs: none
  Operational private-vlan: none
Name: Ethernet1/2
  Switchport: Enabled
  Switchport Monitor: Not enabled
  Switchport Isolated : Not enabled
  Switchport Block Multicast: Not enabled
  Switchport Block Unicast: Not enabled
  Operational Mode: trunk
  Access Mode VLAN: 1 (default)
  Trunking Native Mode VLAN: 5 (Vlan not created)
  Trunking VLANs Allowed: 1-4094
  Voice VLAN: none
  Extended Trust State : not trusted [COS = 0]
  Administrative private-vlan primary host-association: none
  Administrative private-vlan secondary host-association: none
  Administrative private-vlan primary mapping: none
  Administrative private-vlan secondary mapping: none
  Administrative private-vlan trunk native VLAN: none
  Administrative private-vlan trunk encapsulation: dot1q
  Administrative private-vlan trunk normal VLANs: none
  Administrative private-vlan trunk private VLANs: none
  Operational private-vlan: none
Name: Ethernet1/3
  Switchport: Enabled
  Switchport Monitor: Not enabled
  Switchport Isolated : Not enabled
  Switchport Block Multicast: Not enabled
  Switchport Block Unicast: Not enabled
  Operational Mode: trunk
  Access Mode VLAN: 1 (default)
  Trunking Native Mode VLAN: 1 (default)
  Trunking VLANs Allowed: 1-4094
  Voice VLAN: none
  Extended Trust State : not trusted [COS = 0]
  Administrative private-vlan primary host-association: none
  Administrative private-vlan secondary host-association: none
  Administrative private-vlan primary mapping: none
  Administrative private-vlan secondary mapping: none
  Administrative private-vlan trunk native VLAN: none
  Administrative private-vlan trunk encapsulation: dot1q
  Administrative private-vlan trunk normal VLANs: none
  Administrative private-vlan trunk private VLANs: none
  Operational private-vlan: none

```

**Help:** execute the command "show interfaces switchport"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show clock

**Output:**
```
18:57:38.347 UTC Mon Oct 19 2015

```

**Help:** execute the command "show clock"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show ipv6 interface brief

**Output:**
```
IPv6 Interface Status for VRF "default"(1)
Interface        IPv6 Address/Link-local Address           Interface Status
                                                           prot/link/admin
Vlan44           2a01:3333:1:44::2                         up/up/up
                 fe80::333:4444:5555:8888
Vlan45           2a01:3333:1:51::2                         up/up/up
                 fe80::333:4444:5555:8888
Vlan46           2a01:3333:1:52::2                         up/up/up
                 fe80::333:4444:5555:8888
Vlan47           2a01:3333:1:53::2                         up/up/up
                 fe80::333:4444:5555:8888
Vlan48           2a01:3333:1:60::2                         up/up/up
                 fe80::333:4444:5555:8888
Vlan49           2a01:3333:1:79::2                         up/up/up
                 fe80::333:4444:5555:8888
Vlan50           2a01:3333:1:80::2                         up/up/up
                 fe80::333:4444:5555:8888

```

**Help:** execute the command "show ipv6 interface brief"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show cts interface all

**Output:**
```
CTS Information for Interface Ethernet1/2:
    CTS is enabled, mode:   CTS_MODE_MANUAL
    IFC state:              Unknown
    Authentication Status:  CTS_AUTHC_INIT
      Peer Identity:        MyDevice2
      Peer is:              Unknown in manual mode
      802.1X role:          CTS_ROLE_UNKNOWN
      Last Re-Authentication: 
    Authorization Status:   CTS_AUTHZ_INIT
      PEER SGT:             0
      Peer SGT assignment:  Not Trusted
    SAP Status:             CTS_SAP_INIT
      Configured pairwise ciphers: 
      Replay protection: 
      Replay protection mode: 
      Selected cipher: 
    Propagate SGT: Enabled

CTS Information for Interface Ethernet1/3:
    CTS is enabled, mode:   CTS_MODE_MANUAL
    IFC state:              Unknown
    Authentication Status:  CTS_AUTHC_INIT
      Peer Identity:        
      Peer is:              Unknown in manual mode
      802.1X role:          CTS_ROLE_UNKNOWN
      Last Re-Authentication: 
    Authorization Status:   CTS_AUTHZ_SKIPPED_CONFIG
      PEER SGT:             2
      Peer SGT assignment:  Not Trusted
    SAP Status:             CTS_SAP_INIT
      Configured pairwise ciphers: 
      Replay protection: 
      Replay protection mode: 
      Selected cipher: 
    Propagate SGT: Enabled


```

**Help:** execute the command "show cts interface all"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show lldp neighbors

**Output:**
```
Capability codes:
  (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
  (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other
 Device ID            Local Intf      Hold-time  Capability  Port ID  
nx-osv9000-3-long-name.com
                     Eth1/1          120        BR          Ethernet1/1   
nx-osv9000-4-extremely-long-name
                     Eth1/2          120        BR          Ethernet1/1   
nx-osv9000-2         Eth1/3          120        BR          Ethernet1/3   
Total entries displayed: 3

```

**Help:** execute the command "show lldp neighbors"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### show version

**Output:**
```
Documents: http://www.cisco.com/en/US/products/ps9372/tsd_products_support_series_home.html
 Copyright (c) 2002-2016, Cisco Systems, Inc. All rights reserved.
The copyrights to certain works contained herein are owned by
other third parties and are used and distributed under license.
Some parts of this software are covered under the GNU Public
License. A copy of the license is available at
http://www.gnu.org/licenses/gpl.html.

Software
  BIOS:      version 3.6.0
  Power Sequencer Firmware: 
             Module 1: v7.0
             Module 1: v1.0
             Module 2: v1.0
             Module 3: v1.0
  Microcontroller Firmware:        version v1.0.0.2
  QSFP Microcontroller Firmware:   
             Module not detected
  CXP Microcontroller Firmware:   
             Module not detected
  kickstart: version 7.1(4)N1(1)
  system:    version 7.1(4)N1(1)
  BIOS compile time:       05/09/2012
  kickstart image file is: bootflash:///n5000-uk9-kickstart.7.1.4.N1.1.bin
  kickstart compile time:  9/2/2016 10:00:00 [09/02/2016 19:37:35]
  system image file is:    bootflash:///n5000-uk9.7.1.4.N1.1.bin
  system compile time:     9/2/2016 10:00:00 [09/02/2016 21:16:21]


Hardware
  cisco Nexus 5596 Chassis ("O2 48X10GE/Modular Supervisor")
  Intel(R) Xeon(R) CPU         with 8253848 kB of memory.
  Processor Board ID FOC17153X08

  Device name: IEDP02-N5K-SW01
  bootflash:    2007040 kB

Kernel uptime is 749 day(s), 15 hour(s), 17 minute(s), 48 second(s)

Last reset at 958444 usecs after  Wed Nov  1 21:20:35 2017

  Reason: Disruptive upgrade
  System version: 7.0(7)N1(1)
  Service: 

plugin
  Core Plugin, Ethernet Plugin, Fc Plugin

```

**Help:** execute the command "show version"

**Prompt:**
- cisco_nxos>
- cisco_nxos#

### terminal width 511

**Output:** None

**Help:** Execute the command terminal width 511. This automatically generated. Feel free to change it!

**Prompt:**
- cisco_nxos>
- cisco_nxos#

