# brocade_fastiron


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
- brocade_fastiron>

### configure terminal

**Output:** None

**Help:** enter the config mode

**Prompt:**
- brocade_fastiron#

### show monitor

**Output:**
```
Monitored Port 10
  Input mirrored by	:  18
  Output mirrored by	:  18
Monitored Port 16
  Input mirrored by	:  18
  Output mirrored by	:  18

```

**Help:** execute the command "show monitor"

**Prompt:**
- brocade_fastiron>
- brocade_fastiron#
- brocade_fastiron(config)#

### show interfaces

**Output:**
```
GigabitEthernet1 is up, line protocol is up 
  Hardware is GigabitEthernet, address is 001b.ed6b.2000 (bia 001b.ed6b.2000)
  Configured speed auto, actual 1Gbit, configured duplex fdx, actual fdx
  Configured mdi mode AUTO, actual MDI
  Member of 33 L2 VLANs, port is tagged, port state is FORWARDING
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper enabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Not member of any active trunks
  Not member of any configured trunks
  Port name is to MLX1-CLMAMOFW e2/2
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  300 second input rate: 36132912 bits/sec, 7764 packets/sec, 3.73% utilization
  300 second output rate: 81419992 bits/sec, 10603 packets/sec, 8.30% utilization
  1062555728308 packets input, 765022677409544 bytes, 0 no buffer
  Received 2859573621 broadcasts, 859758753 multicasts, 1058836395934 unicasts
  8 input errors, 1 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  1011812222301 packets output, 722190810166867 bytes, 0 underruns
  Transmitted 8889886882 broadcasts, 3251477712 multicasts, 999670857707 unicasts
  0 output errors, 0 collisions                                   
  Relay Agent Information option: Disabled
GigabitEthernet2 is up, line protocol is up 
  Hardware is GigabitEthernet, address is 001b.ed6b.2001 (bia 001b.ed6b.2001)
  Configured speed auto, actual 1Gbit, configured duplex fdx, actual fdx
  Configured mdi mode AUTO, actual MDIX
  Member of 102 L2 VLANs, port is dual mode in Vlan 1, port state is FORWARDING
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper enabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Not member of any active trunks
  Not member of any configured trunks
  Port name is switch1b-3
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  300 second input rate: 146823488 bits/sec, 28327 packets/sec, 15.13% utilization
  300 second output rate: 141339864 bits/sec, 26502 packets/sec, 14.55% utilization
  5491087012866 packets input, 3457816108549760 bytes, 0 no buffer
  Received 12860884133 broadcasts, 8441893951 multicasts, 5469784234782 unicasts
  2 input errors, 1 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  5813899509422 packets output, 4120086470555896 bytes, 0 underruns
  Transmitted 18098146569 broadcasts, 6209711839 multicasts, 5789591651014 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
GigabitEthernet3 is disabled, line protocol is down 
  Hardware is GigabitEthernet, address is 001b.ed6b.2002 (bia 001b.ed6b.2002)
  Configured speed auto, actual unknown, configured duplex fdx, actual unknown
  Configured mdi mode AUTO, actual unknown
  Member of L2 VLAN ID 1, port is untagged, port state is DISABLED
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper disabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Not member of any active trunks
  Not member of any configured trunks
  No port name
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  300 second input rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  300 second output rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  33390937805 packets input, 24077492513601 bytes, 0 no buffer
  Received 17757401 broadcasts, 159518105 multicasts, 33213662299 unicasts
  0 input errors, 0 CRC, 0 frame, 0 ignored                       
  0 runts, 0 giants
  397596845452 packets output, 196556265907165 bytes, 0 underruns
  Transmitted 88287163 broadcasts, 1149908125 multicasts, 396358650164 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
GigabitEthernet4 is disabled, line protocol is down 
  Hardware is GigabitEthernet, address is 001b.ed6b.2003 (bia 001b.ed6b.2003)
  Configured speed 1Gbit, actual unknown, configured duplex fdx, actual unknown
  Configured mdi mode AUTO, actual unknown
  Member of L2 VLAN ID 2033, port is untagged, port state is DISABLED
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper enabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Not member of any active trunks
  Not member of any configured trunks
  Port name is Boyce&Bynum INET Fiber 200 Portland, CLMA, MO
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  30 second input rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  30 second output rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  17293294617 packets input, 6427258200678 bytes, 0 no buffer     
  Received 559796 broadcasts, 44454276 multicasts, 17248280545 unicasts
  6 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  16334048713 packets output, 7618482738879 bytes, 0 underruns
  Transmitted 38137232 broadcasts, 276213 multicasts, 16295635268 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
GigabitEthernet5 is disabled, line protocol is down 
  Hardware is GigabitEthernet, address is 001b.ed6b.2004 (bia 001b.ed6b.2004)
  Configured speed 100Mbit, actual unknown, configured duplex fdx, actual unknown
  Configured mdi mode AUTO, actual unknown
  Member of L2 VLAN ID 1, port is untagged, port state is DISABLED
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper enabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Not member of any active trunks
  Not member of any configured trunks
  No port name
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  300 second input rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  300 second output rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  136280016 packets input, 22867608813 bytes, 0 no buffer
  Received 52700 broadcasts, 2376874 multicasts, 133850442 unicasts
  50639 input errors, 16113 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  378915648 packets output, 39836205125 bytes, 0 underruns
  Transmitted 4375536 broadcasts, 363833 multicasts, 374176279 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
GigabitEthernet6 is disabled, line protocol is down 
  Hardware is GigabitEthernet, address is 001b.ed6b.2005 (bia 001b.ed6b.2005)
  Configured speed auto, actual unknown, configured duplex fdx, actual unknown
  Configured mdi mode AUTO, actual unknown
  Member of L2 VLAN ID 1, port is untagged, port state is DISABLED
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper disabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Not member of any active trunks
  Not member of any configured trunks
  No port name
  IPG MII 96 bits-time, IPG GMII 96 bits-time                     
  IP MTU 10240 bytes
  30 second input rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  30 second output rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  365382054 packets input, 66047121122 bytes, 0 no buffer
  Received 618017 broadcasts, 8237 multicasts, 364755800 unicasts
  1352100 input errors, 486478 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  118120992828 packets output, 26874943907634 bytes, 0 underruns
  Transmitted 38604580 broadcasts, 33427120 multicasts, 118048961128 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
GigabitEthernet7 is up, line protocol is up 
  Hardware is GigabitEthernet, address is 001b.ed6b.2006 (bia 001b.ed6b.2006)
  Configured speed auto, actual 1Gbit, configured duplex fdx, actual fdx
  Configured mdi mode AUTO, actual MDIX
  Member of 1 L2 VLANs, port is tagged, port state is FORWARDING
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper enabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Not member of any active trunks
  Not member of any configured trunks                             
  Port name is ms1a (4B-7)
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  30 second input rate: 95952 bits/sec, 134 packets/sec, 0.00% utilization
  30 second output rate: 3006184 bits/sec, 403 packets/sec, 0.30% utilization
  224220415361 packets input, 273827759119157 bytes, 0 no buffer
  Received 208722 broadcasts, 277126 multicasts, 224219929513 unicasts
  0 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  196413848432 packets output, 60402291469127 bytes, 0 underruns
  Transmitted 5149342419 broadcasts, 432774605 multicasts, 190831731408 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
GigabitEthernet8 is disabled, line protocol is down 
  Hardware is GigabitEthernet, address is 001b.ed6b.2007 (bia 001b.ed6b.2007)
  Configured speed auto, actual unknown, configured duplex fdx, actual unknown
  Configured mdi mode AUTO, actual unknown
  Member of L2 VLAN ID 1, port is untagged, port state is DISABLED
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper disabled, negotiation disabled
  Mirror disabled, Monitor disabled                               
  Not member of any active trunks
  Not member of any configured trunks
  No port name
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  300 second input rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  300 second output rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  1866090726 packets input, 1347732480937 bytes, 0 no buffer
  Received 4921358 broadcasts, 4074011 multicasts, 1857095357 unicasts
  0 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  33026732592 packets output, 9461647968648 bytes, 0 underruns
  Transmitted 811305665 broadcasts, 359636667 multicasts, 31855790260 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
GigabitEthernet9 is up, line protocol is up 
  Hardware is GigabitEthernet, address is 001b.ed6b.2008 (bia 001b.ed6b.2008)
  Configured speed auto, actual 1Gbit, configured duplex fdx, actual fdx
  Configured mdi mode AUTO, actual MDIX
  Member of L2 VLAN ID 450, port is untagged, port state is FORWARDING
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0                        
  Flow Control is config enabled, oper enabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Not member of any active trunks
  Not member of any configured trunks
  Port name is warehouse1
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  300 second input rate: 27576 bits/sec, 3 packets/sec, 0.00% utilization
  300 second output rate: 47872 bits/sec, 74 packets/sec, 0.00% utilization
  59426196640 packets input, 80817825988147 bytes, 0 no buffer
  Received 1997812 broadcasts, 444136 multicasts, 59423754692 unicasts
  0 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  34732344432 packets output, 3429657691197 bytes, 0 underruns
  Transmitted 5967219873 broadcasts, 704148686 multicasts, 28060975873 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
GigabitEthernet10 is up, line protocol is up 
  Hardware is GigabitEthernet, address is 001b.ed6b.2009 (bia 001b.ed6b.2009)
  Configured speed auto, actual 1Gbit, configured duplex fdx, actual fdx
  Configured mdi mode AUTO, actual MDI
  Member of L2 VLAN ID 152, port is untagged, port state is FORWARDING
  BPDU guard is Disabled, ROOT protect is Disabled                
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper enabled, negotiation disabled
  Mirror disabled, Monitor enabled (input and output)
  Not member of any active trunks
  Not member of any configured trunks
  Port name is sbc1.voip.sockettelecom.com-VoIP
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  300 second input rate: 42858536 bits/sec, 24456 packets/sec, 4.67% utilization
  300 second output rate: 43002584 bits/sec, 24589 packets/sec, 4.68% utilization
  434184856717 packets input, 95128491268061 bytes, 0 no buffer
  Received 7297822 broadcasts, 238122 multicasts, 434177320773 unicasts
  106 input errors, 38 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  437616203913 packets output, 95510650536391 bytes, 0 underruns
  Transmitted 50386350 broadcasts, 50385910 multicasts, 437515431653 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
GigabitEthernet11 is up, line protocol is up 
  Hardware is GigabitEthernet, address is 001b.ed6b.200a (bia 001b.ed6b.200a)
  Configured speed auto, actual 1Gbit, configured duplex fdx, actual fdx
  Configured mdi mode AUTO, actual MDIX                           
  Member of 69 L2 VLANs, port is dual mode in Vlan 1, port state is FORWARDING
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper enabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Not member of any active trunks
  Not member of any configured trunks
  Port name is OPTI1-MS13-1 to XO
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  30 second input rate: 251200424 bits/sec, 86193 packets/sec, 26.49% utilization
  30 second output rate: 229451128 bits/sec, 86435 packets/sec, 24.32% utilization
  5873913848979 packets input, 3442283177781007 bytes, 0 no buffer
  Received 13369699781 broadcasts, 5083498868 multicasts, 5855460650330 unicasts
  0 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  6089793610508 packets output, 3506587229877936 bytes, 0 underruns
  Transmitted 5852894414 broadcasts, 5681533710 multicasts, 6078259182384 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
GigabitEthernet12 is disabled, line protocol is down 
  Hardware is GigabitEthernet, address is 001b.ed6b.200b (bia 001b.ed6b.200b)
  Configured speed auto, actual unknown, configured duplex fdx, actual unknown
  Configured mdi mode AUTO, actual unknown
  Member of L2 VLAN ID 1, port is untagged, port state is DISABLED
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper disabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Not member of any active trunks
  Not member of any configured trunks
  No port name
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  300 second input rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  300 second output rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  57522699855 packets input, 24508739775548 bytes, 0 no buffer
  Received 5443757 broadcasts, 1560252 multicasts, 57515695846 unicasts
  0 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  44453437300 packets output, 10271900455982 bytes, 0 underruns
  Transmitted 18130416 broadcasts, 5920878 multicasts, 44429386006 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled                        
GigabitEthernet13 is disabled, line protocol is down 
  Hardware is GigabitEthernet, address is 001b.ed6b.200c (bia 001b.ed6b.200c)
  Configured speed 1Gbit, actual unknown, configured duplex fdx, actual unknown
  Configured mdi mode AUTO, actual unknown
  Member of L2 VLAN ID 1, port is untagged, port state is DISABLED
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper enabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Not member of any active trunks
  Not member of any configured trunks
  No port name
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  300 second input rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  300 second output rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  574462764093 packets input, 402613835806904 bytes, 0 no buffer
  Received 25702257 broadcasts, 218863600 multicasts, 574218198236 unicasts
  4 input errors, 2 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  307428412392 packets output, 123203150572196 bytes, 0 underruns
  Transmitted 148790455 broadcasts, 1158554078 multicasts, 306121067859 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
GigabitEthernet14 is down, line protocol is down 
  Hardware is GigabitEthernet, address is 001b.ed6b.200d (bia 001b.ed6b.200d)
  Configured speed auto, actual unknown, configured duplex fdx, actual unknown
  Configured mdi mode AUTO, actual unknown
  Member of L2 VLAN ID 154, port is untagged, port state is BLOCKING
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper disabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Not member of any active trunks
  Not member of any configured trunks
  Port name is SocketVoIP-DBS1
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  30 second input rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  30 second output rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  4007809813 packets input, 2598671668225 bytes, 0 no buffer
  Received 732505 broadcasts, 796397 multicasts, 4006280911 unicasts
  61 input errors, 30 CRC, 0 frame, 0 ignored
  0 runts, 0 giants                                               
  4281434344 packets output, 3069521551725 bytes, 0 underruns
  Transmitted 35488631 broadcasts, 7395902 multicasts, 4238549811 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
GigabitEthernet15 is disabled, line protocol is down 
  Hardware is GigabitEthernet, address is 001b.ed6b.200e (bia 001b.ed6b.200e)
  Configured speed auto, actual unknown, configured duplex fdx, actual unknown
  Configured mdi mode AUTO, actual unknown
  Member of L2 VLAN ID 1, port is untagged, port state is DISABLED
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper disabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Not member of any active trunks
  Not member of any configured trunks
  No port name
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  300 second input rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  300 second output rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  425136597160 packets input, 224837228841386 bytes, 0 no buffer
  Received 1784872332 broadcasts, 14229303 multicasts, 423337495525 unicasts
  0 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  67426866239 packets output, 56310572280892 bytes, 0 underruns
  Transmitted 1195449599 broadcasts, 636407794 multicasts, 65595008846 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
GigabitEthernet16 is up, line protocol is up 
  Hardware is GigabitEthernet, address is 001b.ed6b.200f (bia 001b.ed6b.200f)
  Configured speed auto, actual 1Gbit, configured duplex fdx, actual fdx
  Configured mdi mode AUTO, actual MDI
  Member of L2 VLAN ID 149, port is untagged, port state is FORWARDING
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper enabled, negotiation disabled
  Mirror disabled, Monitor enabled (input and output)
  Not member of any active trunks
  Not member of any configured trunks
  Port name is sbc1.voip.sockettelecom.com-Public
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  300 second input rate: 56531256 bits/sec, 32360 packets/sec, 6.16% utilization
  300 second output rate: 56512912 bits/sec, 32356 packets/sec, 6.16% utilization
  524015863289 packets input, 116094187547734 bytes, 0 no buffer
  Received 53833717 broadcasts, 238134 multicasts, 523961791438 unicasts
  42 input errors, 17 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  523743357542 packets output, 115906867765047 bytes, 0 underruns
  Transmitted 183579591 broadcasts, 46484853 multicasts, 523513293098 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
 GigabitEthernet17 is up, line protocol is up 
  Hardware is GigabitEthernet, address is 001b.ed6b.2010 (bia 001b.ed6b.2010)
  Configured speed 100Mbit, actual 100Mbit, configured duplex fdx, actual fdx
  Configured mdi mode AUTO, actual MDI
  Member of L2 VLAN ID 2277, port is untagged, port state is FORWARDING
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper enabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Not member of any active trunks
  Not member of any configured trunks
  Port name is Memory Book INET
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes                                              
  30 second input rate: 163104 bits/sec, 287 packets/sec, 0.20% utilization
  30 second output rate: 6878392 bits/sec, 590 packets/sec, 6.96% utilization
  67457723991 packets input, 65859234276036 bytes, 0 no buffer
  Received 696887484 broadcasts, 294342200 multicasts, 66466494307 unicasts
  550394678 input errors, 97937713 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  51840520968 packets output, 27141276257128 bytes, 0 underruns
  Transmitted 20614211 broadcasts, 1422508 multicasts, 51818484249 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
GigabitEthernet18 is up, line protocol is up 
  Hardware is GigabitEthernet, address is 001b.ed6b.2011 (bia 001b.ed6b.2011)
  Configured speed auto, actual 1Gbit, configured duplex fdx, actual fdx
  Configured mdi mode AUTO, actual MDIX
  Member of L2 VLAN ID 1, port is untagged, port state is FORWARDING
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper enabled, negotiation disabled
  Mirror enabled, Monitor disabled
  Not member of any active trunks
  Not member of any configured trunks
  Port name is voipmon1-p1p2                                      
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  30 second input rate: 0 bits/sec, 0 packets/sec, 0.00% utilization
  30 second output rate: 214333840 bits/sec, 120313 packets/sec, 23.35% utilization
  47421168960 packets input, 21330444001424 bytes, 0 no buffer
  Received 11319269 broadcasts, 100537 multicasts, 47409749154 unicasts
  14 input errors, 6 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  1381311191190 packets output, 366733951388972 bytes, 0 underruns
  Transmitted 1026021322 broadcasts, 434328968 multicasts, 1379850840900 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
GigabitEthernet19 is up, line protocol is up 
  Hardware is GigabitEthernet, address is 001b.ed6b.2012 (bia 001b.ed6b.2012)
  Configured speed auto, actual 1Gbit, configured duplex fdx, actual fdx
  Configured mdi mode AUTO, actual MDIX
  Member of 1 L2 VLANs, port is tagged, port state is FORWARDING
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper enabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Not member of any active trunks                                 
  Not member of any configured trunks
  Port name is vmail1.voip
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  300 second input rate: 818984 bits/sec, 88 packets/sec, 0.07% utilization
  300 second output rate: 129120 bits/sec, 54 packets/sec, 0.01% utilization
  17243558469 packets input, 22434976239119 bytes, 0 no buffer
  Received 143775 broadcasts, 234508 multicasts, 17243180186 unicasts
  0 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  9809188575 packets output, 2060714655702 bytes, 0 underruns
  Transmitted 42232043 broadcasts, 8108467 multicasts, 9758848065 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
GigabitEthernet20 is up, line protocol is up 
  Hardware is GigabitEthernet, address is 001b.ed6b.2013 (bia 001b.ed6b.2013)
  Configured speed 100Mbit, actual 100Mbit, configured duplex fdx, actual fdx
  Configured mdi mode AUTO, actual MDIX
  Member of L2 VLAN ID 152, port is untagged, port state is FORWARDING
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper enabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Not member of any active trunks
  Not member of any configured trunks
  Port name is VoIP-ASA-Internal
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  300 second input rate: 604816 bits/sec, 96 packets/sec, 0.61% utilization
  300 second output rate: 381696 bits/sec, 93 packets/sec, 0.39% utilization
  19358089965 packets input, 5913888345210 bytes, 0 no buffer
  Received 142540 broadcasts, 14939793 multicasts, 19343007632 unicasts
  2 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  31825930639 packets output, 38028095856602 bytes, 0 underruns
  Transmitted 58935076 broadcasts, 36437328 multicasts, 31730558235 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
GigabitEthernet21 is up, line protocol is up 
  Hardware is GigabitEthernet, address is 001b.ed6b.2014 (bia 001b.ed6b.2014)
  Configured speed 100Mbit, actual 100Mbit, configured duplex fdx, actual fdx
  Configured mdi mode AUTO, actual MDIX
  Member of L2 VLAN ID 149, port is untagged, port state is FORWARDING
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled                                
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper enabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Not member of any active trunks
  Not member of any configured trunks
  Port name is VoIP-ASA-External
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  300 second input rate: 381296 bits/sec, 93 packets/sec, 0.39% utilization
  300 second output rate: 607304 bits/sec, 100 packets/sec, 0.61% utilization
  31736519059 packets input, 38022380885593 bytes, 0 no buffer
  Received 22277 broadcasts, 0 multicasts, 31736496782 unicasts
  0 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  19672648738 packets output, 5937049134598 bytes, 0 underruns
  Transmitted 241311821 broadcasts, 47443808 multicasts, 19383893109 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
 GigabitEthernet22 is up, line protocol is up 
  Hardware is GigabitEthernet, address is 001b.ed6b.2015 (bia 001b.ed6b.2015)
  Configured speed auto, actual 1Gbit, configured duplex fdx, actual fdx
  Configured mdi mode AUTO, actual MDI
  Member of 1 L2 VLANs, port is tagged, port state is FORWARDING  
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper enabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Not member of any active trunks
  Not member of any configured trunks
  Port name is md1a (2B-1)
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  300 second input rate: 5098944 bits/sec, 715 packets/sec, 0.51% utilization
  300 second output rate: 5116928 bits/sec, 976 packets/sec, 0.52% utilization
  68111921559 packets input, 75022095965149 bytes, 0 no buffer
  Received 60304 broadcasts, 277247 multicasts, 68111584008 unicasts
  0 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  118435866121 packets output, 44194584961407 bytes, 0 underruns
  Transmitted 5149570277 broadcasts, 432776444 multicasts, 112853519400 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
GigabitEthernet23 is up, line protocol is up 
  Hardware is GigabitEthernet, address is 001b.ed6b.2016 (bia 001b.ed6b.2016)
  Configured speed auto, actual 1Gbit, configured duplex fdx, actual fdx
  Configured mdi mode AUTO, actual MDIX
  Member of 16 L2 VLANs, port is dual mode in Vlan 1, port state is FORWARDING
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper enabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Not member of any active trunks
  Not member of any configured trunks
  Port name is MPLSPPP1-G0/1
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  300 second input rate: 22374504 bits/sec, 3857 packets/sec, 2.29% utilization
  300 second output rate: 22465040 bits/sec, 3866 packets/sec, 2.30% utilization
  41020960466 packets input, 23447533535742 bytes, 0 no buffer
  Received 9510500 broadcasts, 263946197 multicasts, 40747503769 unicasts
  38 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  39448761031 packets output, 24063276149536 bytes, 0 underruns
  Transmitted 369728855 broadcasts, 1376474576 multicasts, 37702557600 unicasts
  0 output errors, 0 collisions
  Relay Agent Information option: Disabled
GigabitEthernet24 is up, line protocol is up                      
  Hardware is GigabitEthernet, address is 001b.ed6b.2017 (bia 001b.ed6b.2017)
  Configured speed auto, actual 100Mbit, configured duplex fdx, actual fdx
  Configured mdi mode AUTO, actual MDIX
  Member of L2 VLAN ID 450, port is untagged, port state is FORWARDING
  BPDU guard is Disabled, ROOT protect is Disabled
  Link Error Dampening is Disabled
  STP configured to ON, priority is level0
  Flow Control is config enabled, oper enabled, negotiation disabled
  Mirror disabled, Monitor disabled
  Not member of any active trunks
  Not member of any configured trunks
  Port name is Socket Office MPLS
  IPG MII 96 bits-time, IPG GMII 96 bits-time
  IP MTU 10240 bytes
  30 second input rate: 8504 bits/sec, 3 packets/sec, 0.00% utilization
  30 second output rate: 64928 bits/sec, 108 packets/sec, 0.07% utilization
  1819852606 packets input, 434041256645 bytes, 0 no buffer
  Received 34 broadcasts, 2546245 multicasts, 1817306327 unicasts
  0 input errors, 0 CRC, 0 frame, 0 ignored
  0 runts, 0 giants
  9148279772 packets output, 3489842845205 bytes, 0 underruns
  Transmitted 5954167784 broadcasts, 678793901 multicasts, 2515318087 unicasts
  0 output errors, 0 collisions                                   
  Relay Agent Information option: Disabled

```

**Help:** execute the command "show interfaces"

**Prompt:**
- brocade_fastiron>
- brocade_fastiron#
- brocade_fastiron(config)#

### show lldp neighbors detail

**Output:**
```
Local port: 1/1/2
  Neighbor: 00a0.c85a.a3dd, TTL 118 seconds
    + Chassis ID (MAC address): 00a0.c836.37c8
    + Port ID (locally assigned): "Gigabit-Ethernet 1/A/1"
    + Time to live: 120 seconds
    + Management address (IPv4): 10.255.5.98
    + System name         : "CLMAMOXR-TA5000B"
    + System capabilities : bridge
      Enabled capabilities: bridge

 Local port: 1/1/24
  Neighbor: 609c.9f44.bbf0, TTL 97 seconds
    + Chassis ID (MAC address): cc4e.24c5.57fc
    + Port ID (MAC address): 609c.9f44.bbf0
    + Time to live: 120 seconds
    + System name         : "switch2.clmamoxi"
    + Port description    : "GigabitEthernet2/1/1"
    + System capabilities : bridge
      Enabled capabilities: bridge
    + 802.3 MAC/PHY          : auto-negotiation enabled
      Advertised capabilities: fdxSPause, fdxBPause
      Operational MAU type   : 1000BaseT-FD
    + Link aggregation: aggregated (aggregated port ifIndex: 257)
    + Maximum frame size: 10200 octets                            
    + Port VLAN ID: none
    + Management address (IPv4): 10.255.13.22

Local port: 1/3/1
  Neighbor: 609c.9f44.bc13, TTL 113 seconds
    + Chassis ID (MAC address): cc4e.24c5.57fc
    + Port ID (MAC address): 609c.9f44.bc13
    + Time to live: 120 seconds
    + System name         : "switch2.clmamoxi"
    + Port description    : "10GigabitEthernet2/3/1"
    + System capabilities : bridge
      Enabled capabilities: bridge
    + 802.3 MAC/PHY          : auto-negotiation supported, but disabled
      Operational MAU type   : 10GigBaseER
    + Link aggregation: aggregated (aggregated port ifIndex: 385)
    + Maximum frame size: 10200 octets
    + Port VLAN ID: none
    + Management address (IPv4): 10.255.13.22

Local port: 1/3/2
  Neighbor: 609c.9f44.bc14, TTL 113 seconds
    + Chassis ID (MAC address): cc4e.24c5.57fc
    + Port ID (MAC address): 609c.9f44.bc14                       
    + Time to live: 120 seconds
    + System name         : "switch2.clmamoxi"
    + Port description    : "10GigabitEthernet2/3/2"
    + System capabilities : bridge
      Enabled capabilities: bridge
    + 802.3 MAC/PHY          : auto-negotiation supported, but disabled
      Operational MAU type   : 10GigBaseER
    + Link aggregation: aggregated (aggregated port ifIndex: 385)
    + Maximum frame size: 10200 octets
    + Port VLAN ID: none
    + Management address (IPv4): 10.255.13.22

Local port: 2/1/1
  Neighbor: cc4e.24c7.ccd4, TTL 107 seconds
    + Chassis ID (MAC address): cc4e.24c7.ccd4
    + Port ID (MAC address): cc4e.24c7.ccd4
    + Time to live: 120 seconds
    + System name         : "Switch2.CLMAMOXH"
    + Port description    : "GigabitEthernet1/1/1"
    + System capabilities : bridge
      Enabled capabilities: bridge
    + 802.3 MAC/PHY          : auto-negotiation enabled
      Advertised capabilities:                                    
      Operational MAU type   : 1000BaseT-FD
    + Link aggregation: aggregated (aggregated port ifIndex: 1)
    + Maximum frame size: 10200 octets
    + Port VLAN ID: none
    + Management address (IPv4): 10.255.13.2
 
Local port: 2/3/1
  Neighbor: cc4e.24c7.af6f, TTL 112 seconds
    + Chassis ID (MAC address): cc4e.24c7.ccd4
    + Port ID (MAC address): cc4e.24c7.af6f
    + Time to live: 120 seconds
    + System name         : "Switch2.CLMAMOXH"
    + Port description    : "10GigabitEthernet2/3/1"
    + System capabilities : bridge
      Enabled capabilities: bridge
    + 802.3 MAC/PHY          : auto-negotiation supported, but disabled
      Operational MAU type   : 10GigBaseER
    + Link aggregation: aggregated (aggregated port ifIndex: 385)
    + Maximum frame size: 10200 octets
    + Port VLAN ID: none
    + Management address (IPv4): 10.255.13.2

Local port: 2/3/2                                                 
  Neighbor: cc4e.24c7.af71, TTL 112 seconds
    + Chassis ID (MAC address): cc4e.24c7.ccd4
    + Port ID (MAC address): cc4e.24c7.af71
    + Time to live: 120 seconds
    + System name         : "Switch2.CLMAMOXH"
    + Port description    : "10GigabitEthernet2/3/3"
    + System capabilities : bridge
      Enabled capabilities: bridge
    + 802.3 MAC/PHY          : auto-negotiation supported, but disabled
      Operational MAU type   : 10GigBaseER
    + Link aggregation: aggregated (aggregated port ifIndex: 385)
    + Maximum frame size: 10200 octets
    + Port VLAN ID: none
    + Management address (IPv4): 10.255.13.2


```

**Help:** execute the command "show lldp neighbors detail"

**Prompt:**
- brocade_fastiron>
- brocade_fastiron#
- brocade_fastiron(config)#

### show arp

**Output:**
```
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.51.250.70           94   64f6.9d1e.a4bf  ARPA   Vlan10
Internet  10.51.250.120           -   fc5b.394a.5a7f  ARPA   Vlan10
Internet  10.51.250.1             0   0010.dbff.1002  ARPA   Vlan10
Internet  10.51.250.7            81   046c.9d67.7746  ARPA   Vlan10
Internet  10.51.250.8            67   9c57.ad1e.4b46  ARPA   Vlan10
```

**Help:** execute the command "show arp"

**Prompt:**
- brocade_fastiron>
- brocade_fastiron#
- brocade_fastiron(config)#

### show running-config vlan

**Output:**
```
vlan 1 name DEFAULT-VLAN by port
 no spanning-tree
!
vlan 10 name CLMAMO-RING-1 by port
 tagged ethe 2 ethe 11 
 no spanning-tree
 metro-ring 10
  ring-interfaces  ethernet 11  ethernet 2
  enable
!
vlan 13 name SocketPublicWifi by port
 tagged ethe 1 to 2 
 no spanning-tree
!
vlan 14 name CLMAMOFW-Ring by port
 tagged ethe 1 to 2 
 no spanning-tree
 metro-ring 14
  ring-interfaces  ethernet 1  ethernet 2
  enable
!
vlan 100 by port
 tagged ethe 1 to 2 
 no spanning-tree                                                 
!
 vlan 146 name LabSBC-External by port
 tagged ethe 2 ethe 11 
 no spanning-tree
 !
vlan 149 name SBC-External by port
 tagged ethe 2 ethe 11 
 untagged ethe 16 ethe 21 
 no spanning-tree
!
vlan 151 name LabSBC-Internal by port
 tagged ethe 2 ethe 11 
 no spanning-tree
!
vlan 152 name SBC-Inside by port
 tagged ethe 2 ethe 11 
 untagged ethe 10 ethe 20 
 no spanning-tree
!
vlan 154 name SocketVoIP-Svr by port
 tagged ethe 2 ethe 11 ethe 19 
 untagged ethe 14 
 no spanning-tree                                                 
!
 vlan 175 name CLMAMO10G-to-FW by port
 tagged ethe 1 to 2 
 no spanning-tree
 metro-ring 176
  ring-interfaces  ethernet 1  ethernet 2
  enable
  name CLMAMOFW-to-CLMAMO10G
```

**Help:** execute the command "show running-config vlan"

**Prompt:**
- brocade_fastiron>
- brocade_fastiron#
- brocade_fastiron(config)#

### show lag brief

**Output:**
```
Total number of LAGs:          4
Total number of deployed LAGs: 4
 Total number of trunks created:4 (116 available)
LACP System Priority / ID:     1 / cc4e.2415.015e
LACP Long timeout:             90, default: 90
LACP Short timeout:            3, default: 3

LAG           Type   Deploy Trunk Primary  Port List
10G-Lag2      dynamic  Y    5     2/3/1    e 2/3/1 to 2/3/2
1G-Lag        dynamic  Y    3     1/1/24   e 1/1/24
1G-Lag-2      dynamic  Y    4     2/1/1    e 2/1/1
SW2.XR-SW1A.TEdynamic  Y    1     1/3/1    e 1/3/1 to 1/3/2

```

**Help:** execute the command "show lag brief"

**Prompt:**
- brocade_fastiron>
- brocade_fastiron#
- brocade_fastiron(config)#

### show trunk

**Output:**
```

Configured trunks:

Trunk ID: 5
Hw Trunk ID: 1
Ports_Configured: 2
Primary Port Monitored: Jointly

Ports         5       23      
Port Names    none    none    
Port_Status   enable  enable  
Monitor       off     off     
Rx Mirr Port  N/A     N/A     
Tx Mirr Port  N/A     N/A     
 Monitor Dir   N/A     N/A     

Operational trunks:

Trunk ID: 5
Hw Trunk ID: 1
Duplex: Full
Speed: 1G
Tag: Yes
Priority: level0                                                  
Active Ports: 2

Ports         5       23      
Link_Status   active  active  
port_state    Forward Forward 
LACP_Status   ready   ready   

```

**Help:** execute the command "show trunk"

**Prompt:**
- brocade_fastiron>
- brocade_fastiron#
- brocade_fastiron(config)#

### show interfaces brief

**Output:**
```

Port    Link    State   Dupl Speed Trunk Tag Pvid Pri MAC            Name      
1       Up      Forward Full 1G    None  Yes N/A  0   001b.ed6b.2000  to MLX1-
2       Up      Forward Full 1G    None  Yes 1    0   001b.ed6b.2001  switch1b
3       Disable None    None None  None  No  1    0   001b.ed6b.2002          
4       Disable None    None None  None  No  2033 0   001b.ed6b.2003  Boyce&By
5       Disable None    None None  None  No  1    0   001b.ed6b.2004          
6       Disable None    None None  None  No  1    0   001b.ed6b.2005          
7       Up      Forward Full 1G    None  Yes N/A  0   001b.ed6b.2006  ms1a (4B
8       Disable None    None None  None  No  1    0   001b.ed6b.2007          
9       Up      Forward Full 1G    None  No  450  0   001b.ed6b.2008  warehous
10      Up      Forward Full 1G    None  No  152  0   001b.ed6b.2009  sbc1.voi
11      Up      Forward Full 1G    None  Yes 1    0   001b.ed6b.200a  OPTI1-MS
12      Disable None    None None  None  No  1    0   001b.ed6b.200b          
13      Disable None    None None  None  No  1    0   001b.ed6b.200c          
14      Down    None    None None  None  No  154  0   001b.ed6b.200d  SocketVo
15      Disable None    None None  None  No  1    0   001b.ed6b.200e          
16      Up      Forward Full 1G    None  No  149  0   001b.ed6b.200f  sbc1.voi
17      Up      Forward Full 100M  None  No  2277 0   001b.ed6b.2010  Memory B
18      Up      Forward Full 1G    None  No  1    0   001b.ed6b.2011  voipmon1
19      Up      Forward Full 1G    None  Yes N/A  0   001b.ed6b.2012  vmail1.v
20      Up      Forward Full 100M  None  No  152  0   001b.ed6b.2013  VoIP-ASA
21      Up      Forward Full 100M  None  No  149  0   001b.ed6b.2014  VoIP-ASA
22      Up      Forward Full 1G    None  Yes N/A  0   001b.ed6b.2015  md1a (2B
23      Up      Forward Full 1G    None  Yes 1    0   001b.ed6b.2016  MPLSPPP1
24      Up      Forward Full 100M  None  No  450  0   001b.ed6b.2017  Socket O

```

**Help:** execute the command "show interfaces brief"

**Prompt:**
- brocade_fastiron>
- brocade_fastiron#
- brocade_fastiron(config)#

### show topo

**Output:**
```
Topology Group 10
=================
 master-vlan 10
 member-vlan 146 149 151 to 152 154 200 300 to 303 350 400 453 1280 to 1283
 member-vlan 1295 1335 1395 2005 2022 2024 2030 2033 2035 2039 2049 to 2050
 member-vlan 2054 2069 to 2070 2086 2091 to 2092 2096 to 2097 2099 to 2100
 member-vlan 2129 2184 2188 to 2189 2204 2215 2226 2241 to 2242 2250 2253
 member-vlan 2277 2325 to 2326 2340 2342 2349 to 2351 2360 2367 2414 to 2415
 member-vlan 2442 2895 3008 3840 4001

 Common control ports           L2 protocol         
 ethernet 1/1/24                MRP                 
 ethernet 2/1/1                 MRP                 
 Per vlan free ports                                
 ethernet 1/1/3                  Vlan 10            
 ethernet 1/1/4                  Vlan 10            
 ethernet 1/1/5                  Vlan 10            
 ethernet 1/1/7                  Vlan 10            
 ethernet 1/1/8                  Vlan 10            
 ethernet 1/1/2                  Vlan 400           
 ethernet 2/1/2                  Vlan 400           
 ethernet 1/1/2                  Vlan 2342          
 ethernet 2/1/2                  Vlan 2342          
                                                                  
Topology Group 13
=================
 master-vlan 513
 member-vlan 94 207 223 to 224 280 to 282 290 310 to 311 320 to 321 330 to 331
 member-vlan 340 345 355 360 365 375 380 385 390 401 517 to 518 619 623 999
 member-vlan 1290 1345 1355 to 1356 1380 1385 1390 2004 2006 2011 2018 2043
 member-vlan 2045 to 2046 2058 to 2059 2063 to 2065 2072 2075 2102 2104 to 2107
 member-vlan 2133 2137 2173 2180 to 2181 2190 2195 2197 2199 to 2200 2235
 member-vlan 2257 2261 2265 2267 2270 to 2272 2274 2278 2282 2284 to 2287
 member-vlan 2293 to 2296 2298 2301 to 2302 2305 to 2306 2314 to 2317
 member-vlan 2320 2323 to 2324 2329 2332 2343 to 2345 2352 to 2353 2355
 member-vlan 2357 2359 2362 to 2363 2366 2368 to 2369 2372 2374 to 2376
 member-vlan 2379 2381 2384 2386 to 2387 2393 2395 2399 to 2401 2403 2408
 member-vlan 2412 2416 2418 to 2420 2435 to 2440 2443 to 2446 2449 to 2451
 member-vlan 2453 to 2456 2460 2466 to 2470 2472 2475 2483 2571 2575 to 2576
 member-vlan 2718 2766 3004 3006 to 3007

 Common control ports           L2 protocol         
 ethernet 1/3/1                 MRP                 
 ethernet 1/3/2                 MRP                 
 ethernet 2/3/1                 MRP                 
 ethernet 2/3/2                 MRP                 
 Per vlan free ports                                              
 ethernet 1/1/2                  Vlan 330           
 ethernet 1/1/6                  Vlan 330           
 ethernet 2/1/2                  Vlan 330           
 ethernet 1/1/2                  Vlan 331           
 ethernet 2/1/2                  Vlan 331           
 ethernet 1/1/24                 Vlan 360           
 ethernet 2/1/1                  Vlan 360           
 ethernet 1/1/2                  Vlan 2006          
 ethernet 2/1/2                  Vlan 2006          
 ethernet 1/1/2                  Vlan 2058          
 ethernet 2/1/2                  Vlan 2058          
 ethernet 2/1/1                  Vlan 2063          
 ethernet 1/1/2                  Vlan 2282          
 ethernet 2/1/2                  Vlan 2282          
 ethernet 1/1/2                  Vlan 2352          
 ethernet 2/1/2                  Vlan 2352          
 ethernet 1/1/24                 Vlan 2403          
 ethernet 2/1/1                  Vlan 2403          

Topology Group 60
=================
 master-vlan 60
 member-vlan 2371 2481                                            

 Common control ports           L2 protocol         
 ethernet 1/3/1                 MRP                 
 ethernet 1/3/2                 MRP                 
 ethernet 2/3/1                 MRP                 
 ethernet 2/3/2                 MRP                 
 Per vlan free ports                                

Topology Group 170
=================
 master-vlan 170
 member-vlan 144 to 145 220 454 2040 2191 2422 2459

 Common control ports           L2 protocol         
 ethernet 1/3/1                 MRP                 
 ethernet 1/3/2                 MRP                 
 ethernet 2/3/1                 MRP                 
 ethernet 2/3/2                 MRP                 
 Per vlan free ports                                

Topology Group 175
=================
 master-vlan 175                                                  
 member-vlan 100 450 850 2206 2752 to 2753

 Common control ports           L2 protocol         
 ethernet 1/3/1                 MRP                 
 ethernet 1/3/2                 MRP                 
 ethernet 2/3/1                 MRP                 
 ethernet 2/3/2                 MRP                 
 Per vlan free ports                                
 ethernet 1/1/2                  Vlan 850           
 ethernet 2/1/1                  Vlan 850           
 ethernet 2/1/2                  Vlan 850           

Topology Group 215
=================
 master-vlan 215
 member-vlan none

 Common control ports           L2 protocol         
 ethernet 1/3/1                 MRP                 
 ethernet 2/3/1                 MRP                 
 Per vlan free ports                                
 ethernet 1/3/2                  Vlan 215           
 ethernet 2/3/2                  Vlan 215     

```

**Help:** execute the command "show topo"

**Prompt:**
- brocade_fastiron>
- brocade_fastiron#
- brocade_fastiron(config)#

### show span

**Output:**
```

STP instance owned by VLAN 1

Global STP (IEEE 802.1D) Parameters:
 
VLAN Root             Root Root   Prio Max He- Ho- Fwd Last    Chg Bridge      
 ID   ID              Cost Port   rity Age llo ld  dly Chang   cnt Address     
                                  Hex  sec sec sec sec sec                     
   1 8000cc4e2415015e 0    Root   8000 20  2   1   15  265591169   cc4e2415015e

Port STP Parameters:

Port   Prio Path  State       Fwd    Design  Designated       Designated       
Num    rity Cost              Trans  Cost    Root             Bridge           
       Hex                                                                     
1/1/1  80   0     DISABLED    0      0       0000000000000000 0000000000000000 
1/1/9  80   0     DISABLED    0      0       0000000000000000 0000000000000000 
1/1/10 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
1/1/11 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
1/1/12 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
1/1/13 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
1/1/14 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
1/1/15 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
1/1/16 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
1/1/17 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
1/1/18 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
1/1/19 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
1/1/20 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
1/1/21 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
1/1/22 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
1/1/23 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
1/3/3  80   0     DISABLED    0      0       0000000000000000 0000000000000000 
1/3/4  80   0     DISABLED    0      0       0000000000000000 0000000000000000 
1/3/5  80   0     DISABLED    0      0       0000000000000000 0000000000000000 
1/3/6  80   0     DISABLED    0      0       0000000000000000 0000000000000000 
1/3/7  80   0     DISABLED    0      0       0000000000000000 0000000000000000 
1/3/8  80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/3  80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/4  80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/5  80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/6  80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/7  80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/8  80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/9  80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/10 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/11 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/12 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/13 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/14 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/15 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/16 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/17 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/18 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/19 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/20 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/21 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/22 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/23 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/1/24 80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/3/3  80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/3/4  80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/3/5  80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/3/6  80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/3/7  80   0     DISABLED    0      0       0000000000000000 0000000000000000 
2/3/8  80   0     DISABLED    0      0       0000000000000000 0000000000000000 

Spanning-tree is not configured on port-vlan 385

Spanning-tree is not configured on port-vlan 10
                                                                  
Spanning-tree is not configured on port-vlan 94

Spanning-tree is not configured on port-vlan 144

Spanning-tree is not configured on port-vlan 145

Spanning-tree is not configured on port-vlan 146

Spanning-tree is not configured on port-vlan 149

Spanning-tree is not configured on port-vlan 151

Spanning-tree is not configured on port-vlan 152

Spanning-tree is not configured on port-vlan 154


```

**Help:** execute the command "show span"

**Prompt:**
- brocade_fastiron>
- brocade_fastiron#
- brocade_fastiron(config)#

### show mac-address

**Output:**
```
Total active entries from all ports = 236
MAC Address     Port      Age      VLAN    Type

6cae.8b2d.c979   2/1        0      1000
3440.b5be.e3ac   2/1        0      1000
90e2.ba5a.ab8c   2/1        0      1000
```

**Help:** execute the command "show mac-address"

**Prompt:**
- brocade_fastiron>
- brocade_fastiron#
- brocade_fastiron(config)#

### show metro

**Output:**
```
Metro Ring 10
=============
Ring       State      Ring       Master     Topo       Hello      Prefwing
id                    role       vlan       group      time(ms)   time(ms)
10         enabled    member     10         10         100        300

Ring interfaces Interface role Forwarding state Active interface interface type 
ethernet 11     primary        forwarding       ethernet 11      regular        
ethernet 2      secondary      forwarding       ethernet 2       regular        

RHPs sent            RHPs rcvd            TC RBPDUs rcvd       State changes
0                    1432850207           7970                 154


Metro Ring 14
=============
Ring       State      Ring       Master     Topo       Hello      Prefwing
id                    role       vlan       group      time(ms)   time(ms)
14         enabled    member     14         14         100        300

Ring interfaces Interface role Forwarding state Active interface interface type 
 ethernet 1      primary        forwarding       ethernet 1       regular        
ethernet 2      secondary      forwarding       ethernet 2       regular        

RHPs sent            RHPs rcvd            TC RBPDUs rcvd       State changes
0                    1441064488           1728                 86


Metro Ring 176 - CLMAMOFW-to-CLMAMO10G
=============
Ring       State      Ring       Master     Topo       Hello      Prefwing
id                    role       vlan       group      time(ms)   time(ms)
176        enabled    member     175        175        100        300

Ring interfaces Interface role Forwarding state Active interface interface type 
 ethernet 1      primary        forwarding       ethernet 1       regular        
ethernet 2      secondary      forwarding       ethernet 2       regular        

RHPs sent            RHPs rcvd            TC RBPDUs rcvd       State changes
0                    355056325            689                  9


```

**Help:** execute the command "show metro"

**Prompt:**
- brocade_fastiron>
- brocade_fastiron#
- brocade_fastiron(config)#

### show lldp neighbors

**Output:**
```
Capability codes:
    (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
    (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other
 Device ID           Local Intf     Hold-time  Capability      Port ID
core-sw01           Gi1/3          120        B,R             Gi0/3
Total entries displayed: 1

```

**Help:** execute the command "show lldp neighbors"

**Prompt:**
- brocade_fastiron>
- brocade_fastiron#
- brocade_fastiron(config)#

### show version

**Output:**
```
show version

  Copyright (c) 1996-2016 Brocade Communications Systems, Inc. All rights reserved.
    UNIT 1: compiled on May 19 2016 at 01:15:45 labeled as ICX64S08030h
		(8500344 bytes) from Primary ICX64S08030h.bin
        SW: Version 08.0.30hT311
    UNIT 2: compiled on May 19 2016 at 01:15:45 labeled as ICX64S08030h
 		(8500344 bytes) from Primary ICX64S08030h.bin
        SW: Version 08.0.30hT311
    UNIT 3: compiled on May 19 2016 at 01:15:45 labeled as ICX64S08030h
 		(8500344 bytes) from Primary ICX64S08030h.bin
        SW: Version 08.0.30hT311
    UNIT 4: compiled on May 19 2016 at 01:15:45 labeled as ICX64S08030h
 		(8500344 bytes) from Primary ICX64S08030h.bin
        SW: Version 08.0.30hT311
    UNIT 5: compiled on May 19 2016 at 01:15:45 labeled as ICX64S08030h
 		(8500344 bytes) from Primary ICX64S08030h.bin
        SW: Version 08.0.30hT311
    UNIT 6: compiled on May 19 2016 at 01:15:45 labeled as ICX64S08030h
 		(8500344 bytes) from Primary ICX64S08030h.bin
        SW: Version 08.0.30hT311
  Boot-Monitor Image size = 786944, Version:10.1.05T310 (kxz10105)
  HW: Stackable ICX6450-48-HPOE
==========================================================================
 UNIT 1: SL 1: ICX6450-48P POE 48-port Management Module
 	 Serial  #: BZT3217M025
 	 License: BASE_SOFT_PACKAGE   (LID: dbvIHGMoFHK)
 	 P-ENGINE  0: type DEF0, rev 01
 	 P-ENGINE  1: type DEF0, rev 01
==========================================================================
 UNIT 1: SL 2: ICX6450-SFP-Plus 4port 40G Module
==========================================================================
 UNIT 2: SL 1: ICX6450-48P POE 48-port Management Module
 	 Serial  #: BZT3217M033
 	 License: BASE_SOFT_PACKAGE   (LID: dbvIHGMoFII)
 	 P-ENGINE  0: type DEF0, rev 01
 	 P-ENGINE  1: type DEF0, rev 01
==========================================================================
 UNIT 2: SL 2: ICX6450-SFP-Plus 4port 40G Module
==========================================================================
 UNIT 3: SL 1: ICX6450-48P POE 48-port Management Module
 	 Serial  #: BZT3217M036
 	 License: BASE_SOFT_PACKAGE   (LID: dbvIHGMoFIL)
 	 P-ENGINE  0: type DEF0, rev 01
 	 P-ENGINE  1: type DEF0, rev 01

==========================================================================
 UNIT 3: SL 2: ICX6450-SFP-Plus 4port 40G Module
==========================================================================
 UNIT 4: SL 1: ICX6450-48P POE 48-port Management Module
 	 Serial  #: BZT3217M038
 	 License: BASE_SOFT_PACKAGE   (LID: dbvIHGMoFIN)
 	 P-ENGINE  0: type DEF0, rev 01
 	 P-ENGINE  1: type DEF0, rev 01
==========================================================================
 UNIT 4: SL 2: ICX6450-SFP-Plus 4port 40G Module
==========================================================================
 UNIT 5: SL 1: ICX6450-48P POE 48-port Management Module
 	 Serial  #: BZT3215M02V
 	 License: BASE_SOFT_PACKAGE   (LID: dbvIHGKoFHx)
 	 P-ENGINE  0: type DEF0, rev 01
 	 P-ENGINE  1: type DEF0, rev 01
==========================================================================
 UNIT 5: SL 2: ICX6450-SFP-Plus 4port 40G Module
==========================================================================
 UNIT 6: SL 1: ICX6450-48P POE 48-port Management Module
 	 Serial  #: BZT3217M02G
 	 License: BASE_SOFT_PACKAGE   (LID: dbvIHGMoFHi)
 	 P-ENGINE  0: type DEF0, rev 01
 	 P-ENGINE  1: type DEF0, rev 01
==========================================================================
 UNIT 6: SL 2: ICX6450-SFP-Plus 4port 40G Module
==========================================================================

  800 MHz ARM processor ARMv5TE, 400 MHz bus
65536 KB flash memory
  512 MB DRAM
STACKID 1  system uptime is 730 day(s) 11 hour(s) 11 second(s)
STACKID 2  system uptime is 707 day(s) 8 hour(s) 13 minute(s) 32 second(s)
STACKID 3  system uptime is 707 day(s) 8 hour(s) 13 minute(s) 32 second(s)
STACKID 4  system uptime is 707 day(s) 8 hour(s) 13 minute(s) 32 second(s)
STACKID 5  system uptime is 707 day(s) 8 hour(s) 13 minute(s) 31 second(s)
STACKID 6  system uptime is 730 day(s) 10 hour(s) 59 minute(s) 40 second(s)
The system started at 15:56:16 Pacific Fri Jul 08 2016

 The system : started=cold start
 My stack unit ID = 1, bootup role = active

```

**Help:** execute the command "show version"

**Prompt:**
- brocade_fastiron>
- brocade_fastiron#
- brocade_fastiron(config)#

