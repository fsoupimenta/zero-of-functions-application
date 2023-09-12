from domain.method import method_name
from store.store import store
from view.main_window import MainWindow


class Controller:
    def __init__(self):
        self.main_window = MainWindow()

        self.method = None

        self.connect_events()

    def connect_events(self):
        self.main_window.bisection_button.clicked.connect(self.update_method_choice)

    def show_main_window(self):
        self.main_window.show()

    def update_method_choice(self):
        store.equation = self.main_window.equation.text()
        store.value_a = int(self.main_window.value_a.text())
        store.value_b = int(self.main_window.value_b.text())
        method_name['Newton method'].calculate()
