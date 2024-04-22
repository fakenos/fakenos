# mikrotik_routeros


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
- mikrotik_routeros>

### ip firewall filter print all without-paging

**Output:**
```
Flags: X - disabled, I - invalid, D - dynamic 
 0    ;;; defconf: accept established,related,untracked
      chain=input action=accept connection-state=established,related,untracked 

 1    ;;; defconf: drop invalid
      chain=input action=drop connection-state=invalid 

 2    ;;; FIREWALL-DMZ-1
      chain=forward action=accept connection-state=established,related,new in-interface=dmz-1-vlan out-interface=pppoe-out1 

 3    chain=forward action=accept dst-address=185.163.212.156/30 

 4    ;;; defconf: accept ICMP
      chain=input action=accept protocol=icmp 

 5    ;;; Acces VPN
      chain=input action=accept protocol=udp dst-port=500,1701,4500 log-prefix="Acces VPN" 

 6    chain=input action=accept protocol=ipsec-esp 

 7    ;;; Acces WAN
      chain=input action=accept protocol=tcp src-address-list=Supervision dst-port=4430,22,8291 

 8    ;;; Acces WAN SNMP
      chain=input action=accept protocol=udp src-address-list=Supervision dst-port=161 
17:20:06 echo: system,error,critical login failure for user admin from 65.160.140.13 via ssh

 9    ;;; defconf: accept to local loopback (for CAPsMAN)
      chain=input action=accept dst-address=127.0.0.1 

10    ;;; defconf: drop all not coming from LAN
      chain=input action=drop in-interface-list=!LAN 

11    ;;; defconf: accept in ipsec policy
      chain=forward action=accept ipsec-policy=in,ipsec 

12    ;;; defconf: accept out ipsec policy
      chain=forward action=accept ipsec-policy=out,ipsec 

13 X  ;;; defconf: fasttrack
      chain=forward action=fasttrack-connection hw-offload=yes connection-state=established,related

14    ;;; defconf: accept established,related, untracked
      chain=forward action=accept connection-state=established,related,untracked 

15    ;;; defconf: drop invalid
      chain=forward action=drop connection-state=invalid 

16    ;;; defconf: drop all from WAN not DSTNATed
      chain=forward action=drop connection-state=new connection-nat-state=!dstnat in-interface-list=WAN 

17    ;;; Input
      chain=input action=accept src-address-list=Eqinoxe 

18    ;;; related established
      chain=input connection-state=established,related 

19    chain=forward connection-state=established,related src-mac-address=67:33:EB:0E:EB:A8

20    ;;; drop invalid connections
17:20:06 echo: system,error,critical login failure for user admin from 65.160.140.13 via ssh
      chain=forward action=drop connection-state=invalid protocol=tcp 

21    ;;; Block all entrant
      chain=input action=drop in-interface=all-ppp 

22    chain=input action=drop in-interface=all-ethernet log-prefix=""

```

**Help:** execute the command "ip firewall filter print all without-paging"

**Prompt:**
- mikrotik_routeros>
- mikrotik_routeros#

### system clock print

**Output:**
```
                  time: 10:00:47
                  date: jul/21/2023
  time-zone-autodetect: yes
        time-zone-name: Europe/Moscow
            gmt-offset: +03:00
            dst-active: no
```

**Help:** execute the command "system clock print"

**Prompt:**
- mikrotik_routeros>
- mikrotik_routeros#

### ip route print terse

**Output:**
```
 0 ADS  dst-address=::/0 gateway=pppoe-out1 gateway-status=pppoe-out1 reachable distance=100 scope=30 target-scope=10 
 1 ADC  dst-address=2a05:c100:7::/64 gateway=bridge-lan gateway-status=bridge-lan reachable distance=0 scope=10 
 2   S  dst-address=9bb8:baac:d400::/38 gateway=ether4 gateway-status=ether4 unreachable distance=44 scope=30 target-scope=10 
17:20:06 echo: system,error,critical login failure for user admin from 65.160.140.13 via ssh
 3 X S  dst-address=ec64:a7fd:bc1c:14c:7960:5000::/84 gateway=ether2 gateway-status=ether2 inactive distance=7 scope=30 target-scope=10 
 4   S  dst-address=fd79:f1d4:a400::/39 gateway=ether5 gateway-status=ether5 unreachable distance=24 scope=30 target-scope=10 

```

**Help:** execute the command "ip route print terse"

**Prompt:**
- mikrotik_routeros>
- mikrotik_routeros#

### ip dhcp-server lease print without-paging

**Output:**
```
Flags: X - disabled, R - radius, D - dynamic, B - blocked 
 #   ADDRESS                                 MAC-ADDRESS       HOST-NAME                     SERVER                     RATE-LIMIT                     STATUS  LAST-SEEN                               
17:20:06 echo: system,error,critical login failure for user admin from 65.160.140.13 via ssh
 0                                           AF:D6:C8:F2:36:16                                                                                         waiting never                                   
 1 X 192.168.1.56                                                                                                       15                             waiting never                                   

```

**Help:** execute the command "ip dhcp-server lease print without-paging"

**Prompt:**
- mikrotik_routeros>
- mikrotik_routeros#

### interface ethernet poe print without-paging

**Output:**
```
bad command name po (line 1 column 7)

```

**Help:** execute the command "interface ethernet poe print without-paging"

**Prompt:**
- mikrotik_routeros>
- mikrotik_routeros#

### interface ethernet print

**Output:**
```
Flags: X - disabled, R - running, S - slave
 #    NAME     MTU MAC-ADDRESS       ARP             SWITCH
 0    ether1  1500 12:34:56:78:90:AA enabled         switch1
 1 R  ether2  1500 12:34:56:78:90:AB enabled         switch1
 2 XS ether3  1500 12:34:56:78:90:AC enabled         switch1
 3  S ether4  1500 12:34:56:78:90:AD enabled         switch1
 4 R  ether5  1500 12:34:56:78:90:AE enabled         switch1

```

**Help:** execute the command "interface ethernet print"

**Prompt:**
- mikrotik_routeros>
- mikrotik_routeros#

### system routerboard print

**Output:**
```
       routerboard: yes
        board-name: hEX PoE lite
             model: RouterBOARD 750UP r2
     serial-number: 8B0208F4D5F9
     firmware-type: qca9531L
  factory-firmware: 3.41
  current-firmware: 3.41
  upgrade-firmware: 6.48.6

```

**Help:** execute the command "system routerboard print"

**Prompt:**
- mikrotik_routeros>
- mikrotik_routeros#

### user active print

**Output:**
```
Flags: R - radius, M - by-romon
 #    WHEN                 NAME       ADDRESS         VIA
 0    jul/21/2023 09:38:39 user1      1.2.3.4         ssh
 1    jul/21/2023 11:00:32 user2      1.2.3.5         telnet

```

**Help:** execute the command "user active print"

**Prompt:**
- mikrotik_routeros>
- mikrotik_routeros#

### ip firewall address-list print terse

**Output:**
```
 0   list=Eqinoxe address=185.48.253.0/27 creation-time=jan/01/2002 01:00:25 
 1   list=Eqinoxe address=185.48.254.0/28 creation-time=jan/01/2002 01:00:25 
 2   list=Eqinoxe address=185.163.212.64/28 creation-time=jan/01/2002 01:00:25 
 3   list=Eqinoxe address=185.163.212.48/28 creation-time=jan/01/2002 01:00:25 
 4   list=Eqinoxe address=185.197.109.16/28 creation-time=jan/01/2002 01:00:25 
 5   list=Supervision address=185.132.66.240 creation-time=jan/01/2002 01:00:25 
 6   list=Supervision address=85.14.167.232/29 creation-time=jan/01/2002 01:00:25 
 7   list=Supervision address=185.48.254.16/29 creation-time=jan/01/2002 01:00:25 
 8   list=Supervision address=5.10.130.152/30 creation-time=jan/01/2002 01:00:25 
 9   list=Supervision address=85.14.167.193 creation-time=jan/01/2002 01:00:25 
10   list=azeazeaze address=192.168.1.1 creation-time=jun/14/2022 06:34:30 
11   list=azeazeaze address=192.168.1.2 creation-time=jun/14/2022 06:44:09 
12   list=azeazeaze address=192.168.1.3 creation-time=jun/14/2022 06:44:51 
13 X list=azeazeaze address=192.168.3.0/24 creation-time=jun/14/2022 07:53:30 
14 D list=azeazeaze address=192.168.3.0/24 creation-time=jun/14/2022 07:53:49 timeout=4m52s 
15 list=snmp-monitoring-address-list address=85.14.167.234 creation-time=mar/01/2023 13:59:33

```

**Help:** execute the command "ip firewall address-list print terse"

**Prompt:**
- mikrotik_routeros>
- mikrotik_routeros#

### log print detail without-paging

**Output:**
```
 time=jul/19 14:27:01 topics=script,info message="Ping testA: Packets Sent = 18, Packets Loss = 10 % "

 time=jul/19 16:27:01 topics=script,info message="Ping testA: Packets Sent = 18, Packets Loss = 10 % "

 time=jul/19 16:37:01 topics=script,info message="Ping testA: Packets Sent = 12, Packets Loss = 40 % "

 time=jul/19 19:17:01 topics=script,info message="Ping testA: Packets Sent = 17, Packets Loss = 15 % "

 time=jul/19 03:05:02 topics=script,warning message="Connection via Box bad. Reset USB Modem"

 time=jul/20 03:07:40 topics=interface,info message="lte1 link down"

 time=jul/20 03:07:46 topics=interface,info message="lte1 link up"

 time=jul/20 03:07:46 topics=dhcp,info message="dhcp-client on lte1 got IP address 192.168.1.2"

```

**Help:** execute the command "log print detail without-paging"

**Prompt:**
- mikrotik_routeros>
- mikrotik_routeros#

### ip firewall nat print all without-paging

**Output:**
```
Flags: X - disabled, I - invalid, D - dynamic 
17:20:06 echo: system,error,critical login failure for user admin from 65.160.140.13 via ssh
 0    ;;; dmz-1: masquerade
      chain=srcnat action=masquerade src-address=!185.163.212.156/30 out-interface-list=WAN ipsec-policy=out,none 

 1    chain=dstnat action=redirect protocol=icmp src-address=192.168.1.16 dst-address=31.31.31.31 in-interface-list=dmz-1 log=no log-prefix="" 

 2 X  ;;; qsdqsdqsd
17:20:06 echo: system,error,critical login failure for user admin from 65.160.140.13 via ssh
      chain=srcnat action=accept protocol=vmtp in-interface=all-ethernet out-interface=ether4 log=no log-prefix="" 

 3 X  chain=srcnat action=accept protocol=tcp src-address-list=Supervision dst-address-list=Eqinoxe src-port=80 dst-port=8080 log=no log-prefix="" 

 4    chain=srcnat action=masquerade protocol=icmp src-address=0.0.0.0 out-interface-list=DMZ log=no log-prefix="" ipsec-policy=out,ipsec 

```

**Help:** execute the command "ip firewall nat print all without-paging"

**Prompt:**
- mikrotik_routeros>
- mikrotik_routeros#

### routing bgp peer print status without-paging

**Output:**
```
Flags: X - disabled, E - established
 0 E name="SRV-R1" instance=default remote-address=1.2.3.4 remote-as=8491 tcp-md5-key="" nexthop-choice=default multihop=no route-reflect=no hold-time=3m ttl=255 in-filter=INTERNAL-RR-IN out-filter=INTERNAL-RR-OUT address-families=ip update-source=Loopback0 default-originate=never remove-private-as=no as-override=no passive=no use-bfd=no remote-id=1.2.3.4 local-address=1.2.3.44 uptime=7w6d1h49m36s prefix-count=1836 updates-sent=331 updates-received=237257 withdrawn-sent=301 withdrawn-received=84853 remote-hold-time=1m30s used-hold-time=1m30s used-keepalive-time=30s refresh-capability=yes as4-capability=yes state=established
 
 1 E name="SRV-R2" instance=default remote-address=1.2.3.5 remote-as=8491 tcp-md5-key="" nexthop-choice=default multihop=no route-reflect=no hold-time=3m ttl=255 in-filter=INTERNAL-RR-IN out-filter=INTERNAL-RR-OUT address-families=ip update-source=Loopback0 default-originate=never remove-private-as=no as-override=no passive=no use-bfd=no remote-id=1.2.3.5 local-address=1.2.3.44 uptime=7w6d1h49m43s prefix-count=1835 updates-sent=331 updates-received=243335 withdrawn-sent=301 withdrawn-received=84680 remote-hold-time=1m30s used-hold-time=1m30s used-keepalive-time=30s refresh-capability=yes as4-capability=yes state=established

```

**Help:** execute the command "routing bgp peer print status without-paging"

**Prompt:**
- mikrotik_routeros>
- mikrotik_routeros#

### ipv6 neighbor print without-paging

**Output:**
```
Flags: R - router 
 0   address=ff02::5 interface=main mac-address=33:33:00:00:00:05 status="noarp" 

 1   address=ff02::1 interface=main mac-address=33:33:00:00:00:01 status="noarp" 

 2 R address=fe80::d7:4cff:fec1:2e32 interface=main mac-address=00:0C:42:28:79:45 status="stale" 

 3   address=2a05:c100:1d::351c interface=bridge-lan status="failed"

```

**Help:** execute the command "ipv6 neighbor print without-paging"

**Prompt:**
- mikrotik_routeros>
- mikrotik_routeros#

### ip address print

**Output:**
```
Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE
 0   10.156.1.229/30    10.156.1.228    ether4_CiscoPhone3
 1   10.152.1.229/30    10.152.1.228    ether5_KFCcisco
 2   10.160.1.229/30    10.160.1.228    ether2_BOX
 3 XI 10.100.3.200/27    10.100.3.192    bridge70

```

**Help:** execute the command "ip address print"

**Prompt:**
- mikrotik_routeros>
- mikrotik_routeros#

### interface ethernet monitor name once

**Output:**
```
                     name: ether30
                    status: no-link
          auto-negotiation: done
               advertising: 10M-half,10M-full,100M-half,100M-full,1000M-half,1000M-full
  link-partner-advertising:

```

**Help:** execute the command "interface ethernet monitor name once"

**Prompt:**
- mikrotik_routeros>
- mikrotik_routeros#

### snmp community print without-paging

**Output:**
```
17:20:06 echo: system,error,critical login failure for user admin from 65.160.140.13 via ssh
Flags: * - default, X - disabled 
 #    NAME                                                        ADDRESSES                                                                                         SECURITY   READ-ACCESS WRITE-ACCESS
17:20:06 echo: system,error,critical login failure for user admin from 65.160.140.13 via ssh
 0 *  Monitoring                                                  ::/0                                                                                              none       yes         no          

```

**Help:** execute the command "snmp community print without-paging"

**Prompt:**
- mikrotik_routeros>
- mikrotik_routeros#

### ip arp print without-paging

**Output:**
```
Flags: X - disabled, I - invalid, H - DHCP, D - dynamic, P - published, C - complete 
 #    ADDRESS         MAC-ADDRESS       INTERFACE                                                                                                                                                      
 0 D  185.163.212.158                   dmz-1-vlan                                                                                                                                                     
17:20:06 echo: system,error,critical login failure for user admin from 65.160.140.13 via ssh
 1    185.163.212.159 AF:D6:C8:F2:36:16 vlan-2                                                                                                                                                     

```

**Help:** execute the command "ip arp print without-paging"

**Prompt:**
- mikrotik_routeros>
- mikrotik_routeros#

### ip address export verbose

**Output:**
```
# jul/21/2023 09:42:42 by RouterOS 6.48.6
# software id = 1234-ABCD
 #
# model = RB750UPr2
# serial number = AB12345CD789
/ip address
add address=10.159.1.159/30 disabled=no interface=ether2 network=10.159.1.158
add address=10.80.90.5/27 comment="test comment" disabled=yes interface=eth3_vlan1 network=10.80.90.0

```

**Help:** execute the command "ip address export verbose"

**Prompt:**
- mikrotik_routeros>
- mikrotik_routeros#

### routing ospf neighbor print terse without-paging

**Output:**
```
 0 instance=default router-id=1.2.3.4 address=1.2.3.58 interface=vlan1 priority=128 dr-address=0.0.0.0 backup-dr-address=0.0.0.0 state=Full state-changes=5 ls-retransmits=0 ls-requests=0 db-summaries=0 adjacency=7w5d8h47m54s
 1 instance=default router-id=1.2.3.5 address=1.2.3.59 interface=vlan2 priority=128 dr-address=0.0.0.0 backup-dr-address=0.0.0.0 state=Full state-changes=5 ls-retransmits=0 ls-requests=0 db-summaries=0

```

**Help:** execute the command "routing ospf neighbor print terse without-paging"

**Prompt:**
- mikrotik_routeros>
- mikrotik_routeros#

### interface print terse without-paging

**Output:**
```
 0 D   name=ether1 default-name=ether1 type=ether mtu=1500 actual-mtu=1500 l2mtu=1598 max-l2mtu=2028 mac-address=12:34:56:78:90:AA last-link-up-time=aug/16/1970 13:05:43 link-downs=0
 1 DR  name=ether2_UniFi2 default-name=ether2 type=ether mtu=1500 actual-mtu=1500 l2mtu=1598 max-l2mtu=2028 mac-address=12:34:56:78:90:AB last-link-down-time=aug/17/1970 13:33:01 last-link-up-time=aug/17/1970 13:23:11 link-downs=3
 2     name=ether3_UniFi1 default-name=ether3 type=ether mtu=1500 actual-mtu=1500 l2mtu=1598 max-l2mtu=2028 mac-address=12:34:56:78:90:AC link-downs=0
 3  R  name=bridge-VLAN1 type=bridge mtu=auto actual-mtu=1500 l2mtu=1594 mac-address=12:34:56:78:90:AD last-link-up-time=aug/16/1970 13:05:35 link-downs=0
 4  X  name=bridge-VLAN2 type=bridge mac-address=12:34:56:78:90:AE link-downs=0
 5   S name=eth3_vlan1 type=vlan mtu=1500 actual-mtu=1500 l2mtu=1594 mac-address=12:34:56:78:90:AF last-link-down-time=aug/17/1970 13:33:01 last-link-up-time=aug/17/1970 13:23:11 link-downs=3
 6   S name=eth4_vlan2 type=vlan mtu=1500 actual-mtu=1500 l2mtu=1594 mac-address=12:34:56:78:90:BA link-downs=0
 7  RS name=eth4_vlan3 type=vlan mtu=1500 actual-mtu=1500 l2mtu=1594 mac-address=12:34:56:78:90:BB link-downs=0
 8 D S name=eth4_vlan4 type=vlan mtu=1500 actual-mtu=1500 l2mtu=1594 mac-address=12:34:56:78:90:BC link-downs=0
 9 DXS name=eth5_vlan5 type=vlan mtu=1500 actual-mtu=1500 l2mtu=1594 mac-address=12:34:56:78:90:BD last-link-up-time=aug/16/1970 13:05:43 link-downs=0
10  R  name=eth6_vlan6 type=vlan mtu=1500 actual-mtu=1500 l2mtu=1598 mac-address=12:34:56:78:90:BE fast-path=yes last-link-down-time=sep/08/2023 01:07:00 last-link-up-time=sep/08/2023 01:07:09 link-downs=7

```

**Help:** execute the command "interface print terse without-paging"

**Prompt:**
- mikrotik_routeros>
- mikrotik_routeros#

### ping

**Output:**
```
  SEQ HOST                                     SIZE TTL TIME  STATUS
    0 8.8.8.8                                    56  64 157ms
    1 8.8.8.8                                    56  64 64ms
    2 8.8.8.8                                    56  64 60ms
    3 8.8.8.8                                    56  64 65ms
    sent=13 received=13 packet-loss=0% min-rtt=55ms avg-rtt=67ms max-rtt=157ms

```

**Help:** execute the command "ping"

**Prompt:**
- mikrotik_routeros>
- mikrotik_routeros#

