
'''
write a program go read employee.csv and display all the records where

education is  Bachelors and Gender is Female.

also display total no. records matching above conditions.

'''


import csv
count = 0
with open("employee.csv") as fobj:
    header = fobj.readline()
    reader = csv.reader(fobj)
    for line in reader:
        if line[3].strip() == "Bachelors" and line[9].strip() == "Female":
            print(line)
            count = count + 1
    
    print("No. of records matching above conditions :", count)
