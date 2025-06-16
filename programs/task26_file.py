

'''
Write a Python program to read employee.csv and create a short summary sentence and display all the lines


39-year-old Male working as Adm-clerical earns <=50K.


'''



import csv

race_count = dict()


with open("employee.csv","r") as fobj:
    reader = csv.DictReader(fobj)
    for line in reader:
        age = line['age'].strip()
        gender = line['gender'].strip()
        occupation = line['occupation'].strip()
        score = line['income']

        print("{}-year-old {} working as {}earns {}".format(age,gender,occupation,score))



