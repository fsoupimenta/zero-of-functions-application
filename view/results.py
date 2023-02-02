from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QTableWidget, QLabel, QVBoxLayout


class Results(QDialog):

    def __init__(self, values_t, values_image_t):
        super().__init__()

        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        self.setWindowTitle("Results")

        self.values_t = values_t
        self.values_image_t = values_image_t

        self.tableWidget = QTableWidget()

        self.set_content_attributes()
        self.set_up_layout()

    def set_content_attributes(self):
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(2)

        self.tableWidget.verticalHeader().hide()

        self.tableWidget.setHorizontalHeaderLabels(["Tension Values", "F(T) Values"])

        label_list = [" Insert or +", " Delete or -", " Control + Left-Click", " Left-Click", " Left-Click",
                      " Left-Click"]

        for i, tensions in enumerate(self.values_t):
            label = QLabel(tensions)
            label.setStyleSheet("font-weight: bold")
            self.tableWidget.setCellWidget(i, 0, label)

        for i, image_tensions in enumerate(self.values_image_t):
            label = QLabel(image_tensions)
            label.setStyleSheet("font-weight: bold")
            self.tableWidget.setCellWidget(0, i, label)

        self.tableWidget.horizontalHeader().setDisabled(True)
        self.tableWidget.horizontalHeader().setStyleSheet("color: black; background-color: gray")
        self.tableWidget.setStyleSheet("background-color: #DCDCDC; color: black;")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.tableWidget.setMaximumHeight((self.tableWidget.rowHeight(0) * 7) - 5)
        self.tableWidget.setColumnWidth(0, 150)

    def set_up_layout(self):
        self.setMinimumSize(750, 250)

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)

        self.setLayout(layout)
