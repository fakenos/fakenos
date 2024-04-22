# ubiquiti_edgeswitch


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
- ubiquiti_edgeswitch>

### ex

**Output:**
```
True
```

**Help:** exit the terminal

**Prompt:**
- ubiquiti_edgeswitch>
- ubiquiti_edgeswitch#

### show arp

**Output:**
```

Age Time (seconds)............................. 300
Response Time (seconds)........................ 1
Retries........................................ 4
Cache Size..................................... 493
Dynamic Renew Mode ............................ Disable
Total Entry Count Current / Peak .............. 4 / 4
Static Entry Count Configured / Active / Max .. 0 / 0 / 128

  IP Address        MAC Address      Interface        Type        Age
---------------  -----------------  --------------  --------  -----------
172.16.216.1     80:2A:A8:F1:D2:46  4/1             Gateway    0h  0m 10s
172.16.216.2     E2:91:F5:CC:E8:19  4/1             Dynamic    0h  2m 16s
172.16.216.4     78:8A:20:44:02:7F  4/1             Local         n/a
172.16.216.33    00:00:00:00:00:00  4/1             Dynamic    0h  0m  5s

```

**Help:** execute the command "show arp"

**Prompt:**
- ubiquiti_edgeswitch>
- ubiquiti_edgeswitch#

### show version

**Output:**
```
r

Switch: 1

System Description............................. EdgeSwitch 24-Port 250W, 1.8.0.5106045, Linux 3.6.5-1b505fb7, 0.0.0.0000000
Machine Type................................... EdgeSwitch 24-Port 250W
Machine Model.................................. ES-24-250W
 Serial Number.................................. 788A20BE0E00
Burned In MAC Address.......................... 78:8A:20:BE:0E:00
Software Version............................... 1.8.0.5106045

```

**Help:** execute the command "show version"

**Prompt:**
- ubiquiti_edgeswitch>
- ubiquiti_edgeswitch#

### show vlan

**Output:**
```
VLAN ID VLAN Name                        VLAN Type
------- -------------------------------- -------------------
1       default                          Default
101     ip tv                            Static
102     internet                         Static
216     hjemmenett                       Static
217     server                           Static

```

**Help:** execute the command "show vlan"

**Prompt:**
- ubiquiti_edgeswitch>
- ubiquiti_edgeswitch#

### terminal length 0

**Output:** None

**Help:** set the terminal width to the maximum

**Prompt:**
- ubiquiti_edgeswitch>
- ubiquiti_edgeswitch#

### terminal width 511

**Output:** None

**Help:** Execute the command terminal width 511. This automatically generated. Feel free to change it!

**Prompt:**
- ubiquiti_edgeswitch>
- ubiquiti_edgeswitch#

