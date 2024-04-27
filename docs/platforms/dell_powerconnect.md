# dell_powerconnect


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
- dell_powerconnect>

### show interfaces status

**Output:**
```
Flow Link          Back   Mdix
Port     Type         Duplex  Speed Neg      ctrl State       Pressure Mode
-------- ------------ ------  ----- -------- ---- ----------- -------- -------
g1       1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g2       1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g3       1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g4       1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g5       1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g6       1G-Copper    Full    100   Enabled  Off  Up          Disabled On
g7       1G-Copper    Full    100   Enabled  Off  Up          Disabled On
g8       1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g9       1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g10      1G-Copper    Full    1000  Enabled  Off  Up          Disabled Off
g11      1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g12      1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g13      1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g14      1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g15      1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g16      1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g17      1G-Copper    Full    1000  Enabled  Off  Up          Disabled Off
g18      1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g19      1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g20      1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g21      1G-Copper    Full    100   Enabled  Off  Up          Disabled On
g22      1G-Copper    Full    100   Enabled  Off  Up          Disabled On
g23      1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g24      1G-Copper    Full    1000  Enabled  Off  Up          Disabled Off
g25      1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g26      1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g27      1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g28      1G-Copper    Full    100   Enabled  Off  Up          Disabled On
g29      1G-Copper    Full    100   Enabled  Off  Up          Disabled On
g30      1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g31      1G-Copper    Full    1000  Enabled  Off  Up          Disabled Off
g32      1G-Copper    Full    1000  Enabled  Off  Up          Disabled Off
g33      1G-Copper    Full    100   Enabled  Off  Up          Disabled On
g34      1G-Copper    Full    100   Enabled  Off  Up          Disabled On
g35      1G-Copper    Full    100   Enabled  Off  Up          Disabled On
g36      1G-Copper      --      --     --     --  Down           --     --
g37      1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g38      1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g39      1G-Copper    Full    100   Enabled  Off  Up          Disabled On
g40      1G-Copper      --      --     --     --  Down           --     --
g41      1G-Copper    Full    100   Enabled  Off  Up          Disabled On
g42      1G-Copper    Full    100   Enabled  Off  Up          Disabled On
g43      1G-Copper    Full    1000  Enabled  Off  Up          Disabled On
g44      1G-Copper    Full    1000  Enabled  Off  Up          Disabled Off
g45      1G-Combo-C     --      --     --     --  Down           --     --
g46      1G-Combo-C     --      --     --     --  Down           --     --
g47      1G-Combo-C     --      --     --     --  Down           --     --
g48      1G-Combo-F   Full    1000  Enabled  Off  Up          Disabled Off

Flow    Link
Ch       Type    Duplex  Speed  Neg      control  State
-------- ------- ------  -----  -------- -------  -----------
ch1         --     --      --      --       --    Not Present
ch2         --     --      --      --       --    Not Present
ch3         --     --      --      --       --    Not Present
ch4         --     --      --      --       --    Not Present
ch5         --     --      --      --       --    Not Present
ch6         --     --      --      --       --    Not Present
ch7         --     --      --      --       --    Not Present
ch8         --     --      --      --       --    Not Present

```

**Help:** execute the command "show interfaces status"

**Prompt:**
- dell_powerconnect>
- dell_powerconnect#

### show interfaces description

**Output:**
```
Port      Description
-------   -----------
g1        TO_SRV05-VSAN_[DRAC]
g2        TO_SRV11-V6_[DRAC]
g3        TO_SRV06-V6_[DRAC]
g4        TO_SRV07-V6_[DRAC]
g5        TO_SRV08-V6_[DRAC]
g6        TO-NAS-MASTER_[DRAC]
g7        TO-NAS-MASTER_[admin]
g8        SRV-IDRAC
g9        SRV-EXT2-IDRAC
g10       TO_SRV02-V3_[DRAC]
g11       TO_SRV03-V3_[DRAC]
g12       TO_SRV04-V3_[DRAC]
g13       TO_SRV12-V6_[DRAC]
g14       TO_SRV01-V4_[DRAC]
g15       TO_SRV02-V4_[DRAC]
g16       TO_SRV09-ESS_[DRAC]
g17       TO_SRV01-V2_[DRAC]
g18       TO_SRV02-V2_[DRAC]
g19       TO_SRV03-V2_[DRAC]
g20       TO_SRV04-V2_[DRAC]
g21       TO_SAN-SAS-2_[C0]
g22       TO_SAN-SAS-2_[C1]
g23       TO_SRV09-V6_[DRAC]
g24       TO_SRV10-V6_[DRAC]
g25       TO_SRV04-VSAN_[DRAC]
g26       TO_SRV07-LC_[DRAC]
g27       TO_SRV03-VSAN_[DRAC]
g28       TO_SAN-[CTRL-0]
g29       TO_SAN-[CTRL-1]
g30       TO_SRV10-VSAN_[DRAC]
g31       TO_SRV09-VSAN_[DRAC]
g32       TO_SRV02-VSAN_[DRAC]
g33       TO_SAN2-[CTRL-0]
g34       TO_SAN2-[CTRL-1]
g35       TO_SAN3[CTRL-0]
g36       TO_SAN3[CTRL-1]
g37       TO_SRV01-VSAN_[DRAC]
g38       TO_SRV01-V3_[DRAC]
g39       TO_SAN4[CTRL-0]
g40       TO_SAN4[CTRL-1]
g41       TO_SAN5[CTRL-0]
g42       TO_SAN5[CTRL-1]
g43       TO_UPLINK1_[1Gbit]
g44       TO_UPLINK2_[1Gbit]
g45       TO_SRV07-V2_[DRAC]
g46
g47
g48       ADMIN_[1Gbit]

Ch        Description
-------   -----------
ch1
ch2
ch3
ch4
ch5
ch6
ch7
ch8

```

**Help:** execute the command "show interfaces description"

**Prompt:**
- dell_powerconnect>
- dell_powerconnect#

### show bridge address table

**Output:**
```
Aging time is 300 sec

  Vlan        Mac Address       Port     Type
 -------- --------------------- ------ ----------
   5       00:08:e3:ff:fc:28    g48    dynamic
   5       00:13:c6:05:d3:1f    g48    dynamic
   5       0c:f5:a4:cf:21:1f    g48    dynamic
   5       8c:60:4f:59:90:81    g44    dynamic
   5       8c:60:4f:59:98:01    g43    dynamic
   12      00:08:e3:ff:fc:28    g48    dynamic
   12      00:11:32:7c:0e:ba    g48    dynamic
  220      00:08:e3:ff:fc:28    g48    dynamic
  220      00:0a:f7:14:c0:92    g48    dynamic
  220      00:0a:f7:14:c3:80    g48    dynamic
  220      00:0a:f7:38:33:10    g48    dynamic
  220      00:0a:f7:6a:56:30    g48    dynamic
  220      4c:d9:8f:00:31:7a    g19    dynamic
  220      4c:d9:8f:00:33:24    g17    dynamic
  220      4c:d9:8f:09:c9:10    g31    dynamic
  220      4c:d9:8f:09:c9:16    g30    dynamic
  220      4c:d9:8f:09:c9:40    g37    dynamic
  220      4c:d9:8f:9f:04:3c    g48    dynamic
  220      5c:f9:dd:fd:8b:72    g12    dynamic
  220      5c:f9:dd:fd:8c:28    g38    dynamic
  220      5c:f9:dd:fd:90:bc    g11    dynamic
  220      5c:f9:dd:fd:9a:da    g10    dynamic
  220      70:81:05:1d:e6:e2    g48    dynamic
  220      70:b5:e8:d5:de:d6    g13    dynamic
  220      70:b5:e8:d5:e2:fc     g2    dynamic
  220      70:b5:e8:d5:e6:d4     g1    dynamic

```

**Help:** execute the command "show bridge address table"

**Prompt:**
- dell_powerconnect>
- dell_powerconnect#

