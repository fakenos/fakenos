# avaya_ers


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
- avaya_ers>

### terminal length 0

**Output:** None

**Help:** make the terminal full screen

**Prompt:**
- avaya_ers>
- avaya_ers#

### ex

**Output:**
```
True
```

**Help:** exit the terminal

**Prompt:**
- avaya_ers>
- avaya_ers#

### show sys-info

**Output:**
```
Operation Mode:        Stack, Unit # 1
Size Of Stack:         4
Base Unit:             1
MAC Address:           FF-FF-FF-FF-FF-FF
PoE Module FW:         4.1.0.4
Reset Count:           37
Last Reset Type:       Power Cycle
Autotopology:          Enabled
Pluggable Port 47:     None
Pluggable Port 48:     None
Pluggable Port 49:     SX
Pluggable Port 50:     Direct Attach Cable
Pluggable Port 51:     Direct Attach Cable
Base Unit Selection:   Base unit using rear-panel switch
sysDescr:              Ethernet Routing Switch 3549GTS-PWR+
                       HW:03       FW:5.3.0.6   SW:v5.3.0.005
                       Mfg Date:20150406    HW Dev:none
Serial #:              1XXXXXXXXXXX
Operational Software:  FW:5.3.0.6   SW:v5.3.0.005
Installed software:    FW:5.3.0.6   SW:v5.3.0.005
Operational license:   Base software
 Installed license:     Base software
sysObjectID:           1.3.6.1.4.1.45.3.80.8
sysUpTime:             35 days, 07:24:53
sysNtpTime:            2015-10-21 20:26:44 GMT+00:00
sysServices:           6
sysContact:            sysContact
sysName:               sysName
sysLocation:           sysLocation
Stack sysAssetId:      stackAssetID
Unit sysAssetId:       unitAssetID

```

**Help:** execute the command "show sys-info"

**Prompt:**
- avaya_ers>
- avaya_ers#

### show interface name

**Output:**
```
Unit/Port Name      
--------- ----------------------------------------------------------------      
1/1       
1/2       
1/3       
1/4       
1/5       
1/6       
1/7       
1/8       
1/9       
1/10      
1/11      
1/12      
1/13      
1/14      
1/15      
1/16      
1/17      
1/18      
1/19      
1/20      
1/21      
1/22      
1/23      
1/24      
1/25      
1/26      
1/27      
1/28      
1/29      
1/30      
1/31      
1/32      
1/33      
1/34      
1/35      
1/36      
1/37      
1/38      
1/39      
1/40      
1/41      
1/42      
1/43      
1/44      
1/45      
1/46      
1/47      
1/48      
1/49      
1/50      HALL-FC3: 1/25
2/1       
2/2       
2/3       
2/4       
2/5       
2/6       
2/7       
2/8       
2/9       Bell 10.1.1.100
2/10      
2/11      
2/12      
2/13      
2/14      
2/15      HALL-Park (outdoor WAP)
2/16      
2/17      
2/18      
2/19      
2/20      
2/21      
2/22      
2/23      
2/24      
2/25      
2/26      
2/27      
2/28      
2/29      
2/30      
2/31      
2/32      
2/33      
2/34      
2/35      
2/36      
2/37      
2/38      
2/39      
2/40      
2/41      
2/42      
2/43      
2/44      
2/45      
2/46      
2/47      
2/48      HALL-UPS
2/49      
2/50      HALL-FC4:1/25

```

**Help:** execute the command "show interface name"

**Prompt:**
- avaya_ers>
- avaya_ers#

### show mlt all-members

**Output:**
```
Id: 1
    Name:UPLINK
    Active Members: 1/50,2/50
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 2
    Name:Trunk #2
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 3
    Name:Trunk #3
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 4
    Name:Trunk #4
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 5
    Name:Trunk #5
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 6
    Name:Trunk #6
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 7
    Name:Trunk #7
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 8
    Name:Trunk #8
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 9
    Name:Trunk #9
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 10
    Name:Trunk #10
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 11
    Name:Trunk #11
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 12
    Name:Trunk #12
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 13
    Name:Trunk #13
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 14
    Name:Trunk #14
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 15
    Name:Trunk #15
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 16
    Name:Trunk #16
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 17
    Name:Trunk #17
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 18
    Name:Trunk #18
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 19
    Name:Trunk #19
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 20
    Name:Trunk #20
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 21
    Name:Trunk #21
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 22
    Name:Trunk #22
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 23
    Name:Trunk #23
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 24
    Name:Trunk #24
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 25
    Name:Trunk #25
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 26
    Name:Trunk #26
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 27
    Name:Trunk #27
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 28
    Name:Trunk #28
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 29
    Name:Trunk #29
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 30
    Name:Trunk #30
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 31
    Name:Trunk #31
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE
 Id: 32
    Name:Trunk #32
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
    LACP key: NONE

```

**Help:** execute the command "show mlt all-members"

**Prompt:**
- avaya_ers>
- avaya_ers#

### show vlan

**Output:**
```
Id   Name                 Type     Protocol         PID     Active IVL/SVL Mgmt
---- -------------------- -------- ---------------- ------- ------ ------- ----
1    VLAN #1              Port     None             0x0000  Yes    IVL     No
	Port Members: NONE
2    Dead_VLAN            Port     None             0x0000  Yes    IVL     No
	Port Members: 17-42,49-50
17   Network_Services     Port     None             0x0000  Yes    IVL     No
	Port Members: 5-10,47
27   Lab_Mgmt             Port     None             0x0000  Yes    IVL     Yes
 	Port Members: 1,11,13,16,43-46,48
47   IoT_Devices          Port     None             0x0000  Yes    IVL     No
	Port Members: 14,48
300  Trusted Wifi         Port     None             0x0000  Yes    IVL     No
	Port Members: 3-4,11-13,47
301  Untrusted Wifi       Port     None             0x0000  Yes    IVL     No
	Port Members: 11,13,48
477  VM Environment       Port     None             0x0000  Yes    IVL     No
	Port Members: 2,15,48
999  Native_VLAN          Port     None             0x0000  Yes    IVL     No
 	Port Members: NONE
Total VLANs: 9

```

**Help:** execute the command "show vlan"

**Prompt:**
- avaya_ers>
- avaya_ers#

### show logging config

**Output:**
```
Event Logging: Enabled
Volatile Logging Option: Latch
Event Types To Log: Critical, Serious, Informational
Event Types To Log To NV Storage: Critical, Serious
Remote Logging: Enabled
Remote Logging Address: 0.0.0.0
Secondary Remote Logging Address: 0.0.0.0
Event Types To Log Remotely: Critical, Serious, Informational
Facility: Daemon

```

**Help:** execute the command "show logging config"

**Prompt:**
- avaya_ers>
- avaya_ers#

### show mac-address-table

**Output:**
```
   MAC Address    Vid   Type       Source    
----------------- ---- ------- -------------- 
00-0E-C4-CE-AD-39   15 Dynamic Port:47
00-C0-B7-4C-91-CF   15 Dynamic Port: 7
00-D0-2D-B3-4B-D2   15 Dynamic Port:10
EC-8E-B5-BF-59-5B   15 Dynamic Port: 9
00-0E-C4-CE-AD-3B   25 Dynamic Port:48
00-15-17-2E-58-F3   25 Dynamic Port: 1
50-61-84-DD-58-00   25 Self           
F0-9F-C2-33-4A-00   25 Dynamic Port:13
F0-9F-C2-70-B4-8E   25 Dynamic Port:11
00-0E-C4-CE-AD-3B   45 Dynamic Port:48
AC-CC-8E-47-85-63   45 Dynamic Port:14
00-0E-C4-CE-AD-39  100 Dynamic Port:47
00-11-32-4E-75-07  100 Dynamic Port: 3
00-11-32-4E-75-08  100 Dynamic Port: 4
50-F5-DA-2D-00-A0  100 Dynamic Port:13
6C-40-08-93-CF-94  100 Dynamic Port:11
A4-5E-60-D4-F7-4B  100 Dynamic Port:13
B8-44-D9-1A-BC-42  100 Dynamic Port:11
00-0E-C4-CE-AD-3B  101 Dynamic Port:48
2C-1F-23-2E-89-CB  101 Dynamic Port:13
84-41-67-5E-D7-54  101 Dynamic Port:13
90-FD-61-BE-14-37  101 Dynamic Port:13
AC-CF-5C-73-A1-6D  101 Dynamic Port:11
00-0C-29-AD-8B-03  275 Dynamic Port: 2
00-0E-C4-CE-AD-3B  275 Dynamic Port:48
```

**Help:** execute the command "show mac-address-table"

**Prompt:**
- avaya_ers>
- avaya_ers#

### show mlt

**Output:**
```
Id: 1
    Name:IST
    Active Members: 38-39
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Enabled 
    Type: Trunk
 Id: 2
    Name:Trunk #2
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 3
    Name:Trunk #3
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 4
    Name:Trunk #4
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 5
    Name:Trunk #5
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 6
    Name:Trunk #6
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 7
    Name:Trunk #7
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 8
    Name:Trunk #8
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 9
    Name:Trunk #9
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 10
    Name:Trunk #10
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 11
    Name:Trunk #11
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
 Id: 12
    Name:Trunk #12
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 13
    Name:Trunk #13
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 14
    Name:Trunk #14
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 15
    Name:Trunk #15
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
 Id: 16
    Name:Trunk #16
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 17
    Name:Trunk #17
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 18
    Name:Trunk #18
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 19
    Name:Trunk #19
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
 Id: 20
    Name:Trunk #20
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 21
    Name:Trunk #21
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 22
    Name:Trunk #22
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 23
    Name:Trunk #23
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
 Id: 24
    Name:Trunk #24
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 25
    Name:Trunk #25
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 26
    Name:Trunk #26
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 27
    Name:Trunk #27
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
 Id: 28
    Name:Trunk #28
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 29
    Name:Trunk #29
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 30
    Name:Trunk #30
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 31
    Name:Trunk #31
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
 Id: 32
    Name:Trunk #32
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 33
    Name:Trunk #33
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 34
    Name:Trunk #34
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 35
    Name:Trunk #35
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
 Id: 36
    Name:Trunk #36
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 37
    Name:Trunk #37
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 38
    Name:Trunk #38
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 39
    Name:Trunk #39
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
 Id: 40
    Name:Trunk #40
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 41
    Name:Trunk #41
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 42
    Name:Trunk #42
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 43
    Name:Trunk #43
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
 Id: 44
    Name:Trunk #44
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 45
    Name:Trunk #45
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 46
    Name:Trunk #46
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 47
    Name:Trunk #47
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
 Id: 48
    Name:Trunk #48
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 49
    Name:Trunk #49
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 50
    Name:Trunk #50
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 51
    Name:Trunk #51
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
 Id: 52
    Name:Trunk #52
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 53
    Name:Trunk #53
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 54
    Name:Trunk #54
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 55
    Name:Trunk #55
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
 Id: 56
    Name:Trunk #56
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 57
    Name:Trunk #57
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 58
    Name:Trunk #58
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 59
    Name:Trunk #59
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
 Id: 60
    Name:Trunk #60
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 61
    Name:Trunk #61
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 62
    Name:Trunk #62
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
Id: 63
    Name:Trunk #63
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled
 Id: 64
    Name:Trunk #64
    Active Members: NONE
    Inactive Members: NONE
    Bpdu: All
    Mode: Basic
    Status: Disabled

```

**Help:** execute the command "show mlt"

**Prompt:**
- avaya_ers>
- avaya_ers#

### logout

**Output:** None

**Help:** Execute the command logout. This automatically generated. Feel free to change it!

**Prompt:**
- avaya_ers>
- avaya_ers#

### no page

**Output:** None

**Help:** Execute the command no page. This automatically generated. Feel free to change it!

**Prompt:**
- avaya_ers>
- avaya_ers#

### terminal width 511

**Output:** None

**Help:** Execute the command terminal width 511. This automatically generated. Feel free to change it!

**Prompt:**
- avaya_ers>
- avaya_ers#

