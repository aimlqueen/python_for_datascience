# 7.Write a python program to remove duplicates from a list
input_list = input("Enter elements separated by spaces: ")
elements = input_list.split()
unique_elements = list(set(elements))
print("List after removing duplicates:", unique_elements)
