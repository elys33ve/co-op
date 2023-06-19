import sys, PyQt5
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QCheckBox, QLabel, QLineEdit

### ---------------------------------------------------------------------------------
# keypad
keypad = [["", "", "", "Freq", "7", "8", "9"],
          ["Esc", "<UP>", "*", "Mode", "4", "5", "6"],
          ["<Left>", "Enter", "<Right>", "Rate", "1", "2", "3"],
          ["Clr", "<Down>", "Select unit", "Menu", "0", ".", "+/-"]]

keypresses = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

### find input in list
def find_input(x):
    x = x.strip().replace("<", "").replace(">", "").capitalize()
    for i in range(4):
        for j in range(len(keypad[i])):
            if x in keypad[i][j]:
                return i, j
    return -1, -1
### ---------------------------------------------------------------------------------

# keypad with txt input

# Subclass QMainWindow
class Keypad(QMainWindow):
    def __init__(self):
        super(Keypad, self).__init__()
        # size and title
        self.setWindowTitle("Keypad Qt (attempt)")
        self.setMinimumSize(QSize(500, 400))

        # layout
        self.layout = QGridLayout()

        # write keypad
        self.keypad()

        # Create a line edit and submit button
        self.label = QLabel("")
        self.lineEdit = QLineEdit()
        self.button = QPushButton("keypress")

        # Connect the button to the update_key()
        self.button.clicked.connect(self.update_key)

        # Layout the widgets
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.button)

        # set things
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    ### create keypad
    def keypad(self):
        for i in range(4):
            for j in range(7):
                button = QPushButton(f"{keypad[i-1][j-1]}")
                check = QCheckBox(f"{keypad[i-1][j-1]}")
                self.layout.addWidget(button, i, j)


    ### update key after keypress
    def update_key(self):
        text = self.lineEdit.text()
        i, j = find_input(text)

        # invalid input
        if i == -1 and j == -1:
            return
        
        # incr keypress for key
        keypresses[i][j] += 1
        
        # disable button (1 press)
        if keypresses[i][j] == 1:
            button = QPushButton(f"{keypad[i][j]}")
            button.setDisabled(True)
            self.layout.addWidget(button, i+1, j+1)
        # disable and change lable (1 < presses)
        else:
            button = QPushButton(f"{keypad[i][j]} ({keypresses[i][j]})")
            button.setDisabled(True)
            self.layout.addWidget(button, i+1, j+1)


if __name__ == "__main__":
    app, window = QApplication(sys.argv), Keypad()
    window.show()
    app.exec()