# ericsson_ipos


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
- ericsson_ipos>

### show arp

**Output:**
```
Context   :local                          Context id  : 0x40080001
 ------------------------------------------------------------------
Total number of arp entries in cache: 4
  Resolved entry   : 4
  Incomplete entry : 0

Host              Hardware address    Ttl    Type  Circuit
10.10.10.224      98:a4:04:a2:d8:6a   1380   ARPA  1/9
10.10.10.225      98:a4:04:a2:dc:e9   -      ARPA  1/9
10.10.10.226      98:a4:04:a2:dc:ea   -      ARPA  1/10
10.10.10.227      f8:0f:6f:77:eb:0c   1593   ARPA  1/10

Context   :Abis_IP                        Context id  : 0x40080002
------------------------------------------------------------------
 Total number of arp entries in cache: 2
  Resolved entry   : 2
  Incomplete entry : 0

Host              Hardware address    Ttl    Type  Circuit
10.10.10.33       98:a4:04:a2:dc:e5   -      ARPA  1/5 vlan-id 211
10.10.10.34       34:00:a3:4c:7e:2c   3502   ARPA  1/5 vlan-id 211

Context   :Inband-RTN                     Context id  : 0x40080003
------------------------------------------------------------------
 Total number of arp entries in cache: 2
  Resolved entry   : 2
  Incomplete entry : 0

Host              Hardware address    Ttl    Type  Circuit
10.10.10.173      ec:38:8f:6f:91:68   3197   ARPA  1/5 vlan-id 3976
10.10.10.174      98:a4:04:a2:dc:e5   -      ARPA  1/5 vlan-id 3976

Context   :IuB_UP                         Context id  : 0x40080004
------------------------------------------------------------------
 Total number of arp entries in cache: 2
  Resolved entry   : 2
  Incomplete entry : 0

Host              Hardware address    Ttl    Type  Circuit
10.10.10.97       98:a4:04:a2:dc:e5   -      ARPA  1/5 vlan-id 311
10.10.10.98       34:00:a3:4c:7e:2c   1730   ARPA  1/5 vlan-id 311

Context   :LTE-S1X2                       Context id  : 0x40080005
------------------------------------------------------------------
 Total number of arp entries in cache: 2
  Resolved entry   : 2
  Incomplete entry : 0

Host              Hardware address    Ttl    Type  Circuit
10.10.10.161      98:a4:04:a2:dc:e5   -      ARPA  1/5 vlan-id 411
10.10.10.162      34:00:a3:4c:7e:2c   1259   ARPA  1/5 vlan-id 411

Context   :OM-HWI                         Context id  : 0x40080006
------------------------------------------------------------------
 Total number of arp entries in cache: 2
  Resolved entry   : 2
  Incomplete entry : 0

Host              Hardware address    Ttl    Type  Circuit
10.10.10.225      98:a4:04:a2:dc:e5   -      ARPA  1/5 vlan-id 1051
10.10.10.226      34:00:a3:4c:7e:2c   249    ARPA  1/5 vlan-id 1051

Context   :OM-Power                       Context id  : 0x40080007
------------------------------------------------------------------
 Total number of arp entries in cache: 2
  Resolved entry   : 2
  Incomplete entry : 0

Host              Hardware address    Ttl    Type  Circuit
10.10.10.161      98:a4:04:a2:dc:e5   -      ARPA  1/5 vlan-id 3911
10.10.10.162      00:20:85:ef:bb:aa   2657   ARPA  1/5 vlan-id 3911

```

**Help:** execute the command "show arp"

**Prompt:**
- ericsson_ipos>
- ericsson_ipos#

### show isis adjacency

**Output:**
```
IS-IS Adjacenc(ies) for tag XL:
SystemId        Interface          L  MT   Stat Hold   SNPA            Uptime
MA-BJC547-01    Virtual_Interface_ 2p U    Up   29     41de.24a3.1e8d  04d20h01
MA-BMCI75-01    Virtual_Interface_ 2p U    Up   22     7d7e.b92a.670c  04d20h01
C-BJAHY-01      Virtual_Interface_ 1p U    Up   22     801a.8811.f1a4  04d20h01
0102.1905.0009  Virtual_Interface_ 3p U    Up   23     9aac.0480.2d1a  04d20h01

Total IS-IS Adjacenc(ies):   4

```

**Help:** execute the command "show isis adjacency"

**Prompt:**
- ericsson_ipos>
- ericsson_ipos#

### show version

**Output:**
```

Ericsson IPOS Version IPOS-v20.3.1.803.142-Release
Built by spradmin@ericsson Tue Dec 15 12:49:29 CET 2020
Copyright (C) 1998-2020, Ericsson AB. All rights reserved.
Operating System version is Linux 3.14.65-mvista
System Bootstrap version is CXC1740316_1-R11A01(K0000I0000)
There is no minikernel currently installed
Secure Boot mode: PRODUCTION
Minimal Key Revision is 0, images have 0
Minimal Security Revision is 0, images have 0
Kernel version is Linux-3.14-CXC1740317_1-R11A02(K0000I0000)
 Golden Bootstrap version is CXC1740316_1-R1A08(KFFFFIFFFF)
Golden SBI version is CXC1740314_1-R1A03
Primary SBI version is CXC1740314_1-R11A01(K0000I0000)
 FPGA version is CXC 174 0318/2  -R5C07
CHIMP version is 1.0

slad / mloam-service-layer component version: 0.0.0
Built by nobody Sat Jan 1 00:00:00 UTC 2000
Copyright (C) 1998-2020, Ericsson AB. All rights reserved.
Router Up Time -  10 hours 48 minutes 41 seconds

```

**Help:** execute the command "show version"

**Prompt:**
- ericsson_ipos>
- ericsson_ipos#

### terminal length 0

**Output:** None

**Help:** Execute the command terminal length 0. This automatically generated. Feel free to change it!

**Prompt:**
- ericsson_ipos>
- ericsson_ipos#

### terminal width 512

**Output:** None

**Help:** Execute the command terminal width 512. This automatically generated. Feel free to change it!

**Prompt:**
- ericsson_ipos>
- ericsson_ipos#

### show curpriv

**Output:** None

**Help:** Execute the command show curpriv. This automatically generated. Feel free to change it!

**Prompt:**
- ericsson_ipos>
- ericsson_ipos#

### set cli screen-width 511

**Output:** None

**Help:** Execute the command set cli screen-width 511. This automatically generated. Feel free to change it!

**Prompt:**
- ericsson_ipos>
- ericsson_ipos#

### terminal width 511

**Output:** None

**Help:** Execute the command terminal width 511. This automatically generated. Feel free to change it!

**Prompt:**
- ericsson_ipos>
- ericsson_ipos#

### enable clipaging

**Output:** None

**Help:** Execute the command enable clipaging. This automatically generated. Feel free to change it!

**Prompt:**
- ericsson_ipos>
- ericsson_ipos#

### login

**Output:** None

**Help:** Execute the command login. This automatically generated. Feel free to change it!

**Prompt:**
- ericsson_ipos>
- ericsson_ipos#

