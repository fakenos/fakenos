# zyxel_os


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
- zyxel_os>

### ex

**Output:**
```
True
```

**Help:** exit the terminal

**Prompt:**
- zyxel_os>
- zyxel_os#

### sys atsh

**Output:**
```
Firmware Version        : V5.13(AAXA.8)C0
Bootbase Version        : V1.61 | 05/25/2018 17:08:36
Vendor Name             : Zyxel Communications Corp.
Product Model           : VMG1312-B10D
Serial Number           : S182E47002040
 First MAC Address       : 8C5973AE89B0
Last MAC Address        : 8C5973AE89BB
 MAC Address Quantity    : 12
Default Country Code    : FF
Boot Module Debug Flag  : 00
Kernel Checksum         : 00008FE8
RootFS Checksum         : 00009ACC
 Romfile Checksum        : 00000E1D
Main Feature Bits       : 00
Other Feature Bits      :
7f9f2a9c: 04050202 ffffffff ffffffff ffffffff
7f9f2aac: ffffffff ffffffff ffffffff ffff

```

**Help:** execute the command "sys atsh"

**Prompt:**
- zyxel_os>
- zyxel_os#

### cfg ipalias get

**Output:**
```
handlerName=ethwanlan method=GET i=2
This device do not support Ethernet LAN4 port change to WAN port.                IP Alias Setup                             Public LAN
Group Name      Active     IPv4 Arrdess    Subnet mask     Active     IPv4 Arrdess    Subnet mask     Offer Public IP by DHCP   Enable ARP Proxy
Default         0          N/A             N/A             1          100.200.77.111  255.255.255.252 0                         0
LAN VOIX        0          N/A             N/A             0          N/A             N/A             0                         0
2e65ed5d-d      1          192.168.180.1   255.255.255.0   0          N/A             N/A             0                         0                   
Command Successful.

```

**Help:** execute the command "cfg ipalias get"

**Prompt:**
- zyxel_os>
- zyxel_os#

### cfg snmp get

**Output:**
```
SNMP Agent          : Enabled
Get Community       : Monitoring
Set Community       : Monitoring
Trap Community      : public
System Name         : paris-stella-customer-child-site
System Location     : Paris
System Contact      :
Domain Name         : home
Trap Destination    :
Command Successful.

```

**Help:** execute the command "cfg snmp get"

**Prompt:**
- zyxel_os>
- zyxel_os#

### cfg intf group get

**Output:**
```
Index  Name         WAN Interface                       LAN Interfaces                                          Criteria                            
1      datas        Any WAN                             LAN2,LAN4,LAN3,LAN4,magic 2000,ZyXEL_8B91_guest1,ZyXEL_8B91_guest2,ZyXEL_8B91_guest3 N/A                                 
2      zzefzef      WWAN,VDSL                           N/A                                                     vlangroup<datas>                    
3      qsdq sdqsdqsd ADSL                                N/A                                                     op61<efsdfsdf>;op60<qs qsd>;mac<AA-AA-AA-AA-AA-AA,AA-BB-BB-BB-BB-BB> 
Command Successful.

```

**Help:** execute the command "cfg intf group get"

**Prompt:**
- zyxel_os>
- zyxel_os#

### cfg static dhcp get

**Output:**
```
Index      Status     Mac Address                    IP Address
1          1          eb:fa:ae:cf:34:15              192.168.1.25
2          1          bb:aa:ee:ff:32:12              192.168.1.13
3          1          aa:cc:bb:ee:43:21              192.168.1.1
Command Successful.

```

**Help:** execute the command "cfg static dhcp get"

**Prompt:**
- zyxel_os>
- zyxel_os#

### cfg firewall acl get

**Output:**
```
Index  Enable Order  Name          Source IP                                 Destination IP                            Service                                  Action      
1      true   6      Acces Bureau  85.14.167.234/32                          Any/32                                    ALL                                      Accept      
2      true   5      Eqinoxe_1     185.48.253.0/27                           Any/32                                    ALL                                      Accept      
3      true   4      Eqinoxe_2     185.48.254.0/28                           Any/32                                    ALL                                      Accept      
4      true   3      Eqinoxe_3     185.163.212.48/28                         Any/32                                    ALL                                      Accept      
5      true   2      Eqinoxe_4     185.163.212.64/28                         Any/32                                    ALL                                      Accept      
6      true   1      Eqinoxe_5     185.197.109.16/28                         Any/32                                    ALL                                      Accept      
7      true   7      DMZ0          Any/32                                    23.90.230.192/29                          ALL                                      Accept      
Command Successful.

```

**Help:** execute the command "cfg firewall acl get"

**Prompt:**
- zyxel_os>
- zyxel_os#

### cfg static route get

**Output:**
```
Index      Name       Enable  IPver   DestIPAddress/DestPrefix                      DestMask          Interface       Gateway/NextHop
1          5473a28e-8 0       IPv4    177.41.30.228                                 255.255.255.0     ADSL                      
2          d6e181ce-a 0       IPv4    121.160.211.188                               255.255.0.0       ADSL            66.135.158.175
3          b1a49337-a 0       IPv4    43.188.51.10                                  255.255.0.0       WWAN            221.29.200.232
4          f9ed53d7-5 1       IPv4    101.168.102.179                               255.255.255.0     ADSL            222.173.23.26
5          b7feec47-b 1       IPv4    72.37.37.55                                   255.0.0.0         VDSL                      
6          facf6dd5-a 0       IPv4    59.38.164.29                                  255.0.0.0         VDSL                      
7          3ab0c611-b 0       IPv6    6d78:60da:1b22::/47                                             ADSL            6185:f0a7:164e:7fe3:8549:dfb3:dda5:f330
8          f5f679b4-c 0       IPv6    aff9:c5d3:877d:8276:c5d9:dbc1:8000:0/97                         WWAN                      
9          723130e9-a 1       IPv6    51f2:794e:7305:2a0f:1a80::/73                                   WWAN            e583:cfd7:c872:94b4:e9af:a5f8:b095:a058
10         bd7e5ad3-9 0       IPv6    7ec0::/10                                                       ADSL            1aa8:fc25:8d13:67ac:4740:fdd1:61fd:1f81
Command Successful.

```

**Help:** execute the command "cfg static route get"

**Prompt:**
- zyxel_os>
- zyxel_os#

### cfg wlan get

**Output:**
```
Index   Band     SSID                                Enable     Bandwidth  Channel    MaxDevices   SecurityMode         PskValue            
1       2.4GHz   magic 2000$&                        1          40MHz      Auto       32           WPA2-Personal        TestTest        
2       2.4GHz   ZyXEL_8B91_guest1                   0          40MHz      Auto       16           WPA2-Personal        TestTest          
3       2.4GHz   ZyXEL_8B91_guest2                   0          40MHz      Auto       16           WPA2-Personal        TestTest          
4       2.4GHz   ZyXEL_8B91_guest3                   0          40MHz      Auto       16           WPA2-Personal        TestTest          
5       5GHz     magic 2000$&                        0          80MHz      Auto       32           WPA2-Personal        TestTest        
6       5GHz     ZyXEL_8B91_guest1                   0          80MHz      Auto       16           WPA2-Personal        TestTest          
7       5GHz     ZyXEL_8B91_guest2_5G                0          80MHz      Auto       16           WPA2-Personal        TestTest          
8       5GHz     ZyXEL_8B91_guest3_5G                0          80MHz      Auto       16           WPA2-Personal        TestTest          
Command Successful.

```

**Help:** execute the command "cfg wlan get"

**Prompt:**
- zyxel_os>
- zyxel_os#

### cfg nat addr map get

**Output:**
```
Index MappingRuleName Interface       Type            LocalStartIP    LocalEndIP      GlobalStartIP   GlobalEndIP    
1     DMZ0            ADSL            One-to-One      100.95.11.86                    100.95.11.86                   
2     plop            VDSL            Many-to-Many    192.168.1.1     192.168.1.2     5.5.5.5         5.5.5.6        
3     plop number 2   WWAN            Many-to-One     192.168.2.1     192.168.2.2     5.5.5.5                        
Command Successful.

```

**Help:** execute the command "cfg nat addr map get"

**Prompt:**
- zyxel_os>
- zyxel_os#

### cfg lan get

**Output:**
```
Group Name      LAN IP Address       IPv4 DHCP Server     IPv6 Enable
Default                              Disable              false
LAN VOIX        192.168.72.253       Disable              false
Command Successful.

```

**Help:** execute the command "cfg lan get"

**Prompt:**
- zyxel_os>
- zyxel_os#

### cfg lan get --Name name

**Output:**
```
Group Name      lan_1
IP Address      192.168.1.1
Subnet Mask     255.255.255.0
DHCP            Enable
   Beginning IP Address      192.168.1.10
   Ending IP Address         192.168.1.150
   AutoReserveLanIp          false
   DHCP Server Lease Time    1 Days 0 Hours 0 Minutes
   DNS Values      Static
IPv6 Active     false
Command Successful.

```

**Help:** execute the command "cfg lan get --Name name"

**Prompt:**
- zyxel_os>
- zyxel_os#

### cfg lanhosts get

**Output:**
```
Name                 IP Address        IPv6 Address                   MAC Address          Address Source   Connection Type
device1              192.168.45.65     af:35::25:c7:28                01:23:45:67:89:AB    15.65.85.0.1     Wired 
Command Successful.

```

**Help:** execute the command "cfg lanhosts get"

**Prompt:**
- zyxel_os>
- zyxel_os#

### zycli Ethctl media-type

**Output:**
```
Auto-negotiation enabled.
The autonegotiated media type is Auto Full Duplex
Link is down

```

**Help:** execute the command "zycli Ethctl media-type"

**Prompt:**
- zyxel_os>
- zyxel_os#

### cfg nat get

**Output:**
```
Index Description     Enable  Originating IP  Server IP Address WAN Interface   Start Port End Port   Translation Start Port    Translation End Port      Protocol
1     rabbitmq0       0       185.24.67.123   192.168.1.13      ADSL            15672      15672      15672                     15672                     ALL
2     website0        1       N/A             192.168.1.25      ADSL            80         80         8080                      8080                      ALL
3     phone-udp0      1       34.32.21.43     192.168.1.1       ADSL            4433       4433       433                       433                       UDP
4     phone-udp1      1       45.21.54.76     192.168.1.1       ADSL            4433       4433       433                       433                       UDP
5     phone-udp2      1       21.78.99.34     192.168.1.1       ADSL            4433       4433       433                       433                       UDP
6     phone-udp3      1       185.24.67.123   192.168.1.1       ADSL            4433       4433       433                       433                       UDP
7     phone-tcp0      1       N/A             192.168.1.1       ADSL            8080       8080       80                        80                        TCP
Command Successful.

```

**Help:** execute the command "cfg nat get"

**Prompt:**
- zyxel_os>
- zyxel_os#

