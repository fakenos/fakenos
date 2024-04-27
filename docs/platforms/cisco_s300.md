# cisco_s300


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
- cisco_s300>

### show mac address-table

**Output:**
```
Flags: I - Internal usage VLAN
Aging time is 300 sec

    Vlan          Mac Address         Port       Type
------------ --------------------- ---------- ----------
     1         00:08:32:0f:00:61       0         self
    300        00:1d:9c:a1:46:86      gi7      dynamic
    300        00:1d:9c:a1:50:0a      gi8      dynamic
    300        00:1d:9c:a1:5b:a6      gi9      dynamic
    300        e4:90:69:aa:58:44      gi28     dynamic
    400        00:00:bc:39:be:03      gi1      dynamic
    400        00:0e:f0:4b:30:02      gi2      dynamic
    400        00:0e:f0:4b:30:13      gi2      dynamic
    400        00:0e:f0:5a:19:f1      gi27     dynamic
    400        00:0e:f0:5a:1a:10      gi3      dynamic
    400        00:1d:9c:cd:69:5c      gi1      dynamic
    400        f4:54:33:91:ea:3a      gi2      dynamic
    400        f4:54:33:a8:f0:0a      gi3      dynamic

```

**Help:** execute the command "show mac address-table"

**Prompt:**
- cisco_s300>
- cisco_s300#

### show vlan

**Output:**
```
Created by: D-Default, S-Static, G-GVRP, R-Radius Assigned VLAN

Vlan       Name                   Ports               Created by
---- ----------------- --------------------------- ----------------
 1           1         fa1-2,fa4-8,fa10-14,               D
                       fa17-18,fa20
 29         29                     gi1                    S
402  Test-Long-Vlan-Na           fa5,gi1                  S
     me1
3130       3130                 fa20,gi1                  S
3131 Test-Long-Vlan-Na fa1-2,fa11,fa15-18,fa21-22,        S
     me2               gi1-4
3132       3132                                           S
3133 Test-Long-Vlan-Na                                    S
     me3

```

**Help:** execute the command "show vlan"

**Prompt:**
- cisco_s300>
- cisco_s300#

### show system id

**Output:**
```
Serial number : IDN123456AA

```

**Help:** execute the command "show system id"

**Prompt:**
- cisco_s300>
- cisco_s300#

### show interfaces status

**Output:**
```
                                             Flow Link          Back   Mdix
Port     Type         Duplex  Speed Neg      ctrl State       Pressure Mode
-------- ------------ ------  ----- -------- ---- ----------- -------- -------
gi1      1G-Copper    Full    100   Enabled  Off  Up          Disabled Off
gi2      1G-Copper    Full    100   Enabled  Off  Up          Disabled On
gi3      1G-Copper    Full    100   Enabled  Off  Up          Disabled Off
gi4      1G-Copper      --      --     --     --  Down           --     --
gi5      1G-Copper      --      --     --     --  Down           --     --
gi6      1G-Copper      --      --     --     --  Down           --     --
gi7      1G-Copper    Full    100   Enabled  Off  Up          Disabled On
gi8      1G-Copper    Full    100   Enabled  Off  Up          Disabled Off
gi9      1G-Copper    Full    100   Enabled  Off  Up          Disabled Off
gi10     1G-Copper      --      --     --     --  Down           --     --
gi11     1G-Copper      --      --     --     --  Down           --     --
gi12     1G-Copper      --      --     --     --  Down           --     --
gi13     1G-Copper      --      --     --     --  Down           --     --
gi14     1G-Copper      --      --     --     --  Down           --     --
gi15     1G-Copper      --      --     --     --  Down           --     --
gi16     1G-Copper      --      --     --     --  Down           --     --
gi17     1G-Copper      --      --     --     --  Down           --     --
gi18     1G-Copper      --      --     --     --  Down           --     --
gi19     1G-Copper      --      --     --     --  Down           --     --
gi20     1G-Copper      --      --     --     --  Down           --     --
gi21     1G-Copper      --      --     --     --  Down           --     --
gi22     1G-Copper      --      --     --     --  Down           --     --
gi23     1G-Copper      --      --     --     --  Down           --     --
gi24     1G-Copper      --      --     --     --  Down           --     --
gi25     1G-Copper      --      --     --     --  Down           --     --
gi26     1G-Copper      --      --     --     --  Down           --     --
gi27     1G-Combo-F   Full    1000  Disabled Off  Up          Disabled Off
gi28     1G-Combo-F   Full    1000  Disabled Off  Up          Disabled Off

                                          Flow    Link
Ch       Type    Duplex  Speed  Neg      control  State
-------- ------- ------  -----  -------- -------  -----------
Po1         --     --      --      --       --    Not Present
Po2         --     --      --      --       --    Not Present
Po3         --     --      --      --       --    Not Present
Po4         --     --      --      --       --    Not Present
Po5         --     --      --      --       --    Not Present
Po6         --     --      --      --       --    Not Present
Po7         --     --      --      --       --    Not Present
Po8         --     --      --      --       --    Not Present
```

**Help:** execute the command "show interfaces status"

**Prompt:**
- cisco_s300>
- cisco_s300#

### show system

**Output:**
```
System Description:                       24-Port 10/100 PoE Managed Switch
System Up Time (days,hour:min:sec):       70,03:16:47
System Contact:                           +7(495)363-06-75
System Name:                              ZOO-SF300-POE-2
System Location:                          Moscow, Zoologicheskaya street, room
                                          11
 System MAC Address:                       34:bd:c8:36:2a:41
System Object ID:                         1.3.6.1.4.1.9.6.1.82.24.2

Fans Status:                              OK

```

**Help:** execute the command "show system"

**Prompt:**
- cisco_s300>
- cisco_s300#

### show ip interface

**Output:**
```
  Gateway IP Address        Activity status       Type
----------------------- ----------------------- --------
10.255.1.51             Active                  static


    IP Address         I/F       Type       Status
------------------- --------- ----------- -----------
10.255.1.72/16      vlan 255  Static      Valid

```

**Help:** execute the command "show ip interface"

**Prompt:**
- cisco_s300>
- cisco_s300#

### show interfaces description

**Output:**
```
Port      Description
-------   -----------
fa1       Test
fa2       Printer
fa3       Socket_7/7
fa4       Socket_7/3
fa5
fa6
fa7
fa8       Camera
fa9       Camera
fa10      Camera
fa11
fa12      Socket_7/2
fa13      Socket_7/4
fa14      Socket_7/8
fa15
fa16
fa17
fa18
fa19
fa20
fa21
fa22
fa23      AP
fa24      AP
gi1
gi2
gi3
gi4       Eltex2124-8 - gi1/0/5

Ch        Description
-------   -----------
Po1
Po2
Po3
Po4
Po5
Po6
Po7
Po8

```

**Help:** execute the command "show interfaces description"

**Prompt:**
- cisco_s300>
- cisco_s300#

### show interfaces switchport

**Output:**
```
Port : fa1
Port Mode: Trunk
Gvrp Status: disabled
Ingress Filtering: true
Acceptable Frame Type: admitAll
Ingress UnTagged VLAN ( NATIVE ): 203
 
Port is member in:

Vlan               Name               Egress rule Port Membership Type
---- -------------------------------- ----------- --------------------
203                203                 Untagged          Static
222               VOIP-1                Tagged           Static


Forbidden VLANS:
Vlan               Name
---- --------------------------------


Classification rules:

Mac based VLANs:
  Group ID   Vlan ID
------------ -------

```

**Help:** execute the command "show interfaces switchport"

**Prompt:**
- cisco_s300>
- cisco_s300#

### show lldp neighbors

**Output:**
```

System capability legend:
B - Bridge; R - Router; W - Wlan Access Point; T - telephone;
D - DOCSIS Cable Device; H - Host; r - Repeater;
TP - Two Ports MAC Relay; S - S-VLAN; C - C-VLAN; O - Other

  Port        Device ID        Port ID       System Name    Capabilities  TTL
--------- ----------------- ------------- ----------------- ------------ -----
gi27      00:08:32:0f:1e:bd     gi27       prsw03freeporil       B        99
gi28      00:08:32:0f:04:cc     gi28      prsw01freeportin       B        90

```

**Help:** execute the command "show lldp neighbors"

**Prompt:**
- cisco_s300>
- cisco_s300#

### show version

**Output:**
```
SW version    1.3.7.18 ( date  12-Jan-2014 time  18:02:59 )
Boot version    1.1.0.6 ( date  11-May-2011 time  18:31:00 )
HW version    V02

```

**Help:** execute the command "show version"

**Prompt:**
- cisco_s300>
- cisco_s300#

### terminal datadump

**Output:** None

**Help:** Execute the command terminal datadump. This automatically generated. Feel free to change it!

**Prompt:**
- cisco_s300>
- cisco_s300#

### terminal width 511

**Output:** None

**Help:** Execute the command terminal width 511. This automatically generated. Feel free to change it!

**Prompt:**
- cisco_s300>
- cisco_s300#

