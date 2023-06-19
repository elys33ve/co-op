from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
  

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
  
        # title
        self.setWindowTitle("titiititle")
  
        # set geometry
        self.setGeometry(100, 100, 600, 400)
  
        # vutton
        self.make_button()
  
        # show all the widgets
        self.show()
  

    def make_button(self):
        button = QPushButton("CLICK", self)
        button.setGeometry(200, 150, 100, 40)       # set geometry
        button.clicked.connect(self.when_pressed)
  
    def when_pressed(self):
        print("asdfasdf")
  

#------------------------------------------------------
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
