from view.main_window import MainWindow


class Controller:
    def __init__(self):
        self.main_window = MainWindow()

        self.connect_events()

    def connect_events(self):
        pass

    def show_main_window(self):
        self.main_window.show()
