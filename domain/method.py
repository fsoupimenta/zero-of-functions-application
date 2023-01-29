def equation(x):
    return (x * x * x) - x - 2


def calculate_c(a, b):
    return (a + b) / 2


class Method:
    def __init__(self, x, y, error):
        self.value_a = x
        self.value_b = y
        self.error = error
        self.value_c = calculate_c(self.value_a, self.value_b)
        self.image_c = equation(self.value_c)

    def main_function(self, lineEdit):
        while self.image_c > self.error or self.image_c < -self.error:
            if self.image_c < 0:
                self.value_a = self.value_c
            else:
                self.value_b = self.value_c
            self.value_c = calculate_c(self.value_a, self.value_b)
            self.image_c = equation(self.value_c)
            lineEdit.setText(str(self.image_c))
