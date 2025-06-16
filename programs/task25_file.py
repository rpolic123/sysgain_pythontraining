
'''

Write a Python program to read employee.csv and 
use a dictionary to count how many employees belong to each race.

{'White': 27816, 'Black': 3124, 'Asian-Pac-Islander': 1039}
'''


import csv

race_count = dict()


with open("employee.csv","r") as fobj:
    reader = csv.DictReader(fobj)
    for line in reader:
        race = line['race'].strip()
        if race in race_count:
            race_count[race]+=1
        else:
            race_count[race] = 1
    
print(race_count)

