import math
from time import sleep

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


class BisectionMethod(Method):
    name = "Bisection method"

    @staticmethod
    def calculate():
        print('Hello')


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
