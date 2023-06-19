# convert str to hex
""" quick python script to run from terminal that takes str input
    and converts it to hex values of each character in the format for
    this lab
"""


test = False        # true = print to screen, false = write to file

### string to hex
def str_to_hex(pr=False):
    string = input("hex: ")

    string = " ".join("{:02x}".format(ord(c)) for c in string)
    string = string.replace("0a", "") + ' 00\n'
    
    print(string)


### get hex of str
def get_hex():
    asciival = ""
    x = input("str: ")

    # get ascii
    for i in x:
        asciival += f"{ord(i)} "
    asciival = asciival[:-1]

    # get hex
    hexval = " ".join("{:02x}".format(ord(c)) for c in x)


    # outputs
    a = f"({asciival})"             # ascii value
    h = f"{hexval}"                 # hex value

    if len(asciival) > 25:  # format a bit
        a += '\n'
    print(a + "      " + h)





### get ascii letters from hex values 
def get_letter(string):
    #string = input("hex: ")
    dec = []
    
    # convert to decimal
    for i in range(0, len(string), 3):
        b = int('0x' + string[i:i+2], 16)
        dec.append(b)

    # print dec ints
    dec_strs = map(str, dec)
    print("dec:", " ".join(dec_strs))

    # get ascii values
    for i in range(len(dec)):
        dec[i] = chr(dec[i])

    # print ascii vals
    print("ascii: ", " ".join(dec))




if __name__ == "__main__":
    inpt = ""
    while True:
        inpt = input("hex: ")
        if inpt == "stop this shit":
            break
        get_letter(inpt)