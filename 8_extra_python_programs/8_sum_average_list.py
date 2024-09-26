#8.Write a python program to find the sum and average of elements in a list
input_list = input("Enter numbers separated by spaces: ")
numbers = list(map(float, input_list.split()))
total = sum(numbers)
average = total / len(numbers) if numbers else 0
print(f"Sum: {total}, Average: {average}")
