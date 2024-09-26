#14.Write a python program to iterate over a dictionary and perform operations on key:value pairs
dictionary = {'a': 1, 'b': 2, 'c': 3}
for key, value in dictionary.items():
    print(f"Key: {key}, Value: {value}, Double Value: {value * 2}")
