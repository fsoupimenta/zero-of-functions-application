import math
from time import sleep

from store.store import store


class Method:
    def __init__(self, x, p, y, error, interval):
        self.value_a = 100
        self.value_b = 100
        self.error = error
        self.x = x
        self.density = p
        self.y = y
        self.interval = interval

        self.value_c = self.calculate_c()
        self.list_values_c = [self.value_c]
        self.list_values_image_c = [self.equation(self.value_c)]

        self.set_initial_interval()

    def main_function(self, lineEdit):
        while self.value_b - self.value_a > self.error:
            if self.equation(self.value_a) * self.equation(self.value_c) > 0:
                self.value_a = self.value_c
            else:
                self.value_b = self.value_c
            self.value_c = self.calculate_c()
            self.list_values_c.append(self.value_c)
            self.list_values_image_c.append(self.equation(self.value_c))

        store.values_t = self.list_values_c
        store.values_image_t = self.list_values_image_c
        lineEdit.setText(str(self.equation(self.value_c)))

    def set_initial_interval(self):
        self.value_a = self.interval
        self.value_b = self.interval * 2

        while self.equation(self.value_a) * self.equation(self.value_b) > 0:
            # sleep(0.2)
            self.value_a += self.interval
            self.value_b += self.interval

    def equation(self, t):
        return ((t / (self.density * 10)) * math.cosh((self.density * 10 * self.x) / t)) - self.y

    def calculate_c(self):
        return (self.value_a + self.value_b) / 2
