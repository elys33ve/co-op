import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class Keypad(QWidget):

    def __init__(self):
        super().__init__()

        # Create a layout for the keypad
        self.layout = QGridLayout()

        # Add the buttons to the layout
        for i in range(10):
            button = QPushButton(str(i))
            self.layout.addWidget(button, i // 3, i % 3)

        # Set the layout for the QWidget object
        self.setLayout(self.layout)

    def show(self):
        super().show()

if __name__ == "__main__":

    # Create an application
    app = QApplication([])

    # Create a keypad widget
    keypad = Keypad()

    # Show the keypad widget
    keypad.show()

    # Run the application
    sys.exit(app.exec_())
