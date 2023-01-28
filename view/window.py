from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bisection Method")
        self.setFixedSize(500, 250)

        self.density_edit = QLineEdit()
        self.x_edit = QLineEdit()
        self.y_edit = QLineEdit()
        self.error_edit = QLineEdit()

        self.start_button = QPushButton("Start")

        self.density_edit.setMaximumSize(100, 50)
        self.x_edit.setMaximumSize(100, 50)
        self.y_edit.setMaximumSize(100, 50)
        self.error_edit.setMaximumSize(100, 50)

        self.start_button.clicked.connect(self.function)

        layout = QGridLayout()
        layout.addWidget(QLabel("Insert a density value"), 0, 0)
        layout.addWidget(self.density_edit, 0, 1)
        layout.addWidget(QLabel("Insert a x value"), 1, 0)
        layout.addWidget(self.x_edit, 1, 1)
        layout.addWidget(QLabel("Insert a y value"), 2, 0)
        layout.addWidget(self.y_edit, 2, 1)
        layout.addWidget(QLabel("Insert an error value"), 3, 0)
        layout.addWidget(self.error_edit, 3, 1)
        layout.addWidget(self.start_button, 4, 1)

        print(self.density_edit.text())

        self.setLayout(layout)

    def function(self):
        print(self.density_edit.text())
        print(self.x_edit.text())
        print(self.y_edit.text())
        print(self.error_edit.text())
