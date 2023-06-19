pinout = """"
,--------------------------------.
| oooooooooooooooooooo J8   +======
| 1ooooooooooooooooooo  PoE |   Net
|  Wi                    1o +======
|  Fi  Pi Model 4B  V1.1 oo      |
|        ,----. +---+         +====
| |D|    |SoC | |RAM|         |USB3
| |S|    |    | |   |         +====
| |I|    `----' +---+            |
|                   |C|       +====
|                   |S|       |USB2
| pwr   |hd|   |hd| |I||A|    +====
`-| |---|m0|---|m1|----|V|-------'

Revision           : c03111
SoC                : BCM2711
RAM                : 4GB
Storage            : MicroSD
USB ports          : 4 (of which 2 USB3)
Ethernet ports     : 1 (1000Mbps max. speed)
Wi-fi              : True
Bluetooth          : True
Camera ports (CSI) : 1
Display ports (DSI): 1

J8:
   3V3  (1) (2)  5V    
 GPIO2  (3) (4)  5V    
 GPIO3  (5) (6)  GND   
 GPIO4  (7) (8)  GPIO14
   GND  (9) (10) GPIO15
GPIO17 (11) (12) GPIO18
GPIO27 (13) (14) GND   
GPIO22 (15) (16) GPIO23
   3V3 (17) (18) GPIO24
GPIO10 (19) (20) GND   
 GPIO9 (21) (22) GPIO25
GPIO11 (23) (24) GPIO8 
   GND (25) (26) GPIO7 
 GPIO0 (27) (28) GPIO1 
 GPIO5 (29) (30) GND   
 GPIO6 (31) (32) GPIO12
GPIO13 (33) (34) GND   
GPIO19 (35) (36) GPIO16
GPIO26 (37) (38) GPIO20
   GND (39) (40) GPIO21

POE:
TR01 (1) (2) TR00
TR03 (3) (4) TR02

For further information, please refer to https://pinout.xyz/
"""

p14 = "GPIO 5: level=0 fsel=0 func=INPUT pull=UP"
p15 = "GPIO 5: level=1 fsel=0 func=INPUT pull=UP"
p26 = "GPIO 5: level=0 fsel=0 func=OUTPUT pull=UP"
p2 = "GPIO 5: level=0 fsel=0 func=OUTPUT pull=UP"

def pininfo_str (x):
    if x == '14':
        return p14
    elif x == '15':
        return p15
    elif x == '26':
        return p26
    elif x == '2':
        return p2
    else: 
        return "GPIO 5: level=1 fsel=0 func=OUTPUT pull=UP"


def pin_onoff (x, y):   # 1/0
    global p14, p15, p26
    if x == '14':
        if y == 1:
            p14 = "GPIO 5: level=1 fsel=0 func=OUTPUT pull=UP"
        else:
            p14 = "GPIO 5: level=0 fsel=0 func=OUTPUT pull=UP"
    elif x == '15':
        if y == 1:
            p15 = "GPIO 5: level=1 fsel=0 func=OUTPUT pull=UP"
        else:
            p15 = "GPIO 5: level=0 fsel=0 func=OUTPUT pull=UP"
    elif x == '26':
        if y == 1:
            p26 = "GPIO 5: level=1 fsel=0 func=OUTPUT pull=UP"
        else:
            p26 = "GPIO 5: level=0 fsel=0 func=OUTPUT pull=UP"
    elif x == '2':
        if y == 1:
            p2 = "GPIO 5: level=1 fsel=0 func=OUTPUT pull=UP"
        else:
            p2 = "GPIO 5: level=0 fsel=0 func=OUTPUT pull=UP"
    else: 
        return "GPIO 5: level=1 fsel=0 func=OUTPUT pull=UP"

def pin_inout (x, y):   # 'ip'/'op'
    global p14, p15, p26
    if x == '14':
        if y == 'ip':
            p26 = "GPIO 5: level=1 fsel=0 func=INPUT pull=UP"
        else:
            p26 = "GPIO 5: level=1 fsel=0 func=OUTPUT pull=UP"
    elif x == '15':
        if y == 'ip':
            p26 = "GPIO 5: level=1 fsel=0 func=INPUT pull=UP"
        else:
            p26 = "GPIO 5: level=1 fsel=0 func=OUTPUT pull=UP"
    elif x == '26':
        if y == 'ip':
            p26 = "GPIO 5: level=1 fsel=0 func=INPUT pull=UP"
        else:
            p26 = "GPIO 5: level=1 fsel=0 func=OUTPUT pull=UP"
    elif x == '2':
        if y == 'ip':
            p2 = "GPIO 5: level=1 fsel=0 func=INPUT pull=UP"
        else:
            p2 = "GPIO 5: level=1 fsel=0 func=OUTPUT pull=UP"
    else: 
        return "GPIO 5: level=1 fsel=0 func=OUTPUT pull=UP"



