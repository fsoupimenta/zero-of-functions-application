class Store:
    def __init__(self):
        self.values_t = []
        self.values_image_t = []
        self.values_a = []
        self.values_image_a = []
        self.values_b = []
        self.values_image_b = []

    def get_values_t(self):
        return self.values_t

    def get_values_a(self):
        return self.values_a

    def get_values_b(self):
        return self.values_b

    def get_values_image_t(self):
        return self.values_image_t

    def get_values_image_a(self):
        return self.values_image_a

    def get_values_image_b(self):
        return self.values_image_b


store = Store()
