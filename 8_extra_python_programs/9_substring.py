#Write a python program to check if a string contains a specific sub-string
input_string = input("Enter a string: ")
substring = input("Enter the substring to search for: ")
if substring in input_string:
    print(f"The substring '{substring}' is found in the string.")
else:
    print(f"The substring '{substring}' is not found in the string.")
