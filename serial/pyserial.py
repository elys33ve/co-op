import serial, time, io
from time import sleep

"""
script should look and act like normal ssh or minicom interface for most command things but 
i only tried really simple ones so far.
has an auto login feature but is set to allow manual login (and for auto login, it assumes user and pass are 'rdms')
"""

portname = '/dev/ttyUSB0'
ser = 0
###########################################################################

### connect and login
def connect(login=False):
    global ser
    ser = serial.Serial(portname, baudrate=115200, timeout=1)     # open serial port
    print("connected to", ser.name)
    
    # auto login
    auto_login(login)
    print()


### print output
def show_output():
    output = ser.read(10000).decode('utf-8', 'ignore')
    print(output)
    

### auto writes password and username to login 
def auto_login(login=False):
    username = "username\r\n"
    password = "password\r\n"

    # fail if more than three attempts
    for i in range(3):
        ser.write("\n\r".encode())          # write newline
        output = ser.read(10000).decode('utf-8', 'ignore')  # get output

        # prompts for login
        if " login:" in output:
            # auto on
            if login == True:
                ser.write(username.encode())      # write user
            # auto off
            else:
                usr = input("\nrdms login: ")
                ser.write(f"{usr}\r\n".encode())   
            output = ser.read(10000).decode('utf-8', 'ignore')  # get output     

            # prompts for password
            if "Password" in output:
                # auto on
                if login == True:
                    ser.write(password.encode())      # write pass
                # auto off
                else:
                    usr = input("Password: ")
                    ser.write(f"{usr}\r\n".encode())   
                output = ser.read(10000).decode('utf-8', 'ignore')  # get output
            break


### writes a command and shows output
def write_cmd(stuff, waitfor=2):
    ser.reset_input_buffer()
    ser.reset_output_buffer()

    ser.write(f"{stuff}\r".encode())

    output = ser.read(10000).decode('utf-8', 'ignore')
    output = output.replace("[rdms@rdms ~]$", "")[len(stuff):len(output)]
    #output = "\n[rdms@rdms ~]$ " + output
    print(output)
    


if __name__ == "__main__":
    connect(True)
    exit_list = ["exit", "exit()", "close", "quit"]
    
    cmds = ""
    while cmds not in exit_list:
        cmds = input("[rdms@rdms ~]$ ")
        write_cmd(cmds)
    
    ser.close()                 # close serial connection


