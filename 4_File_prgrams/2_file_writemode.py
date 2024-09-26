file=open("demo.txt","w")
file.write("Cool dear")
file.close()

file=open("demo.txt","r")
#read from file
print(file.read())
file.close()


file=open("demo.txt","w")
list=['hello\n','hi\n','cool\n']
file.writelines(list)
file.close()
print("-"*36)


file=open("demo.txt","r")
print(file.read())
file.close()



file=open("demo.txt","a")
file.write("coooooooooolllllllllll")
file.close()
print("-"*36)


file=open("demo.txt","r")
#read from file
print(file.read())
file.close()
