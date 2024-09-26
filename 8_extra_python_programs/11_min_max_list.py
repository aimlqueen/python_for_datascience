#11.Write a python program to find maximum and minimum elements in a list
input_list = input("Enter numbers separated by spaces: ")
numbers = list(map(float, input_list.split()))
if numbers:
    max_element = max(numbers)
    min_element = min(numbers)
    print(f"Maximum: {max_element}, Minimum: {min_element}")
else:
    print("The list is empty.")
