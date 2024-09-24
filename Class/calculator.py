class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ZeroDivisionError("Ділення на нуль!")

    def power(self, a, b):
        return a ** b

    def sqrt(self, a):
        if a >= 0:
            return a ** 0.5
        else:
            raise ValueError("Неможливо взяти корінь з від'ємного числа")

    def mod(self, a, b):
        return a % b
