# fortinet


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
- fortinet>

### get system interface physical

**Output:**
```
== [onboard]
        ==[dmz1]
                mode: static
                ip: 0.0.0.0 0.0.0.0
                ipv6: ::/0
                status: down
                speed: n/a
        ==[dmz2]
                mode: static
                ip: 0.0.0.0 0.0.0.0
                ipv6: ::/0
                status: down
                speed: n/a
        ==[mgmt]
                mode: static
                ip: 1.2.3.4 255.255.255.248
                ipv6: ::/0
                status: up
                speed: 1000Mbps (Duplex: full)
        ==[port1]
                mode: static
                ip: 2.3.4.5 255.255.255.240
                ipv6: ::/0
                status: up
                speed: 1000Mbps (Duplex: full)
        ==[port2]
                mode: static
                ip: 0.0.0.0 0.0.0.0
                ipv6: ::/0
                status: up
                speed: 1000Mbps (Duplex: full)
        ==[port3]
                mode: static
                ip: 66.51.24.44 255.255.255.248
                ipv6: ::/0
                status: up
                speed: 1000Mbps (Duplex: full)
        ==[port4]
                mode: static
                ip: 192.168.111.1 255.255.255.0
                ipv6: ::/0
                status: up
                speed: 1000Mbps (Duplex: full)
        ==[port5]
                mode: static
                ip: 3.4.5.6 255.255.255.240
                ipv6: ::/0
                status: up
                speed: 1000Mbps (Duplex: full)
        ==[port6]
                mode: static
                ip: 0.0.0.0 0.0.0.0
                ipv6: ::/0
                status: up
                speed: 1000Mbps (Duplex: full)
        ==[port7]
                mode: static
                ip: 0.0.0.0 0.0.0.0
                ipv6: ::/0
                status: down
                speed: n/a
        ==[port8]
                mode: static
                ip: 0.0.0.0 0.0.0.0
                ipv6: ::/0
                status: down
                speed: n/a
        ==[port9]
                mode: static
                ip: 0.0.0.0 0.0.0.0
                ipv6: ::/0
                status: down
                speed: n/a
        ==[port10]
                mode: static
                ip: 0.0.0.0 0.0.0.0
                ipv6: ::/0
                status: down
                speed: n/a
        ==[port11]
                mode: static
                ip: 0.0.0.0 0.0.0.0
                ipv6: ::/0
                status: down
                speed: n/a
        ==[port12]
                mode: static
                ip: 0.0.0.0 0.0.0.0
                ipv6: ::/0
                status: down
                speed: n/a
        ==[port13]
                mode: static
                ip: 0.0.0.0 0.0.0.0
                ipv6: ::/0
                status: down
                speed: n/a
        ==[port14]
                mode: static
                ip: 0.0.0.0 0.0.0.0
                ipv6: ::/0
                status: down
                speed: n/a
        ==[port15]
                mode: static
                ip: 0.0.0.0 0.0.0.0
                ipv6: ::/0
                status: down
                speed: n/a
        ==[port16]
                mode: static
                ip: 0.0.0.0 0.0.0.0
                ipv6: ::/0
                status: up
                speed: 1000Mbps (Duplex: full)
        ==[wan1]
                mode: static
                ip: 0.0.0.0 0.0.0.0
                ipv6: ::/0
                status: down
                speed: n/a
        ==[wan2]
                mode: static
                ip: 0.0.0.0 0.0.0.0
                ipv6: ::/0
                status: down
                speed: n/a
        ==[modem]
                mode: pppoe
                ip: 0.0.0.0 0.0.0.0
                ipv6: ::/0
                status: down
                speed: n/a

```

**Help:** execute the command "get system interface physical"

**Prompt:**
- fortinet>
- fortinet#

### get system status

**Output:**
```
Version: FortiGate-1500D v6.0.7,build0302,191112 (GA)
Virus-DB: 16.00560(2012-10-19 08:31)
Extended DB: 1.00000(2018-04-09 18:07)
Extreme DB: 1.00000(2018-04-09 18:07)
IPS-DB: 6.00741(2015-12-01 02:30)
IPS-ETDB: 15.00748(2019-12-19 04:16)
 APP-DB: 15.00756(2020-01-10 02:10)
INDUSTRIAL-DB: 15.00756(2020-01-10 02:10)
 Serial-Number: FG1K501234567890
IPS Malicious URL Database: 2.00521(2020-01-10 04:24)
Botnet DB: 1.00000(2012-05-28 22:51)
BIOS version: 05000006
System Part-Number: P12917-08
Log hard disk: Available
Hostname: MYCOOLEFIREWALLNAME 
Operation Mode: NAT
Current virtual domain: root
Max number of virtual domains: 10
Virtual domains status: 7 in NAT mode, 1 in TP mode
Virtual domain configuration: enable
FIPS-CC mode: disable
Current HA mode: a-p, master
Cluster uptime: 102 days, 22 hours, 39 minutes, 22 seconds
Cluster state change time: 2019-12-22 05:24:41
Branch point: 0302
Release Version Information: GA
FortiOS x86-64: Yes
System time: Fri Jan 10 23:10:02 2020

```

**Help:** execute the command "get system status"

**Prompt:**
- fortinet>
- fortinet#

### get system ha status

**Output:**
```
HA Health Status: OK
Model: FortiGate-600E
Mode: HA A-P
Group: 5
 Debug: 0
Cluster Uptime: 36 days 22:20:40
Cluster state change time: 2020-12-02 22:40:46
Master selected using:
    <2020/12/02 22:40:46> FG6H0Exxxxxxxxxx is selected as the master because it has the largest value of override priority.
 ses_pickup: enable, ses_pickup_delay=disable
override: enable
Configuration Status:
    FG6H0Exxxxxxxxxx(updated 1 seconds ago): in-sync
    FG6H0Eyyyyyyyyyy(updated 3 seconds ago): in-sync
System Usage stats:
    FG6H0Exxxxxxxxxx(updated 1 seconds ago):
        sessions=692, average-cpu-user/nice/system/idle=0%/0%/0%/100%, memory=25%
    FG6H0Eyyyyyyyyyy(updated 3 seconds ago):
        sessions=303, average-cpu-user/nice/system/idle=0%/0%/0%/100%, memory=23%
HBDEV stats:
    FG6H0Exxxxxxxxxx(updated 1 seconds ago):
        ha: physical/1000auto, up, rx-bytes/packets/dropped/errors=13086049757/51933375/0/0, tx=93993034207/102822032/0/0
    FG6H0Eyyyyyyyyyy(updated 3 seconds ago):
        ha: physical/1000auto, up, rx-bytes/packets/dropped/errors=93993244676/102822709/0/0, tx=13085729171/51934319/0/0
 MONDEV stats:
    FG6H0Exxxxxxxxxx(updated 1 seconds ago):
        x1: physical/10000full, up, rx-bytes/packets/dropped/errors=166373929414532/122946162431/0/0, tx=51746004768400/50869381172/0/0
        x2: physical/10000full, up, rx-bytes/packets/dropped/errors=49656542180617/50909579016/0/337, tx=165637609617619/122981014444/0/0
    FG6H0Eyyyyyyyyyy(updated 3 seconds ago):
        x1: physical/10000full, up, rx-bytes/packets/dropped/errors=409699822/4202261/0/0, tx=0/0/0/0
        x2: physical/10000full, up, rx-bytes/packets/dropped/errors=12425072765/11621697/0/0, tx=0/0/0/0
Master: fgt-600e_a, FG6H0Exxxxxxxxxx, HA cluster index = 1
Slave : fgt-600e_b, FG6H0Eyyyyyyyyyy, HA cluster index = 0
number of vcluster: 1
 vcluster 1: work 169.254.0.2
Master: FG6H0Exxxxxxxxxx, HA operating index = 0
Slave : FG6H0Eyyyyyyyyyy, HA operating index = 1

```

**Help:** execute the command "get system ha status"

**Prompt:**
- fortinet>
- fortinet#

### get router info bgp summary

**Output:**
```
BGP router identifier 85.31.8.8, local AS number 65302
BGP table version is 13
1 BGP AS-PATH entries
0 BGP community entries

Neighbor        V         AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
10.204.35.84   4      65302   43173   43182        0    0    0 09w3d01h Active     
10.205.35.95   4      65302  107081  107168       12    0    0 05:48:47        1
169.132.250.17  4       4224       0       0        0    0    0    never Idle       
169.132.250.21  4       4224       0       0        0    0    0    never Idle       

 Total number of neighbors 4


```

**Help:** execute the command "get router info bgp summary"

**Prompt:**
- fortinet>
- fortinet#

### get system interface

**Output:**
```
== [ ha ]
name: ha   mode: static    management-ip: 0.0.0.0 0.0.0.0   ip: 0.0.0.0 0.0.0.0   status: up    netbios-forward: disable    type: physical   netflow-sampler: disable    sflow-sampler: disable    src-check: enable    explicit-web-proxy: disable    explicit-ftp-proxy: disable    proxy-captive-portal: disable    mtu-override: disable    wccp: disable    drop-overlapped-fragment: disable    drop-fragment: disable
== [ mgmt ]
name: mgmt   mode: static    management-ip: 1.2.3.4 255.255.255.248   ip: 1.2.3.4 255.255.255.248   status: up    netbios-forward: disable    type: physical   netflow-sampler: disable    sflow-sampler: disable    src-check: enable    explicit-web-proxy: disable    explicit-ftp-proxy: disable    proxy-captive-portal: disable    mtu-override: disable    wccp: disable    drop-overlapped-fragment: disable    drop-fragment: disable
== [ port1 ]
name: port1   mode: static    management-ip: 0.0.0.0 0.0.0.0   ip: 0.0.0.0 0.0.0.0   status: up    netbios-forward: disable    type: physical   netflow-sampler: disable    sflow-sampler: disable    src-check: enable    explicit-web-proxy: disable    explicit-ftp-proxy: disable    proxy-captive-portal: disable    mtu-override: disable    wccp: disable    drop-overlapped-fragment: disable    drop-fragment: disable
== [ port2 ]
name: port2   mode: static    management-ip: 0.0.0.0 0.0.0.0   ip: 0.0.0.0 0.0.0.0   status: up    netbios-forward: disable    type: physical   netflow-sampler: disable    sflow-sampler: disable    src-check: enable    explicit-web-proxy: disable    explicit-ftp-proxy: disable    proxy-captive-portal: disable    mtu-override: disable    wccp: disable    drop-overlapped-fragment: disable    drop-fragment: disable
== [ s1 ]
 name: s1   mode: static    management-ip: 0.0.0.0 0.0.0.0   ip: 0.0.0.0 0.0.0.0   status: up    netbios-forward: disable    type: physical   netflow-sampler: disable    sflow-sampler: disable    src-check: enable    explicit-web-proxy: disable    explicit-ftp-proxy: disable    proxy-captive-portal: disable    mtu-override: disable    wccp: disable    drop-overlapped-fragment: disable    drop-fragment: disable
== [ vw1 ]
name: vw1   status: up    type: physical   netflow-sampler: disable    sflow-sampler: disable    src-check: enable    mtu-override: disable    wccp: disable    drop-overlapped-fragment: disable    drop-fragment: disable
 == [ x1 ]
name: x1   mode: static    management-ip: 0.0.0.0 0.0.0.0   ip: 0.0.0.0 0.0.0.0   status: up    netbios-forward: disable    type: physical   netflow-sampler: disable    sflow-sampler: disable    src-check: enable    explicit-web-proxy: disable    explicit-ftp-proxy: disable    proxy-captive-portal: disable    mtu-override: disable    wccp: disable    drop-overlapped-fragment: disable    drop-fragment: disable
== [ modem ]
name: modem   mode: pppoe    management-ip: 0.0.0.0 0.0.0.0   ip: 0.0.0.0 0.0.0.0   netbios-forward: disable    type: physical   netflow-sampler: disable    sflow-sampler: disable    src-check: enable    proxy-captive-portal: disable    mtu-override: disable    wccp: disable    drop-overlapped-fragment: disable    drop-fragment: disable
== [ ssl.root ]
name: ssl.root   ip: 0.0.0.0 0.0.0.0   status: up    netbios-forward: disable    type: tunnel   netflow-sampler: disable    sflow-sampler: disable    src-check: enable    explicit-web-proxy: disable    explicit-ftp-proxy: disable    proxy-captive-portal: disable    wccp: disable
== [ npu0_vlink0 ]
name: npu0_vlink0   mode: static    management-ip: 0.0.0.0 0.0.0.0   ip: 0.0.0.0 0.0.0.0   status: up    netbios-forward: disable    type: physical   netflow-sampler: disable    sflow-sampler: disable    src-check: enable    explicit-web-proxy: disable    explicit-ftp-proxy: disable    proxy-captive-portal: disable    wccp: disable    drop-overlapped-fragment: disable    drop-fragment: disable
== [ fortilink ]
name: fortilink   mode: static    management-ip: 0.0.0.0 0.0.0.0   ip: 169.254.1.1 255.255.255.0   status: up    netbios-forward: disable    type: aggregate   netflow-sampler: disable    sflow-sampler: disable    src-check: enable    explicit-web-proxy: disable    explicit-ftp-proxy: disable    proxy-captive-portal: disable    mtu-override: disable    wccp: disable    drop-overlapped-fragment: disable    drop-fragment: disable
== [ x1.113 ]
name: x1.113   mode: static    management-ip: 0.0.0.0 0.0.0.0   ip: 2.3.4.5 255.255.255.0   status: up    netbios-forward: disable    type: vlan   netflow-sampler: disable    sflow-sampler: disable    src-check: enable    explicit-web-proxy: disable    explicit-ftp-proxy: disable    proxy-captive-portal: disable    mtu-override: disable    wccp: disable    drop-overlapped-fragment: disable    drop-fragment: disable
== [ loopback.0 ]
name: loopback.0   management-ip: 0.0.0.0 0.0.0.0   ip: 10.0.0.100 255.255.255.255   status: up    type: loopback   netflow-sampler: disable    sflow-sampler: disable    src-check: enable    explicit-web-proxy: disable    explicit-ftp-proxy: disable    proxy-captive-portal: disable
== [ VPN-TUN ]
name: VPN-TUN   ip: 3.4.5.6 255.255.255.255   status: up    netbios-forward: disable    type: tunnel   netflow-sampler: disable    sflow-sampler: disable    src-check: enable    explicit-web-proxy: disable    explicit-ftp-proxy: disable    proxy-captive-portal: disable    wccp: disable

```

**Help:** execute the command "get system interface"

**Prompt:**
- fortinet>
- fortinet#

### get system arp

**Output:**
```
Address           Age(min)   Hardware Addr      Interface
192.168.1.4       0          b0:a8:6e:01:61:81 lan
192.168.1.110     0          3c:9b:d6:66:52:ab lan
192.168.1.111     0          18:64:72:c9:02:d2 lan
192.168.1.114     4          40:cb:c0:ce:81:85 lan

```

**Help:** execute the command "get system arp"

**Prompt:**
- fortinet>
- fortinet#

