


# traditional way  # regular way
fobj = open("customers.txt","w")

fobj.write("python programming\n")
fobj.write("unix shell\n")
fobj.writelines(["java","unix","python"])
for val in range(1,10):
    fobj.write(str(val) + "\n")

fobj.close()

