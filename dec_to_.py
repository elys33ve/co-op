dec, binary, hexidecimal = "", "", ""

# simple python script to take decimal input and convert to hex and binary

def dec_to_binary(n):
    global binary
    if n >= 1:
        dec_to_binary(n // 2)
        binary += str(n % 2)


def dec_to_hex(n):
    global hexidecimal
    hexidecimal = hex(int(n))


while dec != "fuck off":
    dec = input("")
    if dec.isnumeric():
        dec_to_binary(int(dec))
        dec_to_hex(int(dec))
        print(hexidecimal, '\t', binary)
