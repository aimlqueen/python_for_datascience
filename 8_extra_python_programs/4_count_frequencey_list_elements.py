#Write a python program to count the frequency of each element in a list
input_list = input("Enter elements separated by spaces: ")
elements = input_list.split()
frequency = {}
for element in elements:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1
for element, count in frequency.items():
    print(f"'{element}' appears {count} time(s).")
