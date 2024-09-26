#Write a python program to find the largest element in a list
input_list = input("Enter numbers separated by spaces: ")
numbers = list(map(int, input_list.split()))
if numbers:
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    print(f"The largest element in the list is {largest}.")
else:
    print("The list is empty.")

