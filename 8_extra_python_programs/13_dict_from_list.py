#13.Write a python program to create a dictionary from a  list of key:value pairs

input_pairs = input("Enter key:value pairs separated by spaces ")
pairs = input_pairs.split()
dictionary = {}
for pair in pairs:
    key, value = pair.split(':')
    dictionary[key] = value
print("Created dictionary:", dictionary)
