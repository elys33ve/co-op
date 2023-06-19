# this script is for controling the voltage output on raspberry pi pins
# use command "pinout" to get pin numbers 
"""
command line:
raspi-gpio get          //prints the state of all GPIO pins
raspi-gpio get X        //prints the state of GPIO pin X
raspi-gpio set X op     //sets GPIO pin X as an output
raspi-gpio set X dh     //sets GPIO pin X to drive high
raspi-gpio set X dl     //sets GPIO pin X to drive low
"""

from pigpio_test import *

#################################




if __name__ == "__main__":
    show_pinnum(2)          # ground, pin 2 
    set_pin(2, onoff=ON)
    sleep(2)
    set_pin(2, onoff=OFF)
