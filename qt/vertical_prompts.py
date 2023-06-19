import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit


class VerticalPrompts(QWidget):
    def __init__(self):
        super().__init__()

        # Create a layout for the grid
        self.layout = QFormLayout()

        # Add widgets to the layout
        for i in range(10):
            label = QLabel(str(i))
            lineEdit = QLineEdit()
            self.layout.addRow(label, lineEdit)

        # Set the layout for the QWidget object
        self.setLayout(self.layout)

    def show(self):
        super().show()

if __name__ == "__main__":

    # Create an application and grid widget
    app = QApplication([])
    grid = VerticalPrompts()
    grid.show()

    # Run the application
    sys.exit(app.exec_())
