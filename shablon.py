class Operation:  # Абстрактный класс
    def perform_operation(self, a, b):
        pass

class Addition(Operation):  # Классы наследники
    def perform_operation(self, a, b):
        return a + b

class Multiplication(Operation):
    def perform_operation(self, a, b):
        return a * b

class Calculator:
    def init(self, operation):
        self.operation = operation

    def calculate(self, a, b):
        return self.operation.perform_operation(a, b)


addition = Addition()
multiplication = Multiplication()

calculator = Calculator(addition)
result = calculator.calculate(4, 5)
print(result)

calculator = Calculator(multiplication)
result = calculator.calculate(4, 5)
print(result)