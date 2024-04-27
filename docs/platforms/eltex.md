# eltex


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
- eltex>

### terminal datadump

**Output:** None

**Help:** set terminal width to maximum

**Prompt:**
- eltex>
- eltex#

### ex

**Output:**
```
True
```

**Help:** exit the terminal

**Prompt:**
- eltex>
- eltex#

### show vlan

**Output:**
```
Vlan            Name                    Tagged ports               Untagged ports            Type     Authorization
---- --------------------------- --------------------------- --------------------------- ------------ -------------
 1                -                           -              gi1/0/2,gi1/0/4-23,te1/0/1,   Default      Required
                                                             te1/0/3-4,Po1-12
 2          Telia-Sonera               te1/0/1,te1/0/4                    -               permanent     Required
111               -                    te1/0/1,te1/0/4                    -               permanent     Required
237           managment                te1/0/1,te1/0/4                 gi1/0/3            permanent     Required
255              NMS                   te1/0/1,te1/0/3-4                  -               permanent     Required
693  SS_1234567890-KOO-Y10-Golgo       te1/0/1,te1/0/4                    -               permanent     Required
     fa
914               -                       te1/0/3-4                       -               permanent     Required

```

**Help:** execute the command "show vlan"

**Prompt:**
- eltex>
- eltex#

### show system id

**Output:**
```
Serial number : ES12345678

```

**Help:** execute the command "show system id"

**Prompt:**
- eltex>
- eltex#

### show interfaces status

**Output:**
```
                                             Flow Link           Uptime       Back   Mdix
Port     Type         Duplex  Speed Neg      ctrl State         (d,h:m:s)   Pressure Mode    Port Mode (VLAN)
-------- ------------ ------  ----- -------- ---- ----------- ------------- -------- ------- ------------------------
gi1/0/1  1G-Copper    Full    1000  Enabled  Off  Up          183,19:35:02  Disabled Off     Trunk
gi1/0/2  1G-Copper    Full    1000  Enabled  Off  Up          183,19:34:59  Disabled On      Trunk
gi1/0/3  1G-Copper    Full    1000  Enabled  Off  Up          183,19:35:00  Disabled On      Trunk
gi1/0/4  1G-Copper    Full    1000  Enabled  Off  Up          183,19:34:59  Disabled Off     Trunk
gi1/0/5  1G-Copper      --      --     --     --  Down (nc)         --         --     --     Trunk
gi1/0/6  1G-Copper    Full    1000  Enabled  Off  Up          183,19:34:56  Disabled On      Trunk
gi1/0/7  1G-Copper    Full    1000  Enabled  Off  Up          181,20:48:48  Disabled On      Trunk
gi1/0/8  1G-Copper    Full    1000  Enabled  Off  Up          183,19:35:00  Disabled On      Trunk
gi1/0/9  1G-Copper    Full    1000  Enabled  Off  Up          183,19:34:56  Disabled On      Trunk
 gi1/0/10 1G-Copper    Full    1000  Enabled  Off  Up          183,19:34:50  Disabled On      Trunk
gi1/0/11 1G-Copper    Full    1000  Enabled  Off  Up          183,19:34:50  Disabled On      Trunk
gi1/0/12 1G-Copper    Full    1000  Enabled  Off  Up          183,19:34:50  Disabled Off     Trunk
 gi1/0/13 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Trunk
gi1/0/14 1G-Copper    Full    1000  Enabled  Off  Up          183,19:34:51  Disabled Off     Trunk
gi1/0/15 1G-Copper    Full    1000  Enabled  Off  Up                --      Disabled Off     Trunk
 gi1/0/16 1G-Copper    Full    1000  Enabled  Off  Up          183,19:34:51  Disabled Off     Trunk
gi1/0/17 1G-Copper    Full    1000  Enabled  Off  Up                --      Disabled Off     Access (1610)
gi1/0/18 1G-Copper    Full    1000  Enabled  Off  Up          00,07:41:23   Disabled On      Access (1)
gi1/0/19 1G-Copper      --      --     --     --  Down (adm)        --         --     --     Access (1609)
gi1/0/20 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
 gi1/0/21 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Trunk
gi1/0/22 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Trunk
gi1/0/23 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi1/0/24 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi1/0/25 1G-Copper    Full    100   Enabled  Off  Up          01,05:52:26   Disabled On      Access (1)
gi1/0/26 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi1/0/27 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi1/0/28 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
 gi1/0/29 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi1/0/30 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi1/0/31 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi1/0/32 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi1/0/33 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
 gi1/0/34 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi1/0/35 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi1/0/36 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi1/0/37 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi1/0/38 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
 gi1/0/39 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (355)
gi1/0/40 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi1/0/41 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1609)
gi1/0/42 1G-Copper    Full    100   Enabled  Off  Up          183,19:35:23  Disabled Off     Access (1609)
gi1/0/43 1G-Copper    Full    1000  Enabled  Off  Up          31,05:07:01   Disabled Off     Access (1609)
 gi1/0/44 1G-Copper    Full    1000  Enabled  Off  Up          31,05:07:01   Disabled On      Access (3800)
gi1/0/45 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (355)
gi1/0/46 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (130)
gi1/0/47 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1609)
gi1/0/48 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1609)
te1/0/1  10G-Fiber    Full    10000 Disabled Off  Up          183,19:35:22  Disabled Off     Trunk
te1/0/2  10G-Fiber      --      --     --     --  Down (nc)         --         --     --     Trunk
gi2/0/1  1G-Copper      --      --     --     --  Down (nc)         --         --     --     Trunk
gi2/0/2  1G-Copper      --      --     --     --  Down (nc)         --         --     --     Trunk
gi2/0/3  1G-Copper      --      --     --     --  Down (nc)         --         --     --     Trunk
gi2/0/4  1G-Copper      --      --     --     --  Down (nc)         --         --     --     Trunk
gi2/0/5  1G-Copper      --      --     --     --  Down (nc)         --         --     --     Trunk
gi2/0/6  1G-Copper      --      --     --     --  Down (nc)         --         --     --     Trunk
gi2/0/7  1G-Copper      --      --     --     --  Down (nc)         --         --     --     Trunk
gi2/0/8  1G-Copper      --      --     --     --  Down (nc)         --         --     --     Trunk
gi2/0/9  1G-Copper      --      --     --     --  Down (nc)         --         --     --     Trunk
gi2/0/10 1G-Copper    Full    1000  Enabled  Off  Up                --      Disabled On      Trunk
 gi2/0/11 1G-Copper    Full    1000  Enabled  Off  Up                --      Disabled On      Trunk
gi2/0/12 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Trunk
gi2/0/13 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Trunk
 gi2/0/14 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Trunk
gi2/0/15 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Trunk
gi2/0/16 1G-Copper    Full    1000  Enabled  Off  Up                --      Disabled On      Trunk
 gi2/0/17 1G-Copper    Full    1000  Enabled  Off  Up                --      Disabled Off     Access (1610)
gi2/0/18 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi2/0/19 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi2/0/20 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi2/0/21 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
 gi2/0/22 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi2/0/23 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi2/0/24 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1609)
gi2/0/25 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi2/0/26 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
 gi2/0/27 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi2/0/28 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi2/0/29 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi2/0/30 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1609)
gi2/0/31 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
 gi2/0/32 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi2/0/33 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi2/0/34 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi2/0/35 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi2/0/36 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
 gi2/0/37 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi2/0/38 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi2/0/39 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi2/0/40 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi2/0/41 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
 gi2/0/42 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi2/0/43 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi2/0/44 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi2/0/45 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1)
gi2/0/46 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (130)
 gi2/0/47 1G-Copper    Full    1000  Enabled  Off  Up          183,19:37:01  Disabled Off     Access (1609)
gi2/0/48 1G-Copper      --      --     --     --  Down (nc)         --         --     --     Access (1609)
te2/0/1  10G-Fiber      --      --     --     --  Down (nc)         --         --     --     Access (1)
te2/0/2  10G-Fiber      --      --     --     --  Down (nc)         --         --     --     Trunk

                                          Flow    Link
Ch       Type    Duplex  Speed  Neg      control  State         Port Mode (VLAN)
-------- ------- ------  -----  -------- -------  ------------- ------------------------
Po1         --     --      --      --       --    Not Present   Trunk
Po2         --     --      --      --       --    Not Present   Trunk
Po3         --     --      --      --       --    Not Present   Trunk
Po4         --     --      --      --       --    Not Present   Trunk
Po5         --     --      --      --       --    Not Present   Trunk
Po6         --     --      --      --       --    Not Present   Trunk
Po7         --     --      --      --       --    Not Present   Trunk
Po8         --     --      --      --       --    Not Present   Trunk
Po9         --     --      --      --       --    Not Present   Trunk
Po10        --     --      --      --       --    Not Present   Trunk
Po11        --     --      --      --       --    Not Present   Trunk
Po12        --     --      --      --       --    Not Present   Trunk
Po13        --     --      --      --       --    Not Present   Trunk
Po14        --     --      --      --       --    Not Present   Trunk
Po15        --     --      --      --       --    Not Present   Trunk
Po16        --     --      --      --       --    Not Present   Trunk
Po17        --     --      --      --       --    Not Present   Access (1)
Po18        --     --      --      --       --    Not Present   Access (1)
Po19        --     --      --      --       --    Not Present   Access (1)
Po20        --     --      --      --       --    Not Present   Access (1)
Po21        --     --      --      --       --    Not Present   Access (1)
Po22        --     --      --      --       --    Not Present   Access (1)
Po23        --     --      --      --       --    Not Present   Access (1)
Po24        --     --      --      --       --    Not Present   Access (1)
Po25        --     --      --      --       --    Not Present   Access (1)
Po26        --     --      --      --       --    Not Present   Access (1)
Po27        --     --      --      --       --    Not Present   Access (1)
Po28        --     --      --      --       --    Not Present   Access (1)
Po29        --     --      --      --       --    Not Present   Access (1)
Po30        --     --      --      --       --    Not Present   Access (1)
Po31        --     --      --      --       --    Not Present   Access (1)
Po32        --     --      --      --       --    Not Present   Access (1)
Po33        --     --      --      --       --    Not Present   Access (1)
Po34        --     --      --      --       --    Not Present   Access (1)
Po35        --     --      --      --       --    Not Present   Access (1)
Po36        --     --      --      --       --    Not Present   Access (1)
Po37        --     --      --      --       --    Not Present   Access (1)
Po38        --     --      --      --       --    Not Present   Access (1)
Po39        --     --      --      --       --    Not Present   Access (1)
Po40        --     --      --      --       --    Not Present   Access (1)
Po41        --     --      --      --       --    Not Present   Access (1)
Po42        --     --      --      --       --    Not Present   Access (1)
Po43        --     --      --      --       --    Not Present   Access (1)
Po44        --     --      --      --       --    Not Present   Access (1)
Po45        --     --      --      --       --    Not Present   Access (1)
Po46        --     --      --      --       --    Not Present   Access (1)
Po47        --     --      --      --       --    Not Present   Access (1)
Po48        --     --      --      --       --    Not Present   Access (1)

                                              Link
Oob       Type         Duplex  Speed Neg      State
--------  ------------ ------  ----- -------- -----------
oob       1G-Copper      --      --     --    Down

nc (not connected): The interface is not connected.
err (error-disabled): The interface was suspended by the system.
adm (admin.shutdown): The interface was suspended by administrator.

```

**Help:** execute the command "show interfaces status"

**Prompt:**
- eltex>
- eltex#

### show system

**Output:**
```
System Description:                       MES3124 28-port 1G/10G Managed Switch
System Up Time (days,hour:min:sec):       67,08:57:53
System Contact:                           email@email.com
System Name:                              Eltex3124-3
System Location:                          Elm street, 1428
System MAC Address:                       12:34:56:78:90:00
System Object ID:                         1.3.6.1.4.1.35265.1.24

Main Power Supply Status [AC]:            OK
Redundant Power Supply Status [DC]:       OK
Fan 1 Status:                             OK
Fan 2 Status:                             OK
Fan 3 Status:                             OK
Fan 4 Status:                             OK

 Sensor Index            Temperature (Celsius)           Status
---------------------  --------------------------  -------------------
      1                       29                          OK
      2                       43                          OK
      3                       45                          OK

```

**Help:** execute the command "show system"

**Prompt:**
- eltex>
- eltex#

### show interface

**Output:**
```
------------------ show interfaces gi1/0/1 ------------------
gigabitethernet1/0/1 is up (connected)
  Interface index is 49
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:41
  Description: link_to_MGTS_ADSL
  Interface MTU is 1500
  Full-duplex, 1000Mbps, link type is auto, media type is 1G-Fiber
  Link is up for 0 days, 0 hours, 0 minutes and -40760306 seconds
  Advertised link modes: 1000baseT/Full
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 1321 Kbit/s
  15 second output rate is 1315 Kbit/s
      108873837739 packets input, 7385782387851 bytes received
      73700287 broadcasts, 4537873 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      109055618146 packets output, 7350024234403 bytes sent
      108034 broadcasts, 1439641 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/2 ------------------
gigabitethernet1/0/2 is up (connected)
  Interface index is 50
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:42
  Description: LAN (Office)
  Interface MTU is 1500
  Full-duplex, 1000Mbps, link type is auto, media type is 1G-Fiber
  Link is up for 2 days, 18 hours, 37 minutes and 5 seconds
  Advertised link modes: 1000baseT/Full
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 168706 Kbit/s
  15 second output rate is 51870 Kbit/s
      396190779063 packets input, 476968058054193 bytes received
      2824380 broadcasts, 25865641 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      330426396743 packets output, 227106169368911 bytes sent
      38634166 broadcasts, 132202046940 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/3 ------------------
 gigabitethernet1/0/3 is up (connected)
  Interface index is 51
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:43
  Description: Eltex1124M - gi1/0/1
  Interface MTU is 1500
  Full-duplex, 1000Mbps, link type is auto, media type is 1G-Fiber
  Link is up for 0 days, 0 hours, 0 minutes and -12007484 seconds
  Advertised link modes: 1000baseT/Full
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 21 Kbit/s
  15 second output rate is 28 Kbit/s
      1127701000 packets input, 330048141411 bytes received
      5798212 broadcasts, 3596982 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      2248533117 packets output, 2498371279437 bytes sent
      84020339 broadcasts, 19047121 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/4 ------------------
gigabitethernet1/0/4 is up (connected)
  Interface index is 52
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:44
  Description: L2_OST_M9
  Interface MTU is 1500
  Full-duplex, 1000Mbps, link type is auto, media type is 1G-Fiber
  Link is up for 0 days, 0 hours, 0 minutes and -39131125 seconds
  Advertised link modes: 1000baseT/Full
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 674910 Kbit/s
  15 second output rate is 34908 Kbit/s
      324252795264 packets input, 441557871273045 bytes received
      670821 broadcasts, 324194976402 multicasts
      1 input errors, 0 FCS, 0 alignment
      0 oversize, 1 internal MAC
      0 pause frames received
      14199838076 packets output, 19261838800370 bytes sent
      262737 broadcasts, 14142282124 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/5 ------------------
 gigabitethernet1/0/5 is down (admin.shutdown)
  Interface index is 53
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:45
  Interface MTU is 1500
  Link is down for 2 days, 18 hours, 37 minutes and 33 seconds
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/6 ------------------
gigabitethernet1/0/6 is down (admin.shutdown)
  Interface index is 54
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:46
  Interface MTU is 1500
  Link is down for 2 days, 18 hours, 37 minutes and 33 seconds
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/7 ------------------
gigabitethernet1/0/7 is down (admin.shutdown)
  Interface index is 55
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:47
  Interface MTU is 1500
  Link is down for 2 days, 18 hours, 37 minutes and 34 seconds
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/8 ------------------
gigabitethernet1/0/8 is down (admin.shutdown)
  Interface index is 56
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:48
  Interface MTU is 1500
  Link is down for 2 days, 18 hours, 37 minutes and 35 seconds
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/9 ------------------
gigabitethernet1/0/9 is down (admin.shutdown)
  Interface index is 57
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:49
  Interface MTU is 1500
  Link is down for 2 days, 18 hours, 37 minutes and 36 seconds
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/10 ------------------
gigabitethernet1/0/10 is down (admin.shutdown)
  Interface index is 58
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:4a
  Interface MTU is 1500
  Link is down for 2 days, 18 hours, 37 minutes and 37 seconds
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/11 ------------------
gigabitethernet1/0/11 is up (connected)
  Interface index is 59
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:4b
  Description: ASR920-1 - Gi0 (MGMT_BSH2)
  Interface MTU is 1500
  Full-duplex, 1000Mbps, link type is auto, media type is 1G-Combo-C
  Link is up for 0 days, 0 hours, 0 minutes and -31270588 seconds
  Advertised link modes: 1000baseT/Full 100baseT/Full
                         100baseT/Half 10baseT/Full
                         10baseT/Half
  Flow control is off, MDIX mode is cross
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      36368707 packets input, 8017641772 bytes received
      12 broadcasts, 11854 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      41766075 packets output, 4693865203 bytes sent
      15107491 broadcasts, 1511338 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/12 ------------------
 gigabitethernet1/0/12 is up (connected)
  Interface index is 60
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:4c
  Description: ASR920-2 - Gi0 (MGMT_BSH2)
  Interface MTU is 1500
  Full-duplex, 1000Mbps, link type is auto, media type is 1G-Combo-C
  Link is up for 0 days, 0 hours, 0 minutes and -31274488 seconds
  Advertised link modes: 1000baseT/Full 100baseT/Full
                         100baseT/Half 10baseT/Full
                         10baseT/Half
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      36635681 packets input, 8790158609 bytes received
      12 broadcasts, 11833 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      41798808 packets output, 4773894689 bytes sent
      15107508 broadcasts, 1511357 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/13 ------------------
 gigabitethernet1/0/13 is down (admin.shutdown)
  Interface index is 61
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:4d
  Interface MTU is 1500
  Link is down for 2 days, 18 hours, 37 minutes and 40 seconds
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/14 ------------------
 gigabitethernet1/0/14 is down (admin.shutdown)
  Interface index is 62
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:4e
  Interface MTU is 1500
  Link is down for 2 days, 18 hours, 37 minutes and 41 seconds
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/15 ------------------
 gigabitethernet1/0/15 is down (admin.shutdown)
  Interface index is 63
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:4f
  Interface MTU is 1500
  Link is down for 2 days, 18 hours, 37 minutes and 43 seconds
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/16 ------------------
 gigabitethernet1/0/16 is down (admin.shutdown)
  Interface index is 64
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:50
  Interface MTU is 1500
  Link is down for 2 days, 18 hours, 37 minutes and 45 seconds
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/17 ------------------
 gigabitethernet1/0/17 is down (admin.shutdown)
  Interface index is 65
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:51
  Interface MTU is 1500
  Link is down for 2 days, 18 hours, 37 minutes and 46 seconds
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/18 ------------------
 gigabitethernet1/0/18 is down (admin.shutdown)
  Interface index is 66
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:52
  Interface MTU is 1500
  Link is down for 2 days, 18 hours, 37 minutes and 47 seconds
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/19 ------------------
 gigabitethernet1/0/19 is down (admin.shutdown)
  Interface index is 67
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:53
  Interface MTU is 1500
  Link is down for 2 days, 18 hours, 37 minutes and 48 seconds
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/20 ------------------
 gigabitethernet1/0/20 is down (admin.shutdown)
  Interface index is 68
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:54
  Interface MTU is 1500
  Link is down for 2 days, 18 hours, 37 minutes and 50 seconds
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/21 ------------------
 gigabitethernet1/0/21 is down (admin.shutdown)
  Interface index is 69
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:55
  Interface MTU is 1500
  Link is down for 2 days, 18 hours, 37 minutes and 51 seconds
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/22 ------------------
 gigabitethernet1/0/22 is down (admin.shutdown)
  Interface index is 70
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:56
  Interface MTU is 1500
  Link is down for 2 days, 18 hours, 37 minutes and 52 seconds
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/23 ------------------
 gigabitethernet1/0/23 is down (admin.shutdown)
  Interface index is 71
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:57
  Interface MTU is 1500
  Link is down for 2 days, 18 hours, 37 minutes and 53 seconds
  Flow control is off, MDIX mode is unknown
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces gi1/0/24 ------------------
 gigabitethernet1/0/24 is down (admin.shutdown)
  Interface index is 72
  Hardware is gigabitethernet, MAC address is e8:28:c1:5c:02:58
  Interface MTU is 1500
  Link is down for 2 days, 18 hours, 38 minutes and 0 seconds
  Flow control is off, MDIX mode is unknown
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces te1/0/1 ------------------
tengigabitethernet1/0/1 is up (connected)
  Interface index is 105
  Hardware is tengigabitethernet, MAC address is e8:28:c1:5c:02:59
  Description: N9K-1 - eth1/18 (Po1)
  Interface MTU is 1500
  Full-duplex, 10000Mbps, link type is 10000Mbps full-duplex, media type is 10G-Fiber
  Link is up for 2 days, 18 hours, 38 minutes and 0 seconds
  Flow control is off, MDIX mode is normal
  FEC is disabled
  5 second input rate is 51910 Kbit/s
  5 second output rate is 344782 Kbit/s
      274085380822 packets input, 164119962658503 bytes received
      243661784 broadcasts, 105648246049 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      346719236719 packets output, 371416643096885 bytes sent
      9147208 broadcasts, 123471943176 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces te1/0/2 ------------------
 tengigabitethernet1/0/2 is up (connected)
  Interface index is 106
  Hardware is tengigabitethernet, MAC address is e8:28:c1:5c:02:5a
  Description: N9K-1 - eth1/19 (Po1)
  Interface MTU is 1500
  Full-duplex, 10000Mbps, link type is 10000Mbps full-duplex, media type is 10G-Fiber
  Link is up for 0 days, 0 hours, 0 minutes and -36668287 seconds
  Flow control is off, MDIX mode is normal
  FEC is disabled
  5 second input rate is 36277 Kbit/s
  5 second output rate is 499662 Kbit/s
      93081707442 packets input, 51410670602855 bytes received
      90432414 broadcasts, 25421955562 multicasts
      56 input errors, 38 FCS, 0 alignment
      0 oversize, 16 internal MAC
      0 pause frames received
      314234071944 packets output, 371471867677116 bytes sent
      3345667 broadcasts, 200541023323 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces te1/0/3 ------------------
 tengigabitethernet1/0/3 is down (admin.shutdown)
  Interface index is 107
  Hardware is tengigabitethernet, MAC address is e8:28:c1:5c:02:5b
  Interface MTU is 1500
  Link is down for 2 days, 18 hours, 38 minutes and 3 seconds
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces te1/0/4 ------------------
 tengigabitethernet1/0/4 is up (connected)
  Interface index is 108
  Hardware is tengigabitethernet, MAC address is e8:28:c1:5c:02:5c
  Description: Eltex3124-2 - te1/0/1
  Interface MTU is 1500
  Full-duplex, 10000Mbps, link type is 10000Mbps full-duplex, media type is 10G-Fiber
  Link is up for 2 days, 18 hours, 38 minutes and 3 seconds
  Flow control is off, MDIX mode is normal
  FEC is disabled
  15 second input rate is 0 Kbit/s
  15 second output rate is 1 Kbit/s
      49640783 packets input, 4437603028 bytes received
      1454 broadcasts, 23188937 multicasts
      2 input errors, 1 FCS, 0 alignment
      0 oversize, 1 internal MAC
      0 pause frames received
      73595762 packets output, 9744002055 bytes sent
      26740544 broadcasts, 20413128 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
  Output queues: (queue #: packets passed/packets dropped)
      1: 0/0
      2: 0/0
      3: 0/0
      4: 0/0
      5: 0/0
      6: 0/0
      7: 0/0
      8: 0/0
------------------ show interfaces Po1 ------------------
 Po1 is up (connected)
  Interface index is 1000
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:41
  Description: N9K-1 - po25
  Interface MTU is 1500
  Link is up for 2 days, 18 hours, 38 minutes and 0 seconds
    Link aggregation type is LACP
    No. of members in this port-channel: 2 (active 2)
      tengigabitethernet1/0/1, full-duplex, LACP active, 10000Mbps (active)
      tengigabitethernet1/0/2, full-duplex, LACP active, 10000Mbps (active)
    Active bandwidth is 20000Mbps
  15 second input rate is 88280 Kbit/s
  15 second output rate is 848490 Kbit/s
      367167172559 packets input, 215530683039427 bytes received
      334094237 broadcasts, 131070234700 multicasts
      56 input errors, 38 FCS, 0 alignment
      0 oversize, 16 internal MAC
      0 pause frames received
      660953658224 packets output, 742888970320949 bytes sent
      12492875 broadcasts, 324013229657 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po2 ------------------
Po2 is down (not connected)
  Interface index is 1001
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po3 ------------------
 Po3 is down (not connected)
  Interface index is 1002
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po4 ------------------
Po4 is down (not connected)
  Interface index is 1003
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po5 ------------------
Po5 is down (not connected)
  Interface index is 1004
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po6 ------------------
Po6 is down (not connected)
  Interface index is 1005
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po7 ------------------
Po7 is down (not connected)
  Interface index is 1006
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po8 ------------------
Po8 is down (not connected)
  Interface index is 1007
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po9 ------------------
Po9 is down (not connected)
  Interface index is 1008
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po10 ------------------
Po10 is down (not connected)
  Interface index is 1009
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po11 ------------------
Po11 is down (not connected)
  Interface index is 1010
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po12 ------------------
Po12 is down (not connected)
  Interface index is 1011
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po13 ------------------
Po13 is down (not connected)
  Interface index is 1012
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po14 ------------------
Po14 is down (not connected)
  Interface index is 1013
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po15 ------------------
Po15 is down (not connected)
  Interface index is 1014
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po16 ------------------
Po16 is down (not connected)
  Interface index is 1015
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po17 ------------------
Po17 is down (not connected)
  Interface index is 1016
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po18 ------------------
Po18 is down (not connected)
  Interface index is 1017
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po19 ------------------
Po19 is down (not connected)
  Interface index is 1018
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po20 ------------------
Po20 is down (not connected)
  Interface index is 1019
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po21 ------------------
Po21 is down (not connected)
  Interface index is 1020
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po22 ------------------
Po22 is down (not connected)
  Interface index is 1021
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po23 ------------------
Po23 is down (not connected)
  Interface index is 1022
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po24 ------------------
Po24 is down (not connected)
  Interface index is 1023
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po25 ------------------
Po25 is down (not connected)
  Interface index is 1024
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po26 ------------------
Po26 is down (not connected)
  Interface index is 1025
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po27 ------------------
Po27 is down (not connected)
  Interface index is 1026
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po28 ------------------
Po28 is down (not connected)
  Interface index is 1027
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po29 ------------------
Po29 is down (not connected)
  Interface index is 1028
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po30 ------------------
Po30 is down (not connected)
  Interface index is 1029
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po31 ------------------
Po31 is down (not connected)
  Interface index is 1030
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po32 ------------------
Po32 is down (not connected)
  Interface index is 1031
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po33 ------------------
Po33 is down (not connected)
  Interface index is 1032
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po34 ------------------
Po34 is down (not connected)
  Interface index is 1033
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po35 ------------------
Po35 is down (not connected)
  Interface index is 1034
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po36 ------------------
Po36 is down (not connected)
  Interface index is 1035
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po37 ------------------
Po37 is down (not connected)
  Interface index is 1036
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po38 ------------------
Po38 is down (not connected)
  Interface index is 1037
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po39 ------------------
Po39 is down (not connected)
  Interface index is 1038
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po40 ------------------
Po40 is down (not connected)
  Interface index is 1039
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po41 ------------------
Po41 is down (not connected)
  Interface index is 1040
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po42 ------------------
Po42 is down (not connected)
  Interface index is 1041
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po43 ------------------
Po43 is down (not connected)
  Interface index is 1042
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po44 ------------------
Po44 is down (not connected)
  Interface index is 1043
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po45 ------------------
Po45 is down (not connected)
  Interface index is 1044
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po46 ------------------
Po46 is down (not connected)
  Interface index is 1045
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po47 ------------------
Po47 is down (not connected)
  Interface index is 1046
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces Po48 ------------------
Po48 is down (not connected)
  Interface index is 1047
  Hardware is aggregated ethernet interface(s), MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1500
  15 second input rate is 0 Kbit/s
  15 second output rate is 0 Kbit/s
      0 packets input, 0 bytes received
      0 broadcasts, 0 multicasts
      0 input errors, 0 FCS, 0 alignment
      0 oversize, 0 internal MAC
      0 pause frames received
      0 packets output, 0 bytes sent
      0 broadcasts, 0 multicasts
      0 output errors, 0 collisions
      0 excessive collisions, 0 late collisions
      0 pause frames transmitted
      0 symbol errors, 0 carrier, 0 SQE test error
------------------ show interfaces tunnel1 ------------------
tunnel1 is down (not connected)
  Interface index is 3000
  Hardware is tunnel, MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1476
------------------ show interfaces tunnel2 ------------------
 tunnel2 is down (not connected)
  Interface index is 3001
  Hardware is tunnel, MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1476
------------------ show interfaces tunnel3 ------------------
tunnel3 is down (not connected)
  Interface index is 3002
  Hardware is tunnel, MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1476
------------------ show interfaces tunnel4 ------------------
 tunnel4 is down (not connected)
  Interface index is 3003
  Hardware is tunnel, MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1476
------------------ show interfaces tunnel5 ------------------
tunnel5 is down (not connected)
  Interface index is 3004
  Hardware is tunnel, MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1476
------------------ show interfaces tunnel6 ------------------
 tunnel6 is down (not connected)
  Interface index is 3005
  Hardware is tunnel, MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1476
------------------ show interfaces tunnel7 ------------------
tunnel7 is down (not connected)
  Interface index is 3006
  Hardware is tunnel, MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1476
------------------ show interfaces tunnel8 ------------------
 tunnel8 is down (not connected)
  Interface index is 3007
  Hardware is tunnel, MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1476
------------------ show interfaces tunnel9 ------------------
tunnel9 is down (not connected)
  Interface index is 3008
  Hardware is , MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1476
------------------ show interfaces tunnel10 ------------------
 tunnel10 is down (not connected)
  Interface index is 3009
  Hardware is tunnel, MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1476
------------------ show interfaces tunnel11 ------------------
tunnel11 is down (not connected)
  Interface index is 3010
  Hardware is tunnel, MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1476
------------------ show interfaces tunnel12 ------------------
 tunnel12 is down (not connected)
  Interface index is 3011
  Hardware is tunnel, MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1476
------------------ show interfaces tunnel13 ------------------
tunnel13 is down (not connected)
  Interface index is 3012
  Hardware is tunnel, MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1476
------------------ show interfaces tunnel14 ------------------
 tunnel14 is down (not connected)
  Interface index is 3013
  Hardware is tunnel, MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1476
------------------ show interfaces tunnel15 ------------------
tunnel15 is down (not connected)
  Interface index is 3014
  Hardware is tunnel, MAC address is e8:28:c1:5c:02:40
  Interface MTU is 1476

```

**Help:** execute the command "show interface"

**Prompt:**
- eltex>
- eltex#

### show ip interface

**Output:**
```
  Gateway IP Address        Activity status       Type
----------------------- ----------------------- --------
10.150.0.101            Active                  static


    IP Address         I/F       Type       Status
------------------- --------- ----------- -----------
0.0.0.0/32          vlan 1    DHCP        Not
                                          received
10.150.0.9/24       vlan 150  Static      Valid

```

**Help:** execute the command "show ip interface"

**Prompt:**
- eltex>
- eltex#

### show interfaces description

**Output:**
```
                                  Admin Link
Port     Port Mode (VLAN)         State State       Description
-------- ------------------------ ----- ----------- -----------
gi1/0/1  Trunk                    Up    Up          link_to_MGTS_ADSL
gi1/0/2  Trunk                    Up    Up          BS12700_-LAN (Office)
gi1/0/3  Trunk                    Up    Up          Eltex1124M - gi1/0/1
gi1/0/4  Trunk                    Up    Up          L2_OST_M9
gi1/0/5  Access (1)               Down  Down
gi1/0/6  Access (1)               Down  Down
gi1/0/7  Access (1)               Down  Down
gi1/0/8  Access (1)               Down  Down
gi1/0/9  Access (1)               Down  Down
gi1/0/10 Access (1)               Down  Down
gi1/0/11 Access (111)             Up    Up          ASR920-1 - Gi0
gi1/0/12 Access (111)             Up    Up          ASR920-2 - Gi0
gi1/0/13 Access (1)               Down  Down
gi1/0/14 Access (1)               Down  Down
gi1/0/15 Access (1)               Down  Down
 gi1/0/16 Access (1)               Down  Down
gi1/0/17 Access (1)               Down  Down
gi1/0/18 Access (1)               Down  Down
gi1/0/19 Access (1)               Down  Down
gi1/0/20 Access (1)               Down  Down
 gi1/0/21 Access (1)               Down  Down
gi1/0/22 Access (1)               Down  Down
gi1/0/23 Access (1)               Down  Down
gi1/0/24 Access (1)               Down  Down
te1/0/1  Trunk                    Up    Up          N9K-1 - eth1/18 (Po1)
te1/0/2  Trunk                    Up    Up          N9K-1 - eth1/19 (Po1)
te1/0/3  Access (1)               Down  Down
te1/0/4  Trunk                    Up    Up          Eltex3124-2 - te1/0/1

                                  Admin Link
Ch       Port Mode (VLAN)         State State       Description
-------- ------------------------ ----- ----------- -----------
Po1      Trunk                    Up    Up          N9K-1 - po25
Po2      Access (1)               Up    Not Present
Po3      Access (1)               Up    Not Present
Po4      Access (1)               Up    Not Present
Po5      Access (1)               Up    Not Present
Po6      Access (1)               Up    Not Present
Po7      Access (1)               Up    Not Present
Po8      Access (1)               Up    Not Present
Po9      Access (1)               Up    Not Present
Po10     Access (1)               Up    Not Present
Po11     Access (1)               Up    Not Present
Po12     Access (1)               Up    Not Present

Vlan Admin State Link State           Description
---- ----------- ---------- --------------------------------
1    Up          Up         -
4    Up          Up         SW_MGMT
634  Up          Up         Multicast Office


         Admin Link
Oob-eth  State State       Description
-------- ----- ----------- -----------
oob      Up    Up          ASR920-1 - Gi0/0/0

```

**Help:** execute the command "show interfaces description"

**Prompt:**
- eltex>
- eltex#

### show interfaces switchport

**Output:**
```
Added by: D-Default, S-Static, G-GVRP, R-Radius Assigned VLAN, T-Guest VLAN, V-Voice VLAN
Port : gi1/0/1
Port Mode: Trunk
Gvrp Status: disabled
 Ingress Filtering: true
Acceptable Frame Type: admitAll
Ingress UnTagged VLAN ( NATIVE ): 4094
Protected: Disabled

Port is member in:

Vlan               Name               Egress rule     Added by
---- -------------------------------- ----------- ----------------
130             Servers_OS              Tagged           S
4094               NULL                Untagged          S

 
Forbidden VLANS:
Vlan               Name
---- --------------------------------
 

Classification rules:

Protocol based VLANs:
  Group ID   Vlan ID
------------ -------


Mac based VLANs:
  Group ID   Vlan ID
------------ -------

```

**Help:** execute the command "show interfaces switchport"

**Prompt:**
- eltex>
- eltex#

