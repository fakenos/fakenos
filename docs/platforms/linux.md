# linux


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
- linux$

### ip vrf show

**Output:**
```
Name              Table
-----------------------
vrf-blue            10
vrf-red             20

```

**Help:** execute the command "ip vrf show"

**Prompt:**
- linux$
- linux#

### ip address show

**Output:**
```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: ens32: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:0c:29:56:07:1b brd ff:ff:ff:ff:ff:ff
    inet 192.168.131.128/24 brd 192.168.131.255 scope global dynamic ens32
       valid_lft 1307sec preferred_lft 1307sec
3: gpd0: <POINTOPOINT,MULTICAST,NOARP,UP,LOWER_UP> mtu 1400 qdisc fq_codel state UNKNOWN group default qlen 500
    link/none
    inet 10.20.20.12/32 scope global gpd0
       valid_lft forever preferred_lft forever
4: br-218f5e637867: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default
    link/ether 02:42:5d:d7:c2:c1 brd ff:ff:ff:ff:ff:ff
    inet 172.21.0.1/16 brd 172.21.255.255 scope global br-218f5e637867
       valid_lft forever preferred_lft forever
5: vrf-blue: <NOARP,MASTER,UP,LOWER_UP> mtu 65575 qdisc noqueue state UP group default qlen 1000
    link/ether ee:be:e9:28:70:69 brd ff:ff:ff:ff:ff:ff
6: brblue: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master vrf-blue state UNKNOWN group default qlen 1000
    link/ether 66:37:23:9b:9e:e4 brd ff:ff:ff:ff:ff:ff
    inet 10.0.0.1/24 scope global brblue
       valid_lft forever preferred_lft forever
    inet 192.168.0.1/25 scope global brred
       valid_lft forever preferred_lft forever

```

**Help:** execute the command "ip address show"

**Prompt:**
- linux$
- linux#

### ip link show

**Output:**
```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
 2: ens32: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 00:0c:29:56:07:1b brd ff:ff:ff:ff:ff:ff
 3: gpd0: <POINTOPOINT,MULTICAST,NOARP,UP,LOWER_UP> mtu 1400 qdisc fq_codel state UNKNOWN mode DEFAULT group default qlen 500
    link/none
4: br-218f5e637867: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default
    link/ether 02:42:5d:d7:c2:c1 brd ff:ff:ff:ff:ff:ff
5: vrf-blue: <NOARP,MASTER,UP,LOWER_UP> mtu 65575 qdisc noqueue state UP mode DEFAULT group default qlen 1000
    link/ether ee:be:e9:28:70:69 brd ff:ff:ff:ff:ff:ff
 6: vrf-red: <NOARP,MASTER,UP,LOWER_UP> mtu 65575 qdisc noqueue state UP mode DEFAULT group default qlen 1000
    link/ether d6:a6:dd:0d:d5:f9 brd ff:ff:ff:ff:ff:ff
 7: brblue: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master vrf-blue state UNKNOWN mode DEFAULT group default qlen 1000
    link/ether 66:37:23:9b:9e:e4 brd ff:ff:ff:ff:ff:ff
8: brred: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master vrf-red state UNKNOWN mode DEFAULT group default qlen 1000
    link/ether da:ca:17:97:f5:34 brd ff:ff:ff:ff:ff:ff

```

**Help:** execute the command "ip link show"

**Prompt:**
- linux$
- linux#

### arp -a

**Output:**
```
? (192.168.13.197) at 00:04:4b:cc:9c:ba [ether] on eth1.100
? (192.168.10.100) at <incomplete> on eth1.10
? (192.168.13.252) at 5c:e2:8c:fc:a4:74 [ether] on eth1.100
esxi (192.168.13.5) at 00:e0:67:05:9d:5a [ether] on eth1.100
 ? (192.168.13.253) at dc:f7:19:cd:d6:c4 [ether] on eth1.100
? (192.168.123.199) at 00:0f:c9:0e:c8:ec [ether] on eth0.21
? (192.168.10.52) at <incomplete> on eth1.10
? (192.168.10.7) at 00:0c:29:02:3b:93 [ether] on eth1.10
? (192.168.10.249) at 00:0c:29:bb:5f:a2 [ether] on eth1.10

```

**Help:** execute the command "arp -a"

**Prompt:**
- linux$
- linux#

### ip route show

**Output:**
```
default via 10.0.0.4 dev brblue
unreachable default metric 4278198272
 broadcast 10.0.0.0 dev brblue proto kernel scope link src 10.0.0.1
10.0.0.0/24 dev brblue proto kernel scope link src 10.0.0.1
local 10.0.0.1 dev brblue proto kernel scope host src 10.0.0.1
broadcast 10.0.0.255 dev brblue proto kernel scope link src 10.0.0.1
192.168.0.0/24 via 10.0.0.2 dev brblue
192.168.131.2 dev ens32 proto dhcp scope link src 192.168.131.128 metric 100

```

**Help:** execute the command "ip route show"

**Prompt:**
- linux$
- linux#

