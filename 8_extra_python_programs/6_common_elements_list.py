#6.Write a python program to find the common elements between two lists
input_list1 = input("Enter the first list of elements separated by spaces: ")
list1 = input_list1.split()
input_list2 = input("Enter the second list of elements separated by spaces: ")
list2 = input_list2.split()
common_elements = []
for element in list1:
    if element in list2:
        common_elements.append(element)
if common_elements:
    print("Common elements:", ' '.join(common_elements))
else:
    print("No common elements found.")
