# ubiquiti_edgerouter


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
- ubiquiti@ubiquiti:~$

### show interfaces

**Output:**
```
Codes: S - State, L - Link, u - Up, D - Down, A - Admin Down
Interface    IP Address                        S/L  Description                 
---------    ----------                        ---  -----------                 
eth0         -                                 u/u  Port
eth1         192.168.1.1/24                    u/u  Eth 1
             2a05:c100:1d::1/64
eth2         -                                 u/D  Port
eth3         -                                 u/D  Port
lo           127.0.0.1/8                       u/u
             ::1/128      
eth4         192.168.1.1/24                    u/u  datas
eth4.2900    -                                 u/u
eth5         2a05:c100:1d::1/64                u/u
switch0.1    192.168.10.251/24                 u/u  vl1-siege-serveurs

```

**Help:** execute the command "show interfaces"

**Prompt:**
- ubiquiti@ubiquiti:~$
- ubiquiti@ubiquiti:#

### show arp

**Output:**
```
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.2.10             ether   34:29:8f:76:0f:e8   C                     eth1
192.168.11.127                   (incomplete)                              switch0.1
172.16.39.98             ether   00:0a:b0:04:98:fb   C                     eth5
172.16.35.123            ether   00:21:b6:00:34:c8   C                     eth3
172.16.36.200                    (incomplete)                              eth6
172.16.37.165            ether   ac:cc:8e:15:a6:3f   C                     eth7
172.16.37.21             ether   90:b1:1c:2f:92:82   C                     eth7

```

**Help:** execute the command "show arp"

**Prompt:**
- ubiquiti@ubiquiti:~$
- ubiquiti@ubiquiti:#

### show dhcp leases

**Output:**
```
Warning: leased IP address [2886804269] not in any of the pools
Warning: leased IP address [2886804283] not in any of the pools
Warning: leased IP address [2886804287] not in any of the pools
Warning: leased IP address [2886804295] not in any of the pools
Warning: leased IP address [2886804284] not in any of the pools
Warning: leased IP address [2886804252] not in any of the pools
 Warning: leased IP address [2886804248] not in any of the pools
Warning: leased IP address [2886804305] not in any of the pools
IP address      Hardware Address   Lease expiration     Pool       Client Name
----------      ----------------   ----------------     ----       -----------
125.125.15.12   00:0a:95:9d:68:16  Sep 18, 2021         5          HOSTNAME  

```

**Help:** execute the command "show dhcp leases"

**Prompt:**
- ubiquiti@ubiquiti:~$
- ubiquiti@ubiquiti:#

### show dhcpv6 server leases

**Output:**
```
There are 6 DHCPv6 leases:

IPv6 Address                            Expiration          State
--------------------------------------- ------------------- ------
2001:d98:5554::210                      2014/01/27 18:55:53 active
2001:d98:5554::212                      2014/01/27 19:46:12 active
2001:d98:5554::213                      2014/01/27 19:00:18 active
2001:d98:5554::225                      2014/01/27 20:31:06 active
2001:d98:5554::214                      2014/01/27 18:55:57 active
2001:d98:5554::219                      2011/06/01 06:02:16 expired

```

**Help:** execute the command "show dhcpv6 server leases"

**Prompt:**
- ubiquiti@ubiquiti:~$
- ubiquiti@ubiquiti:#

### show ipv6 neighbors

**Output:**
```
2a01::68e5:a41e:722c:2f7b dev eth0 lladdr 6c:40:08:4f:35:bc STALE
fe80::7e91:22ff:fe87:d336 dev eth0 lladdr 7c:91:22:87:d3:36 STALE
fe80::feec:daff:fe47:bf49 dev eth0 lladdr fc:ec:da:47:bf:49 router STALE
fe80::250:56ff:fe90:50ee dev eth4.51 lladdr 00:50:56:90:50:ee router REACHABLE
fe80::11:32ff:fe2a:c970 dev eth1 lladdr 02:11:32:2a:c9:70 STALE
2a05:c100:37:0:6d40:4b07:e518:9ada dev switch0.1  FAILED
fe80::be16:65ff:fe7e:1cc1  FAILED
2a02:33:44::1  router INCOMPLETE
 fe80::d093:e5ff:fe8e:8427 lladdr d2:93:e5:8e:84:27 STALE
2a02:33:44::12 lladdr d2:93:e5:8e:84:27 STALE
fe80::be16:65ff:fe7e:1cc1 lladdr bc:16:65:7e:1c:c1 DELAY
2a02:33:44::1 lladdr bc:16:65:7e:1c:c1 router REACHABLE
fe80::d093:e5ff:fe8e:8427 lladdr d2:93:e5:8e:84:27 STALE
2a02:33:44::12 lladdr d2:93:e5:8e:84:27 STALE

```

**Help:** execute the command "show ipv6 neighbors"

**Prompt:**
- ubiquiti@ubiquiti:~$
- ubiquiti@ubiquiti:#

### show interfaces ethernet physical

**Output:**
```
Settings for eth0:
   Auto-negotiation: off
   Speed: 1000Mb/s
   Duplex: Full
   Link detected: no

```

**Help:** execute the command "show interfaces ethernet physical"

**Prompt:**
- ubiquiti@ubiquiti:~$
- ubiquiti@ubiquiti:#

### show ipv6 route

**Output:**
```
IPv6 Routing Table
Codes: K - kernel route, C - connected, S - static, R - RIP, O - OSPF,
       IA - OSPF inter area, E1 - OSPF external type 1,
       E2 - OSPF external type 2, N1 - OSPF NSSA external type 1,
       N2 - OSPF NSSA external type 2, B - BGP
Timers: Uptime

IP Route Table for VRF "default"
S      ::/0 [50/0] via ::, pppoe4, 01w0d05h
S      ::/64 [50/0] via 2a05:c100:1d::2, eth1, 00:00:04
C      ::1/128 via ::, lo, 01w0d05h
C      2a05:b780:0:1d::/64 via ::, pppoe4, 01w0d05h
C      2a05:c100:1d::/64 via ::, eth1, 01:11:26
C      fe80::/10 via ::, pppoe4, 01w0d05h
C      fe80::/64 via ::, eth1, 01:11:25


```

**Help:** execute the command "show ipv6 route"

**Prompt:**
- ubiquiti@ubiquiti:~$
- ubiquiti@ubiquiti:#

### show nat rules

**Output:**
```
Type Codes:  SRC - source, DST - destination, MASQ - masquerade
              X at the front of rule implies rule is excluded

rule   type  intf     translation                                               
----   ----  ----     -----------                                               
1      DST   pppoe4   daddr 23.90.233.198 to 192.168.1.100                      
    proto-tcp         dport 8080 to 80                                              

2      DST   pppoe4   daddr 23.90.233.198 to 192.168.1.231                      
    proto-tcp         dport 65001 to 3389                                           

3      DST   pppoe4   daddr 23.90.233.198 to 192.168.1.2                        
    proto-tcp         dport 6666 to 6666                                            

4      DST   pppoe4   daddr 23.90.233.198 to 192.168.1.111                      
    proto-tcp_udp     dport 83 to 83                                                

5      DST   pppoe4   daddr 23.90.233.198 to 192.168.1.110                      
    proto-tcp_udp     dport 80 to 80                                                

6      DST   pppoe4   daddr 23.90.233.198 to 192.168.1.1                        
    proto-tcp_udp     dport 81 to 81                                                

5001   MASQ  pppoe4   saddr 192.168.1.0/24 to 23.90.233.198                     
    proto-all         sport ANY                                                     

5002   MASQ  pppoe4   saddr 192.168.42.0/24 to 23.90.233.198                    
    proto-all         sport ANY

```

**Help:** execute the command "show nat rules"

**Prompt:**
- ubiquiti@ubiquiti:~$
- ubiquiti@ubiquiti:#

### show ip route

**Output:**
```
Codes: K - kernel, C - connected, S - static, R - RIP, B - BGP
       O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       > - selected route, * - FIB route, p - stale info

IP Route Table for VRF "default"
S    *> 0.0.0.0/0 [50/0] is directly connected, pppoe4
S    *> 22.22.23.0/24 [1/0] via 198.168.0.1 (recursive is directly connected, pppoe4) )
S    *> 23.23.23.0/24 [1/0] via 198.168.0.1 (recursive is directly connected, pppoe4) )
C    *> 23.90.232.243/32 is directly connected, pppoe4
S    *> 25.22.23.0/24 [35/0] via 198.168.0.1 (recursive is directly connected, pppoe4) )
C    *> 100.95.11.96/32 is directly connected, pppoe4
C    *> 127.0.0.0/8 is directly connected, lo
S    *> 192.100.111.0/24 [1/0] via 192.168.1.25 (recursive is directly connected, pppoe4) )
     *>                  [1/0] via 192.168.1.20 (recursive is directly connected, pppoe4) )

```

**Help:** execute the command "show ip route"

**Prompt:**
- ubiquiti@ubiquiti:~$
- ubiquiti@ubiquiti:#

### show version

**Output:**
```
Version:      v2.0.6
Build ID:     5208554
Build on:     07/08/19 06:11
Copyright:    2012-2018 Ubiquiti Networks, Inc.
HW model:     EdgeRouter 6P
 HW S/N:       FCECDA47BF8A
Uptime:       16:17:57 up 11 days,  6:15,  1 user,  load average: 0.09, 0.06, 0.01

```

**Help:** execute the command "show version"

**Prompt:**
- ubiquiti@ubiquiti:~$
- ubiquiti@ubiquiti:#

### terminal length 0

**Output:** None

**Help:** Execute the command terminal length 0. This automatically generated. Feel free to change it!

**Prompt:**
- ubiquiti_edgerouter>
- ubiquiti_edgerouter#

### terminal width 512

**Output:** None

**Help:** Execute the command terminal width 512. This automatically generated. Feel free to change it!

**Prompt:**
- ubiquiti_edgerouter>
- ubiquiti_edgerouter#

