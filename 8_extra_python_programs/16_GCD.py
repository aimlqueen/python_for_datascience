#Write a python program to implement a function for finding the GCD(Greatest common divisor) of two numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
while b:
    a, b = b, a % b

print(f"The GCD is {a}.")
