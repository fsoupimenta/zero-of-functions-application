import math

from store.store import store


class Method:
    name = None

    def __init__(self):
        self.all = Method.__subclasses__()
        self.dict_name_method: {str: Method} = {}
        for method in self.all:
            self.dict_name_method[method.name] = method

    @staticmethod
    def calculate():
        pass

    @staticmethod
    def image_x(x):
        return math.log(x) + 2 - x


class BisectionMethod(Method):
    name = "Bisection method"

    @staticmethod
    def calculate():
        interval_avg = (store.value_a + store.value_b) / 2
        image_interval_avg = Method.image_x(interval_avg)
        error = 10**(-3)
        while image_interval_avg > error or image_interval_avg < -error:
            if image_interval_avg > 0:
                store.value_a = interval_avg
            else:
                store.value_b = interval_avg
            interval_avg = (store.value_a + store.value_b) / 2
            image_interval_avg = Method.image_x(interval_avg)
            print(image_interval_avg)
        print(interval_avg)


class SecantMethod(Method):
    name = "Secant method"

    @staticmethod
    def calculate():
        pass


class NewtonMethod(Method):
    name = "Newton method"

    @staticmethod
    def calculate():
        pass


method_ = Method()

method_name = method_.dict_name_method
