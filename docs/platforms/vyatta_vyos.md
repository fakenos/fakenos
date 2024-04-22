# vyatta_vyos


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
- vyatta@vyatta:~$

### set terminal length 0

**Output:**
```
set terminal length 0
```

**Help:** set the terminal to max width

**Prompt:**
- vyatta@vyatta:~$
- vyatta@vyatta#

### show interfaces

**Output:**
```
Codes: S - State, L - Link, u - Up, D - Down, A - Admin Down
Interface        IP Address                        S/L  Description
---------        ----------                        ---  -----------
eth0             -                                 u/u  
eth0.40          123.123.120.123/27                u/u  OUTSIDE 
eth1             -                                 u/u  
eth1.204         123.123.123.81/28                 u/u  CUST-DS-LAN 
eth1.269         172.18.32.14/28                   u/u  CUST-COM 
                 123.123.123.123/32
eth1.437         123.123.116.169/29                u/u  CUST-VIDEO 
eth1.1753        172.18.161.196/29                 u/u  SERVICE-LINK 
eth2             -                                 u/u  
lo               127.0.0.1/8                       u/u  
                 172.18.255.110/32
                 ::1/128
vtun0            192.168.80.2                      u/u  
vtun1            192.168.80.4                      u/u   OpenVPN-TUNNEL1
vtun2            192.168.80.6                      u/u  


```

**Help:** execute the command "show interfaces"

**Prompt:**
- vyatta@vyatta:~$
- vyatta@vyatta#

### show arp

**Output:**
```
Address                  HWtype  HWaddress           Flags Mask            Iface
10.123.254.20            ether   9c:8e:99:fa:15:0a   C                     eth1.1230
123.12.120.44            ether   11:22:33:aa:02:90   C                     eth0.42
123.12.120.218                   (incomplete)                              eth1.1234
10.123.254.21            ether   00:0c:29:59:94:56   C                     eth1.1230
123.12.120.219                   (incomplete)                              eth1.1234
123.12.120.57            ether   11:22:33:aa:65:bb   C                     eth0.42

```

**Help:** execute the command "show arp"

**Prompt:**
- vyatta@vyatta:~$
- vyatta@vyatta#

### show ip bgp summary

**Output:**
```
IPv4 Unicast Summary:
BGP router identifier 10.10.10.1, local AS number 123456 vrf-id 0
BGP table version 50711224
RIB entries 1537189, using 270 MiB of memory
Peers 3, using 593 KiB of memory
Peer groups 4, using 256 bytes of memory

Neighbor        V         AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
10.10.10.10     4       1234   71460   69353        0    0    0 5d13h10m            0
123.123.123.123 4     345612  450590   34688        0    0    0 1d00h18m            0
193.189.82.105  4     12365        0       0        0    0    0    never       Active

Total number of neighbors 3

```

**Help:** execute the command "show ip bgp summary"

**Prompt:**
- vyatta@vyatta:~$
- vyatta@vyatta#

