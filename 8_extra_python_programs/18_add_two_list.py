#18.Write a python program to adding two list elements together

input_list1 = input("Enter the first list of numbers separated by spaces: ")
input_list2 = input("Enter the second list of numbers separated by spaces: ")
list1 = list(map(int, input_list1.split()))
list2 = list(map(int, input_list2.split()))
added_list = [a + b for a, b in zip(list1, list2)]
print("Sum of the two lists:", added_list)
