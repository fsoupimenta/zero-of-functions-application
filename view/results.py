from time import sleep

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QTableWidget, QLabel, QVBoxLayout

from store.store import store


class Results(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Results")

        self.values_a = store.get_values_a()
        self.values_image_a = store.get_values_image_a()
        self.values_b = store.get_values_b()
        self.values_image_b = store.get_values_image_b()
        self.values_t = store.get_values_t()
        self.values_image_t = store.get_values_image_t()

        self.tableWidget = QTableWidget()

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.tableWidget.setRowCount(len(self.values_t))
        self.tableWidget.setColumnCount(6)

        self.tableWidget.setHorizontalHeaderLabels(["A Values", "F(A) Values", "B Values", "F(B) Values",
                                                    "Tension Values", "F(T) Values"])

        for i, tensions in enumerate(self.values_a):
            label = QLabel(str(tensions))
            label.setStyleSheet("font-weight: bold")
            self.tableWidget.setCellWidget(i, 0, label)

        for i, tensions in enumerate(self.values_image_a):
            label = QLabel(str(tensions))
            label.setStyleSheet("font-weight: bold")
            self.tableWidget.setCellWidget(i, 1, label)

        for i, tensions in enumerate(self.values_b):
            label = QLabel(str(tensions))
            label.setStyleSheet("font-weight: bold")
            self.tableWidget.setCellWidget(i, 2, label)

        for i, tensions in enumerate(self.values_image_b):
            label = QLabel(str(tensions))
            label.setStyleSheet("font-weight: bold")
            self.tableWidget.setCellWidget(i, 3, label)

        for i, tensions in enumerate(self.values_t):
            label = QLabel(str(tensions))
            label.setStyleSheet("font-weight: bold")
            self.tableWidget.setCellWidget(i, 4, label)

        for i, image_tensions in enumerate(self.values_image_t):
            label = QLabel(str(image_tensions))
            label.setStyleSheet("font-weight: bold")
            self.tableWidget.setCellWidget(i, 5, label)

        self.tableWidget.horizontalHeader().setDisabled(True)
        self.tableWidget.horizontalHeader().setStyleSheet("color: black; background-color: gray")
        self.tableWidget.setStyleSheet("background-color: #DCDCDC; color: black;")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.tableWidget.setMaximumHeight((self.tableWidget.rowHeight(0) * len(self.values_image_t)) - 5)
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 150)

    def set_up_layout(self):
        self.setMinimumSize(1000, 500)

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)

        self.setLayout(layout)
