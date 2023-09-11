from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtGui


class MainWindow(QWizardPage):
    def __init__(self):
        super().__init__()

        self.equation = QLineEdit()
        self.equation_validation = QLabel()
        self.bisection_button = QPushButton()
        self.secant_button = QPushButton()
        self.newton_button = QPushButton()

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.equation.setPlaceholderText("Insert your equation here...")
        self.equation.setFont(QFont("Montserrat", 12))
        self.equation.setMaximumHeight(30)

        self.bisection_button.setText("Bisection method")
        self.bisection_button.setMinimumHeight(50)
        self.bisection_button.setMinimumWidth(50)
        self.bisection_button.setCheckable(True)

        self.secant_button.setText("Secant method")
        self.secant_button.setMinimumHeight(50)
        self.secant_button.setMinimumWidth(50)
        self.secant_button.setCheckable(True)

        self.newton_button.setText("Newton method")
        self.newton_button.setMinimumHeight(50)
        self.newton_button.setMinimumWidth(50)
        self.newton_button.setCheckable(True)

    def set_up_layout(self):
        self.setTitle("Zero of functions application")

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.equation)
        main_layout.addWidget(self.equation_validation)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.bisection_button)
        button_layout.addWidget(self.secant_button)
        button_layout.addWidget(self.newton_button)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def set_label_validation_equation(self, error_message):
        if len(error_message) == 0:
            self.equation_validation.setText("Valid equation")
            self.equation_validation.setFont(QtGui.QFont("Arial", 8))
            self.equation_validation.setStyleSheet("color: green")
        else:
            self.equation_validation.setText("Invalid Equation: " + str(error_message))
            self.equation_validation.setFont(QtGui.QFont("Arial", 8))
            self.equation_validation.setStyleSheet("color: red")
