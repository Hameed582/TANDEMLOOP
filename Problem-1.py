class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == '+':
            return self.a + self.b
        elif self.operation == '-':
            return self.a - self.b
        elif self.operation == '*':
            return self.a * self.b
        elif self.operation == '/':
            if self.b == 0:
                return "Error: Division by zero"
            return self.a / self.b
        else:
            return "Error: Invalid operation"

a = float(input("Enter first number : "))
b = float(input("Enter second number : "))
operation = input("Enter operation : \n + for addition \n - for subtraction \n * for multiplication \n / for division \n")

calc = Calculator(a, b, operation)
result = calc.calculate()
print("Result is :", result)
