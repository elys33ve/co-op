import sys, random, PyQt5
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel

# keypad with keypad input


### ====================================================================================

### ====================================================================================
# Global Variables

# keypad layout
keypad = [["", "", "", "Freq", "7", "8", "9"],
          ["Esc", "<UP>", "*", "Mode", "4", "5", "6"],
          ["<Left>", "Enter", "<Right>", "Rate", "1", "2", "3"],
          ["Clr", "<Down>", "Select unit", "Menu", "0", ".", "+/-"]]

ehe = []

# window size
size_x, size_y = 500, 400

# (this is only here because i wanted to see how it would work
pipi = "3.141592653589793238462643383279502884197169399375105820"
def itspi():
    pp = ["ahshsj", "woiejfso", "siiienn", "diiiii", "pipi", 
          "sitis pi", "still pui", "omhg", "asjjs", "didii", 
          ":D", ":DD", "dosokesaj"]
    pwewe = "".join(ehe)
    pwowo = pwewe[0:len(pwewe)-1]
    if pwewe == "3.14": 
        return "pi its pi"
    elif pwewe == "3.141592": 
        return "whoaooa more pi"
    elif pwowo == pipi: 
        return "fck idk but jokes on u uwasted ur time"
    elif pwewe in pipi and "3.141592" in pwewe: 
        return pp[random.randint(0,len(pp)-1)]
    elif pwowo in pipi and "3.141592" in pwowo and pwewe not in pipi: 
        return ":("


### ====================================================================================
# Button class that keeps track of presses
class Button(QPushButton):
    def __init__(self, label):
        super().__init__(label)
        self.label = label
        self.checked = False        # toggle on/off
        self.presses = 0            # number of presses

    ### keep track of button presses
    def pressed(self):
        # incr presses
        self.presses += 1

        # toggle on/off
        if self.checked == False:
            self.checked = True
        else:
            self.checked = False

        # heh
        ehe.append(self.label)
        




### ====================================================================================
# subclass of QMainWindow
class Keypad(QMainWindow):
    def __init__(self):
        super(Keypad, self).__init__()

        # size and title
        self.setWindowTitle("Keypad Qt Test")
        self.setMinimumSize(QSize(size_x, size_y))

        # layout
        self.layout = QGridLayout()

        # write keypad (to press for tests)
        self.buttons = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        for i in range(len(keypad)):
            for j in range(len(keypad[i])):
                # unused key places
                if i == 0 and j < 3: 
                    pass
                # for keys on keypad
                else:
                    # create buttons
                    self.buttons[i][j] = Button(f"{keypad[i][j]}")
                    self.buttons[i][j].clicked.connect(self.buttons[i][j].pressed)     # button was clicked
                    self.buttons[i][j].clicked.connect(self.update_key)
                    self.layout.addWidget(self.buttons[i][j], i, j)
        
        self.keypad()   # keypad to show keypresses
        self.call_label()
        self.call_reset()

        # set things
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    ### --------------------------------------- functions
    
    ### create label
    def call_label(self, l="press keys above"):
        # label
        label = QLabel(l)
        self.layout.addWidget(label, 4, 0, 4, 3)

    ### create reset button
    def call_reset(self, l="reset"):
        # reset button
        reset_button = Button(l)
        reset_button.clicked.connect(self.reset)     # button was clicked
        self.layout.addWidget(reset_button, 4, 4, 4, 4)


    ### create keypad to show keypresses (not for click)
    def keypad(self):
        # set second keypad for show
        for i in range(len(keypad)):
            for j in range(len(keypad[i])):
                b = self.buttons[i][j]

                # unused key places
                if i == 0 and j < 3: 
                    pass
                # for keys on keypad
                else:
                    # presses > 1
                    if b.presses > 1:
                        button = QPushButton(f"{keypad[i][j]} ({b.presses})")
                        self.layout.addWidget(button, i+len(keypad)+2, j)
                    # presses <= 1
                    else:
                        button = QPushButton(f"{keypad[i][j]}")
                        self.layout.addWidget(button, i+len(keypad)+2, j)
                    
                    # disable if pressed
                    if b.presses > 0:
                        button.setDisabled(True)
                

    ### update key after keypress
    def update_key(self):
        self.keypad()

        if itspi() is not None: print(itspi())


    ### reset show keypad
    def reset(self):
        global ehe
        ehe = []
        # reset all presses to zero
        for i in range(len(keypad)):
            for j in range(len(keypad[i])):
                # unused key places
                if i == 0 and j < 3: 
                    pass
                # for keys on keypad
                else:
                    b = self.buttons[i][j]
                    b.presses = 0
        self.keypad()

### ---------------------------------------------------------------------------------
### ---------------------------------------------------------------------------------


if __name__ == "__main__":
    app, window = QApplication(sys.argv), Keypad()
    window.show()
    app.exec()
