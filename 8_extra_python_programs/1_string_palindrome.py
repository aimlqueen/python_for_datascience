#1.Write a python program to check a string is a palindrome
new_txt = input("Enter a string: ")
if new_txt == new_txt[::-1]:
    print(f'"{new_txt}" is a palindrome.')
else:
    print(f'"{new_txt}" is not a palindrome.')
