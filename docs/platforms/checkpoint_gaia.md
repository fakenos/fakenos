# checkpoint_gaia


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
- checkpoint_gaia>

### set clienv rows 0

**Output:** None

**Help:** set the terminal width to full

**Prompt:**
- checkpoint_gaia>
- checkpoint_gaia#

### show domainname

**Output:**
```
Domain name  example.com

```

**Help:** execute the command "show domainname"

**Prompt:**
- checkpoint_gaia>
- checkpoint_gaia#

### show version all

**Output:**
```
Product version Check Point Gaia R77.30
OS build 204
OS kernel version 2.6.18-92cp
OS edition 32-bit

```

**Help:** execute the command "show version all"

**Prompt:**
- checkpoint_gaia>
- checkpoint_gaia#

### show asset all

**Output:**
```
Platform: T-180-00
Model: Check Point 4800
Serial Number: 0000000000
 CPU Frequency: 2660.283
Disk Model: XXX NNNNNNNNNN-XXXXXXX
Disk Capacity: 251 GB
Memory Slot 1 Size: 4096 MB
Number of line cards: 1
Line card 1 model: AAA-00000-111
Line card 1 type: 8 port0 1GbE Copper
Power supply 1 name: Power Supply #1
Power supply 1 status: Up
Power supply 2 name: Power Supply #2
 Power supply 2 status: Up



```

**Help:** execute the command "show asset all"

**Prompt:**
- checkpoint_gaia>
- checkpoint_gaia#

### show virtual-system all

**Output:**
```
Virtual systems list
VS ID       VS NAME
0           0
1           gandalf_VR01
2           gandalf_SRCXT-VS01
```

**Help:** execute the command "show virtual-system all"

**Prompt:**
- checkpoint_gaia>
- checkpoint_gaia#

### show interfaces all

**Output:**
```
Interface Mgmt
    state on
    mac-addr 00:1c:7f:43:08:28
    type ethernet
    link-state link up
    instance 0
    mtu 1500
    auto-negotiation on
    speed 1000M
    ipv6-autoconfig Not configured
    monitor-mode Not configured
    duplex full
    link-speed 1000M/full
    comments
    ipv4-address 2.2.2.2/29
    ipv6-address Not Configured
    ipv6-local-link-address Not Configured

Statistics:
    TX bytes:65587685757 packets:135150363 errors:0 dropped:0 overruns:0 carrier:0
    RX bytes:8575369842 packets:80348499 errors:0 dropped:0 overruns:0 frame:0


Interface Sync
    state on
    mac-addr 00:1c:7f:43:08:29
    type ethernet
    link-state link up
    instance 0
    mtu 1500
    auto-negotiation Not configured
    speed 1000M
    ipv6-autoconfig Not configured
    monitor-mode Not configured
    duplex full
    link-speed Not configured
    comments
    ipv4-address 192.168.0.1/30
    ipv6-address Not Configured
    ipv6-local-link-address Not Configured

Statistics:
    TX bytes:259664923573 packets:2251872598 errors:0 dropped:0 overruns:0 carrier:0
    RX bytes:259266301613 packets:2251102479 errors:0 dropped:0 overruns:0 frame:0


Interface bond18
    state on
    mac-addr 00:1c:7f:64:10:9e
    type bond
    link-state not available
    instance 0
    mtu 1500
    auto-negotiation Not configured
    speed N/A
    ipv6-autoconfig Not configured
    monitor-mode Not configured
    duplex N/A
    link-speed Not configured
    comments
    ipv4-address Not Configured
    ipv6-address Not Configured
    ipv6-local-link-address Not Configured

Statistics:
    TX bytes:488671526784 packets:6484144830 errors:0 dropped:0 overruns:0 carrier:0
    RX bytes:30726434732106 packets:22116800051 errors:0 dropped:0 overruns:0 frame:0


Interface bond18.51
    state on
    mac-addr 00:1c:7f:64:10:9e
    type vlan
    link-state not available
    instance 2
    mtu 1500
    auto-negotiation Not configured
    speed N/A (bond18)
    ipv6-autoconfig Not configured
    monitor-mode Not configured
    duplex N/A (bond18)
    link-speed Not configured
    comments
    ipv4-address 1.1.1.1/27
    ipv6-address Not Configured
    ipv6-local-link-address Not Configured

Statistics:
    TX bytes:4378789096 packets:35892004 errors:0 dropped:0 overruns:0 carrier:0
    RX bytes:3878961582 packets:35887605 errors:0 dropped:0 overruns:0 frame:0


Interface eth1-01
    state on
    mac-addr 00:1c:7f:64:10:9e
    type ethernet
    link-state link up
    instance 0
    mtu 1500
    auto-negotiation Not configured
    speed 10G
    ipv6-autoconfig Not configured
    monitor-mode Not configured
    duplex full
    link-speed Not configured
    comments
    ipv4-address Not Configured
    ipv6-address Not Configured
    ipv6-local-link-address Not Configured

Statistics:
    TX bytes:250113820171 packets:3347079150 errors:0 dropped:0 overruns:0 carrier:0
    RX bytes:15432889269477 packets:11081410222 errors:0 dropped:0 overruns:0 frame:0


Interface lo
    state on
    mac-addr Not configured
    type loopback
    link-state not available
    instance 0
    mtu 65536
    auto-negotiation Not configured
    speed N/A
    ipv6-autoconfig Not configured
    monitor-mode Not configured
    duplex N/A
    link-speed Not configured
    comments
    ipv4-address 127.0.0.1/8
    ipv6-address Not Configured
    ipv6-local-link-address Not Configured

Statistics:
    TX bytes:16669231829 packets:78838857 errors:0 dropped:0 overruns:0 carrier:0
    RX bytes:16669231829 packets:78838857 errors:0 dropped:0 overruns:0 frame:0
 

Interface wrp128
    state on
    mac-addr 00:00:00:00:00:00
    type wrp
    link-state not available
    instance 2
    mtu 1500
    auto-negotiation Not configured
    speed N/A
    ipv6-autoconfig Not configured
    monitor-mode Not configured
    duplex N/A
    link-speed Not configured
    comments
    ipv4-address 1.1.1.1/32
    ipv6-address Not Configured
    ipv6-local-link-address Not Configured

Statistics:
    TX bytes:9367255 packets:222957 errors:0 dropped:0 overruns:0 carrier:0
    RX bytes:6242740 packets:222940 errors:0 dropped:0 overruns:0 frame:0
```

**Help:** execute the command "show interfaces all"

**Prompt:**
- checkpoint_gaia>
- checkpoint_gaia#

### show arp dynamic all

**Output:**
```
Dynamic Arp Parameters

IP Address                 Mac Address
192.168.13.233                  BC:30:5B:B5:76:DB
10.19.252.42                    74:8E:F8:A4:59:60
172.31.254.101                  60:9C:9F:3B:7E:40
172.19.4.144                    00:50:56:9A:41:8A
10.200.12.61                    A0:D3:C1:FB:61:31
192.168.13.146                  A4:5D:36:2B:58:7C

```

**Help:** execute the command "show arp dynamic all"

**Prompt:**
- checkpoint_gaia>
- checkpoint_gaia#

### show route

**Output:**
```
Codes: C - Connected, S - Static, R - RIP, B - BGP (D - Default),
       O - OSPF IntraArea (IA - InterArea, E - External, N - NSSA)
       A - Aggregate, K - Kernel Remnant, H - Hidden, P - Suppressed,
       U - Unreachable, i - Inactive

S         0.0.0.0/0           via 10.10.10.1, eth1-02.122, cost 0, age 4238351
                                  default
S         10.0.0.0/24        via 10.1.1.254, eth1-01.100, cost 0, age 4238351
                                  Comment-static-Route-1
C         10.1.1.0/24      is directly connected, eth1.111
                                  Comment-Network-1

```

**Help:** execute the command "show route"

**Prompt:**
- checkpoint_gaia>
- checkpoint_gaia#

### show ntp servers

**Output:**
```
IP Address               Type              Version  
1.1.1.1                  Primary           3        
2.2.2.2                  Secondary         3   

```

**Help:** execute the command "show ntp servers"

**Prompt:**
- checkpoint_gaia>
- checkpoint_gaia#

### show ipv6 route

**Output:**
```
Codes: C - Connected, S - Static, B - BGP, A - Aggregate,
       O - OSPFv3 IntraArea (IA - InterArea, E - External),
       K - Kernel Remnant, H - Hidden, P - Suppressed,
       U - Unreachable, i - Inactive

C         ::1/128                  is directly connected, lo
C         2001:db8:a::/64  is directly connected, eth1-02.100
                                       Comment-Network-1
S         2001:db8:b::/64  via fe80::aaa:65:111, eth1-01.100, cost 0, age 4237508
                                       Comment-static-Route-1

```

**Help:** execute the command "show ipv6 route"

**Prompt:**
- checkpoint_gaia>
- checkpoint_gaia#

### fw stat

**Output:**
```
HOST      POLICY     DATE
localhost Example-Policy 19Oct2017 16:34:20 :  [>Mgmt] [<Mgmt] [>eth1-01.100] [<eth1-01.100] [>eth1-01] [<eth1-01]

```

**Help:** execute the command "fw stat"

**Prompt:**
- checkpoint_gaia>
- checkpoint_gaia#

### show dns

**Output:**
```
DNS setup
Name                  Value                 

Domain                test.com            
DNS server            1.1.1.1
DNS server            2.2.2.2
DNS server              

```

**Help:** execute the command "show dns"

**Prompt:**
- checkpoint_gaia>
- checkpoint_gaia#

### show lom

**Output:**
```
Firmware Revision : 2.2
IP Address : 192.168.0.100

```

**Help:** execute the command "show lom"

**Prompt:**
- checkpoint_gaia>
- checkpoint_gaia#

