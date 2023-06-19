# this script is for controling the voltage output on raspberry pi pins

# pi gpio in python -- https://www.ics.com/blog/control-raspberry-pi-gpio-pins-python#:~:text=Raspberry%2Dgpio%2Dpython%20or%20RPi,has%20documentation%20including%20example%20programs
# raspberry pi pinout -- https://www.elektronik-kompendium.de/sites/raspberry-pi/bilder/raspberry-pi-gpio.png
# gpiozero documentation -- https://gpiozero.readthedocs.io/en/stable/
# pi config and setup video -- https://www.youtube.com/watch?v=wf1SdgoZEJY
# pi inputs in python -- https://raspi.tv/2013/rpi-gpio-basics-6-using-inputs-and-outputs-together-with-rpi-gpio-pull-ups-and-pull-downs

# raspberry pi 3: user= pi, pass= pipi3, ip= 192.168.100.43
# use command "pinout" to get pin numbers 

"""
command line:
raspi-gpio get          //prints the state of all GPIO pins
raspi-gpio get X        //prints the state of GPIO pin X
raspi-gpio set X op     //sets GPIO pin X as an output
raspi-gpio set X dh     //sets GPIO pin X to drive high
raspi-gpio set X dl     //sets GPIO pin X to drive low
"""

from time import sleep
import paramiko


#################################

host = 'host ip'
user = 'poop'
password = 'password'

#################################

ON = 'dh'
OFF = 'dl'

OUTPUT = 'op'
INPUT = 'ip'

#################################

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



pigpio = SSH(host, user, password)

###########################################################

def show_pinout ():                         # print pinout for board
    print(pigpio.ssh("pinout"))


def show_pinstate ():                       # print state for all pins
    print(pigpio.ssh("raspi-gpio get"))


def show_pinnum (pin):                      # print info for pin
    print(pigpio.ssh(f"raspi-gpio get {pin}"))


def get_pininfo (pin):                                  # get level, fsel, and function of pin
    pininfo = pigpio.ssh(f"raspi-gpio get {pin}")
    lvl = pininfo[pininfo.index('level=') + 6]
    fsel = pininfo[pininfo.index('fsel=') + 5]
    func = pininfo[pininfo.index('func=') + 5]

    if lvl == '0':          # for input and output
        lvl = 'dl'
    elif lvl == '1':
        lvl = 'dh'

    if func == 'O':
        func = OUTPUT
    elif func == 'I':
        func = INPUT

    return [lvl, fsel, func]

    

def set_pin (pin, inout=0, onoff=0):            # change function or lvl of pin

    if inout == INPUT or inout == OUTPUT:
        pigpio.ssh(f"raspi-gpio set {pin} {inout}")
    
    if get_pininfo(pin)[2] == OUTPUT:
        if onoff == ON or onoff == OFF:
            pigpio.ssh(f"raspi-gpio set {pin} {onoff}")





