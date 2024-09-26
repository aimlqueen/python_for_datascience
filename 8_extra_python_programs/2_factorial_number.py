#Write a python program to find the factorial of a number
number = int(input("Enter a Number: "))
factorial = 1
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial of {number} is {factorial}.")
