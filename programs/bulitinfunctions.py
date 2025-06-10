

print(dir(__builtins__))  # will display all builtin functions and exceptions

print(list(range(1,10)))

val = int(34.3)
print(val)

alist =[ 10,20,30,40,90]
print(sum(alist))

print(max(alist))


print(min(alist))

print(sum(alist))

print(id(alist))  # will display the memory reference of object ( just like address in C )
print(id(val))


fobj = open('hello.txt',"w")
fobj.write("python programming\n")
fobj.close()




