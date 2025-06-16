# method1
#fobj acts like cursor or handler
with open("customers.txt","r") as fobj:
    for line in fobj:
        line = line.strip()
        print(line)


### display the names only
with open("customers.txt","r") as fobj:
    for line in fobj:
        line = line.strip()
        output = line.split(",")
        print(output[0])

# method2
with open("customers.txt","r") as fobj:
    print(fobj.readlines())  # display all the lines in list


#method3 : just like ctrl+A  ctrl+C  ctrl+V
# not suggested for bigger files 
with open("customers.txt","r") as fobj:
    print(fobj.read())  # will read the whole file at once

#method4

import csv  # Advantage: Each line is automatically converting to list
with open("customers.txt","r") as fobj:
    reader = csv.reader(fobj)  # converting file object to csv object
    for line in reader:
        print(line)

#method5
import pandas
print(pandas.read_csv("customers.txt"))



# If the file is in different path in windows:

#with open(r"D:\newfolder\customers.txt","r") as fobj:   # raw string
#with open("D:\\newfolder\\customers.txt","r") as fobj:
#with open("D:/newfolder/customers.txt","r") as fobj:


with open("customers.txt","r") as fobj:
    for line in fobj:
        line = line.strip()
        print(line)
