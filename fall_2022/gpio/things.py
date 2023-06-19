# things to use
# - ip addresses of the different things
# - commands
# - notes

from time import sleep
import paramiko, os

############################################ --- files
ifconfigtxt = "ifconfig.txt"
results = "test_results.txt"

HOST = 'host ip'
############################################ --- ip addresses

"""
* ip address variables for things so i could be lazy *

tmoip2
powerstrip2
backuppi3
pi4gpio
"""

############################################ --- ssh
num_tests = 3       # number of tests to do
seconds = 60        # number of seconds tests take
outlet = 0          # number of powerstrip outlet
mbps = 400          # mb per sec

port = 5201         # 5201 is defult for iperf3

# tmoip boards
tmoip_ssh = [tmoip2, user, passw]       # ip, user, pass
# powerstrip
power_ssh = [powerstrip2, user, passw]
# backup pi
backuppi = [backuppi3, user, passw]
# gpio pi
gpio_ssh = [pi4gpio, user, passw]

############################################ --- functions/classes

class SSH:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password


    def print_self (self):
        print(f"host: {self.host}\t{type(self.host)}")
        print(f"username: {self.username}\t{type(self.username)}")
        print(f"password: {self.password}\t{type(self.password)}")


        ### ssh
    def ssh (self, command):
        host = self.host
        username = self.username
        password = self.password

        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        _stdin, _stdout,_stderr = client.exec_command(command)
                      
        output = _stdout.read().decode()
        client.close()

        return output


############################################ --- temp test strings

pi = SSH(gpio_ssh[0], gpio_ssh[1], gpio_ssh[2])

#pinout = pi.ssh("pinout")

def pininfo (pin):
   pinfo = pi.ssh(f"raspi-gpio get {pin}")
   return pinfo


##########################

# rsync -a [source path] [user]@[ip]:[destination path]
pinout = """
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


tpininfo = "level=0 func=I"





