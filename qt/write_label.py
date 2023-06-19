import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget


# https://www.pythonguis.com/tutorials/pyqt-signals-slots-events/

# subclass QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window Title")

        # ----------------------------------------- 
        # WINDOW SIZE
        #self.setFixedSize(QSize(400, 300))         # will not resize
        #self.setMaximumSize(QSize(600, 900))
        self.setMinimumSize(QSize(300, 200))

        # ----------------------------------------- 
        # LABEL
        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # ----------------------------------------- 

# run the things   
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

