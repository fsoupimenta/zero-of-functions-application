class Store:
    def __inti__(self):
        self.values_t = []
        self.values_image_t = []

    def get_values_t(self):
        return self.values_t

    def get_values_image_t(self):
        return self.values_image_t


store = Store()
