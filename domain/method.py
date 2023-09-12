import math
import sympy as sp

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
        value_c = SecantMethod.get_secant(store.value_a, store.value_b)
        image_value_c = Method.image_x(value_c)
        error = 10**(-3)
        while image_value_c > error or image_value_c < -error:
            if image_value_c < 0:
                store.value_a = value_c
            else:
                store.value_b = value_c
            value_c = SecantMethod.get_secant(store.value_a, store.value_b)
            image_value_c = Method.image_x(value_c)
            print(image_value_c)
        print(value_c)

    @staticmethod
    def get_secant(value_a, value_b):
        return (value_a * Method.image_x(value_b) - value_b * Method.image_x(value_a)) / \
            (Method.image_x(value_b) - Method.image_x(value_a))


class NewtonMethod(Method):
    name = "Newton method"

    @staticmethod
    def calculate():
        x = sp.symbols('x')
        function = x**3 - 7*x**2 + sp.exp(2*x) - 40 - x
        derivative_function = sp.diff(function, x)
        image_value_c = sp.N(function.subs(x, store.value_a))
        derivative_value_c = sp.N(derivative_function.subs(x, store.value_a))
        value_c = store.value_a - image_value_c / derivative_value_c
        error = 10**(-3)
        while image_value_c > error or image_value_c < -error:
            image_value_c = sp.N(function.subs(x, value_c))
            derivative_value_c = sp.N(derivative_function.subs(x, value_c))
            value_c = value_c - image_value_c / derivative_value_c
            print(image_value_c)
        print(value_c)


method_ = Method()

method_name = method_.dict_name_method
