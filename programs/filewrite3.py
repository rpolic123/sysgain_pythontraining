
'''
fobj = open("customers.txt","w")

fobj.write("python programming\n")
fobj.write("unix shell\n")
fobj.writelines(["java","unix","python"])
for val in range(1,10):
    fobj.write(str(val) + "\n")

fobj.close()
'''

# not required to close the file
# context manager
# If any line starts with the keyword 'with' ... it is called as context manager
# Advantage : file is closed automatically ... NOT required to close manually.


# pythonic way   # lastest way

# If path is not defined .. file gets created in same directory
with open("customerinfo.csv","w") as fobj:
    fobj.write("python programming\n")
    fobj.write("unix shell\n")
    fobj.writelines(["java","unix","python"])
    print(fobj.closed)


#file is closed here
print(fobj.closed)
    



with open("customerinfo.csv","w") as fobj,open("customerdata.txt","w") as fobj1:
    fobj.write("python programming\n")
    fobj.write("unix shell\n")
    fobj.writelines(["java","unix","python"])
    fobj1.write("this is file2\n")
    print(fobj.closed)

#file is closed here
print(fobj.closed)
    




