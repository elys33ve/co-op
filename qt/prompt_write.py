import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

class WriteText(QWidget):
    def __init__(self):
        super().__init__()

        # Create a label
        self.label = QLabel("Enter text:")

        # Create a line edit
        self.lineEdit = QLineEdit()

        # Create a button
        self.button = QPushButton("Write")

        # Connect the button to the writeText() method
        self.button.clicked.connect(self.writeText)

        # Layout the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.button)

        # Set the layout for the widget
        self.setLayout(layout)

    def writeText(self):
        # Get the text from the line edit
        text = self.lineEdit.text()

        # Write the text to the label
        self.label.setText(text)


if __name__ == "__main__":

    # Create application and widget
    app = QApplication([])
    widget = WriteText()
    widget.show()

    # Run the application
    sys.exit(app.exec_())
