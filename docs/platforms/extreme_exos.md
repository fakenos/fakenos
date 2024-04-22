# extreme_exos


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
- extreme_exos>

### disable cli prompting

**Output:** None

**Help:** set the terminal width to maximum

**Prompt:**
- extreme_exos>
- extreme_exos#

### ex

**Output:**
```
True
```

**Help:** exit the terminal

**Prompt:**
- extreme_exos>
- extreme_exos#

### show ipconfig

**Output:**
```
       Use Redirects : Disabled
       IpOption LSRR : Enabled
       IpOption SSRR : Enabled
         IpOption RR : Enabled
         IpOption TS : Enabled
         IpOption RA : Enabled
       Route Sharing : Disabled
   Route Compression : Disabled
  Originated Packets : Don't require ipforwarding
 Max Shared Gateways : Current: 4  Configured: 4
  Route Sharing Hash : CRC Lower

      IRDP:
         Advertisement Address: 255.255.255.255      Maximum Interval: 600
         Minimum Interval: 450     Lifetime: 1800  Preference: 0

Interface    IP Address          Flags                   nSIA
VLAN0255     10.255.254.3    /16 EU----MPuRX---------    0
VLAN2222     10.1.222.3      /24 EUf---MPuRX---------    0

Flags: (A) Address Mask Reply Enabled (B) BOOTP Enabled
       (b) Broadcast Forwarding Enabled
       (D) Duplicate address detected on VLAN, (E) Interface Enabled
       (f) Forwarding Enabled (g) Ignore IP Broadcast Enabled
       (h) Directed Broadcast Forwarding by Hardware Enabled
       (I) IRDP Advertisement Enabled, (M) Send Parameter Problem Enabled
       (m) Multicast forwarding Enabled, (n) Multinetted VLAN
       (nSIA ) Number of Secondary IP Addresses
       (P) Send Port Unreachables Enabled, (R) Send Redirects Enabled
       (r) Unicast Reverse Path Enabled on at least one port of the VLAN
       (t) Tentative address, (T) Time Stamp Reply Enabled
       (u) Send Unreachables Enabled, (U) Interface Up
       (v) VRRP Enabled, (X) Send Time Exceeded Enabled

```

**Help:** execute the command "show ipconfig"

**Prompt:**
- extreme_exos>
- extreme_exos#

### show ports description

**Output:**
```
Port   Display String        Description String
=====  ====================  ==================================================
1                            AggregateLink
2
3
4
5                            MX5-2 - xe0/0/3
6                            BLADE-3 - VC1-4
7                            BLADE-3 - VC2-4
8                            BGW-R1 - xe0/1/1 (LAG7)
9                            FREE
10                           SRV-R1 - xe-0/0/1 (LAG6)
11                           3COM - Gi1/0/26 Link for PIM
12                           C4948-1 - te1/49
13                           Eltex3124-7 - te1/0/1
14                           Eltex3124-6 - te1/0/1
15                           Eltex3124-5 - te1/0/1
16                           Eltex3124-4 - te1/0/1
17                           MX5-1 - xe-0/0/3
18                           MX5-1 - xe-0/0/1
19                           CCR1036 - sfp1
20
21
22                           RS-CORE-1 - Gi0/1
23
24                           Uplink-GARS
25                           CRM-139204
26                           FREE
27                           FREE
28                           FREE
29                           N3K-2 - eth1/1 (LAG29)
30                           3COM - Te1/1/1
31                           FREE
32
33                           N9K-1 - eth1/46 (LAG33)
34                           N3K-2 - eth1/2 (LAG29)
35                           N9K-1 - eth1/47 (LAG33)
36                           Carbon-Reductor-NetXtreme-1 MIRROR
37                           VoipMonitor_Mirror
38                           Eltex3324-1 - te1/0/1 (LAG38)
39                           Eltex3324-1 - te1/0/2 (LAG38)
40                           FREE
41                           FREE
42                           BLADE-2-VC2 - VC8
43                           Storage-SMicro - eth0
44                           SCST-SSD_Cache - eth1
45                           Eltex5248-1 - Te1/0/1
46                           VEEAM1 - eth1
47                           BLADE-1-VC2 - VC1
48                           BLADE-1-VC2 - VC8
=====  ====================  ==================================================

```

**Help:** execute the command "show ports description"

**Prompt:**
- extreme_exos>
- extreme_exos#

### show ports information detail

**Output:**
```
Port:	1
	Description String: "AggregateLink"
	Virtual-router:	 VR-Default
	Type:		NONE
	Random Early drop:	Unsupported
	Admin state:	 Disabled with  10G full-duplex
	Link State:	Ready (local fault)
	Link Ups:       0        Last: Mon Apr 12 12:30:24 2021
	Link Downs:     1        Last: Thu Jun 23 12:41:45 2022

	VLAN cfg:
		 Name: Default, Internal Tag = 1, MAC-limit = No-limit, Virtual router:   VR-Default
		 Name: VLAN2222, 802.1Q Tag = 2222, MAC-limit = No-limit, Virtual router:   VR-Default
		       Port-specific VLAN ID: 2222
		 Name: VLAN1801, 802.1Q Tag = 1801, MAC-limit = No-limit, Virtual router:   VR-Default
		       Port-specific VLAN ID: 1801

    STP cfg:
		s1(enable), Tag=(none), Mode=802.1D, State=DISABLED
 
	Protocol:
		 Name: Default      Protocol: ANY      Match all protocols.
 	Trunking:	Master port with 4 members using algorithm address based - L3_L4
 algorithm
	Members: 	1-4

	EDP:		Enabled

	ELSM:		Disabled
	 Ethernet OAM:		Disabled
	Learning:	Enabled
	Unicast Flooding:	Enabled
 	Multicast Flooding:	Enabled
	Broadcast Flooding:	Enabled
	Jumbo:	Enabled, MTU= 9216
	Flow Control:	Rx-Pause: Enabled	Tx-Pause: Disabled
	Priority Flow Control: Disabled
	Reflective Relay:	Disabled
	Link up/down SNMP trap filter setting:	Enabled
	Egress Port Rate:	No-limit
	Broadcast Rate:	 	No-limit
	Multicast Rate:		No-limit
	Unknown Dest Mac Rate:	No-limit
 	QoS Profile:	None configured
    Ingress Rate Shaping : 		Unsupported
 	Ingress IPTOS Examination: 	Disabled
	Ingress 802.1p Examination: 	Enabled
 	Ingress 802.1p Inner Exam: 	Disabled
	Egress IPTOS Replacement:	Disabled
 	Egress 802.1p Replacement:	Disabled
	NetLogin: 			Disabled
	NetLogin port mode: 		Port based VLANs
	Smart redundancy: 		Enabled
	Software redundant port: 	Disabled
	IPFIX:   Disabled		Metering:  Ingress, All Packets, All Traffic
		IPv4 Flow Key Mask:	SIP: 255.255.255.255 		DIP: 255.255.255.255
 		IPv6 Flow Key Mask:	SIP: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
			 		DIP: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff

	Far-End-Fault-Indication: 	Disabled
	Shared packet buffer:		default
	VMAN CEP egress filtering:	 Disabled
	Isolation:			Off
	PTP Configured:      		Disabled
	Time-Stamping Mode:  		None
	Synchronous Ethernet:		Unsupported
	Dynamic VLAN Uplink:          	Disabled
	VM Tracking Dynamic VLANs:    	Disabled
Port:	2
 	Virtual-router:	VR-Default
	Type:		NONE
	Random Early drop:	Unsupported
 	Admin state:	Disabled with  10G full-duplex
	Link State:	Ready (local fault)
	Link Ups:       1        Last: Mon Jun 13 19:21:19 2022
	Link Downs:     2        Last: Thu Jun 23 12:41:37 2022

	VLAN cfg:
		 Name: Default, Internal Tag = 1, MAC-limit = No-limit, Virtual router:   VR-Default
		 Name: VLAN2222, 802.1Q Tag = 2222, MAC-limit = No-limit, Virtual router:   VR-Default
		       Port-specific VLAN ID: 2222
		 Name: VLAN1802, 802.1Q Tag = 1802, MAC-limit = No-limit, Virtual router:   VR-Default
		       Port-specific VLAN ID: 1802

    STP cfg:
		s1(enable), Tag=(none), Mode=802.1D, State=DISABLED
 
	Protocol:
		 Name: Default      Protocol: ANY      Match all protocols.
 	Trunking:	Master port with 4 members using algorithm address based - L3_L4
 algorithm
	Members: 	1-4

	EDP:		Enabled

	ELSM:		Disabled
	 Ethernet OAM:		Disabled
	Learning:	Enabled
	Unicast Flooding:	Enabled
 	Multicast Flooding:	Enabled
	Broadcast Flooding:	Enabled
	Jumbo:	Enabled, MTU= 9216
	Flow Control:	Rx-Pause: Enabled	Tx-Pause: Disabled
	Priority Flow Control: Disabled
	Reflective Relay:	Disabled
	Link up/down SNMP trap filter setting:	Enabled
	Egress Port Rate:	No-limit
	Broadcast Rate:	 	No-limit
	Multicast Rate:		No-limit
	Unknown Dest Mac Rate:	No-limit
 	QoS Profile:	None configured
    Ingress Rate Shaping : 		Unsupported
 	Ingress IPTOS Examination: 	Disabled
	Ingress 802.1p Examination: 	Enabled
 	Ingress 802.1p Inner Exam: 	Disabled
	Egress IPTOS Replacement:	Disabled
 	Egress 802.1p Replacement:	Disabled
	NetLogin: 			Disabled
	NetLogin port mode: 		Port based VLANs
	Smart redundancy: 		Enabled
	Software redundant port: 	Disabled
	IPFIX:   Disabled		Metering:  Ingress, All Packets, All Traffic
		IPv4 Flow Key Mask:	SIP: 255.255.255.255 		DIP: 255.255.255.255
 		IPv6 Flow Key Mask:	SIP: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
			 		DIP: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff

	Far-End-Fault-Indication: 	Disabled
	Shared packet buffer:		default
	VMAN CEP egress filtering:	 Disabled
	Isolation:			Off
	PTP Configured:      		Disabled
	Time-Stamping Mode:  		None
	Synchronous Ethernet:		Unsupported
	Dynamic VLAN Uplink:          	Disabled
	VM Tracking Dynamic VLANs:    	Disabled

```

**Help:** execute the command "show ports information detail"

**Prompt:**
- extreme_exos>
- extreme_exos#

### show ports information

**Output:**
```
Port      Flags               Link      ELSM Link Num Num  Num   Jumbo QOS     Load
                              State     /OAM UPS  STP VLAN Proto Size  profile Master
=====================================================================================
1         Dmjla---e--fMB---x- ready     - / -  0    1 3288   1   9216  none    1 a
2         Dmjla---e--fMB---x- ready     - / -  1    1 3288   1   9216  none    1 a
3         Dmjla---e--fMB---x- ready     - / -  7    1 3288   1   9216  none    1 a
4         Dmjla---e--fMB---x- ready     - / -  0    1 3288   1   9216  none    1 a
5         Emj-----e--fMB---x- active    - / -  1    0    1   0   9216  none
6         Emj-----e--fMB---x- active    - / -  2    0   74   0   9216  none
7         Emj-----e--fMB---x- active    - / -  2    0   74   0   9216  none
8         Emj-----e--fMB---x- ready     - / -  0    0    0   0   9216  none
9         Dmj-----e--fMB---x- ready     - / -  0    0    0   0   9216  none
10        Emj-----e--fMB---x- ready     - / -  0    0    0   0   9216  none
11        Emj-----e--fMB---x- ready     - / -  0    0    1   1   9216  none
12        Emj-----e--fMB---x- active    - / -  0    0   97   0   9216  none
13        Emj-----e--fMB---x- active    - / -  1    1   55   1   9216  none
14        Emj-----e--fMB---x- active    - / - 10    1  130   1   9216  none
15        Emj-----e--fMB---x- active    - / -  0    1  191   1   9216  none
16        Emj-----e--fMB---x- active    - / -  1    1  312   1   9216  none
17        Emj-----e--fMB---x- ready     - / -  0    0 3289   0   9216  none
18        Emj-----e--fMB---x- ready     - / -  0    0    0   0   9216  none
19        Emj-----e--fMB---x- active    - / - 22    0  176   0   9216  none
20        Emj-----e--fMB---x- ready     - / -  0    1    7   1   9216  none
21        Dmj-----e--fMB---x- ready     - / -  4    0    1   1   9216  none
22        Emj-----e--fMB---x- ready     - / -  0    1   11   1   9216  none
23        Emj-----e--fMB---x- active    - / -  2    1 3324   1   9216  none
24        Emj-----e--fMB---x- ready     - / -  2    0    1   0   9216  none
25        Dmj-----e--fMB---x- ready     - / -  3    0    5   0   9216  none
26        Emj-----e--fMB---x- ready     - / -  4    0    5   0   9216  none
27        Emj-----e--fMB---x- ready     - / - 11    0    5   0   9216  none
28        Emj-----e--fMB---x- ready     - / -  0    0    5   0   9216  none
29        Emjla---e--fMB---x- ready     - / - 12    0   72   0   9216  none    29 a
30        Dmj-----e--fMB---x- ready     - / -  2    1  532   1   9216  none
31        Emj-----e--fMB---x- ready     - / -  0    0    0   0   9216  none
32        Emj-----e--fMB---x- ready     - / -  0    0    0   0   9216  none
33        Emjla---e--fMB---x- active    - / -  2    0  856   0   9216  none    33 a
34        Emjla---e--fMB---x- ready     - / -  7    0   72   0   9216  none    29 a
35        Emjla---e--fMB---x- active    - / -  1    0  856   0   9216  none    33 a
36        Emj-----e--fMB---x- active    - / - 10    0    0   0   9216  none
37        Emj-----e--fMB---x- active    - / -  0    0    0   0   9216  none
38        Emjla---e--fMB---x- ready     - / -  0    0   26   0   9216  none    38 a
39        Emjla---e--fMB---x- ready     - / -  0    0   26   0   9216  none    38 a
40        Emj-----e--fMB---x- ready     - / -  0    0    7   0   9216  none
41        Emj-----e--fMB---x- ready     - / -  0    1  118   1   9216  none
42        Emj-----e--fMB---x- ready     - / -  0    1  317   1   9216  none
43        Emj-----e--fMB---x- ready     - / -  5    1    2   1   9216  none
44        Emj-----e--fMB---x- active    - / -  2    0    1   1   9216  none
45        Emj-----e--fMB----- active    - / -  1    0  388   0   9216  none
46        Emj-----e--fMB----- active    - / - 17    0    6   0   9216  none
47        Emj-----e--fMB----- active    - / -  0    0  261   0   9216  none
48        Emj-----e--fMB----- active    - / -  0    0  265   0   9216  none
=====================================================================================
 > indicates Port Display Name truncated past 8 characters
Flags : a - Load Sharing Algorithm address-based, D - Port Disabled,
        e - Extreme Discovery Protocol Enabled, E - Port Enabled,
        g - Egress TOS Enabled, i - Isolation, j - Jumbo Frame Enabled,
        l - Load Sharing Enabled, m - MACLearning Enabled,
        n - Ingress TOS Enabled, o - Dot1p Replacement Enabled,
        P - Software redundant port(Primary),
        R - Software redundant port(Redundant),
        q - Background QOS Monitoring Enabled,
        s - diffserv Replacement Enabled,
        v - Vman Enabled, f - Unicast Flooding Enabled,
        M - Multicast Flooding Enabled, B - Broadcast Flooding Enabled
        L - Extreme Link Status Monitoring Enabled
        O - Ethernet OAM Enabled
        w - MACLearning Disabled with Forwarding
        b - Rx and Tx Flow Control Enabled, x - Rx Flow Control Enabled
        p - Priority Flow Control Enabled

```

**Help:** execute the command "show ports information"

**Prompt:**
- extreme_exos>
- extreme_exos#

### show sharing

**Output:**
```
Load Sharing Monitor
Config    Current    Agg       Ld Share    Ld Share  Agg   Link    Link Up
Master    Master     Control   Algorithm   Group     Mbr   State   Transitions
==============================================================================
     1               LACP      L3_L4       1          -      R        0
                               L3_L4       2          -      R        1
                               L3_L4       3          -      R        7
                               L3_L4       4          -      R        0
    29               LACP      L3_L4       29         -      R       12
                               L3_L4       34         -      R        7
    33     33        LACP      L2          33         Y      A        2
                               L2          35         Y      A        1
    38               LACP      L3_L4       38         -      R        0
                               L3_L4       39         -      R        0
==============================================================================
 Link State: A-Active, D-Disabled, R-Ready, NP-Port not present, L-Loopback
 Load Sharing Algorithm: (L2) Layer 2 address based, (L3) Layer 3 address based
                        (L3_L4) Layer 3 address and Layer 4 port based
                        (custom) User-selected address-based configuration
 Custom Algorithm Configuration: ipv4 L3-and-L4, xor
Number of load sharing trunks: 4

```

**Help:** execute the command "show sharing"

**Prompt:**
- extreme_exos>
- extreme_exos#

### show vlan description

**Output:**
```
-------------------------------------------------------------------------------
Name            VID  Description
-------------------------------------------------------------------------------
Default         1
Mgmt            4095 Management VLAN
VLAN0002        2    sw-3
VLAN0003        3    VLAN0003
VLAN0004        4    VLAN0004
VLAN0005        5    tech
VLAN0006        6    zr
VLAN0007        7
VLAN0008        8    VLAN0008
VLAN0009        9    VGWsubnet1
VLAN0010        10   LAN
VLAN0011        11   dsl-Internet
VLAN0012        12   VLAN0012
VLAN0013        13   VLAN0013
VLAN0014        14   VLAN0014
VLAN0015        15   l3-sw-3
VLAN0016        16   l3sw-2-6
VLAN0017        17   VLAN0017
VLAN0018        18   VLAN0018
VLAN0019        19   VLAN0019
VLAN0020        20   NNI-TEST-QnQ
VLAN0021        21   VLAN0021
VLAN0022        22   VLAN0022
VLAN0023        23   TEST_EXFO
VLAN0024        24   VLAN0024
VLAN0025        25   VLAN0025
VLAN0026        26   VLAN0026
VLAN0027        27   VLAN0027
VLAN0028        28   VLAN0028
VLAN0029        29   VLAN0029
VLAN0030        30   VLAN0030
VLAN0031        31   VLAN0031
VLAN0032        32   user VOIP
VLAN0033        33   VLAN0033
VLAN0034        34   VLAN0034
VLAN0035        35   VLAN0035
VLAN0036        36   VLAN0036
VLAN0037        37   VLAN0037
VLAN0038        38   SS_voip
VLAN0248        248
-------------------------------------------------------------------------------
 
> Indicates description string truncated past 57 characters

Total number of VLAN(s) : 3469

```

**Help:** execute the command "show vlan description"

**Prompt:**
- extreme_exos>
- extreme_exos#

### disable clipaging

**Output:** None

**Help:** Execute the command disable clipaging. This automatically generated. Feel free to change it!

**Prompt:**
- extreme_exos>
- extreme_exos#

