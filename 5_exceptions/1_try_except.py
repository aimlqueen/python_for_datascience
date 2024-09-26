a=[2,8,10]
try:
    print(a[2])
    print(a[22])#IndexError: list index out of range
except:
    print("IndexError: list index out of range")
