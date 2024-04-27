# dell_force10


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
- dell_force10>

### show arp

**Output:**
```
Protocol    Address         Age(min)  Hardware Address    Interface  VLAN             CPU
-----------------------------------------------------------------------------------------
Internet    192.168.168.5        34   fc:93:ee:c6:73:b2   Ma 0/0      -               CP
Internet    192.168.168.11        0   e5:97:c1:0e:cb:b7   Ma 0/0      -               CP
Internet    192.168.168.130       0   8a:72:f4:ef:fe:e3   Ma 0/0      -               CP
Internet    192.168.186.99        6   5d:7c:2f:d5:62:57   Te 0/22    Vl 10            CP
Internet    192.168.186.254       -   5d:7c:2f:d5:62:58      -       Vl 10            CP

```

**Help:** execute the command "show arp"

**Prompt:**
- dell_force10>
- dell_force10#

### show vlan

**Output:**
```

Codes: * - Default VLAN, G - GVRP VLANs, P - Primary, C - Community, I - Isolated
Q: U - Untagged, T - Tagged
   x - Dot1x untagged, X - Dot1x tagged
   G - GVRP tagged, M - Vlan-stack, H - Hyperpull tagged

    NUM    Status    Description                     Q Ports
*   1      Inactive                                  U Te 0/42-43
                                                     U Fo 0/48,56,60
    12     Inactive                                  U Te 0/0-9,45-47
    13     Inactive  myvlan13                        
    14     Inactive                                  
    100    Inactive  pixelrebel is awesome           T Te 0/30
                                                     U Te 0/40-41,44
                                                     U Fo 0/52
    200    Inactive                                  
    330    Inactive  tagged example                  T Te 0/30,35-37
                                                     U Te 0/31-34,38-39
    351    Inactive  dev 351 vlan                    U Te 0/10-19
    380    Active    dev-VLAN 380                    U Te 0/20-29

```

**Help:** execute the command "show vlan"

**Prompt:**
- dell_force10>
- dell_force10#

### show ip interface brief

**Output:**
```
Interface                     IP-Address      OK  Method Status                Protocol
TenGigabitEthernet 0/1        unassigned      NO  None   up                    down
TenGigabitEthernet 0/2        unassigned      NO  None   up                    down
TenGigabitEthernet 0/3        unassigned      YES None   up                    up
TenGigabitEthernet 0/4        unassigned      YES None   up                    up
TenGigabitEthernet 0/5        unassigned      YES None   up                    up
TenGigabitEthernet 0/6        unassigned      NO  None   up                    down
TenGigabitEthernet 0/7        unassigned      NO  None   up                    down
TenGigabitEthernet 0/8        unassigned      NO  None   up                    down
TenGigabitEthernet 0/9        unassigned      NO  None   up                    down
TenGigabitEthernet 0/10       unassigned      YES None   up                    up
TenGigabitEthernet 0/11       unassigned      YES None   up                    up
TenGigabitEthernet 0/12       unassigned      YES None   up                    up
TenGigabitEthernet 0/13       unassigned      YES None   up                    up
TenGigabitEthernet 0/14       unassigned      NO  None   up                    down
TenGigabitEthernet 0/15       unassigned      NO  None   up                    down
TenGigabitEthernet 0/16       unassigned      NO  None   up                    down
TenGigabitEthernet 0/17       unassigned      NO  None   up                    down
TenGigabitEthernet 0/18       unassigned      NO  None   up                    down
TenGigabitEthernet 0/19       unassigned      NO  None   up                    down
TenGigabitEthernet 0/20       unassigned      NO  None   up                    down
TenGigabitEthernet 0/21       unassigned      NO  None   up                    down
TenGigabitEthernet 0/22       unassigned      NO  None   up                    down
TenGigabitEthernet 0/23       unassigned      NO  None   up                    down
TenGigabitEthernet 0/24       unassigned      NO  None   up                    down
TenGigabitEthernet 0/25       unassigned      NO  None   up                    down
TenGigabitEthernet 0/26       unassigned      NO  None   up                    down
TenGigabitEthernet 0/27       unassigned      NO  None   up                    down
TenGigabitEthernet 0/28       unassigned      NO  None   up                    down
TenGigabitEthernet 0/29       unassigned      NO  None   up                    down
TenGigabitEthernet 0/30       unassigned      NO  None   up                    down
TenGigabitEthernet 0/31       unassigned      NO  None   up                    down
TenGigabitEthernet 0/32       unassigned      NO  None   up                    down
TenGigabitEthernet 0/33       unassigned      NO  None   up                    down
TenGigabitEthernet 0/34       unassigned      NO  None   up                    down
TenGigabitEthernet 0/35       unassigned      NO  None   up                    down
TenGigabitEthernet 0/36       unassigned      NO  None   up                    down
TenGigabitEthernet 0/37       unassigned      NO  None   up                    down
TenGigabitEthernet 0/38       unassigned      NO  None   up                    down
TenGigabitEthernet 0/39       unassigned      NO  None   up                    down
TenGigabitEthernet 0/40       unassigned      NO  None   up                    down
TenGigabitEthernet 0/41       unassigned      YES None   up                    up
TenGigabitEthernet 0/42       unassigned      YES None   up                    up
TenGigabitEthernet 0/43       unassigned      YES None   up                    up
TenGigabitEthernet 0/44       unassigned      YES None   up                    up
TenGigabitEthernet 0/49       unassigned      NO  None   up                    down
TenGigabitEthernet 0/50       unassigned      NO  None   up                    down
TenGigabitEthernet 0/51       unassigned      NO  None   up                    down
TenGigabitEthernet 0/52       unassigned      NO  None   up                    down
TenGigabitEthernet 0/53       unassigned      NO  None   up                    down
TenGigabitEthernet 0/54       unassigned      NO  None   up                    down
TenGigabitEthernet 0/55       unassigned      NO  None   up                    down
TenGigabitEthernet 0/56       unassigned      NO  None   up                    down
ManagementEthernet 0/0        10.151.5.208    YES Manual up                    up
Port-channel 128              unassigned      YES None   up                    up
```

**Help:** execute the command "show ip interface brief"

**Prompt:**
- dell_force10>
- dell_force10#

### show vlan brief

**Output:**
```
VLAN Name                             STG   MAC Aging IP Address         
---- -------------------------------- ----  --------- ------------------ 
1                                     0     1800      unassigned         
12                                    0     1800      10.10.10.254/24    
13   thirteen                         0     1800      192.168.100.0/22         
14   fourteen                         0     1800      unassigned         
15   fifteen                          0     1800      unassigned         
67   sixty seven                      0     1800      unassigned         

```

**Help:** execute the command "show vlan brief"

**Prompt:**
- dell_force10>
- dell_force10#

### show version

**Output:**
```
Dell Real Time Operating System Software
Dell Operating System Version:  2.0
Dell Application Software Version:  9.9(0.0)
Copyright (c) 1999-2015 by Dell Inc. All Rights Reserved.
Build Time: Tue Sep  8 03:51:15 2015
Build Path: /sites/eqx/work/swbuild01_1/patch02/E9-9-0/SW/SRC
Dell Networking OS uptime is 1 week(s), 2 day(s), 9 hour(s), 5 minute(s)

System image file is "system://A"

System Type: S4820T
Control Processor: Freescale QorIQ P2020 with 2 Gbytes (2147483648 bytes) of memory, core(s) 1.

128M bytes of boot flash memory.

  1 52-port GE/TE/FG (SE)
 48 Ten GigabitEthernet/IEEE 802.3 interface(s)
  4 Forty GigabitEthernet/IEEE 802.3 interface(s)
```

**Help:** execute the command "show version"

**Prompt:**
- dell_force10>
- dell_force10#

### terminal width 511

**Output:** None

**Help:** Execute the command terminal width 511. This automatically generated. Feel free to change it!

**Prompt:**
- dell_force10>
- dell_force10#

### terminal length 0

**Output:** None

**Help:** Execute the command terminal length 0. This automatically generated. Feel free to change it!

**Prompt:**
- dell_force10>
- dell_force10#

