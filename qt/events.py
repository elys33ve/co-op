import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

### ---------------------------------------------------------------------------------
# https://www.pythonguis.com/tutorials/pyqt-signals-slots-events/

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("I see the mouse.")
        self.setMinimumSize(QSize(300, 200))

        # -- label for events
        self.label = QLabel("click here")
        self.setCentralWidget(self.label)

    ### ============================= Mouse Events
    def mouseMoveEvent(self, e):
        self.label.setText("the mouse is moving")

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("left click press")
        elif e.button() == Qt.MiddleButton:
            self.label.setText("middle click press")
        elif e.button() == Qt.RightButton:
            self.label.setText("right click press")

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("left click release")
        elif e.button() == Qt.MiddleButton:
            self.label.setText("middle click release")
        elif e.button() == Qt.RightButton:
            self.label.setText("right click release")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("left double click")
        elif e.button() == Qt.MiddleButton:
            self.label.setText("middle double click")
        elif e.button() == Qt.RightButton:
            self.label.setText("right double click")

# run the thing
app, window = QApplication(sys.argv), MainWindow()
window.show()
app.exec()