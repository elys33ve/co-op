import sys, PyQt5


### ---------------------------------------------------------------------------------
### ---------------------------------------------------------------------------------
def push_button():
    from PyQt5.QtWidgets import QApplication, QPushButton
    app = QApplication(sys.argv)

    window = QPushButton("Push Button")
    window.show()

    app.exec()

### ---------------------------------------------------------------------------------
### ---------------------------------------------------------------------------------
# https://www.pythonguis.com/tutorials/pyqt-layouts/
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QWidget

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

### ---------------------------------------------------------------------------------
### ---------------------------------------------------------------------------------
def main_window():
    from PyQt5.QtWidgets import QApplication, QMainWindow
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.show()

    app.exec()

### ---------------------------------------------------------------------------------
### ---------------------------------------------------------------------------------
