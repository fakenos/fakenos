# huawei_smartax

## Platforms:
-  [Huawei OptiXaccess MA5800](
https://e.huawei.com/es/products/optical-access/ma5800)
-  [Huawei SmartAX MA5801-FL16](
https://e.huawei.com/es/products/optical-access/ma5801-fl16)
-  [Huawei OptiXaccess EA5801S-FL16](
https://e.huawei.com/es/products/optical-access/optixaccess-ea5801s-fl16)
-  [Huawei OptiXaccess EA5801E-FL16](
https://e.huawei.com/es/products/optical-access/optixaccess-ea5801e-fl16)
-  [Huawei OptiXaccess EA5801E-GP16](
https://e.huawei.com/es/products/optical-access/optixaccess-ea5801e)
-  [Huawei OptiXaccess EA5801E-GP04](
https://e.huawei.com/es/products/optical-access/optixaccess-ea5801e-gp04)
-  [Huawei OptiXaccess EA5801E-GP08](
https://e.huawei.com/es/products/optical-access/optixaccess-ea5801e-gp08)
-  [Huawei OptiXaccess EA5800](
https://e.huawei.com/es/products/optical-access/ea5800)
-  [Huawei OptiXaccess S1016-L](
https://e.huawei.com/es/products/optical-access/optixaccess-s1016-l)

## Commands

### enable

**Output:** None

**Help:** enter enable mode

**Prompt:**

- huawei_smartax>

### undo smart

**Output:** None

**Help:** undo the command completion mode (smart mode)

**Prompt:**

- huawei_smartax>
- huawei_smartax#

### scroll

**Output:** None

**Help:** disables the paging so the output is complete always

**Prompt:**

- huawei_smartax>
- huawei_smartax#

### display cpu

**Output:**
```
  CPU occupancy: 17%
```

**Help:** execute the command "display cpu"

**Prompt:**

- huawei_smartax>
- huawei_smartax#

### display board

**Output:**
```
  -------------------------------------------------------------------------
  SlotID  BoardName  Status          SubType0 SubType1    Online/Offline
  -------------------------------------------------------------------------
  0       A123ABCD   Normal                           
  1     
  2       A123ABCDE  Normal                           
  3       A123ABCDE  Active_normal   CPCF             
  4       A123ABCDE  Standby_failed  CPCF                 Offline  
  5     
  -------------------------------------------------------------------------
```

**Help:** execute the command "display board"

**Prompt:**

- huawei_smartax>
- huawei_smartax#

### display version

**Output:**
```

  VERSION : AB1234C342A123D23
  PATCH   : QEF227
  PRODUCT : MA5608T
 
  Active Mainboard Running Area Information: 
  --------------------------------------------------
  Current Program Area : Area A 
  Current Data Area : Area A
 
  Program Area A Version : AB1234C342A123D23 
  Program Area B Version : AB1234C342A123D23
 
  Data Area A Version : AB1234C342A123D23 
  Data Area B Version : AB1234C342A123D23 
  --------------------------------------------------
 
  Standby Mainboard Running Area Information: 
  --------------------------------------------------
  Current Program Area : Area A 
  Current Data Area : Area A
 
  Program Area A Version : AB1234C342A123D23 
  Program Area B Version : AB1234C342A123D23
 
  Data Area A Version : AB1234C342A123D23 
  Data Area B Version : AB1234C342A123D23 
  --------------------------------------------------
 
  Uptime is 20 day(s), 23 hour(s), 19 minute(s), 16 second(s)
```

**Help:** execute the command "display version"

**Prompt:**

- huawei_smartax>
- huawei_smartax#

### display sysman service state

**Output:**
```
  ---------------------------------------------------------------------------
  Network service                                   Port           State
  ---------------------------------------------------------------------------
  telnet                                            23             disable
  trace                                             1026           disable
  ssh                                               22             enable
  snmp                                              161            enable
  ftp-client                                        ----           ----
  sftp-client                                       ----           ----
  ntp                                               123            enable
  radius                                            ----           enable
  dhcp-relay                                        67             disable
  dhcpv6-relay                                      547            disable
  ntp6                                              123            disable
  ipdr                                              4737           enable
  twamp                                             4294967295     enable
  netconf                                           830            enable
  telnetv6                                          23             disable
  sshv6                                             22             disable
  snmpv6                                            161            disable
  web-proxy                                         8024           disable
  portal                                            2000           disable
  capwap                                            5246           disable
  ---------------------------------------------------------------------------

```

**Help:** execute the command "display sysman service state"

**Prompt:**

- huawei_smartax>
- huawei_smartax#

### display ont info summary ont

**Output:**
```
  ------------------------------------------------------------------------------
  In port 0/1/0, the total of ONTs are: 23, online: 23
  ------------------------------------------------------------------------------
  ONT  Run     Last                Last                Last
  ID   State   UpTime              DownTime            DownCause
  ------------------------------------------------------------------------------
  0    online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  1    online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  2    online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  3    online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  4    online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  5    online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  6    online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  7    online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  8    online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  9    online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  10   online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  11   online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  12   online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  13   online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  14   online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  15   online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  16   online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  17   online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  18   online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  19   online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  20   online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  21   online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  22   online  2000-01-01 00:00:00 2000-01-01 00:00:00 LOSi/LOBi
  ------------------------------------------------------------------------------
  ONT        SN        Type          Distance Rx/Tx power  Description
  ID                                    (m)      (dBm)
  ------------------------------------------------------------------------------
  0   1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  1   1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  2   1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  3   1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  4   1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  5   1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  6   1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  7   1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  8   1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  9   1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  10  1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  11  1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  12  1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  13  1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  14  1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  15  1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  16  1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  17  1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  18  1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  19  1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  20  1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  21  1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  22  1234567890ABCDEF AB1234C5         100   -10.12/2.03  AB12
  ------------------------------------------------------------------------------
```

**Help:** execute the command "display ont info summary ont"

**Prompt:**

- huawei_smartax>
- huawei_smartax#

### display port info

**Output:**
```
  -----------------------------------------------------------
  F/S/P                                      0/0/0
  Min distance(km)                           0
  Max distance(km)                           20
  Max guaranteed bandwidth(kbps)             -
  Left guaranteed bandwidth(kbps)            1000000
  Number of T-CONTs                          0
  Autofind                                   Enable
  FEC check                                  Disable
  Admin State                                On
  ONT encryption key switching interval(m)   1440
  PON-ID switch                              Disable
  PON-ID identifier                          1
  Jumbo frame switch                         Disable
  Port MTU(bytes)                            1024
  Surplus bandwidth assignment               Disable
  Best-effort bandwidth assignment           -
  Traffic alarm-profile ID                   -
  ONT online power threshold(dBm)            -
  Low-latency                                no
  Multichannel low latency                   Disable
  Optical module work mode                   Standard
  -----------------------------------------------------------
  Channel 0 Information              
  -----------------------------------------------------------
  Channel Type                               GPON
  Online ONT number threshold                Disable
  -----------------------------------------------------------
```

**Help:** execute the command "display port info"

**Prompt:**

- huawei_smartax>
- huawei_smartax#

### display ont autofind

**Output:**
```
   ----------------------------------------------------------------------------
   Number              : 1
   F/S/P               : 0/0/0
   Ont SN              : 12345678A12BC3AB (ABCD-A12BC3DE)
   Password            : 0x00000000000000000000
   Loid                :
   Checkcode           :
   VendorID            : HWTC
   Ont Version         : 1234A.D
   Ont SoftwareVersion : A1B123D12E123
   Ont EquipmentID     : EG8145X6-10
   Ont Customized Info : EUCOMMONEBG4
   Ont MAC             : 1234-ABCD-1234
   Ont Equipment SN    : 123456789ABCDEFGHIJK
   Ont autofind time   : 2000-01-01 00:00:00+00:00
   Multi channel       : -
   ----------------------------------------------------------------------------
```

**Help:** execute the command "display ont autofind"

**Prompt:**

- huawei_smartax>
- huawei_smartax#

### display ont info by-sn sn

**Output:**
```
  -----------------------------------------------------------------------------
  F/S/P                   : 0/1/1
  ONT-ID                  : 131
  Control flag            : active
  Run state               : online
  Config state            : normal
  Match state             : match
  DBA type                : SR
  ONT distance(m)         : 100
  ONT last distance(m)    : 100
  ONT battery state       : not support
  ONT power type          : -
  Memory occupation       : 23%
  CPU occupation          : 30%
  Temperature             : 70(C)
  Authentic type          : SN-auth
  SN                      : 123456789123AB12AB (HWTC-12AB12AB)
  Management mode         : OMCI
  Software work mode      : normal
  Isolation state         : normal
  ONT IP 0 address/mask   : 192.168.0.1/24
  ONT IP 1 address/mask   : 192.168.0.1/24
  Description             : ABCD
  Last down cause         : dying-gasp
  Last up time            : 09/02/2019 01:58:52+00:00
  Last down time          : 22/01/2019 01:57:55+00:00
  Last dying gasp time    : 22/01/2019 01:57:55+00:00
  Last restart reason     : -
  ONT online duration     : 22 day(s), 1 hour(s), 23 minute(s), 23 second(s) 
  ONT system up duration  : 22 day(s), 1 hour(s), 23 minute(s), 23 second(s) 
  Type C support          : Not support
  Interoperability-mode   : ITU-T
  Power reduction status  : -
  FEC upstream state      : use-profile-config
  VS-ID                   : 0
  VS name                 : admin-vs
  Global ONT-ID           : 131
  -----------------------------------------------------------------------------
  VoIP configure method   : Default
  -----------------------------------------------------------------------------
  Line profile ID      : 100
  Line profile name    : ftth
  -----------------------------------------------------------------------------
  FEC upstream switch :Disable 
  OMCC encrypt switch :On
  Qos mode            :PQ
  Mapping mode        :VLAN
  TR069 management    :Enable        
  TR069 IP index      :0
  ------------------------------------------------------------------------------
  Notes: * indicates Discrete TCONT(TCONT Unbound)
  ------------------------------------------------------------------------------
  <T-CONT   0>          DBA Profile-ID:1
  <T-CONT   1>          DBA Profile-ID:100
   <Gem Index 1>
   --------------------------------------------------------------------
   |Serv-Type:ETH |Encrypt:on  |Cascade:off |GEM-CAR:-            |
   |Upstream-priority-queue:0  |Downstream-priority-queue:-       |
   --------------------------------------------------------------------
    Mapping VLAN  Priority Port    Port  Bundle  Flow  Transparent
    index                  type    ID    ID      CAR   
   --------------------------------------------------------------------
    0       40    -        -       -     -       -     -          
    1       41    -        -       -     -       -     -          
   --------------------------------------------------------------------
  <T-CONT   2>          DBA Profile-ID:101
   <Gem Index 2>
   --------------------------------------------------------------------
   |Serv-Type:ETH |Encrypt:on  |Cascade:off |GEM-CAR:-            |
   |Upstream-priority-queue:0  |Downstream-priority-queue:-       |
   --------------------------------------------------------------------
    Mapping VLAN  Priority Port    Port  Bundle  Flow  Transparent
    index                  type    ID    ID      CAR   
   --------------------------------------------------------------------
    0       42    -        -       -     -       -     -          
   --------------------------------------------------------------------
  <T-CONT   3>          DBA Profile-ID:102
   <Gem Index 3>
   --------------------------------------------------------------------
   |Serv-Type:ETH |Encrypt:on  |Cascade:off |GEM-CAR:-            |
   |Upstream-priority-queue:0  |Downstream-priority-queue:-       |
   --------------------------------------------------------------------
    Mapping VLAN  Priority Port    Port  Bundle  Flow  Transparent
    index                  type    ID    ID      CAR   
   --------------------------------------------------------------------
    0       1     -        -       -     -       -     -          
    1       2     -        -       -     -       -     -          
    2       3     -        -       -     -       -     -          
    3       4     -        -       -     -       -     -          
   --------------------------------------------------------------------
  <T-CONT   4>          DBA Profile-ID:103
   <Gem Index 4>
   --------------------------------------------------------------------
   |Serv-Type:ETH |Encrypt:on  |Cascade:off |GEM-CAR:-            |
   |Upstream-priority-queue:0  |Downstream-priority-queue:-       |
   --------------------------------------------------------------------
    Mapping VLAN  Priority Port    Port  Bundle  Flow  Transparent
    index                  type    ID    ID      CAR   
   --------------------------------------------------------------------
    0       8     -        -       -     -       -     -          
   --------------------------------------------------------------------
  <T-CONT   5>          DBA Profile-ID:104
   <Gem Index 5>
   --------------------------------------------------------------------
   |Serv-Type:ETH |Encrypt:on  |Cascade:off |GEM-CAR:-            |
   |Upstream-priority-queue:0  |Downstream-priority-queue:-       |
   --------------------------------------------------------------------
  ------------------------------------------------------------------------------
  Notes: Run the display traffic table ip command to query 
         traffic table configuration
  -----------------------------------------------------------------------------
  Service profile ID   : 100
  Service profile name : ftth
  -----------------------------------------------------------------------------
  Port-type     Port-number     Max-adaptive-number
  -----------------------------------------------------------------------------
  POTS          adaptive        32
  ETH           adaptive        8
  VDSL          0               -
  TDM           0               -    
  MOCA          0               -
  CATV          adaptive        8
  -----------------------------------------------------------------------------
  TDM port type                     : E1
  TDM service type                  : TDMoGem
  MAC learning function switch      : Enable
  ONT transparent function switch   : Disable
  Ring check switch                 : Enable
  Ring port auto-shutdown           : Enable
  Ring detect frequency             : 8 (pps)
  Ring resume interval              : 240 (s)
  Ring detect period                : 0 (s)
  Multicast forward mode            : Unconcern
  Multicast forward VLAN            : -
  Multicast mode                    : Unconcern
  Upstream IGMP packet forward mode : Unconcern
  Upstream IGMP packet forward VLAN : -
  Upstream IGMP packet priority     : -
  Native VLAN option                : Concern
  Upstream PQ color policy          : -
  Downstream PQ color policy        : -
  Monitor link                      : Unconcern
  MTU(byte)                         : Unconcern
  -----------------------------------------------------------------------------
  Port-type Port-ID QinQmode  PriorityPolicy Inbound     Outbound
  -----------------------------------------------------------------------------
  ETH       1       unconcern unconcern      unconcern   unconcern
  ETH       2       unconcern unconcern      unconcern   unconcern
  ETH       3       unconcern unconcern      unconcern   unconcern
  ETH       4       unconcern unconcern      unconcern   unconcern
  ETH       5       unconcern unconcern      unconcern   unconcern
  ETH       6       unconcern unconcern      unconcern   unconcern
  ETH       7       unconcern unconcern      unconcern   unconcern
  ETH       8       unconcern unconcern      unconcern   unconcern
  IPHOST    1       unconcern unconcern      unconcern   unconcern
  -----------------------------------------------------------------------------
  Notes: * indicates the discretely configured traffic profile,
         run the display traffic table ip command to query
         traffic table configuration.
  -----------------------------------------------------------------------------
  Port-type Port-ID  DownstreamMode  MismatchPolicy
  -----------------------------------------------------------------------------
  ETH             1  operation       discard       
  ETH             2  operation       discard       
  ETH             3  operation       discard       
  ETH             4  operation       discard       
  ETH             5  operation       discard       
  ETH             6  operation       discard       
  ETH             7  operation       discard       
  ETH             8  operation       discard       
  -----------------------------------------------------------------------------
  Port-type Port-ID Dscp-mapping-table-index Classification-profile-id
  -----------------------------------------------------------------------------
  ETH       1       0                        -        
  ETH       2       0                        -        
  ETH       3       0                        -        
  ETH       4       0                        -        
  ETH       5       0                        -        
  ETH       6       0                        -        
  ETH       7       0                        -        
  ETH       8       0                        -        
  IPHOST    1       0                        -
  -----------------------------------------------------------------------------
  Port-type  Port-ID    IGMP-mode         IGMP-VLAN  IGMP-PRI  Max-MAC-Count
  -----------------------------------------------------------------------------
  ETH              1    -                         -         -      Unlimited
  ETH              2    -                         -         -      Unlimited
  ETH              3    -                         -         -      Unlimited
  ETH              4    -                         -         -      Unlimited
  ETH              5    -                         -         -      Unlimited
  ETH              6    -                         -         -      Unlimited
  ETH              7    -                         -         -      Unlimited
  ETH              8    -                         -         -      Unlimited
  IPHOST           1    -                         -         -      Unlimited
  -----------------------------------------------------------------------------
  Port-type Port-ID   Traffic-suppress   Traffic-suppress   Traffic-suppress
                      unicast(kbps)      multicast(kpbs)    broadcast(kbps)
  -----------------------------------------------------------------------------
  ETH             1   -                  -                  -               
  ETH             2   -                  -                  -               
  ETH             3   -                  -                  -               
  ETH             4   -                  -                  -               
  ETH             5   -                  -                  -               
  ETH             6   -                  -                  -               
  ETH             7   -                  -                  -               
  ETH             8   -                  -                  -               
  -----------------------------------------------------------------------------
  Port-type  Port-ID  L2-isolate
  -----------------------------------------------------------------------------
  ETH              1  unconcern           
  ETH              2  unconcern           
  ETH              3  unconcern           
  ETH              4  unconcern           
  ETH              5  unconcern           
  ETH              6  unconcern           
  ETH              7  unconcern           
  ETH              8  unconcern           
  -----------------------------------------------------------------------------
  Alarm policy profile ID      : 0
  Alarm policy profile name    : alarm-policy_0
  -----------------------------------------------------------------------------
  TR069 server profile ID      : 1
  TR069 server profile name    : tr069-server-profile_1
  -----------------------------------------------------------------------------
  -----------------------------------------------------------------------------
  The number of required ONTs     : 1
  -----------------------------------------------------------------------------
```

**Help:** execute the command "display ont info by-sn sn"

**Prompt:**

- huawei_smartax>
- huawei_smartax#

### display temperature

**Output:**
```
  SlotID:  4      BoardName: H805GPFD       Temperature:   57C( 134F)

  SlotID:  5      BoardName: H808EPSD       Temperature:   59C( 138F)

  SlotID:  7      BoardName: H802SCUN       Temperature:   69C( 156F)

  SlotID:  8      BoardName: H802SCUN       Temperature:   67C( 152F)

  SlotID: 11      BoardName: H807GPBD       Temperature:   55C( 131F)

  SlotID: 18      BoardName: H801X2CS       Temperature:   38C( 100F)
```

**Help:** execute the command "display temperature"

**Prompt:**

- huawei_smartax>
- huawei_smartax#

### display mem

**Output:**
```
  Memory occupancy: 79%
```

**Help:** execute the command "display mem"

**Prompt:**

- huawei_smartax>
- huawei_smartax#

### display board serial-number

**Output:**
```
  -------------------------------------------------------------------------
  Solt ID        Board Name         Serial Number 
  -------------------------------------------------------------------------
  0              A123ABCD           123ABC45D6789012                
  1                                                                 
  2              A123ABCDE          123ABC45D6789012                
  3              A123ABCDE          123456789123                    
  4              A123ABCDE          --                              
  5                                                                 
  -------------------------------------------------------------------------
```

**Help:** execute the command "display board serial-number"

**Prompt:**

- huawei_smartax>
- huawei_smartax#

### display sysuptime

**Output:**
```
  System up time: 11 day 22 hour 5 minute 17 second
```

**Help:** execute the command "display sysuptime"

**Prompt:**

- huawei_smartax>
- huawei_smartax#

### display ont info fsp

**Output:**
```
  -----------------------------------------------------------------------------
  F/S/P   ONT         SN         Control     Run      Config   Match    Protect
          ID                     flag        state    state    state    side 
  -----------------------------------------------------------------------------
  0/ 1/0    0  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0    1  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0    2  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0    3  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0    4  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0    5  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0    6  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0    7  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0    8  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0    9  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0   10  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0   11  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0   12  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0   13  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0   14  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0   15  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0   16  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0   17  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0   18  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0   19  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0   20  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0   21  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0   22  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0   23  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0   24  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0   25  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0   26  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0   27  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0   28  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0   29  1234567890ABCDEF  active      online   normal   match    no 
  0/ 1/0   30  1234567890ABCDEF  active      online   normal   match    no 
  -----------------------------------------------------------------------------
  F/S/P       ONT  Description  
              ID  
  -----------------------------------------------------------------------------
  0/ 1/0       0   Generic_description
  0/ 1/0       1   Generic_description
  0/ 1/0       2   Generic_description
  0/ 1/0       3   Generic_description
  0/ 1/0       4   Generic_description
  0/ 1/0       5   Generic_description
  0/ 1/0       6   Generic_description
  0/ 1/0       7   Generic_description
  0/ 1/0       8   Generic_description
  0/ 1/0       9   Generic_description
  0/ 1/0      10   Generic_description
  0/ 1/0      11   Generic_description
  0/ 1/0      12   Generic_description
  0/ 1/0      13   Generic_description
  0/ 1/0      14   Generic_description
  0/ 1/0      15   Generic_description
  0/ 1/0      16   Generic_description
  0/ 1/0      17   Generic_description
  0/ 1/0      18   Generic_description
  0/ 1/0      19   Generic_description
  0/ 1/0      20   Generic_description
  0/ 1/0      21   Generic_description
  0/ 1/0      22   Generic_description
  0/ 1/0      23   Generic_description
  0/ 1/0      24   Generic_description
  0/ 1/0      25   Generic_description
  0/ 1/0      26   Generic_description
  0/ 1/0      27   Generic_description
  0/ 1/0      28   Generic_description
  0/ 1/0      29   Generic_description
  0/ 1/0      30   Generic_description
  -----------------------------------------------------------------------------
  In port 0/ 1/0 , the total of ONTs are: 31, online: 31
  -----------------------------------------------------------------------------
```

**Help:** execute the command "display ont info fsp"

**Prompt:**

- huawei_smartax>
- huawei_smartax#

