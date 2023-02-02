import math
from time import sleep


def equation(t, x, y, p):
    return ((t / (p * 10)) * math.cosh((p * 10 * x) / t)) - y


def calculate_c(a, b):
    return (a + b) / 2


class Method:
    def __init__(self, x, p, y, error):
        self.value_a = 100
        self.value_b = 100
        self.error = error
        self.x = x
        self.density = p
        self.y = y
        self.value_c = calculate_c(self.value_a, self.value_b)
        self.image_a = equation(self.value_a, self.x, self.y, self.density)
        self.image_b = equation(self.value_b, self.x, self.y, self.density)
        self.image_c = equation(self.value_c, self.x, self.y, self.density)

        self.set_initial_interval()

    def main_function(self, lineEdit):
        print(self.value_a, self.value_b)
        while self.value_b - self.value_a > self.error:
            print("C:", self.value_c)
            if self.image_a * self.image_c > 0:
                self.value_a = self.value_c
            else:
                self.value_b = self.value_c
            self.value_c = calculate_c(self.value_a, self.value_b)
            self.image_c = equation(self.value_c, self.x, self.y, self.density)
            lineEdit.setText(str(self.image_c))

    def set_initial_interval(self):
        distance = 100
        self.value_a = distance
        self.value_b = distance * 2

        while self.image_a * self.image_b > 0:
            print(self.value_a, self.value_b)
            print(self.image_a, self.image_b)
            sleep(1)
            self.value_a += distance
            self.value_b += distance
            self.image_a = equation(self.value_a, self.x, self.y, self.density)
            self.image_b = equation(self.value_b, self.x, self.y, self.density)
