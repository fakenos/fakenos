# cisco_asa


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
- cisco_asa>

### login

**Output:** None

**Help:** It enters the terminal

**Prompt:**
- cisco_asa>

### show running-config all crypto map

**Output:**
```
crypto map WAN1_CMAP 10 match address CMAP_RU16
crypto map WAN1_CMAP 10 set connection-type bidirectional
crypto map WAN1_CMAP 10 set peer 1.1.1.1
 crypto map WAN1_CMAP 10 set ikev1 phase1-mode main
crypto map WAN1_CMAP 10 set ikev1 transform-set ESP-AES-256-SHA ESP-AES-192-SHA
crypto map WAN1_CMAP 10 set ikev2 mode tunnel
no crypto map WAN1_CMAP 10 set tfc-packets
crypto map WAN1_CMAP 20 match address CMAP_RU11
crypto map WAN1_CMAP 20 set connection-type bidirectional
crypto map WAN1_CMAP 20 set peer 2.2.2.2
crypto map WAN1_CMAP 20 set ikev1 phase1-mode main
crypto map WAN1_CMAP 20 set ikev1 transform-set ESP-AES-256-SHA ESP-AES-192-SHA
crypto map WAN1_CMAP 20 set ikev2 mode tunnel
 no crypto map WAN1_CMAP 20 set tfc-packets
crypto map WAN1_CMAP 30 match address CMAP_RU12
crypto map WAN1_CMAP 30 set connection-type bidirectional
crypto map WAN1_CMAP 30 set peer 3.3.3.3
crypto map WAN1_CMAP 30 set ikev1 phase1-mode main
crypto map WAN1_CMAP 30 set ikev1 transform-set ESP-AES-256-SHA ESP-AES-192-SHA
 crypto map WAN1_CMAP 30 set ikev2 mode tunnel
no crypto map WAN1_CMAP 30 set tfc-packets
crypto map WAN1_CMAP 40 match address CMAP_RU17
crypto map WAN1_CMAP 40 set connection-type bidirectional
crypto map WAN1_CMAP 40 set peer 4.4.4.4
 crypto map WAN1_CMAP 40 set ikev1 phase1-mode main
crypto map WAN1_CMAP 40 set ikev1 transform-set ESP-AES-256-SHA ESP-AES-192-SHA
crypto map WAN1_CMAP 40 set ikev2 mode tunnel
no crypto map WAN1_CMAP 40 set tfc-packets
crypto map WAN1_CMAP 100 match address CMAP_FR_TEST_VPN
crypto map WAN1_CMAP 100 set pfs group5
crypto map WAN1_CMAP 100 set connection-type bidirectional
crypto map WAN1_CMAP 100 set peer 185.108.69.37
crypto map WAN1_CMAP 100 set ikev1 phase1-mode main
crypto map WAN1_CMAP 100 set ikev1 transform-set DES-MD5
 crypto map WAN1_CMAP 100 set ikev2 mode tunnel
crypto map WAN1_CMAP 100 set security-association lifetime seconds 3600
no crypto map WAN1_CMAP 100 set tfc-packets
crypto map WAN1_CMAP 65535 ipsec-isakmp dynamic SYSTEM_DEFAULT_CRYPTO_MAP
 crypto map WAN1_CMAP interface WAN1
crypto map S2S_CMAP 10 match address CMAP_RU17
 crypto map S2S_CMAP 10 set connection-type bidirectional
crypto map S2S_CMAP 10 set peer 10.0.10.1
crypto map S2S_CMAP 10 set ikev1 phase1-mode main
crypto map S2S_CMAP 10 set ikev1 transform-set ESP-AES-256-SHA ESP-AES-192-SHA
crypto map S2S_CMAP 10 set ikev2 mode tunnel
no crypto map S2S_CMAP 10 set tfc-packets
 crypto map S2S_CMAP 20 match address CMAP_RU12
crypto map S2S_CMAP 20 set connection-type bidirectional
crypto map S2S_CMAP 20 set peer 10.0.20.1
crypto map S2S_CMAP 20 set ikev1 phase1-mode main
crypto map S2S_CMAP 20 set ikev1 transform-set ESP-AES-256-SHA ESP-AES-192-SHA
crypto map S2S_CMAP 20 set ikev2 mode tunnel
 no crypto map S2S_CMAP 20 set tfc-packets
crypto map S2S_CMAP 30 match address CMAP_RU11
crypto map S2S_CMAP 30 set connection-type bidirectional
crypto map S2S_CMAP 30 set peer 10.0.30.1
crypto map S2S_CMAP 30 set ikev1 phase1-mode main
crypto map S2S_CMAP 30 set ikev1 transform-set ESP-AES-256-SHA ESP-AES-192-SHA
 crypto map S2S_CMAP 30 set ikev2 mode tunnel
no crypto map S2S_CMAP 30 set tfc-packets
crypto map S2S_CMAP 40 match address CMAP_RU16
crypto map S2S_CMAP 40 set connection-type bidirectional
crypto map S2S_CMAP 40 set peer 10.0.40.1
 crypto map S2S_CMAP 40 set ikev1 phase1-mode main
crypto map S2S_CMAP 40 set ikev1 transform-set ESP-AES-256-SHA ESP-AES-192-SHA
crypto map S2S_CMAP 40 set ikev2 mode tunnel
no crypto map S2S_CMAP 40 set tfc-packets
crypto map S2S_CMAP interface S2SVPN
```

**Help:** execute the command "show running-config all crypto map"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show interface ip brief

**Output:**
```
Interface                  IP-Address      OK? Method Status                Protocol
Virtual0                   127.1.0.1       YES unset  up                    up  
GigabitEthernet1/1         192.168.1.253   YES CONFIG up                    up  
GigabitEthernet1/2         unassigned      YES unset  up                    up  
GigabitEthernet1/3         unassigned      YES unset  up                    up  
GigabitEthernet1/4         unassigned      YES unset  administratively down down
GigabitEthernet1/5         unassigned      YES unset  administratively down down
GigabitEthernet1/6         unassigned      YES unset  administratively down down
GigabitEthernet1/7         unassigned      YES unset  administratively down down
GigabitEthernet1/8         unassigned      YES unset  administratively down down
Internal-Control1/1        unassigned      YES unset  up                    down
Internal-Data1/1           unassigned      YES unset  up                    up  
Internal-Data1/2           unassigned      YES unset  down                  down
Internal-Data1/3           unassigned      YES unset  up                    up  
Internal-Data1/4           169.254.1.1     YES unset  up                    up  
Management1/1              10.10.12.2      YES CONFIG up                    up  
Port-channel1              unassigned      YES unset  up                    up  
Port-channel1.144          10.10.14.1      YES CONFIG up                    up  
Port-channel1.3101         10.10.54.2      YES CONFIG up                    up  

```

**Help:** execute the command "show interface ip brief"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show module

**Output:**
```

Mod  Card Type                                    Model              Serial No.
---- -------------------------------------------- ------------------ -----------
   1 ASA 5506-X with SW, 8GE Data, 1GE Mgmt, AC   ASA5506            JAD22466666
 sfr FirePOWER Services Software Module           ASA5506            JAD22666666

Mod  MAC Address Range                 Hw Version   Fw Version   Sw Version
---- --------------------------------- ------------ ------------ ---------------
   1 70b3.17be.aaaa to 70b3.17be.bbbb  2.2          1.1.13       9.0(2)
 sfr 70b3.17be.cccc to 70b3.17be.dddd  N/A          N/A          6.5.2-81

Mod  SSM Application Name           Status           SSM Application Version
---- ------------------------------ ---------------- --------------------------
 sfr ASA FirePOWER                  Up               6.5.2-81

Mod  Status             Data Plane Status     Compatibility
 ---- ------------------ --------------------- -------------
   1 Up Sys             Not Applicable
 sfr Up                 Up
```

**Help:** execute the command "show module"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show failover

**Output:**
```
Failover On
Failover unit Primary
Failover LAN Interface: fover Vlan150 (up)
Unit Poll frequency 1 seconds, holdtime 15 seconds
Interface Poll frequency 5 seconds, holdtime 25 seconds
Interface Policy 1
Monitored Interfaces 4 of 250 maximum
Version: Ours 7.2(0)55, Mate 7.2(0)55
Last Failover at: 19:59:58 PST Apr 6 2006
 
This host: Primary - Active
Active time: 34 (sec)
slot 0: ASA5505 hw/sw rev (1.0/7.2(0)55) status (Up Sys)
Interface inside (192.168.1.1): Normal
Interface outside (192.168.2.201): Normal
Interface dmz (172.16.0.1): Normal
Interface test (172.23.62.138): Normal
slot 1: empty
 
Other host: Secondary - Standby Ready
Active time: 0 (sec)
slot 0: ASA5505 hw/sw rev (1.0/7.2(0)55) status (Up Sys)
Interface inside (192.168.1.2): Normal
Interface outside (192.168.2.211): Normal
Interface dmz (172.16.0.2): Normal
Interface test (172.23.62.137): Normal
slot 1: empty

```

**Help:** execute the command "show failover"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show asp table vpn-context detail

**Output:**
```
VPN CTX  = 0x01177414

Peer IP  = 10.10.200.25
Pointer  = 0xCC11B670
State    = UP+DIP
Flags    = DECR+ESP+NATT
SA   = 0x0DA8FA2F
SPI  = 0x4F456306
Group    = 1
Pkts     = 8092
Bad Pkts = 1
Bad SPI  = 1
Spoof    = 1
Bad Crypto = 1
Rekey Pkt  = 3
Rekey Call = 3
VPN Filter = <none>

VPN CTX  = 0x0116C1F4

Peer IP  = 10.10.200.25
Pointer  = 0xCC11A688
State    = UP+DIP
Flags    = ENCR+ESP+NATT
SA   = 0x0DAB083D
SPI  = 0xDB16183C
Group    = 1
Pkts     = 7972
Bad Pkts = 1
Bad SPI  = 1
Spoof    = 1
Bad Crypto = 1
Rekey Pkt  = 3
Rekey Call = 3
VPN Filter = <none>

VPN CTX  = 0x01155524
 
Peer IP  = 10.11.200.23
Pointer  = 0xCC05C8F0
State    = UP
Flags    = DECR+ESP+PRESERVE
SA   = 0x0DACF9C5
SPI  = 0x0F51782D
Group    = 1
Pkts     = 27257
Bad Pkts = 0
Bad SPI  = 0
Spoof    = 0
Bad Crypto = 0
Rekey Pkt  = 5
Rekey Call = 5
VPN Filter = VPN-ACL-1

VPN CTX  = 0x0114BD44

 Peer IP  = 10.11.200.23
Pointer  = 0xC848E250
State    = UP
Flags    = ENCR+ESP+PRESERVE
SA   = 0x0DAE8F1B
SPI  = 0x4ACE6F27
Group    = 1
Pkts     = 24194
Bad Pkts = 0
Bad SPI  = 0
Spoof    = 0
Bad Crypto = 0
Rekey Pkt  = 5
Rekey Call = 5
VPN Filter = VPN-ACL-1

VPN CTX  = 0x0114044C

Peer IP  = 10.12.200.22
Pointer  = 0xCC11C010
State    = UP
Flags    = DECR+ESP+NATT
SA   = 0x0DA50609
SPI  = 0xDEFE481D
Group    = 1
Pkts     = 2495
Bad Pkts = 0
Bad SPI  = 0
Spoof    = 0
Bad Crypto = 0
Rekey Pkt  = 5
Rekey Call = 5
VPN Filter = <none>

```

**Help:** execute the command "show asp table vpn-context detail"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show running-config crypto ikev1

**Output:**
```
crypto ikev1 policy 5
 authentication pre-share
 encryption aes-256
 hash sha
 group 5
 lifetime 86400
crypto ikev1 policy 10
 authentication pre-share
 encryption 3des
 hash md5
 group 2
 lifetime 86400
crypto ikev1 policy 15
 authentication pre-share
 encryption 3des
 hash sha
 group 2
 lifetime 86400
crypto ikev1 policy 20
 authentication pre-share
 encryption 3des
 hash md5
 group 5
 lifetime 86400
crypto ikev1 policy 25
 authentication pre-share
 encryption 3des
 hash sha
 group 5
 lifetime 86400
crypto ikev1 policy 30
 authentication pre-share
 encryption aes-192
 hash md5
 group 2
 lifetime 86400
crypto ikev1 policy 35
 authentication pre-share
 encryption aes-192
 hash sha
 group 2
 lifetime 86400
crypto ikev1 policy 40
 authentication pre-share
 encryption aes-192
 hash md5
 group 5
 lifetime 86400
crypto ikev1 policy 45
 authentication pre-share
 encryption aes-192
 hash sha
 group 5
 lifetime 86400
crypto ikev1 policy 50
 authentication pre-share
 encryption aes-256
 hash md5
 group 2
 lifetime 86400
crypto ikev1 policy 55
 authentication pre-share
 encryption aes-256
 hash sha
 group 2
 lifetime 86400
crypto ikev1 policy 60
 authentication pre-share
 encryption aes-256
 hash md5
 group 5      
 lifetime 86400

```

**Help:** execute the command "show running-config crypto ikev1"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show crypto ikev1 sa detail

**Output:**
```
IKE Peer      Type  Dir   Rky  State      Encrypt Hash  Auth    Lifetime
 1 209.165.200.225 User  Resp  No   AM_Active  3des    SHA   preshrd 86400
 IKE Peer      Type  Dir   Rky  State      Encrypt Hash  Auth    Lifetime
2 209.165.200.226 User  Resp  No   AM_ACTIVE  3des    SHA   preshrd 86400
IKE Peer      Type  Dir   Rky  State      Encrypt Hash  Auth    Lifetime
3 209.165.200.227 User  Resp  No   AM_ACTIVE  3des    SHA   preshrd 86400
IKE Peer      Type  Dir   Rky  State      Encrypt Hash  Auth    Lifetime
4 209.165.200.228 User  Resp  No   AM_ACTIVE  3des    SHA   preshrd 86400
```

**Help:** execute the command "show crypto ikev1 sa detail"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show port-channel summary

**Output:**
```
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        U - in use      N - not in use, no aggregation/nameif
        M - not in use, no aggregation due to minimum links not met
        w - waiting to be aggregated
Number of channel-groups in use: 3
Group  Port-channel  Protocol  Span-cluster  Ports
------+-------------+---------+------------+------------------------------------
1      Po1(U)            LACP          No     Gi0/0(P)   Gi0/1(P)
2      Po2(U)            LACP          No     Gi0/2(P)   Gi0/3(P)

```

**Help:** execute the command "show port-channel summary"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show arp

**Output:**
```
        outside 1.2.3.4 444e.6df8.b97e 15
        DMZ 192.168.10.9 0013.2401.01a3 5054
        DMZ1 172.19.0.5 000c.2911.ebc4 711
        DMZ2 172.19.1.11 000c.293b.d502 8744
        INSIDE 10.0.0.1 2401.c75e.3acb 12074

```

**Help:** execute the command "show arp"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show license all

**Output:**
```
Smart Licensing Status
======================

Smart Licensing is ENABLED

Registration:
  Status: REGISTERED
  Smart Account: COMPANY LLC
  Virtual Account: DEFAULT
  Export-Controlled Functionality: ALLOWED
  Initial Registration: SUCCEEDED on Feb 10 2023 11:27:20 UTC
  Last Renewal Attempt: None
  Next Renewal Attempt: Aug 18 2023 13:40:54 UTC
  Registration Expires: Feb 29 2024 13:21:17 UTC

License Authorization:
  Status: AUTHORIZED on Feb 10 2023 08:20:02 UTC
  Last Communication Attempt: SUCCEEDED on Feb 11 2023 17:28:02 UTC
  Next Communication Attempt: Mar 10 2023 09:43:06 UTC
  Communication Deadline: May 09 2023 18:22:16 UTC

Export Authorization Key:
  Features Authorized:
    <none>

Utility:
  Status: DISABLED

 Data Privacy:
  Sending Hostname: yes
    Callhome hostname privacy: DISABLED
    Smart Licensing hostname privacy: DISABLED
  Version privacy: DISABLED

Transport:
  Type: Callhome

License Usage
==============

ASAv50 Standard - 10G (ASAv-STD-10G):
  Description: ASAv50 Standard - 10G
  Count: 1
  Version: 1.0
  Status: AUTHORIZED
  Export status: NOT RESTRICTED

Product Information
 ===================
UDI: PID:ASAv,SN:9X61HSQEA6Z

Agent Version
=============
 Smart Agent for Licensing: 4.9.3_rel/34

Reservation Info
================
 License reservation: DISABLED

```

**Help:** execute the command "show license all"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show interface detail

**Output:**
```
Interface Virtual0 "_internal_loopback", is up, line protocol is up
  Hardware is Virtual   MAC address 0000.0000.0000, MTU 1500
        IP address 127.1.0.1, subnet mask 255.255.0.0
  Traffic Statistics for "_internal_loopback":
        1 packets input, 28 bytes
        1 packets output, 28 bytes
        1 packets dropped
      1 minute input rate 0 pkts/sec,  0 bytes/sec
      1 minute output rate 0 pkts/sec,  0 bytes/sec
      1 minute drop rate, 0 pkts/sec
      5 minute input rate 0 pkts/sec,  0 bytes/sec
      5 minute output rate 0 pkts/sec,  0 bytes/sec
      5 minute drop rate, 0 pkts/sec
  Control Point Interface States:
        Interface number is 16
        Interface config status is active
        Interface state is active

```

**Help:** execute the command "show interface detail"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show ospf interface brief

**Output:**
```
Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Outside      101   101             10.10.100.10/255.255.255.248    10   P2P 1/1
Transit      100   100             10.255.111.1/255.255.255.248    10   BDR 1/1
Inside       100   110             10.25.1.17/255.255.255.240    10    DR 2/2
CustA        101   0.0.1.1         10.200.0.1/255.255.255.240    10    DR 0/0
```

**Help:** execute the command "show ospf interface brief"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show logging

**Output:**
```
Syslog logging: enabled
    Facility: 20
    Timestamp logging: disabled
    Hide Username logging: disabled
    Standby logging: disabled
    Debug-trace logging: disabled
    Console logging: disabled
    Monitor logging: disabled
    Buffer logging: level warnings, 4908890 messages logged
    Trap logging: level informational, facility 20, 0 messages logged
    Global TCP syslog stats::
        NOT_PUTABLE: 0, ALL_CHANNEL_DOWN: 0
        CHANNEL_FLAP_CNT: 0, SYSLOG_PKT_LOSS: 0
        PARTIAL_REWRITE_CNT: 0
    Permit-hostdown logging: disabled
    History logging: disabled
    Device ID: disabled
    Mail logging: disabled
    ASDM logging: level warnings, 4 messages logged
HQ-ASA5585 : %ASA-4-106023: Deny udp src dmz:10.20.22.121/123 dst outside:123.34.0.90/123 by access-group "dmz" [0x0, 0x0]
HQ-ASA5585 : %ASA-4-313005: No matching connection for ICMP error message: icmp src inside:192.168.45.44 dst outside:4.2.2.9 (type 3, code 3) on inside interface.  Original IP payload: udp src 4.2.2.9/53 dst 192.168.45.44/50765.
 HQ-ASA5585 : %ASA-3-305006: regular translation creation failed for icmp src inside:172.16.111.2 dst outside:1.1.1.4 (type 3, code 3)
HQ-ASA5585 : %ASA-4-733100: [ Scanning] drop rate-1 exceeded. Current burst rate is 2 per second, max configured rate is 10; Current average rate is 5 per second, max configured rate is 5; Cumulative total count is 3299
HQ-ASA5585 : %ASA-4-313005: No matching connection for ICMP error message: icmp src inside:172.16.111.2 dst outside:75.66.66.22 (type 3, code 3) on inside interface.  Original IP payload: udp src 75.66.66.22/53 dst 172.16.111.2/57348.

```

**Help:** execute the command "show logging"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show vpn-sessiondb detail l2l

**Output:**
```
Session Type: LAN-to-LAN Detailed

Connection   : 169.254.107.1
Index        : 6539                   IP Addr      : 169.254.107.1
Protocol     : IKE IPsec
Encryption   : AES128 AES256          Hashing      : SHA1
 Bytes Tx     : 3419524983             Bytes Rx     : 275429647
Login Time   : 10:58:15 PDT Thu Jul 19 2018
Duration     : 10d 7h:26m:52s

IKE Tunnels: 1
IPsec Tunnels: 5

IKE:
  Tunnel ID    : 6539.1
  UDP Src Port : 500                    UDP Dst Port : 500
  IKE Neg Mode : Main                   Auth Mode    : preSharedKeys
  Encryption   : AES128                 Hashing      : SHA1
  Rekey Int (T): 86400 Seconds          Rekey Left(T): 76776 Seconds
  D/H Group    : 2
  Filter Name  : TestFilter
  IPv6 Filter  : 

IPsec:
  Tunnel ID    : 6539.2
  Local Addr   : 169.254.44.0/255.255.252.0/0/0
  Remote Addr  : 1.1.1.1/255.255.255.255/0/0
  Encryption   : AES256                 Hashing      : SHA1                   
  Encapsulation: Tunnel                 
  Rekey Int (T): 28800 Seconds          Rekey Left(T): 19174 Seconds          
  Rekey Int (D): 4608000 K-Bytes        Rekey Left(D): 4586873 K-Bytes        
  Idle Time Out: 30 Minutes             Idle TO Left : 29 Minutes             
  Bytes Tx     : 3256642959             Bytes Rx     : 268532214              
  Pkts Tx      : 4539818                Pkts Rx      : 2958857                
  
IPsec:
  Tunnel ID    : 6539.3
  Local Addr   : 169.254.44.0/255.255.255.0/0/0
  Remote Addr  : 1.1.1.1/255.255.255.255/0/0
  Encryption   : AES256                 Hashing      : SHA1                   
  Encapsulation: Tunnel                 
  Rekey Int (T): 28800 Seconds          Rekey Left(T): 19482 Seconds          
  Rekey Int (D): 4608000 K-Bytes        Rekey Left(D): 4607988 K-Bytes        
  Idle Time Out: 30 Minutes             Idle TO Left : 23 Minutes             
  Bytes Tx     : 162882024              Bytes Rx     : 6897433                
  Pkts Tx      : 136730                 Pkts Rx      : 121906                 
  
NAC:
  Reval Int (T): 0 Seconds              Reval Left(T): 0 Seconds
  SQ Int (T)   : 0 Seconds              EoU Age(T)   : 890906 Seconds
  Hold Left (T): 0 Seconds              Posture Token: 
  Redirect URL : 

Connection   : 169.254.104.1
Index        : 7379                   IP Addr      : 169.254.104.1
Protocol     : IKE IPsec
Encryption   : AES256                 Hashing      : SHA1
Bytes Tx     : 2005616                Bytes Rx     : 79487
Login Time   : 04:00:32 PDT Sun Jul 29 2018
Duration     : 14h:24m:35s

IKE Tunnels: 1
IPsec Tunnels: 4

IKE:
  Tunnel ID    : 7379.1
  UDP Src Port : 500                    UDP Dst Port : 500
  IKE Neg Mode : Main                   Auth Mode    : preSharedKeys
  Encryption   : AES256                 Hashing      : SHA1
  Rekey Int (T): 28800 Seconds          Rekey Left(T): 20119 Seconds
  D/H Group    : 2
  Filter Name  : acl_SOURCE_MED
  IPv6 Filter  : 

IPsec:
  Tunnel ID    : 7379.6
  Local Addr   : 169.254.32.0/255.255.252.0/0/0
  Remote Addr  : 172.20.8.183/255.255.255.255/0/0
  Encryption   : AES256                 Hashing      : SHA1                   
  Encapsulation: Tunnel                 
  Rekey Int (T): 28800 Seconds          Rekey Left(T): 6889 Seconds           
  Rekey Int (D): 4608000 K-Bytes        Rekey Left(D): 4607947 K-Bytes        
  Idle Time Out: 30 Minutes             Idle TO Left : 29 Minutes             
  Bytes Tx     : 140576                 Bytes Rx     : 79487                  
  Pkts Tx      : 1520                   Pkts Rx      : 1509                   
  
IPsec:
  Tunnel ID    : 7379.8
  Local Addr   : 169.254.20.23/255.255.252.0/0/0
  Remote Addr  : 172.20.8.98/255.255.255.255/0/0
  Encryption   : AES256                 Hashing      : SHA1                   
  Encapsulation: Tunnel                 
  Rekey Int (T): 28800 Seconds          Rekey Left(T): 25947 Seconds          
  Rekey Int (D): 4608000 K-Bytes        Rekey Left(D): 0 K-Bytes              
  Idle Time Out: 30 Minutes             Idle TO Left : 29 Minutes             
  Bytes Tx     : 102540                 Bytes Rx     : 0                      
  Pkts Tx      : 1709                   Pkts Rx      : 0                      
  
NAC:
  Reval Int (T): 0 Seconds              Reval Left(T): 0 Seconds
  SQ Int (T)   : 0 Seconds              EoU Age(T)   : 51881 Seconds
  Hold Left (T): 0 Seconds              Posture Token: 
  Redirect URL : 

Connection   : 169.254.99.1
Index        : 79                     IP Addr      : 169.254.99.1
Protocol     : IKEv1 IPsec
Encryption   : IKEv1: (1)3DES  IPsec: (2)3DES
Hashing      : IKEv1: (1)SHA1  IPsec: (2)MD5
Bytes Tx     : 3722401287             Bytes Rx     : 445893825
Login Time   : 16:01:03 MDT Fri Jul 6 2018
Duration     : 21d 15h:39m:02s

IKEv1 Tunnels: 1
IPsec Tunnels: 3

IKEv1:
  Tunnel ID    : 79.1
  UDP Src Port : 500                    UDP Dst Port : 500
  IKE Neg Mode : Main                   Auth Mode    : preSharedKeys
  Encryption   : 3DES                   Hashing      : SHA1
  Rekey Int (T): 28800 Seconds          Rekey Left(T): 18795 Seconds
  D/H Group    : 2
  Filter Name  : TestFilter

IPsec:
  Tunnel ID    : 79.3
  Local Addr   : 169.254.20.22/255.255.255.255/0/0
  Remote Addr  : 192.168.6.74/255.255.255.255/0/0
  Encryption   : 3DES                   Hashing      : MD5                    
  Encapsulation: Tunnel                 
  Rekey Int (T): 28800 Seconds          Rekey Left(T): 18904 Seconds          
  Rekey Int (D): 4608000 K-Bytes        Rekey Left(D): 4607926 K-Bytes        
  Idle Time Out: 30 Minutes             Idle TO Left : 28 Minutes             
  Bytes Tx     : 12721728               Bytes Rx     : 2387175                
  Pkts Tx      : 29085                  Pkts Rx      : 29509                  
  
IPsec:
  Tunnel ID    : 79.71
  Local Addr   : 169.254.20.21/255.255.255.255/0/0
  Remote Addr  : 192.168.6.71/255.255.255.255/0/0
  Encryption   : 3DES                   Hashing      : MD5                    
  Encapsulation: Tunnel                 
  Rekey Int (T): 28800 Seconds          Rekey Left(T): 25194 Seconds          
  Rekey Int (D): 4608000 K-Bytes        Rekey Left(D): 4607999 K-Bytes        
  Idle Time Out: 30 Minutes             Idle TO Left : 25 Minutes             
  Bytes Tx     : 519703                 Bytes Rx     : 437245                 
  Pkts Tx      : 8681                   Pkts Rx      : 8677                   

Connection   : 169.254.44.1
Index        : 5092                   IP Addr      : 169.254.44.1
Protocol     : IKEv1 IPsec
Encryption   : IKEv1: (1)AES256  IPsec: (1)AES128
Hashing      : IKEv1: (1)SHA1  IPsec: (1)SHA1
Bytes Tx     : 2994391497             Bytes Rx     : 337511800
Login Time   : 01:00:20 MDT Wed Jul 11 2018
Duration     : 17d 6h:39m:45s

IKEv1 Tunnels: 1
IPsec Tunnels: 1

IKEv1:
  Tunnel ID    : 5092.1
  UDP Src Port : 500                    UDP Dst Port : 500
  IKE Neg Mode : Main                   Auth Mode    : preSharedKeys
  Encryption   : AES256                 Hashing      : SHA1
  Rekey Int (T): 28800 Seconds          Rekey Left(T): 11946 Seconds
  D/H Group    : 2
  Filter Name  : TestFilter

IPsec:
  Tunnel ID    : 5092.2
  Local Addr   : 169.254.20.20/255.255.255.255/0/0
  Remote Addr  : 10.10.10.13/255.255.255.255/0/0
  Encryption   : AES128                 Hashing      : SHA1                   
  Encapsulation: Tunnel                 PFS Group    : 2                      
  Rekey Int (T): 3600 Seconds           Rekey Left(T): 2132 Seconds           
  Rekey Int (D): 4608000 K-Bytes        Rekey Left(D): 4607009 K-Bytes        
  Idle Time Out: 30 Minutes             Idle TO Left : 29 Minutes             
  Bytes Tx     : 2994391497             Bytes Rx     : 337511800              
  Pkts Tx      : 3539590                Pkts Rx      : 2455325                

Connection   : 169.254.60.1
Index        : 3908                   IP Addr      : 169.254.60.1
Protocol     : IKEv2 IPsec
Encryption   : IKEv2: (1)AES256  IPsec: (1)AES256
Hashing      : IKEv2: (1)SHA1  IPsec: (1)SHA256
Bytes Tx     : 31086457               Bytes Rx     : 19006105
Login Time   : 16:33:31 PDT Fri May 18 2018
Duration     : 79d 16h:39m:59s

IKEv2 Tunnels: 1
IPsec Tunnels: 1

IKEv2:
  Tunnel ID    : 3908.1
  UDP Src Port : 500                    UDP Dst Port : 500
  Rem Auth Mode: preSharedKeys
  Loc Auth Mode: preSharedKeys
  Encryption   : AES256                 Hashing      : SHA1
  Rekey Int (T): 86400 Seconds          Rekey Left(T): 21432 Seconds
  PRF          : SHA1                   D/H Group    : 5
  Filter Name  : 

IPsec:
  Tunnel ID    : 3908.2
  Local Addr   : 0.0.0.0/0.0.0.0/0/0
  Remote Addr  : 10.250.253.120/255.255.255.248/0/0
  Encryption   : AES256                 Hashing      : SHA256                 
  Encapsulation: Tunnel                 
  Rekey Int (T): 3600 Seconds           Rekey Left(T): 3094 Seconds           
  Rekey Int (D): 4608000 K-Bytes        Rekey Left(D): 4607999 K-Bytes        
  Idle Time Out: 30 Minutes             Idle TO Left : 27 Minutes             
  Bytes Tx     : 9993110                Bytes Rx     : 12080533               
  Pkts Tx      : 93673                  Pkts Rx      : 72095 

```

**Help:** execute the command "show vpn-sessiondb detail l2l"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show resource usage

**Output:**
```
Resource                 Current        Peak      Limit        Denied Context
Telnet                         0           1          5             0 admin
SSH Server                     2           5          5             0 admin
ASDM                           1           5          5            18 admin
Syslogs [rate]                 0        1153  unlimited             0 admin
Conns                        177         319  unlimited             0 admin
Hosts                         11          19  unlimited             0 admin
Inspects [rate]                0          99  unlimited             0 admin
Routes                         3           3  unlimited             0 admin
Syslogs [rate]                 0         112  unlimited             0 DATA
Conns                         20        1031  unlimited             0 DATA
Hosts                         18          28  unlimited             0 DATA
Inspects [rate]                0          73  unlimited             0 DATA
Routes                        30          30  unlimited             0 DATA
Syslogs [rate]               329        6727  unlimited             0 TEST
Conns                       5802       32491  unlimited             0 TEST
Xlates                       943         944  unlimited             0 TEST
Hosts                       2085        7120  unlimited             0 TEST
Conns [rate]                 605        7235  unlimited             0 TEST
Inspects [rate]              510        3574  unlimited             0 TEST
Routes                       701         701  unlimited             0 TEST
S = System: Combined context limits exceed the system limit; the system limit is shown

```

**Help:** execute the command "show resource usage"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show route

**Output:**
```
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route, + - replicated route
Gateway of last resort is 192.168.1.2 to network 0.0.0.0

S*       0.0.0.0 0.0.0.0 [1/0] via 192.168.1.2, outside
O E1     10.15.0.0 255.255.0.0 [110/21] via 192.168.2.1, 3w1d, inside
O E1     172.23.100.0 255.255.254.0 
           [110/50] via 192.168.2.1, 3w1d, inside
O E1     172.23.42.0 255.255.254.0 
           [110/11] via 172.17.13.52, 2w2d, routing
           [110/11] via 172.17.13.51, 7w0d, routing
C        172.17.13.0 255.255.255.0 is directly connected, routing
L        172.17.13.60 255.255.255.255 is directly connected, routing           
C        192.168.1.0 255.255.255.0 is directly connected, outside
L        192.168.1.108 255.255.255.255 is directly connected, outside
C        192.168.2.0 255.255.255.0 is directly connected, inside
L        192.168.2.108 255.255.255.255 is directly connected, inside

```

**Help:** execute the command "show route"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show crypto ipsec sa

**Output:**
```
interface: outside2
     Crypto map tag: def, local addr: 10.132.0.17
       local ident (addr/mask/prot/port): (0.0.0.0/0.0.0.0/0/0)
       remote ident (addr/mask/prot/port): (172.20.0.21/255.255.255.255/0/0)
       current_peer: 172.20.0.21
       dynamic allocated peer ip: 10.135.1.5
       #pkts encaps: 0, #pkts encrypt: 0, #pkts digest: 0
       #pkts decaps: 1145, #pkts decrypt: 1145, #pkts verify: 1145
       #pkts compressed: 0, #pkts decompressed: 0
       #pkts not compressed: 0, #pkts comp failed: 0, #pkts decomp failed: 0
       #pre-frag successes: 2, #pre-frag failures: 1, #fragments created: 10
       #PMTUs sent: 5, #PMTUs rcvd: 2, #decapsulated frags needing reassembly: 1
       #send errors: 0, #recv errors: 0
       local crypto endpt.: 10.132.0.17, remote crypto endpt.: 172.20.0.21
       path mtu 1500, ipsec overhead 60, media mtu 1500
       current outbound spi: DC15BF68
     inbound esp sas:
       spi: 0x1E8246FC (511854332)
          transform: esp-3des esp-md5-hmac
          in use settings ={{RA, Tunnel, }}
          slot: 0, conn_id: 3, crypto-map: def
          sa timing: remaining key lifetime (sec): 548
          IV size: 8 bytes
          replay detection support: Y
     outbound esp sas:
       spi: 0xDC15BF68 (3692412776)
          transform: esp-3des esp-md5-hmac
          in use settings ={{RA, Tunnel, }}
          slot: 0, conn_id: 3, crypto-map: def
          sa timing: remaining key lifetime (sec): 548
          IV size: 8 bytes
          replay detection support: Y

interface: COLO
    Crypto map tag: COLO-MAP, seq num: 2, local addr: 172.16.248.119

      access-list 2 extended permit ip 172.16.122.32 255.255.255.240 host 172.30.1.153
      local ident (addr/mask/prot/port): (172.16.122.32/255.255.255.240/0/0)
      remote ident (addr/mask/prot/port): (172.30.1.153/255.255.255.255/0/0)
      current_peer: 8.8.8.8


      #pkts encaps: 13915315, #pkts encrypt: 13915315, #pkts digest: 13915315
      #pkts decaps: 23606461, #pkts decrypt: 23606461, #pkts verify: 23606461
      #pkts compressed: 0, #pkts decompressed: 0
      #pkts not compressed: 13915315, #pkts comp failed: 0, #pkts decomp failed: 0
      #pre-frag successes: 0, #pre-frag failures: 0, #fragments created: 0
      #PMTUs sent: 0, #PMTUs rcvd: 0, #decapsulated frgs needing reassembly: 0
      #TFC rcvd: 0, #TFC sent: 0
      #Valid ICMP Errors rcvd: 0, #Invalid ICMP Errors rcvd: 0
      #send errors: 0, #recv errors: 0

      local crypto endpt.: 172.16.248.119/4500, remote crypto endpt.: 8.8.8.8/4500
      path mtu 1500, ipsec overhead 82(52), media mtu 1500
      PMTU time remaining (sec): 0, DF policy: copy-df
      ICMP error validation: disabled, TFC packets: disabled
      current outbound spi: 50023DDC
      current inbound spi : 32F752FF

    inbound esp sas:
      spi: 0x32F752FF (855069439)
         SA State: active
         transform: esp-aes-256 esp-md5-hmac no compression
         in use settings ={{L2L, Tunnel,  NAT-T-Encaps, IKEv1, }}
         slot: 0, conn_id: 159694848, crypto-map: COLO-MAP
         sa timing: remaining key lifetime (kB/sec): (2699423/25461)
         IV size: 16 bytes
         replay detection support: Y
         Anti replay bitmap:
          0xFFFFFFFF 0xFFFFFFFF
    outbound esp sas:
      spi: 0x50023DDC (1342324188)
         SA State: active
         transform: esp-aes-256 esp-md5-hmac no compression
         in use settings ={{L2L, Tunnel,  NAT-T-Encaps, IKEv1, }}
         slot: 0, conn_id: 159694848, crypto-map: COLO-MAP
         sa timing: remaining key lifetime (kB/sec): (3892153/25461)
         IV size: 16 bytes
         replay detection support: Y
         Anti replay bitmap:
          0x00000000 0x00000001

    Crypto map tag: COLO-MAP, seq num: 3, local addr: LOCAL-ADDR-172.20.248.119

      access-list 200 extended permit ip 172.20.122.32 255.255.255.240 10.160.4.0 255.255.255.0
      local ident (addr/mask/prot/port): (172.20.122.32/255.255.255.240/0/0)
      remote ident (addr/mask/prot/port): (10.160.4.0/255.255.255.0/0/0)
      current_peer: REMOTE-PEER-8.8.4.4


      #pkts encaps: 0, #pkts encrypt: 0, #pkts digest: 0
      #pkts decaps: 0, #pkts decrypt: 0, #pkts verify: 0
      #pkts compressed: 0, #pkts decompressed: 0
      #pkts not compressed: 0, #pkts comp failed: 0, #pkts decomp failed: 0
      #pre-frag successes: 0, #pre-frag failures: 0, #fragments created: 0
      #PMTUs sent: 0, #PMTUs rcvd: 0, #decapsulated frgs needing reassembly: 0
      #TFC rcvd: 0, #TFC sent: 0
      #Valid ICMP Errors rcvd: 0, #Invalid ICMP Errors rcvd: 0
      #send errors: 0, #recv errors: 0

      local crypto endpt.: LOCAL-ADDR-172.20.248.119/500, remote crypto endpt.: REMOTE-PEER-8.8.4.4/500
      path mtu 1500, ipsec overhead 74(44), media mtu 1500
      PMTU time remaining (sec): 0, DF policy: copy-df
      ICMP error validation: disabled, TFC packets: disabled
      current outbound spi: EA40155F
      current inbound spi : 6A7391E0

    inbound esp sas:
      spi: 0x6A7391E0 (1785958880)
         SA State: active
         transform: esp-aes-256 esp-md5-hmac no compression
         in use settings ={{L2L, Tunnel, IKEv1, }}
         slot: 0, conn_id: 14376960, crypto-map: COLO-MAP
         sa timing: remaining key lifetime (kB/sec): (2038431743/70749)
         IV size: 16 bytes
         replay detection support: Y
         Anti replay bitmap:
          0x00000000 0x00000001
    outbound esp sas:
      spi: 0xEA40155F (3930068319)
         SA State: active
         transform: esp-aes-256 esp-md5-hmac no compression
         in use settings ={{L2L, Tunnel, IKEv1, }}
         slot: 0, conn_id: 14376960, crypto-map: COLO-MAP
         sa timing: remaining key lifetime (kB/sec): (2038431743/70749)
         IV size: 16 bytes
         replay detection support: Y
         Anti replay bitmap:
          0x00000000 0x00000001

```

**Help:** execute the command "show crypto ipsec sa"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show name

**Output:**
```
name 10.1.1.1 server
name 10.1.1.10 server1
name 10.1.10.1 server-1
 name 10.1.1.1 server_1
name 10.10.1.1 server_web
name 10.1.10.10 server-db
 name 10.10.1.10 server_web1
name 10.10.10.10 server-web1
name 10.1.1.100 1server
 name 10.1.100.100 1-server
name 10.100.1.100 1_server
name 10.100.100.100 server2

```

**Help:** execute the command "show name"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show vpn-sessiondb anyconnect

**Output:**
```
Session Type: AnyConnect

Username     : USER               Index        : 1018
Assigned IP  : 10.254.254.22          Public IP    : 1.2.3.4
Protocol     : AnyConnect-Parent SSL-Tunnel DTLS-Tunnel
License      : AnyConnect Premium
Encryption   : AnyConnect-Parent: (1)none  SSL-Tunnel: (1)AES-GCM-256  DTLS-Tunnel: (1)AES128
Hashing      : AnyConnect-Parent: (1)none  SSL-Tunnel: (1)SHA384  DTLS-Tunnel: (1)SHA1
Bytes Tx     : 17186425               Bytes Rx     : 7094561
Group Policy : RAVPN                  Tunnel Group : RAVPN
 Login Time   : 14:28:09 CDT Tue Mar 17 2020
Duration     : 2h:21m:21s
Inactivity   : 0h:00m:00s
VLAN Mapping : N/A                    VLAN         : none
 Audt Sess ID : ac1063fe003fa0005e715555
Security Grp : none                   

Username     : lee                    Index        : 1
Assigned IP  : 192.168.246.1           Public IP    : 10.139.1.2
Protocol     : AnyConnect-Parent SSL-Tunnel DTLS-Tunnel
License      : AnyConnect Premium
Encryption   : RC4 AES128
Hashing      : SHA1
Bytes Tx     : 11079                  Bytes Rx     : 4942
Group Policy : EngPolicy            Tunnel Group : EngGroup
 Login Time   : 15:25:13 EST Fri Jan 28 2011
Duration     : 0h:00m:15s
Inactivity   : 0h:00m:00s
VLAN Mapping : N/A                    VLAN         : none
 Audt Sess ID : a31867c632efaeaad
Security Grp : none                   

```

**Help:** execute the command "show vpn-sessiondb anyconnect"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show xlate

**Output:**
```
5 in use, 5 most used
Flags: D - DNS, i - dynamic, r - portmap, s - static, I - identity, T - twice
e - extended
NAT from any:10.90.67.2 to any:10.9.1.0/24
 flags idle 277:05:26 timeout 0:00:00
NAT from any:10.1.1.0/24 to any:172.16.1.0/24
 flags idle 277:05:26 timeout 0:00:00
NAT from any:10.90.67.2 to any:10.86.94.0
 flags idle 277:05:26 timeout 0:00:00
NAT from any:10.9.0.9, 10.9.0.10/31, 10.9.0.12/30,
 10.9.0.16/28, 10.9.0.32/29, 10.9.0.40/30,
10.9.0.44/31 to any:0.0.0.0
flags idle 277:05:26 timeout 0:00:00
NAT from any:10.1.1.0/24 to any:172.16.1.0/24
 flags idle 277:05:14 timeout 0:00:00
NAT from inside:192.168.1.150 to outside:172.18.254.252 flags s idle 0:01:37 timeout 0:00:00

```

**Help:** execute the command "show xlate"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show running-config crypto map

**Output:**
```
crypto map Standard-1 20 match address peer1
crypto map Standard-1 20 set pfs group5
crypto map Standard-1 20 set peer Peer-1 
crypto map Standard-1 20 set ikev1 transform-set Standard-Transform
crypto map Standard-1 20 set security-association lifetime seconds 28800
crypto map Standard-1 25 match address peer2
crypto map Standard-1 25 set pfs group2
crypto map Standard-1 25 set peer Peer-2 
crypto map Standard-1 25 set ikev1 transform-set Standard-Transform
 crypto map Standard-1 25 set security-association lifetime seconds 28800
crypto map Standard-1 interface outside

```

**Help:** execute the command "show running-config crypto map"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show inventory

**Output:**
```
Name: "Chassis", DESCR: "ASA 5506-X with FirePOWER services, 8GE, AC, DES"
PID: ASA5506           , VID: V01     , SN: JMX8318372GB

Name: "Storage Device 1", DESCR: "ASA 5506-X SSD"
PID: ASA5506-SSD       , VID: N/A     , SN:
```

**Help:** execute the command "show inventory"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show running-config ipsec

**Output:**
```
crypto ipsec ikev1 transform-set AES-256_MD5 esp-aes-256 esp-md5-hmac 
crypto ipsec ikev1 transform-set AES-256_SHA esp-aes-256 esp-sha-hmac 
crypto ipsec ikev1 transform-set 3DES_MD5 esp-3des esp-md5-hmac 
crypto ipsec ikev1 transform-set 3DES_SHa esp-3des esp-sha-hmac 
crypto ipsec ikev1 transform-set AES_MD5 esp-aes esp-md5-hmac 
crypto ipsec ikev1 transform-set AES_SHA esp-aes esp-sha-hmac 
crypto ipsec ikev1 transform-set AES-192_MD5 esp-aes-192 esp-md5-hmac 
crypto ipsec ikev1 transform-set AES-192_SHA esp-aes-192 esp-sha-hmac 
crypto ipsec ikev2 ipsec-proposal IKE2
 protocol esp encryption aes-gcm-256 aes-gcm-192 aes-gcm aes-256 aes-192 aes 3des des aes-gmac-256 aes-gmac-192 aes-gmac
 protocol esp integrity sha-512 sha-384 sha-256 sha-1 md5
crypto ipsec ikev2 ipsec-proposal NEW_IKE2
 protocol esp encryption aes-gcm-256 aes-gcm-192 aes-gcm aes-256 aes-192 aes 3des des aes-gmac-256 aes-gmac-192 aes-gmac
crypto ipsec ikev2 ipsec-proposal newer_ike2
 protocol esp integrity sha-512 sha-384 sha-256 sha-1 md5
crypto ipsec ikev1 transform-set DES_MD5 esp-des esp-md5-hmac 
crypto ipsec ikev1 transform-set DES_SHA esp-des esp-sha-hmac 
crypto ipsec ikev2 ipsec-proposal final_IKE2
 protocol esp encryption aes-gcm-256 aes-gcm-192 3des des aes-gmac-256 aes-gmac-192 aes-gmac
 protocol esp integrity sha-512 sha-1 md5
```

**Help:** execute the command "show running-config ipsec"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show object-group network

**Output:**
```
object-group network NETWORK-10.42.89.0_24
 network-object 10.142.89.0 255.255.255.0
object-group network network-10.0.0.0_8
 network-object 10.0.0.0 255.0.0.0
object-group network SITE-A
 network-object host 10.1.1.22
object-group network site-b
 network-object host 10.1.1.33
object-group network Lab
 network-object 10.143.185.10 255.255.255.255
 network-object 10.143.185.15 255.255.255.255
 object-group network Dev
 group-object dev_web-servers
 network-object object DEV_DB
object-group network Prod
 description: Prod Environment
 network-object 10.14.88.115 255.255.255.255
 network-object host 10.135.92.6
 network-object object svr01
 group-object prod_dc
object-group network dr
 description: dr-network
 network-object 10.210.0.0 255.255.0.0
object-group network dr2
 description dr2-network
 network-object 10.211.0.0 255.255.0.0

```

**Help:** execute the command "show object-group network"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show interface

**Output:**
```
Interface GigabitEthernet0/0 "outside", is up, line protocol is up
  Hardware is i82540EM rev03, BW 1000 Mbps, DLY 10 usec
        Full-Duplex(Full-duplex), Auto-Speed(1000 Mbps)
        Input flow control is unsupported, output flow control is off
        Description: to iosv-1
        MAC address fa16.3eb0.c3d3, MTU 1500
        IP address 10.0.0.5, subnet mask 255.255.255.252
        2 packets input, 0 bytes, 0 no buffer
        Received 0 broadcasts, 0 runts, 0 giants
        0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
        0 pause input, 0 resume input
        0 L2 decode drops
        1 packets output, 0 bytes, 0 underruns
        0 pause output, 0 resume output
        0 output errors, 0 collisions, 2 interface resets
        0 late collisions, 0 deferred
        0 input reset drops, 0 output reset drops
        input queue (blocks free curr/low): hardware (511/511)
        output queue (blocks free curr/low): hardware (511/511)
  Traffic Statistics for "outside":
        2 packets input, 381 bytes
        1 packets output, 28 bytes
        2 packets dropped
      1 minute input rate 0 pkts/sec,  0 bytes/sec
      1 minute output rate 0 pkts/sec,  0 bytes/sec
      1 minute drop rate, 0 pkts/sec
      5 minute input rate 0 pkts/sec,  0 bytes/sec
      5 minute output rate 0 pkts/sec,  0 bytes/sec
      5 minute drop rate, 0 pkts/sec
 Interface GigabitEthernet0/1 "outside-1", is up, line protocol is up
  Hardware is i82540EM rev03, BW 1000 Mbps, DLY 10 usec
        Full-Duplex(Full-duplex), Auto-Speed(1000 Mbps)
        Input flow control is unsupported, output flow control is off
        Description: to iosv-2
        MAC address fa16.3ed1.7e26, MTU 1500
        IP address 10.0.0.13, subnet mask 255.255.255.252
        2 packets input, 0 bytes, 0 no buffer
        Received 0 broadcasts, 0 runts, 0 giants
        0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
        0 pause input, 0 resume input
        0 L2 decode drops
        1 packets output, 0 bytes, 0 underruns
        0 pause output, 0 resume output
        0 output errors, 0 collisions, 1 interface resets
        0 late collisions, 0 deferred
        0 input reset drops, 0 output reset drops
        input queue (blocks free curr/low): hardware (509/509)
        output queue (blocks free curr/low): hardware (511/510)
  Traffic Statistics for "outside-1":
        2 packets input, 381 bytes
        1 packets output, 28 bytes
        2 packets dropped
      1 minute input rate 0 pkts/sec,  0 bytes/sec
      1 minute output rate 0 pkts/sec,  0 bytes/sec
      1 minute drop rate, 0 pkts/sec
      5 minute input rate 0 pkts/sec,  0 bytes/sec
      5 minute output rate 0 pkts/sec,  0 bytes/sec
      5 minute drop rate, 0 pkts/sec
 Interface Management0/0 "mgmt", is up, line protocol is up
  Hardware is i82540EM rev03, BW 1000 Mbps, DLY 10 usec
        Full-Duplex(Full-duplex), Auto-Speed(1000 Mbps)
        Input flow control is unsupported, output flow control is off
        Description: OOB Management
        MAC address fa16.3e1c.d1c3, MTU 1500
        IP address 172.16.1.222, subnet mask 255.255.255.0
        119798 packets input, 0 bytes, 0 no buffer
        Received 0 broadcasts, 0 runts, 0 giants
        0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
        0 pause input, 0 resume input
        0 L2 decode drops
        107180 packets output, 0 bytes, 0 underruns
        0 pause output, 0 resume output
        0 output errors, 0 collisions, 1 interface resets
        0 late collisions, 0 deferred
        77 input reset drops, 0 output reset drops
        input queue (blocks free curr/low): hardware (462/426)
        output queue (blocks free curr/low): hardware (509/464)
  Traffic Statistics for "mgmt":
        119720 packets input, 72808618 bytes
        107180 packets output, 33059275 bytes
        28855 packets dropped
      1 minute input rate 1 pkts/sec,  79 bytes/sec
      1 minute output rate 1 pkts/sec,  117 bytes/sec
      1 minute drop rate, 0 pkts/sec
      5 minute input rate 0 pkts/sec,  91 bytes/sec
      5 minute output rate 0 pkts/sec,  11 bytes/sec
      5 minute drop rate, 0 pkts/sec
        Management-only interface. Blocked 0 through-the-device packets
Interface DMZ "DMZ", is up, line protocol is up
        Description: DMZ (Vl3)
        MAC address fa16.3eb0.c3d3, MTU 1500
        IP address 10.6.2.1, subnet mask 255.255.255.0
  Traffic Statistics for "DMZ":
        10797302304 packets input, 7672861881962 bytes
        4822409435 packets output, 1511083097851 bytes
        868027 packets dropped
Interface outside "outside-3", is up, line protocol is up
        Description: outside(Vl2)
        MAC address fa16.3eb0.c3d3, MTU 1500
        IP address 10.12.16.237, subnet mask 255.255.255.248
  Traffic Statistics for "outside-3":
        668040831 packets input, 193650939031 bytes
        700470696 packets output, 316092320235 bytes
        26397124 packets dropped
Interface inside "inside", is up, line protocol is up
        MAC address fa16.3eb0.c3d3, MTU 1500
        IP address 10.6.10.1, subnet mask 255.255.255.0
  Traffic Statistics for "inside":
        7645054611 packets input, 2415587779568 bytes
        4906203211 packets output, 778812612541 bytes
        32105760 packets dropped

```

**Help:** execute the command "show interface"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show vpn-sessiondb

**Output:**
```
---------------------------------------------------------------------------
 VPN Session Summary
---------------------------------------------------------------------------
                               Active : Cumulative : Peak Concur : Inactive
                             ----------------------------------------------
 AnyConnect Client            :     38 :     330351 :         442 :        0
  SSL/TLS/DTLS               :     38 :     330351 :         442 :        0
 Clientless VPN               :      0 :       1040 :           9
  Browser                    :      0 :       1040 :           9
---------------------------------------------------------------------------
 Total Active and Inactive    :     38             Total Cumulative : 331391
 Device Total VPN Capacity    :   5000
Device Load                  :     1%
 ---------------------------------------------------------------------------
 ---------------------------------------------------------------------------
 Tunnels Summary
---------------------------------------------------------------------------
                               Active : Cumulative : Peak Concurrent
                             ----------------------------------------------
Clientless                   :      0 :       1040 :               9
AnyConnect-Parent            :     38 :     330351 :             442
SSL-Tunnel                   :     38 :     985244 :             392
DTLS-Tunnel                  :     37 :    2227003 :             386
---------------------------------------------------------------------------
Totals                       :    113 :    3543638
---------------------------------------------------------------------------

```

**Help:** execute the command "show vpn-sessiondb"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show cpu usage detailed

**Output:**
```
Break down of per-core data path versus control point cpu usage:
Core         5 sec               1 min               5 min
Core 0       35.0 (22.4 + 12.6)  35.8 (23.6 + 12.2)  35.2 (23.8 + 11.4)
Core 1       34.6 (34.6 +  0.0)  36.1 (36.1 +  0.0)  36.3 (36.3 +  0.0)
Core 2       34.8 (34.8 +  0.0)  36.4 (36.4 +  0.0)  36.6 (36.6 +  0.0)
Core 3       34.6 (34.6 +  0.0)  36.1 (36.1 +  0.0)  36.2 (36.2 +  0.0)
Core 4       34.4 (34.4 +  0.0)  36.1 (36.1 +  0.0)  36.2 (36.2 +  0.0)
Core 5       34.4 (34.4 +  0.0)  36.0 (36.0 +  0.0)  36.1 (36.1 +  0.0)
Core 6       34.4 (34.4 +  0.0)  36.0 (36.0 +  0.0)  36.1 (36.1 +  0.0)
Core 7       34.6 (34.6 +  0.0)  36.3 (36.3 +  0.0)  36.5 (36.5 +  0.0)
Core 8       34.8 (34.8 +  0.0)  36.4 (36.4 +  0.0)  36.5 (36.5 +  0.0)
Core 9       35.0 (35.0 +  0.0)  36.5 (36.5 +  0.0)  36.6 (36.6 +  0.0)
Core 10      35.2 (35.2 +  0.0)  36.6 (36.6 +  0.0)  36.7 (36.7 +  0.0)
Core 11      35.6 (22.2 + 13.4)  36.1 (23.6 + 12.5)  35.3 (23.8 + 11.6)
 Core 12      34.6 (34.6 +  0.0)  36.1 (36.1 +  0.0)  36.2 (36.2 +  0.0)
Core 13      34.8 (34.8 +  0.0)  36.2 (36.2 +  0.0)  36.3 (36.3 +  0.0)
Core 14      34.8 (34.8 +  0.0)  36.2 (36.2 +  0.0)  36.3 (36.3 +  0.0)
Core 15      34.4 (34.4 +  0.0)  36.1 (36.1 +  0.0)  36.2 (36.2 +  0.0)
Core 16      34.6 (34.6 +  0.0)  36.1 (36.1 +  0.0)  36.2 (36.2 +  0.0)
Core 17      34.6 (34.6 +  0.0)  36.1 (36.1 +  0.0)  36.2 (36.2 +  0.0)
Core 18      35.2 (35.2 +  0.0)  36.6 (36.6 +  0.0)  36.8 (36.8 +  0.0)
Core 19      35.0 (35.0 +  0.0)  36.5 (36.5 +  0.0)  36.7 (36.7 +  0.0)
Core 20      35.0 (35.0 +  0.0)  36.6 (36.6 +  0.0)  36.7 (36.7 +  0.0)
Core 21      35.2 (35.2 +  0.0)  36.8 (36.8 +  0.0)  37.0 (37.0 +  0.0)

Current control point elapsed versus the maximum control point elapsed for:
      5 seconds = 50.0%; 1 minute: 46.5%; 5 minutes: 42.2%


CPU utilization of external processes for:
      5 seconds = 0.0%; 1 minute: 0.0%; 5 minutes: 0.0%


Total CPU utilization for:
      5 seconds = 34.2%; 1 minute: 36.2%; 5 minutes: 36.4%
```

**Help:** execute the command "show cpu usage detailed"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show ospf neighbor

**Output:**
```
Neighbor ID     Pri   State           Dead Time   Address         Interface
10.10.100.9       0   FULL/  -        0:00:07    10.255.100.9    Outside
192.168.100.3     1   FULL/DR         0:00:30    192.168.100.3   Transit
10.25.1.18        1   FULL/BDR        0:00:07    10.253.1.18     Inside
10.25.1.19        1   FULL/DROTHER    0:00:07    10.253.1.19     Inside

```

**Help:** execute the command "show ospf neighbor"

**Prompt:**
- cisco_asa>
- cisco_asa#

### dir

**Output:**
```

Directory of disk0:/

120    -rwx  74369568     19:39:56 Nov 03 2015  asa951-lfbff-k8.spa
121    -rwx  25025404     19:40:46 Nov 03 2015  asdm-751.bin
122    -rwx  89           11:48:07 May 04 2016  .boot_string
11     drwx  4096         19:43:48 Nov 03 2015  log
23     drwx  4096         19:44:38 Nov 03 2015  crypto_archive
24     drwx  4096         19:44:40 Nov 03 2015  coredumpinfo
123    drwx  4096         08:33:16 May 31 2016  LOCAL-CA-SERVER
124    -rwx  4096         00:00:00 Jan 01 1980  FSCK0000.REC
125    -rwx  28672        00:00:00 Jan 01 1980  FSCK0001.REC
126    -rwx  4096         00:00:00 Jan 01 1980  FSCK0002.REC
127    -rwx  28672        00:00:00 Jan 01 1980  FSCK0003.REC
128    -rwx  4096         00:00:00 Jan 01 1980  FSCK0004.REC
129    -rwx  19183882     05:45:32 Feb 12 2016  anyconnect-win-4.2.01035-k9.pkg
130    -rwx  17469933     05:45:56 Feb 12 2016  anyconnect-macosx-i386-4.2.01035-k9.pkg
131    -rwx  82330784     05:56:48 Feb 12 2016  asa952-2-lfbff-k8.SPA
132    -rwx  4102         07:07:44 Feb 12 2016  scp_f1
133    -rwx  4102         07:09:04 Feb 12 2016  scp_f2
134    -rwx  2595         07:20:42 Feb 12 2016  general.xml
 
7859437568 bytes total (4417200128 bytes free)

```

**Help:** execute the command "dir"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show bgp summary

**Output:**
```
BGP router identifier 10.10.254.1, local AS number 65101
BGP table version is 9, main routing table version 9
8 network entries using 1600 bytes of memory
 8 path entries using 640 bytes of memory
8/7 BGP path/bestpath attribute entries using 1664 bytes of memory
4 BGP extended community entries using 96 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
BGP using 4000 total bytes of memory
 BGP activity 8/0 prefixes, 8/0 paths, scan interval 60 secs

Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
10.10.254.1     4        65101 961788  961836         9    0    0 4w6d  5       
10.10.254.9     4        65101 961784  961836         9    0    0 4w6d  1   
```

**Help:** execute the command "show bgp summary"

**Prompt:**
- cisco_asa>
- cisco_asa#

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
- cisco_asa>
- cisco_asa#

### show running-config object network

**Output:**
```
object network corp
 subnet 10.0.0.0 255.0.0.0
object network internal
 subnet 192.168.0.0 255.255.255.0
object network any
 subnet 0.0.0.0 0.0.0.0
 object network host-10.10.11.1
 host 10.10.11.1
object network block
 host 10.75.51.11
object network dmz
 description dmz GW ip
 host 11.1.2.2
object network server-vip
 host 10.1.11.8
object network visitors
 range 10.10.10.4 10.10.10.60
object network contractor
 range 10.75.51.15 10.75.51.100
object network cloudflare-ipv6-dns-primary
 host 2606:4700:4700::1111
object network google-ipv6-dns-primary
 host 2001:4860:4860::8888
object network internal-ipv6-range
 range fd00:: fd00::ffff
object network internal-ipv6-subnet
 subnet fd00::/8

```

**Help:** execute the command "show running-config object network"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show access-list

**Output:**
```
access-list test; 51 elements; name hash: 0xcb4257a3
access-list test line 1 extended permit ah any4 interface outside log informational interval 300 inactive (hitcnt=0) (inactive) 0x20db5032 
access-list test line 2 extended deny udp host 10.10.10.11 host 10.10.12.12 eq dnsix (hitcnt=0) 0xfe42d16f 
 access-list test line 3 extended permit object svc1 object test1 object test2 log informational interval 300 (hitcnt=0) 0xb18beb2d 
  access-list test line 3 extended permit icmp fqdn test.com (unresolved) host 10.1.1.2 echo-reply 4 log informational interval 300 (inactive) 0x0397cac0 
access-list test line 4 extended permit tcp object-group grptest1 10.10.10.0 255.255.255.128 (hitcnt=0) 0x26e50070 
  access-list test line 4 extended permit tcp host 10.1.1.10 10.10.10.0 255.255.255.128 (hitcnt=0) 0x44aceee4 
  access-list test line 4 extended permit tcp fqdn test.com (unresolved) 10.10.10.0 255.255.255.128 (inactive) 0x27806b87 
  access-list test line 4 extended permit tcp 10.1.1.8 255.255.255.248 10.10.10.0 255.255.255.128 (hitcnt=0) 0xb65d6d2a 
access-list test line 5 extended permit object-group svcgrp1 object test2 object test3 (hitcnt=0) 0xffc8818e 
  access-list test line 5 extended permit tcp host 10.1.1.2 range 10.1.1.3 10.1.1.8 eq 60 (hitcnt=0) 0x09fd553e 
  access-list test line 5 extended permit tcp host 10.1.1.2 range 10.1.1.3 10.1.1.8 eq www (hitcnt=0) 0xc366785c 
  access-list test line 5 extended permit tcp host 10.1.1.2 range 10.1.1.3 10.1.1.8 gt 100 (hitcnt=0) 0xc7a44ae8 
  access-list test line 5 extended permit tcp host 10.1.1.2 range 10.1.1.3 10.1.1.8 range gopher 71 (hitcnt=0) 0x4db36dd4 
access-list test line 6 extended permit ip object-group grptest2 any4 (hitcnt=0) 0x1b9c9328 
  access-list test line 6 extended permit ip host 10.1.1.10 any4 (hitcnt=0) 0x9d5931ab 
  access-list test line 6 extended permit ip fqdn test.com (unresolved) any4 (inactive) 0x0268299f 
  access-list test line 6 extended permit ip 10.1.1.8 255.255.255.248 any4 (hitcnt=0) 0xa6f62ec7 
  access-list test line 6 extended permit ip host 10.10.10.10 any4 (hitcnt=0) 0xac0ce8e7 
access-list test line 7 extended permit object-group svcgrp4 object test3 object test2 (hitcnt=0) 0x866dbeab 
  access-list test line 7 extended permit tcp range 10.1.1.3 10.1.1.8 host 10.1.1.2 eq domain (hitcnt=0) 0xbef61d61 
  access-list test line 7 extended permit udp range 10.1.1.3 10.1.1.8 host 10.1.1.2 eq domain (hitcnt=0) 0x3f9b81a1 
  access-list test line 7 extended permit tcp range 10.1.1.3 10.1.1.8 host 10.1.1.2 eq 55 (hitcnt=0) 0x99a487f5 
  access-list test line 7 extended permit udp range 10.1.1.3 10.1.1.8 host 10.1.1.2 eq 55 (hitcnt=0) 0xcd700fb1 
access-list test line 8 extended permit tcp object test1 object test1 object-group svcgrp6 (hitcnt=0) 0xd76472ac 
  access-list test line 8 extended permit tcp fqdn test.com (unresolved) fqdn test.com (unresolved) eq aol (inactive) 0x64af6768 
  access-list test line 8 extended permit tcp fqdn test.com (unresolved) fqdn test.com (unresolved) eq www (inactive) 0x29864b9c 
  access-list test line 8 extended permit tcp fqdn test.com (unresolved) fqdn test.com (unresolved) eq 84 (inactive) 0x1f80e564 
access-list test line 9 extended permit object-group prtgrp1 any4 any4 (hitcnt=0) 0x0d8479f0 
  access-list test line 9 extended permit esp any4 any4 (hitcnt=0) 0x79a30bff 
access-list test line 10 extended permit tcp object-group grptest1 object test1 object-group svcgrp8 (hitcnt=0) 0x0ca66136 
  access-list test line 10 extended permit tcp host 10.1.1.10 fqdn test.com (unresolved) eq aol (inactive) 0xd93c8317 
  access-list test line 10 extended permit tcp host 10.1.1.10 fqdn test.com (unresolved) eq www (inactive) 0x98d3e56f 
  access-list test line 10 extended permit tcp host 10.1.1.10 fqdn test.com (unresolved) eq 84 (inactive) 0x45e3cb59 
  access-list test line 10 extended permit tcp fqdn test.com (unresolved) fqdn test.com (unresolved) eq aol (inactive) 0x64af6768 
  access-list test line 10 extended permit tcp fqdn test.com (unresolved) fqdn test.com (unresolved) eq www (inactive) 0x29864b9c 
  access-list test line 10 extended permit tcp fqdn test.com (unresolved) fqdn test.com (unresolved) eq 84 (inactive) 0x1f80e564 
  access-list test line 10 extended permit tcp 10.1.1.8 255.255.255.248 fqdn test.com (unresolved) eq aol (inactive) 0xddad57f9 
  access-list test line 10 extended permit tcp 10.1.1.8 255.255.255.248 fqdn test.com (unresolved) eq www (inactive) 0x38389426 
  access-list test line 10 extended permit tcp 10.1.1.8 255.255.255.248 fqdn test.com (unresolved) eq 84 (inactive) 0x883a126a 
access-list test line 11 extended permit tcp object-group grptest1 object test1 object-group svcgrp7 (hitcnt=0) 0xb396512b 
  access-list test line 11 extended permit tcp host 10.1.1.10 fqdn test.com (unresolved) eq domain (inactive) 0x5637d648 
  access-list test line 11 extended permit tcp fqdn test.com (unresolved) fqdn test.com (unresolved) eq domain (inactive) 0x3cd20161 
  access-list test line 11 extended permit tcp 10.1.1.8 255.255.255.248 fqdn test.com (unresolved) eq domain (inactive) 0x69655129 
access-list test line 12 extended permit tcp 10.20.30.0 255.255.255.0 10.50.12.0 255.255.255.224 eq www (hitcnt=0) 0x3f0331e6 
access-list test line 13 extended permit object svc10 host 10.21.10.5 host 10.50.20.10 (hitcnt=0) 0xc766bdc7 
  access-list test line 13 extended permit tcp host 10.21.10.5 host 10.50.20.10 range www 88 (hitcnt=0) 0xc766bdc7 
access-list test line 14 extended permit tcp host 10.20.30.22 10.50.12.0 255.255.255.224 eq www (hitcnt=0) 0x3f0331e6 
access-list test line 15 remark explicit-deny 
access-list test line 16 extended deny ip any4 any (hitcnt=0) 0x60edeab9
access-list test line 17 remark ************ Allow ICMP *************
access-list test line 18 extended permit icmp any any time-exceeded log informational interval 300 (hitcnt=31778) 0x6c633843
 access-list test line 19 extended permit icmp any4 any4 time-exceeded log informational interval 300 (hitcnt=0) 0x19b0643c
access-list test line 20 extended permit icmp any4 any4 unreachable log informational interval 300 (hitcnt=1902659) 0x5e72d761
 access-list test line 21 extended permit icmp any4 any4 echo log informational interval 300 (hitcnt=0) 0x2405f42c
access-list test line 22 extended permit icmp any4 any4 echo-reply log informational interval 300 (hitcnt=572136) 0x95dca5e7
 access-list test line 23 extended permit icmp any4 169.254.148.0 255.255.0.0 echo (hitcnt=0) 0x735d2ad8
access-list test line 24 extended permit icmp any4 169.254.148.0 255.255.0.0 echo-reply (hitcnt=0) 0x4b1cc532
access-list test line 25 extended permit icmp any4 169.254.148.0 255.255.0.0 unreachable (hitcnt=0) 0x3111e9c0
access-list test line 26 extended permit icmp any4 169.254.148.0 255.255.0.0 time-exceeded (hitcnt=0) 0x7a963265
access-list test line 27 extended permit icmp any4 169.254.147.0 255.255.0.0 echo-reply (hitcnt=0) 0x07bfbf99
 access-list test line 28 extended permit icmp any4 169.254.147.0 255.255.0.0 echo (hitcnt=0) 0x99e30c47
access-list test line 29 extended permit icmp any4 169.254.147.0 255.255.0.0 unreachable (hitcnt=0) 0x91a15afa
access-list test line 30 extended permit icmp any4 169.254.151.0 255.255.0.0 echo-reply (hitcnt=0) 0xfb31202c
access-list test line 31 extended permit icmp any4 169.254.147.0 255.255.0.0 time-exceeded (hitcnt=0) 0x2bc95316
access-list test line 32 extended permit icmp any4 169.254.151.0 255.255.0.0 echo (hitcnt=0) 0x0f3edcdd
access-list test line 33 extended permit icmp any4 169.254.151.0 255.255.0.0 unreachable (hitcnt=0) 0x7887741b
access-list test line 34 extended permit icmp any4 169.254.151.0 255.255.0.0 time-exceeded (hitcnt=0) 0x480bef5c
access-list test line 35 extended deny icmp any any (hitcnt=3) 0xff7fd0ca
access-list test line 36 extended permit tcp object-group test_gr object-group test_gr_02 eq ftp-data (hitcnt=0) 0x05e8add7 
  access-list test line 36 extended permit tcp host 212.179.71.34 host 10.2.74.35 eq ftp-data (hitcnt=0) 0x9fb86c39 
access-list test line 37 extended permit tcp object network-172.16.0.0 object aps03-aps04_gaibu_vip eq ssh inactive (hitcnt=0) (inactive) 0xcc9741b2 
  access-list test line 37 extended permit tcp 172.16.0.0 255.240.0.0 host 10.2.66.237 eq ssh inactive (hitcnt=0) (inactive) 0xcc9741b2 
access-list test line 38 extended permit tcp object ClientPC object-group NETWORK_100 inactive (hitcnt=0) (inactive) 0xc47bdfe9 
  access-list test line 38 extended permit tcp host 172.31.168.7 host 10.2.88.104 inactive (hitcnt=0) (inactive) 0x7e7a99ef 
  access-list test line 38 extended permit tcp host 172.31.168.7 host 10.2.88.100 inactive (hitcnt=0) (inactive) 0x4094da11 
access-list test line 39 extended permit tcp object-group NETWORK_88 object aps0506_VIP_10.2.66.53 eq 6991 log disable (hitcnt=55) 0xe547ccd6 
  access-list test line 39 extended permit tcp 10.0.247.0 255.255.255.0 host 10.2.66.53 eq 6991 log disable (hitcnt=40) 0xea52300b 

```

**Help:** execute the command "show access-list"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show running-config tunnel-group

**Output:**
```
tunnel-group tun01 type remote-access
tunnel-group tun01 general-attributes
 dhcp-server 10.10.10.10
 dhcp-server link-selection 10.10.10.11
 dhcp-server subnet-selection 10.10.10.12
 authorization-required
 authorization-server-group (outside) aaa
 accounting-server-group aaa
 address-pool (vpn) vpn_pool
 authentication-server-group (outside) LOCAL
 authentication-attr-from-server secondary
 authenticated-session-username secondary
 default-group-policy default_gpol
 ipv6-address-pool (outside) v6pool
 nat-assigned-to-public-ip outside 
 scep-enrollment enable 
 secondary-authentication-server-group (outside) aaa LOCAL use-primary-username
 secondary-username-from-certificate C CN no-certificate-fallback cert
 username-from-certificate C CN
 strip-group
 strip-realm
tunnel-group tun01 webvpn-attributes
 authentication aaa certificate
 customization DfltCustomization
 dns-group dnsgrp
 group-alias grpalias enable
 group-alias aj disable
 group-url https://blah enable
 nbns-server 10.10.10.10 master timeout 20 retry 8
 nbns-server 10.1.1.1 timeout 2 retry 2
 override-svc-download
 pre-fill-username clientless
 pre-fill-username ssl-client hide
 proxy-auth sdi
 radius-reject-message
 saml identity-provider idp
 secondary pre-fill-username clientless hide
 secondary pre-fill-username ssl-client
 without-csd anyconnect 
tunnel-group tun01 ipsec-attributes
 ikev1 pre-shared-key *****
 chain
 ikev1 client-update type Win9X url https://blah rev-nums 1,3
 ikev1 client-update type WinNT url https://blah rev-nums 1,3
 ikev1 client-update type Windows url https://blah rev-nums 1,3
 ikev1 client-update type mac url https://blah rev-nums 5,9
 ikev1 client-update type linux url https://blah rev-nums 3,5
 ikev1 client-update type vpn3002 url tftp://blah rev-nums 13,15
 ikev1 trust-point trust_point
 ikev1 user-authentication (outside) hybrid
 ikev2 local-authentication certificate cert
 ikev2 local-authentication pre-shared-key
 ikev2 remote-authentication certificate
 ikev2 remote-authentication eap query-identity
 ikev2 remote-authentication pre-shared-key *****
 peer-id-validate nocheck
 radius-with-expiry
tunnel-group tun01 ppp-attributes
 authentication pap
 authentication ms-chap-v2
 authentication eap-proxy
tunnel-group 10.15.20.25 type ipsec-l2l
tunnel-group 10.15.20.25 ipsec-attributes
 ikev1 pre-shared-key *****
tunnel-group 10.20.30.40 type ipsec-l2l
tunnel-group 10.20.30.40 ipsec-attributes
 ikev1 pre-shared-key *****

```

**Help:** execute the command "show running-config tunnel-group"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show nat

**Output:**
```
Manual NAT Policies (Section 1)
1 (any) to (any) source static any any   description source dynamic static destination static net-to-net service any pat-pool interface dns unidirectional no-proxy-arp route-lookup ipv6 inactive description <-- THESE ARE ALL PART OF THE DESCRIPTION
    translate_hits = 505, untranslate_hits = 750
2 (any) to (outside) source dynamic test1 test2   destination static test3 test4 net-to-net inactive description test
    translate_hits = 900, untranslate_hits = 883
3 (any) to (outside) source dynamic test1 test2   destination static test3 test4 service test-service-1 test-service-2
    translate_hits = 826, untranslate_hits = 961
4 (any) to (outside) source dynamic test1 test2   destination static test3 test4 service any test-service-2
    translate_hits = 722, untranslate_hits = 201
5 (any) to (outside) source dynamic test1 pat-pool interface  destination static test3 test4
    translate_hits = 563, untranslate_hits = 48
6 (any) to (outside) source dynamic test1 pat-pool test11  destination static test3 test4
    translate_hits = 997, untranslate_hits = 159
7 (any) to (outside) source dynamic any test2   destination static test3 test4 net-to-net
    translate_hits = 488, untranslate_hits = 313
8 (any) to (outside) source dynamic test1 test2   destination static test3 any
    translate_hits = 606, untranslate_hits = 395
9 (any) to (outside) source static test1 test2   destination static test3 test4 description extended flat include-reserve round-robin dns 169.254.1.1 2006::2/128 <-- THESE ARE ALL PART OF THE DESCRIPTION
    translate_hits = 303, untranslate_hits = 275
 10 (any) to (outside) source static test1 test2   destination static test3 test4 unidirectional no-proxy-arp
    translate_hits = 359, untranslate_hits = 447
 11 (any) to (outside) source static test1 test2   destination static test3 test4 net-to-net inactive description test
    translate_hits = 393, untranslate_hits = 527
12 (any) to (outside) source static test1 test2   destination static test3 test4 service test-service-1 test-service-2
    translate_hits = 327, untranslate_hits = 527
13 (any) to (outside) source static test1 test2   destination static test3 test4 service any test-service-2
    translate_hits = 683, untranslate_hits = 110
14 (any) to (outside) source static test2 test2   destination static test3 test3 no-proxy-arp route-lookup
    translate_hits = 373, untranslate_hits = 811
15 (any) to (outside) source static test1 test1   destination static test3 test3 route-lookup
    translate_hits = 666, untranslate_hits = 609
 16 (any) to (outside) source static any test2   destination static test3 test4 net-to-net
    translate_hits = 263, untranslate_hits = 131
17 (any) to (outside) source static test1 test2   dns unidirectional no-proxy-arp
    translate_hits = 408, untranslate_hits = 436
18 (any) to (outside) source static test1 test2   destination static test3 any
    translate_hits = 892, untranslate_hits = 922
19 (inside) to (outside) source dynamic test1 test2   destination static interface test4
    translate_hits = 142, untranslate_hits = 129
20 (inside) to (outside) source dynamic test1 test2   destination static interface any
    translate_hits = 620, untranslate_hits = 50
21 (inside) to (outside) source dynamic test6 test7   destination static interface ipv6 test9
    translate_hits = 152, untranslate_hits = 359
22 (inside) to (outside) source dynamic test6 interface ipv6   destination static test8 test9
    translate_hits = 214, untranslate_hits = 411
23 (inside) to (outside) source dynamic any interface ipv6   destination static test8 test9
    translate_hits = 341, untranslate_hits = 651
24 (inside) to (outside) source dynamic test1 interface   destination static test3 test4
    translate_hits = 992, untranslate_hits = 255

Auto NAT Policies (Section 2)
1 (any) to (any) source static test11 169.254.11.11   no-proxy-arp route-lookup
    translate_hits = 694, untranslate_hits = 246
2 (inside) to (outside) source static test6 interface ipv6   net-to-net no-proxy-arp
    translate_hits = 655, untranslate_hits = 840
3 (inside) to (outside) source static test7 test8   service tcp ssh 2222
    translate_hits = 680, untranslate_hits = 7
4 (inside) to (outside) source static test9 2006::2/128
    translate_hits = 976, untranslate_hits = 175
5 (any) to (outside) source dynamic test1 169.254.1.1   dns
    translate_hits = 683, untranslate_hits = 761
6 (any) to (outside) source dynamic test2 test3
    translate_hits = 117, untranslate_hits = 939
 7 (any) to (outside) source dynamic test3 pat-pool test11 extended flat include-reserve round-robin dns
    translate_hits = 936, untranslate_hits = 246
8 (any) to (outside) source dynamic test4 pat-pool test11 interface flat round-robin dns
    translate_hits = 383, untranslate_hits = 467
9 (any) to (outside) source dynamic test5 interface   dns
    translate_hits = 795, untranslate_hits = 263
10 (inside) to (outside) source static test7 test8   service udp https 8443
    translate_hits = 680, untranslate_hits = 7
11 (inside) to (outside) source static test7 test8   service sctp www 8080
    translate_hits = 680, untranslate_hits = 7

Manual NAT Policies (Section 3)
1 (any) to (outside) source dynamic test11 test12   destination static test13 test14 net-to-net inactive description source dynamic static destination static net-to-net service any pat-pool interface dns unidirectional no-proxy-arp route-lookup ipv6 inactive description <-- THESE ARE ALL PART OF THE DESCRIPTION
    translate_hits = 687, untranslate_hits = 666
2 (any) to (outside) source dynamic test11 test12   destination static test13 test14 service test-service-1 test-service-2
    translate_hits = 911, untranslate_hits = 47
3 (any) to (outside) source dynamic test11 test12   destination static test13 test14 service any test-service-2
    translate_hits = 651, untranslate_hits = 130
4 (any) to (outside) source dynamic test11 pat-pool interface  destination static test13 test14
    translate_hits = 350, untranslate_hits = 231
5 (any) to (outside) source dynamic test11 pat-pool test21  destination static test13 test14
    translate_hits = 553, untranslate_hits = 961
6 (any) to (outside) source dynamic any test12   destination static test13 test14 net-to-net
    translate_hits = 957, untranslate_hits = 766
7 (any) to (outside) source dynamic test11 test12   destination static test13 any
    translate_hits = 997, untranslate_hits = 468
8 (any) to (outside) source static test11 test12   destination static test13 test14 description extended flat include-reserve round-robin dns 169.254.1.1 2006::2/128 <-- THESE ARE ALL PART OF THE DESCRIPTION
    translate_hits = 622, untranslate_hits = 632
 9 (any) to (outside) source static test11 test12   destination static test13 test14 unidirectional no-proxy-arp
    translate_hits = 425, untranslate_hits = 474
10 (any) to (outside) source static test11 test12   destination static test13 test14 net-to-net inactive description test1
    translate_hits = 99, untranslate_hits = 610
11 (any) to (outside) source static test11 test12   destination static test13 test14 service test-service-1 test-service-2
    translate_hits = 948, untranslate_hits = 144
12 (any) to (outside) source static test11 test12   destination static test13 test14 service any test-service-2
    translate_hits = 386, untranslate_hits = 211
13 (any) to (outside) source static test12 test12   destination static test13 test13 no-proxy-arp route-lookup
    translate_hits = 443, untranslate_hits = 600
14 (any) to (outside) source static test11 test11   destination static test13 test13 route-lookup
    translate_hits = 957, untranslate_hits = 705
15 (any) to (outside) source static any test12   destination static test13 test14 net-to-net
    translate_hits = 171, untranslate_hits = 11
16 (any) to (outside) source static test11 test12   dns unidirectional no-proxy-arp
    translate_hits = 843, untranslate_hits = 956
17 (any) to (outside) source static test11 test12   destination static test13 any
    translate_hits = 302, untranslate_hits = 950
18 (inside) to (outside) source dynamic test11 test12   destination static interface test14
    translate_hits = 662, untranslate_hits = 278
19 (inside) to (outside) source dynamic test11 test12   destination static interface any
    translate_hits = 269, untranslate_hits = 859
20 (inside) to (outside) source dynamic test16 test17   destination static interface ipv6 test19
    translate_hits = 92, untranslate_hits = 257
21 (inside) to (outside) source dynamic test16 interface ipv6   destination static test18 test19
    translate_hits = 97, untranslate_hits = 354
22 (inside) to (outside) source dynamic any interface ipv6   destination static test18 test19
    translate_hits = 780, untranslate_hits = 376
23 (inside) to (outside) source dynamic test11 interface   destination static test13 test14
    translate_hits = 291, untranslate_hits = 3

```

**Help:** execute the command "show nat"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show version

**Output:**
```

Cisco Adaptive Security Appliance Software Version 9.8(3)21 <context>
 Firepower Extensible Operating System Version 2.4(1.103)
Device Manager Version 7.8(2)

Compiled on Tue 07-Aug-18 23:18 PDT by builders

fw002 up 114 days 18 hours
failover cluster up 700 days 16 hours

Hardware:   FPR4K-SM-12
 
License mode: Smart Licensing

Licensed features for this user context:
Failover                          : Active/Active  
Encryption-DES                    : Enabled        
Encryption-3DES-AES               : Enabled        
Carrier                           : Disabled       
AnyConnect Premium Peers          : 0              
Other VPN Peers                   : 500            
AnyConnect for Mobile             : Enabled        
AnyConnect for Cisco VPN Phone    : Enabled        
Advanced Endpoint Assessment      : Enabled        
Cluster                           : Enabled        
              

Failover cluster licensed features for this user context:
Failover                          : Active/Active  
Encryption-DES                    : Enabled        
Encryption-3DES-AES               : Enabled        
Carrier                           : Disabled       
AnyConnect Premium Peers          : 0              
Other VPN Peers                   : 500            
AnyConnect for Mobile             : Enabled        
AnyConnect for Cisco VPN Phone    : Enabled        
Advanced Endpoint Assessment      : Enabled        
Cluster                           : Enabled        

 Configuration last modified by thatperson at 09:15:45.959 EST Mon Dec 12 2018
```

**Help:** execute the command "show version"

**Prompt:**
- cisco_asa>
- cisco_asa#

### show asp drop

**Output:**
```
Frame drop:
  Unsupported IP version (unsupported-ip-version)                            111
  TCP dup of packet in Out-of-Order queue (tcp-dup-in-queue)                 112
  SVC Module unable to fragment packet (mp-svc-no-fragment)                  113
  SVC Module is in flow control (mp-svc-flow-control)                        114
  SVC Module does not have a session (mp-svc-no-session)                     115
  SVC Module does not have a channel for reinjection (mp-svc-no-channel)     116
  NAT-T keepalive message (natt-keepalive)                                   117
  IPSEC tunnel is down (ipsec-tun-down)                                      118
  Dropped pending packets due to a failed attempt to get an internal socket lock (np-socket-lock-failu         61
  Bad IPSEC NATT packet (bad-ipsec-natt)                                     119
  ttl exceeded (ttl-exceeded)                                                  3
  Virtual firewall classification failed (ifc-classify)                        9
  Unable to obtain connection lock (connection-lock)                           1
  TCP replicated flow pak drop (tcp-fo-drop)                                   6
  TCP packet failed PAWS test (tcp-paws-fail)                                  1
  TCP packet SEQ past window (tcp-seq-past-win)                                6
  TCP option list invalid (tcp-bad-option-list)                                2
  TCP invalid ACK (tcp-invalid-ack)                                            1
  TCP global Out-of-Order packet buffer full (tcp-global-buffer-full)         53
  TCP failed 3 way handshake (tcp-3whs-failed)                                76
  TCP data send after FIN (tcp-data-past-fin)                                107
  TCP SYNACK on established conn (tcp-synack-ooo)                           1345
  TCP SEQ in SYN/SYNACK invalid (tcp-seq-syn-diff)                           404
  TCP RST/SYN in window (tcp-rst-syn-in-win)                                  30
  TCP RST/FIN out of order (tcp-rstfin-ooo)                                12678
  TCP Out-of-Order packet buffer timeout (tcp-buffer-timeout)                 45
  TCP Out-of-Order packet buffer full (tcp-buffer-full)                      328
  TCP Dual open denied (tcp-dual-open)                                         6
  TCP ACK in SYNACK invalid (tcp-ack-syn-diff)                               130
  Slowpath security checks failed (sp-security-failed)                        79
  Reverse-path verify failed (rpf-violated)                                 1083
  Received a multicast packet in the non-active device (mcast-in-nonactive-device)                           4063
  RM connection rate limit reached (rm-conn-rate-limit)                       24
  Punt no memory (punt-no-mem)                                              1150
  Packet shunned (shunned)                                                     8
  No valid adjacency (no-adjacency)                                            8
  No route to host (no-route)                                                 30
  NAT failed (nat-xlate-failed)                                                1
  Layer 3 protocol of the packet is not IP (cluster-non-ip-pkt)               41
  Invalid encapsulation (invalid-encap)                                        1
  Invalid UDP Length (invalid-udp-length)                                      6
  Invalid TCP Length (invalid-tcp-hdr-length)                                  4
  Invalid LU packet (lu-invalid-pkt)                                           2
  Invalid IP length (invalid-ip-length)                                      166
  Invalid IP header (invalid-ip-header)                                      209
  Interface is down (interface-down)                                         169
  Intercept unexpected packet (intercept-unexpected)                           4
  IP option drop (invalid-ip-option)                                           3
  ICMP Inspect seq num not matched (inspect-icmp-seq-num-not-matched)         45
  ICMP Inspect bad icmp code (inspect-icmp-bad-code)                          32
  ICMP Error Inspect no existing conn (inspect-icmp-error-no-existing-conn)                                    13
  Flow is denied by configured rule (acl-drop)                              2077
  Flow is being freed (flow-being-freed)                                       4
  Flow denied due to resource limitation (unable-to-create-flow)               1
  First TCP packet not SYN (tcp-not-syn)                                     205
  Failed to fetch the trailer of the packet (cluster-bad-trailer)            309
  FP L2 rule drop (l2_acl)                                                   150
  Expired flow (flow-expired)                                                 10
  Early security checks failed (security-failed)                              34
  Dropped pending packets in a closed socket (np-socket-closed)                3
  Dropped by standby unit (fo-standby)                                         5
  Dispatch queue tail drops (dispatch-queue-limit)                           770
  DNS Inspect packet too long (inspect-dns-pak-too-long)                       9
  DNS Inspect invalid packet (inspect-dns-invalid-pak)                        61
  DNS Inspect invalid domain label (inspect-dns-invalid-domain-label)          9
  DNS Inspect id not matched (inspect-dns-id-not-matched)                      6
  Core local block alloc failure (dispatch-block-alloc)                      980
  Connection to PAT address without pre-existing xlate (nat-no-xlate-to-pat-pool)                              50
  Connection limit reached (conn-limit)                                       18
  Cluster packet rcvd over CCL, unit has stub flow and unknown role (cluster-ccl-unknown-stub)               9026
  Cluster packet rcvd over CCL, unit has no flow and unknown role (cluster-ccl-unknown)                    185782
  Cluster packet rcvd over CCL on backup (cluster-ccl-backup)              21121
  CTM returned error (ctm-error)                                              22
  Bad TCP flags (bad-tcp-flags)                                               50
  Async lock queue limit exceeded (async-lock-queue-limit)                  4926

Last clearing: Never

Flow drop:
  VPN overlap conflict (vpn-overlap-conflict)                                201
  VPN decryption missing (vpn-missing-decrypt)                               202
  SVC replacement connection established (svc-replacement-conn)              203
  SVC inner policy mismatch failure (svc-selector-failure)                   204
  SVC failover (svc-failover)                                                205
  SSL record decryption failed (ssl-record-decrypt-error)                    206
  DTLS hello processed and closed (dtls-hello-close)                          90
  CTM crypto request error (ctm-crypto-request-error)                        187
  VPN handle not found (vpn-handle-not-found)                                 20
  NP socket data movement failure (np-socket-data-move-failure)               10
  SSL handshake failed (ssl-handshake-failed)                               2181
  SSL bad record detected (ssl-bad-record-detect)                              1
  No memory to complete flow (out-of-memory)                                   2
  NAT reverse path failed (nat-rpf-failed)                                    16
  Inspection failure (inspect-fail)                                            4
  Flow shunned (shunned)                                                       2
  Flow removed, packet sent to owner (cluster-redirect)                      576
  Flow is denied by access rule (acl-drop)                                192350

```

**Help:** execute the command "show asp drop"

**Prompt:**
- cisco_asa>
- cisco_asa#

