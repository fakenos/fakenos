# ciena_saos


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
- ciena_saos>

### system shell session set more off

**Output:** None

**Help:** It enters the machine-to-machine interface mode (mmi-mode)

**Prompt:**
- ciena_saos>
- ciena_saos#

### rstp show

**Output:**
```
+---------------------Bridge-------------------+BridgeTimer+-------Bridge------+
|Rstp|    |            |  Root  |  Root  |Force|Fwd|Hlo|Max|T Chg|    Time     |
|Adm |Prio|   MacAdd   |  Cost  |  Port  |Versn|Dly|Tim|Age|Count|  Since TC   |
+----+----+------------+--------+--------+-----+---+---+---+-----+-------------+
 | ENA|8000|C4836F193CC0|       0|  ----  | RSTP| 15|  2| 20|    0|0000D00:00:00|
 +----+------------Designated-------------+-----+-RootTimer-+-----Enhancement---+
 |Rstp| Designated Root |Designated Bridge|Hops2|Fwd|Hlo|Max| Standards  |Debug |
|Mode|Prio|   MacAdd   |Prio|   MacAdd   |RootB|Dly|Tim|Age| Compliance |Events|
+----+----+------------+----+------------+-----+---+---+---+------------+------+
|RSTP|8000|C4836F193CC0|8000|C4836F193CC0|   0 | 15|  2| 20|CienaEnhance|  more|
 +----+----+------------+----+------------+-----+---+---+---+------------+------+
 +------------------------------ RSTP  Port  Info ------------------------------+
|        Port       |RSTP| STP|  |Path Cost |EdgeP|P2P_Mac|Domain|     Port    |
| Name  |Op|STP|Role| ST | ST |Pr|  Oper  |D|Ad|Op|Adm |Op|Adm|Ef|    UpTime   |
+-------+--+---+----+----+----+--+--------+-+--+--+----+--+---+--+-------------+
|1      |--|Ena| DIS|DISC| DIS| 8|   20000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|2      |--|Ena| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|3      |--|Ena| DIS|DISC| DIS| 8|   20000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|4      |--|Ena| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|5      |--|Ena| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|6      |--|Ena| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|7      |--|Ena| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|8      |--|Ena| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|9      |--|Ena| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|10     |--|Ena| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|11     |--|Ena| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|12     |--|Ena| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|13     |--|Ena| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|14     |--|Ena| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|15     |--|Ena| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|16     |--|Ena| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|17     |--|Ena| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|18     |--|Dis| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|19     |--|Dis| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|20     |--|Ena| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|21     |--|Dis| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|22     |--|Dis| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|23     |--|Ena| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|24     |--|Ena| DIS|DISC| DIS| 8|    2000|T| F| F|AUTO| F|  0| 0|0000D00:00:00|
|LAG1   |Up|Dis| DIS|FWD |FWD | 8|   20000|T| F| F|AUTO|T |  0| 0|0030D04:51:46|
|LAG2   |Up|Dis| DIS|FWD |FWD | 8|   20000|T| F| F|AUTO|T |  0| 0|0030D04:22:36|
 |LATERAL|--|Ena| DIS|DISC| DIS| 8| ------ |T| F| F|AUTO| F|  0| 0|0000D00:00:00|
+-------+--+---+----+----+----+--+--------+-+--+--+----+--+---+--+-------------+

```

**Help:** execute the command "rstp show"

**Prompt:**
- ciena_saos>
- ciena_saos#

### traffic-profiling standard-profile show

**Output:**
```
+---------------------------------------- STANDARD PROFILE TABLE -----------------------------------------+
|  Port |      Profile       |    |Parent|        BW (Kbps)    |   Max Burst KB  |       CLASSIFIERS      |
|       | ID | Name          |Role|#Child|    CIR   |    EIR   |   CBS  |   EBS  |                        |
+-------+----+---------------+----+------+----------+----------+--------+--------+------------------------+
|21     |1   |V4096          | N  |    0 |    10000 |        0 |   2000 |      0 | VS | TestA             |
+-------+----+---------------+----+------+----------+----------+--------+--------+------------------------+
|22     |1   |V4096          | N  |    0 |   100000 |        0 |   2000 |      0 | VS | TestB             |
+-------+----+---------------+----+------+----------+----------+--------+--------+------------------------+
|24     |1   |V4096          | N  |    0 |       32 |        0 |   3000 |      0 | VS | TestC             |
+-------+----+---------------+----+------+----------+----------+--------+--------+------------------------+
```

**Help:** execute the command "traffic-profiling standard-profile show"

**Prompt:**
- ciena_saos>
- ciena_saos#

### vlan show

**Output:**
```
+------------ VLAN GLOBAL CONFIGURATION ------------+
| Parameter         | Value                         |
+-------------------+---------------+---------------+
 | Inner TPID State  | Disabled                      |
|                   |                               |
| Field             | Admin         | Oper          |
+-------------------+---------------+---------------+
| Inner TPID        | 8100          | 8100          |
+-------------------+---------------+---------------+

+----+--------------------------------+------------------------+
|VLAN|                                |         111111111122222|
| ID | VLAN Name                Ports |123456789012345678901234|
+----+--------------------------------+------------------------+
|   1|Default                         |           x           x|
| 127|VLAN#127                        |x                      x|
| 666|Blackhole                       | xxxxxxxxxx xxxxxxxxxxx |
| 800|Mgmt                            |x                      x|
|1001|RVID_1001                       |x                      x|
+----+--------------------------------+------------------------+
 
+----------------------------- CROSS CONNECTION TABLE ------------------------------+
 | OVID | IVID |                           Port-A |                           Port-B |
+------+------+----------------------------------+----------------------------------+
 | No Entry Found                                                                    |
+------+------+----------------------------------+----------------------------------+
```

**Help:** execute the command "vlan show"

**Prompt:**
- ciena_saos>
- ciena_saos#

### chassis show temperature

**Output:**
```
+- TEMPERATURE THRESHOLD -+
| Low        | High       |
+------------+------------+
 | -40 C      | 65  C      |
+------------+------------+

+--- TEMPERATURE STATUS --+
| Current | Low   | High  |
+---------+-------+-------+
| 19  C   | 17  C | 20  C |
+---------+-------+-------+
```

**Help:** execute the command "chassis show temperature"

**Prompt:**
- ciena_saos>
- ciena_saos#

### software show

**Output:**
```
+------------------------------------------------------------------------------+
 | Installed Package   : saos-06-18-00-1848                                     |
| Running Package     : saos-06-18-00-1848                                     |
| Application Build   : 17704                                                  |
| Package Build Info  : Thu Feb 21 04:19:00 2019 autouser onxvpnjk02           |
| Running Kernel      : 3.10.54-grsec                                          |
| Running MIB Version : 04-18-00-0028                                          |
| Release Status      : GA                                                     |
+------------------------------------------------------------------------------+
 | Running bank        : B                                                      |
| Bank package version: saos-06-18-00-1848                                     |
| Bootloader version  : 17704                                                  |
| Bootloader status   : valid                                                  |
| Bank status         : valid (validated    17hr  7min 15sec ago)              |
| Standby bank        : A                                                      |
| Bank package version: saos-06-15-00-0242                                     |
| Bootloader version  : 12760                                                  |
| Bootloader status   : valid                                                  |
| Bank status         : valid (validated    17hr  6min 51sec ago)              |
+------------------------------------------------------------------------------+
 | Last command file: unknown                                                   |
| Last configuration file: unknown                                             |
+------------------------------------------------------------------------------+

```

**Help:** execute the command "software show"

**Prompt:**
- ciena_saos>
- ciena_saos#

### port show

**Output:**
```
+--------------- PORT GLOBAL CONFIGURATION ----------------+
|            Parameter             |       Value           |
+----------------------------------+-----------------------+
 | Rx Low Power Detect Admin State  | Disabled              |
+----------------------------------+-----------------------+
 +-------------------------------------------------------------------------------+
 | Port Table        |           Operational Status            |  Admin Config   |
|---------+---------+----+--------------+----+---+-------+----+----+-------+----|
 | Port    | Port    |    |  Link State  |    |   |       |Auto|    |       |Auto|
 | Name    | Type    |Link|   Duration   |XCVR|STP| Mode  |Neg |Link| Mode  |Neg |
|---------+---------+----+--------------+----+---+-------+----+----+-------+----|
 | 1.11    |100/G    | Up |  30d 2h24m21s|Ena |Dis|1000/FD| On |Ena |Auto/FD| On |
| 2.1     |100G/Gig |Down|   0d 0h 0m 0s|UCTF|Dis|       |    |Ena |Auto/FD| On |
| 3       |10/100/G | Up |  30d 1h55m12s|Ena |Dis|1000/FD| On |Ena |Auto/FD| On |
| 4       | G/10Gig |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |Auto/FD| On |
| 5       | G/10Gig |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |Auto/FD| On |
| 6       | G/10Gig |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |Auto/FD| On |
| 7       | G/10Gig |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |Auto/FD| On |
| 8       | G/10Gig |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |Auto/FD| On |
| 9       | G/10Gig |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |Auto/FD| On |
| 10      | G/10Gig |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |Auto/FD| On |
| 11      | G/10Gig |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |Auto/FD| On |
| 12      | G/10Gig |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |Auto/FD| On |
| 13      | G/10Gig |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |Auto/FD| On |
| 14      | G/10Gig |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |Auto/FD| On |
| 15      | G/10Gig |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |Auto/FD| On |
| 16      | G/10Gig |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |Auto/FD| On |
| 17      | G/10Gig |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |Auto/FD| On |
| 18      | G/10Gig |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |Auto/FD| On |
| 19      | G/10Gig |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |Auto/FD| On |
| 20      | G/10Gig |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |Auto/FD| On |
| 21      | G/10Gig |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |Auto/FD| On |
| 22      | G/10Gig |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |Auto/FD| On |
| 23      | G/10Gig |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |Auto/FD| On |
| 24      | G/10Gig |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |Auto/FD| On |
| LAG1    | LAG     | Up |  30d 2h24m21s|    |FWD|       |    |Ena |       |    |
| LAG2    | LAG     | Up |  30d 1h55m11s|    |FWD|       |    |Ena |       |    |
| LATERAL | LAG     |Down|   0d 0h 0m 0s|    |Dis|       |    |Ena |       |    |
+---------+---------+----+--------------+----+---+-------+----+----+-------+----+
```

**Help:** execute the command "port show"

**Prompt:**
- ciena_saos>
- ciena_saos#

### ssh server show key

**Output:**
```
+---------------------------- SSH SERVER KEY --------------------------------+
 | Key Status              | Generated                                        |
| Key Fingerprint [MD5]   | 1a:1d:1c:1e:da:11:1d:1d:11:aa:11:11:11:a1:11:1c  |
+-------------------------+--------------------------------------------------+
 
+------------------------ SSH PUBLIC KEY AUTHENTICATION USERS ------------------------+
 | Username                         | Key Status                                       |
+----------------------------------+--------------------------------------------------+
 | abc1                             | installed                                        |
| abc2                             | installed                                        |
+----------------------------------+--------------------------------------------------+

```

**Help:** execute the command "ssh server show key"

**Prompt:**
- ciena_saos>
- ciena_saos#

