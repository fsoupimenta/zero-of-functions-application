from PyQt5 import QtCore
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bisection Method")
        self.setFixedSize(750, 500)
