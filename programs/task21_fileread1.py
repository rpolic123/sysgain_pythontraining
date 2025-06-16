

'''
write a program go read employee.csv and display all the distinct workclasses.

State-gov
Self-emp-not-inc
Private
Federal-gov
Local-gov

'''

import csv
workset = set()
with open("employee.csv") as fobj:
    header = fobj.readline()
    reader = csv.reader(fobj)
    # processing
    for line in reader:
        workclass = line[1]
        workset.add(workclass.strip())
    # displaying output
    for item in workset:
        print(item)


import csv
print("**** using dictionaries *****")
workdict = dict()
with open("employee.csv") as fobj:
    header = fobj.readline()
    reader = csv.reader(fobj)
    # processing
    for line in reader:
        workclass = line[1]
        workdict[workclass] = 1      #workdict = {"Never-worked":1 , "Federal-gov":1,"Private":1,"State-gov":1}
    # displaying output
    for item in workdict:
        print(item)