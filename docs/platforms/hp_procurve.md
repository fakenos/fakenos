# hp_procurve


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
- hp_procurve>

### show ip

**Output:**
```
 Internet (IP) Service


  Default Gateway : 10.11.11.254   
  Default TTL     : 64   
  Arp Age         : 20  
  Domain Suffix   :                               
  DNS server      :                                         

  VLAN                 | IP Config  IP Address      Subnet Mask    
  -------------------- + ---------- --------------- ---------------
  DEFAULT_VLAN         | Disabled 
  MGMTVLAN             | Manual     10.11.11.200    255.255.255.0  
```

**Help:** execute the command "show ip"

**Prompt:**
- hp_procurve>
- hp_procurve#

### no page

**Output:** None

**Help:** Disable pagination

**Prompt:**
- hp_procurve>
- hp_procurve#

### logout

**Output:**
```
True
```

**Help:** not implemented the exit

**Prompt:**
- hp_procurve>
- hp_procurve#

### show lldp info remote-device detail

**Output:**
```

 LLDP Remote Device Information Detail

  Local Port   : 1
  ChassisType  : mac-address         
  ChassisId    : 3821c7-c1cd00            
  PortType     : local                                                     
  PortId       : 1                                                         
  SysName      : 65432p-swi006-abcd-srvroom-4asd 
  System Descr : Aruba JL357A 2540-48G-PoE+-4SFP+ Switch, revision YC.16.0...
  PortDescr    : 1                                                           
  Pvid         : 0                        

  System Capabilities Supported  : bridge, router
  System Capabilities Enabled    : bridge

  Remote Management Address
     Type    : ipv4
     Address : 192.168.130.100

  Poe Plus Information Detail 

    Poe Device Type         : Type2 PSE
    Power Source            : Unknown
    Power Priority          : Unknown
    PD Requested Power Value   : 0.0 Watts
    PSE Allocated Power Value      : 0.0 Watts

------------------------------------------------------------------------------
  Local Port   : 3
  ChassisType  : mac-address         
  ChassisId    : 3ce1a1-2218f0            
  PortType     : mac-address                                               
  PortId       : 3c e1 a1 22 18 f0                                         
  SysName      :                                 
  System Descr :                                                             
  PortDescr    :                                                             
  Pvid         :                          

  System Capabilities Supported  : 
  System Capabilities Enabled    : 

  Remote Management Address

  MED Information Detail 
    EndpointClass          :Class1

------------------------------------------------------------------------------
  Local Port   : 7
  ChassisType  : mac-address         
  ChassisId    : bcf310-1f8b40            
  PortType     : interface-name                                            
  PortId       : mgt0                                                      
  SysName      : AH-cust-AP21                    
  System Descr :                                                             
  PortDescr    :                                                             
  Pvid         :                          

  System Capabilities Supported  : bridge, wlan-access-point
  System Capabilities Enabled    : bridge, wlan-access-point

  Remote Management Address
     Type    : ipv4
     Address : 192.168.100.55

  MED Information Detail 
    EndpointClass          :Class1
    Poe Device Type        :PD
    Power Requested        :17.5 W
    Power Source           :From PSE
    Power Priority         :Critical

  Poe Plus Information Detail 

    Poe Device Type         : Type2 PD
    Power Source            : Unknown
    Power Priority          : Critical
    PD Requested Power Value   : 17.5 Watts
    PSE Allocated Power Value      : 17.5 Watts

------------------------------------------------------------------------------
  Local Port   : 25
  ChassisType  : mac-address         
  ChassisId    : d8cb8a-6d303c            
  PortType     : mac-address                                               
  PortId       : d8 cb 8a 6d 30 3c                                         
  SysName      :                                 
  System Descr :                                                             
  PortDescr    :                                                             
  Pvid         :                          

  System Capabilities Supported  : 
  System Capabilities Enabled    : 

  Remote Management Address

  MED Information Detail 
    EndpointClass          :Class1

------------------------------------------------------------------------------
  Local Port   : 29
  ChassisType  : mac-address         
  ChassisId    : 484d7e-e66c42            
  PortType     : mac-address                                               
  PortId       : 48 4d 7e e6 6c 42                                         
  SysName      :                                 
  System Descr :                                                             
  PortDescr    :                                                             
  Pvid         :                          

  System Capabilities Supported  : 
  System Capabilities Enabled    : 

  Remote Management Address

  MED Information Detail 
    EndpointClass          :Class1

------------------------------------------------------------------------------
  Local Port   : 36
  ChassisType  : mac-address         
  ChassisId    : 603197-7aa548            
  PortType     : local                                                     
  PortId       : 1                                                         
  SysName      : NAP203                          
  System Descr : ZLD 6.00(###.8)B1 (cannon)                                  
  PortDescr    : UPLINK                                                      
  Pvid         :                          

  System Capabilities Supported  : bridge, wlan-access-point, router
  System Capabilities Enabled    : bridge, wlan-access-point, router

  Remote Management Address
     Type    : ipv4
     Address : 192.168.100.50

  Poe Plus Information Detail 

    Poe Device Type         : Type2 PD
    Power Source            : Unknown
    Power Priority          : High
    PD Requested Power Value   : 16.0 Watts
    PSE Allocated Power Value      : 16.0 Watts

------------------------------------------------------------------------------
  Local Port   : 37
  ChassisType  : mac-address         
  ChassisId    : b00cd1-359a98            
  PortType     : mac-address                                               
  PortId       : b0 0c d1 35 9a 98                                         
  SysName      :                                 
  System Descr :                                                             
  PortDescr    :                                                             
  Pvid         :                          

  System Capabilities Supported  : 
  System Capabilities Enabled    : 

  Remote Management Address

  MED Information Detail 
    EndpointClass          :Class1

------------------------------------------------------------------------------
  Local Port   : 42
  ChassisType  : mac-address         
  ChassisId    : d8cb8a-894644            
  PortType     : mac-address                                               
  PortId       : d8 cb 8a 89 46 44                                         
  SysName      :                                 
  System Descr :                                                             
  PortDescr    :                                                             
  Pvid         :                          

  System Capabilities Supported  : 
  System Capabilities Enabled    : 

  Remote Management Address

  MED Information Detail 
    EndpointClass          :Class1



```

**Help:** execute the command "show lldp info remote-device detail"

**Prompt:**
- hp_procurve>
- hp_procurve#

### show vlans

**Output:**
```
 Status and Counters - VLAN Information

  Maximum VLANs to support : 256                  
  Primary VLAN : DEFAULT_VLAN
  Management VLAN :             

  VLAN ID Name                             | Status     Voice Jumbo
  ------- -------------------------------- + ---------- ----- -----
  1       DEFAULT_VLAN                     | Port-based No    No   
  10      Router Vlan                      | Port-based No    No   
  50      Voice                            | Port-based Yes   No   

```

**Help:** execute the command "show vlans"

**Prompt:**
- hp_procurve>
- hp_procurve#

### show interfaces

**Output:**
```
Status and Counters - Port Counters

                                                                    Flow
 Port       Total Bytes    Total Frames   Errors Rx    Drops Tx     Ctrl
 ---------- -------------- -------------- ------------ ------------ ----
 1          200,205        1861           0            0            off
 2          0              0              0            0            off
 3          0              0              0            0            off
 4          0              0              0            0            off
 5          0              0              0            0            off
 6          0              0              0            0            off
 7          0              0              0            0            off
 8          0              0              0            0            off
 9          0              0              0            0            off
 10         0              0              0            0            off
 11         0              0              0            0            off
 12         0              0              0            0            off
 13         0              0              0            0            off
 14         0              0              0            0            off
 15         0              0              0            0            off
 16         0              0              0            0            off
 17         0              0              0            0            off
 18         0              0              0            0            off
 19         0              0              0            0            off
 20         0              0              0            0            off
 21         0              0              0            0            off
 22         0              0              0            0            off
 23         0              0              0            0            off
 24         0              0              0            0            off
 25         0              0              0            0            off
 26         0              0              0            0            off
 27         0              0              0            0            off
 28         0              0              0            0            off
 29         0              0              0            0            off
 30         0              0              0            0            off
 31         0              0              0            0            off
 32         0              0              0            0            off
 33         0              0              0            0            off
 34         0              0              0            0            off
 35         0              0              0            0            off
 36         0              0              0            0            off
 37         0              0              0            0            off
 38         0              0              0            0            off
 39         0              0              0            0            off
 40         0              0              0            0            off
 41         0              0              0            0            off
 42         0              0              0            0            off
 43         0              0              0            0            off
 44         0              0              0            0            off
 45         0              0              0            0            off
 46         0              0              0            0            off
 47         0              0              0            0            off
 48         0              0              0            0            off
 49         0              0              0            0            off
 50         0              0              0            0            off
 51         0              0              0            0            off
 52         0              0              0            0            off

```

**Help:** execute the command "show interfaces"

**Prompt:**
- hp_procurve>
- hp_procurve#

### show port-security

**Output:**
```
 Port Security

  Port  Learn Mode         | Action                   Eavesdrop Prevention
  ----- ------------------ + ------------------------ --------------------
  1     Continuous         | None                     Enabled
  2     Continuous         | None                     Enabled
  3     Continuous         | None                     Enabled
  4     Continuous         | None                     Enabled
  5     Continuous         | None                     Enabled
  6     Continuous         | None                     Enabled
  7     Continuous         | None                     Enabled
  8     Continuous         | None                     Enabled
  9     Continuous         | None                     Enabled
  10    Static             | Send Alarm, Disable Port Enabled
  11    Configured         | Send Alarm               Enabled
  12    Port-Access        | None                     Enabled
  13    Limited-Continuous | Send Alarm               Enabled
  14    Continuous         | None                     Enabled
  15    Continuous         | None                     Enabled
  16    Continuous         | None                     Enabled
  17    Continuous         | None                     Enabled
  18    Continuous         | None                     Enabled
  19    Continuous         | None                     Enabled
  20    Continuous         | None                     Enabled
  21    Continuous         | None                     Enabled
  22    Continuous         | None                     Enabled
  23    Continuous         | None                     Enabled
  24    Continuous         | None                     Enabled
  25    Continuous         | None                     Enabled
  26    Continuous         | None                     Enabled
  27    Continuous         | None                     Enabled
  28    Continuous         | None                     Enabled
  29    Continuous         | None                     Enabled
  30    Continuous         | None                     Enabled
  31    Continuous         | None                     Enabled
  32    Continuous         | None                     Enabled
  33    Continuous         | None                     Enabled
  34    Continuous         | None                     Enabled
  35    Continuous         | None                     Enabled
  36    Continuous         | None                     Enabled
  37    Continuous         | None                     Enabled
  38    Continuous         | None                     Enabled
  39    Continuous         | None                     Enabled
  40    Continuous         | None                     Enabled
  41    Continuous         | None                     Enabled
  42    Continuous         | None                     Enabled
  43    Continuous         | None                     Enabled
  44    Continuous         | None                     Enabled
  45    Continuous         | None                     Enabled
  46    Continuous         | None                     Enabled
  47    Continuous         | None                     Enabled
  48    Continuous         | None                     Enabled
  49    Continuous         | None                     Enabled
  50    Continuous         | None                     Enabled
  51    Continuous         | None                     Enabled
  52    Continuous         | None                     Enabled

```

**Help:** execute the command "show port-security"

**Prompt:**
- hp_procurve>
- hp_procurve#

### show lldp info remote-device

**Output:**
```

 LLDP Remote Devices Information

  LocalPort | ChassisId          PortId             PortDescr SysName           
  --------- + ------------------ ------------------ --------- ------------------
  1         | 3821c7-c1cd00      1                  1         65432p-swi006-g...
  3         | 3ce1a1-2218f0      3c e1 a1 22 18 f0                              
  7         | bcf310-1f8b40      mgt0                         AH-cust-AP21      
  25        | d8cb8a-6d303c      d8 cb 8a 6d 30 3c                              
  29        | 484d7e-e66c42      48 4d 7e e6 6c 42                              
  36        | 603197-7aa548      1                  UPLINK    NAP203            
  37        | b00cd1-359a98      b0 0c d1 35 9a 98                              
  42        | d8cb8a-894644      d8 cb 8a 89 46 44                              
 

```

**Help:** execute the command "show lldp info remote-device"

**Prompt:**
- hp_procurve>
- hp_procurve#

### show arp

**Output:**
```

 IP ARP table

  IP Address      MAC Address       Type    Port
  --------------- ----------------- ------- ----
  10.11.12.11     0015b2-a45078     dynamic

```

**Help:** execute the command "show arp"

**Prompt:**
- hp_procurve>
- hp_procurve#

### show trunks

**Output:**
```

 Load Balancing Method:  L3-based (default)

  Port   | Name                             Type       | Group Type    
  ------ + -------------------------------- ---------- + ----- --------
  49     | Uplink 65432p-swi001             1000LX     | Trk2  LACP    
  50     | Uplink 65432p-swi001             1000LX     | Trk2  LACP    
 

```

**Help:** execute the command "show trunks"

**Prompt:**
- hp_procurve>
- hp_procurve#

### show interfaces brief

**Output:**
```
 Status and Counters - Port Status

                          | Intrusion                           MDI  Flow Bcast
  Port         Type       | Alert     Enabled Status Mode       Mode Ctrl Limit
  ------------ ---------- + --------- ------- ------ ---------- ---- ---- -----
  1            100/1000T  | No        Yes     Down   1000FDx    Auto off  0
  2            100/1000T  | No        Yes     Down   1000FDx    Auto off  0
  3            100/1000T  | Yes       Yes     Down   1000FDx    Auto off  0
  4            100/1000T  | No        Yes     Down   1000FDx    Auto off  0
  5            100/1000T  | No        No      Down   1000FDx    Auto off  0
  6            100/1000T  | No        Yes     Down   1000FDx    Auto on   0    
  7            100/1000T  | No        Yes     Down   1000FDx    Auto off  0
  8            100/1000T  | No        Yes     Down   1000FDx    Auto off  0
  9            100/1000T  | No        Yes     Down   1000FDx    Auto off  0
  10           100/1000T  | No        Yes     Down   1000FDx    Auto on   50
  11           100/1000T  | No        Yes     Down   1000FDx    Auto off  0
  12           100/1000T  | No        Yes     Down   1000FDx    Auto off  0
  13           100/1000T  | No        Yes     Down   1000FDx    Auto off  0
  14           100/1000T  | No        Yes     Down   1000FDx    Auto off  0
  15           100/1000T  | No        Yes     Down   1000FDx    Auto off  0
  16           100/1000T  | No        Yes     Down   1000FDx    Auto off  0
  17           100/1000T  | No        Yes     Down   1000FDx    Auto off  0
  18           100/1000T  | No        Yes     Down   1000FDx    Auto off  0
  19           100/1000T  | No        Yes     Down   1000FDx    Auto off  0
  20           100/1000T  | No        Yes     Down   1000FDx    Auto off  0
  21           100/1000T  | No        Yes     Down   1000FDx    Auto off  0
  22           100/1000T  | No        Yes     Down   1000FDx    Auto off  0
  23           100/1000T  | No        Yes     Down   1000FDx    Auto off  0
  24           100/1000T  | No        Yes     Up     100FDx     MDI  off  0

```

**Help:** execute the command "show interfaces brief"

**Prompt:**
- hp_procurve>
- hp_procurve#

### show tech buffers

**Output:**
```










CRASHLogfileshow


Active Management Module 2 Crash Log

...Crash Log File Header..........................
Product:   HP J9091A
Name:      HP Switch E8212zl
Date:      Apr 20 2012 12:34:21
Build:     13
Version:   K.15.06.0017
Directory: /ws/swbuildm/ec_rel_eureka_qaoff/code/b
CPU:       PPC85XX
  crash rec index = 1
   boot type    = Warm Boot
   willBootType = UNKNOWN BOOT
..................................................
    CrashRecordPointer (ff419a8)  for Crash Record Index 1
----- Crash Record:   1 at 0xff419a8 -----
 crash id = 0x7f0c3993
crash info = 0xbaabface
Mgmt Module 2 went down in Active Mode
timestamp:  03/08/16 00:04:11
Crash msg:  Operator warm reload.
-----
 

Standby Management Module 1 Crash Log

Crash Log Uninitialized


CRASHData
 
Slot 1

CRASHLogfileshow

slot a:
-------

...Crash Log File Header..........................
Product:   Procurve CA
Name:      Procurve Switch card id:68
Date:      Apr 20 2012 12:18:16
Build:     288
Version:   K.15.06.0017
Directory: /ws/swbuildm/ec_rel_eureka_qaoff/code/b
CPU:       arm11
  crash rec index = 0
   boot type    = POWER ON
   willBootType = UNKNOWN BOOT
..................................................
  No Saved Crash Information


CRASHData

slot a:
-------

MSGCOUNTERSshow

 slot a:
-------
 txSeq        =      64295     rxSeq       =      42342 
 rxAcks       =    1209122     txAcks      =    2151500 
 retx         =          0     rxOutOfSeq  =          0 
 rtx_pktcnt   =          0     rxSeqQcnt   =          0 
 Max pktcnt   =         31     Max Qcnt    =          0 
 Bad CRCs     =          0     dupSeq      =          3 


MSGpoolStatsShow
 
slot a:
-------
             total   free  allocated  min-free  missed  corrupt
             -----  -----  ---------  --------  ------  -------
  MSG_BUF     4400   4168      232       4010        0       0


Checking buffer pool structures... PASSED

Allocation statistics for MSG buffer pool:
 Current system time: 01/16/90 15:16:02
   OwnerName    OwnerID    #Owned        Oldest
  -----------   --------   ------   -----------------
       (null)   1b215600       3    01/01/90 00:00:00
     muiCore1   1b1ed400       2    01/01/90 00:00:04
      mSess11   1b1eda40       1    01/01/90 00:00:03
    mSesInp11   1b1ea880       1    01/01/90 00:00:04
   mChassAgnt   1b1f1500       8    01/01/90 00:00:04
   mInstUpCtl   1b215740       2    01/16/90 15:14:59
     mAsicUpd   1b1e78c0       1    01/16/90 15:16:01
   mAdMUpCtrl   1b1e7e00       3    01/01/90 00:00:05
    mHttpCtUp   1b1dfc00       1    01/16/90 15:16:01
   mIpAdMUpCt   1b1e4c80       3    01/01/90 00:00:05
   mPmSlvCtrl   1b1db500       3    01/01/90 00:00:05
   mPoeMgrCtl   1b1f7e80       2    01/01/90 00:00:06
   tagentConsole   1b1f7900       1    01/16/90 15:16:01
     muiAgent   1b1f7640       1    01/16/90 15:16:01
    INTERRUPT          0     199    01/16/90 15:15:13
  Note: (null) indicates buffer allocated at init time (not used since).


Slot 2

CRASHLogfileshow
 
slot b:
-------

...Crash Log File Header..........................
Product:   Procurve CA
Name:      Procurve Switch card id:124
Date:      Apr 20 2012 12:18:16
Build:     288
Version:   K.15.06.0017
Directory: /ws/swbuildm/ec_rel_eureka_qaoff/code/b
CPU:       arm11
  crash rec index = 0
   boot type    = POWER ON
   willBootType = UNKNOWN BOOT
..................................................
  No Saved Crash Information


CRASHData

slot b:
-------

MSGCOUNTERSshow

 slot b:
-------
 txSeq        =      12101     rxSeq       =      44667 
 rxAcks       =    1237277     txAcks      =    2131969 
 retx         =          0     rxOutOfSeq  =          0 
 rtx_pktcnt   =          0     rxSeqQcnt   =          0 
 Max pktcnt   =         31     Max Qcnt    =          0 
 Bad CRCs     =          0     dupSeq      =          1 


MSGpoolStatsShow
 
slot b:
-------
             total   free  allocated  min-free  missed  corrupt
             -----  -----  ---------  --------  ------  -------
  MSG_BUF     4400   4168      232       4062        0       0


Checking buffer pool structures... PASSED

Allocation statistics for MSG buffer pool:
 Current system time: 01/16/90 15:16:00
   OwnerName    OwnerID    #Owned        Oldest
  -----------   --------   ------   -----------------
       (null)   1b215600       3    01/01/90 00:00:00
     muiCore2   1b1f1bc0       2    01/01/90 00:00:04
      mSess21   1b1ed000       1    01/01/90 00:00:04
    mSesInp21   1b215740       1    01/01/90 00:00:04
   mChassAgnt   1b1f1500       8    01/01/90 00:00:07
     mAsicUpd   1b1e8d40       1    01/16/90 15:15:59
   mAdMUpCtrl   1b1e5280       3    01/01/90 00:00:08
    mHttpCtUp   1b1dc080       1    01/16/90 15:15:59
   mIpAdMUpCt   1b1e1100       3    01/01/90 00:00:08
   mPmSlvCtrl   1b1dc980       3    01/01/90 00:00:08
   mInstUpCtl   1b1eaf40       2    01/16/90 15:14:59
   mPoeMgrCtl   1b1f7f00       2    01/01/90 00:00:09
   tagentConsole   1b1f7980       1    01/16/90 15:15:59
     muiAgent   1b1f76c0       1    01/16/90 15:15:59
    INTERRUPT          0     199    01/16/90 15:15:06
  Note: (null) indicates buffer allocated at init time (not used since).


```

**Help:** execute the command "show tech buffers"

**Prompt:**
- hp_procurve>
- hp_procurve#

### show system

**Output:**
```

 Status and Counters - General System Information

  System Name        : HP_Procurve-01                           
  System Contact     : John Smith
  System Location    : Downtown DC2

  MAC Age Time (sec) : 300    

  Time Zone          : -480 
  Daylight Time Rule : Continental-US-and-Canada 


  Software revision  : K.15.06.0017         Base MAC Addr      : 7446a0-41a56f
  ROM Version        : K.15.29              Serial Number      : AB12CDE3FG  
  Allow V1 Modules   : Yes

  Up Time            : 15 days              Memory   - Total   : 128,380,928 
  CPU Util (%)       : 22                              Free    : 61,999,280  

  IP Mgmt  - Pkts Rx : 39,808,402           Packet   - Total   : 6750        
             Pkts Tx : 4,524,902            Buffers    Free    : 5086        
                                                       Lowest  : 3416        
                                                       Missed  : 0           


```

**Help:** execute the command "show system"

**Prompt:**
- hp_procurve>
- hp_procurve#

### show cdp neighbors detail

**Output:**
```
 CDP neighbors information

  Port : 1   
  Device ID : AP01-Site
  Address Type : IP          
  Address      : 10.11.11.16                                                 
  Platform     : 5.9.1.5-001RAP-6521-60020-WR                               
  Capability   : Router                                                     
  Device Port  : ge1                                                        
  Version      : 5.9.1.5-001RAP-6521-60020-WR                               

------------------------------------------------------------------------------

  Port : 1   
  Device ID : 5c 0e 8b 11 11 11                                             
  Address Type : IP          
  Address      : 10.11.11.16                                                 
  Platform     : AP-6521-60020-WR, Version 5.9.1.5-001R                     
  Capability   : Router                                                     
  Device Port  : ge1                                                        
  Version      : AP-6521-60020-WR, Version 5.9.1.5-001R                     

------------------------------------------------------------------------------

  Port : 2   
  Device ID : 5c 0e 8b 12 22 22                                             
  Address Type : IP          
  Address      : Unsupported format                                          
  Platform     : AP-6521-60020-WR, Version 5.9.1.5-001R                     
  Capability   : Router                                                     
  Device Port  : ge1                                                        
  Version      : AP-6521-60020-WR, Version 5.9.1.5-001R                     

------------------------------------------------------------------------------

  Port : 2   
  Device ID : AP02-Site
  Address Type : IP          
  Address      : 10.11.11.17                                                 
  Platform     : 5.9.1.5-001RAP-6521-60020-WR                               
  Capability   : Router                                                     
  Device Port  : ge1                                                        
  Version      : 5.9.1.5-001RAP-6521-60020-WR                               
```

**Help:** execute the command "show cdp neighbors detail"

**Prompt:**
- hp_procurve>
- hp_procurve#

### show mac-address

**Output:**
```

 Status and Counters - Port Address Table

  MAC Address   Port
  ------------- -----
  00000d-600000 10
  000424-731040 10
  0010f3-841dea 10
  5c0e8b-97d9db 3
```

**Help:** execute the command "show mac-address"

**Prompt:**
- hp_procurve>
- hp_procurve#

### show ip route

**Output:**
```

                                                                                                                                                                                                                                                       IP Route Entries

  Destination        Gateway         VLAN Type      Sub-Type   Metric     Dist.
  ------------------ --------------- ---- --------- ---------- ---------- -----
  0.0.0.0/0          10.11.11.254    1111 static               250        1
  10.11.11.0/24      mgmt            1111 connected            1          0
  127.0.0.0/8        reject               static               0          0
  127.0.0.1/32                            connected            1          0    

```

**Help:** execute the command "show ip route"

**Prompt:**
- hp_procurve>
- hp_procurve#

### terminal width 511

**Output:** None

**Help:** Execute the command terminal width 511. This automatically generated. Feel free to change it!

**Prompt:**
- hp_procurve>
- hp_procurve#

### screen-length 0 temporary

**Output:** None

**Help:** Execute the command screen-length 0 temporary. This automatically generated. Feel free to change it!

**Prompt:**
- hp_procurve>
- hp_procurve#

### terminal datadump

**Output:** None

**Help:** Execute the command terminal datadump. This automatically generated. Feel free to change it!

**Prompt:**
- hp_procurve>
- hp_procurve#

### terminal length 0

**Output:** None

**Help:** Execute the command terminal length 0. This automatically generated. Feel free to change it!

**Prompt:**
- hp_procurve>
- hp_procurve#

### disable cli prompting

**Output:** None

**Help:** Execute the command disable cli prompting. This automatically generated. Feel free to change it!

**Prompt:**
- hp_procurve>
- hp_procurve#

### disable clipaging

**Output:** None

**Help:** Execute the command disable clipaging. This automatically generated. Feel free to change it!

**Prompt:**
- hp_procurve>
- hp_procurve#

### screen-length disable

**Output:** None

**Help:** Execute the command screen-length disable. This automatically generated. Feel free to change it!

**Prompt:**
- hp_procurve>
- hp_procurve#

