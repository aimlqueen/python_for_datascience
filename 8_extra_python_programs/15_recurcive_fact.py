#15.Write a python program to implement a recursive function for calculating the factorial of a number
number = int(input("Enter a non-negative integer: "))
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
print(f"The factorial of {number} is {factorial(number)}.")
