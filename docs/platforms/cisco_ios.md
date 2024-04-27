# cisco_ios


!!! warning
    This is automatically generated. In case of any issues, 
    please refer to the source code or, even better, 
    open an issue on the GitHub repository. Thanks! 🤗📖
## Platforms:
-  
## Commands

### enable

**Output:**
```
null
```

**Help:** enter enable mode

**Prompt:**
- cisco_ios>

### show rep topology

**Output:**
```
REP Segment 1
BridgeName       PortName   Edge Role
---------------- ---------- ---- ----
Switch01          Fa0/2      Pri  Alt
Switch02          Fa1/0/23   Sec  Open
```

**Help:** execute the command "show rep topology"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip mroute

**Output:**
```
IP Multicast Forwarding is not enabled.
IP Multicast Routing Table
 Flags: D - Dense, S - Sparse, B - Bidir Group, s - SSM Group, C - Connected,
       L - Local, P - Pruned, R - RP-bit set, F - Register flag,
       T - SPT-bit set, J - Join SPT, M - MSDP created entry, E - Extranet,
       X - Proxy Join Timer Running, A - Candidate for MSDP Advertisement,
       U - URD, I - Received Source Specific Host Report,
       Z - Multicast Tunnel, z - MDT-data group sender,
       Y - Joined MDT-data group, y - Sending to MDT-data group,
       V - RD & Vector, v - Vector
Outgoing interface flags: H - Hardware switched, A - Assert winner
 Timers: Uptime/Expires
 Interface state: Interface, Next-Hop or VCD, State/Mode

```

**Help:** execute the command "show ip mroute"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip bgp

**Output:**
```
BGP table version is 17, local router ID is 10.0.0.0
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
              x best-external, a additional-path, c RIB-compressed, 
              t secondary path, 
Origin codes: i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
 *>   10.1.0.0/16      0.0.0.0                  0         32768 i
 *>   10.2.0.0/16      0.0.0.0                  0         32768 i
 *>   10.3.0.0/16      0.0.0.0                  0         32768 i
 *>   10.4.0.0/16      0.0.0.0                  0         32768 i
 *>i  10.11.0.0/16     10.0.0.1                 0    100      0 i
 *>i  10.12.0.0/16     10.0.0.1                 0    100      0 i
 *>i  10.13.0.0/16     10.0.0.1                 0    100      0 i
 *>i  10.14.0.0/16     10.0.0.1                 0    100      0 i

```

**Help:** execute the command "show ip bgp"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show module

**Output:**
```
Switch  Ports    Model                Serial No.   MAC address     Hw Ver.       Sw Ver. 
------  -----   ---------             -----------  --------------  -------       --------
 1       28     C9200L-24T-4G-E       3YEEQEY2MND  dc8c.5322.19c6  V01           16.12.6  
 2       28     C9200L-24T-4G-E       CBC7DQFNB7F  dc8c.aaa0.1b77  V01           16.12.6  

```

**Help:** execute the command "show module"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show crypto pki certificates

**Output:**
```
Certificate
  Status: Available
  Certificate Serial Number (hex): 1234567890ABCDEFGHIJK
  Certificate Usage: General Purpose
  Issuer: 
    e=email.address@domain.com
    cn=CommonName
    ou=OrganizationalUnit
    o=Organization
    l=Locality
    st=StateOrProvinceName
    c=CountryName
  Subject:
    Name: ROUTERNAME.domain.com
    Serial Number: 1234ABCD
    hostname=ROUTERNAME.domain.com
    serialNumber=1234ABCD
  CRL Distribution Points: 
    http://cdp.domain.com/crl/issuing-ca.crl
  Validity Date: 
    start date: 09:17:52 UTC Jun 22 2022
    end   date: 09:17:52 UTC Jun 22 2023
    renew date: 09:19:52 UTC Apr 10 2023
  Associated Trustpoints: caserver.domain.com 
  Storage: nvram:certfile.cer

CA Certificate
  Status: Available
  Certificate Serial Number (hex): ABCDEFGHIJK1234567890
  Certificate Usage: Signature
  Issuer: 
    e=email.address@domain.com
    cn=CommonName
    ou=OrganizationalUnit
    o=Organization
    l=Locality
    st=StateOrProvinceName
    c=CountryName
  Subject: 
    e=email.address@domain.com
    cn=CommonName
    ou=OrganizationalUnit
    o=Organization
    l=Locality
    st=StateOrProvinceName
    c=CountryName
  CRL Distribution Points: 
    http://cdp.domain.com/crl/issuing-ca.crl
  Validity Date: 
    start date: 00:00:00 UTC Nov 9 2018
    end   date: 00:00:00 UTC Nov 9 2028
  Associated Trustpoints: caserver.domain.com
  Storage: nvram:certfile.cer

CA Certificate
  Status: Available
  Certificate Serial Number (hex): 12345ABCDEFGHIJK67890
  Certificate Usage: Signature
  Issuer: 
    e=email.address@domain.com
    cn=CommonName
    ou=OrganizationalUnit
    o=Organization
    l=Locality
    st=StateOrProvinceName
    c=CountryName
  Subject: 
    e=email.address@domain.com
    cn=CommonName
    ou=OrganizationalUnit
    o=Organization
    l=Locality
    st=StateOrProvinceName
    c=CountryName
  Validity Date: 
    start date: 00:00:00 UTC Nov 5 2018
    end   date: 00:00:00 UTC Nov 5 2038
  Associated Trustpoints: ROOT-CA 
  Storage: nvram:certfile.cer

```

**Help:** execute the command "show crypto pki certificates"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip prefix-list

**Output:**
```
ip prefix-list OSPF_Redist: 2 entries
   seq 5 deny 10.0.0.0/24
   seq 10 permit 0.0.0.0/0 le 32
   seq 15 deny 10.0.0.0/8 ge 10 le 20

```

**Help:** execute the command "show ip prefix-list"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show file systems

**Output:**
```
File Systems:

       Size(b)       Free(b)      Type  Flags  Prefixes
             -             -    opaque     rw   system:
             -             -    opaque     rw   tmpsys:
    1651314688    1561067520      disk     rw   crashinfo:
*  11353194496    9936510976      disk     rw   flash:
    3846701056    3758395392      disk     ro   webui:
             -             -    opaque     rw   null:
             -             -    opaque     ro   tar:
             -             -   network     rw   tftp:
       2097152       2057602     nvram     rw   nvram:
             -             -   network     rw   rcp:
             -             -   network     rw   http:
             -             -   network     rw   ftp:
             -             -   network     rw   scp:
             -             -   network     rw   sftp:
             -             -   network     rw   https:
             -             -    opaque     ro   cns:

```

**Help:** execute the command "show file systems"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show isdn status

**Output:**
```
Global ISDN Switchtype = primary-ni
ISDN Serial0/2/0:23 interface
        dsl 0, interface ISDN Switchtype = primary-ni
    Layer 1 Status:
        ACTIVE
    Layer 2 Status:
        TEI = 0, Ces = 1, SAPI = 0, State = MULTIPLE_FRAME_ESTABLISHED
    Layer 3 Status:
        1 Active Layer 3 Call(s)
        CCB:callid=97E3, sapi=0, ces=0, B-chan=23, calltype=VOICE
    Active dsl 0 CCBs = 1
    The Free Channel Mask:  0x803FFFFF
    Number of L2 Discards = 0, L2 Session ID = 10
ISDN Serial0/2/1:23 interface
        dsl 1, interface ISDN Switchtype = primary-ni
    Layer 1 Status:
        ACTIVE
    Layer 2 Status:
        TEI = 0, Ces = 1, SAPI = 0, State = MULTIPLE_FRAME_ESTABLISHED
    Layer 3 Status:
        0 Active Layer 3 Call(s)
    Active dsl 1 CCBs = 0
    The Free Channel Mask:  0x807FFFFF
    Number of L2 Discards = 0, L2 Session ID = 6
ISDN Serial0/3/0:23 interface
        dsl 2, interface ISDN Switchtype = primary-ni
    Layer 1 Status:
        ACTIVE
    Layer 2 Status:
        TEI = 0, Ces = 1, SAPI = 0, State = MULTIPLE_FRAME_ESTABLISHED
    Layer 3 Status:
        0 Active Layer 3 Call(s)
    Active dsl 2 CCBs = 0
    The Free Channel Mask:  0x807FFFFF
    Number of L2 Discards = 0, L2 Session ID = 1
    Total Allocated ISDN CCBs = 1

```

**Help:** execute the command "show isdn status"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show interface link

**Output:**
```
Port    Name               Down Time        Down Since
Gi1/1                      37 weeks, 3 days, 5 hours, 52 minutes 18 secs      08:07:10  Mon Feb 14 2022
Gi1/6                      15 weeks, 11 minutes 57 secs      13:47:31  Thu Jul 21 2022
Gi1/10   Fitness           10 weeks, 5 days, 20 hours, 26 minutes 38 secs      17:32:50  Fri Aug 19 2022
Gi1/11                     00 secs
Gi1/24   SV-Service-Office 1 year , 25 weeks, 2 days, 4 hours, 17 minutes 24 secs      09:42:04  Mon May 10 2021
Gi1/48   WERFBZW5236KARA   00 secs
Gi2/3                      00 secs
Gi2/6                      4 hours, 58 minutes 17 secs      09:01:11  Thu Nov 3 2022
Gi2/8    Fitness           00 secs
Gi2/9    Fit area          00 secs
Gi2/10   Guest access      00 secs
Gi2/11                     3 weeks, 1 day, 23 hours, 49 minutes 40 secs      14:09:48  Tue Oct 11 2022
Gi2/12                     21 hours, 17 minutes 27 secs      16:42:01  Wed Nov 2 2022
Gi2/17                     1 week, 1 day, 22 hours, 51 minutes 28 secs      15:08:00  Tue Oct 25 2022
Gi2/23                     5 weeks, 1 day, 23 hours, 22 minutes 02 secs      14:37:26  Tue Sep 27 2022
Gi2/25                     00 secs
Gi2/27                     1 year , 25 weeks, 2 days, 4 hours, 17 minutes 24 secs      09:42:04  Mon May 10 2021
Gi2/29                     43 weeks, 3 days, 2 hours, 18 minutes 11 secs      11:41:17  Mon Jan 3 2022
Gi4/47   DOFKYLW5823AP83   00 secs
Tw1/0/48   WERFBZW5236KARA   00 secs
Te6/1    ICN-DOFKYLW5823TV000 secs
```

**Help:** execute the command "show interface link"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip eigrp neighbors

**Output:**
```
EIGRP-IPv4 Neighbors for AS(545)
H   Address                 Interface              Hold Uptime   SRTT   RTO  Q  Seq
                                                   (sec)         (ms)       Cnt Num
2   10.205.205.11           Vl624                    10 3w2d        4   100  0  13336
0   10.230.205.27           Vl942                    13 9w4d        1   100  0  35073
1   10.230.205.23           Vl942                    13 15w2d       1   100  0  1051652

```

**Help:** execute the command "show ip eigrp neighbors"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show vrf detail

**Output:**
```
VRF Management (VRF Id = 1); default RD <not set>; default VPNID <not set>
  Old CLI format, supports IPv4 only
  Flags: 0x8
  Interfaces:
    Gi1                     
Address family ipv4 unicast (Table ID = 0x1):
  Flags: 0x0
  No Export VPN route-target communities
  No Import VPN route-target communities
  No import route-map
  No global export route-map
  No export route-map
  VRF label distribution protocol: not configured
  VRF label allocation mode: per-prefix
Address family ipv6 unicast not active
Address family ipv4 multicast not active
Address family ipv6 multicast not active

VRF testr (VRF Id = 2); default RD 65000:42; default VPNID <not set>
  Old CLI format, supports IPv4 only
  Flags: 0xC
  No interfaces
Address family ipv4 unicast (Table ID = 0x2):
  Flags: 0x0
  Export VPN route-target communities
    RT:65000:42             
  Import VPN route-target communities
    RT:65000:43 
    RT:65000:44             
  No import route-map
  No global export route-map
  No export route-map
  VRF label distribution protocol: not configured
  VRF label allocation mode: per-prefix
Address family ipv6 unicast not active
 Address family ipv4 multicast not active
Address family ipv6 multicast not active

VRF test2 (VRF Id = 3); default RD <not set>; default VPNID <not set>
  Description: test2 description
  Old CLI format, supports IPv4 only
  Flags: 0x8
  No interfaces
Address family ipv4 unicast (Table ID = 0x3):
  Flags: 0x0
  No Export VPN route-target communities
  No Import VPN route-target communities
  No import route-map
  No global export route-map
  No export route-map
  VRF label distribution protocol: not configured
  VRF label allocation mode: per-prefix
Address family ipv6 unicast not active
Address family ipv4 multicast not active
Address family ipv6 multicast not active


```

**Help:** execute the command "show vrf detail"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show vlans

**Output:**
```
VLAN ID: 1 (IEEE 802.1Q Encapsulation)
 This is configured as native Vlan for the following interface(s) :
GigabitEthernet0/0/0    Native-vlan Tx-type: Untagged
GigabitEthernet0/0/1    Native-vlan Tx-type: Untagged
TenGigabitEthernet0/1/0    Native-vlan Tx-type: Untagged
   Protocols Configured:          Received:        Transmitted:
                     IP         2192679791          2184903327
 VLAN trunk interfaces for VLAN ID 1:
GigabitEthernet0/0/0
GigabitEthernet0/0/0 (1)
                     IP: 10.0.2.86
      Total 9958707 packets, 3870632644 bytes input
      Total 943133 packets, 357934647 bytes output
      Total 0 oversubscription packet drops
GigabitEthernet0/0/1
GigabitEthernet0/0/1 (1)
                     IP: 10.0.2.225
      Total 10048435 packets, 3854174982 bytes input
      Total 942969 packets, 357871090 bytes output
      Total 0 oversubscription packet drops
TenGigabitEthernet0/1/0
TenGigabitEthernet0/1/0 (1)
                     IP: 10.252.212.189
      Total 129733168 packets, 42443829815 bytes input
      Total 793182 packets, 36432663 bytes output
      Total 0 oversubscription packet drops
VLAN ID: 3141 (IEEE 802.1Q Encapsulation)
   Protocols Configured:          Received:        Transmitted:
                     IP       144695187064         11111892659
VLAN trunk interfaces for VLAN ID 3141:
GigabitEthernet0/0/0.3141
GigabitEthernet0/0/0.3141 (3141)
                     IP: 10.0.2.94
      Total 143692091694 packets, 80311269603551 bytes input
      Total 10027923256 packets, 1021853446362 bytes output
      Total 0 oversubscription packet drops
GigabitEthernet0/0/1.3141
GigabitEthernet0/0/1.3141 (3141)
                     IP: 10.0.2.233
      Total 1003101498 packets, 70246942495 bytes input
      Total 1083981803 packets, 122490850063 bytes output
      Total 0 oversubscription packet drops

VLAN ID: 100 (IEEE 802.1Q Encapsulation)
   Protocols Configured:          Received:        Transmitted:
                     IP         9082316335        142649676727
VLAN trunk interfaces for VLAN ID 100:
TenGigabitEthernet0/1/0.100
TenGigabitEthernet0/1/0.100 (100)
                     IP: 10.0.2.149
      Total 13377307173 packets, 915523477657 bytes input
      Total 142649815357 packets, 80766632402700 bytes output
      Total 0 oversubscription packet drops

VLAN ID: 101 (IEEE 802.1Q Encapsulation)
   Protocols Configured:          Received:        Transmitted:
                     IP           10049693              624835
VLAN trunk interfaces for VLAN ID 101:
TenGigabitEthernet0/1/0.101
TenGigabitEthernet0/1/0.101 (101)
                     IP: 10.0.2.145
      Total 10063958 packets, 711071685 bytes input
      Total 2563528 packets, 155505178 bytes output
      Total 0 oversubscription packet drops

VLAN ID: 102 (IEEE 802.1Q Encapsulation)
   Protocols Configured:          Received:        Transmitted:
                     IP            7643307              501212
VLAN trunk interfaces for VLAN ID 102:
TenGigabitEthernet0/1/0.102
TenGigabitEthernet0/1/0.102 (102)
                     IP: 10.0.2.153
      Total 7653711 packets, 536047078 bytes input
      Total 2107241 packets, 127679557 bytes output
      Total 0 oversubscription packet drops

VLAN ID: 103 (IEEE 802.1Q Encapsulation)
   Protocols Configured:          Received:        Transmitted:
                     IP           16964732             1016648
VLAN trunk interfaces for VLAN ID 103:
TenGigabitEthernet0/1/0.103
TenGigabitEthernet0/1/0.103 (103)
                     IP: 10.0.2.157
      Total 16988470 packets, 1189442738 bytes input
      Total 1155284 packets, 80642016 bytes output
      Total 0 oversubscription packet drops

VLAN ID: 104 (IEEE 802.1Q Encapsulation)
   Protocols Configured:          Received:        Transmitted:
                     IP           85800249            93390973
VLAN trunk interfaces for VLAN ID 104:
TenGigabitEthernet0/1/0.104
TenGigabitEthernet0/1/0.104 (104)
                     IP: 10.0.231.229
      Total 85813215 packets, 55432999639 bytes input
      Total 93432033 packets, 10854590863 bytes output
      Total 0 oversubscription packet drops

VLAN ID: 3228 (IEEE 802.1Q Encapsulation)
   Protocols Configured:          Received:        Transmitted:
                     IP         2039324150          2128294473
VLAN trunk interfaces for VLAN ID 3228:
GigabitEthernet0/0/0.3228
GigabitEthernet0/0/0.3228 (3228)
                     IP: 10.0.231.242
      Total 976946299 packets, 73982774167 bytes input
      Total 1279353761 packets, 207713874159 bytes output
      Total 0 oversubscription packet drops
GigabitEthernet0/0/1.3228
GigabitEthernet0/0/1.3228 (3228)
                     IP: 10.0.231.233
      Total 1062383291 packets, 101338350618 bytes input
      Total 848951745 packets, 62850598908 bytes output
      Total 0 oversubscription packet drops
VLAN ID: 3000 (IEEE 802.1Q Encapsulation)
   Protocols Configured:          Received:        Transmitted:
                     IP         1965781161          1965862226
VLAN trunk interfaces for VLAN ID 3000:
GigabitEthernet0/0/0.3000
GigabitEthernet0/0/0.3000 (3000)
                     IP: 10.0.2.90
      Total 962685934 packets, 67415074722 bytes input
      Total 962758529 packets, 71277047385 bytes output
      Total 0 oversubscription packet drops
GigabitEthernet0/0/1.3000
GigabitEthernet0/0/1.3000 (3000)
                     IP: 10.0.2.229
      Total 1003101351 packets, 70246933000 bytes input
      Total 1003116090 packets, 74260358613 bytes output
      Total 0 oversubscription packet drops
VLAN ID: 3017 (IEEE 802.1Q Encapsulation)
   Protocols Configured:          Received:        Transmitted:
                     IP         1965764076          1965783813
VLAN trunk interfaces for VLAN ID 3017:
GigabitEthernet0/0/0.3017
GigabitEthernet0/0/0.3017 (3017)
                     IP: 10.0.2.98
      Total 962668297 packets, 67413748724 bytes input
      Total 962679932 packets, 71269330446 bytes output
      Total 0 oversubscription packet drops
GigabitEthernet0/0/1.3017
GigabitEthernet0/0/1.3017 (3017)
                     IP: 10.0.2.237
      Total 1003101905 packets, 70246968079 bytes input
      Total 1003116275 packets, 74260373320 bytes output
      Total 0 oversubscription packet drops
VLAN ID: 3062 (IEEE 802.1Q Encapsulation)
   Protocols Configured:          Received:        Transmitted:
                     IP         1965727740          1965748350

VLAN trunk interfaces for VLAN ID 3062:
GigabitEthernet0/0/0.3062
GigabitEthernet0/0/0.3062 (3062)
                     IP: 10.0.2.102
      Total 962634040 packets, 67411184249 bytes input
      Total 962647204 packets, 71266733940 bytes output
      Total 0 oversubscription packet drops
GigabitEthernet0/0/1.3062
GigabitEthernet0/0/1.3062 (3062)
                     IP: 10.0.2.241

      Total 1003099825 packets, 70246823077 bytes input
      Total 1003113541 packets, 74260171809 bytes output
      Total 0 oversubscription packet drops

```

**Help:** execute the command "show vlans"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show interfaces

**Output:**
```
FastEthernet1 is down, line protocol is down 
  Hardware is RP management port, address is 6c41.6aba.b47f (bia 6c41.6aba.b47f)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Half-duplex, 10Mb/s, 100BaseTX/FX
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/0 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/1 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet Port, address is 6c41.6aba.b440 (bia 6c41.6aba.b440)
  Description: vss
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is QSFP-10G 1M
  input flow-control is on, output flow-control is on 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 4
  Queueing strategy: Class-based queueing
  Output queue: 0/40 (size/max)
  5 minute input rate 1180000 bits/sec, 131 packets/sec
  5 minute output rate 38000 bits/sec, 33 packets/sec
     4035758153 packets input, 2783400652228 bytes, 0 no buffer
     Received 160702941 broadcasts (60693400 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     956714742 packets output, 377708181830 bytes, 0 underruns
     0 output errors, 0 collisions, 4 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/2 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet Port, address is 6c41.6aba.b441 (bia 6c41.6aba.b441)
  Description: fast hello
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is QSFP-10G 1M
  input flow-control is on, output flow-control is on 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:21, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 6000 bits/sec, 10 packets/sec
  5 minute output rate 6000 bits/sec, 10 packets/sec
     237748374 packets input, 16820309764 bytes, 0 no buffer
     Received 383456 broadcasts (383456 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     237747059 packets output, 16820212146 bytes, 0 underruns
     0 output errors, 0 collisions, 5 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/3 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet Port, address is 6c41.6aba.b442 (bia 6c41.6aba.b442)
  Description: vss
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is QSFP-10G 1M
  input flow-control is on, output flow-control is on 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 3
  Queueing strategy: Class-based queueing
  Output queue: 0/40 (size/max)
  5 minute input rate 196000 bits/sec, 50 packets/sec
  5 minute output rate 11000 bits/sec, 16 packets/sec
     9594383489 packets input, 7302479029074 bytes, 0 no buffer
     Received 66218427 broadcasts (60570610 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     814075627 packets output, 479172141396 bytes, 0 underruns
     0 output errors, 0 collisions, 4 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/4 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet Port, address is 6c41.6aba.b443 (bia 6c41.6aba.b443)
  Description: wan
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, link type is auto, media type is 1000BaseT
  input flow-control is on, output flow-control is on 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 1842857
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 419000 bits/sec, 173 packets/sec
  5 minute output rate 1582000 bits/sec, 261 packets/sec
     21777507643 packets input, 11789825980301 bytes, 0 no buffer
     Received 23753204 broadcasts (23750450 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     37553221421 packets output, 35764893203339 bytes, 0 underruns
     0 output errors, 0 collisions, 3 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/5 is administratively down, line protocol is down (disabled) 
  Hardware is Ten Gigabit Ethernet Port, address is 6c41.6aba.b444 (bia 6c41.6aba.b444)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, Auto-speed, link type is auto, media type is 1000BaseT
  input flow-control is off, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of " show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/6 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet Port, address is 6c41.6aba.b445 (bia 6c41.6aba.b445)
  Description: wireless
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, link type is auto, media type is 1000BaseT
  input flow-control is off, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:07, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 32416
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1261000 bits/sec, 243 packets/sec
  5 minute output rate 1582000 bits/sec, 200 packets/sec
     9295308398 packets input, 6075966632228 bytes, 0 no buffer
     Received 23393246 broadcasts (20908873 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     8107505603 packets output, 6210024688013 bytes, 0 underruns
     0 output errors, 0 collisions, 3 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/7 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet Port, address is 6c41.6aba.b446 (bia 6c41.6aba.b446)
  Description: wireless
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, link type is auto, media type is 1000BaseT
  input flow-control is off, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:17, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     169728331 packets input, 129190060864 bytes, 0 no buffer
     Received 13015669 broadcasts (10933489 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     242553619 packets output, 112374124403 bytes, 0 underruns
     0 output errors, 0 collisions, 3 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/8 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet Port, address is 6c41.6aba.b447 (bia 6c41.6aba.b447)
  Description: nas
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 1000Mb/s, link type is auto, media type is 1000BaseT
  input flow-control is on, output flow-control is on 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:08, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     15804107 packets input, 9120651162 bytes, 0 no buffer
     Received 345932 broadcasts (345113 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     13861965 packets output, 1342553433 bytes, 0 underruns
     0 output errors, 0 collisions, 3 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/9 is administratively down, line protocol is down (disabled) 
  Hardware is Ten Gigabit Ethernet Port, address is 6c41.6aba.b448 (bia 6c41.6aba.b448)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, Auto-speed, link type is auto, media type is No XCVR
  input flow-control is off, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/10 is administratively down, line protocol is down (disabled) 
  Hardware is Ten Gigabit Ethernet Port, address is 6c41.6aba.b449 (bia 6c41.6aba.b449)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, Auto-speed, link type is auto, media type is No XCVR
  input flow-control is off, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/11 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet Port, address is 6c41.6aba.b44a (bia 6c41.6aba.b44a)
  Description: shop access
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is QSFP-10G 5M
  input flow-control is on, output flow-control is on 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:03, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 1
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 289000 bits/sec, 170 packets/sec
  5 minute output rate 7166000 bits/sec, 714 packets/sec
     33070723737 packets input, 27913140863803 bytes, 0 no buffer
     Received 102530192 broadcasts (91747041 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     36245627794 packets output, 35298352607317 bytes, 0 underruns
     0 output errors, 0 collisions, 3 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/12 is down, line protocol is down (notconnect) 
  Hardware is Ten Gigabit Ethernet Port, address is 6c41.6aba.b44b (bia 6c41.6aba.b44b)
  Description: shop floor
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, Auto-speed, link type is auto, media type is 1000BaseSX
  input flow-control is off, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 3 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/13 is up, line protocol is up (connected) 
  Hardware is Ten Gigabit Ethernet Port, address is 6c41.6aba.b44c (bia 6c41.6aba.b44c)
  Description: shop access
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 10Gb/s, link type is auto, media type is 10GBase-SR
  input flow-control is on, output flow-control is on 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:03, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 11
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 128000 bits/sec, 48 packets/sec
  5 minute output rate 897000 bits/sec, 126 packets/sec
     2706943013 packets input, 593239780527 bytes, 0 no buffer
     Received 10407156 broadcasts (9275413 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     5030894569 packets output, 4585304759149 bytes, 0 underruns
     0 output errors, 0 collisions, 3 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/14 is administratively down, line protocol is down (disabled) 
  Hardware is Ten Gigabit Ethernet Port, address is 6c41.6aba.b44d (bia 6c41.6aba.b44d)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, Auto-speed, link type is auto, media type is No XCVR
  input flow-control is off, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
TenGigabitEthernet1/1/15 is administratively down, line protocol is down (disabled) 
  Hardware is Ten Gigabit Ethernet Port, address is 6c41.6aba.b44e (bia 6c41.6aba.b44e)
  MTU 1500 bytes, BW 10000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, Auto-speed, link type is auto, media type is No XCVR
  input flow-control is off, output flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
```

**Help:** execute the command "show interfaces"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show dmvpn

**Output:**
```
Legend: Attrb --> S - Static, D - Dynamic, I - Incomplete
        N - NATed, L - Local, X - No Socket
        T1 - Route Installed, T2 - Nexthop-override
        C - CTS Capable
        # Ent --> Number of NHRP entries with same NBMA peer
        NHS Status: E --> Expecting Replies, R --> Responding, W --> Waiting
        UpDn Time --> Up or Down Time for a Tunnel
==========================================================================
 
Interface: Tunnel100, IPv4 NHRP Details 
Type:Spoke, NHRP Peers:2, 

 # Ent  Peer NBMA Addr Peer Tunnel Add State  UpDn Tm Attrb
 ----- --------------- --------------- ----- -------- -----
     1 10.200.0.3           10.253.0.1    UP 03:19:46     S
     1 10.202.0.170         10.253.0.2  NHRP    48w0d     S


```

**Help:** execute the command "show dmvpn"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show controller t1

**Output:**
```
T1 0/2/0 is up.        
  Applique type is Channelized T1        
  Cablelength is long gain36 0db        
  No alarms detected.        
  alarm-trigger is not set        
  Soaking time: 3, Clearance time: 10        
  AIS State:Clear  LOS State:Clear  LOF State:Clear         
  Framing is ESF, Line Code is B8ZS, Clock Source is Line Primary.        
  Data in current interval (190 seconds elapsed):
     0 Line Code Violations, 0 Path Code Violations        
     0 Slip Secs, 0 Fr Loss Secs, 0 Line Err Secs, 0 Degraded Mins        
     0 Errored Secs, 0 Bursty Err Secs, 0 Severely Err Secs, 0 Unavail Secs        
  Total Data (last 64 15 minute intervals):        
     0 Line Code Violations, 0 Path Code Violations,        
     0 Slip Secs, 0 Fr Loss Secs, 0 Line Err Secs, 0 Degraded Mins,        
     0 Errored Secs, 0 Bursty Err Secs, 0 Severely Err Secs, 0 Unavail Secs        
T1 0/2/1 is up.        
  Applique type is Channelized T1        
  Cablelength is long gain36 0db        
  No alarms detected.        
  alarm-trigger is not set        
  Soaking time: 3, Clearance time: 10        
  AIS State:Clear  LOS State:Clear  LOF State:Clear         
  Framing is ESF, Line Code is B8ZS, Clock Source is Line.        
  Data in current interval (189 seconds elapsed):        
     0 Line Code Violations, 0 Path Code Violations        
     0 Slip Secs, 0 Fr Loss Secs, 0 Line Err Secs, 0 Degraded Mins        
     0 Errored Secs, 0 Bursty Err Secs, 0 Severely Err Secs, 0 Unavail Secs        
  Total Data (last 64 15 minute intervals):        
     0 Line Code Violations, 0 Path Code Violations,        
     0 Slip Secs, 0 Fr Loss Secs, 0 Line Err Secs, 0 Degraded Mins,        
     0 Errored Secs, 0 Bursty Err Secs, 0 Severely Err Secs, 0 Unavail Secs        
T1 0/3/0 is up.        
  Applique type is Channelized T1        
  Cablelength is long gain36 0db        
  No alarms detected.        
  alarm-trigger is not set        
  Soaking time: 3, Clearance time: 10        
  AIS State:Clear  LOS State:Clear  LOF State:Clear         
  Framing is ESF, Line Code is B8ZS, Clock Source is Line.        
  Data in current interval (429 seconds elapsed):        
     0 Line Code Violations, 0 Path Code Violations        
     0 Slip Secs, 0 Fr Loss Secs, 0 Line Err Secs, 0 Degraded Mins        
     0 Errored Secs, 0 Bursty Err Secs, 0 Severely Err Secs, 0 Unavail Secs        
  Total Data (last 65 15 minute intervals):        
     0 Line Code Violations, 0 Path Code Violations,        
     0 Slip Secs, 0 Fr Loss Secs, 0 Line Err Secs, 0 Degraded Mins,        
     0 Errored Secs, 0 Bursty Err Secs, 0 Severely Err Secs, 0 Unavail Secs        
T1 0/3/1 is down.        
  Applique type is Channelized T1        
  Cablelength is long gain36 0db        
  Transmitter is sending remote alarm.        
  Receiver has loss of signal.
  alarm-trigger is not set
  Soaking time: 3, Clearance time: 10
  AIS State:Clear  LOS State:Failure LOF State:Clear   
  Framing is ESF, Line Code is B8ZS, Clock Source is Line.
  Data in current interval (428 seconds elapsed):      
     0 Line Code Violations, 0 Path Code Violations
     0 Slip Secs, 0 Fr Loss Secs, 0 Line Err Secs, 0 Degraded Mins
     0 Errored Secs, 0 Bursty Err Secs, 0 Severely Err Secs, 428 Unavail Secs
  Total Data (last 65 15 minute intervals):
     0 Line Code Violations, 0 Path Code Violations,
     0 Slip Secs, 0 Fr Loss Secs, 0 Line Err Secs, 0 Degraded Mins,
     0 Errored Secs, 0 Bursty Err Secs, 0 Severely Err Secs, 58500 Unavail Secs

```

**Help:** execute the command "show controller t1"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show platform diag

**Output:**
```
Chassis type: ASR1004 
 Slot: 0, ASR1000-SIP10 
 Running state               : ok
 Internal state              : online
 Internal operational state  : ok
 Physical insert detect time : 00:00:48 (4d22h ago)
 Software declared up time   : 00:01:40 (4d22h ago)
 CPLD version                : 07091401
 Firmware version            : 12.2(33r)XNB

 Sub-slot: 0/0, SPA-5X1GE-V2
 Operational status          : ok
 Internal state              : inserted
 Physical insert detect time : 00:00:36 (4d22h ago)
 Logical insert detect time  : 00:02:23 (4d22h ago)

 Sub-slot: 0/1, SPA-2XT3/E3
 Operational status          : ok
 Internal state              : inserted
   Physical insert detect time : 00:00:36 (4d22h ago)
   Logical insert detect time  : 00:02:23 (4d22h ago)

 Slot: R0, ASR1000-RP1         
   Running state               : ok
   Internal state              : online
   Internal operational state  : ok
   Physical insert detect time : 00:00:48 (4d22h ago)
   Software declared up time   : 00:00:48 (4d22h ago)
   CPLD version                : 07062111
   Firmware version            : 12.2(33r)XNB

 Sub-slot: R0/0, 
   Running state               : ok, active
   Logical insert detect time  : 00:00:48 (4d22h ago)
   Became HA Active time       : 00:04:56 (4d22h ago)

 Sub-slot: R0/1, 
   Running state               : ok, standby
   Logical insert detect time  : 00:02:50 (4d22h ago)

 Slot: F0, ASR1000-ESP10       
   Running state               : ok, active
   Internal state              : online
   Internal operational state  : ok
   Physical insert detect time : 00:00:48 (4d22h ago)
   Software declared up time   : 00:01:40 (4d22h ago)
   Hardware ready signal time  : 00:00:49 (4d22h ago)
   Packet ready signal time    : 00:01:49 (4d22h ago)
   CPLD version                : 07051680
   Firmware version            : 12.2(33r)XNB

 Slot: P0, ASR1004-PWR-AC
   State                       : ok
   Physical insert detect time : 00:01:40 (4d22h ago)

 Slot: P1, ASR1004-PWR-AC
   State                       : ok
   Physical insert detect time : 00:01:40 (4d22h ago)


```

**Help:** execute the command "show platform diag"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip cef

**Output:**
```
Prefix               Next Hop             Interface
0.0.0.0/0            10.180.122.153       GigabitEthernet0/1
0.0.0.0/8            drop
0.0.0.0/32           receive
10.0.0.0/16          10.180.122.153       GigabitEthernet0/1
10.157.1.0/24        172.17.100.101       Tunnel60701
10.180.122.7/32      receive              Loopback0
10.180.122.152/29    attached             GigabitEthernet0/1
10.180.122.152/32    receive              GigabitEthernet0/1
224.0.0.0/4          drop
224.0.0.0/24         receive
240.0.0.0/4          drop
255.255.255.255/32   receive

```

**Help:** execute the command "show ip cef"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show nve peers

**Output:**
```
Interface  VNI      Type Peer-IP          RMAC/Num_RTs   eVNI     state flags UP time
nve1       1033 L3CP 192.168.111.81   0200.c0a8.433c 1033   UP   A/M 6d22h
nve1       1033 L3CP 192.168.111.48   cc7f.76a5.3c56 1033   UP   A/M 6d22h
nve1       1031 L3CP 192.168.111.81   0200.c0a8.433c 1031   UP   A/M 6d22h
nve1       1031 L3CP 192.168.111.48   cc7f.76a5.3c56 1031   UP   A/M 6d22h
nve1       1032 L3CP 192.168.111.48   cc7f.76a5.3c56 1032   UP   A/M 6d22h
nve1       1036 L3CP 192.168.111.48   cc7f.76a5.3c56 1036   UP   A/M 6d22h

```

**Help:** execute the command "show nve peers"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show dhcp lease

**Output:**
```
Temp IP addr: 0.0.0.0  for peer on Interface: Vlan1
Temp  sub net mask: 0.0.0.0
   DHCP Lease server: 0.0.0.0, state: 10 Purging
   DHCP transaction id: BD28
   Lease: 0 secs,  Renewal: 0 secs,  Rebind: 0 secs
   Next timer fires after: 00:00:31
   Retry count: 0   Client-ID: cisco-0025.46e6.0cc0-Vl1
   Client-ID hex dump: 636973636F2D303032352E343665362E
                       306363302D566C31
   Hostname: hostname-2
```

**Help:** execute the command "show dhcp lease"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show lldp neighbors detail

**Output:**
```
Local Intf: Gi0/1/7
Chassis id: 10.10.0.1
Port id: C8F9F9D61BC2:P1
 Port Description: SW PORT
System Name: SEPC8F9F9D61BC2

System Description:
 Cisco IP Phone 7962G,V12, SCCP42.9-3-1ES27S

Time remaining: 127 seconds
 System Capabilities: B,T
Enabled Capabilities: B,T
Management Addresses:
    IP: 10.10.0.1
Auto Negotiation - supported, enabled
Physical media capabilities:
    1000baseT(HD)
    1000baseX(FD)
    Symm, Asym Pause(FD)
    Symm Pause(FD)
 Media Attachment Unit type: 16
Vlan ID: - not advertised

MED Information:

    MED Codes:
          (NP) Network Policy, (LI) Location Identification
          (PS) Power Source Entity, (PD) Power Device
          (IN) Inventory

    H/W revision: 12
    F/W revision: tnp62.8-3-1-21a.bin
    S/W revision: SCCP42.9-3-1ES27S
    Serial number: FCH1610A5S5
    Manufacturer: Cisco Systems, Inc.
    Model: CP-7962G
    Capabilities: NP, PD, IN
    Device type: Endpoint Class III
    Network Policy(Voice): VLAN 10, tagged, Layer-2 priority: 5, DSCP: 46
    Network Policy(Voice Signal): VLAN 10, tagged, Layer-2 priority: 4, DSCP: 32
    PD device, Power source: Unknown, Power Priority: Unknown, Wattage: 6.3
    Location - not advertised
```

**Help:** execute the command "show lldp neighbors detail"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show mpls interfaces

**Output:**
```
Interface              IP            Tunnel   BGP Static Operational
TenGigabitEthernet1/1  Yes (ldp)     No       No  No     Yes     
TenGigabitEthernet1/5  Yes (ldp)     No       No  No     Yes     
TenGigabitEthernet1/9  Yes (ldp)     No       No  No     Yes     
TenGigabitEthernet1/11 Yes (ldp)     No       No  No     Yes     
TenGigabitEthernet1/13 Yes (ldp)     No       No  No     Yes     
TenGigabitEthernet1/15 Yes (ldp)     No       No  No     Yes     
Vlan101                Yes (ldp)     No       No  No     Yes     

```

**Help:** execute the command "show mpls interfaces"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ap summary

**Output:**
```
Number of APs: 1

AP Name                            Slots    AP Model  Ethernet MAC    Radio MAC       Location                          Country     IP Address                                 State         
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
device-name                         2      9120AXI   0000.0000.000a  000a.000a.0000  default location                  US          1.1.1.1                            Registered

```

**Help:** execute the command "show ap summary"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show object-group

**Output:**
```
Network object group NNNN
Service object group SSSS
Service object group TEST-SVC-OGR
 Description ! Test Service Group !
 icmp echo-reply
 tcp eq smtp
 udp eq tacacs
 udp range tacacs 50
 tcp range 79 www
 tcp eq www
 tcp eq 81
 udp lt 999
 udp gt 97
 tcp-udp range 12200 12700
 icmp
 tcp
 udp
 tcp-udp range 0 65535
 group-object SSSS
 ip
 ipinip
 99
Network object group TEST_NET_OGR
 Description ###TEST NETWORK OGR###
 any
 host 1.1.1.1
 range 2.2.2.2 3.3.3.3
 group-object NNNN
 1.1.1.0 255.255.255.0
 Network object group XXXX
Network object group YYYY

```

**Help:** execute the command "show object-group"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show snmp community

**Output:**
```
Community name: ILMI
Community Index: cisco0
Community SecurityName: ILMI
storage-type: read-only  active


Community name: public
Community Index: cisco1
Community SecurityName: public
storage-type: nonvolatile        active


Community name: private
Community Index: cisco2
Community SecurityName: private
storage-type: nonvolatile        active


```

**Help:** execute the command "show snmp community"

**Prompt:**
- cisco_ios>
- cisco_ios#

### traceroute

**Output:**
```
Type escape sequence to abort.
Tracing the route to 10.225.2.1
VRF info: (vrf in name/id, vrf out name/id)
  1 10.180.140.150 1 msec 1 msec 1 msec
  2 172.17.10.225 169 msec 142 msec 135 msec
  3 108.170.246.129 13 msec *  *  *  *  *  *  *  *  * 
  4 74.125.242.97 14 msec
    216.239.63.218 12 msec
    172.253.68.212 13 msec
    74.125.242.97 13 msec
    216.239.56.192 13 msec
    74.125.242.97 13 msec
    108.170.238.117 13 msec
    216.239.58.220 13 msec
    74.125.242.97 13 msec 13 msec
  5 216.58.204.46 13 msec
    74.125.242.115 12 msec
    74.125.242.114 15 msec
    108.170.238.117 12 msec
    108.170.238.119 13 msec
    74.125.242.83 12 msec 12 msec 13 msec
    74.125.242.82 12 msec
    108.170.238.117 14 msec
  6 172.17.10.225 !H  *  !H
```

**Help:** execute the command "traceroute"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show power supplies

**Output:**
```
Power supplies needed by system    : 1
Power supplies currently available : 2

```

**Help:** execute the command "show power supplies"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ipv6 access-lists

**Output:**
```
IPv6 access list ACL2_IPv6
    deny ipv6 2A01:728::/29 any sequence 10
IPv6 access list ACL3_IPv6
    permit tcp 2A01:720::/29 any log auth routing sequence 10
IPv6 access list ACL_IPv6
    deny ipv6 2A01:728::/29 any sequence 10
IPv6 access list WAN_LOCAL
    permit tcp AAAA:BBBB::/64 2A05:C100:53::/64 eq 6543 sequence 11
    permit udp AAAA:BBBB::/64 2A05:C100:53::/64 eq 6543 sequence 12
    deny udp host 2A05:C100:53::17 host 2A05:C100:53::145 eq 45 sequence 14
    deny tcp host 2A05:C100:53::14 host 2A05:C100:53::17 range 46 48 sequence 15
    permit tcp any any established sequence 9996
    permit icmp any any sequence 9997
    permit udp any any sequence 9998
    deny ipv6 any any sequence 9999
IPv6 access list WAN_ROUTEUR
    permit ipv6 2A05:C100:53::/64 any sequence 10
    permit ipv6 2A05:C100:53:1::/64 any sequence 20
    permit ipv6 2A05:C100::/48 any sequence 30
    permit ipv6 2A00:41E0::/48 any sequence 40
    permit ipv6 2A05:C100:43::/64 any sequence 45
    deny ipv6 any any sequence 50
    permit tcp any any established sequence 9996

```

**Help:** execute the command "show ipv6 access-lists"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show alert counters

**Output:**
```
Interface: Fa1/1
Error Code: ALERT-5-STP_BLOCK
Timestamp:  2020 04 28 19 12 03
Description:  This port is blocked by Spanning Tree Protocol (STP).
Recommendation:  Make sure that no Spanning Tree Protocol loops exist in the network.


Interface: Fa1/2
Error Code: ALERT-5-STP_BLOCK
Timestamp:  2020 08 10 11 34 47
Description:  This port is blocked by Spanning Tree Protocol (STP).
Recommendation:  Make sure that no Spanning Tree Protocol loops exist in the network.


Error Code: ALERT-5-COLLISION_ERR
Timestamp:  2020 08 27 13 50 25
Description:  Detected lower performance on this link, possibly because of half duplex configuration or duplex mismatch.
Recommendation:  Change the duplex setting of both the ports on this link to "auto" or "full-duplex".


Interface: Fa1/3
Error Code: ALERT-4-PORT_PSECURE_VIOLATION
Timestamp:  2020 08 27 13 53 22
Description:  Access denied to one or more connecting devices on this port.
Recommendation:  Maximum allowed devices on this port are already connected, or an unauthorized device attempted to connect on this secure port. Disconnect the device.


Error Code: ALERT-5-ALIGN_FCS_ERR
Timestamp:  2020 08 27 13 48 25
Description:  Detected a faulty cable, or bad hardware on connected device, or the connected device is generating frames with bad Frame Check Sequence (FCS).
Recommendation:  Change the duplex setting of both the ports on this link to "full-duplex" or change the duplex setting of this port to "auto". Check if the cable is faulty and replace it if needed. The hardware on the connected device might be bad, disconnect the connected device.


Error Code: ALERT-5-RX_TX_ERR
Timestamp:  2020 08 27 13 48 25
Description:  Detected a possible over-utilization of the switch link or bad frames generated by the connected device.
Recommendation:  Change the port settings of this port to "auto". It might help to create an Ether Channel by grouping this port with other under-utilized or unused ports. Disconnect the connected device.


Interface: Fa1/4

Interface: Fa1/5

Interface: Fa1/6

Interface: Fa1/7

Interface: Fa1/8

Interface: Gi1/1

Interface: Gi1/2

Global Errors :


```

**Help:** execute the command "show alert counters"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show switch detail

**Output:**
```
Switch/Stack Mac Address : 4c4e.3573.ac00
                                           H/W   Current
Switch#  Role   Mac Address     Priority Version  State 
----------------------------------------------------------
*1       Master 4c4e.3573.ac00     15     3       Ready               
 2       Member 4c4e.3573.7b00     8      3       Ready               
 3       Member 4c4e.3573.ac80     7      3       Ready               



         Stack Port Status             Neighbors     
Switch#  Port 1     Port 2           Port 1   Port 2 
--------------------------------------------------------
  1        Ok         Ok                3        2 
  2        Ok         Ok                1        3 
  3        Ok         Ok                2        1 

```

**Help:** execute the command "show switch detail"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip bgp neighbors advertised-routes

**Output:**
```
BGP table version is 143173748, local router ID is 192.168.88.2
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter,
              x best-external, a additional-path, c RIB-compressed,
              t secondary path,
Origin codes: i - IGP, e - EGP, ? - incomplete
 RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
 *>   113.55.45.0/24   0.0.0.0                            32768 i
 *>   113.55.48.0/24   0.0.0.0                            32768 i
 *>   113.55.50.0/24   0.0.0.0                            32768 i
 *>   113.55.51.0/24   0.0.0.0                            32768 i
 *>   113.55.53.0/24   0.0.0.0                            32768 i
 *>   113.55.54.0/24   0.0.0.0                            32768 i
 *>   113.55.58.0/24   0.0.0.0                            32768 i

Total number of prefixes 7

```

**Help:** execute the command "show ip bgp neighbors advertised-routes"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show processes memory sorted

**Output:**
```
Processor Pool Total:  919638648 Used:  236752096 Free:  682886552
 lsmpi_io Pool Total:    6295128 Used:    6294296 Free:        832

 PID TTY  Allocated      Freed    Holding    Getbufs    Retbufs Process
   0   0  209299480   13474544  178205704          0          0 *Init*          
  78   0 2569666688    1554280   27061536          0          0 IOSD ipc task   
   0   0  607956496  428619384    6374592   17503559          0 *Dead*          
 365   0    3946896       5680    3983160     849828          0 EEM ED Syslog   
   1   0    1583728       3472    1613672          0          0 Chunk Manager   
 382   0    1510464      33704    1506704          0          0 EEM Server      
 165   0    2957736      12304    1112904          0          0 CWAN OIR Handler
   0   0          0          0     657856          0          0 *MallocLite*    
   4   0     525856      23256     458696          0          0 RF Slave Main Th
 366   0     381680       5680     417944      72316          0 EEM ED Generic  
 338   0     309184       1640     361488          0          0 Crypto IKEv2    
 480   0     167752        448     221248          0          0 MRIB Process    
  10   0 4096314696 4096430632     215576 3914231834 3914277834 Pool Manager    

342936032 Total

```

**Help:** execute the command "show processes memory sorted"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show standby brief

**Output:**
```
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Vl1         1    120 P Active  local           10.1.1.3      10.1.1.1
Vl1         6    120 P Active  local           FE80::B         FE80::DEF
Vl51        1    120 P Init    unknown         unknown         10.1.51.1
Vl51        6    120 P Init    unknown         unknown         FE80::DEF
Vl500       1    120 P Active  local           10.1.5.3      10.1.5.1
Vl500       6    120 P Active  local           FE80::B         FE80::DEF
Vl4010 
     1    120 P Active  local           10.1.254.3    10.1.254.1

```

**Help:** execute the command "show standby brief"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip ospf neighbor

**Output:**
```
Neighbor ID     Pri   State           Dead Time   Address         Interface
10.0.0.1          0   FULL/  -        00:00:32    10.0.1.1        Port-channel1
10.0.0.2          0   FULL/  -        00:00:33    10.0.2.1        Port-channel2
10.0.0.3          0   FULL/  -        00:00:39    10.0.3.1        Vlan1000

```

**Help:** execute the command "show ip ospf neighbor"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show aliases

**Output:**
```
Exec mode aliases:
  h                     help
  lo                    logout
  p                     ping
  r                     resume
  s                     show
  u                     undebug
  un                    undebug
  w                     where
  sps                   show platform software vnic-if interface-mapping

ATM virtual circuit configuration mode aliases:
  vbr                   vbr-nrt
```

**Help:** execute the command "show aliases"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show logging

**Output:**
```
Syslog logging: enabled (0 messages dropped, 21 messages rate-limited, 0 flushes, 0 overruns, xml disabled, filtering disabled)

No Active Message Discriminator.



No Inactive Message Discriminator.


    Console logging: level debugging, 10027 messages logged, xml disabled,
                     filtering disabled
    Monitor logging: level debugging, 0 messages logged, xml disabled,
                     filtering disabled
    Buffer logging:  level informational, 10048 messages logged, xml disabled,
                    filtering disabled
    Exception Logging: size (8192 bytes)
    Count and timestamp logging messages: disabled
    Persistent logging: disabled
 
No active filter modules.

    Trap logging: level debugging, 10180 message lines logged
        Logging to 81.95.32.138  (udp port 514, audit disabled,
              link up),
              10179 message lines logged,
              0 message lines rate-limited,
              0 message lines dropped-by-MD,
              xml disabled, sequence number disabled
              filtering disabled
        Logging to 192.168.214.143  (udp port 514, audit disabled,
              link up),
              10180 message lines logged,
              0 message lines rate-limited,
              0 message lines dropped-by-MD,
              xml disabled, sequence number disabled
              filtering disabled
        Logging Source-Interface:       VRF Name:

Log Buffer (100000 bytes):
rtual-PPP2, changed state to down
*Sep 14 05:59:54.113: %LINEPROTO-5-UPDOWN: Line protocol on Interface Virtual-PPP2, changed state to up
*Sep 14 06:00:45.693: %CRYPTO-4-PKT_REPLAY_ERR: decrypt: replay check failed
        connection id=29, sequence number=219

*Sep 14 06:07:26.245: %LINEPROTO-5-UPDOWN: Line protocol on Interface Virtual-PPP2, changed state to down

```

**Help:** execute the command "show logging"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show environment power all

**Output:**
```
SW  PID                 Serial#     Status           Sys Pwr  PoE Pwr  Watts
--  ------------------  ----------  ---------------  -------  -------  -----
1A  PWR-C1-1100WAC      DEF123456AB  OK              Good     Good     1100
1B  PWR-C1-1100WAC      DEF123456CD  OK              Good     Good     1100
2A  PWR-C1-1100WAC      DEF123456EF  OK              Good     Good     1100
2B  PWR-C1-1100WAC      DEF123456GH  OK              Good     Good     1100

```

**Help:** execute the command "show environment power all"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show tacacs

**Output:**
```
Tacacs+ Server -  public  :
               Server name: TACACS_ABC
            Server address: 10.1.1.141
               Server port: 49
              Socket opens:     146715
             Socket closes:     146715
             Socket aborts:          0
             Socket errors:          0
           Socket Timeouts:          0
   Failed Connect Attempts:        114
        Total Packets Sent:     166094
        Total Packets Recv:     166094


Tacacs+ Server -  public  :
               Server name: TACACS_XYZ
            Server address: 10.2.1.141
               Server port: 49
              Socket opens:       2640
             Socket closes:       2640
             Socket aborts:          0
             Socket errors:          0
           Socket Timeouts:          0
   Failed Connect Attempts:          0
        Total Packets Sent:       2954
        Total Packets Recv:       2953

```

**Help:** execute the command "show tacacs"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show license

**Output:**
```
Index 1 Feature: appxk9                         
        Period left: Life time
        License Type: Permanent
        License State: Active, In Use
        License Count: Non-Counted
        License Priority: Medium
 Index 2 Feature: uck9                           
        Period left: Not Activated
        Period Used: 0  minute  0  second
        License Type: EvalRightToUse
        License State: Active, Not in Use, EULA not accepted
        License Count: Non-Counted
        License Priority: None
Index 3 Feature: securityk9                     
        Period left: Life time
        License Type: Permanent
        License State: Active, In Use
        License Count: Non-Counted
        License Priority: Medium
Index 4 Feature: ipbasek9                       
        Period left: Life time
        License Type: Permanent
        License State: Active, In Use
        License Count: Non-Counted
        License Priority: Medium
Index 5 Feature: FoundationSuiteK9              
        Period left: Not Activated
        Period Used: 0  minute  0  second
        License Type: EvalRightToUse
        License State: Active, Not in Use, EULA not accepted
        License Count: Non-Counted
        License Priority: None
Index 6 Feature: AdvUCSuiteK9                   
        Period left: Not Activated
        Period Used: 0  minute  0  second
        License Type: EvalRightToUse
        License State: Active, Not in Use, EULA not accepted
        License Count: Non-Counted
        License Priority: None
Index 7 Feature: cme-srst                       
        Period left: Not Activated
        Period Used: 0  minute  0  second
        License Type: EvalRightToUse
        License State: Active, Not in Use, EULA not accepted
        License Count: 0/0  (In-use/Violation)
        License Priority: None
Index 8 Feature: hseck9                         
        Period left: Life time
        License Type: Permanent
        License State: Active, In Use
        License Count: Non-Counted
        License Priority: Medium
Index 9 Feature: throughput                     
        Period left: Not Activated
        Period Used: 0  minute  0  second
        License Type: EvalRightToUse
        License State: Active, Not in Use, EULA not accepted
        License Count: Non-Counted
        License Priority: None
Index 10 Feature: internal_service              

```

**Help:** execute the command "show license"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show crypto session detail

**Output:**
```
Crypto session current status
 
Code: C - IKE Configuration mode, D - Dead Peer Detection    
K - Keepalives, N - NAT-traversal, T - cTCP encapsulation    
X - IKE Extended Authentication, F - IKE Fragmentation
R - IKE Auto Reconnect
 
Interface: Tunnel1201
Session status: DOWN-NEGOTIATING
Peer: 10.161.255.14 port 500 fvrf: (none) ivrf: (none)
      Desc: (none)
      Phase1_id: (none)
  Session ID: 0 
  IKEv1 SA: local 10.175.200.116/500 remote 10.161.255.14/500 Inactive
          Capabilities:(none) connid:0 lifetime:0
  Session ID: 0 
  IKEv1 SA: local 10.175.200.116/500 remote 10.161.255.14/500 Inactive
          Capabilities:(none) connid:0 lifetime:0
  IPSEC FLOW: permit 47 host 10.175.200.116 host 10.161.255.14
        Active SAs: 0, origin: crypto map
        Inbound:  #pkts dec'ed 0 drop 0 life (KB/Sec) 0/0
        Outbound: #pkts enc'ed 0 drop 0 life (KB/Sec) 0/0
 
Interface: Tunnel1101
Uptime: 7w0d
 Session status: UP-ACTIVE    
Peer: 192.168.0.1 port 4500 fvrf: (none) ivrf: (none)
      Phase1_id: SOME_DEVICE1234.1pc.com
      Desc: (none)
  Session ID: 0 
  IKEv1 SA: local 169.0.1.1/4500 remote 192.168.0.1/4500 Active
          Capabilities:DN connid:2913 lifetime:09:03:41
  IPSEC FLOW: permit 47 host 169.0.1.1 host 192.168.0.1
        Active SAs: 2, origin: crypto map
        Inbound:  #pkts dec'ed 15344097 drop 0 life (KB/Sec) 4236992/615
        Outbound: #pkts enc'ed 18074395 drop 0 life (KB/Sec) 4236962/615
 
Interface: Tunnel2201
Session status: DOWN-NEGOTIATING
Peer: 10.163.255.14 port 500 fvrf: (none) ivrf: (none)
      Desc: (none)
      Phase1_id: (none)
  Session ID: 0 
  IKEv1 SA: local 10.175.200.116/500 remote 10.163.255.14/500 Inactive
          Capabilities:(none) connid:0 lifetime:0
  Session ID: 0 
  IKEv1 SA: local 10.175.200.116/500 remote 10.163.255.14/500 Inactive
          Capabilities:(none) connid:0 lifetime:0
  IPSEC FLOW: permit 47 host 10.175.200.116 host 10.163.255.14
        Active SAs: 0, origin: crypto map
        Inbound:  #pkts dec'ed 0 drop 0 life (KB/Sec) 0/0
        Outbound: #pkts enc'ed 0 drop 0 life (KB/Sec) 0/0

```

**Help:** execute the command "show crypto session detail"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show snmp group

**Output:**
```
groupname: GROUP1                           security model:v3 priv 
 contextname: <no context specified>         storage-type: nonvolatile
readview : g1readview                       writeview: <no writeview specified>        
notifyview: g1notifyview                     
row status: active      access-list: snmp-acl-name

groupname: ILMI                             security model:v1 
contextname: <no context specified>         storage-type: permanent
readview : *ilmi                            writeview: *ilmi                           
notifyview: <no notifyview specified>       
row status: active

groupname: ILMI                             security model:v2c 
contextname: <no context specified>         storage-type: permanent
readview : *ilmi                            writeview: *ilmi                           
notifyview: <no notifyview specified>       
row status: active

groupname: GROUP2                           security model:v1 
contextname: <no context specified>         storage-type: nonvolatile
readview : v1default                        writeview: <no writeview specified>        
notifyview: <no notifyview specified>       
row status: active      access-list: snmp-acl-name
 
groupname: GROUP2                           security model:v2c 
contextname: <no context specified>         storage-type: nonvolatile
readview : v1default                        writeview: <no writeview specified>        
notifyview: <no notifyview specified>       
row status: active      access-list: snmp-acl-name
 
groupname: GROUP3                           security model:v1 
contextname: <no context specified>         storage-type: nonvolatile
readview : v1default                        writeview: <no writeview specified>        
notifyview: <no notifyview specified>       
row status: active      access-list: snmp-acl-name
 
groupname: GROUP3                           security model:v2c 
contextname: <no context specified>         storage-type: nonvolatile
readview : v1default                        writeview: <no writeview specified>        
notifyview: <no notifyview specified>       
row status: active      access-list: snmp-acl-name
```

**Help:** execute the command "show snmp group"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip eigrp interfaces detail

**Output:**
```
EIGRP-IPv4 Interfaces for AS(12345)
                              Xmit Queue   PeerQ        Mean   Pacing Time   Multicast    Pending
Interface              Peers  Un/Reliable  Un/Reliable  SRTT   Un/Reliable   Flow Timer   Routes
Tu10                   1        0/0       0/0          97       1/45         433           0
  Hello-interval is 5, Hold-time is 15
  Split-horizon is enabled
  Next xmit serial <none>
  Packetized sent/expedited: 13389/102
  Hello's sent/expedited: 23525118/224
  Un/reliable mcasts: 0/0  Un/reliable ucasts: 14237/1554
  Mcast exceptions: 0  CR packets: 0  ACKs suppressed: 298
  Retransmissions sent: 662  Out-of-sequence rcvd: 738
  Topology-ids on interface - 0 
  Authentication mode is not set
  Topologies advertised on this interface:  base
  Topologies not advertised on this interface:

Tu20                   1        0/0       0/0          88       1/45         397           0
  Hello-interval is 5, Hold-time is 15
  Split-horizon is enabled
  Next xmit serial <none>
  Packetized sent/expedited: 13095/136
  Hello's sent/expedited: 23525540/259
  Un/reliable mcasts: 0/0  Un/reliable ucasts: 17661/1561
  Mcast exceptions: 0  CR packets: 0  ACKs suppressed: 713
  Retransmissions sent: 701  Out-of-sequence rcvd: 2865
  Topology-ids on interface - 0 
  Authentication mode is not set
  Topologies advertised on this interface:  base
  Topologies not advertised on this interface:

```

**Help:** execute the command "show ip eigrp interfaces detail"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show crypto ipsec sa detail

**Output:**
```
interface: Tunnel1
    Crypto map tag: Tunnel1-head-0, local addr 1.2.3.4

   protected vrf: (none)
   local  ident (addr/mask/prot/port): (1.2.3.4/255.255.255.255/47/0)
   remote ident (addr/mask/prot/port): (2.2.2.2/255.255.255.255/47/0)
   current_peer 2.2.2.2 port 4500
     PERMIT, flags={{origin_is_acl,}}
    #pkts encaps: 4981028, #pkts encrypt: 4981028, #pkts digest: 4981028
    #pkts decaps: 4112421, #pkts decrypt: 4112421, #pkts verify: 4112421
    #pkts compressed: 0, #pkts decompressed: 0
    #pkts not compressed: 0, #pkts compr. failed: 0
    #pkts not decompressed: 0, #pkts decompress failed: 0
    #pkts no sa (send) 0, #pkts invalid sa (rcv) 0
    #pkts encaps failed (send) 0, #pkts decaps failed (rcv) 0
    #pkts invalid prot (recv) 0, #pkts verify failed: 0
    #pkts invalid identity (recv) 0, #pkts invalid len (rcv) 0
    #pkts replay rollover (send): 0, #pkts replay rollover (rcv) 0
    ##pkts replay failed (rcv): 0
    #pkts tagged (send): 0, #pkts untagged (rcv): 0
    #pkts not tagged (send): 0, #pkts not untagged (rcv): 0
    #pkts internal err (send): 0, #pkts internal err (recv) 0

     local crypto endpt.: 1.2.3.4, remote crypto endpt.: 2.2.2.2
     plaintext mtu 1442, path mtu 1500, ip mtu 1500, ip mtu idb GigabitEthernet8
     current outbound spi: 0x1234ABCD(305441741)
     PFS (Y/N): N, DH group: none

     inbound esp sas:
      spi: 0xABCD1234(2882343476)
        transform: esp-256-aes esp-sha-hmac ,
        in use settings ={{Transport UDP-Encaps, }}
        conn id: 124, flow_id: Onboard VPN:124, sibling_flags 80000000, crypto map: Tunnel1-head-0
        sa timing: remaining key lifetime (k/sec): (4332650/3205)
        IV size: 16 bytes
        replay detection support: Y  replay window size: 1024
        Status: ACTIVE(ACTIVE)

     inbound ah sas:
          
     inbound pcp sas:

     outbound esp sas:
      spi: 0x1234ABCD(305441741)
        transform: esp-256-aes esp-sha-hmac ,
        in use settings ={{Transport UDP-Encaps, }}
        conn id: 123, flow_id: Onboard VPN:123, sibling_flags 80000000, crypto map: Tunnel1-head-0
        sa timing: remaining key lifetime (k/sec): (4332649/3205)
        IV size: 16 bytes
        replay detection support: Y  replay window size: 1024
        Status: ACTIVE(ACTIVE)

     outbound ah sas:

     outbound pcp sas:

interface: Tunnel2
    Crypto map tag: Tunnel2-head-0, local addr 1.2.3.4

   protected vrf: (none)
   local  ident (addr/mask/prot/port): (1.2.3.4/255.255.255.255/47/0)
   remote ident (addr/mask/prot/port): (3.3.3.3/255.255.255.255/47/0)
   current_peer 3.3.3.3 port 4500
     PERMIT, flags={{origin_is_acl,}}
    #pkts encaps: 13133657, #pkts encrypt: 13133657, #pkts digest: 13133657
    #pkts decaps: 12013064, #pkts decrypt: 12013064, #pkts verify: 12013064
    #pkts compressed: 0, #pkts decompressed: 0
    #pkts not compressed: 0, #pkts compr. failed: 0
    #pkts not decompressed: 0, #pkts decompress failed: 0
    #pkts no sa (send) 0, #pkts invalid sa (rcv) 0
    #pkts encaps failed (send) 0, #pkts decaps failed (rcv) 0
    #pkts invalid prot (recv) 0, #pkts verify failed: 0
    #pkts invalid identity (recv) 0, #pkts invalid len (rcv) 0
    #pkts replay rollover (send): 0, #pkts replay rollover (rcv) 0
    ##pkts replay failed (rcv): 1
    #pkts tagged (send): 0, #pkts untagged (rcv): 0
    #pkts not tagged (send): 0, #pkts not untagged (rcv): 0
    #pkts internal err (send): 0, #pkts internal err (recv) 0

     local crypto endpt.: 1.2.3.4, remote crypto endpt.: 3.3.3.3
     plaintext mtu 1442, path mtu 1500, ip mtu 1500, ip mtu idb GigabitEthernet8
     current outbound spi: 0x4321DCBA(0987612345)
     PFS (Y/N): N, DH group: none

     inbound esp sas:
      spi: 0x1234DCBA(4321567890)
        transform: esp-256-aes esp-sha-hmac ,
        in use settings ={{Transport UDP-Encaps, }}
        conn id: 457, flow_id: Onboard VPN:457, sibling_flags 80000000, crypto map: Tunnel2-head-0
        sa timing: remaining key lifetime (k/sec): (4272028/2813)
        IV size: 16 bytes
        replay detection support: Y  replay window size: 1024
        Status: ACTIVE(ACTIVE)

     inbound ah sas:

     inbound pcp sas:

     outbound esp sas:
      spi: 0x4321DCBA(0987612345)
        transform: esp-256-aes esp-sha-hmac ,
        in use settings ={{Transport UDP-Encaps, }}
        conn id: 456, flow_id: Onboard VPN:456, sibling_flags 80000000, crypto map: Tunnel2-head-0
        sa timing: remaining key lifetime (k/sec): (4272026/2813)
        IV size: 16 bytes
        replay detection support: Y  replay window size: 1024
        Status: ACTIVE(ACTIVE)

     outbound ah sas:

     outbound pcp sas:
```

**Help:** execute the command "show crypto ipsec sa detail"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show capability feature routing

**Output:**
```
Displaying capability information for all available features: 
L3VPN Inter-AS Hybrid: Enabled 
L3VPN PE-CE Link Protection: Enabled 
OSPF nssa-only: Enabled 
OSPF Connected prefix suppression: Enabled 
OSPF support of RFC3101: Enabled 
OSPF prefix priority: Enabled 
OSPFv3 IPsec auth/encr: Enabled 
 OSPFv3 BFD: Enabled 
OSPFv3 Graceful Restart: Enabled 
OSPFv3 Address Families: Enabled 
OSPFv3 PE-CE: Enabled 
OSPFv3 external path preference: Enabled 
 OSPFv3 Stub Router Advertisement: Enabled 
OSPFv3 support of RFC3101: Enabled 

```

**Help:** execute the command "show capability feature routing"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show bfd neighbors details

**Output:**
```
OurAddr       NeighAddr      LD/RD  RH/RS    Holdown(mult)  State     Int
172.16.1.1    172.16.1.3     5/3    1(RH)    150 (3 )       Up   Fa0/1       
Session state is UP and not using echo function.
Local Diag: 0, Demand mode: 0, Poll bit: 0
MinTxInt: 50000, MinRxInt: 50000, Multiplier: 3
Received MinRxInt: 50000, Received Multiplier: 3
Holdown (hits): 150(0), Hello (hits): 50(1364284)
Rx Count: 1351813, Rx Interval (ms) min/max/avg: 28/64/49 last: 4 ms ago
Tx Count: 1364289, Tx Interval (ms) min/max/avg: 40/68/49 last: 32 ms ago
Registered protocols: EIGRP
Uptime: 18:42:45
Last packet: Version: 0            - Diagnostic: 0
             I Hear You bit: 1     - Demand bit: 0
             Poll bit: 0           - Final bit: 0
             Multiplier: 3         - Length: 24
             My Discr.: 3          - Your Discr.: 5
             Min tx interval: 50000    - Min rx interval: 50000
             Min Echo interval: 0

OurAddr       NeighAddr     LD/RD  RH/RS   Holdown(mult)  State     Int
172.16.1.1    172.16.1.2     6/1    Up        0    (3 )   Up        Fa0/1       
Session state is UP and using echo function with 50 ms interval.
Local Diag: 0, Demand mode: 0, Poll bit: 0
MinTxInt: 1000000, MinRxInt: 1000000, Multiplier: 3
Received MinRxInt: 1000000, Received Multiplier: 3
Holdown (hits): 3000(0), Hello (hits): 1000(317)
Rx Count: 305, Rx Interval (ms) min/max/avg: 1/1016/887 last: 448 ms ago
Tx Count: 319, Tx Interval (ms) min/max/avg: 1/1008/880 last: 532 ms ago
Registered protocols: EIGRP
Uptime: 00:04:30
Last packet: Version: 1            - Diagnostic: 0
             State bit: Up         - Demand bit: 0
             Poll bit: 0           - Final bit: 0
             Multiplier: 3         - Length: 24
             My Discr.: 1          - Your Discr.: 6
             Min tx interval: 1000000    - Min rx interval: 1000000
             Min Echo interval: 50000

```

**Help:** execute the command "show bfd neighbors details"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show vrrp all

**Output:**
```

GigabitEthernet0/0 - Group 1 - Address-Family IPv4
  State is MASTER
  State duration 37 mins 23.080 secs
  Virtual IP address is 10.0.1.1
  Virtual MAC address is 0000.5E00.0101
  Advertisement interval is 1000 msec
  Preemption enabled
  Priority is 110
    Track object 1 state UP decrement 10
  Master Router is 10.0.1.2 (local), priority is 110
  Master Advertisement interval is 1000 msec (expires in 32 msec)
  Master Down interval is unknown

GigabitEthernet0/0 - Group 6 - Address-Family IPv6
  State is MASTER
  State duration 37 mins 22.120 secs
  Virtual IP address is FE80::1:1
  Virtual MAC address is 0000.5E00.0206
  Advertisement interval is 1000 msec
  Preemption enabled
  Priority is 110
    Track object 1 state UP shutdown
  Master Router is FE80::1:A (local), priority is 110
  Master Advertisement interval is 1000 msec (expires in 260 msec)
  Master Down interval is unknown


GigabitEthernet0/0.4010 - Group 1 - Address-Family IPv4
  State is BACKUP
  State duration 37 mins 14.859 secs
  Virtual IP address is 10.254.1.1
  Virtual MAC address is 0000.5E00.0101
  Advertisement interval is 1000 msec
  Preemption enabled
  Priority is 110
  Master Router is 10.254.1.3, priority is 120
  Master Advertisement interval is 1000 msec (learned)
  Master Down interval is 3570 msec (expires in 3194 msec)

GigabitEthernet0/0.4010 - Group 6 - Address-Family IPv6
  State is BACKUP
  State duration 37 mins 13.888 secs
  Virtual IP address is FE80::4010:1
  Virtual MAC address is 0000.5E00.0206
  Advertisement interval is 1000 msec
  Preemption enabled
  Priority is 110
  Master Router is FE80::4010:3, priority is 120
  Master Advertisement interval is 1000 msec (learned)
  Master Down interval is 3570 msec (expires in 3420 msec)


GigabitEthernet0/0.2600 - Group 1 - Address-Family IPv4
  State is BACKUP
  State duration 2 mins 48.646 secs
  Virtual IP address is 172.26.0.1
  Virtual MAC address is 0000.5E00.0101
  Advertisement interval is 1000 msec
  Preemption enabled
  Priority is 90 (Configured 110)
    Track object 2 state DOWN decrement 20
  Master Router is 172.26.0.3, priority is 100
  Master Advertisement interval is 1000 msec (learned)
  Master Down interval is 3648 msec (expires in 3427 msec)

GigabitEthernet0/0.2600 - Group 6 - Address-Family IPv6
  State is INIT (Group is shutdown - Tracked object down)
  State duration 8 mins 57.183 secs
  Virtual IP address is FE80::2600:1
  Virtual MAC address is 0000.5E00.0206
  Advertisement interval is 1000 msec
  Preemption enabled
  Priority is 110
    Track object 2 state DOWN shutdown
  Master Router is unknown, priority is unknown
  Master Advertisement interval is unknown
  Master Down interval is unknown



```

**Help:** execute the command "show vrrp all"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show environment temperature

**Output:**
```
Switch 1: SYSTEM TEMPERATURE is OK
Inlet Temperature Value: 29 Degree Celsius
Temperature State: GREEN
Yellow Threshold : 46 Degree Celsius
Red Threshold    : 56 Degree Celsius

Hotspot Temperature Value: 67 Degree Celsius
 Temperature State: GREEN
Yellow Threshold : 105 Degree Celsius
Red Threshold    : 125 Degree Celsius
Switch 2: SYSTEM TEMPERATURE is OK
Inlet Temperature Value: 28 Degree Celsius
Temperature State: GREEN
Yellow Threshold : 46 Degree Celsius
Red Threshold    : 56 Degree Celsius

Hotspot Temperature Value: 69 Degree Celsius
Temperature State: GREEN
Yellow Threshold : 105 Degree Celsius
 Red Threshold    : 125 Degree Celsius
```

**Help:** execute the command "show environment temperature"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show vlan

**Output:**
```
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Gi0/1
10   Management                       active    
50   VLan50                           active    Fa0/1, Fa0/2, Fa0/3, Fa0/4, Fa0/5, Fa0/6, Fa0/7, Fa0/8, Fa0/9
                                                Fa0/10, Fa0/11, Fa0/12
60   VLan60                           active    Fa0/13, Fa0/14, Fa0/15, Fa0/16, Fa0/17, Fa0/18, Fa0/19, Fa0/20
                                                Fa0/21, Fa0/22, Fa0/23, Fa0/24
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 

VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
1    enet  100001     1500  -      -      -        -    -        0      0   
10   enet  100010     1500  -      -      -        -    -        0      0   
50   enet  100050     1500  -      -      -        -    -        0      0   
60   enet  100060     1500  -      -      -        -    -        0      0   
1002 fddi  101002     1500  -      -      -        -    -        0      0   
1003 tr    101003     1500  -      -      -        -    srb      0      0   
1004 fdnet 101004     1500  -      -      -        ieee -        0      0   
1005 trnet 101005     1500  -      -      -        ibm  -        0      0   

Remote SPAN VLANs
------------------------------------------------------------------------------
 

Primary Secondary Type              Ports
------- --------- ----------------- ------------------------------------------

```

**Help:** execute the command "show vlan"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip source binding

**Output:**
```
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
DC:A9:04:80:02:0F   192.168.1.48     583720      dhcp-snooping   1     GigabitEthernet1/0/9
8C:85:90:8E:AC:13   192.168.1.66     583795      dhcp-snooping   1     GigabitEthernet1/0/9
9C:A0:B0:16:26:D2   192.168.1.104    591457      dhcp-snooping   1     GigabitEthernet1/0/9
 Total number of bindings: 3

```

**Help:** execute the command "show ip source binding"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show power available

**Output:**
```
Power Summary                      Maximum
 (in Watts)              Used     Available
----------------------   ----     ---------
System Power (12V)        575         750
Inline Power (-50V)         0           0
Backplane Power (3.3V)      0           0
----------------------   ----     ---------
Total                     575         750


```

**Help:** execute the command "show power available"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ap cdp neighbors

**Output:**
```
Number of neighbors: 4

AP Name                          AP IP                                     Neighbor Name                              Neighbor IP        Neighbor Port
-------------------------------------------------------------------------------------------------------------------------------------------------------------
AP-INDOOR-01                     192.0.2.1                                 sw-test-123.local.lan                      192.0.2.101       GigabitEthernet1/0/1     
AP-INDOOR-02                     192.0.2.2                                 sw_test                                    192.0.2.103       Ethernet1/1     
AP-OUTDOOR-01                    192.0.2.3                                 sw456.example.lan                          192.2.0.67        TenGigabitEthernet1/0/10.45     
AP-OUTDOOR-02                    2001:db8:abc:def::1234                    sw456.example.lan                          192.2.0.67        TenGigabitEthernet1/0/10.45     

```

**Help:** execute the command "show ap cdp neighbors"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip interface brief

**Output:**
```
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                unassigned      YES NVRAM  up                    up
Ethernet0/0.11             10.0.1.38       YES NVRAM  up                    up
Ethernet0/1                1.1.1.1         YES NVRAM  up                    up
Ethernet0/2                unassigned      YES NVRAM  administratively down down
Ethernet0/3                unassigned      YES NVRAM  administratively down down
Loopback0                  10.0.1.2        YES NVRAM  up                    up

```

**Help:** execute the command "show ip interface brief"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show vrf

**Output:**
```
  Name                             Default RD            Protocols   Interfaces
  OOB-MGMT                         <not set>             ipv4        Gi0/3
  vpn21                            65201:21              ipv4,ipv6   Gi0/0.21
                                                                     Gi0/1.21
  vpn22                            65201:22              ipv4        

```

**Help:** execute the command "show vrf"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show interfaces status

**Output:**
```

--------------------------------------------------------------------------------
Port          Name               Status    Vlan      Duplex  Speed   Type
 --------------------------------------------------------------------------------
 fc2/1 is up    Port mode is NP
fc2/2 is up    Port mode is NP
fc2/3 is up    Port mode is NP
fc2/4 is up    Port mode is NP
fc2/5 is down (SFP not present)
fc2/6 is down (SFP not present)
Eth1/1        XXXXXXX1_bond1_Act connected 111       full    1000    SFP-1000BAS
Eth1/2        XXXXXXX3_bond1_Act connected 112       full    1000    SFP-1000BAS
Eth1/3        YYYYYYYY1_ha1      connected 115       full    1000    SFP-1000BAS
Eth1/4        ZZZZZZZZZZZZZ1_tru connected trunk     full    10G     10Gbase-SR
Eth1/5        ZZZZZZZZZZZZZ1_tru connected trunk     full    10G     10Gbase-SR
Eth1/6        AAAAAAAAA1_po2     connected trunk     full    1000    SFP-1000BAS
Eth1/7        BBBBBBBB10-1       connected 4093      full    10G     Fabric Exte
Eth1/8        BBBBBBBB10-1       connected 4093      full    10G     Fabric Exte
Eth1/9        BBBBBBBB11-1       connected 4093      full    10G     Fabric Exte
Eth1/10       BBBBBBBB11-1       connected 4093      full    10G     Fabric Exte

```

**Help:** execute the command "show interfaces status"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show isis neighbors

**Output:**
```

System Id       Type Interface     IP Address      State Holdtime Circuit Id
vMX1            L1   Gi2           10.1.2.1        UP    19       XRv3.03
vMX1            L2   Gi2           10.1.2.1        UP    24       XRv3.03
XRv3            L1   Gi2           10.1.2.3        UP    8        XRv3.03
XRv3            L2   Gi2           10.1.2.3        UP    7        XRv3.03
vEOS4           L2   Gi3           10.2.4.4        UP    23       0F

```

**Help:** execute the command "show isis neighbors"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip ospf database

**Output:**
```
OSPF Router with id(192.168.239.66) (Process ID 300)
                 Displaying Router Link States(Area 0.0.0.0)
  Link ID       ADV Router    Age        Seq#     Checksum  Link count
172.16.21.6   172.16.21.6    1731    0x80002CFB    0x69BC       8
172.16.21.5   172.16.21.5    1112    0x800009D2    0xA2B8       5
172.16.1.2    172.16.1.2     1662    0x80000A98    0x4CB6       9
                Displaying Net Link States(Area 0.0.0.0)
  Link ID       ADV Router      Age        Seq#        Checksum
172.16.1.3  192.168.239.66     1245    0x800000EC      0x82E
                Displaying Summary Net Link States(Area 0.0.0.0)
  Link ID       ADV Router       Age        Seq#        Checksum
172.16.240.0   172.16.241.5    1152      0x80000077      0x7A05
                Displaying Summary Net Link States(Area 1)
  Link ID       ADV Router       Age        Seq#        Checksum
172.16.240.0   172.16.241.5    1152      0x80000077      0x7A05
172.16.241.0   172.16.241.5    1152      0x80000070      0xAEB7
		Type-5 AS External Link States

 Link ID         ADV Router      Age         Seq#       Checksum Tag
192.168.1.0     0.0.0.3         542         0x80000001 0x003F23 0
192.168.1.128   0.0.0.3         565         0x80000001 0x007C05 0
192.168.1.160   0.0.0.3         567         0x80000001 0x003B26 0

```

**Help:** execute the command "show ip ospf database"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show route-map

**Output:**
```
route-map equal, permit, sequence 10
   Match clauses:
     length 150 200
   Set clauses:
     ip next-hop 10.10.11.254
   Policy routing matches: 0 packets, 0 bytes
route-map equal, permit, sequence 20
  Match clauses:
    ip address prefix-lists: PFX
    ip address (access-lists): 101
  Set clauses:
    ip next-hop 10.10.11.14
  Policy routing matches: 144 packets, 15190 bytes

```

**Help:** execute the command "show route-map"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show adjacency

**Output:**
```
Protocol Interface                 Address
IP       Vlan1                     10.255.1.1(11)
IP       Vlan1                     10.255.1.11(8)
IP       Vlan1                     10.255.1.250(8)
IP       Vlan1                     227.0.0.0(3)
```

**Help:** execute the command "show adjacency"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show access-session

**Output:**
```


Interface    Identifier     Method  Domain  Status Fg Session ID
Gi1/0/10     c89a.12cd.3b74 dot1x   DATA    Auth      0A0A1DFE00000FB3000101FF
Gi1/0/5      848a.12cd.3636 mab     VOICE   Auth      0A0A1DFE00000FBD000101FF
Gi2/0/33     848a.12cd.3624 mab     VOICE   Auth      0A0A1DFE00000FBA000101FF
Gi1/0/26     005a.12cd.3567 N/A     UNKNOWN Unauth    0A0A1DFE00001F8D160101FF
Gi1/0/26     004a.12cd.3c40 mab     DATA    Auth      0A0A1DFE00001C8D5E0101FF
Gi1/0/43     848a.12cd.3db2 mab     VOICE   Auth      0A0A1DFE00000FC8000101FF
Gi1/0/20     54ea.12cd.3568 dot1x   DATA    Auth      0A0A1DFE000013DF820101FF
Gi2/0/1      002a.12cd.3906 mab     DATA    Auth      0A0A1DFE00000FB2000101FF
Gi1/0/21     b4ba.12cd.3f3b mab     VOICE   Auth      0A0A1DFE00000FCC000101FF
Gi1/0/40     002a.12cd.3d7d mab     DATA    Auth      0A0A1DFE00001D3B990101FF
Gi1/0/39     8c8a.12cd.3c83 dot1x   DATA    Auth      0A0A1DFE000010EE7C0101FF
Gi1/0/41     54ea.12cd.32e3 dot1x   DATA    Auth      0A0A1DFE00000FD6000101FF
Gi1/0/16     848a.12cd.35b8 mab     VOICE   Auth      0A0A1DFE00000FC2000101FF
Gi1/0/31     54ea.12cd.32dc dot1x   DATA    Auth      0A0A1DFE00000FD3000101FF
Gi1/0/22     848a.12cd.3626 mab     VOICE   Auth      0A0A1DFE00000FCD000101FF
Gi1/0/12     c89a.12cd.3be0 dot1x   DATA    Auth      0A0A1DFE00000FB6000101FF
Gi1/0/43     106a.12cd.36a4 mab     DATA    Auth      0A0A1DFE00000FB5000101FF
Gi1/0/46     347a.12cd.3aae mab     VOICE   Auth      0A0A1DFE0000201A380101FF
Gi1/0/15     347a.12cd.3bf5 mab     VOICE   Auth      0A0A1DFE00000FFD110101FF
Gi1/0/31     848a.12cd.3d3d mab     VOICE   Auth      0A0A1DFE00000FCE000101FF
Gi1/0/30     347a.12cd.3c00 mab     VOICE   Auth      0A0A1DFE00000FC6000101FF
Gi1/0/3      848a.12cd.35c3 mab     VOICE   Auth      0A0A1DFE00000FBE000101FF
Gi1/0/45     8c8a.12cd.3636 dot1x   DATA    Auth      0A0A1DFE00000FD8000101FF
Gi1/0/37     c89a.12cd.329d dot1x   DATA    Auth      0A0A1DFE00000FD5000101FF
Gi1/0/5      8c8a.12cd.3096 dot1x   DATA    Auth      0A0A1DFE00000FB4000101FF
Gi1/0/46     54ea.12cd.3325 dot1x   DATA    Auth      0A0A1DFE00002019380101FF
Gi2/0/1      848a.12cd.3615 mab     VOICE   Auth      0A0A1DFE00000FBB000101FF
Gi1/0/12     848a.12cd.34a6 mab     VOICE   Auth      0A0A1DFE00000FC1000101FF
Gi1/0/2      004a.12cd.3c3f mab     DATA    Auth      0A0A1DFE00001FC12D0101FF
Gi2/0/15     1c6a.12cd.317e mab     DATA    Auth      0A0A1DFE00001865F80101FF
Gi1/0/20     848a.12cd.36aa mab     VOICE   Auth      0A0A1DFE00001225F90101FF
Gi1/0/21     8c8a.12cd.38e9 dot1x   DATA    Auth      0A0A1DFE00000FB7000101FF
Gi1/0/37     347a.12cd.345b mab     VOICE   Auth      0A0A1DFE00000FC0000101FF
Gi1/0/45     848a.12cd.35fa mab     VOICE   Auth      0A0A1DFE00000FBF000101FF
Gi1/0/15     54ea.12cd.31ae dot1x   DATA    Auth      0A0A1DFE00000FFE110101FF
Gi1/0/41     848a.12cd.359f mab     VOICE   Auth      0A0A1DFE00000FC4000101FF
Gi1/0/23     848a.12cd.35a3 mab     VOICE   Auth      0A0A1DFE00000FC3000101FF
Gi1/0/1      001a.12cd.3402 mab     DATA    Auth      0A0A1DFE0000164F6A0101FF
Gi1/0/10     848a.12cd.35ec mab     VOICE   Auth      0A0A1DFE00000FC5000101FF
Gi1/0/39     24da.12cd.3b4f mab     VOICE   Auth      0A0A1DFE000010EF7C0101FF
Gi1/0/29     8c8a.12cd.3943 dot1x   DATA    Auth      0A0A1DFE0000202C3F0101FF
 
Session count = 41

Key to Session Events Blocked Status Flags:

  A - Applying Policy (multi-line status for details)
  D - Awaiting Deletion
  F - Final Removal in progress
  I - Awaiting IIF ID allocation
  N - Waiting for AAA to come up
  P - Pushed Session
  R - Removing User Profile (multi-line status for details)
  U - Applying User Profile (multi-line status for details)
  X - Unknown Blocker


```

**Help:** execute the command "show access-session"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip flow toptalkers

**Output:**
```
SrcIf         SrcIPaddress    DstIf         DstIPaddress    Pr SrcP DstP  Pkts
Gi0/2/0.30    10.2.100.83     Null          224.0.0.2       11 07C1 07C1   414
Gi0/2/0.40    10.2.100.99     Null          224.0.0.2       11 07C1 07C1   410

```

**Help:** execute the command "show ip flow toptalkers"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip ospf database router

**Output:**
```
            OSPF Router with ID (100.1.1.1) (Process ID 1)

                Router Link States (Area 0)

  LS age: 14
  Options: (No TOS-capability, DC)
  LS Type: Router Links
  Link State ID: 100.1.1.1
  Advertising Router: 100.1.1.1
  LS Seq Number: 80000206
  Checksum: 0x8A21
  Length: 72
  Number of Links: 4

    Link connected to: a Stub Network
     (Link ID) Network/subnet number: 100.1.1.1
     (Link Data) Network Mask: 255.255.255.255
      Number of MTID metrics: 0
       TOS 0 Metrics: 1

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 192.168.2.1
     (Link Data) Router Interface address: 192.168.2.1
      Number of MTID metrics: 0
       TOS 0 Metrics: 1

    Link connected to: another Router (point-to-point)
     (Link ID) Neighboring Router ID: 100.3.3.3
     (Link Data) Router Interface address: 192.168.1.1
      Number of MTID metrics: 0
       TOS 0 Metrics: 1

    Link connected to: a Stub Network
     (Link ID) Network/subnet number: 192.168.1.0
     (Link Data) Network Mask: 255.255.255.252
      Number of MTID metrics: 0
       TOS 0 Metrics: 1


  LS age: 1694
  Options: (No TOS-capability, DC)
  LS Type: Router Links
  Link State ID: 100.2.2.2
  Advertising Router: 100.2.2.2
  LS Seq Number: 80000202
  Checksum: 0xCA4F
  Length: 60
  Number of Links: 3

    Link connected to: a Stub Network
     (Link ID) Network/subnet number: 100.2.2.2
     (Link Data) Network Mask: 255.255.255.255
      Number of MTID metrics: 0
       TOS 0 Metrics: 1

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 192.168.3.2
     (Link Data) Router Interface address: 192.168.3.1
      Number of MTID metrics: 0
       TOS 0 Metrics: 1

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 192.168.2.1
     (Link Data) Router Interface address: 192.168.2.2
      Number of MTID metrics: 0
       TOS 0 Metrics: 1


  LS age: 15
  Options: (No TOS-capability, DC)
  LS Type: Router Links
  Link State ID: 100.3.3.3
  Advertising Router: 100.3.3.3
  LS Seq Number: 800001FD
  Checksum: 0x3969
  Length: 72
  Number of Links: 4

    Link connected to: a Stub Network
     (Link ID) Network/subnet number: 100.3.3.3
     (Link Data) Network Mask: 255.255.255.255
      Number of MTID metrics: 0
       TOS 0 Metrics: 1

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 192.168.4.2
     (Link Data) Router Interface address: 192.168.4.1
      Number of MTID metrics: 0
       TOS 0 Metrics: 1

    Link connected to: another Router (point-to-point)
     (Link ID) Neighboring Router ID: 100.1.1.1
     (Link Data) Router Interface address: 192.168.1.2
      Number of MTID metrics: 0
       TOS 0 Metrics: 1

    Link connected to: a Stub Network
     (Link ID) Network/subnet number: 192.168.1.0
     (Link Data) Network Mask: 255.255.255.252
      Number of MTID metrics: 0
       TOS 0 Metrics: 1


  LS age: 1752
  Options: (No TOS-capability, DC)
  LS Type: Router Links
  Link State ID: 100.4.4.4
  Advertising Router: 100.4.4.4
  LS Seq Number: 800001F7
  Checksum: 0x5CB0
  Length: 60
  Number of Links: 3

    Link connected to: a Stub Network
     (Link ID) Network/subnet number: 100.4.4.4
     (Link Data) Network Mask: 255.255.255.255
      Number of MTID metrics: 0
       TOS 0 Metrics: 1

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 192.168.4.2
     (Link Data) Router Interface address: 192.168.4.2
      Number of MTID metrics: 0
       TOS 0 Metrics: 1

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 192.168.3.2
     (Link Data) Router Interface address: 192.168.3.2
      Number of MTID metrics: 0
       TOS 0 Metrics: 1

```

**Help:** execute the command "show ip ospf database router"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip cef detail

**Output:**
```
IPv4 CEF is enabled and running
VRF Default
 823 prefixes (823/0 fwd/non-fwd)
 Table id 0x0
 Database epoch:        0 (823 entries at this epoch)

0.0.0.0/0, epoch 0, flags rib only nolabel, rib defined all labels, default route
  NetFlow: Origin AS 0, Peer AS 0, Mask Bits 0
  recursive via 10.181.150.18
    attached to GigabitEthernet0/2
0.0.0.0/8, epoch 0
  NetFlow: Origin AS 0, Peer AS 0, Mask Bits 0
  Special source: drop
  drop
0.0.0.0/32, epoch 0, flags receive
  NetFlow: Origin AS 0, Peer AS 0, Mask Bits 0
  Special source: receive
  receive
10.0.0.0/16, epoch 0
  NetFlow: Origin AS 0, Peer AS 0, Mask Bits 16
  nexthop 10.180.150.33 Port-channel1.1822
10.0.120.0/24, epoch 0, flags rib only nolabel, rib defined all labels
  NetFlow: Origin AS 65005, Peer AS 0, Mask Bits 24
  recursive via 10.181.150.18
    attached to GigabitEthernet0/2
 10.180.140.153/32, epoch 0, flags [attached]
  Interest List:
     - fib bfd tracking
  BFD state up, tracking attached BFD session on GigabitEthernet0/1
  Adj source: IP adj out of GigabitEthernet0/1, addr 10.180.140.153 3ED40F00
    Dependent covered prefix type adjfib, cover 10.180.140.152/29
  1 IPL source [no flags]
  attached to GigabitEthernet0/1
10.180.150.0/26, epoch 0, flags rib only nolabel, rib defined all labels
  NetFlow: Origin AS 0, Peer AS 0, Mask Bits 26
  attached to Null0
10.180.150.5/32, epoch 0, flags attached, connected, receive, local, source eligible
  NetFlow: Origin AS 0, Peer AS 0, Mask Bits 32
  Interface source: Loopback180 flags: local, source eligible
  receive for Loopback180
10.180.150.32/29, epoch 0, flags attached, connected, cover dependents, need deagg
  NetFlow: Origin AS 0, Peer AS 0, Mask Bits 29
  Covered dependent prefixes: 3
    need deagg: 2
    notify cover updated: 1
  attached to Port-channel1.1822
10.180.150.32/32, epoch 0, flags receive
  NetFlow: Origin AS 0, Peer AS 0, Mask Bits 29
  Interface source: Port-channel1.1822 flags: none
  Dependent covered prefix type cover need deagg, cover 10.180.150.32/29
  receive for Port-channel1.1822
10.180.150.33/32, epoch 0, flags attached
  NetFlow: Origin AS 0, Peer AS 0, Mask Bits 29
  Adj source: IP adj out of Port-channel1.1822, addr 10.180.150.33 01F3E080
   Dependent covered prefix type adjfib, cover 10.180.150.32/29
  attached to Port-channel1.1822
10.180.150.38/32, epoch 0, flags receive, local, source eligible
  NetFlow: Origin AS 0, Peer AS 0, Mask Bits 29
  Interface source: Port-channel1.1822 flags: local, source eligible
  receive for Port-channel1.1822
10.180.150.192/26, epoch 0, flags rib only nolabel, rib defined all labels
  NetFlow: Origin AS 65150, Peer AS 0, Mask Bits 26
  recursive via 10.181.150.18
    attached to GigabitEthernet0/2
 10.181.150.0/26, epoch 0, flags rib only nolabel, rib defined all labels
  NetFlow: Origin AS 0, Peer AS 0, Mask Bits 26
  attached to Null0
224.0.0.0/4, epoch 0
  NetFlow: Origin AS 0, Peer AS 0, Mask Bits 0
  Special source: multicast
  multicast
224.0.0.0/24, epoch 0, flags receive
  NetFlow: Origin AS 0, Peer AS 0, Mask Bits 0
  Special source: receive
  receive
240.0.0.0/4, epoch 0
  NetFlow: Origin AS 0, Peer AS 0, Mask Bits 0
  Special source: drop
  drop
255.255.255.255/32, epoch 0, flags receive
  NetFlow: Origin AS 0, Peer AS 0, Mask Bits 0
  Special source: receive
  receive

```

**Help:** execute the command "show ip cef detail"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show authentication sessions

**Output:**
```


Interface    MAC Address    Method  Domain  Status Fg Session ID
------------------------------------------------------------------------------
Gi1/0/10     c89a.12cd.3b74 dot1x   DATA    Auth      0A0A1DFE00000FB3000101FF
Gi1/0/5      848a.12cd.3636 mab     VOICE   Auth      0A0A1DFE00000FBD000101FF
Gi2/0/33     848a.12cd.3624 mab     VOICE   Auth      0A0A1DFE00000FBA000101FF
Gi1/0/26     005a.12cd.3567 N/A     UNKNOWN Unauth    0A0A1DFE00001F8D160101FF
Gi1/0/26     004a.12cd.3c40 mab     DATA    Auth      0A0A1DFE00001C8D5E0101FF
Gi1/0/43     848a.12cd.3db2 mab     VOICE   Auth      0A0A1DFE00000FC8000101FF
Gi1/0/20     54ea.12cd.3568 dot1x   DATA    Auth      0A0A1DFE000013DF820101FF
Gi2/0/1      002a.12cd.3906 mab     DATA    Auth      0A0A1DFE00000FB2000101FF
Gi1/0/21     b4ba.12cd.3f3b mab     VOICE   Auth      0A0A1DFE00000FCC000101FF
Gi1/0/40     002a.12cd.3d7d mab     DATA    Auth      0A0A1DFE00001D3B990101FF
Gi1/0/39     8c8a.12cd.3c83 dot1x   DATA    Auth      0A0A1DFE000010EE7C0101FF
Gi1/0/41     54ea.12cd.32e3 dot1x   DATA    Auth      0A0A1DFE00000FD6000101FF
Gi1/0/16     848a.12cd.35b8 mab     VOICE   Auth      0A0A1DFE00000FC2000101FF
Gi1/0/31     54ea.12cd.32dc dot1x   DATA    Auth      0A0A1DFE00000FD3000101FF
Gi1/0/22     848a.12cd.3626 mab     VOICE   Auth      0A0A1DFE00000FCD000101FF
Gi1/0/12     c89a.12cd.3be0 dot1x   DATA    Auth      0A0A1DFE00000FB6000101FF
Gi1/0/43     106a.12cd.36a4 mab     DATA    Auth      0A0A1DFE00000FB5000101FF
Gi1/0/46     347a.12cd.3aae mab     VOICE   Auth      0A0A1DFE0000201A380101FF
Gi1/0/15     347a.12cd.3bf5 mab     VOICE   Auth      0A0A1DFE00000FFD110101FF
Gi1/0/31     848a.12cd.3d3d mab     VOICE   Auth      0A0A1DFE00000FCE000101FF
Gi1/0/30     347a.12cd.3c00 mab     VOICE   Auth      0A0A1DFE00000FC6000101FF
Gi1/0/3      848a.12cd.35c3 mab     VOICE   Auth      0A0A1DFE00000FBE000101FF
Gi1/0/45     8c8a.12cd.3636 dot1x   DATA    Auth      0A0A1DFE00000FD8000101FF
Gi1/0/37     c89a.12cd.329d dot1x   DATA    Auth      0A0A1DFE00000FD5000101FF
Gi1/0/5      8c8a.12cd.3096 dot1x   DATA    Auth      0A0A1DFE00000FB4000101FF
Gi1/0/46     54ea.12cd.3325 dot1x   DATA    Auth      0A0A1DFE00002019380101FF
Gi2/0/1      848a.12cd.3615 mab     VOICE   Auth      0A0A1DFE00000FBB000101FF
Gi1/0/12     848a.12cd.34a6 mab     VOICE   Auth      0A0A1DFE00000FC1000101FF
Gi1/0/2      004a.12cd.3c3f mab     DATA    Auth      0A0A1DFE00001FC12D0101FF
Gi2/0/15     1c6a.12cd.317e mab     DATA    Auth      0A0A1DFE00001865F80101FF
Gi1/0/20     848a.12cd.36aa mab     VOICE   Auth      0A0A1DFE00001225F90101FF
Gi1/0/21     8c8a.12cd.38e9 dot1x   DATA    Auth      0A0A1DFE00000FB7000101FF
Gi1/0/37     347a.12cd.345b mab     VOICE   Auth      0A0A1DFE00000FC0000101FF
Gi1/0/45     848a.12cd.35fa mab     VOICE   Auth      0A0A1DFE00000FBF000101FF
Gi1/0/15     54ea.12cd.31ae dot1x   DATA    Auth      0A0A1DFE00000FFE110101FF
Gi1/0/41     848a.12cd.359f mab     VOICE   Auth      0A0A1DFE00000FC4000101FF
Gi1/0/23     848a.12cd.35a3 mab     VOICE   Auth      0A0A1DFE00000FC3000101FF
Gi1/0/1      001a.12cd.3402 mab     DATA    Auth      0A0A1DFE0000164F6A0101FF
Gi1/0/10     848a.12cd.35ec mab     VOICE   Auth      0A0A1DFE00000FC5000101FF
Gi1/0/39     24da.12cd.3b4f mab     VOICE   Auth      0A0A1DFE000010EF7C0101FF
Gi1/0/29     8c8a.12cd.3943 dot1x   DATA    Auth      0A0A1DFE0000202C3F0101FF
 
Session count = 41

Key to Session Events Blocked Status Flags:

  A - Applying Policy (multi-line status for details)
  D - Awaiting Deletion
  F - Final Removal in progress
  I - Awaiting IIF ID allocation
  N - Waiting for AAA to come up
  P - Pushed Session
  R - Removing User Profile (multi-line status for details)
  U - Applying User Profile (multi-line status for details)
  X - Unknown Blocker


```

**Help:** execute the command "show authentication sessions"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip eigrp topology

**Output:**
```
IP-EIGRP Topology Table for AS(100)/ID(10.255.11.6)

Codes: P - Passive, A - Active, U - Update, Q - Query, R - Reply,
       r - reply Status, s - sia Status

P 66.128.208.232/32, 2 successors, FD is 264448
        via 10.254.11.9, TenGigabitEthernet1/1
        via 10.254.11.33, TenGigabitEthernet2/1
P 10.254.6.8/30, 1 successors, FD is 1024
        via 10.254.6.14, Port-channel10
P 67.230.223.128/28, 2 successors, FD is 5632, tag is 53471
        via 10.254.11.9, TenGigabitEthernet1/1
        via 10.254.11.33, TenGigabitEthernet2/1
P 10.255.10.5/32, 1 successors, FD is 130816
        via 10.254.10.34, GigabitEthernet9/29
P 10.255.1.14/32, 1 successors, FD is 128768
        via 10.254.1.34, Port-channel3
P 10.254.2.12/30, 1 successors, FD is 768
        via 10.254.2.22, TenGigabitEthernet3/3
P 10.255.11.4/32, 4 successors, FD is 128768
        via 10.254.56.6, TenGigabitEthernet1/4
        via 10.254.55.6, TenGigabitEthernet1/6
        via 10.254.11.33, TenGigabitEthernet2/1
        via 10.254.11.9, TenGigabitEthernet1/1
        via 10.254.52.6, TenGigabitEthernet1/5
        via 10.254.4.10, TenGigabitEthernet4/4
        via 10.254.4.14, TenGigabitEthernet4/5
        via 10.254.54.6, TenGigabitEthernet1/3

IP-EIGRP Topology Table for AS(65000)/ID(10.2.0.1)

Codes: P - Passive, A - Active, U - Update, Q - Query, R - Reply,
       r - reply Status, s - sia Status

P 10.50.20.4/32, 2 successors, FD is 128039168
        via 10.4.0.1, GigabitEthernet1/1
        via 10.4.0.2, GigabitEthernet1/2
P 10.50.21.0/27, 0 successors, FD is Inaccessible, tag is 6508497
        via 10.4.0.1, GigabitEthernet1/1
        via 10.4.0.2, GigabitEthernet1/2
 P 10.50.75.0/24, 1 successors, FD is 2816
        via Rstatic
P 10.50.23.92/30, 1 successors, FD is 3840256, tag is 5507497
        via Redistributed

```

**Help:** execute the command "show ip eigrp topology"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show vtp status

**Output:**
```
VTP Version capable             : 1 to 3
VTP version running             : 1
VTP Domain Name                 : router_vtp
VTP Pruning Mode                : Disabled
VTP Traps Generation            : Disabled
Device ID                       : e05f.dead.beef
Configuration last modified by 10.0.0.1 at 6-12-15 14:06:57
Local updater ID is 10.1.1.1 on interface Vl1 (lowest numbered VLAN interface found)

Feature VLAN:
--------------
VTP Operating Mode                : Server
Maximum VLANs supported locally   : 1005
Number of existing VLANs          : 20
Configuration Revision            : 38
MD5 digest                        : 0xFF 0xFF 0xFF 0xFF 0xFF 0xFF 0xFF 0xFF 
                                    0x89 0x07 0xE4 0x53 0xBA 0xB1 0x1C 0xC1 

```

**Help:** execute the command "show vtp status"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ipv6 neighbors

**Output:**
```
IPv6 Address                              Age Link-layer Addr State Interface
2402:1234:106:100:793A:F08D:5B3A:EF89      33 54e1.addb.200f  STALE Vl6
2402:1234:106:100:A193:9153:7CAF:9802       1 54e1.addb.200f  STALE Vl6
2402:1234:106:100:B419:F5DF:B315:F3C5     144 0800.2729.8bc1  STALE Vl6
2402:1234:106:100:B8F1:D9D3:A5F1:C1C9       4 507b.9dcd.c2ae  STALE Vl6
2402:1234:106:100:CC71:364E:A3E7:62B8      36 507b.9dcd.c2ae  STALE Vl6
FE80::5AAC:78FF:FEF8:CCCC                  23 58ac.78f8.cccc  STALE Vl6
FE80::7A0C:F0FF:FE8E:2FF4                 103 780c.f08e.2ff4  STALE Vl6
FE80::7EAD:74FF:FE85:B86                   22 7cad.7485.0c16  STALE Vl6
FE80::208:E3FF:FEFF:FC28                    0 0008.e3ff.fc28  REACH Vl687
FE80::9277:EEFF:FE9B:4E00                   - -               REACH Di0

```

**Help:** execute the command "show ipv6 neighbors"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show running-config partition route-map

**Output:**
```
route-map BGP_IN permit 100
 match ip address prefix-list BGP_IN
 set local-preference 200
route-map BGP_IN permit 110
 match community 500
 set community no-advertise
route-map BGP_IN permit 120
 match community 11167_4000
 set local-preference 200
route-map BGP_OUT permit 50
 match community 4
 set as-path prepend 65005 65005 65005
 set community 11167:5000 additive
 route-map BGP_OUT permit 100
 match ip address prefix-list BGP_OUT
 set community 11167:5000

```

**Help:** execute the command "show running-config partition route-map"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show archive

**Output:**
```
 Archive feature not enabled
```

**Help:** execute the command "show archive"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show running-config partition access-list

**Output:**
```
ip access-list extended filter01
 20 deny   udp any host 200.10.11.135 eq 5060
 30 deny   tcp any 200.10.0.0 0.0.255.255 eq telnet
 40 deny   tcp any any eq telnet
 50 deny   ip 210.144.0.0 0.15.255.255 any
 280 deny   53 any any
 290 deny   55 any any
 300 deny   77 any any
 310 deny   pim any any
 320 remark Vodafone BGP
 320 permit icmp host 113.17.12.113 host 113.17.12.114
 330 permit icmp host 113.117.249.33 host 113.117.249.34
 340 permit icmp host 8.8.8.8 host 113.17.12.114
 350 permit icmp host 8.8.8.8 host 113.117.249.34
 360 permit icmp host 203.109.180.181 host 113.17.12.114
 370 permit icmp host 203.109.180.181 host 113.117.249.34
 380 permit icmp host 108.170.247.49 host 113.17.12.114
 390 permit icmp host 108.170.247.49 host 113.117.249.34
 400 permit icmp any host 113.17.12.114 echo-reply
 410 permit icmp host 203.50.13.93 host 113.17.12.114
 420 permit icmp host 203.50.13.93 host 113.117.249.34
 430 permit icmp any host 113.117.249.34 echo-reply
 440 permit tcp host 113.17.12.113 host 113.17.12.114 eq bgp
 450 permit tcp host 113.17.70.169 host 113.117.249.34 eq bgp
ip access-list extended nineoneone
 20 deny   udp any host 200.10.11.135 eq 5060
 30 deny   tcp any 200.10.0.0 0.0.255.255 eq telnet
 40 deny   tcp any any eq telnet
 50 deny   ip 210.144.0.0 0.15.255.255 any
 280 deny   53 any any
 290 deny   55 any any
 300 deny   77 any any
 310 deny   pim any any
 320 remark Vodafone BGP
 320 permit icmp host 113.17.12.113 host 113.17.12.114
 330 permit icmp host 113.117.249.33 host 113.117.249.34
 340 permit icmp host 8.8.8.8 host 113.17.12.114
 350 permit icmp host 8.8.8.8 host 113.117.249.34
 360 permit icmp host 203.109.180.181 host 113.17.12.114
 370 permit icmp host 203.109.180.181 host 113.117.249.34
 380 permit icmp host 108.170.247.49 host 113.17.12.114
 390 permit icmp host 108.170.247.49 host 113.117.249.34
 400 permit icmp any host 113.17.12.114 echo-reply
 410 permit icmp host 203.50.13.93 host 113.17.12.114
 420 permit icmp host 203.50.13.93 host 113.117.249.34
 430 permit icmp any host 113.117.249.34 echo-reply
 440 permit tcp host 113.17.12.113 host 113.17.12.114 eq bgp
 450 permit tcp host 113.17.70.169 host 113.117.249.34 eq bgp
 460 permit icmp host 10.10.10.10 any echo-reply
 470 permit icmp host 10.10.10.10 any administratively-prohibited
 480 permit icmp host 10.10.10.10 any unreachable log
 490 permit icmp 10.10.10.0 0.0.0.255 20.20.0.0 0.0.255.255 port-unreachable
 500 permit icmp host 1.1.11.1 host 1.1.22.4 echo-reply log-input
 510 permit tcp any any match-all +ack -fin log
 520 permit tcp any any match-any +ack -fin log
 521 permit tcp any any match-any +ack +fin +syn +psh
 530 permit tcp any 10.1.0.0 0.0.255.255 established psh

```

**Help:** execute the command "show running-config partition access-list"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show cdp neighbors detail

**Output:**
```
-------------------------
Device ID: desktop-switch
Entry address(es):
  IP address: 10.1.1.2
Platform: cisco WS-C2960-8TC-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet1/0/16,  Port ID (outgoing port): GigabitEthernet0/1
 Holdtime : 164 sec

Version :
Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE9, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
 Copyright (c) 1986-2014 by Cisco Systems, Inc.
Compiled Mon 03-Mar-14 22:53 by prod_rel_team

advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010205010000000000000024508ECA00FF0000
 VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
  IP address: 10.1.1.2

-------------------------
Device ID: ce-router
 Entry address(es):
  IP address: 10.1.1.1
Platform: Cisco 3825,  Capabilities: Router Switch IGMP
Interface: GigabitEthernet1/0/22,  Port ID (outgoing port): GigabitEthernet0/0
Holdtime : 156 sec

Version :
Cisco IOS Software, 3800 Software (C3825-ADVENTERPRISEK9-M), Version 12.4(24)T1, RELEASE SOFTWARE (fc3)
 Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2009 by Cisco Systems, Inc.
Compiled Fri 19-Jun-09 18:40 by prod_rel_team

advertisement version: 2
VTP Management Domain: ''
Duplex: full
Management address(es):
 
-------------------------
Device ID: server
Entry address(es):
  IP address: 10.1.1.232
Platform: VMware,  Capabilities: Host
Interface: GigabitEthernet1/0/19,  Port ID (outgoing port): eth0
Holdtime : 145 sec

Version :
Linux 2.6.32-431.20.3.el6.x86_64 #1 SMP Fri Jun 6 18:30:54 EDT 2014 CCM:10.5.2.10000-5.i386

advertisement version: 2
Duplex: full
Management address(es):

-------------------------
 Device ID: vIOS-L2-1
Entry address(es):
Platform: Cisco ,  Capabilities: Router Switch IGMP
Interface: GigabitEthernet0/3,  Port ID (outgoing port): GigabitEthernet0/3
 Holdtime : 173 sec

Version :
Cisco IOS Software, vios_l2 Software (vios_l2-ADVENTERPRISEK9-M), Version 15.2(CML_NIGHTLY_20150414)FLO_DSGS7, EARLY DEPLOYMENT DEVELOPMENT BUILD, synced to  DSGS_PI5_POSTCOLLAPSE_TEAM_TRACK_CLONE
Technical Support: http://www.cisco.com/techsupport
 Copyright (c) 1986-2015 by Cisco Systems, Inc.
Compiled Wed 15-Apr-15 00:42 by mmen

advertisement version: 2
Native VLAN: 1
Duplex: full


```

**Help:** execute the command "show cdp neighbors detail"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show authentication sessions method details

**Output:**
```
            Interface:  GigabitEthernet1/0/31
               IIF-ID:  0x18438F31
          MAC Address:  cc96.abcd.1234
         IPv6 Address:  Unknown
         IPv4 Address:  10.10.10.190
            User-Name:  CC-96-AA-BB-CC-DD
          Device-type:  Microsoft-Workstation
          Device-name:  MOED-9212345
               Status:  Authorized
               Domain:  DATA
       Oper host mode:  multi-auth
     Oper control dir:  both
      Session timeout:  43200s (server), Remaining: 3574s
       Timeout action:  Reauthenticate
  Acct update timeout:  172800s (local), Remaining: 89824s
    Common Session ID:  0A4014AC0000002F555FD224
      Acct Session ID:  0x00000027
               Handle:  0xe0000025
       Current Policy:  PMAP_DefaultWiredDot1xClosedAuth_1X
 
Local Policies:

Server Policies:
             VN Value:  WALKUPED_VN
      Session-Timeout: 43200 sec
           Vlan Group:  Vlan: 1011
   Interface Template:  PXE-ClosedMode-Template
            SGT Value:  40

Method status list:
       Method           State
        dot1x           Stopped
          mab           Authc Success
```

**Help:** execute the command "show authentication sessions method details"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show redundancy

**Output:**
```
Redundant System Information :
------------------------------
       Available system uptime = 1 hour, 22 minutes
Switchovers system experienced = 0
              Standby failures = 0
        Last switchover reason = none
                 Hardware Mode = Duplex
    Configured Redundancy Mode = sso
     Operating Redundancy Mode = sso
              Maintenance Mode = Disabled
                Communications = Up

Current Processor Information :
-------------------------------
               Active Location = slot 1/5
        Current Software state = ACTIVE
       Uptime in current state = 1 hour, 22 minutes
                 Image Version = Cisco IOS Software, s2t54 Software (s2t54-ADVENTERPRISEK9-M), Version 15.5(1)SY4, RELEASE SOFTWARE (fc4)
Technical Support: http://www.cisco.com/techsupport
 Copyright (c) 1986-2019 by Cisco Systems, Inc.
Compiled Mon 02-Sep-19 07:17 by prod_rel_team
                          BOOT = bootdisk:s2t54-adventerprisek9-mz.SPA.155-1.SY4.bin,1;
                   CONFIG_FILE = 
                       BOOTLDR = 
        Configuration register = 0x2102

Peer Processor Information :
----------------------------
              Standby Location = slot 2/5
        Current Software state = STANDBY HOT 
       Uptime in current state = 19 minutes
                 Image Version = Cisco IOS Software, s2t54 Software (s2t54-ADVENTERPRISEK9-M), Version 15.5(1)SY4, RELEASE SOFTWARE (fc4)
Technical Support: http://www.cisco.com/techsupport
 Copyright (c) 1986-2019 by Cisco Systems, Inc.
Compiled Mon 02-Sep-19 07:17 by prod_rel_team
                          BOOT = bootdisk:s2t54-adventerprisek9-mz.SPA.155-1.SY4.bin,1;
                   CONFIG_FILE = 
                       BOOTLDR = 
        Configuration register = 0x2102
```

**Help:** execute the command "show redundancy"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show boot

**Output:**
```
2960l#show boot
BOOT path-list : flash:c2960l-universalk9-mz.152-7.E2/c2960l-universalk9-mz.152-7.E2.bin
 Config file : flash:/config.text
Private Config file : flash:/private-config.text
 Enable Break : yes
Manual Boot : no
Allow Dev Key : yes
HELPER path-list :
Boot optimization : disabled
NVRAM/Config file
buffer size: 524288
Timeout for Config
Download: 0 seconds
Config Download
via DHCP: disabled (next boot: disabled)

```

**Help:** execute the command "show boot"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show inventory

**Output:**
```
NAME: "3640 chassis", DESCR: "3640 chassis"
PID:                   , VID: 0xFF, SN: FF1045C5

NAME: "One port Fastethernet TX", DESCR: "One port Fastethernet TX"
PID: NM-1FE-TX=        , VID: 1.0, SN: 7720321
 
NAME: "One port Fastethernet TX", DESCR: "One port Fastethernet TX"
 PID: NM-1FE-TX=        , VID: 1.0, SN: 7720321

NAME: "One port Fastethernet TX", DESCR: "One port Fastethernet TX"
PID: NM-1FE-TX=        , VID: 1.0, SN: 7720321


```

**Help:** execute the command "show inventory"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip bgp vpnv4 all neighbors

**Output:**
```
BGP neighbor is 10.255.11.4,  vrf VRF11,  remote AS 65514,  local AS 65534, external link
  BGP version 4, remote router ID 10.255.255.6
  BGP state = Established, up for 2w6d
  Last read 00:00:54, last write 00:00:35, hold time is 180, keepalive interval is 60 seconds
  Neighbor sessions:
    1 active, is not multisession capable (disabled)
  Neighbor capabilities:
    Route refresh: advertised and received(new)
    Four-octets ASN Capability: advertised and received
    Address family IPv4 Unicast: advertised and received
    Enhanced Refresh Capability: advertised and received
    Multisession Capability: 
    Stateful switchover support enabled: NO for session 1
  Message statistics:
    InQ depth is 0
    OutQ depth is 0
    
                         Sent       Rcvd
    Opens:                  1          1
    Notifications:          0          0
    Updates:                1          2
    Keepalives:         32792      32803
    Route Refresh:          0          0
    Total:              32794      32808
  Do log neighbor state changes (via global configuration)
  Default minimum time between advertisement runs is 0 seconds
 
 For address family: VPNv4 Unicast
  Translates address family IPv4 Unicast for VRF VRF11
  Session: 10.255.11.4
  BGP table version 2399, neighbor version 2399/0
  Output queue size : 0
  Index 4, Advertise bit 0
  4 update-group member
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Extended-community attribute sent to this neighbor
  Inbound path policy configured
  Outbound path policy configured
  Route map for incoming advertisements is BGP_IN
  Route map for outgoing advertisements is BGP_OUT
  Slow-peer detection is disabled
  Slow-peer split-update-group dynamic is disabled
                                 Sent       Rcvd
  Prefix activity:               ----       ----
    Prefixes Current:               0          1 (Consumes 272 bytes)
    Prefixes Total:                 0          1
    Implicit Withdraw:              0          0
    Explicit Withdraw:              0          0
    Used as bestpath:             n/a          0
    Used as multipath:            n/a          0
    Used as secondary:            n/a          0
    Saved (soft-reconfig):        n/a          1 (Consumes 136 bytes)

                                   Outbound    Inbound
  Local Policy Denied Prefixes:    --------    -------
    Other Policies:                       1        n/a
    Total:                                1          0
  Number of NLRIs in the update sent: max 0, min 0
  Last detected as dynamic slow peer: never
  Dynamic slow peer recovered: never
  Refresh Epoch: 2
  Last Sent Refresh Start-of-rib: never
  Last Sent Refresh End-of-rib: never
  Last Received Refresh Start-of-rib: 2w6d
  Last Received Refresh End-of-rib: 2w6d
  Refresh-In took 0 seconds
                                       Sent       Rcvd
        Refresh activity:              ----       ----
          Refresh Start-of-RIB          0          1
          Refresh End-of-RIB            0          1

  Address tracking is enabled, the RIB does have a route to 10.255.11.4
  Route to peer address reachability Up: 1; Down: 0
    Last notification 2w6d
  Connections established 1; dropped 0
  Last reset never
  External BGP neighbor configured for connected checks (single-hop no-disable-connected-check)
  Interface associated: Tunnel11 (peering address in same link)
  Transport(tcp) path-mtu-discovery is enabled
  Graceful-Restart is disabled
  SSO is disabled
Connection state is ESTAB, I/O status: 1, unread input bytes: 0            
Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 1
Local host: 10.255.11.204, Local port: 33514
Foreign host: 10.255.11.4, Foreign port: 179
Connection tableid (VRF): 3
Maximum output segment queue size: 50

Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

Event Timers (current time is 0x4AE0695D1):
Timer          Starts    Wakeups            Next
Retrans         32804         10             0x0
TimeWait            0          0             0x0
AckHold         32805      32223             0x0
SendWnd             0          0             0x0
KeepAlive           0          0             0x0
GiveUp              0          0             0x0
PmtuAger      1781782    1781781     0x4AE069986
DeadWait            0          0             0x0
Linger              0          0             0x0
ProcessQ            0          0             0x0
 
iss: 2115004957  snduna: 2115628086  sndnxt: 2115628086
irs: 3296319032  rcvnxt: 3296942468

sndwnd:  15700  scale:      0  maxrcvwnd:  16384
rcvwnd:  15396  scale:      0  delrcvwnd:    988

SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
minRTT: 22 ms, maxRTT: 1000 ms, ACK hold: 200 ms
uptime: 1788576610 ms, Sent idletime: 35652 ms, Receive idletime: 35428 ms 
Status Flags: active open
Option Flags: VRF id set, nagle, path mtu capable
IP Precedence value : 6

Datagrams (max data segment is 1360 bytes):
Rcvd: 65496 (out of order: 0), with data: 32806, total data bytes: 623435
Sent: 65477 (retransmit: 10, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 32794, total data bytes: 623128

 Packets received in fast path: 0, fast processed: 0, slow path: 0
 fast lock acquisition failures: 0, slow path: 0
TCP Semaphore      0x7F1747D2ACD0  FREE 
          
BGP neighbor is 10.255.11.9,  vrf VRF11,  remote AS 65519,  local AS 65534, external link
  BGP version 4, remote router ID 10.255.250.6
  BGP state = Established, up for 2w6d
  Last read 00:00:15, last write 00:00:09, hold time is 180, keepalive interval is 60 seconds
  Neighbor sessions:
    1 active, is not multisession capable (disabled)
  Neighbor capabilities:
    Route refresh: advertised and received(new)
    Four-octets ASN Capability: advertised and received
    Address family IPv4 Unicast: advertised and received
    Enhanced Refresh Capability: advertised and received
    Multisession Capability: 
    Stateful switchover support enabled: NO for session 1
  Message statistics:
    InQ depth is 0
    OutQ depth is 0
    
                         Sent       Rcvd
    Opens:                  1          1
    Notifications:          0          0
    Updates:                1          2
    Keepalives:         32813      32820
    Route Refresh:          0          0
    Total:              32815      32825
  Do log neighbor state changes (via global configuration)
  Default minimum time between advertisement runs is 0 seconds

 For address family: VPNv4 Unicast
  Translates address family IPv4 Unicast for VRF VRF11
  Session: 10.255.11.9
  BGP table version 2399, neighbor version 2399/0
  Output queue size : 0
  Index 6, Advertise bit 1
  6 update-group member
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Extended-community attribute sent to this neighbor
  Inbound path policy configured
  Outbound path policy configured
  Route map for incoming advertisements is BGP_IN
  Route map for outgoing advertisements is BGP_OUT
  Slow-peer detection is disabled
  Slow-peer split-update-group dynamic is disabled
                                 Sent       Rcvd
  Prefix activity:               ----       ----
    Prefixes Current:               0          1 (Consumes 272 bytes)
    Prefixes Total:                 0          1
    Implicit Withdraw:              0          0
    Explicit Withdraw:              0          0
    Used as bestpath:             n/a          1
    Used as multipath:            n/a          0
    Used as secondary:            n/a          0
    Saved (soft-reconfig):        n/a          1 (Consumes 136 bytes)

                                   Outbound    Inbound
  Local Policy Denied Prefixes:    --------    -------
    Other Policies:                       1        n/a
    Total:                                1          0
  Number of NLRIs in the update sent: max 0, min 0
  Last detected as dynamic slow peer: never
  Dynamic slow peer recovered: never
  Refresh Epoch: 2
  Last Sent Refresh Start-of-rib: never
  Last Sent Refresh End-of-rib: never
  Last Received Refresh Start-of-rib: 2w6d
  Last Received Refresh End-of-rib: 2w6d
  Refresh-In took 0 seconds
                                       Sent       Rcvd
        Refresh activity:              ----       ----
          Refresh Start-of-RIB          0          1
          Refresh End-of-RIB            0          1

  Address tracking is enabled, the RIB does have a route to 10.255.11.9
  Route to peer address reachability Up: 1; Down: 0
    Last notification 2w6d
  Connections established 1; dropped 0
  Last reset never
  External BGP neighbor configured for connected checks (single-hop no-disable-connected-check)
  Interface associated: Tunnel11 (peering address in same link)
  Transport(tcp) path-mtu-discovery is enabled
  Graceful-Restart is disabled
  SSO is disabled
 Connection state is ESTAB, I/O status: 1, unread input bytes: 0            
 Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 1
Local host: 10.255.11.204, Local port: 38993
Foreign host: 10.255.11.9, Foreign port: 179
 Connection tableid (VRF): 3
Maximum output segment queue size: 50

Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

Event Timers (current time is 0x4AE069763):
Timer          Starts    Wakeups            Next
Retrans         32816          1             0x0
TimeWait            0          0             0x0
AckHold         32822      32248             0x0
SendWnd             0          0             0x0
KeepAlive           0          0             0x0
GiveUp              0          0             0x0
PmtuAger      1782044    1782043     0x4AE0699B0
DeadWait            0          0             0x0
Linger              0          0             0x0
ProcessQ            0          0             0x0

iss:  957193073  snduna:  957816601  sndnxt:  957816601
irs: 1068505590  rcvnxt: 1069129349

sndwnd:  15301  scale:      0  maxrcvwnd:  16384
rcvwnd:  15073  scale:      0  delrcvwnd:   1311

SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
minRTT: 9 ms, maxRTT: 1000 ms, ACK hold: 200 ms
uptime: 1788574963 ms, Sent idletime: 9426 ms, Receive idletime: 9216 ms 
Status Flags: active open
 Option Flags: VRF id set, nagle, path mtu capable
IP Precedence value : 6
 
Datagrams (max data segment is 1360 bytes):
Rcvd: 65523 (out of order: 0), with data: 32823, total data bytes: 623758
Sent: 65522 (retransmit: 1, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 32815, total data bytes: 623527

 Packets received in fast path: 0, fast processed: 0, slow path: 0
 fast lock acquisition failures: 0, slow path: 0
TCP Semaphore      0x7F174807D408  FREE 
          
BGP neighbor is 10.255.12.4,  vrf VRF12,  remote AS 65514,  local AS 65534, external link
  BGP version 4, remote router ID 10.255.255.6
  BGP state = Established, up for 2w6d
  Last read 00:00:42, last write 00:00:19, hold time is 180, keepalive interval is 60 seconds
  Neighbor sessions:
    1 active, is not multisession capable (disabled)
  Neighbor capabilities:
    Route refresh: advertised and received(new)
    Four-octets ASN Capability: advertised and received
    Address family IPv4 Unicast: advertised and received
    Enhanced Refresh Capability: advertised and received
    Multisession Capability: 
    Stateful switchover support enabled: NO for session 1
  Message statistics:
    InQ depth is 0
    OutQ depth is 0
    
                         Sent       Rcvd
    Opens:                  1          1
    Notifications:          0          0
    Updates:              148          6
    Keepalives:         32761      32801
    Route Refresh:          0          0
    Total:              32910      32810
  Do log neighbor state changes (via global configuration)
  Default minimum time between advertisement runs is 0 seconds
 
 For address family: VPNv4 Unicast
  Translates address family IPv4 Unicast for VRF VRF12
  Session: 10.255.12.4
  BGP table version 2399, neighbor version 2399/0
  Output queue size : 0
  Index 7, Advertise bit 0
  7 update-group member
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Extended-community attribute sent to this neighbor
  Inbound path policy configured
  Outbound path policy configured
  Route map for incoming advertisements is BGP_IN
  Route map for outgoing advertisements is BGP_OUT
  Slow-peer detection is disabled
  Slow-peer split-update-group dynamic is disabled
                                 Sent       Rcvd
  Prefix activity:               ----       ----
    Prefixes Current:               9          1 (Consumes 272 bytes)
    Prefixes Total:               148          5
    Implicit Withdraw:              1          4
    Explicit Withdraw:            138          0
    Used as bestpath:             n/a          0
    Used as multipath:            n/a          0
    Used as secondary:            n/a          0
    Saved (soft-reconfig):        n/a          1 (Consumes 136 bytes)

                                   Outbound    Inbound
  Local Policy Denied Prefixes:    --------    -------
    Other Policies:                    1064        n/a
    Total:                             1064          0
  Number of NLRIs in the update sent: max 2, min 0
  Last detected as dynamic slow peer: never
  Dynamic slow peer recovered: never
  Refresh Epoch: 2
  Last Sent Refresh Start-of-rib: never
  Last Sent Refresh End-of-rib: never
  Last Received Refresh Start-of-rib: 2w6d
  Last Received Refresh End-of-rib: 2w6d
  Refresh-In took 0 seconds
                                       Sent       Rcvd
        Refresh activity:              ----       ----
          Refresh Start-of-RIB          0          1
          Refresh End-of-RIB            0          1

  Address tracking is enabled, the RIB does have a route to 10.255.12.4
  Route to peer address reachability Up: 1; Down: 0
    Last notification 2w6d
  Connections established 1; dropped 0
  Last reset never
  External BGP neighbor configured for connected checks (single-hop no-disable-connected-check)
  Interface associated: Tunnel12 (peering address in same link)
  Transport(tcp) path-mtu-discovery is enabled
  Graceful-Restart is disabled
  SSO is disabled
Connection state is ESTAB, I/O status: 1, unread input bytes: 0            
Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 1
Local host: 10.255.12.204, Local port: 41858
Foreign host: 10.255.12.4, Foreign port: 179
Connection tableid (VRF): 4
Maximum output segment queue size: 50

Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

Event Timers (current time is 0x4AE069977):
Timer          Starts    Wakeups            Next
Retrans         32864          4             0x0
TimeWait            0          0             0x0
AckHold         32806      32235             0x0
SendWnd             0          0             0x0
KeepAlive           0          0             0x0
GiveUp              0          0             0x0
PmtuAger      1782005    1782004     0x4AE069B3B
DeadWait            0          0             0x0
Linger              0          0             0x0
ProcessQ            0          0             0x0

iss:  639459013  snduna:  640094455  sndnxt:  640094455
irs: 2469711945  rcvnxt: 2470335582

sndwnd:  16308  scale:      0  maxrcvwnd:  16384
rcvwnd:  15187  scale:      0  delrcvwnd:   1197

SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
minRTT: 22 ms, maxRTT: 1000 ms, ACK hold: 200 ms
uptime: 1788571400 ms, Sent idletime: 20201 ms, Receive idletime: 19977 ms 
Status Flags: active open
Option Flags: VRF id set, nagle, path mtu capable
IP Precedence value : 6

Datagrams (max data segment is 1360 bytes):
Rcvd: 65548 (out of order: 0), with data: 32808, total data bytes: 623636
Sent: 65558 (retransmit: 4, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 32862, total data bytes: 635441

 Packets received in fast path: 0, fast processed: 0, slow path: 0
 fast lock acquisition failures: 0, slow path: 0
TCP Semaphore      0x7F174807D4D8  FREE 
          
BGP neighbor is 10.255.12.9,  vrf VRF12,  remote AS 65519,  local AS 65534, external link
  BGP version 4, remote router ID 10.255.250.6
  BGP state = Established, up for 2w6d
  Last read 00:00:18, last write 00:00:06, hold time is 180, keepalive interval is 60 seconds
  Neighbor sessions:
    1 active, is not multisession capable (disabled)
  Neighbor capabilities:
    Route refresh: advertised and received(new)
    Four-octets ASN Capability: advertised and received
    Address family IPv4 Unicast: advertised and received
    Enhanced Refresh Capability: advertised and received
    Multisession Capability: 
    Stateful switchover support enabled: NO for session 1
  Message statistics:
    InQ depth is 0
    OutQ depth is 0
    
                         Sent       Rcvd
    Opens:                  1          1
    Notifications:          0          0
    Updates:              148          6
    Keepalives:         32776      32810
    Route Refresh:          0          0
    Total:              32925      32819
  Do log neighbor state changes (via global configuration)
  Default minimum time between advertisement runs is 0 seconds

 For address family: VPNv4 Unicast
  Translates address family IPv4 Unicast for VRF VRF12
  Session: 10.255.12.9
  BGP table version 2399, neighbor version 2399/0
  Output queue size : 0
  Index 8, Advertise bit 1
  8 update-group member
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Extended-community attribute sent to this neighbor
  Inbound path policy configured
  Outbound path policy configured
  Route map for incoming advertisements is BGP_IN
  Route map for outgoing advertisements is BGP_OUT
  Slow-peer detection is disabled
  Slow-peer split-update-group dynamic is disabled
                                 Sent       Rcvd
  Prefix activity:               ----       ----
    Prefixes Current:               9          1 (Consumes 272 bytes)
    Prefixes Total:               148          4
    Implicit Withdraw:              1          2
    Explicit Withdraw:            138          1
    Used as bestpath:             n/a          1
    Used as multipath:            n/a          0
    Used as secondary:            n/a          0
    Saved (soft-reconfig):        n/a          1 (Consumes 136 bytes)

                                   Outbound    Inbound
  Local Policy Denied Prefixes:    --------    -------
    Other Policies:                    1064        n/a
    Total:                             1064          0
  Number of NLRIs in the update sent: max 2, min 0
  Last detected as dynamic slow peer: never
  Dynamic slow peer recovered: never
  Refresh Epoch: 2
  Last Sent Refresh Start-of-rib: never
  Last Sent Refresh End-of-rib: never
  Last Received Refresh Start-of-rib: 2w6d
  Last Received Refresh End-of-rib: 2w6d
  Refresh-In took 0 seconds
                                       Sent       Rcvd
        Refresh activity:              ----       ----
          Refresh Start-of-RIB          0          1
          Refresh End-of-RIB            0          1

  Address tracking is enabled, the RIB does have a route to 10.255.12.9
  Route to peer address reachability Up: 1; Down: 0
    Last notification 2w6d
  Connections established 1; dropped 0
  Last reset never
  External BGP neighbor configured for connected checks (single-hop no-disable-connected-check)
  Interface associated: Tunnel12 (peering address in same link)
  Transport(tcp) path-mtu-discovery is enabled
  Graceful-Restart is disabled
  SSO is disabled
 Connection state is ESTAB, I/O status: 1, unread input bytes: 0            
 Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 1
Local host: 10.255.12.204, Local port: 54769
Foreign host: 10.255.12.9, Foreign port: 179
 Connection tableid (VRF): 4
Maximum output segment queue size: 50

Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

Event Timers (current time is 0x4AE069C03):
Timer          Starts    Wakeups            Next
Retrans         32878          3             0x0
TimeWait            0          0             0x0
AckHold         32815      32241             0x0
SendWnd             0          0             0x0
KeepAlive           0          0             0x0
GiveUp              0          0             0x0
PmtuAger      1782055    1782054     0x4AE069E75
DeadWait            0          0             0x0
Linger              0          0             0x0
ProcessQ            0          0             0x0

iss: 1747014950  snduna: 1747650273  sndnxt: 1747650273
irs: 2226126303  rcvnxt: 2226750079

sndwnd:  15548  scale:      0  maxrcvwnd:  16384
rcvwnd:  15073  scale:      0  delrcvwnd:   1311

SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
minRTT: 9 ms, maxRTT: 1000 ms, ACK hold: 200 ms
uptime: 1788571028 ms, Sent idletime: 6514 ms, Receive idletime: 6304 ms 
Status Flags: active open
 Option Flags: VRF id set, nagle, path mtu capable
IP Precedence value : 6
 
Datagrams (max data segment is 1360 bytes):
Rcvd: 65566 (out of order: 0), with data: 32817, total data bytes: 623775
Sent: 65578 (retransmit: 3, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 32877, total data bytes: 635322

 Packets received in fast path: 0, fast processed: 0, slow path: 0
 fast lock acquisition failures: 0, slow path: 0
TCP Semaphore      0x7F174807D5A8  FREE 
          
BGP neighbor is 10.255.13.4,  vrf VRF13,  remote AS 65514,  local AS 65534, external link
  BGP version 4, remote router ID 10.255.255.6
  BGP state = Established, up for 2w6d
  Last read 00:00:09, last write 00:00:00, hold time is 180, keepalive interval is 60 seconds
  Neighbor sessions:
    1 active, is not multisession capable (disabled)
  Neighbor capabilities:
    Route refresh: advertised and received(new)
    Four-octets ASN Capability: advertised and received
    Address family IPv4 Unicast: advertised and received
    Enhanced Refresh Capability: advertised and received
    Multisession Capability: 
    Stateful switchover support enabled: NO for session 1
  Message statistics:
    InQ depth is 0
    OutQ depth is 0
    
                         Sent       Rcvd
    Opens:                  1          1
    Notifications:          0          0
    Updates:                1          7
    Keepalives:         32782      32806
    Route Refresh:          0          0
    Total:              32784      32816
  Do log neighbor state changes (via global configuration)
  Default minimum time between advertisement runs is 0 seconds
 
 For address family: VPNv4 Unicast
  Translates address family IPv4 Unicast for VRF VRF13
  Session: 10.255.13.4
  BGP table version 2399, neighbor version 2399/0
  Output queue size : 0
  Index 2, Advertise bit 0
  2 update-group member
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Extended-community attribute sent to this neighbor
  Inbound path policy configured
  Outbound path policy configured
  Route map for incoming advertisements is BGP_IN
  Route map for outgoing advertisements is BGP_OUT
  Slow-peer detection is disabled
  Slow-peer split-update-group dynamic is disabled
                                 Sent       Rcvd
  Prefix activity:               ----       ----
    Prefixes Current:               0          1 (Consumes 272 bytes)
    Prefixes Total:                 0          6
    Implicit Withdraw:              0          5
    Explicit Withdraw:              0          0
    Used as bestpath:             n/a          0
    Used as multipath:            n/a          0
    Used as secondary:            n/a          0
    Saved (soft-reconfig):        n/a          1 (Consumes 136 bytes)

                                   Outbound    Inbound
  Local Policy Denied Prefixes:    --------    -------
    Other Policies:                       6        n/a
    Total:                                6          0
  Number of NLRIs in the update sent: max 0, min 0
  Last detected as dynamic slow peer: never
  Dynamic slow peer recovered: never
  Refresh Epoch: 2
  Last Sent Refresh Start-of-rib: never
  Last Sent Refresh End-of-rib: never
  Last Received Refresh Start-of-rib: 2w6d
  Last Received Refresh End-of-rib: 2w6d
  Refresh-In took 0 seconds
                                       Sent       Rcvd
        Refresh activity:              ----       ----
          Refresh Start-of-RIB          0          1
          Refresh End-of-RIB            0          1

  Address tracking is enabled, the RIB does have a route to 10.255.13.4
  Route to peer address reachability Up: 1; Down: 0
    Last notification 2w6d
  Connections established 1; dropped 0
  Last reset never
  External BGP neighbor configured for connected checks (single-hop no-disable-connected-check)
  Interface associated: Tunnel13 (peering address in same link)
  Transport(tcp) path-mtu-discovery is enabled
  Graceful-Restart is disabled
  SSO is disabled
Connection state is ESTAB, I/O status: 1, unread input bytes: 0            
Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 1
Local host: 10.255.13.204, Local port: 39746
Foreign host: 10.255.13.4, Foreign port: 179
Connection tableid (VRF): 5
Maximum output segment queue size: 50

Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

Event Timers (current time is 0x4AE069E1B):
Timer          Starts    Wakeups            Next
Retrans         32792          8             0x0
TimeWait            0          0             0x0
AckHold         32812      32253             0x0
SendWnd             0          0             0x0
KeepAlive           0          0             0x0
GiveUp              0          0             0x0
PmtuAger      1781845    1781844     0x4AE06A0CA
DeadWait            0          0             0x0
Linger              0          0             0x0
ProcessQ            0          0             0x0

iss:  452660100  snduna:  453283039  sndnxt:  453283039
irs: 3919747522  rcvnxt: 3920371334

sndwnd:  15890  scale:      0  maxrcvwnd:  16384
rcvwnd:  16384  scale:      0  delrcvwnd:      0

SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
minRTT: 22 ms, maxRTT: 1000 ms, ACK hold: 200 ms
uptime: 1788579756 ms, Sent idletime: 906 ms, Receive idletime: 683 ms 
Status Flags: active open
Option Flags: VRF id set, nagle, path mtu capable
IP Precedence value : 6

Datagrams (max data segment is 1360 bytes):
Rcvd: 65473 (out of order: 0), with data: 32814, total data bytes: 623811
Sent: 65499 (retransmit: 8, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 32784, total data bytes: 622938

 Packets received in fast path: 0, fast processed: 0, slow path: 0
 fast lock acquisition failures: 0, slow path: 0
TCP Semaphore      0x7F1744DF0BD0  FREE 
          
BGP neighbor is 10.255.13.9,  vrf VRF13,  remote AS 65519,  local AS 65534, external link
  BGP version 4, remote router ID 10.255.250.6
  BGP state = Established, up for 2w6d
  Last read 00:00:03, last write 00:00:04, hold time is 180, keepalive interval is 60 seconds
  Neighbor sessions:
    1 active, is not multisession capable (disabled)
  Neighbor capabilities:
    Route refresh: advertised and received(new)
    Four-octets ASN Capability: advertised and received
    Address family IPv4 Unicast: advertised and received
    Enhanced Refresh Capability: advertised and received
    Multisession Capability: 
    Stateful switchover support enabled: NO for session 1
  Message statistics:
    InQ depth is 0
    OutQ depth is 0
    
                         Sent       Rcvd
    Opens:                  1          1
    Notifications:          0          0
    Updates:                1          7
    Keepalives:         32803      32833
    Route Refresh:          0          0
    Total:              32805      32843
  Do log neighbor state changes (via global configuration)
  Default minimum time between advertisement runs is 0 seconds

 For address family: VPNv4 Unicast
  Translates address family IPv4 Unicast for VRF VRF13
  Session: 10.255.13.9
  BGP table version 2399, neighbor version 2399/0
  Output queue size : 0
  Index 3, Advertise bit 1
  3 update-group member
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Extended-community attribute sent to this neighbor
  Inbound path policy configured
  Outbound path policy configured
  Route map for incoming advertisements is BGP_IN
  Route map for outgoing advertisements is BGP_OUT
  Slow-peer detection is disabled
  Slow-peer split-update-group dynamic is disabled
                                 Sent       Rcvd
  Prefix activity:               ----       ----
    Prefixes Current:               0          1 (Consumes 272 bytes)
    Prefixes Total:                 0          6
    Implicit Withdraw:              0          5
    Explicit Withdraw:              0          0
    Used as bestpath:             n/a          1
    Used as multipath:            n/a          0
    Used as secondary:            n/a          0
    Saved (soft-reconfig):        n/a          1 (Consumes 136 bytes)

                                   Outbound    Inbound
  Local Policy Denied Prefixes:    --------    -------
    Other Policies:                       6        n/a
    Total:                                6          0
  Number of NLRIs in the update sent: max 0, min 0
  Last detected as dynamic slow peer: never
  Dynamic slow peer recovered: never
  Refresh Epoch: 2
  Last Sent Refresh Start-of-rib: never
  Last Sent Refresh End-of-rib: never
  Last Received Refresh Start-of-rib: 2w6d
  Last Received Refresh End-of-rib: 2w6d
  Refresh-In took 0 seconds
                                       Sent       Rcvd
        Refresh activity:              ----       ----
          Refresh Start-of-RIB          0          1
          Refresh End-of-RIB            0          1

  Address tracking is enabled, the RIB does have a route to 10.255.13.9
  Route to peer address reachability Up: 1; Down: 0
    Last notification 2w6d
  Connections established 1; dropped 0
  Last reset never
  External BGP neighbor configured for connected checks (single-hop no-disable-connected-check)
  Interface associated: Tunnel13 (peering address in same link)
  Transport(tcp) path-mtu-discovery is enabled
  Graceful-Restart is disabled
  SSO is disabled
 Connection state is ESTAB, I/O status: 1, unread input bytes: 0            
 Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 1
Local host: 10.255.13.204, Local port: 12197
Foreign host: 10.255.13.9, Foreign port: 179
 Connection tableid (VRF): 5
Maximum output segment queue size: 50

Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

Event Timers (current time is 0x4AE069FB4):
Timer          Starts    Wakeups            Next
Retrans         32806          1             0x0
TimeWait            0          0             0x0
AckHold         32839      32252             0x0
SendWnd             0          0             0x0
KeepAlive           0          0             0x0
GiveUp              0          0             0x0
PmtuAger      1782035    1782034     0x4AE06A25E
DeadWait            0          0             0x0
Linger              0          0             0x0
ProcessQ            0          0             0x0

iss: 4215501672  snduna: 4216125010  sndnxt: 4216125010
irs:  341672035  rcvnxt:  342296360

sndwnd:  15491  scale:      0  maxrcvwnd:  16384
rcvwnd:  15852  scale:      0  delrcvwnd:    532

SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
minRTT: 9 ms, maxRTT: 1000 ms, ACK hold: 200 ms
uptime: 1788579142 ms, Sent idletime: 3724 ms, Receive idletime: 3924 ms 
Status Flags: active open
 Option Flags: VRF id set, nagle, path mtu capable
IP Precedence value : 6
 
Datagrams (max data segment is 1360 bytes):
Rcvd: 65550 (out of order: 0), with data: 32841, total data bytes: 624324
Sent: 65518 (retransmit: 1, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 32805, total data bytes: 623337

 Packets received in fast path: 0, fast processed: 0, slow path: 0
 fast lock acquisition failures: 0, slow path: 0
TCP Semaphore      0x7F173C61CF30  FREE 
          
BGP neighbor is 172.16.0.4,  vrf VRF10,  remote AS 65514,  local AS 65534, external link
  BGP version 4, remote router ID 10.255.255.6
  BGP state = Established, up for 2w6d
  Last read 00:00:15, last write 00:00:20, hold time is 180, keepalive interval is 60 seconds
  Neighbor sessions:
    1 active, is not multisession capable (disabled)
  Neighbor capabilities:
    Route refresh: advertised and received(new)
    Four-octets ASN Capability: advertised and received
    Address family IPv4 Unicast: advertised and received
    Enhanced Refresh Capability: advertised and received
    Multisession Capability: 
    Stateful switchover support enabled: NO for session 1
  Message statistics:
    InQ depth is 0
    OutQ depth is 0
    
                         Sent       Rcvd
    Opens:                  1          1
    Notifications:          0          0
    Updates:                1          2
    Keepalives:         32810      32795
    Route Refresh:          0          0
    Total:              32812      32800
  Do log neighbor state changes (via global configuration)
  Default minimum time between advertisement runs is 0 seconds
 
 For address family: VPNv4 Unicast
  Translates address family IPv4 Unicast for VRF VRF10
  Session: 172.16.0.4
  BGP table version 2399, neighbor version 2399/0
  Output queue size : 0
  Index 5, Advertise bit 1
  5 update-group member
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Extended-community attribute sent to this neighbor
  Inbound path policy configured
  Outbound path policy configured
  Route map for incoming advertisements is BGP_IN
  Route map for outgoing advertisements is BGP_OUT
  Slow-peer detection is disabled
  Slow-peer split-update-group dynamic is disabled
                                 Sent       Rcvd
  Prefix activity:               ----       ----
    Prefixes Current:               0          1 (Consumes 272 bytes)
    Prefixes Total:                 0          1
    Implicit Withdraw:              0          0
    Explicit Withdraw:              0          0
    Used as bestpath:             n/a          0
    Used as multipath:            n/a          0
    Used as secondary:            n/a          0
    Saved (soft-reconfig):        n/a          1 (Consumes 136 bytes)

                                   Outbound    Inbound
  Local Policy Denied Prefixes:    --------    -------
    Other Policies:                       1        n/a
    Total:                                1          0
  Number of NLRIs in the update sent: max 0, min 0
  Last detected as dynamic slow peer: never
  Dynamic slow peer recovered: never
  Refresh Epoch: 2
  Last Sent Refresh Start-of-rib: never
  Last Sent Refresh End-of-rib: never
  Last Received Refresh Start-of-rib: 2w6d
  Last Received Refresh End-of-rib: 2w6d
  Refresh-In took 0 seconds
                                       Sent       Rcvd
        Refresh activity:              ----       ----
          Refresh Start-of-RIB          0          1
          Refresh End-of-RIB            0          1

  Address tracking is enabled, the RIB does have a route to 172.16.0.4
  Route to peer address reachability Up: 1; Down: 0
    Last notification 2w6d
  Connections established 1; dropped 0
  Last reset never
  External BGP neighbor configured for connected checks (single-hop no-disable-connected-check)
  Interface associated: Tunnel10 (peering address in same link)
  Transport(tcp) path-mtu-discovery is enabled
  Graceful-Restart is disabled
  SSO is disabled
Connection state is ESTAB, I/O status: 1, unread input bytes: 0            
Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 1
Local host: 172.16.0.141, Local port: 32322
Foreign host: 172.16.0.4, Foreign port: 179
Connection tableid (VRF): 2
Maximum output segment queue size: 50

Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

Event Timers (current time is 0x4AE06A2FC):
Timer          Starts    Wakeups            Next
Retrans         32817          5             0x0
TimeWait            0          0             0x0
AckHold         32797      32259             0x0
SendWnd             0          0             0x0
KeepAlive           0          0             0x0
GiveUp              0          0             0x0
PmtuAger      1781931    1781930     0x4AE06A4B5
DeadWait            0          0             0x0
Linger              0          0             0x0
ProcessQ            0          0             0x0

iss:  922591666  snduna:  923215137  sndnxt:  923215137
irs: 3979427565  rcvnxt: 3980050845

sndwnd:  15358  scale:      0  maxrcvwnd:  16384
rcvwnd:  15548  scale:      0  delrcvwnd:    836

SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
minRTT: 22 ms, maxRTT: 1000 ms, ACK hold: 200 ms
uptime: 1788578957 ms, Sent idletime: 16417 ms, Receive idletime: 16617 ms 
Status Flags: active open
Option Flags: VRF id set, nagle, path mtu capable
IP Precedence value : 6

Datagrams (max data segment is 1360 bytes):
Rcvd: 65522 (out of order: 0), with data: 32798, total data bytes: 623279
Sent: 65531 (retransmit: 5, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 32812, total data bytes: 623470

 Packets received in fast path: 0, fast processed: 0, slow path: 0
 fast lock acquisition failures: 0, slow path: 0
TCP Semaphore      0x7F174807D678  FREE 
          
BGP neighbor is 172.16.0.9,  vrf VRF10,  remote AS 65519,  local AS 65534, external link
  BGP version 4, remote router ID 10.255.250.6
  BGP state = Established, up for 2w6d
  Last read 00:00:14, last write 00:00:50, hold time is 180, keepalive interval is 60 seconds
  Neighbor sessions:
    1 active, is not multisession capable (disabled)
  Neighbor capabilities:
    Route refresh: advertised and received(new)
    Four-octets ASN Capability: advertised and received
    Address family IPv4 Unicast: advertised and received
    Enhanced Refresh Capability: advertised and received
    Multisession Capability: 
    Stateful switchover support enabled: NO for session 1
  Message statistics:
    InQ depth is 0
    OutQ depth is 0
    
                         Sent       Rcvd
    Opens:                  1          1
    Notifications:          0          0
    Updates:                1          2
    Keepalives:         32806      32808
    Route Refresh:          0          0
    Total:              32808      32813
  Do log neighbor state changes (via global configuration)
  Default minimum time between advertisement runs is 0 seconds

 For address family: VPNv4 Unicast
  Translates address family IPv4 Unicast for VRF VRF10
  Session: 172.16.0.9
  BGP table version 2399, neighbor version 2399/0
  Output queue size : 0
  Index 1, Advertise bit 0
  1 update-group member
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Extended-community attribute sent to this neighbor
  Inbound path policy configured
  Outbound path policy configured
  Route map for incoming advertisements is BGP_IN
  Route map for outgoing advertisements is BGP_OUT
  Slow-peer detection is disabled
  Slow-peer split-update-group dynamic is disabled
                                 Sent       Rcvd
  Prefix activity:               ----       ----
    Prefixes Current:               0          1 (Consumes 272 bytes)
    Prefixes Total:                 0          1
    Implicit Withdraw:              0          0
    Explicit Withdraw:              0          0
    Used as bestpath:             n/a          1
    Used as multipath:            n/a          0
    Used as secondary:            n/a          0
    Saved (soft-reconfig):        n/a          1 (Consumes 136 bytes)

                                   Outbound    Inbound
  Local Policy Denied Prefixes:    --------    -------
    Other Policies:                       1        n/a
    Total:                                1          0
  Number of NLRIs in the update sent: max 0, min 0
  Last detected as dynamic slow peer: never
  Dynamic slow peer recovered: never
  Refresh Epoch: 2
  Last Sent Refresh Start-of-rib: never
  Last Sent Refresh End-of-rib: never
  Last Received Refresh Start-of-rib: 2w6d
  Last Received Refresh End-of-rib: 2w6d
  Refresh-In took 0 seconds
                                       Sent       Rcvd
        Refresh activity:              ----       ----
          Refresh Start-of-RIB          0          1
          Refresh End-of-RIB            0          1

  Address tracking is enabled, the RIB does have a route to 172.16.0.9
  Route to peer address reachability Up: 1; Down: 0
    Last notification 2w6d
  Connections established 1; dropped 0
  Last reset never
  External BGP neighbor configured for connected checks (single-hop no-disable-connected-check)
  Interface associated: Tunnel10 (peering address in same link)
  Transport(tcp) path-mtu-discovery is enabled
  Graceful-Restart is disabled
  SSO is disabled
 Connection state is ESTAB, I/O status: 1, unread input bytes: 0            
 Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 1
Local host: 172.16.0.141, Local port: 49926
Foreign host: 172.16.0.9, Foreign port: 179
 Connection tableid (VRF): 2
Maximum output segment queue size: 50

Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

Event Timers (current time is 0x4AE06A51B):
Timer          Starts    Wakeups            Next
Retrans         32809          1             0x0
TimeWait            0          0             0x0
AckHold         32810      32252             0x0
SendWnd             0          0             0x0
KeepAlive           0          0             0x0
GiveUp              0          0             0x0
PmtuAger      1782044    1782043     0x4AE06A571
DeadWait            0          0             0x0
Linger              0          0             0x0
ProcessQ            0          0             0x0

iss: 3051876655  snduna: 3052500050  sndnxt: 3052500050
irs: 2636422233  rcvnxt: 2637045760

sndwnd:  15434  scale:      0  maxrcvwnd:  16384
rcvwnd:  15301  scale:      0  delrcvwnd:   1083

SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
minRTT: 9 ms, maxRTT: 1000 ms, ACK hold: 200 ms
uptime: 1788585645 ms, Sent idletime: 14322 ms, Receive idletime: 14522 ms 
Status Flags: active open
 Option Flags: VRF id set, nagle, path mtu capable
IP Precedence value : 6
 
Datagrams (max data segment is 1360 bytes):
Rcvd: 65496 (out of order: 0), with data: 32811, total data bytes: 623526
Sent: 65520 (retransmit: 1, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 32808, total data bytes: 623394

 Packets received in fast path: 0, fast processed: 0, slow path: 0
 fast lock acquisition failures: 0, slow path: 0
TCP Semaphore      0x7F1747D2ADA0  FREE
```

**Help:** execute the command "show ip bgp vpnv4 all neighbors"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show mac-address-table

**Output:**
```
Legend: * - primary entry
        age - seconds since last seen
        n/a - not available

  vlan   mac address     type    learn     age              ports
------+----------------+--------+-----+----------+--------------------------
   666  30a3.30a3.a1c3   dynamic  Yes       1200   Te1/30
   666  30a3.30a3.5ab8   dynamic  Yes          0   Po3
    60  30a3.30a3.4d54   dynamic  Yes       3600   Te1/21
*  777  0000.30a3.0167    static  No           -   Router
   664  30a3.30a3.58b5   dynamic  Yes        180   Po6
   667  30a3.30a3.daf5   dynamic  Yes          0   Te3/20
   668  30a3.30a3.e401   dynamic  Yes        600   Po6
   669  30a3.30a3.5a22   dynamic  Yes        300   Te3/20
  2000  30a3.30a3.5a22   dynamic  Yes        300   Te3/20

```

**Help:** execute the command "show mac-address-table"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip vrf interfaces

**Output:**
```
Interface              IP-Address      VRF                              Protocol
Vl1100                 192.168.100.1   BYOD-Guest                       up      
Vl1200                 192.168.200.1   BYOD-Guest                       up      
Vl1832                 10.255.0.10     BYOD-Guest                       up      
Gi0/0                  unassigned      Mgmt-vrf                         down    
Vl520                  172.31.2.253    SP-INET                          up      
Vl1836                 10.255.0.18     SP-INET                          up
```

**Help:** execute the command "show ip vrf interfaces"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip nat translations

**Output:**
```
Pro Inside global      Inside local       Outside local      Outside global
tcp 10.9.0.0:51776     10.1.0.2:51776     10.2.0.2:21        10.2.0.2:21
 tcp 10.9.0.0:51778     10.1.0.2:51778     10.2.0.2:21        10.2.0.2:21
tcp 10.9.0.0:56384     10.1.0.2:56384     10.2.0.2:22        10.2.0.2:22
icmp 10.9.0.0:513     10.1.0.2:512     10.2.0.2:512        10.2.0.2:513
tcp 100.95.3.180:8080     192.168.1.12:80       ---                   ---

--- 10.9.0.0     10.1.0.2     ---        ---
```

**Help:** execute the command "show ip nat translations"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show standby

**Output:**
```
Vlan111 - Group 1
  State is Standby
    1 state change, last state change 26w2d
  Virtual IP address is 192.168.77.62
  Active virtual MAC address is 0000.0c07.ac01
    Local virtual MAC address is 0000.0c07.ac01 (v1 default)
  Hello time 3 sec, hold time 10 sec
    Next hello sent in 0.704 secs
  Preemption enabled, delay min 180 secs
  Active router is 192.168.77.60, priority 255 (expires in 10.416 sec)
  Standby router is local
  Priority 255 (configured 255)
    Track object 1 state Up decrement 60
  Group name is "hsrp-Vl111-1" (default)
BDI10 - Group 1
  State is Active
    14 state changes, last state change 17w6d
    Track object 1 state Up
  Virtual IP address is 203.57.147.1
  Active virtual MAC address is 0000.0c07.ac01 (MAC In Use)
    Local virtual MAC address is 0000.0c07.ac01 (v1 default)
  Hello time 3 sec, hold time 10 sec
    Next hello sent in 1.040 secs
  Preemption enabled, delay min 180 secs
  Active router is local
  Standby router is 203.57.147.3, priority 230 (expires in 10.240 sec)
  Priority 240 (configured 240)
  Group name is "hsrp-BD10-1" (default)
  FLAGS: 1/1
Vlan703 - Group 4
  State is Active
    11 state changes, last state change 5d14h
  Virtual IP address is 172.23.40.9
  Active virtual MAC address is 0000.0c07.ac04
    Local virtual MAC address is 0000.0c07.ac04 (v1 default)
  Hello time 3 sec, hold time 10 sec
    Next hello sent in 0.340 secs
  Preemption enabled, delay min 180 secs
  Active router is local
  Standby router is unknown
  Priority 200 (configured 200)
    Track interface Dialer0 state Up decrement 10
  IP redundancy name is "hsrp-Vl703-4" (default)
GigabitEthernet0/1.2951 - Group 1 (version 2)
  State is Active
    2 state changes, last state change 3y37w
  Virtual IP address is 111.222.230.17
  Active virtual MAC address is 0000.0c9f.f001
    Local virtual MAC address is 0000.0c9f.f001 (v2 default)
  Hello time 3 sec, hold time 10 sec
    Next hello sent in 2.720 secs
  Preemption enabled, delay min 180 secs, reload 300 secs
  Active router is local
  Standby router is unknown
  Priority 255 (configured 255)
    Track object 1 (unknown)
  Group name is "hsrp-Gi0/1.2951-1" (default)
```

**Help:** execute the command "show standby"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip interface

**Output:**
```
GigabitEthernet0/0/0 is up, line protocol is up
  Internet address is 10.1.1.1/30
  Broadcast address is 255.255.255.255
  Address determined by non-volatile memory
  MTU is 1500 bytes
  Helper address is not set
  Directed broadcast forwarding is disabled
  Outgoing Common access list is not set
  Outgoing access list is not set
  Inbound Common access list is not set
  Inbound  access list is not set
  Proxy ARP is enabled
  Local Proxy ARP is disabled
  Security level is default
  Split horizon is enabled
  ICMP redirects are always sent
  ICMP unreachables are always sent
  ICMP mask replies are never sent
  IP fast switching is enabled
  IP Flow switching is disabled
  IP CEF switching is enabled
  IP CEF switching turbo vector
  IP Null turbo vector
  Associated unicast routing topologies:
        Topology "base", operation state is UP
  IP multicast fast switching is enabled
  IP multicast distributed fast switching is disabled
  IP route-cache flags are Fast, CEF
  Router Discovery is disabled
  IP output packet accounting is disabled
  IP access violation accounting is disabled
  TCP/IP header compression is disabled
  RTP/IP header compression is disabled
  Probe proxy name replies are disabled
  Policy routing is disabled
  Network address translation is disabled
  BGP Policy Mapping is disabled
  Input features: Virtual Fragment Reassembly, IPSec input classification, MCI Check
  Output features: IPSec output classification, IPSec: to crypto engine, Post-encryption output features
  IPv4 WCCP Redirect outbound is disabled
  IPv4 WCCP Redirect inbound is disabled
  IPv4 WCCP Redirect exclude is disabled
  IP Clear Dont Fragment is disabled
GigabitEthernet0/0/1 is up, line protocol is up
  Internet protocol processing disabled
GigabitEthernet0/0/1.10 is up, line protocol is up
  Internet address is 172.2.2.2/25
  Broadcast address is 255.255.255.255
  Address determined by non-volatile memory
  MTU is 1500 bytes
  Helper address is not set
  Directed broadcast forwarding is disabled
  Multicast reserved groups joined: 224.0.0.2 224.0.0.5
  Outgoing Common access list is not set
  Outgoing access list is not set
  Inbound Common access list is not set
  Inbound  access list is not set
  Proxy ARP is disabled
  Local Proxy ARP is disabled
  Security level is default
  Split horizon is enabled
  ICMP redirects are never sent
  ICMP unreachables are never sent
  ICMP mask replies are never sent
  IP fast switching is enabled
  IP Flow switching is disabled
  IP CEF switching is enabled
  IP CEF switching turbo vector
  IP Null turbo vector
  Associated unicast routing topologies:
        Topology "base", operation state is UP
  IP multicast fast switching is enabled
  IP multicast distributed fast switching is disabled
  IP route-cache flags are Fast, CEF
  Router Discovery is disabled
  IP output packet accounting is disabled
  IP access violation accounting is disabled
  TCP/IP header compression is disabled
  RTP/IP header compression is disabled
  Probe proxy name replies are disabled
  Policy routing is disabled
  Network address translation is disabled
  BGP Policy Mapping is disabled
  Input features: MCI Check
  IPv4 WCCP Redirect outbound is disabled
  IPv4 WCCP Redirect inbound is disabled
  IPv4 WCCP Redirect exclude is disabled
  IP Clear Dont Fragment is enabled
Tunnel102 is up, line protocol is up
  Internet address is 10.1.0.214/30
  Broadcast address is 255.255.255.255
  Address determined by non-volatile memory
  MTU is 1400 bytes
  Helper address is not set
  Directed broadcast forwarding is disabled
  Multicast reserved groups joined: 224.0.0.5
  Outgoing Common access list is not set
  Outgoing access list is not set
  Inbound Common access list is not set
  Inbound  access list is not set
  Proxy ARP is enabled
  Local Proxy ARP is disabled
  Security level is default
  Split horizon is enabled
  ICMP redirects are always sent
  ICMP unreachables are always sent
  ICMP mask replies are never sent
  IP fast switching is enabled
  IP Flow switching is disabled
  IP CEF switching is enabled
  IP CEF switching turbo vector
  IP Null turbo vector
  Associated unicast routing topologies:
        Topology "base", operation state is UP
  IP multicast fast switching is enabled
  IP multicast distributed fast switching is disabled
  IP route-cache flags are Fast, CEF
  Router Discovery is disabled
  IP output packet accounting is disabled
  IP access violation accounting is disabled
  TCP/IP header compression is disabled
  RTP/IP header compression is disabled
  Probe proxy name replies are disabled
  Policy routing is disabled
  Network address translation is disabled
  BGP Policy Mapping is disabled
  Input features: MCI Check, TCP Adjust MSS
  Output features: TCP Adjust MSS
  IPv4 WCCP Redirect outbound is disabled
  IPv4 WCCP Redirect inbound is disabled
  IPv4 WCCP Redirect exclude is disabled
  IP Clear Dont Fragment is disabled


```

**Help:** execute the command "show ip interface"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show spanning-tree

**Output:**
```

VLAN0001
  Spanning tree enabled protocol ieee
  Root ID    Priority    32769
             Address     fa16.3e57.336f
             Cost        8
             Port        4 (GigabitEthernet0/3)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     fa16.3e77.b50c
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Gi0/2               Desg FWD 4         128.3    Shr
Gi0/3               Root FWD 4         128.4    Shr
Gi1/0               Altn BLK 4         128.5    Shr



VLAN0002
  Spanning tree enabled protocol ieee
  Root ID    Priority    32770
             Address     fa16.3e57.336f
             Cost        8
             Port        4 (GigabitEthernet0/3)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32770  (priority 32768 sys-id-ext 2)
             Address     fa16.3e77.b50c
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Gi0/3               Root FWD 4         128.4    Shr
Gi1/0               Altn BLK 4         128.5    Shr



VLAN0003
  Spanning tree enabled protocol ieee
  Root ID    Priority    32771
             Address     fa16.3e57.336f
             Cost        8
             Port        4 (GigabitEthernet0/3)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32771  (priority 32768 sys-id-ext 3)
             Address     fa16.3e77.b50c
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Gi0/3               Root FWD 4         128.4    Shr
Gi1/0               Altn BLK 4         128.5    Shr

```

**Help:** execute the command "show spanning-tree"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ipv6 route

**Output:**
```
IPv6 Routing Table - default - 6 entries
Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
       B - BGP, HA - Home Agent, MR - Mobile Router, R - RIP
       H - NHRP, D - EIGRP, EX - EIGRP external, ND - ND Default
       NDp - ND Prefix, DCE - Destination, NDr - Redirect, O - OSPF Intra
       OI - OSPF Inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2, ON1 - OSPF NSSA ext 1
       ON2 - OSPF NSSA ext 2, l - LISP
C   2A05:C100:2A::/64 [0/0]
     via Vlan1, directly connected
B   2001:DB8:4::2/48 [20/0]
     via FE80::A8BB:CCFF:FE02:8B00, Serial6/0
     via A8BB::FE80:CCFF:FE02:8B00, Serial4/0
L   FF00::/8 [0/0]
     via Null0, receive
S   5555:4444::4/128 [1/0]
     via 2A05:C100:2A::56
     via 2A05:C100:2A::5765
     via 2A05:C100:2A::3:344, Vlan1
     via Vlan1, directly connected

```

**Help:** execute the command "show ipv6 route"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show interfaces description

**Output:**
```
Interface                      Status         Protocol Description
Vl1                            admin down     down
Vl99                           up             up       10.20.99.0_Switch_mgmt_VLAN
Gi0/1                          down           down     D3 USER
Gi0/2                          down           down     D3 USER
Gi0/3                          down           down     D3 USER
Gi0/4                          down           down     D3 USER
Gi0/5                          down           down     D3 USER
Gi0/6                          down           down     D3 USER
Gi0/7                          down           down     D3 USER
Gi0/8                          up             up       MERAKI TEST AP
Gi0/9                          admin down     down
Gi0/10                         up             up       UPLINK TO TULCCD3S01P
Gi0/10.10                      deleted        down
Gi0/10.20                      up             up       Carrier VLAN
Gi0/10.30                      reset          down     Garbage

```

**Help:** execute the command "show interfaces description"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip http server status

**Output:**
```
HTTP server status: Enabled
HTTP server port: 80
HTTP server active supplementary listener ports: 21111  
HTTP server authentication method: local
 HTTP server auth-retry 0 time-window 0
HTTP server digest algorithm: md5
 HTTP server access class: 0
HTTP server IPv4 access class: None
HTTP server IPv6 access class: None
HTTP server base path: 
HTTP File Upload status: Disabled
 HTTP server upload path: 
HTTP server help root: 
Maximum number of concurrent server connections allowed: 300
Maximum number of secondary server connections allowed: 50
Server idle time-out: 180 seconds
Server life time-out: 180 seconds
 Server session idle time-out: 600 seconds
Maximum number of requests allowed on a connection: 25
Server linger time : 60 seconds
HTTP server active session modules: ALL
HTTP secure server capability: Present
HTTP secure server status: Enabled
HTTP secure server port: 443
HTTP secure server ciphersuite:  rsa-aes-cbc-sha2 rsa-aes-gcm-sha2
        dhe-aes-cbc-sha2 dhe-aes-gcm-sha2 ecdhe-rsa-aes-cbc-sha2
        ecdhe-rsa-aes-gcm-sha2 ecdhe-ecdsa-aes-gcm-sha2
HTTP secure server TLS version:  TLSv1.2 TLSv1.1
HTTP secure server client authentication: Disabled
 HTTP secure server PIV authentication: Disabled
HTTP secure server PIV authorization only: Disabled
HTTP secure server trustpoint: TP-self-signed-4212509801
HTTP secure server peer validation trustpoint: 
HTTP secure server ECDHE curve: secp256r1
HTTP secure server active session modules: ALL

```

**Help:** execute the command "show ip http server status"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip route summary

**Output:**
```
Route Source    Networks    Subnets     Replicates  Overhead    Memory (bytes)
connected       0           6           0           408         1080
static          0           0           0           0           0
application     0           0           0           0           0
eigrp 100       0           0           0           0           0
bgp 65001       0           0           0           0           0
  External: 0 Internal: 0 Local: 0
isis test1      0           0           0           0           0
  Level 1: 0 Level 2: 0 Inter-area: 0
ospf 188        0           0           0           0           0
  Intra-area: 0 Inter-area: 0 External-1: 0 External-2: 0
  NSSA External-1: 0 NSSA External-2: 0
internal        2                                               920
Total           2           6           0           408         2000

```

**Help:** execute the command "show ip route summary"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show interface transceiver

**Output:**
```
If device is externally calibrated, only calibrated values are printed.
 ++ : high alarm, +  : high warning, -  : low warning, -- : low alarm.
NA or N/A: not applicable, Tx: transmit, Rx: receive.
mA: milliamperes, dBm: decibels (milliwatts).

                                 Optical   Optical
           Temperature  Voltage  Tx Power  Rx Power
Port       (Celsius)    (Volts)  (dBm)     (dBm)
---------  -----------  -------  --------  --------
Te1/49       23.1       3.29      -2.2      -3.0   
Te1/50       23.4       3.31      -2.2      -2.6   
Te1/51       21.5       3.29      -2.2      -2.1   
Te1/52       23.5       3.29      -2.4      -2.8  

```

**Help:** execute the command "show interface transceiver"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip bgp neighbors

**Output:**
```
BGP neighbor is 175.135.172.146,  vrf DEV, remote AS 65180, internal link
 Description: nsxe-core-rtr1
 Member of peer-group HMCO-core for session parameters
  BGP version 4, remote router ID 9.229.30.214
  BGP state = Established, up for 38w4d
  Last read 00:00:01, last write 00:00:01, hold time is 15, keepalive interval is 5 seconds
  Configured hold time is 15, keepalive interval is 5 seconds
  Minimum holdtime from neighbor is 0 seconds
  Neighbor sessions:
    1 active, is not multisession capable (disabled)
  Neighbor capabilities:
    Route refresh: advertised and received(new)
    Four-octets ASN Capability: advertised and received
    Address family IPv4 Unicast: advertised and received
    Enhanced Refresh Capability: advertised and received
    Multisession Capability: 
    Stateful switchover support enabled: NO for session 1
  Message statistics:
    InQ depth is 0
    OutQ depth is 0
    
                         Sent       Rcvd
    Opens:                  1          1
    Notifications:          0          0
    Updates:            22459      18491
    Keepalives:       4552728    4553516
    Route Refresh:          0          0
    Total:            4575188    4572008
  Default minimum time between advertisement runs is 0 seconds

 For address family: IPv4 Unicast
  Session: 58.146.178.38
  BGP table version 55515, neighbor version 55515/0
  Output queue size : 0
  Index 8, Advertise bit 7
  8 update-group member
  HMCO-core peer-group member
  NEXT_HOP is always this router for eBGP paths
  Community attribute sent to this neighbor
  Slow-peer detection is disabled
  Slow-peer split-update-group dynamic is disabled
  Interface associated: (none)
                                 Sent       Rcvd
  Prefix activity:               ----       ----
    Prefixes Current:             563        169 (Consumes 13520 bytes)
    Prefixes Total:             27674      20492
    Implicit Withdraw:          11693       5943
    Explicit Withdraw:          15418      14380
    Used as bestpath:             n/a         10
    Used as multipath:            n/a          0

                                   Outbound    Inbound
  Local Policy Denied Prefixes:    --------    -------
    Bestpath from this peer:          12589        n/a
    Total:                            12589          0
  Number of NLRIs in the update sent: max 514, min 0
  Last detected as dynamic slow peer: never
  Dynamic slow peer recovered: never
  Minimum time between advertisement runs is 1 seconds
  Refresh Epoch: 1
  Last Sent Refresh Start-of-rib: never
  Last Sent Refresh End-of-rib: never
  Last Received Refresh Start-of-rib: never
  Last Received Refresh End-of-rib: never
				       Sent	  Rcvd
	Refresh activity:	       ----	  ----
	  Refresh Start-of-RIB          0          0
	  Refresh End-of-RIB            0          0

  Address tracking is enabled, the RIB does have a route to 104.22.155.173
  Connections established 1; dropped 0
  Last reset never
  Transport(tcp) path-mtu-discovery is enabled
  Graceful-Restart is disabled
Connection state is ESTAB, I/O status: 1, unread input bytes: 0            
Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 255
Local host: 47.101.28.250, Local port: 1039
Foreign host: 90.58.27.224, Foreign port: 179
Connection tableid (VRF): 0
Maximum output segment queue size: 50

Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

Event Timers (current time is 0x56F2E076A):
Timer          Starts    Wakeups            Next
Retrans       4569450          5             0x0
TimeWait            0          0             0x0
AckHold       4566922    4209405             0x0
SendWnd             0          0             0x0
KeepAlive           0          0             0x0
GiveUp              0          0             0x0
PmtuAger        38900      38899     0x56F30239C
DeadWait            0          0             0x0
Linger              0          0             0x0
ProcessQ            0          0             0x0

iss:   63323904  snduna:  151468819  sndnxt:  151468819
irs: 1216800858  rcvnxt: 1304621530

sndwnd:  15890  scale:      0  maxrcvwnd:  16384
rcvwnd:  16156  scale:      0  delrcvwnd:    228

SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
minRTT: 0 ms, maxRTT: 1690 ms, ACK hold: 200 ms
uptime: -1 ms, Sent idletime: 830 ms, Receive idletime: 1030 ms 
Status Flags: active open
Option Flags: nagle, path mtu capable, md5
IP Precedence value : 6

 Datagrams (max data segment is 1460 bytes):
Rcvd: 8852438 (out of order: 0), with data: 4567355, total data bytes: 87820671
Sent: 8840238 (retransmit: 5, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 4570488, total data bytes: 88144914

 Packets received in fast path: 0, fast processed: 0, slow path: 0
 fast lock acquisition failures: 0, slow path: 0
TCP Semaphore      0x38C42C38  FREE 

BGP neighbor is 42.116.171.166,  remote AS 65182, external link
 Description: nsxe-lan-rtr1
 Member of peer-group LAN for session parameters
  BGP version 4, remote router ID 62.166.23.23
  BGP state = Established, up for 38w4d
  Last read 00:00:00, last write 00:00:01, hold time is 15, keepalive interval is 5 seconds
  Configured hold time is 15, keepalive interval is 5 seconds
  Minimum holdtime from neighbor is 0 seconds
  Neighbor sessions:
    1 active, is not multisession capable (disabled)
  Neighbor capabilities:
    Route refresh: advertised and received(new)
    Four-octets ASN Capability: advertised and received
    Address family IPv4 Unicast: advertised and received
    Enhanced Refresh Capability: advertised and received
    Multisession Capability: 
    Stateful switchover support enabled: NO for session 1
  Message statistics:
    InQ depth is 0
    OutQ depth is 0
    
                         Sent       Rcvd
    Opens:                  1          1
    Notifications:          0          0
    Updates:            25328      26783
    Keepalives:       4554193    4552827
    Route Refresh:          0          1
    Total:            4579524    4579614
  Default minimum time between advertisement runs is 30 seconds

 For address family: IPv4 Unicast
  Session: 205.156.57.241
  BGP table version 55515, neighbor version 55515/0
  Output queue size : 0
  Index 2, Advertise bit 1
  2 update-group member
  LAN peer-group member
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Slow-peer detection is disabled
  Slow-peer split-update-group dynamic is disabled
  Interface associated: Port-channel3
                                 Sent       Rcvd
  Prefix activity:               ----       ----
    Prefixes Current:             566          9 (Consumes 720 bytes)
    Prefixes Total:             38073         12
    Implicit Withdraw:          25567          0
    Explicit Withdraw:          11940          3
    Used as bestpath:             n/a          7
    Used as multipath:            n/a          0

                                   Outbound    Inbound
  Local Policy Denied Prefixes:    --------    -------
    AS_PATH loop:                       n/a      48694
    Bestpath from this peer:             17        n/a
    Total:                               17      48694
  Number of NLRIs in the update sent: max 514, min 0
  Last detected as dynamic slow peer: never
  Dynamic slow peer recovered: never
  Minimum time between advertisement runs is 5 seconds
  Refresh Epoch: 2
  Last Sent Refresh Start-of-rib: 20w2d
  Last Sent Refresh End-of-rib: 20w2d
  Refresh-Out took 0 seconds
  Last Received Refresh Start-of-rib: 38w4d
  Last Received Refresh End-of-rib: 38w4d
  Refresh-In took 0 seconds
				       Sent	  Rcvd
	Refresh activity:	       ----	  ----
	  Refresh Start-of-RIB          1          1
	  Refresh End-of-RIB            1          1

  Address tracking is enabled, the RIB does have a route to 234.182.178.210
  Connections established 1; dropped 0
  Last reset never
  Transport(tcp) path-mtu-discovery is enabled
  Graceful-Restart is disabled
Connection state is ESTAB, I/O status: 1, unread input bytes: 0            
Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 1
Local host: 39.236.86.64, Local port: 179
Foreign host: 85.15.185.206, Foreign port: 28912
Connection tableid (VRF): 0
Maximum output segment queue size: 50

Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

Event Timers (current time is 0x56F2E0788):
Timer          Starts    Wakeups            Next
Retrans       4565119          8             0x0
TimeWait            0          0             0x0
AckHold       4567627    4091483             0x0
SendWnd             0          0             0x0
KeepAlive           0          0             0x0
GiveUp              0          0             0x0
PmtuAger            0          0             0x0
DeadWait            0          0             0x0
Linger              0          0             0x0
ProcessQ            0          0             0x0

iss: 1165022199  snduna: 1253344612  sndnxt: 1253344612
irs: 3669450514  rcvnxt: 3758042091

sndwnd:  16194  scale:      0  maxrcvwnd:  16384
rcvwnd:  15567  scale:      0  delrcvwnd:    817

SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
minRTT: 0 ms, maxRTT: 1690 ms, ACK hold: 200 ms
uptime: -1 ms, Sent idletime: 590 ms, Receive idletime: 790 ms 
Status Flags: passive open, gen tcbs
Option Flags: nagle, path mtu capable, md5, Retrans timeout
 IP Precedence value : 6

Datagrams (max data segment is 1460 bytes):
Rcvd: 8750829 (out of order: 0), with data: 4574238, total data bytes: 88591576
 Sent: 8732984 (retransmit: 8, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 4574502, total data bytes: 88322412

 Packets received in fast path: 0, fast processed: 0, slow path: 0
 fast lock acquisition failures: 0, slow path: 0
TCP Semaphore      0x3DC1BAEC  FREE 

BGP neighbor is 5.233.102.244,  remote AS 65181, external link
 Description: nsxe-vndr-rtr1
 Member of peer-group Vendor for session parameters
  BGP version 4, remote router ID 33.131.26.189
  BGP state = Established, up for 8w1d
  Last read 00:00:00, last write 00:00:01, hold time is 15, keepalive interval is 5 seconds
  Configured hold time is 15, keepalive interval is 5 seconds
  Minimum holdtime from neighbor is 0 seconds
  Neighbor sessions:
    1 active, is not multisession capable (disabled)
  Neighbor capabilities:
    Route refresh: advertised and received(new)
    Four-octets ASN Capability: advertised and received
    Address family IPv4 Unicast: advertised and received
    Enhanced Refresh Capability: advertised and received
    Multisession Capability: 
    Stateful switchover support enabled: NO for session 1
  Message statistics:
    InQ depth is 0
    OutQ depth is 0
    
                         Sent       Rcvd
    Opens:                  1          1
    Notifications:          0          0
    Updates:             1135        121
    Keepalives:        965497     965602
    Route Refresh:          0          0
    Total:             966633     965726
  Default minimum time between advertisement runs is 30 seconds

 For address family: IPv4 Unicast
  Session: 252.31.34.152
  BGP table version 55515, neighbor version 55515/0
  Output queue size : 0
  Index 24, Advertise bit 0
  24 update-group member
  Vendor peer-group member
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Inbound path policy configured
  Outbound path policy configured
  Route map for incoming advertisements is BGP_Vendor_in
  Route map for outgoing advertisements is BGP_Vendor_out
  Slow-peer detection is disabled
  Slow-peer split-update-group dynamic is disabled
  Interface associated: (none)
                                 Sent       Rcvd
  Prefix activity:               ----       ----
    Prefixes Current:             507         56 (Consumes 4480 bytes)
    Prefixes Total:              3163        211
    Implicit Withdraw:           1338         69
    Explicit Withdraw:           1318         86
    Used as bestpath:             n/a         56
    Used as multipath:            n/a          0

                                   Outbound    Inbound
  Local Policy Denied Prefixes:    --------    -------
    Other Policies:                     380        n/a
    Total:                              380          0
  Number of NLRIs in the update sent: max 504, min 0
  Last detected as dynamic slow peer: never
  Dynamic slow peer recovered: never
  Minimum time between advertisement runs is 5 seconds
  Refresh Epoch: 2
  Last Sent Refresh Start-of-rib: never
  Last Sent Refresh End-of-rib: never
  Last Received Refresh Start-of-rib: 8w1d
  Last Received Refresh End-of-rib: 8w1d
  Refresh-In took 0 seconds
				       Sent	  Rcvd
	Refresh activity:	       ----	  ----
	  Refresh Start-of-RIB          0          1
	  Refresh End-of-RIB            0          1

  Address tracking is enabled, the RIB does have a route to 132.220.214.224
  Connections established 3; dropped 2
  Last reset 8w1d, due to BGP protocol initialization
  External BGP neighbor may be up to 2 hops away.
  Transport(tcp) path-mtu-discovery is enabled
  Graceful-Restart is disabled
  TCP session must be opened actively
Connection state is ESTAB, I/O status: 1, unread input bytes: 0            
Connection is ECN Disabled, Mininum incoming TTL 253, Outgoing TTL 255
Local host: 216.31.37.199, Local port: 10158
Foreign host: 58.98.25.93, Foreign port: 179
Connection tableid (VRF): 0
Maximum output segment queue size: 50

Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

Event Timers (current time is 0x56F2E0788):
Timer          Starts    Wakeups            Next
Retrans        965809          0             0x0
TimeWait            0          0             0x0
AckHold        965655     913486             0x0
SendWnd             0          0             0x0
KeepAlive           0          0             0x0
GiveUp              0          0             0x0
PmtuAger            1          1             0x0
DeadWait            0          0             0x0
Linger              0          0             0x0
ProcessQ            0          0             0x0

iss: 2242315978  snduna: 2260751350  sndnxt: 2260751350
 irs: 1630580063  rcvnxt: 1648939350

sndwnd:  15206  scale:      0  maxrcvwnd:  16384
rcvwnd:  15776  scale:      0  delrcvwnd:    608

SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
minRTT: 0 ms, maxRTT: 1000 ms, ACK hold: 200 ms
uptime: -1 ms, Sent idletime: 110 ms, Receive idletime: 310 ms 
Status Flags: active open
Option Flags: nagle, path mtu capable, md5
IP Precedence value : 6

Datagrams (max data segment is 1380 bytes):
Rcvd: 1887905 (out of order: 0), with data: 965681, total data bytes: 18359286
Sent: 1892826 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 966076, total data bytes: 18435371

 Packets received in fast path: 0, fast processed: 0, slow path: 0
 fast lock acquisition failures: 0, slow path: 0
TCP Semaphore      0x3DD686A8  FREE 

BGP neighbor is 191.113.218.187,  remote AS 65181, external link
 Description: nsxe-vndr-rtr2
 Member of peer-group Vendor for session parameters
  BGP version 4, remote router ID 44.66.10.77
  BGP state = Idle
  Configured hold time is 15, keepalive interval is 5 seconds
  Minimum holdtime from neighbor is 0 seconds
  Neighbor sessions:
    0 active, is not multisession capable (disabled)
    Stateful switchover support enabled: NO
  Default minimum time between advertisement runs is 30 seconds

 For address family: IPv4 Unicast
  BGP table version 55515, neighbor version 1/55515
  Output queue size : 0
  Index 0, Advertise bit 0
  Address family unwanted by neighbor
  Vendor peer-group member
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Inbound path policy configured
  Outbound path policy configured
  Route map for incoming advertisements is BGP_Vendor_in
  Route map for outgoing advertisements is BGP_Vendor_out
  Slow-peer detection is disabled
  Slow-peer split-update-group dynamic is disabled
  Interface associated: (none)
                                 Sent       Rcvd
  Prefix activity:               ----       ----
    Prefixes Current:               0          0
    Prefixes Total:                 0          0
    Implicit Withdraw:              0          0
    Explicit Withdraw:              0          0
    Used as bestpath:             n/a          0
    Used as multipath:            n/a          0

                                   Outbound    Inbound
  Local Policy Denied Prefixes:    --------    -------
    Total:                                0          0
  Number of NLRIs in the update sent: max 504, min 0
  Last detected as dynamic slow peer: never
  Dynamic slow peer recovered: never
  Minimum time between advertisement runs is 5 seconds
  Refresh Epoch: 1
  Last Sent Refresh Start-of-rib: never
  Last Sent Refresh End-of-rib: never
  Last Received Refresh Start-of-rib: never
  Last Received Refresh End-of-rib: never
				       Sent	  Rcvd
	Refresh activity:	       ----	  ----
	  Refresh Start-of-RIB          0          0
	  Refresh End-of-RIB            0          0

  Address tracking is enabled, the RIB does have a route to 198.79.87.139
  Connections established 1; dropped 1
  Last reset 8w1d, due to BGP Notification received, no supported AFI/SAFI
  External BGP neighbor may be up to 2 hops away.
  Transport(tcp) path-mtu-discovery is enabled
  Graceful-Restart is disabled
  TCP session must be opened actively
  No active TCP connection
 
BGP neighbor is 50.231.89.165,  remote AS 65183, external link
 Description: nsxe-aws-rtr1
 Member of peer-group AWS for session parameters
  BGP version 4, remote router ID 103.170.198.79
  BGP state = Established, up for 8w1d
  Last read 00:00:02, last write 00:00:04, hold time is 15, keepalive interval is 5 seconds
  Configured hold time is 15, keepalive interval is 5 seconds
  Minimum holdtime from neighbor is 0 seconds
  Neighbor sessions:
    1 active, is not multisession capable (disabled)
  Neighbor capabilities:
    Route refresh: advertised and received(new)
    Four-octets ASN Capability: advertised and received
    Address family IPv4 Unicast: advertised and received
    Enhanced Refresh Capability: advertised and received
    Multisession Capability: 
    Stateful switchover support enabled: NO for session 1
  Message statistics:
    InQ depth is 0
    OutQ depth is 0
    
                         Sent       Rcvd
    Opens:                  1          1
    Notifications:          0          0
    Updates:              766        348
    Keepalives:        966339     966378
    Route Refresh:          0          0
    Total:             967108     966729
  Default minimum time between advertisement runs is 30 seconds

 For address family: IPv4 Unicast
  Session: 117.218.189.254
  BGP table version 55515, neighbor version 55515/0
  Output queue size : 0
  Index 23, Advertise bit 4
  23 update-group member
  AWS peer-group member
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Inbound path policy configured
  Outbound path policy configured
  Route map for incoming advertisements is BGP_AWS_in
  Route map for outgoing advertisements is BGP_AWS_out
  Slow-peer detection is disabled
  Slow-peer split-update-group dynamic is disabled
  Interface associated: (none)
                                 Sent       Rcvd
  Prefix activity:               ----       ----
    Prefixes Current:             489         76 (Consumes 6080 bytes)
    Prefixes Total:              3604        300
    Implicit Withdraw:           1793        150
    Explicit Withdraw:           1322         74
    Used as bestpath:             n/a         22
    Used as multipath:            n/a         76

                                   Outbound    Inbound
  Local Policy Denied Prefixes:    --------    -------
    Other Policies:                     615        n/a
    Total:                              615          0
  Number of NLRIs in the update sent: max 504, min 0
  Last detected as dynamic slow peer: never
  Dynamic slow peer recovered: never
  Minimum time between advertisement runs is 5 seconds
  Refresh Epoch: 2
  Last Sent Refresh Start-of-rib: 8w1d
  Last Sent Refresh End-of-rib: 8w1d
  Refresh-Out took 0 seconds
  Last Received Refresh Start-of-rib: 8w1d
  Last Received Refresh End-of-rib: 8w1d
  Refresh-In took 0 seconds
				       Sent	  Rcvd
	Refresh activity:	       ----	  ----
	  Refresh Start-of-RIB          1          1
	  Refresh End-of-RIB            1          1

  Address tracking is enabled, the RIB does have a route to 164.252.173.140
  Connections established 2; dropped 1
  Last reset 8w1d, due to BGP protocol initialization
  External BGP neighbor may be up to 2 hops away.
  Transport(tcp) path-mtu-discovery is enabled
  Graceful-Restart is disabled
  TCP session must be opened actively
Connection state is ESTAB, I/O status: 1, unread input bytes: 0            
Connection is ECN Disabled, Mininum incoming TTL 253, Outgoing TTL 255
Local host: 87.243.6.230, Local port: 10156
Foreign host: 211.76.120.22, Foreign port: 179
Connection tableid (VRF): 0
Maximum output segment queue size: 50

Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

Event Timers (current time is 0x56F2E079C):
Timer          Starts    Wakeups            Next
Retrans        966552          0             0x0
TimeWait            0          0             0x0
AckHold        966521     918506             0x0
SendWnd             0          0             0x0
KeepAlive           0          0             0x0
GiveUp              0          0             0x0
PmtuAger            1          1             0x0
DeadWait            0          0             0x0
Linger              0          0             0x0
ProcessQ            0          0             0x0
 
iss: 3081669307  snduna: 3100105984  sndnxt: 3100105984
irs:  682628929  rcvnxt:  701010163

sndwnd:  16023  scale:      0  maxrcvwnd:  16384
rcvwnd:  15035  scale:      0  delrcvwnd:   1349

SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
minRTT: 0 ms, maxRTT: 1000 ms, ACK hold: 200 ms
uptime: -1 ms, Sent idletime: 2470 ms, Receive idletime: 2670 ms 
Status Flags: active open
Option Flags: nagle, path mtu capable, md5
IP Precedence value : 6

 Datagrams (max data segment is 1380 bytes):
Rcvd: 1896164 (out of order: 0), with data: 966533, total data bytes: 18381233
Sent: 1898490 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 966721, total data bytes: 18436676

 Packets received in fast path: 0, fast processed: 0, slow path: 0
 fast lock acquisition failures: 0, slow path: 0
TCP Semaphore      0x3DD68658  FREE 

BGP neighbor is 121.216.88.225,  remote AS 65183, external link
 Description: nsxe-aws-rtr2
 Member of peer-group AWS for session parameters
  BGP version 4, remote router ID 220.111.31.249
  BGP state = Established, up for 8w1d
  Last read 00:00:01, last write 00:00:04, hold time is 15, keepalive interval is 5 seconds
  Configured hold time is 15, keepalive interval is 5 seconds
  Minimum holdtime from neighbor is 0 seconds
  Neighbor sessions:
    1 active, is not multisession capable (disabled)
  Neighbor capabilities:
    Route refresh: advertised and received(new)
    Four-octets ASN Capability: advertised and received
    Address family IPv4 Unicast: advertised and received
    Enhanced Refresh Capability: advertised and received
    Multisession Capability: 
    Stateful switchover support enabled: NO for session 1
  Message statistics:
    InQ depth is 0
    OutQ depth is 0
    
                         Sent       Rcvd
    Opens:                  1          1
    Notifications:          0          0
    Updates:              769        335
    Keepalives:        966340     966371
    Route Refresh:          0          0
    Total:             967110     966707
  Default minimum time between advertisement runs is 30 seconds

 For address family: IPv4 Unicast
  Session: 113.21.95.163
  BGP table version 55515, neighbor version 55515/0
  Output queue size : 0
  Index 23, Advertise bit 4
  23 update-group member
  AWS peer-group member
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Inbound path policy configured
  Outbound path policy configured
  Route map for incoming advertisements is BGP_AWS_in
  Route map for outgoing advertisements is BGP_AWS_out
  Slow-peer detection is disabled
  Slow-peer split-update-group dynamic is disabled
  Interface associated: (none)
                                 Sent       Rcvd
  Prefix activity:               ----       ----
    Prefixes Current:             489         76 (Consumes 6080 bytes)
    Prefixes Total:              3604        280
    Implicit Withdraw:           1793        120
    Explicit Withdraw:           1322         84
    Used as bestpath:             n/a         54
    Used as multipath:            n/a         76

                                   Outbound    Inbound
  Local Policy Denied Prefixes:    --------    -------
    Other Policies:                     615        n/a
    Total:                              615          0
  Number of NLRIs in the update sent: max 504, min 0
  Last detected as dynamic slow peer: never
  Dynamic slow peer recovered: never
  Minimum time between advertisement runs is 5 seconds
  Refresh Epoch: 1
  Last Sent Refresh Start-of-rib: never
  Last Sent Refresh End-of-rib: never
  Last Received Refresh Start-of-rib: never
  Last Received Refresh End-of-rib: never
				       Sent	  Rcvd
 	Refresh activity:	       ----	  ----
	  Refresh Start-of-RIB          0          0
	  Refresh End-of-RIB            0          0

  Address tracking is enabled, the RIB does have a route to 126.166.143.50
  Connections established 2; dropped 1
  Last reset 8w1d, due to BGP protocol initialization
  External BGP neighbor may be up to 2 hops away.
  Transport(tcp) path-mtu-discovery is enabled
  Graceful-Restart is disabled
  TCP session must be opened actively
 Connection state is ESTAB, I/O status: 1, unread input bytes: 0            
 Connection is ECN Disabled, Mininum incoming TTL 253, Outgoing TTL 255
Local host: 69.201.247.212, Local port: 10153
Foreign host: 201.3.14.224, Foreign port: 179
Connection tableid (VRF): 0
Maximum output segment queue size: 50
 
Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

 Event Timers (current time is 0x56F2E07A6):
Timer          Starts    Wakeups            Next
Retrans        966551          0             0x0
TimeWait            0          0             0x0
AckHold        966516     913881             0x0
SendWnd             0          0             0x0
KeepAlive           0          0             0x0
GiveUp              0          0             0x0
PmtuAger            1          1             0x0
DeadWait            0          0             0x0
Linger              0          0             0x0
ProcessQ            0          0             0x0

iss: 3605059539  snduna: 3623496403  sndnxt: 3623496403
irs: 3608557898  rcvnxt: 3626937928

sndwnd:  16023  scale:      0  maxrcvwnd:  16384
rcvwnd:  15434  scale:      0  delrcvwnd:    950

SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
minRTT: 0 ms, maxRTT: 1000 ms, ACK hold: 200 ms
uptime: -1 ms, Sent idletime: 1090 ms, Receive idletime: 1290 ms 
Status Flags: active open
Option Flags: nagle, path mtu capable, md5
IP Precedence value : 6

 Datagrams (max data segment is 1380 bytes):
Rcvd: 1891283 (out of order: 0), with data: 966532, total data bytes: 18380029
Sent: 1893869 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 966721, total data bytes: 18436863

 Packets received in fast path: 0, fast processed: 0, slow path: 0
 fast lock acquisition failures: 0, slow path: 0
TCP Semaphore      0x3DD68748  FREE 

BGP neighbor is 71.163.23.191,  remote AS 65184, external link
 Description: nsxe-merge-rtr1
 Member of peer-group Merge for session parameters
  BGP version 4, remote router ID 252.9.89.15
  BGP state = Idle
  Configured hold time is 15, keepalive interval is 5 seconds
  Minimum holdtime from neighbor is 0 seconds
  Neighbor sessions:
    0 active, is not multisession capable (disabled)
    Stateful switchover support enabled: NO
  Default minimum time between advertisement runs is 30 seconds

 For address family: IPv4 Unicast
  BGP table version 55515, neighbor version 1/55515
  Output queue size : 0
  Index 0, Advertise bit 0
  Address family unwanted by neighbor
  Merge peer-group member
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Inbound path policy configured
  Outbound path policy configured
  Route map for incoming advertisements is BGP_Merge_in
  Route map for outgoing advertisements is BGP_Merge_out
  Slow-peer detection is disabled
  Slow-peer split-update-group dynamic is disabled
  Interface associated: (none)
                                 Sent       Rcvd
  Prefix activity:               ----       ----
    Prefixes Current:               0          0
    Prefixes Total:                 0          0
    Implicit Withdraw:              0          0
    Explicit Withdraw:              0          0
    Used as bestpath:             n/a          0
    Used as multipath:            n/a          0

                                   Outbound    Inbound
  Local Policy Denied Prefixes:    --------    -------
    Total:                                0          0
  Number of NLRIs in the update sent: max 514, min 0
  Last detected as dynamic slow peer: never
  Dynamic slow peer recovered: never
  Minimum time between advertisement runs is 5 seconds
  Refresh Epoch: 1
  Last Sent Refresh Start-of-rib: never
  Last Sent Refresh End-of-rib: never
  Last Received Refresh Start-of-rib: never
  Last Received Refresh End-of-rib: never
				       Sent	  Rcvd
	Refresh activity:	       ----	  ----
	  Refresh Start-of-RIB          0          0
	  Refresh End-of-RIB            0          0

  Address tracking is enabled, the RIB does have a route to 136.152.166.35
  Connections established 2; dropped 2
  Last reset 8w1d, due to BGP Notification received, no supported AFI/SAFI
  External BGP neighbor may be up to 2 hops away.
  Transport(tcp) path-mtu-discovery is enabled
  Graceful-Restart is disabled
  TCP session must be opened actively
  No active TCP connection
 
BGP neighbor is 87.90.154.72,  remote AS 65004, external link
 Description: nsxe-ent-l3ce1 (CASR1001-ET-01 gm73688) direct
 Member of peer-group L3-CE-SEC for session parameters
  BGP version 4, remote router ID 245.20.27.53
  BGP state = Idle
  Configured hold time is 15, keepalive interval is 5 seconds
  Minimum holdtime from neighbor is 0 seconds
  Neighbor sessions:
    0 active, is not multisession capable (disabled)
    Stateful switchover support enabled: NO
  Default minimum time between advertisement runs is 30 seconds
 
 For address family: IPv4 Unicast
  BGP table version 55515, neighbor version 1/55515
  Output queue size : 0
  Index 0, Advertise bit 0
  L3-CE-SEC peer-group member
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Inbound path policy configured
  Outbound path policy configured
  Route map for incoming advertisements is BGP-L3-CE-SEC-in
  Route map for outgoing advertisements is BGP-L3-CE-SEC-out
  Slow-peer detection is disabled
  Slow-peer split-update-group dynamic is disabled
  Interface associated: GigabitEthernet1/0/13
                                 Sent       Rcvd
  Prefix activity:               ----       ----
    Prefixes Current:               0          0
    Prefixes Total:                 0          0
    Implicit Withdraw:              0          0
    Explicit Withdraw:              0          0
    Used as bestpath:             n/a          0
    Used as multipath:            n/a          0

                                   Outbound    Inbound
  Local Policy Denied Prefixes:    --------    -------
    Total:                                0          0
  Number of NLRIs in the update sent: max 478, min 0
  Last detected as dynamic slow peer: never
  Dynamic slow peer recovered: never
  Minimum time between advertisement runs is 5 seconds
  Refresh Epoch: 1
  Last Sent Refresh Start-of-rib: never
  Last Sent Refresh End-of-rib: never
  Last Received Refresh Start-of-rib: never
  Last Received Refresh End-of-rib: never
				       Sent	  Rcvd
	Refresh activity:	       ----	  ----
	  Refresh Start-of-RIB          0          0
	  Refresh End-of-RIB            0          0

  Address tracking is enabled, the RIB does have a route to 173.122.238.227
  Connections established 1; dropped 1
  Last reset 25w2d, due to Interface flap of session 1
  External BGP neighbor not directly connected.
  Transport(tcp) path-mtu-discovery is enabled
  Graceful-Restart is disabled
  No active TCP connection

BGP neighbor is 35.139.51.35,  remote AS 65004, external link
 Description: nsxe-ent-l3ce2 (CASR1001-ET-02 gm73690) via riverbed
 Member of peer-group L3-CE-PRI for session parameters
  BGP version 4, remote router ID 164.86.209.25
  BGP state = Idle
  Configured hold time is 15, keepalive interval is 5 seconds
  Minimum holdtime from neighbor is 0 seconds
  Neighbor sessions:
    0 active, is not multisession capable (disabled)
    Stateful switchover support enabled: NO
  Default minimum time between advertisement runs is 30 seconds

 For address family: IPv4 Unicast
  BGP table version 55515, neighbor version 1/55515
  Output queue size : 0
  Index 0, Advertise bit 0
  L3-CE-PRI peer-group member
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Inbound path policy configured
  Outbound path policy configured
  Route map for incoming advertisements is BGP-L3-CE-PRI-in
  Route map for outgoing advertisements is BGP-L3-CE-PRI-out
  Slow-peer detection is disabled
  Slow-peer split-update-group dynamic is disabled
  Interface associated: GigabitEthernet1/0/1
                                 Sent       Rcvd
  Prefix activity:               ----       ----
    Prefixes Current:               0          0
    Prefixes Total:                 0          0
    Implicit Withdraw:              0          0
    Explicit Withdraw:              0          0
    Used as bestpath:             n/a          0
    Used as multipath:            n/a          0

                                   Outbound    Inbound
  Local Policy Denied Prefixes:    --------    -------
    Total:                                0          0
  Number of NLRIs in the update sent: max 478, min 0
  Last detected as dynamic slow peer: never
  Dynamic slow peer recovered: never
  Minimum time between advertisement runs is 5 seconds
  Refresh Epoch: 1
  Last Sent Refresh Start-of-rib: never
  Last Sent Refresh End-of-rib: never
  Last Received Refresh Start-of-rib: never
  Last Received Refresh End-of-rib: never
				       Sent	  Rcvd
	Refresh activity:	       ----	  ----
	  Refresh Start-of-RIB          0          0
	  Refresh End-of-RIB            0          0

  Address tracking is enabled, the RIB does have a route to 203.247.36.3
  Connections established 2; dropped 2
  Last reset 25w2d, due to Interface flap of session 1
  External BGP neighbor not directly connected.
  Transport(tcp) path-mtu-discovery is enabled
  Graceful-Restart is disabled
  No active TCP connection

BGP neighbor is 13.167.37.139,  remote AS 64514, external link
 Description: SDWAN-DIA
 Member of peer-group SDWAN-DIA for session parameters
  BGP version 4, remote router ID 127.89.47.147
  BGP state = Established, up for 5w6d
  Last read 00:00:03, last write 00:00:01, hold time is 15, keepalive interval is 5 seconds
  Configured hold time is 15, keepalive interval is 5 seconds
  Minimum holdtime from neighbor is 0 seconds
  Neighbor sessions:
    1 active, is not multisession capable (disabled)
  Neighbor capabilities:
    Route refresh: advertised and received(new)
    Four-octets ASN Capability: advertised and received
    Address family IPv4 Unicast: advertised and received
    Address family IPv6 Unicast: received
    Enhanced Refresh Capability: advertised
    Multisession Capability: 
    Stateful switchover support enabled: NO for session 1
  Message statistics:
    InQ depth is 0
    OutQ depth is 0
    
                         Sent       Rcvd
    Opens:                  1          1
    Notifications:          0          0
    Updates:              504        439
    Keepalives:        701190     825244
    Route Refresh:          0          0
    Total:             701695     825684
  Default minimum time between advertisement runs is 30 seconds

 For address family: IPv4 Unicast
  Session: 186.131.158.4
  BGP table version 55515, neighbor version 55515/0
  Output queue size : 0
  Index 27, Advertise bit 3
  27 update-group member
  SDWAN-DIA peer-group member
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Inbound path policy configured
  Outbound path policy configured
  Incoming update network filter list is 1
  Route map for incoming advertisements is BGP-SDWAN-in
  Route map for outgoing advertisements is BGP-SDWAN-out
  Slow-peer detection is disabled
  Slow-peer split-update-group dynamic is disabled
  Interface associated: Vlan990
                                 Sent       Rcvd
  Prefix activity:               ----       ----
    Prefixes Current:             172        401 (Consumes 64160 bytes)
    Prefixes Total:               906        710
    Implicit Withdraw:            196         49
    Explicit Withdraw:            538        260
    Used as bestpath:             n/a        401
    Used as multipath:            n/a          0
    Saved (soft-reconfig):        n/a        401 (Consumes 32080 bytes)

                                   Outbound    Inbound
  Local Policy Denied Prefixes:    --------    -------
    AS_PATH loop:                       n/a        171
    Bestpath from this peer:            696        n/a
    Total:                              696        171
  Number of NLRIs in the update sent: max 161, min 0
  Last detected as dynamic slow peer: never
  Dynamic slow peer recovered: never
  Minimum time between advertisement runs is 5 seconds
  Refresh Epoch: 1
  Last Sent Refresh Start-of-rib: never
  Last Sent Refresh End-of-rib: never
  Last Received Refresh Start-of-rib: never
  Last Received Refresh End-of-rib: never
				       Sent	  Rcvd
	Refresh activity:	       ----	  ----
	  Refresh Start-of-RIB          0          0
	  Refresh End-of-RIB            0          0

  Address tracking is enabled, the RIB does have a route to 31.89.40.20
  Connections established 12; dropped 11
  Last reset 5w6d, due to Active open failed
  Transport(tcp) path-mtu-discovery is enabled
  Graceful-Restart is disabled
Connection state is ESTAB, I/O status: 1, unread input bytes: 0            
Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 1
Local host: 203.2.115.150, Local port: 10926
Foreign host: 152.83.67.150, Foreign port: 179
Connection tableid (VRF): 0
Maximum output segment queue size: 50

Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

Event Timers (current time is 0x56F2E07BA):
Timer          Starts    Wakeups            Next
Retrans        701373          6             0x0
TimeWait            0          0             0x0
AckHold        825469     784292             0x0
SendWnd             0          0             0x0
KeepAlive           0          0             0x0
GiveUp              0          0             0x0
PmtuAger         5984       5983     0x56F2F0DAE
DeadWait            0          0             0x0
Linger              0          0             0x0
ProcessQ            0          0             0x0

iss: 2944481514  snduna: 2957842032  sndnxt: 2957842032
 irs: 1075563855  rcvnxt: 1091276216

sndwnd:  64240  scale:      0  maxrcvwnd:  16384
rcvwnd:  15928  scale:      0  delrcvwnd:    456

SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
minRTT: 0 ms, maxRTT: 1000 ms, ACK hold: 200 ms
uptime: -704633926 ms, Sent idletime: 1840 ms, Receive idletime: 1840 ms 
Status Flags: active open
Option Flags: nagle, path mtu capable
IP Precedence value : 6

Datagrams (max data segment is 1460 bytes):
Rcvd: 1526890 (out of order: 0), with data: 825473, total data bytes: 15712360
Sent: 1496482 (retransmit: 6, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 701376, total data bytes: 13360517

 Packets received in fast path: 0, fast processed: 0, slow path: 0
 fast lock acquisition failures: 0, slow path: 0
TCP Semaphore      0x3DC1B9FC  FREE 

BGP neighbor is 72.37.28.119,  remote AS 18830, external link
 Description: nsxe-int-rtr1
 Member of peer-group Internet for session parameters
  BGP version 4, remote router ID 167.184.30.114
  BGP state = Established, up for 8w1d
  Last read 00:00:02, last write 00:00:02, hold time is 15, keepalive interval is 5 seconds
  Configured hold time is 15, keepalive interval is 5 seconds
  Minimum holdtime from neighbor is 0 seconds
  Neighbor sessions:
    1 active, is not multisession capable (disabled)
  Neighbor capabilities:
    Route refresh: advertised and received(new)
    Four-octets ASN Capability: advertised and received
    Address family IPv4 Unicast: advertised and received
    Enhanced Refresh Capability: advertised and received
    Multisession Capability: 
    Stateful switchover support enabled: NO for session 1
  Message statistics:
    InQ depth is 0
    OutQ depth is 0
    
                         Sent       Rcvd
    Opens:                  1          1
    Notifications:          0          0
    Updates:                1          5
    Keepalives:        965620     965619
    Route Refresh:          0          0
    Total:             965624     965627
  Default minimum time between advertisement runs is 30 seconds

 For address family: IPv4 Unicast
  Session: 225.120.110.131
  BGP table version 55515, neighbor version 55515/0
  Output queue size : 0
  Index 25, Advertise bit 2
  25 update-group member
  Internet peer-group member
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Inbound path policy configured
  Outbound path policy configured
  Route map for incoming advertisements is BGP_Internet_in
  Route map for outgoing advertisements is BGP_Internet_out
  Slow-peer detection is disabled
  Slow-peer split-update-group dynamic is disabled
  Interface associated: (none)
                                 Sent       Rcvd
  Prefix activity:               ----       ----
    Prefixes Current:               0          5 (Consumes 400 bytes)
    Prefixes Total:                 0          5
    Implicit Withdraw:              0          0
    Explicit Withdraw:              0          0
    Used as bestpath:             n/a          0
    Used as multipath:            n/a          5

                                   Outbound    Inbound
  Local Policy Denied Prefixes:    --------    -------
    Other Policies:                    4069        n/a
    Total:                             4069          0
  Number of NLRIs in the update sent: max 0, min 0
  Last detected as dynamic slow peer: never
  Dynamic slow peer recovered: never
  Minimum time between advertisement runs is 5 seconds
  Refresh Epoch: 2
  Last Sent Refresh Start-of-rib: 8w1d
  Last Sent Refresh End-of-rib: 8w1d
  Refresh-Out took 0 seconds
  Last Received Refresh Start-of-rib: 8w1d
  Last Received Refresh End-of-rib: 8w1d
  Refresh-In took 0 seconds
				       Sent	  Rcvd
 	Refresh activity:	       ----	  ----
	  Refresh Start-of-RIB          1          1
	  Refresh End-of-RIB            1          1

  Address tracking is enabled, the RIB does have a route to 134.194.251.21
  Connections established 3; dropped 2
  Last reset 8w1d, due to BGP protocol initialization
  External BGP neighbor may be up to 2 hops away.
  Transport(tcp) path-mtu-discovery is enabled
  Graceful-Restart is disabled
  TCP session must be opened actively
 Connection state is ESTAB, I/O status: 1, unread input bytes: 0            
 Connection is ECN Disabled, Mininum incoming TTL 253, Outgoing TTL 255
Local host: 98.13.124.95, Local port: 10160
Foreign host: 29.194.88.38, Foreign port: 179
Connection tableid (VRF): 0
Maximum output segment queue size: 50

 Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

Event Timers (current time is 0x56F2E07C4):
Timer          Starts    Wakeups            Next
Retrans        965622          0             0x0
TimeWait            0          0             0x0
AckHold        965621     906305             0x0
SendWnd             0          0             0x0
KeepAlive           0          0             0x0
GiveUp              0          0             0x0
PmtuAger            1          1             0x0
DeadWait            0          0             0x0
Linger              0          0             0x0
ProcessQ            0          0             0x0

iss:  443328812  snduna:  461675719  sndnxt:  461675719
irs:  358195107  rcvnxt:  376542326

sndwnd:  15320  scale:      0  maxrcvwnd:  16384
rcvwnd:  15016  scale:      0  delrcvwnd:   1368

SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
minRTT: 0 ms, maxRTT: 1000 ms, ACK hold: 200 ms
uptime: -1 ms, Sent idletime: 2880 ms, Receive idletime: 2680 ms 
Status Flags: active open
Option Flags: nagle, path mtu capable, md5
IP Precedence value : 6

 Datagrams (max data segment is 1380 bytes):
Rcvd: 1899964 (out of order: 0), with data: 965622, total data bytes: 18347218
Sent: 1885160 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 965623, total data bytes: 18346906

 Packets received in fast path: 0, fast processed: 0, slow path: 0
 fast lock acquisition failures: 0, slow path: 0
TCP Semaphore      0x3DD68568  FREE 

BGP neighbor is 201.93.188.161,  remote AS 18830, external link
 Description: nsxe-int-rtr2
 Member of peer-group Internet for session parameters
  BGP version 4, remote router ID 208.50.107.235
  BGP state = Established, up for 8w1d
  Last read 00:00:02, last write 00:00:02, hold time is 15, keepalive interval is 5 seconds
  Configured hold time is 15, keepalive interval is 5 seconds
  Minimum holdtime from neighbor is 0 seconds
  Neighbor sessions:
    1 active, is not multisession capable (disabled)
  Neighbor capabilities:
    Route refresh: advertised and received(new)
    Four-octets ASN Capability: advertised and received
    Address family IPv4 Unicast: advertised and received
    Enhanced Refresh Capability: advertised and received
    Multisession Capability: 
    Stateful switchover support enabled: NO for session 1
  Message statistics:
    InQ depth is 0
    OutQ depth is 0
    
                         Sent       Rcvd
    Opens:                  1          1
    Notifications:          0          0
    Updates:                1          5
    Keepalives:        965621     965622
    Route Refresh:          0          0
    Total:             965623     965630
  Default minimum time between advertisement runs is 30 seconds

 For address family: IPv4 Unicast
  Session: 144.132.205.228
  BGP table version 55515, neighbor version 55515/0
  Output queue size : 0
  Index 25, Advertise bit 2
  25 update-group member
  Internet peer-group member
  Inbound soft reconfiguration allowed
  Community attribute sent to this neighbor
  Inbound path policy configured
  Outbound path policy configured
  Route map for incoming advertisements is BGP_Internet_in
  Route map for outgoing advertisements is BGP_Internet_out
  Slow-peer detection is disabled
  Slow-peer split-update-group dynamic is disabled
  Interface associated: (none)
                                 Sent       Rcvd
  Prefix activity:               ----       ----
    Prefixes Current:               0          5 (Consumes 400 bytes)
    Prefixes Total:                 0          5
    Implicit Withdraw:              0          0
    Explicit Withdraw:              0          0
    Used as bestpath:             n/a          5
    Used as multipath:            n/a          5

                                   Outbound    Inbound
  Local Policy Denied Prefixes:    --------    -------
    Other Policies:                    4069        n/a
    Total:                             4069          0
  Number of NLRIs in the update sent: max 0, min 0
  Last detected as dynamic slow peer: never
  Dynamic slow peer recovered: never
  Minimum time between advertisement runs is 5 seconds
  Refresh Epoch: 2
  Last Sent Refresh Start-of-rib: never
  Last Sent Refresh End-of-rib: never
  Last Received Refresh Start-of-rib: 8w1d
  Last Received Refresh End-of-rib: 8w1d
  Refresh-In took 0 seconds
				       Sent	  Rcvd
	Refresh activity:	       ----	  ----
	  Refresh Start-of-RIB          0          1
	  Refresh End-of-RIB            0          1

  Address tracking is enabled, the RIB does have a route to 39.75.88.112
  Connections established 4; dropped 3
  Last reset 8w1d, due to BGP Notification received of session 1, hold time expired
  External BGP neighbor may be up to 2 hops away.
  Transport(tcp) path-mtu-discovery is enabled
  Graceful-Restart is disabled
  TCP session must be opened actively
 Connection state is ESTAB, I/O status: 1, unread input bytes: 0            
 Connection is ECN Disabled, Mininum incoming TTL 253, Outgoing TTL 255
Local host: 125.0.195.99, Local port: 10159
Foreign host: 84.229.16.220, Foreign port: 179
Connection tableid (VRF): 0
Maximum output segment queue size: 50
 
Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)

 Event Timers (current time is 0x56F2E07CE):
Timer          Starts    Wakeups            Next
Retrans        965624          1             0x0
TimeWait            0          0             0x0
AckHold        965624     946418             0x0
SendWnd             0          0             0x0
KeepAlive           0          0             0x0
GiveUp              0          0             0x0
PmtuAger            1          1             0x0
DeadWait            0          0             0x0
Linger              0          0             0x0
ProcessQ            0          0             0x0

iss: 1700449210  snduna: 1718796090  sndnxt: 1718796090
irs: 3379899633  rcvnxt: 3398246909

sndwnd:  15358  scale:      0  maxrcvwnd:  16384
rcvwnd:  16346  scale:      0  delrcvwnd:     38

SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
minRTT: 0 ms, maxRTT: 1010 ms, ACK hold: 200 ms
uptime: -1 ms, Sent idletime: 2890 ms, Receive idletime: 2690 ms 
Status Flags: active open
Option Flags: nagle, path mtu capable, md5
IP Precedence value : 6

 Datagrams (max data segment is 1380 bytes):
Rcvd: 1921217 (out of order: 0), with data: 965625, total data bytes: 18347275
Sent: 1925273 (retransmit: 1, fastretransmit: 0, partialack: 0, Second Congestion: 0), with data: 965623, total data bytes: 18346879

 Packets received in fast path: 0, fast processed: 0, slow path: 0
 fast lock acquisition failures: 0, slow path: 0
TCP Semaphore      0x3DD685B8  FREE 

```

**Help:** execute the command "show ip bgp neighbors"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show power status

**Output:**
```
Power                                             Fan      Inline
Supply  Model No          Type       Status       Sensor   Status
------  ----------------  ---------  -----------  -------  -------
PS1     PWR-C45-4200ACV   AC 4200W   good         good     good   
PS1-1                         220V   good         
PS1-2                         220V   good         
PS2     PWR-C45-4200ACV   AC 4200W   err-disable  good     good   
PS2-1                                off          
PS2-2                         220V   good         
 
*** Power Supplies of different type have been detected***

```

**Help:** execute the command "show power status"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip bgp summary

**Output:**
```
BGP router identifier 10.0.0.0, local AS number 65000
BGP table version is 512185206, main routing table version 512185206
566019 network entries using 140372712 bytes of memory
4478571 path entries using 501599952 bytes of memory
 448860/89167 BGP path/bestpath attribute entries using 100544640 bytes of memory
 78 BGP rrinfo entries using 3120 bytes of memory
208442 BGP AS-PATH entries using 10129234 bytes of memory
1790 BGP community entries using 180118 bytes of memory
30 BGP extended community entries using 976 bytes of memory
1015 BGP route-map cache entries using 64960 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
BGP using 752895712 total bytes of memory
 1121781 received paths for inbound soft reconfiguration
BGP activity 19247146/18656050 prefixes, 368760729/364163114 paths, scan interval 60 secs

Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
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

```

**Help:** execute the command "show ip bgp summary"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show dot1x all

**Output:**
```
Sysauthcontrol             Disabled
Dot1x Protocol Version            2
Critical Recovery Delay         100
Critical EAPOL             Disabled
 
Dot1x Info for Ethernet1/0
-----------------------------------
PAE                       = AUTHENTICATOR
PortControl               = AUTO
ControlDirection          = Both
HostMode                  = SINGLE_HOST
ReAuthentication          = Disabled
QuietPeriod               = 60
ServerTimeout             = 30
SuppTimeout               = 30
ReAuthPeriod              = 3600 (Locally configured)
ReAuthMax                 = 2
MaxReq                    = 2
TxPeriod                  = 30
RateLimitPeriod           = 0

 Dot1x Info for Ethernet1/2
-----------------------------------

PAE                       = AUTHENTICATOR
PortControl               = AUTO
ControlDirection          = Both
HostMode                  = SINGLE_HOST
ReAuthentication          = Disabled
QuietPeriod               = 60
ServerTimeout             = 30
SuppTimeout               = 30
ReAuthPeriod              = 3600 (Locally configured)
ReAuthMax                 = 2
MaxReq                    = 2
TxPeriod                  = 30
RateLimitPeriod           = 0

```

**Help:** execute the command "show dot1x all"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show nve vni

**Output:**
```
Interface  VNI        Multicast-group VNI state  Mode  BD    cfg vrf                                         
nve1       10306   N/A             Up         L3CP  306  CLI GRY                     
nve1       10303   N/A             Up         L3CP  303  CLI AMB                     
nve1       10302   N/A             Up         L3CP  302  CLI GRN                                         
nve1       10301   N/A             Up         L3CP  301  CLI BLU  
```

**Help:** execute the command "show nve vni"

**Prompt:**
- cisco_ios>
- cisco_ios#

### dir

**Output:**
```
Directory of bootflash:/

   11  drwx            16384   Mar 2 2015 08:46:31 +00:00  lost+found
681409  drwx             4096   Mar 2 2015 08:47:35 +00:00  .super.iso.dir
   12  -rw-               46  Apr 22 2016 12:36:24 +00:00  .CsrLxc_LastInstall
   13  -rw-               84   Mar 2 2015 08:50:43 +00:00  virtual-instance.conf
876097  drwx             4096   Mar 2 2015 08:49:40 +00:00  core
   15  -rw-        161136640   Mar 2 2015 08:47:34 +00:00  iosxe-remote-mgmt.03.14.01.S.155-1.S1-std.ova
519172  -rw-        250578048   Mar 2 2015 08:48:31 +00:00  csr1000v-mono-universalk9.03.14.01.S.155-1.S1-std.SPA.pkg
519170  -rw-             4892   Mar 2 2015 08:48:30 +00:00  csr1000v-packages-universalk9.03.14.01.S.155-1.S1-std.conf
519171  -rw  -             5681   Mar 2 2015 08:48:31 +00:00  packages.conf
827425  drwx             4096   Mar 2 2015 08:49:40 +00:00  .prst_sync
730081  drwx             4096   Mar 2 2015 08:49:43 +00:00  .rollback_timer
   16  -rw-                0   Mar 2 2015 08:49:46 +00:00  tracelogs.394

7835619328 bytes total (6612774912 bytes free)
```

**Help:** execute the command "dir"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show cdp neighbors

**Output:**
```
Capability Codes: R - Router, T - Trans Bridge, B- Source Route Bridge
	       S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone

Device ID         Local Intrfce Holdtme    Capability   Platform   Port ID
R1-PBX            Gig 1/0/10    144          R S I      2811       Fas 0/0
TS-1              Gig 1/0/39    122          R          2611       Eth 0/1
Cisco-WAP-N       Gig 1/0/1     120          T I        AIR-AP125  Gig 0
SEP04FE7F689D33   Gig 1/0/2     125          H P        IP Phone   Port 1
SEP000DBC50FCD1   Gig 1/0/4     147          H P        IP Phone   Port 1
SEP00124362C4D2   Gig 1/0/42    147          H P        IP Phone   Port 1

```

**Help:** execute the command "show cdp neighbors"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip route

**Output:**
```
Tue May 22 22:32:30.765 UTC

Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR

Gateway of last resort is 192.168.1.2 to network 0.0.0.0

      192.168.1.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.1.0/24 is directly connected, vasileft1
L        192.168.1.1/32 is directly connected, vasileft1

```

**Help:** execute the command "show ip route"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip ospf interface brief

**Output:**
```
Interface    PID   Area  IP Address/Mask    Cost  State Nbrs F/C
Lo0          1     0     172.16.0.11/32     1     LOOP  0/0
Se0/0/0.100  1     0     172.16.1.1/30      50    P2P   1/1
Fa0/0        1     0     10.0.0.5/24        1     BDR   1/1
Fa0/1        1     11    10.1.2.1/24        1     DR    0/0
Tu1610 		 1	   0 	 0.0.0.0/0			50 	  P2P 	0/0
Lo5 		 1	   0 	 10.48.8.5/32		1 	  LOOP 	0/0
Lo4 		 1	   0 	 10.48.8.4/32	 	1 	  LOOP 	0/0
Tu1603 		 1	   0 	 0.0.0.0/0			50	  DOWN 	0/0
 Tu1602 		 1	   0 	 0.0.0.0/0			50	  P2P 	0/0
PO4/0 		 1	   0 	 10.1.232.6/30 		6 	  P2P	1/1
Se3/2:0 	 1	   0 	 10.1.224.218/30 	6	  P2P	1/1
Se3/1:0 	 1	   0 	 10.1.225.150/30 	6	  P2P	1/1

```

**Help:** execute the command "show ip ospf interface brief"

**Prompt:**
- cisco_ios>
- cisco_ios#

### ping

**Output:**
```
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.245.179.14, timeout is 2 seconds:
U..U.
Success rate is 0 percent (0/5)

```

**Help:** execute the command "ping"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show etherchannel summary

**Output:**
```
Flags:  D - down        P/bndl - bundled in port-channel
        I - stand-alone s/susp - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port
 

Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
 10	Po10(RU)		LACP	 Te0/0/2(bndl) Te0/0/3(bndl)

RU - L3 port-channel UP State
SU - L2 port-channel UP state
P/bndl -  Bundled
S/susp  - Suspended

```

**Help:** execute the command "show etherchannel summary"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show processes cpu

**Output:**
```
CPU utilization for five seconds: 4%/0%; one minute: 6%; five minutes: 5%
 PID Runtime(ms)   Invoked      uSecs   5Sec   1Min   5Min TTY Process
   1           0        22          0  0.00%  0.00%  0.00%   0 Chunk Manager
   2          81    275153          0  0.00%  0.00%  0.00%   0 Load Meter
   3           0         1          0  0.00%  0.00%  0.00%   0 Connection Mgr
   4    12798734    606112      21116  0.00%  1.18%  0.92%   0 Check heaps
   5           0       175          0  0.00%  0.00%  0.00%   0 Pool Manager
   6           0         2          0  0.00%  0.00%  0.00%   0 Timers
   7        4176     92069         45  0.00%  0.00%  0.00%   0 Net Input
   8           0         1          0  0.00%  0.00%  0.00%   0 Crash writer
   9       71196    328952        216  0.00%  0.00%  0.00%   0 ARP Input
  10           0         1          0  0.00%  0.00%  0.00%   0 CEF MIB API
  11          16      3442          4  0.00%  0.00%  0.00%   0 AAA_SERVER_DEADT
  12           0         2          0  0.00%  0.00%  0.00%   0 AAA high-capacit
  13           0         1          0  0.00%  0.00%  0.00%   0 Policy Manager
  14          17         3       5666  0.00%  0.00%  0.00%   0 Entity MIB API
  15           0         1          0  0.00%  0.00%  0.00%   0 IFS Agent Manage
  16           8     22957          0  0.00%  0.00%  0.00%   0 IPC Dynamic Cach
  17           0         1          0  0.00%  0.00%  0.00%   0 IPC Zone Manager
  18          51   1368737          0  0.00%  0.00%  0.00%   0 IPC Periodic Tim
  19           0         1          0  0.00%  0.00%  0.00%   0 IPC Managed Time
  20          35   1368737          0  0.00%  0.00%  0.00%   0 IPC Deferred Por
  21           9     91820          0  0.00%  0.00%  0.00%   0 IPC Seat Manager
  22           0         1          0  0.00%  0.00%  0.00%   0 IPC Session Serv
  23         168         6      28000  0.00%  0.00%  0.00%   0 PrstVbl
  24         192   1368736          0  0.00%  0.00%  0.00%   0 Dynamic ARP Insp
  25           0         1          0  0.00%  0.00%  0.00%   0 ARP Snoop
  26         265   1368710          0  0.00%  0.00%  0.00%   0 GraphIt
  27           0         2          0  0.00%  0.00%  0.00%   0 XML Proxy Client
  28           0         1          0  0.00%  0.00%  0.00%   0 Critical Bkgnd
  29         556    585865          0  0.00%  0.00%  0.00%   0 Net Background
  30           0         1          0  0.00%  0.00%  0.00%   0 IDB Work
  31           9        31        290  0.00%  0.00%  0.00%   0 Logger
  32         534   1368706          0  0.00%  0.00%  0.00%   0 TTY Background
  33         957   1368765          0  0.00%  0.00%  0.00%   0 Per-Second Jobs
  34      577745     23165      24940  0.00%  0.04%  0.00%   0 Per-minute Jobs
  35           0         6          0  0.00%  0.00%  0.00%   0 IF-MGR control p
  36           0         8          0  0.00%  0.00%  0.00%   0 IF-MGR event pro
  37         511    275156          1  0.00%  0.00%  0.00%   0 Compute load avg
  38           0         1          0  0.00%  0.00%  0.00%   0 AggMgr Process
  39           0      1615          0  0.00%  0.00%  0.00%   0 Transport Port A
  40         294    412572          0  0.00%  0.00%  0.00%   0 HC Counter Timer
  41           0         1          0  0.00%  0.00%  0.00%   0 SFF8472
  42         847  27329654          0  0.00%  0.00%  0.00%   0 DownWhenLooped
  43           0         1          0  0.00%  0.00%  0.00%   0 HULC PBR Tcam Me
  44           0         1          0  0.00%  0.00%  0.00%   0 HULC ACL Tcam Me
  45           0         1          0  0.00%  0.00%  0.00%   0 HRPC EnergyWise
  46           0         1          0  0.00%  0.00%  0.00%   0 HRPC actual powe
  47           0         1          0  0.00%  0.00%  0.00%   0 HRPC lpip reques
  48           0         2          0  0.00%  0.00%  0.00%   0 HLPIP Sync Proce
  49           0         1          0  0.00%  0.00%  0.00%   0 HULC QM Tcam Mem
  50        3739     22998        162  0.00%  0.00%  0.00%   0 EEM ED ND
  51           0        24          0  0.00%  0.00%  0.00%   0 EEM ED Identity
  52          17        47        361  0.00%  0.00%  0.00%   0 EEM ED MAT
  53           0         1          0  0.00%  0.00%  0.00%   0 HRPC asic-stats
  54           0         1          0  0.00%  0.00%  0.00%   0 HRPC hsm request
  55           0         7          0  0.00%  0.00%  0.00%   0 Stack Mgr
  56         134         7      19142  0.00%  0.00%  0.00%   0 Stack Mgr Notifi
  57        5329  73160933          0  0.00%  0.00%  0.00%   0 Fifo Error Detec
  58           0         5          0  0.00%  0.00%  0.00%   0 Adjust Regions
  59         388   1368744          0  0.00%  0.00%  0.00%   0 hrpc -> response
  60          24    275169          0  0.00%  0.00%  0.00%   0 hrpc -> request
  61          49    275169          0  0.00%  0.00%  0.00%   0 hrpc <- response
  62           0         1          0  0.00%  0.00%  0.00%   0 HRPC hcomp reque
  63           0         3          0  0.00%  0.00%  0.00%   0 HULC Device Mana
  64           0         3          0  0.00%  0.00%  0.00%   0 HRPC hdm non blo
  65           0         2          0  0.00%  0.00%  0.00%   0 HRPC hdm blockin
  66           8    275153          0  0.00%  0.00%  0.00%   0 HIPC bkgrd proce
  67           8         6       1333  0.00%  0.00%  0.00%   0 Hulc Port-Securi
  68           0         1          0  0.00%  0.00%  0.00%   0 HRPC hpsecure re
  69           0         1          0  0.00%  0.00%  0.00%   0 HRPC hlfm reques
  70        1861  40920612          0  0.00%  0.00%  0.00%   0 HLFM address lea
  71          67   1368710          0  0.00%  0.00%  0.00%   0 HLFM aging proce
  72        1462  40920541          0  0.00%  0.00%  0.00%   0 HLFM address ret
  73           0         1          0  0.00%  0.00%  0.00%   0 HRPC hulc misc r
  74         811    137719          5  0.00%  0.00%  0.00%   0 HULC Tcam Memory
  75          24    458821          0  0.00%  0.00%  0.00%   0 HVLAN main bkgrd
  76           0         2          0  0.00%  0.00%  0.00%   0 HVLAN Mapped Vla
  77           0         2          0  0.00%  0.00%  0.00%   0 Vlan shutdown Pr
  78           0         3          0  0.00%  0.00%  0.00%   0 HRPC vlan reques
  79           0         1          0  0.00%  0.00%  0.00%   0 HULC VLAN REF Ba
  80           0         1          0  0.00%  0.00%  0.00%   0 HRPC isis reques
  81           0         1          0  0.00%  0.00%  0.00%   0 HRPC hfbm reques
  82           0      7656          0  0.00%  0.00%  0.00%   0 HCMP sync proces
  83           0         1          0  0.00%  0.00%  0.00%   0 HRPC ilp request
  84           0         1          0  0.00%  0.00%  0.00%   0 HULC PM Vector P
  85           0         1          0  0.00%  0.00%  0.00%   0 HPM Msg Retry Pr
  86           0     11865          0  0.00%  0.00%  0.00%   0 DHCPD Timer
  87        2926  11067366          0  0.00%  0.00%  0.00%   0 hpm main process
  88           0         4          0  0.00%  0.00%  0.00%   0 HPM Stack Sync P
  89           0         1          0  0.00%  0.00%  0.00%   0 HRPC pm request
  90        9084   1368710          6  0.00%  0.00%  0.00%   0 hpm counter proc
  91           0         1          0  0.00%  0.00%  0.00%   0 HRPC pm-counters
  92           0         1          0  0.00%  0.00%  0.00%   0 hpm vp events ca
  93           0         1          0  0.00%  0.00%  0.00%   0 HRPC hcmp reques
  94           0       658          0  0.00%  0.00%  0.00%   0 HCEF ADJ Refresh
  95           0         1          0  0.00%  0.00%  0.00%   0 HRPC hl3mm reque
  96           0         1          0  0.00%  0.00%  0.00%   0 hl3md_rpfq_thrl_
  97          67    961221          0  0.00%  0.00%  0.00%   0 hl3mm
  98          16    687261          0  0.00%  0.00%  0.00%   0 hl3mm_rp
  99           0         1          0  0.00%  0.00%  0.00%   0 HACL Queue Proce
 100           0         1          0  0.00%  0.00%  0.00%   0 HRPC acl request
 101           8        27        296  0.00%  0.00%  0.00%   0 HACL Acl Manager
 102           0         1          0  0.00%  0.00%  0.00%   0 HRPC backup inte
 103         443       184       2407  0.31%  0.40%  0.11%   1 SSH Process
 104           0         1          0  0.00%  0.00%  0.00%   0 HRPC cdp request
 105           0         1          0  0.00%  0.00%  0.00%   0 HRPC lldp reques
 106           0         1          0  0.00%  0.00%  0.00%   0 HULC CISP Proces
 107           0         1          0  0.00%  0.00%  0.00%   0 HRPC dot1x reque
 108           0         3          0  0.00%  0.00%  0.00%   0 HULC DOT1X Proce
 109           0         1          0  0.00%  0.00%  0.00%   0 HRPC system mtu
 110           0         1          0  0.00%  0.00%  0.00%   0 HRPC rep request
 111           0         3          0  0.00%  0.00%  0.00%   0 REP Helper Proc
 112           0         1          0  0.00%  0.00%  0.00%   0 SMI MSG Retry Pr
 113           0         1          0  0.00%  0.00%  0.00%   0 HRPC Smart Insta
 114           0         1          0  0.00%  0.00%  0.00%   0 HRPC sdm request
 115         870   6840245          0  0.00%  0.00%  0.00%   0 Hulc Storm Contr
 116           0         2          0  0.00%  0.00%  0.00%   0 HSTP Sync Proces
 117           0         1          0  0.00%  0.00%  0.00%   0 HRPC stp_cli req
 118           0         1          0  0.00%  0.00%  0.00%   0 HRPC stp_state_s
 119           0         2          0  0.00%  0.00%  0.00%   0 S/W Bridge Proce
 120           0         1          0  0.00%  0.00%  0.00%   0 HRPC hudld reque
 121           0         1          0  0.00%  0.00%  0.00%   0 HRPC vqpc reques
 122           0         1          0  0.00%  0.00%  0.00%   0 HRPC iec_load_ba
 123           0         1          0  0.00%  0.00%  0.00%   0 HRPC l2pt qnq rp
 124           0         1          0  0.00%  0.00%  0.00%   0 HRPC aim request
 125           0         1          0  0.00%  0.00%  0.00%   0 HRPC hled reques
 126       77860  32749110          2  0.00%  0.00%  0.00%   0 Hulc LED Process
 127         671   1008171          0  0.00%  0.00%  0.00%   0 HL3U bkgrd proce
 128           0         1          0  0.00%  0.00%  0.00%   0 HRPC hl3u reques
 129           0    314685          0  0.00%  0.00%  0.00%   0 HL3U PBR bkgrd p
 130           0     11483          0  0.00%  0.00%  0.00%   0 HL3U PBR n-h res
 131           0         1          0  0.00%  0.00%  0.00%   0 HRPC dtp request
 132           0         1          0  0.00%  0.00%  0.00%   0 HRPC show_forwar
 133           0         1          0  0.00%  0.00%  0.00%   0 HRPC snmp reques
 134           0         1          0  0.00%  0.00%  0.00%   0 HULC SNMP Proces
 135        2508    275168          9  0.00%  0.00%  0.00%   0 HQM Stack Proces
 136       60158    550317        109  0.00%  0.00%  0.00%   0 HRPC qos request
 137           0         1          0  0.00%  0.00%  0.00%   0 HRPC span reques
 138           0         1          0  0.00%  0.00%  0.00%   0 HRPC system post
 139           0         1          0  0.00%  0.00%  0.00%   0 Hulc Reload Mana
 140           0         1          0  0.00%  0.00%  0.00%   0 HRPC hrcli-event
 141          49   1338922          0  0.00%  0.00%  0.00%   0 BGP Scheduler
 142           8         2       4000  0.00%  0.00%  0.00%   0 image mgr
 143          41    458820          0  0.00%  0.00%  0.00%   0 Power RPS Proces
 144           8         3       2666  0.00%  0.00%  0.00%   0 HL2MCM
 145           0         3          0  0.00%  0.00%  0.00%   0 HL2MCM
 146         133   1368710          0  0.00%  0.00%  0.00%   0 PI MATM Aging Pr
 147           0         2          0  0.00%  0.00%  0.00%   0 REP Topology cha
 148           0         2          0  0.00%  0.00%  0.00%   0 Switch Backup In
 149           0     22956          0  0.00%  0.00%  0.00%   0 MMN bkgrd proces
 150           0         4          0  0.00%  0.00%  0.00%   0 Auth Manager
 151           0         2          0  0.00%  0.00%  0.00%   0 Dot1x Mgr Proces
 152           0         1          0  0.00%  0.00%  0.00%   0 MAB Framework
 153           0         1          0  0.00%  0.00%  0.00%   0 AUTH POLICY Fram
 154           0         1          0  0.00%  0.00%  0.00%   0 CMD HANDLER
 155           0         2          0  0.00%  0.00%  0.00%   0 802.1x switch
 156          16     22957          0  0.00%  0.00%  0.00%   0 802.1x MDA Aging
 157           0         1          0  0.00%  0.00%  0.00%   0 802.1x Webauth F
 158           0         2          0  0.00%  0.00%  0.00%   0 DTP Protocol
 159           0         1          0  0.00%  0.00%  0.00%   0 EAP Framework
 160           0         1          0  0.00%  0.00%  0.00%   0 EAP Test
 161           0         1          0  0.00%  0.00%  0.00%   0 HRPC dai request
 162       95120    320678        296  0.00%  0.00%  0.00%   0 HULC DAI Process
 163           0         1          0  0.00%  0.00%  0.00%   0 HRPC ip device t
 164           0         1          0  0.00%  0.00%  0.00%   0 HRPC ip source g
 165           0         1          0  0.00%  0.00%  0.00%   0 HULC IP Source g
 166         135   1377942          0  0.00%  0.00%  0.00%   0 UDLD
 167           0     45932          0  0.00%  0.00%  0.00%   0 Port-Security
 168           0         3          0  0.00%  0.00%  0.00%   0 IP Host Track Pr
 169           0         1          0  0.00%  0.00%  0.00%   0 Link State Group
 170           0    137723          0  0.00%  0.00%  0.00%   0 Ethchnl
 171           0         4          0  0.00%  0.00%  0.00%   0 VMATM Callback
 172           0         2          0  0.00%  0.00%  0.00%   0 CDP Forward Proc
 173         227      5848         38  0.00%  0.00%  0.00%   0 AAA Server
 174           0         1          0  0.00%  0.00%  0.00%   0 AAA ACCT Proc
 175           0         1          0  0.00%  0.00%  0.00%   0 ACCT Periodic Pr
 176           0         1          0  0.00%  0.00%  0.00%   0 AAA System Acct
 177           0         1          0  0.00%  0.00%  0.00%   0 Auth-proxy AAA B
 178           0      4594          0  0.00%  0.00%  0.00%   0 IP Admin SM Proc
 179       15553    162485         95  0.00%  0.00%  0.00%   0 CDP Protocol
 180           8     91818          0  0.00%  0.00%  0.00%   0 MDFS LC Download
 181           0         1          0  0.00%  0.00%  0.00%   0 HRPC x_setup req
 182           0         2          0  0.00%  0.00%  0.00%   0 AAA Dictionary R
 183           0     11483          0  0.00%  0.00%  0.00%   0 DHCP Snooping
 184           0         1          0  0.00%  0.00%  0.00%   0 DHCP Snooping db
 185           0         3          0  0.00%  0.00%  0.00%   0 CEF switching ba
 186       65746    165537        397  0.00%  0.01%  0.00%   0 IP Input
 187           0         1          0  0.00%  0.00%  0.00%   0 ICMP event handl
 188          83   2659472          0  0.00%  0.00%  0.00%   0 IP ARP Track
 189           0         1          0  0.00%  0.00%  0.00%   0 IPv6 ping proces
 190         957  13678194          0  0.00%  0.00%  0.00%   0 MDFS MFIB Proces
 191           0         4          0  0.00%  0.00%  0.00%   0 ADJ resolve proc
 192           0         2          0  0.00%  0.00%  0.00%   0 ADJ NSF process
 193           0     56289          0  0.00%  0.00%  0.00%   0 BGP Open
 194           0         1          0  0.00%  0.00%  0.00%   0 SMI Director DB
 195           0         1          0  0.00%  0.00%  0.00%   0 SMI CDP Update H
 196           0         1          0  0.00%  0.00%  0.00%   0 SMI Backup Proce
 197           0         2          0  0.00%  0.00%  0.00%   0 SMI IBC server p
 198           0         1          0  0.00%  0.00%  0.00%   0 SMI IBC client p
 199           0         2          0  0.00%  0.00%  0.00%   0 SMI IBC Download
 200       53416    687249         77  0.00%  0.00%  0.00%   0 Spanning Tree
 201           0     22967          0  0.00%  0.00%  0.00%   0 Spanning Tree St
 202           0         2          0  0.00%  0.00%  0.00%   0 EAPoUDP Process
 203           0         2          0  0.00%  0.00%  0.00%   0 KRB5 AAA
 204           0        99          0  0.00%  0.00%  0.00%   0 SXP CORE
 205          50     28117          1  0.00%  0.00%  0.00%   0 CEF background p
 206           0         1          0  0.00%  0.00%  0.00%   0 IP IRDP
 207           0         1          0  0.00%  0.00%  0.00%   0 CEF RF HULC Conv
 208           0         3          0  0.00%  0.00%  0.00%   0 XDR mcast
 209           0    137722          0  0.00%  0.00%  0.00%   0 IP ACL XDR LC Ba
 210           0         1          0  0.00%  0.00%  0.00%   0 IPC LC Message H
 211           0         1          0  0.00%  0.00%  0.00%   0 XDR RP Ping Back
 212           0     11483          0  0.00%  0.00%  0.00%   0 XDR RP backgroun
 213           0         1          0  0.00%  0.00%  0.00%   0 XDR RP Test Back
 214           0         3          0  0.00%  0.00%  0.00%   0 MDFS LC Process
 215        1625     60942         26  0.00%  0.00%  0.00%   0 TCP Timer
 216         399      1616        246  0.00%  0.00%  0.00%   0 TCP Protocols
 217         107   1369387          0  0.00%  0.00%  0.00%   0 Socket Timers
 218           0      4596          0  0.00%  0.00%  0.00%   0 HTTP CORE
 219           0     17226          0  0.00%  0.00%  0.00%   0 Cluster L2
 220          25    137721          0  0.00%  0.00%  0.00%   0 Cluster RARP
 221        3812    195136         19  0.00%  0.00%  0.00%   0 Cluster Base
 222           0         3          0  0.00%  0.00%  0.00%   0 RARP Input
 223           0     22961          0  0.00%  0.00%  0.00%   0 DHCPD Database
 224           0         2          0  0.00%  0.00%  0.00%   0 REP LSL Proc
 225           0         2          0  0.00%  0.00%  0.00%   0 REP BPA/EPA Proc
 226           0         2          0  0.00%  0.00%  0.00%   0 Critical Auth
 227           0         2          0  0.00%  0.00%  0.00%   0 Dot1x Supplicant
 228           0         2          0  0.00%  0.00%  0.00%   0 Dot1x Supplicant
 229           0         2          0  0.00%  0.00%  0.00%   0 Dot1x Supplicant
 230           0         1          0  0.00%  0.00%  0.00%   0 HRPC dhcp snoopi
 231           0         4          0  0.00%  0.00%  0.00%   0 HULC DHCP Snoopi
 232           0         6          0  0.00%  0.00%  0.00%   0 IGMPSN L2MCM
 233           0         1          0  0.00%  0.00%  0.00%   0 IGMPSN MRD
 234           0         1          0  0.00%  0.00%  0.00%   0 IGMPSN
 235           0         1          0  0.00%  0.00%  0.00%   0 IGMPQR
 236           8         3       2666  0.00%  0.00%  0.00%   0 L2TRACE SERVER
 237           0         6          0  0.00%  0.00%  0.00%   0 MLDSN L2MCM
 238           0         1          0  0.00%  0.00%  0.00%   0 MRD
 239           0         1          0  0.00%  0.00%  0.00%   0 MLD_SNOOP
 240           0         1          0  0.00%  0.00%  0.00%   0 HRPC hwccp reque
 241           0         1          0  0.00%  0.00%  0.00%   0 HULC_WCCP_BACKGR
 242           0         2          0  0.00%  0.00%  0.00%   0 REP Switch Helpe
 243         842     22960         36  0.00%  0.00%  0.00%   0 IP RIB Update
 244        6017   2740239          2  0.00%  0.00%  0.00%   0 DHCPD Receive
 245           0         1          0  0.00%  0.00%  0.00%   0 HRPC hl2mcm igmp
 246         932  13761838          0  0.00%  0.00%  0.00%   0 MDFS RP process
 247           0         1          0  0.00%  0.00%  0.00%   0 HRPC hl2mcm mlds
 248         343   1351077          0  0.00%  0.00%  0.00%   0 OSPF-100 Router
 249           0         1          0  0.00%  0.00%  0.00%   0 EPM MAIN PROCESS
 250        8604     52867        162  0.00%  0.01%  0.00%   0 LOCAL AAA
 251           0         2          0  0.00%  0.00%  0.00%   0 ENABLE AAA
 252           0         2          0  0.00%  0.00%  0.00%   0 LINE AAA
 253           0         2          0  0.00%  0.00%  0.00%   0 BGP I/O
 254           0         2          0  0.00%  0.00%  0.00%   0 TPLUS
 255           8        12        666  0.00%  0.00%  0.00%   0 crypto engine pr
 256          33         4       8250  0.00%  0.00%  0.00%   0 Crypto CA
 257           0         1          0  0.00%  0.00%  0.00%   0 Crypto PKI-CRL
 258           0         1          0  0.00%  0.00%  0.00%   0 Crypto SSL
 259           0         1          0  0.00%  0.00%  0.00%   0 encrypt proc
 260           0        14          0  0.00%  0.00%  0.00%   0 VTP Trap Process
 261           0         2          0  0.00%  0.00%  0.00%   0 VTPMIB EDIT BUFF
 262           0         2          0  0.00%  0.00%  0.00%   0 DHCP Security He
 263           0         1          0  0.00%  0.00%  0.00%   0 HCD Process
 264           0         1          0  0.00%  0.00%  0.00%   0 HRPC cable diagn
 265           0         2          0  0.00%  0.00%  0.00%   0 DiagCard1/-1
 266         194   3649120          0  0.00%  0.00%  0.00%   0 PM Callback
 267          25         3       8333  0.00%  0.00%  0.00%   0 VLAN Manager
 268          58     91950          0  0.00%  0.00%  0.00%   0 BGP Router
 269           0    110175          0  0.00%  0.00%  0.00%   0 dhcp snooping sw
 271         402      1600        251  0.00%  0.00%  0.00%   0 AAA SEND STOP EV
 272           0         2          0  0.00%  0.00%  0.00%   0 EEM ED Routing
 273           8        23        347  0.00%  0.00%  0.00%   0 EEM ED Syslog
 274           0         1          0  0.00%  0.00%  0.00%   0 Syslog Traps
 275           0        15          0  0.00%  0.00%  0.00%   0 Syslog
 276          42       146        287  0.00%  0.00%  0.00%   0 EEM Server
 277           0         2          0  0.00%  0.00%  0.00%   0 EEM Policy Direc
 279           0         2          0  0.00%  0.00%  0.00%   0 EEM ED CLI
 280           0         3          0  0.00%  0.00%  0.00%   0 EEM ED Counter
 281           0         3          0  0.00%  0.00%  0.00%   0 EEM ED Interface
 282           0         3          0  0.00%  0.00%  0.00%   0 EEM ED IOSWD
 283           0         3          0  0.00%  0.00%  0.00%   0 EEM ED None
 284           0         3          0  0.00%  0.00%  0.00%   0 EEM ED OIR
 285         254       767        331  0.00%  0.00%  0.00%   0 SSH Event handle
 286           0         3          0  0.00%  0.00%  0.00%   0 EEM ED SNMP
 287           0         3          0  0.00%  0.00%  0.00%   0 EEM ED SNMP Obje
 288           0         3          0  0.00%  0.00%  0.00%   0 EEM ED Ipsla
 289           0         2          0  0.00%  0.00%  0.00%   0 EEM ED SNMP Noti
 290           0     36810          0  0.00%  0.00%  0.00%   0 EEM ED Timer
 291           0         2          0  0.00%  0.00%  0.00%   0 STP FAST TRANSIT
 292           0         2          0  0.00%  0.00%  0.00%   0 CSRT RAPID TRANS
 293          16         3       5333  0.00%  0.00%  0.00%   0 EEM ED RPC
 294           0         3          0  0.00%  0.00%  0.00%   0 RBM CORE
 295           0         3          0  0.00%  0.00%  0.00%   0 RADIUS POD SERVE
 296        1686   2140245          0  0.00%  0.00%  0.00%   0 CEF: IPv4 proces
 297           0         3          0  0.00%  0.00%  0.00%   0 ADJ background
 298         264     22971         11  0.00%  0.00%  0.00%   0 IP Background
 299           0         3          0  0.00%  0.00%  0.00%   0 Dot1x Authentica
 300           0         2          0  0.00%  0.00%  0.00%   0 Dot1x Authentica
 301           0         1          0  0.00%  0.00%  0.00%   0 TCP Listener
 302      595843     33279      17904  0.00%  0.00%  0.00%   0 crypto sw pk pro
 303      192694     91817       2098  0.00%  0.00%  0.00%   0 BGP Scanner
 304           0         2          0  0.00%  0.00%  0.00%   0 SNMP Timers
 305           0         2          0  0.00%  0.00%  0.00%   0 IP SNMP
 306           0         1          0  0.00%  0.00%  0.00%   0 PDU DISPATCHER
 307           0         1          0  0.00%  0.00%  0.00%   0 SNMP ENGINE
 308           0         2          0  0.00%  0.00%  0.00%   0 IP SNMPV6
 309           0         1          0  0.00%  0.00%  0.00%   0 SNMP ConfCopyPro
 310           8         2       4000  0.00%  0.00%  0.00%   0 SNMP Traps
 311        1785  40930829          0  0.00%  0.00%  0.00%   0 RADIUS
 312          18      3407          5  0.00%  0.00%  0.00%   0 AAA Test Process
 313          75   1377947          0  0.00%  0.00%  0.00%   0 NTP
 314           0         2          0  0.00%  0.00%  0.00%   0 hulc cfg mgr mas
 315        6963        50     139260  0.00%  0.00%  0.00%   0 hulc running con
 316           0         1          0  0.00%  0.00%  0.00%   0 OSPF-100 Hello
 317           0         1          0  0.00%  0.00%  0.00%   0 CEF RP IPC Backg
 318           0         3          0  0.00%  0.00%  0.00%   0 Collection proce

```

**Help:** execute the command "show processes cpu"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show hosts summary

**Output:**
```
Default domain is test.com
Name servers are 127.0.0.2, 127.0.0.3
Local cache entries: 0
Dynamic cache entries: 0

```

**Help:** execute the command "show hosts summary"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show snmp user

**Output:**
```

User name: user_snmp1
Engine ID: 80000009030000451DEC1085
storage-type: nonvolatile        active
Authentication Protocol: SHA
Privacy Protocol: AES128
 Group-name: managerpriv

User name: user_snmp2
Engine ID: 80000009030000451DEC1085
 storage-type: nonvolatile       active access-list: 10
Authentication Protocol: SHA
Privacy Protocol: AES128
Group-name: managerpriv

User name: test-user
 Engine ID: 8000000903005E0000010000
storage-type: nonvolatile        active
 Authentication Protocol: None
Privacy Protocol: -
Group-name: test-group

```

**Help:** execute the command "show snmp user"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip arp

**Output:**
```
Protocol  Address              Age(min)       Hardware Addr     Type      Interface
Internet  172.16.233.229       -              0000.0c59.f892    ARPA      Ethernet0/0
Internet  172.16.233.218       -              0000.0c07.ac00    ARPA      Ethernet0/0
Internet  172.16.233.19        -              0000.0c63.1300    ARPA      Ethernet0/0
Internet  172.16.233.209       -              0000.0c36.6965    ARPA      Ethernet0/0
Internet  172.16.168.11        -              0000.0c63.1300    ARPA      Ethernet0/0
Internet  172.16.168.254       9              0000.0c36.6965    ARPA      Ethernet0/0 
Internet  10.0.0.0             -              aabb.cc03.8200    SRP-A


```

**Help:** execute the command "show ip arp"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip ospf database network

**Output:**
```
            OSPF Router with ID (100.1.1.1) (Process ID 1)

                Net Link States (Area 0)

  LS age: 500
  Options: (No TOS-capability, DC)
  LS Type: Network Links
  Link State ID: 192.168.2.1 (address of Designated Router)
  Advertising Router: 100.1.1.1
  LS Seq Number: 80000224
  Checksum: 0x4B27
  Length: 32
  Network Mask: /30
        Attached Router: 100.1.1.1
        Attached Router: 100.2.2.2

  LS age: 872
  Options: (No TOS-capability, DC)
  LS Type: Network Links
  Link State ID: 192.168.3.2 (address of Designated Router)
  Advertising Router: 100.4.4.4
  LS Seq Number: 80000224
  Checksum: 0x4816
  Length: 32
  Network Mask: /30
        Attached Router: 100.4.4.4
        Attached Router: 100.2.2.2

  LS age: 351
  Options: (No TOS-capability, DC)
  LS Type: Network Links
  Link State ID: 192.168.4.2 (address of Designated Router)
  Advertising Router: 100.4.4.4
  LS Seq Number: 80000226
  Checksum: 0x60F7
  Length: 32
  Network Mask: /30
        Attached Router: 100.4.4.4
        Attached Router: 100.3.3.3

```

**Help:** execute the command "show ip ospf database network"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show access-list

**Output:**
```
Standard IP access list 1
10 permit 4.5.6.0 log
20 permit any
Standard IP access list 2
10 permit 0.0.0.0, wildcard bits 255.255.255.252 log (4556 matches)
20 permit any (11665 matches)

```

**Help:** execute the command "show access-list"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip device tracking all

**Output:**
```
Global IP Device Tracking for clients = Enabled
Global IP Device Tracking Probe Count = 3
Global IP Device Tracking Probe Interval = 30
Global IP Device Tracking Probe Delay Interval = 0
-----------------------------------------------------------------------------------------------
  IP Address    MAC Address   Vlan  Interface           Probe-Timeout      State    Source
-----------------------------------------------------------------------------------------------
192.168.1.104   8c12.9011.00e2 1    GigabitEthernet1/0/9   30              ACTIVE   ARP
192.168.1.108   0065.2da2.5d6e 1    GigabitEthernet1/0/1   30              ACTIVE   ARP
192.168.1.110   000c.29ed.e090 1    GigabitEthernet1/0/1   30              ACTIVE   ARP

Total number interfaces enabled: 32
Enabled interfaces:
  Vl1, Vl3, Vl42, Fa0, Gi1/0/1, Gi1/0/2, Gi1/0/3,
  Gi1/0/4, Gi1/0/5, Gi1/0/6, Gi1/0/7, Gi1/0/8, Gi1/0/9, Gi1/0/10,
  Gi1/0/11, Gi1/0/12, Gi1/0/13, Gi1/0/14, Gi1/0/15, Gi1/0/16, Gi1/0/17,
  Gi1/0/18, Gi1/0/19, Gi1/0/20, Gi1/0/21, Gi1/0/22, Gi1/0/23, Gi1/0/24,
  Gi1/0/25, Gi1/0/26, Gi1/0/27, Gi1/0/28

```

**Help:** execute the command "show ip device tracking all"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show interfaces switchport

**Output:**
```
Name: Te5/0/1
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: Off
Access Mode VLAN: 1 (default)
 Trunking Native Mode VLAN: 1 (default)
Administrative Native VLAN tagging: disabled
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk Native VLAN tagging: enabled
 Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk associations: none
 Administrative private-vlan trunk mappings: none
Operational private-vlan: none
Trunking VLANs Enabled: 1,12,15,31-36,40-42,80,85,101,201,240,410,420,602,604,
     900,910,920,930,940
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
 Capture VLANs Allowed: ALL

Protected: false
Unknown unicast blocked: disabled
 Unknown multicast blocked: disabled
Vepa Enabled: false
Appliance trust: none
 
Name: Te5/0/2
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: Off
Access Mode VLAN: 1 (default)
 Trunking Native Mode VLAN: 1 (default)
Administrative Native VLAN tagging: disabled
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk Native VLAN tagging: enabled
 Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk associations: none
 Administrative private-vlan trunk mappings: none
Operational private-vlan: none
Trunking VLANs Enabled: 1,12,15,31-36,40-42,80,85,101,201,240,410,420,602,604,
     900,910,920,930,940
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
 Capture VLANs Allowed: ALL

Protected: false
Unknown unicast blocked: disabled
 Unknown multicast blocked: disabled
Vepa Enabled: false
Appliance trust: none

```

**Help:** execute the command "show interfaces switchport"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show vrrp brief

**Output:**
```
  Interface          Grp  A-F Pri  Time Own Pre State   Master addr/Group addr
  Gi0/0                1 IPv4 110     0  N   Y  MASTER  10.0.1.2(local) 10.0.1.1
  Gi0/0                6 IPv6 110     0  N   Y  MASTER  FE80::1:A(local) FE80::1:1
  Gi0/0.4010           1 IPv4 110  3570  N   Y  BACKUP  10.254.1.3 10.254.1.1
  Gi0/0.4010           6 IPv6 110  3570  N   Y  BACKUP  FE80::4010:3 FE80::4010:1
  Gi0/0.2600           1 IPv4  90  3648  N   Y  BACKUP  172.26.0.3 172.26.0.1


```

**Help:** execute the command "show vrrp brief"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show clock

**Output:**
```
*18:57:38.347 UTC Mon Oct 19 2015

```

**Help:** execute the command "show clock"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ipv6 interface brief

**Output:**
```
TenGigabitEthernet1/1  [up/up]
    FE80::333:3333:3333:3333
    2A01:3333:3333::5
TenGigabitEthernet2/1  [up/up]
    FE80::333:3333:3333:3333
    2A01:3333:3333::9
TenGigabitEthernet2/2  [up/up]
    unassigned
TenGigabitEthernet2/3  [up/up]
    unassigned
TenGigabitEthernet2/4  [up/up]
    unassigned
TenGigabitEthernet2/5  [up/up]
    unassigned
TenGigabitEthernet2/6  [up/down]
    unassigned
TenGigabitEthernet3/9  [up/up]
    unassigned
TenGigabitEthernet3/10 [administratively down/down]
    unassigned
TenGigabitEthernet3/11 [administratively down/down]
    unassigned
TenGigabitEthernet3/12 [down/down]
    unassigned
TenGigabitEthernet3/13 [administratively down/down]
    unassigned
TenGigabitEthernet3/14 [administratively down/down]
    unassigned
TenGigabitEthernet3/15 [administratively down/down]
    unassigned
TenGigabitEthernet3/16 [up/up]
    unassigned
TenGigabitEthernet4/1  [up/down]
    unassigned
TenGigabitEthernet4/2  [up/up]
    unassigned
TenGigabitEthernet4/3  [up/up]
    unassigned
TenGigabitEthernet4/4  [down/down]
    unassigned
TenGigabitEthernet4/5  [administratively down/down]
    unassigned
TenGigabitEthernet4/6  [administratively down/down]
    unassigned
TenGigabitEthernet4/7  [up/up]
    unassigned
TenGigabitEthernet4/8  [up/up]
    unassigned
TenGigabitEthernet4/9  [up/up]
    unassigned
TenGigabitEthernet4/10 [up/up]
    unassigned
TenGigabitEthernet4/11 [administratively down/down]
    unassigned
 TenGigabitEthernet4/12 [administratively down/down]
    unassigned
TenGigabitEthernet4/13 [administratively down/down]
    unassigned
TenGigabitEthernet4/14 [administratively down/down]
    unassigned
TenGigabitEthernet4/15 [administratively down/down]
    unassigned
TenGigabitEthernet4/16 [up/up]
    unassigned
GigabitEthernet5/1     [administratively down/down]
    unassigned
GigabitEthernet5/2     [administratively down/down]
    unassigned
GigabitEthernet5/3     [administratively down/down]
    unassigned
TenGigabitEthernet5/4  [administratively down/down]
    unassigned
TenGigabitEthernet5/5  [administratively down/down]
    unassigned
GigabitEthernet6/1     [administratively down/down]
    unassigned
GigabitEthernet6/2     [administratively down/down]
    unassigned
GigabitEthernet6/3     [administratively down/down]
    unassigned
TenGigabitEthernet6/4  [administratively down/down]
    unassigned
TenGigabitEthernet6/5  [administratively down/down]
    unassigned
GigabitEthernet1/1     [up/up]
    unassigned
GigabitEthernet1/16    [up/up]
    FE80::333:3333:3333:3333
    2A01:3333:3333::9A
GigabitEthernet1/17    [up/up]
    FE80::333:3333:3333:3333
    2A01:3333:3333::9E
GigabitEthernet1/18    [up/up]
    FE80::333:3333:3333:3333
    2A01:3333:3333::A2
GigabitEthernet1/48    [administratively down/down]
    unassigned
Loopback0              [up/up]
    FE80::333:3333:3333:3333
    2A01:5A20:1FFF::13
Port-channel1          [up/up]
    unassigned
Port-channel2          [up/up]
    unassigned
Port-channel3          [up/up]
    unassigned
Port-channel4          [up/up]
    unassigned
Port-channel5          [up/up]
    unassigned
Port-channel6          [up/up]
    unassigned
Port-channel7          [up/up]
    unassigned
Port-channel8          [up/up]
    unassigned
Port-channel9          [up/up]
    unassigned
Port-channel10         [up/up]
    unassigned
Port-channel11         [up/up]
    unassigned
Vlan1                  [administratively down/down]
    unassigned
Vlan76                 [up/up]
    FE80::333:3333:3333:3333
    2A01:3333:3333:33::1
    2A01:3333:3333:33::2
Vlan77                 [up/up]
    unassigned
Vlan100                [up/up]
    FE80::333:3333:3333:3333
    2A01:3333:3336:100::1
    2A01:3333:3336:100::2
Vlan762                [up/up]
    FE80::333:3333:3333:3333
    2A01:3333:3336:101::1
    2A01:3333:3336:101::2
Vlan763                [up/up]
    FE80::333:3333:3333:3333
    2A01:3333:3336:102::1
    2A01:3333:3336:102::2
Vlan764                [up/up]
    FE80::333:3333:3333:3333
    2A01:3333:3336:103::1
    2A01:3333:3336:103::2
Vlan765                [up/up]
    FE80::333:3333:3333:3333
    2A01:3333:3336:104::1
    2A01:3333:3336:104::2
Vlan767                [up/up]
    FE80::333:3333:3333:3333
    2A01:3333:3336:110::1
    2A01:3333:3336:110::2
Vlan768                [up/up]
    FE80::333:3333:3333:3333
    2A01:3333:3336:111::1
    2A01:3333:3336:111::2
Vlan769                [up/up]
    FE80::333:3333:3333:3333
    2A01:3333:3336:112::1
    2A01:3333:3336:112::2
Vlan770                [up/up]
    FE80::333:3333:3333:3333
    2A01:3333:3336:113::1
    2A01:3333:3336:113::2
Vlan771                [up/up]
    unassigned
Vlan772                [up/up]
    unassigned
Vlan773                [administratively down/down]
    unassigned
Vlan774                [administratively down/down]
    unassigned
Vlan775                [up/up]
    FE80::333:3333:3333:3333
    2A01:3333:3336:220::1
    2A01:3333:3336:220::2
Vlan776                [up/up]
    unassigned
Vlan777                [up/up]
    FE80::333:3333:3333:3333
    2A01:3333:3336:225::1
    2A01:3333:3336:225::2
Vlan2300               [administratively down/down]
    unassigned

```

**Help:** execute the command "show ipv6 interface brief"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show port-security interface interface

**Output:**
```
Port Security              : Disabled
Port Status                : Secure-down
 Violation Mode             : Shutdown
Aging Time                 : 1440 mins
 Aging Type                 : Absolute
SecureStatic Address Aging : Disabled
 Maximum MAC Addresses      : 1
Total MAC Addresses        : 0
Configured MAC Addresses   : 0
Sticky MAC Addresses       : 0
Last Source Address:Vlan   : 0000.0000.0000:0
Security Violation Count   : 0

```

**Help:** execute the command "show port-security interface interface"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show ip access-lists

**Output:**
```
Standard IP access list 99
    10 permit 172.16.191.199
    20 deny   any log
    30 permit 10.0.10.0, wildcard bits 0.255.0.255 (20 matches)
 Standard IP access list stdacl
    10 permit 10.1.1.1
Extended IP access list test
Extended IP access list 101
    10 permit tcp any host 10.1.1.1 eq www
    20 permit tcp any host 10.1.1.1 eq 443 log
    30 permit ahp any any log-input
    40 permit ahp any any log-input time-range test (active)
    50 permit ip any host 10.1.10.11 log time-range test2 (inactive)
    60 permit udp any range 16384 32767 10.1.1.0 0.0.0.255 range 16384 32767
    70 permit udp any eq snmp bootpc 10.1.0.0 0.0.0.255
    80 permit tcp 10.0.0.0 0.255.255.255 eq telnet ssh http 8080 host 10.1.0.0 neq telnet ssh
    90 permit tcp any any match-all +ack -fin log
    100 permit tcp host 10.1.1.1 any established
    110 permit tcp any 10.1.1.0 0.0.255.255 established psh
Extended IP access list sample
    10 permit tcp host 10.10.37.18 host 10.10.37.17 eq bgp
    20 permit tcp host 10.10.37.18 eq bgp host 10.10.37.17
    30 permit icmp 10.10.37.16 0.0.0.3 host 10.10.37.17
    40 permit icmp 10.10.37.24 0.0.0.7 host 10.10.37.17
    50 permit icmp 10.10.37.16 0.0.0.3 host 10.10.5.20
    60 permit icmp 10.10.37.24 0.0.0.7 host 10.10.5.20
    70 permit icmp 10.10.37.16 0.0.0.3 host 10.10.6.144
    80 permit icmp 10.10.37.24 0.0.0.7 host 10.10.6.144
    90 permit icmp 10.10.37.16 0.0.0.3 host 10.10.6.146
    100 permit icmp 10.10.37.24 0.0.0.7 host 10.10.6.146
    110 permit icmp 10.10.37.16 0.0.0.3 host 10.10.6.148
    120 permit icmp 10.10.37.24 0.0.0.7 host 10.10.6.148
    130 permit icmp 10.10.37.16 0.0.0.3 host 10.10.6.152
    140 permit icmp 10.10.37.24 0.0.0.7 host 10.10.6.152
    150 permit icmp 10.10.37.16 0.0.0.3 host 10.10.8.26
    160 permit icmp 10.10.37.24 0.0.0.7 host 10.10.8.26
    170 permit icmp 10.10.37.16 0.0.0.3 host 10.10.8.152
    180 permit icmp 10.10.37.24 0.0.0.7 host 10.10.8.152
    190 permit icmp 10.10.37.16 0.0.0.3 10.3.140.0 0.0.0.127
    200 permit icmp 10.10.37.24 0.0.0.7 10.3.140.0 0.0.0.127
    210 permit icmp 10.10.37.16 0.0.0.3 host 10.3.139.248
    220 permit icmp 10.10.37.24 0.0.0.7 host 10.3.139.248
    230 permit icmp 10.10.37.16 0.0.0.3 10.3.139.128 0.0.0.7
    240 permit icmp 10.10.37.24 0.0.0.7 10.3.139.128 0.0.0.7
    250 permit tcp 10.10.37.24 0.0.0.7 host 10.10.5.20 eq 4000
    260 permit tcp 10.10.37.24 0.0.0.7 host 10.10.5.20 eq 4010
    270 permit tcp 10.10.37.24 0.0.0.7 host 10.10.5.20 eq 4020
    280 permit tcp 10.10.37.24 0.0.0.7 host 10.10.5.20 eq 4080
    290 permit tcp 10.10.37.24 0.0.0.7 host 10.10.5.20 eq 4300
    300 permit tcp 10.10.37.24 0.0.0.7 host 10.10.5.20 eq 4310
    310 permit tcp 10.10.37.24 0.0.0.7 host 10.10.5.20 eq 4320
    320 permit tcp 10.10.37.24 0.0.0.7 host 10.10.5.20 eq 4380
    330 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.144 eq 4000
    340 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.144 eq 4010
    350 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.144 eq 4020
    360 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.144 eq 4300
    370 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.144 eq 4310
    380 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.144 eq 4320
    390 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.146 eq 4000
    400 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.146 eq 4010
    410 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.146 eq 4020
    420 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.146 eq 4300
    430 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.146 eq 4310
    440 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.146 eq 4320
    450 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.148 eq 4050
    460 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.148 eq 4060
    470 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.148 eq 4350
    480 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.148 eq 4360
    490 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.152 eq 4000
    500 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.152 eq 4010
    510 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.152 eq 4020
    520 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.152 eq 4080
    530 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.152 eq 4300
    540 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.152 eq 4310
    550 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.152 eq 4320
    560 permit tcp 10.10.37.24 0.0.0.7 host 10.10.6.152 eq 4380
    570 permit tcp 10.10.37.24 0.0.0.7 host 10.10.8.26 eq 4001
    580 permit tcp 10.10.37.24 0.0.0.7 host 10.10.8.152 eq 4001
    590 permit tcp 10.10.37.24 0.0.0.7 10.3.140.64 0.0.0.31 eq 9815 log time-range test (active)
    600 permit tcp 10.10.37.24 0.0.0.7 10.3.140.64 0.0.0.31 range 9821 9823
    610 permit tcp 10.10.37.24 0.0.0.7 10.3.140.96 0.0.0.31 range 7400 7407
    620 permit udp 10.10.37.16 0.0.0.3 host 10.3.139.133 range 13001 13191
    630 permit udp 10.10.37.24 0.0.0.7 host 10.3.139.133 range 13001 13191
    640 permit tcp 10.10.37.16 0.0.0.3 host 10.3.139.134 range 13001 13191
    650 permit tcp 10.10.37.24 0.0.0.7 host 10.3.139.134 range 13001 13191
    660 permit pim host 10.10.37.18 host 224.0.0.1 time-range test2 (inactive)
Extended IP access list test2

```

**Help:** execute the command "show ip access-lists"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show lldp neighbors

**Output:**
```
Capability codes:
    (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
    (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other
 
Device ID           Local Intf     Hold-time  Capability      Port ID
S2                  Fa0/13         120        B               Gi0/13
Cisco-switch-1      Gi1/0/7        120                        Gi0/1
Juniper-switch1     Gi2/0/1        120        B,R             666
Juniper-switch1     Gi1/0/1        120        B,R             531
Polycom VVX 500     Gi1/0/2        120        T               0004.f2d1.2222

Total entries displayed: 5

```

**Help:** execute the command "show lldp neighbors"

**Prompt:**
- cisco_ios>
- cisco_ios#

### show version

**Output:**
```
Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M), Version 15.8(3)M2, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
 Copyright (c) 1986-2019 by Cisco Systems, Inc.
Compiled Thu 28-Mar-19 14:06 by prod_rel_team


ROM: Bootstrap program is IOSv

rtr-01 uptime is 1 week, 3 days, 16 hours, 11 minutes
System returned to ROM by reload
System image file is "flash0:/vios-adventerprisek9-m"
Last reload reason: Unknown reason
 


This product contains cryptographic features and is subject to United
 States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.
 
A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.
 
Cisco IOSv (revision 1.0) with  with 460137K/62464K bytes of memory.
Processor board ID 991UCMIHG4UAJ1J010CQG
4 Gigabit Ethernet interfaces
DRAM configuration is 72 bits wide with parity disabled.
256K bytes of non-volatile configuration memory.
2097152K bytes of ATA System CompactFlash 0 (Read/Write)
0K bytes of ATA CompactFlash 1 (Read/Write)
11217K bytes of ATA CompactFlash 2 (Read/Write)
 0K bytes of ATA CompactFlash 3 (Read/Write)



Configuration register is 0x0
```

**Help:** execute the command "show version"

**Prompt:**
- cisco_ios>
- cisco_ios#

### terminal length 0

**Output:** None

**Help:** Execute the command terminal length 0. This automatically generated. Feel free to change it!

**Prompt:**
- cisco_ios>
- cisco_ios#

### terminal width 511

**Output:** None

**Help:** Execute the command terminal width 511. This automatically generated. Feel free to change it!

**Prompt:**
- cisco_ios>
- cisco_ios#

