# ruckus_fastiron


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
- ruckus_fastiron>

### show interfaces

**Output:**
```
40GigabitEthernet2/3/3 is up, line protocol is up
  Port up for 128 day(s) 19 hour(s) 49 minute(s) 25 second(s)
  Hardware is 40GigabitEthernet, address is d4c1.9e16.8d10 (bia d4c1.9e16.8d10)
  Interface type is 40Gig Copper
  Configured speed 40Gbit, actual 40Gbit, configured duplex fdx, actual fdx
  Configured mdi mode AUTO, actual MDI
  Stacking Port, port state is FORWARDING
  BPDU guard is Disabled, ROOT protect is Disabled, Designated protect is Disabled
  Link Error Dampening is Disabled
  STP configured to OFF, priority is level0, mac-learning is enabled
  Openflow is Disabled, Openflow Hybrid mode is Disabled,  Flow Control is config enabled, oper disabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Mac-notification is disabled
  Not member of any active trunks
  Not member of any configured trunks
  No port name
  IPG MII 64 bits-time, IPG GMII 64 bits-time
  MTU 1500 bytes, encapsulation ethernet
  MMU Mode is Store-and-forward
  300 second input rate: 25496 bits/sec, 18 packets/sec, 0.00% utilization
  300 second output rate: 4208 bits/sec, 5 packets/sec, 0.00% utilization
  130393421 packets input, 26755527458 bytes, 0 no buffer
  Received 1819460 broadcasts, 128573834 multicasts, 127 unicasts
  0 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  24082238 packets output, 2734736336 bytes, 0 underruns
  Transmitted 32 broadcasts, 24082204 multicasts, 2 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
  Protected: No
  MAC Port Security: Disabled
 
UC Egress queues:
Queue counters      Queued packets    Dropped Packets
         0                   0                   0
         1                   0                   0
         2                   0                   0
         3                   0                   0
         4                   0                   0
         5                   0                   0
         6                   0                   0
         7                   0                   0
         8                   0                   0
         9            11119857                   0
 
 
MC Egress queues:
Queue counters    Queued packets    Dropped Packets
         0                2480                   0
         1                   0                   0
         2                   0                   0
         3                   0                   0
         4                  34                   0
         5                   0                   0
         6            12959867                   0
         7                   0                   0
         8                   0                   0
         9                   0                   0
 
Oversubscribed ingress drop counters:
High priority drop                     0
Low priority drop                     0
Total drop                             0
40GigabitEthernet2/3/4 is down, line protocol is down
  Port down for 128 day(s) 19 hour(s) 49 minute(s) 29 second(s)
  Hardware is 40GigabitEthernet, address is d4c1.9e16.8d11 (bia d4c1.9e16.8d11)
  Interface type is 40Gig Fiber
  Configured speed 40Gbit, actual unknown, configured duplex fdx, actual unknown
  Configured mdi mode AUTO, actual unknown
  Member of L2 VLAN ID 0, port is untagged, port state is BLOCKING
  BPDU guard is Disabled, ROOT protect is Disabled, Designated protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0, mac-learning is enabled
  Openflow is Disabled, Openflow Hybrid mode is Disabled,  Flow Control is config enabled, oper enabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Mac-notification is disabled
  Not member of any active trunks
  Not member of any configured trunks
  No port name
  IPG MII 64 bits-time, IPG GMII 64 bits-time
  MTU 1500 bytes, encapsulation ethernet
  MMU Mode is Store-and-forward
  300 second input rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  300 second output rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  0 packets input, 0 bytes, 0 no buffer
  Received 0 broadcasts, 0 multicasts, 0 unicasts
  0 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  0 packets output, 0 bytes, 0 underruns
  Transmitted 0 broadcasts, 0 multicasts, 0 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
  Protected: No
  MAC Port Security: Disabled
 
UC Egress queues:
Queue counters      Queued packets    Dropped Packets
         0                   0                   0
         1                   0                   0
         2                   0                   0
         3                   0                   0
         4                   0                   0
         5                   0                   0
         6                   0                   0
        7                   0                   0
         8                   0                   0
         9                   0                   0
 
 
MC Egress queues:
Queue counters    Queued packets    Dropped Packets
         0                   0                   0
         1                   0                   0
         2                   0                   0
         3                   0                   0
         4                   0                   0
         5                   0                   0
         6                   0                   0
         7                   0                   0
         8                   0                   0
         9                   0                   0
 
Oversubscribed ingress drop counters:
 High priority drop                     0
Low priority drop                     0
Total drop                             0
Lag lg10 is up, line protocol is up
  Configured speed 20G, actual 20G, configured duplex fdx, actual fdx
  Member of 17 L2 VLANs, port is tagged, port state is Forward
  BPDU guard is Disabled, ROOT protect is Disabled, Designated protect is Disabled
  STP configured to ON, priority is level0, mac-learning is enabled
  Openflow is Disabled,  Openflow Hybrid mode is Disabled
  Mirror disabled, Monitor disabled
  Mac-notification is disabled
  Member of active trunk ports 1/2/1,2/2/1,lg10, Lag Interface is lg10
  Member of configured trunk ports 1/2/1,2/2/1,lg10, Lag Interface is lg10
  No port name
  300 second input rate: 4824 bits/sec, 6 packets/sec, 0.00% utilization
  300 second output rate: 3856 bits/sec, 5 packets/sec, 0.00% utilization
  42361177 packets input, 3884151979 bytes, 0 no buffer
  Received 3638818 broadcasts, 38722115 multicasts, 244 unicasts
  0 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  23699093 packets output, 2526068617 bytes, 0 underruns
  Transmitted 12 broadcasts, 23699080 multicasts, 0 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
GigEthernetmgmt1 is up, line protocol is up
  Port up for 66 day(s) 7 hour(s) 10 minute(s) 15 second(s)
  Hardware is GigEthernet, address is d4c1.9e16.9e87 (bia d4c1.9e16.9eb7)
  Configured speed auto, actual 1Gbit, configured duplex fdx, actual fdx
  Configured mdi mode AUTO, actual none
  Not a Member of any VLAN , port is untagged, port state is NONE
  No port name
  Internet address is 10.203.35.106/24, MTU 1500 bytes, encapsulation ethernet
  300 second input rate: 4208 bits/sec, 6 packets/sec, 0.00% utilization
  300 second output rate: 14656 bits/sec, 6 packets/sec, 0.00% utilization
  12656202 packets input, 1480617278 bytes, 0 no buffer
  Received 0 broadcasts, 0 multicasts, 12656202 unicasts
  0 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  72034 packets output, 8813479 bytes, 0 underruns
  Transmitted 0 broadcasts, 0 multicasts, 72034 unicasts
  0 output errors, 0 collisions
```

**Help:** execute the command "show interfaces"

**Prompt:**
- ruckus_fastiron>
- ruckus_fastiron#

### show arp

**Output:**
```
All ARPs: 3, maximum capacity: 4096
No.   IP              MAC            Type     Age Port           Status VLAN 
1     10.103.3.1      70db.9862.224c Dynamic  0   1/2/1          Valid  1    
2     10.103.3.10     c81f.6603.c442 Dynamic  4   1/1/8          Valid  1    
3     10.103.3.4      f8bc.1294.dd30 Dynamic  4   1/1/6          Valid  1    
Total ARP Entries : 3
```

**Help:** execute the command "show arp"

**Prompt:**
- ruckus_fastiron>
- ruckus_fastiron#

### show vlan

**Output:**
```
Total PORT-VLAN entries: 53
Maximum PORT-VLAN entries: 1024

Legend: [Stk=Stack-Id, S=Slot]

PORT-VLAN 1, Name [None], Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 9, Name Service_Desk, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 10, Name MIS_Infrastructure, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 11, Name Datacenter_MDF, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 12, Name East_Basement_IDF, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 13, Name West_Basement_IDF, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 14, Name West_Wing_IDF, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 15, Name West_Wing_IDF_MAC, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 16, Name DVR_Access, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled
 
PORT-VLAN 17, Name Accounting_Rita_Access, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 18, Name Accounting_Spreadsheet_Access, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 20, Name Test_Lab_IDF, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 21, Name Bailout_Switch, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 25, Name Train-O-Rama, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 32, Name 904RFD_Network, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 33, Name Guest_WLAN, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 35, Name [None], Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 50, Name LEGALNOLO, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 51, Name HR_Servers, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 52, Name HR, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 75, Name AC_Management, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 77, Name P2PE_Cert_Station, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 101, Name 001_OPS, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled
 
PORT-VLAN 102, Name 001_POS, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled
 
PORT-VLAN 103, Name 001_Non-Store, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled
 
PORT-VLAN 104, Name P2PE_LAN, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled
 
PORT-VLAN 107, Name 001_SIPS, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled
 
PORT-VLAN 108, Name 001_POS_Training, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled
 
PORT-VLAN 109, Name 001_Management, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled
 
PORT-VLAN 110, Name 001_AP, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled
 
PORT-VLAN 111, Name 001_901SIPS, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled
 
PORT-VLAN 112, Name 001_Customer_WiFi, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled
 
PORT-VLAN 113, Name New_Store_SIPS, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled
 
PORT-VLAN 122, Name 001_SYOD, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled
 
PORT-VLAN 191, Name NWH_CCTV, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled
 
PORT-VLAN 200, Name 000_Dev_Store, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled
 
PORT-VLAN 222, Name Conference, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled
 
PORT-VLAN 225, Name Keyless_Entry, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled
 
PORT-VLAN 226, Name [None], Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled
 
PORT-VLAN 254, Name Test_STore, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled
 
PORT-VLAN 300, Name NetMgt, Priority level0, Off
 Untagged Ports: (U1/M1)  37  38
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 301, Name Internal_Devices, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 302, Name Physical_Security, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 303, Name HPB_Users, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled
 
PORT-VLAN 306, Name VOICE, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 307, Name Guests, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 501, Name Flagship_WLAN, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 502, Name 888DEV, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)   1   2   3   4   5   6   7   8   9  10  11  12
   Tagged Ports: (U1/M1)  29  45  46
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1   7  11  12  13  14  21  22  31  32  41  51
   Tagged Ports: (LAG)    61  71
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 666, Name DEFAULT-VLAN, Priority level0, Off
 Untagged Ports: (U1/M1)  13  14  15  16  17  18  19  20  21  22  23  24
 Untagged Ports: (U1/M1)  25  26  27  28  29  31  32  33  34  35  36  39
 Untagged Ports: (U1/M1)  43  44  47  48
 Untagged Ports: (U1/M2)   1   2   3   4
   Tagged Ports: None
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 1700, Name [None], Priority level0, Off
 Untagged Ports: (U1/M1)  40
   Tagged Ports: (U1/M1)  29
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 1800, Name NWH_PUBLIC, Priority level0, Off
 Untagged Ports: (U1/M1)  30  41  42
   Tagged Ports: (U1/M1)   2  29
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1  12
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 4084, Name MCT-keep-alive, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M1)  48
 Mac-Vlan Ports: None
     Monitoring: Disabled

PORT-VLAN 4085, Name Session-VLAN, Priority level0, Off
 Untagged Ports: None
   Tagged Ports: (U1/M2)   5   6
   Tagged Ports: (LAG)     1
 Mac-Vlan Ports: None
     Monitoring: Disabled

```

**Help:** execute the command "show vlan"

**Prompt:**
- ruckus_fastiron>
- ruckus_fastiron#

### show interfaces brief

**Output:**
```

Port       Link    State   Dupl Speed Trunk Tag Pvid Pri MAC             Name
1/1/1      Up      Forward Full 10G   11    Yes N/A  0   c0c5.2050.a500  001-rk-mdf1
1/1/2      Up      Forward Full 10G   12    Yes N/A  0   c0c5.2050.a500  001-rk-mdf2
1/1/3      Up      Forward Full 10G   13    Yes N/A  0   c0c5.2050.a500  001-rk-mdf3
1/1/4      Up      Forward Full 10G   14    Yes N/A  0   c0c5.2050.a500  001-rk-mdf4
1/1/5      Up      Forward Full 10G   21    Yes N/A  0   c0c5.2050.a500  001-rk-ww1
1/1/6      Up      Forward Full 10G   22    Yes N/A  0   c0c5.2050.a500  001-rk-ww2
1/1/7      Up      Forward Full 10G   31    Yes N/A  0   c0c5.2050.a500  001-rk-ni1
1/1/8      Down    None    None None  32    Yes N/A  0   c0c5.2050.a500  001-rk-ni2
1/1/9      Up      Forward Full 10G   41    Yes N/A  0   c0c5.2050.a500  001-rk-si1
1/1/10     Up      Forward Full 10G   51    Yes N/A  0   c0c5.2050.a500  001-rk-sd1
1/1/11     Up      Forward Full 10G   61    Yes N/A  0   c0c5.2050.a500  001-rk-eb1
1/1/12     Up      Forward Full 10G   71    Yes N/A  0   c0c5.2050.a500  001-rk-wb1
1/1/13     Down    None    None None  None  No  666  0   c0c5.2050.a50c
1/1/14     Down    None    None None  None  No  666  0   c0c5.2050.a50d
1/1/15     Down    None    None None  None  No  666  0   c0c5.2050.a50e
1/1/16     Down    None    None None  None  No  666  0   c0c5.2050.a50f
1/1/17     Down    None    None None  None  No  666  0   c0c5.2050.a510
1/1/18     Down    None    None None  None  No  666  0   c0c5.2050.a511
1/1/19     Down    None    None None  None  No  666  0   c0c5.2050.a512
1/1/20     Down    None    None None  None  No  666  0   c0c5.2050.a513
1/1/21     Down    None    None None  None  No  666  0   c0c5.2050.a514
1/1/22     Down    None    None None  None  No  666  0   c0c5.2050.a515
1/1/23     Down    None    None None  None  No  666  0   c0c5.2050.a516
1/1/24     Down    None    None None  None  No  666  0   c0c5.2050.a517
1/1/25     Down    None    None None  None  No  666  0   c0c5.2050.a518
1/1/26     Down    None    None None  None  No  666  0   c0c5.2050.a519
1/1/27     Down    None    None None  None  No  666  0   c0c5.2050.a51a
1/1/28     Down    None    None None  None  No  666  0   c0c5.2050.a51b
1/1/29     Up      Forward Full 1G    None  Yes 666  0   c0c5.2050.a500
1/1/30     Down    None    None None  None  No  1800 0   c0c5.2050.a51d
1/1/31     Down    None    None None  None  No  666  0   c0c5.2050.a51e
1/1/32     Down    None    None None  None  No  666  0   c0c5.2050.a51f
1/1/33     Down    None    None None  None  No  666  0   c0c5.2050.a520
1/1/34     Down    None    None None  None  No  666  0   c0c5.2050.a521
1/1/35     Down    None    None None  None  No  666  0   c0c5.2050.a522
1/1/36     Down    None    None None  None  No  666  0   c0c5.2050.a523
1/1/37     Down    None    None None  None  No  300  0   c0c5.2050.a500  001-NAS-A
1/1/38     Down    None    None None  None  No  300  0   c0c5.2050.a500  001-NAS-B
1/1/39     Down    None    None None  None  No  666  0   c0c5.2050.a526
1/1/40     Down    None    None None  None  No  1700 0   c0c5.2050.a500
1/1/41     Down    None    None None  None  No  1800 0   c0c5.2050.a528
1/1/42     Down    None    None None  None  No  1800 0   c0c5.2050.a529
1/1/43     Down    None    None None  None  No  666  0   c0c5.2050.a52a
1/1/44     Down    None    None None  None  No  666  0   c0c5.2050.a52b
1/1/45     Up      Forward Full 1G    7     Yes N/A  0   c0c5.2050.a500  w3750
1/1/46     Up      Forward Full 1G    7     Yes N/A  0   c0c5.2050.a500  w3750
1/1/47     Down    None    None None  None  No  666  0   c0c5.2050.a52e
1/1/48     Up      Forward Full 10G   None  Yes 666  0   c0c5.2050.a52f
1/2/1      Down    None    None None  None  No  666  0   c0c5.2050.a531
1/2/2      Down    None    None None  None  No  666  0   c0c5.2050.a535
1/2/3      Down    None    None None  None  No  666  0   c0c5.2050.a539
1/2/4      Down    None    None None  None  No  666  0   c0c5.2050.a53d
1/2/5      Up      Forward Full 40G   1     Yes N/A  0   c0c5.2050.a500
1/2/6      Up      Forward Full 40G   1     Yes N/A  0   c0c5.2050.a500
lg1        Up      Forward Full 80G   1     Yes N/A  0   c0c5.2050.a500
lg7        Up      Forward Full 2G    7     Yes N/A  0   c0c5.2050.a500  w3750
lg11       Up      Forward Full 10G   11    Yes N/A  0   c0c5.2050.a500  001-rk-mdf1
lg12       Up      Forward Full 10G   12    Yes N/A  0   c0c5.2050.a500  001-rk-mdf2
lg13       Up      Forward Full 10G   13    Yes N/A  0   c0c5.2050.a500  001-rk-mdf3
lg14       Up      Forward Full 10G   14    Yes N/A  0   c0c5.2050.a500  001-rk-mdf4
lg21       Up      Forward Full 10G   21    Yes N/A  0   c0c5.2050.a500  001-rk-ww1
lg22       Up      Forward Full 10G   22    Yes N/A  0   c0c5.2050.a500  001-rk-ww2
lg31       Up      Forward Full 10G   31    Yes N/A  0   c0c5.2050.a500  001-rk-ni1
lg32       Down    None    None None  32    Yes N/A  0   c0c5.2050.a500  001-rk-ni2
lg41       Up      Forward Full 10G   41    Yes N/A  0   c0c5.2050.a500  001-rk-si1
lg51       Up      Forward Full 10G   51    Yes N/A  0   c0c5.2050.a500  001-rk-sd1
lg61       Up      Forward Full 10G   61    Yes N/A  0   c0c5.2050.a500  001-rk-eb1
lg71       Up      Forward Full 10G   71    Yes N/A  0   c0c5.2050.a500  001-rk-wb1
mgmt1      Up      None    Full 1G    None  No  None 0   c0c5.2050.a500

Port       Link    State   Dupl Speed Trunk Tag Pvid Pri MAC             Name
ve1        Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve9        Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve10       Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve11       Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve12       Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve13       Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve14       Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve15       Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve16       Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve17       Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve18       Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve20       Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve21       Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve25       Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve32       Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve33       Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve35       Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve51       Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve52       Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve75       Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve77       Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve101      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve102      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve103      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve104      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve107      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve108      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve109      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve110      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve111      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve112      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve113      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve122      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve191      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve200      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve222      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve225      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve226      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve254      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve300      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve301      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve302      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve303      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve306      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve307      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve501      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve502      Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve1700     Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
ve4085     Up      N/A     N/A  N/A   None  N/A N/A  N/A c0c5.2050.a500
```

**Help:** execute the command "show interfaces brief"

**Prompt:**
- ruckus_fastiron>
- ruckus_fastiron#

### show mac-address

**Output:**
```

Total active entries from all ports = 93
MAC-Address     Port                 Type         VLAN 
70db.9895.73aa  1/2/1                Dynamic      3    
0010.20d0.b22b  1/1/2                Dynamic      10   
000f.7c0f.f387  2/1/11               Dynamic      3    
54bf.646f.d304  1/1/6                Dynamic      1    
000f.7c0f.f374  2/1/7                Dynamic      3    
70db.9895.73aa  1/2/1                Dynamic      5    
54bf.6479.a8de  1/1/22               Dynamic      2    
000f.7c0f.f385  2/1/18               Dynamic      3    
9890.96d9.f0ab  2/1/48               Dynamic      3    
e454.e85d.bfe1  1/1/48               Dynamic      4    
6c2b.59f8.ec1b  1/1/9                Dynamic      1    
000f.7c0f.f322  2/1/27               Dynamic      3    
0010.20ce.0655  1/1/2                Dynamic      10   
000f.7c0f.f320  2/1/28               Dynamic      3    
0010.20d1.1387  1/1/2                Dynamic      10   
184b.0d22.d780  1/1/5                Dynamic      5    
484d.7edb.1431  1/1/16               Dynamic      1    
0010.20d2.8b0d  1/1/2                Dynamic      10   
000f.7c0f.f324  2/1/30               Dynamic      3    
184b.0d22.48c0  1/1/1                Dynamic      5    
70db.9895.73ab  1/2/1                Dynamic      12   
MAC-Address     Port                 Type         VLAN 
0010.20d0.b23d  1/1/2                Dynamic      10   
0010.20d2.8afd  1/1/2                Dynamic      10   
184b.0d22.e2a0  1/1/2                Dynamic      5    
54bf.64a2.66c5  1/1/23               Dynamic      2    
6c2b.59ef.7457  1/1/27               Dynamic      1    
000f.7c15.7df0  2/1/38               Dynamic      3    
0010.20d0.b2a3  1/1/2                Dynamic      10   
000f.7c0f.f373  2/1/9                Dynamic      3    
000f.7c0f.f357  2/1/13               Dynamic      3    
70db.9895.73ab  1/2/1                Dynamic      666  
184b.0d22.4610  1/1/4                Dynamic      5    
000f.7c0f.f328  2/1/21               Dynamic      3    
0010.20cf.9f4d  1/1/2                Dynamic      10   
e454.e85d.9381  1/1/47               Dynamic      4    
000f.7c0f.f371  2/1/2                Dynamic      3    
000f.7c0f.f355  2/1/15               Dynamic      3    
70db.9895.73ab  1/2/1                Dynamic      1    
0010.20d2.8b2b  1/1/2                Dynamic      10   
6c2b.59e9.aa1c  1/1/20               Dynamic      2    
000f.7c0f.f382  2/1/12               Dynamic      3    
d89e.f344.6592  1/1/11               Dynamic      1    
000f.7c0f.f377  2/1/10               Dynamic      3    
MAC-Address     Port                 Type         VLAN 
184b.0d22.d920  1/1/3                Dynamic      5    
70db.9895.73aa  1/2/1                Dynamic      2    
000f.7c0f.f380  2/1/23               Dynamic      3    
000f.7c0f.f32c  2/1/31               Dynamic      3    
000f.7c10.683f  2/1/35               Dynamic      3    
000f.7c0f.f375  2/1/3                Dynamic      3    
70db.9895.73ab  1/2/1                Dynamic      5    
000f.7c0f.f386  2/1/14               Dynamic      3    
6400.6a01.18a6  1/1/18               Dynamic      1    
509a.4c4e.bb73  1/1/12               Dynamic      1    
000f.7c0f.f323  2/1/25               Dynamic      3    
70db.9895.73ab  1/2/1                Dynamic      7    
000f.7c0f.f384  2/1/22               Dynamic      3    
001a.ef5b.6804  1/1/4                Dynamic      10   
000f.7c15.7e23  2/1/34               Dynamic      3    
000f.7c15.7e07  2/1/37               Dynamic      3    
54bf.6474.f6bb  1/1/10               Dynamic      1    
d89e.f31b.48ea  1/1/17               Dynamic      1    
0010.40b3.a1de  1/1/2                Dynamic      10   
6c2b.59d6.b345  1/1/21               Dynamic      2    
000f.7c0f.f327  2/1/24               Dynamic      3    
70db.9895.73ab  1/2/1                Dynamic      11   
MAC-Address     Port                 Type         VLAN 
000f.7c0f.f325  2/1/29               Dynamic      3    
000f.7c0f.f352  2/1/19               Dynamic      3    
d89e.f344.64bc  1/1/46               Dynamic      4    
f8bc.128f.04ee  1/1/14               Dynamic      1    
000f.7c10.212e  2/1/32               Dynamic      3    
6c2b.59d6.9fcd  1/1/19               Dynamic      2    
6c2b.59dd.c6fa  1/1/8                Dynamic      1    
fa98.6b8a.a8b9  1/1/4                Dynamic      11   
d861.6240.f255  1/1/1                Dynamic      10   
54bf.6496.c555  1/1/7                Dynamic      1    
000f.7c0f.f372  2/1/4                Dynamic      3    
000f.7c14.fa31  2/1/26               Dynamic      3    
000f.7c0f.f356  2/1/33               Dynamic      3    
000f.7c0f.f383  2/1/8                Dynamic      3    
484d.7edb.1116  1/1/15               Dynamic      1    
000f.7c0f.f370  2/1/6                Dynamic      3    
000f.7c0f.f354  2/1/16               Dynamic      3    
000f.7c0f.16df  2/1/1                Dynamic      3    
70db.9895.73aa  1/2/1                Dynamic      1    
000f.7c0f.f381  2/1/17               Dynamic      3    
000f.7c0f.f32d  2/1/20               Dynamic      3    
000f.7c0f.f376  2/1/5                Dynamic      3    
MAC-Address     Port                 Type         VLAN 
70db.9895.73aa  1/2/1                Dynamic      10   
70db.9895.73aa  1/2/1                Dynamic      4    
70db.9895.73ab  1/2/1                Dynamic      10   
70db.9895.73ab  1/2/1                Dynamic      4    
70db.9895.73ab  1/2/1                Dynamic      3    
70db.9895.73ab  1/2/1                Dynamic      2    
```

**Help:** execute the command "show mac-address"

**Prompt:**
- ruckus_fastiron>
- ruckus_fastiron#

### show media validation

**Output:**
```
Port       Supported Vendor               Type
----------------------------------------------------------------------
1/2/1      No        CISCO-OEM             Type  : 10GE SR 300m (SFP+)
1/2/3      Yes       RUCKUS                Type  : 10GE SR 300m (SFP+)
1/3/1      Yes       RUCKUS                Type  : 40GBASE-Passive Copper 0.5m (QSFP+)
1/3/3      Yes       RUCKUS                Type  : 40GBASE-Passive Copper 0.5m (QSFP+)
2/2/1      No        OTHERS                Type  : 10GE SR 300m (SFP+)
2/3/1      Yes       RUCKUS                Type  : 40GBASE-Passive Copper 0.5m (QSFP+)
2/3/3      Yes       RUCKUS                Type  : 40GBASE-Passive Copper 0.5m (QSFP+)
```

**Help:** execute the command "show media validation"

**Prompt:**
- ruckus_fastiron>
- ruckus_fastiron#

### show version

**Output:**
```
  Copyright (c) Ruckus Networks, Inc. All rights reserved.
    UNIT 1: compiled on Feb 19 2019 at 13:48:49 labeled as SPS08090
      (28575972 bytes) from Primary SPS08090.bin (UFI)
        SW: Version 08.0.90T211
      Compressed Primary Boot Code size = 786944, Version:10.1.15T225 (mnz10115)
       Compiled on Thu Jan 31 01:08:55 2019
    UNIT 2: compiled on Feb 19 2019 at 13:48:49 labeled as SPS08090
      (28575972 bytes) from Primary SPS08090.bin (UFI)
        SW: Version 08.0.90T211
      Compressed Primary Boot Code size = 786944, Version:10.1.15T225 (mnz10115)

  HW: Stackable ICX7150-48-POEF
 ==========================================================================
 UNIT 1: SL 1: ICX7150-48PF-2X10G_2X1G POE 48-port Management Module
      Serial  #:FEE3816Q018
      Software Package: BASE_SOFT_PACKAGE
      Current License: 2X10G
      P-ASIC  0: type B160, rev 11  Chip BCM56160_B0
==========================================================================
 UNIT 1: SL 2: ICX7150-2X1GC 2-port 2G Module
==========================================================================
 UNIT 1: SL 3: ICX7150-4X10GF 4-port 40G Module
==========================================================================
 UNIT 2: SL 1: ICX7150-48PF-2X10G_2X1G POE 48-port Management Module
      Serial  #:FEE3816Q017
      Software Package: BASE_SOFT_PACKAGE
      Current License: 2X10G
==========================================================================
 UNIT 2: SL 2: ICX7150-2X1GC 2-port 2G Module
==========================================================================
 UNIT 2: SL 3: ICX7150-4X10GF 4-port 40G Module
==========================================================================
 1000 MHz ARM processor ARMv7 88 MHz bus
 8192 KB boot flash memory
 2048 MB code flash memory
 1024 MB DRAM
STACKID 1  system uptime is 24 day(s) 4 hour(s) 11 minute(s) 1 second(s)
STACKID 2  system uptime is 24 day(s) 4 hour(s) 11 minute(s) 1 second(s)
The system started at 18:28:15 Central Fri Dec 31 1999
 
The system : started=cold start
My stack unit ID = 1, bootup role = active


```

**Help:** execute the command "show version"

**Prompt:**
- ruckus_fastiron>
- ruckus_fastiron#

