
#### objects should be of same type

print(4 + 4)   # will work
print("hi" + "python")  # will work
print(4 + "hello")   # doesnt work
print([10,20] + [40,50])  # will work
print( (50,60) + [30,40])  # doesnt work




fobj = open("customers.txt","w")

fobj.write("python programming\n")
fobj.write("unix shell\n")

for val in range(1,10):
    fobj.write(str(val)  + "\n")

fobj.close()