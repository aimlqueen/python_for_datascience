#12.Write a python program to filter elements from a list based on a condition
input_list = input("Enter numbers separated by spaces: ")
numbers = list(map(int, input_list.split()))
filtered_numbers = [num for num in numbers if num % 2 == 0]

print("Filtered elements (even numbers):", filtered_numbers)
