#Take a string as a input and count the vowels

s=input("Enter a string:")
vowels="aeiouAEIOU"
count=0
for i in s:
    if i in vowels:
        count+=1
print("No of vowels:",count)