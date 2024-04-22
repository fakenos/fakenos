# juniper_screenos


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
- juniper_screenos>

### set console page 0

**Output:** None

**Help:** set the terminal width to maximum

**Prompt:**
- juniper_screenos>
- juniper_screenos#

### get route

**Output:**
```
IPv4 Dest-Routes for <untrust-vr> (0 entries)
----------------------------------------------------------------------
 H: Host C: Connected S: Static A: Auto-Exported
I: Imported R: RIP P: Permanent D: Auto-Discovered
iB: IBGP eB: EBGP O: OSPF E1: OSPF external type 1
E2: OSPF external type 2

IPv4 Dest-Routes for <trust-vr> (4 entries)
----------------------------------------------------------------------
   ID          IP-Prefix  Interface    Gateway   P Pref    Mtr    Vsys
----------------------------------------------------------------------
*   4         1.1.1.2/32     eth0/1    0.0.0.0   H    0      0    Root
*   2     192.168.1.1/32     eth0/0    0.0.0.0   H    0      0    Root
*   1     192.168.1.0/24     eth0/0    0.0.0.0   C    0      0    Root
*   3         1.1.1.0/24     eth0/1    0.0.0.0   C    0      0    Root

```

**Help:** execute the command "get route"

**Prompt:**
- juniper_screenos>
- juniper_screenos#

