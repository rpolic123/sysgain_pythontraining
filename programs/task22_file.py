

'''
write a program to read employee.csv and display the below output

Total no. of males : xxx
Total no. of females: xx


'''



import csv
mcount = 0
fcount = 0
with open("employee.csv") as fobj:
    header = fobj.readline()
    reader = csv.reader(fobj)
    for line in reader:
        gender = line[9].strip()
        if gender == "Male":
            mcount+=1
        elif gender == "Female":
            fcount+=1
    print("Total no. of males   :", mcount)
    print("Total no. of females :", fcount)