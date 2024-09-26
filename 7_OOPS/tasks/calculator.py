#write a python program to create a calculator using class

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b

def calculator_program():
    calc = Calculator()

    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                result = calc.add(num1, num2)
                print(f"Result: {result}")
            elif choice == '2':
                result = calc.subtract(num1, num2)
                print(f"Result: {result}")
            elif choice == '3':
                result = calc.multiply(num1, num2)
                print(f"Result: {result}")
            elif choice == '4':
                result = calc.divide(num1, num2)
                print(f"Result: {result}")
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

calculator_program()

