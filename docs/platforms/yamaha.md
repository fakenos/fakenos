# yamaha


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
- yamaha>

### console lines infinity

**Output:**
```
True
```

**Help:** set the terminal width to maximum

**Prompt:**
- yamaha>
- yamaha#

### show environment

**Output:**
```
RTX1200 BootROM Ver.1.01
RTX1200 Rev.10.01.71 (Thu Sep 29 15:08:40 2016)
  main:  RTX1200 ver=c0 serial=D12345678 MAC-Address=00:a0:de:aa:bb:11 MAC-Addr
 ess=00:a0:de:aa:bb:22 MAC-Address=00:a0:de:aa:bb:33
CPU:   1%(5sec)   2%(1min)   3%(5min)    Memory: 24% used
Packet-buffer:   0%(small)   0%(middle)   5%(large)   0%(huge) used
Firmware: exec1  Config. file: config1
Default firmware: exec0  Default config. file: config0
Boot time: 2021/01/24 12:32:36 +09:00
Current time: 2021/01/30 09:44:53 +09:00
Elapsed time from boot: 5days 21:12:17
Security Class: 1, FORGET: ON, TELNET: OFF
Inside Temperature(C.): 36
```

**Help:** execute the command "show environment"

**Prompt:**
- yamaha>
- yamaha#

### show ip route

**Output:**
```
Destination         Gateway          Interface       Kind  Additional Info.
default             -                    PP[01]    static  
10.0.0.0/8          192.168.1.254          LAN2    static  k(1)
10.0.0.0/8          192.168.1.253          LAN2    static  w(0)
10.1.0.0/24         192.168.1.253          LAN2      OSPF     cost=2 
10.2.0.0/24         192.168.1.252          LAN2      OSPF     cost=2 
203.0.113.2/32      -                    PP[01]  implicit  
169.254.1.1/30      -                 TUNNEL[1]  implicit  
192.168.1.0/24      192.168.1.8            LAN2  implicit  
192.168.100.0/24    192.168.100.1          LAN1  implicit  
203.0.113.1/32       -                    PP[01] temporary 
```

**Help:** execute the command "show ip route"

**Prompt:**
- yamaha>
- yamaha#

