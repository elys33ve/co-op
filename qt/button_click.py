import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


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
        # BUTTON
        self.button = QPushButton("Push the Button.")

        self.button_checked = False     # toggle on/off
        self.num_presses = 0            # count presses
        self.button.setCheckable(True)

        self.button.clicked.connect(self.button_was_clicked)     # button was clicked
        self.button.setChecked(self.button_checked)
        self.setCentralWidget(self.button)

        # ----------------------------------------- 
    
    ### ============================= Button
    ### lock button
    def lock_button(self):
        self.button.setText("Stop.")
        self.button.setEnabled(False)
        self.setWindowTitle("Fuck You.")

    ### button click
    def button_was_clicked(self, checked):
        self.button_checked = checked
        self.num_presses += 1

        # toggle button
        if checked == True:
            print("How dare you.")
        else: 
            print("I cannot believe this.")

        # lock button
        if self.num_presses == 10:
            self.lock_button()


# run the things   
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
