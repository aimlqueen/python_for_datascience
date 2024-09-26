file=open("demo.txt","r")
#read from file
print(file.read()) #read all contert
file.close()
print("-"*36)

file=open("demo.txt","r")
print(file.read(3))#read n char
file.close()
print("-"*36)

file=open("demo.txt","r")
print(file.readline())#read single line
file.close()
print("-"*36)

file=open("demo.txt","r")
print(file.readlines())#read list of all lines
file.close()
print("-"*36)
