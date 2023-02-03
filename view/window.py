from PyQt5.QtWidgets import *

from domain.method import Method
from view.results import Results


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bisection Method")

        self.density_edit = QLineEdit()
        self.x_edit = QLineEdit()
        self.y_edit = QLineEdit()
        self.error_edit = QLineEdit()
        self.interval_edit = QLineEdit()
        self.response_value = QLineEdit()
        self.response_value.setDisabled(True)

        self.start_button = QPushButton("Start")
        self.results_button = QPushButton("Show Results")

        self.results = None

        self.start_button.clicked.connect(self.function)
        self.results_button.clicked.connect(self.show_results)

        layout = QGridLayout()
        layout.addWidget(QLabel("Tension approximately: "), 0, 0)
        layout.addWidget(self.response_value, 0, 1)
        layout.addWidget(QLabel("Insert a density value"), 1, 0)
        layout.addWidget(self.density_edit, 1, 1)
        layout.addWidget(QLabel("Insert a x value"), 2, 0)
        layout.addWidget(self.x_edit, 2, 1)
        layout.addWidget(QLabel("Insert a y value"), 3, 0)
        layout.addWidget(self.y_edit, 3, 1)
        layout.addWidget(QLabel("Insert an error value"), 4, 0)
        layout.addWidget(self.error_edit, 4, 1)
        layout.addWidget(QLabel("Insert an interval"), 5, 0)
        layout.addWidget(self.interval_edit, 5, 1)
        layout.addWidget(self.start_button, 6, 0)
        layout.addWidget(self.results_button, 6, 1)

        self.setLayout(layout)

    def function(self):
        method = Method(float(self.x_edit.text()), float(self.density_edit.text()), float(self.y_edit.text()),
                        float(self.error_edit.text()), float(self.interval_edit.text()))
        method.main_function(self.response_value)

    def show_results(self):
        self.results = Results()
        self.results.show()
