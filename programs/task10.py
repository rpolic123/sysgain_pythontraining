'''
Write a program to join corresponding strings from two lists.

first = ["Good", "Data", "Machine"]
second = ["Morning", "Science", "Learning"]

Output:
Good Morning
Data Science
Machine Learning
'''


first = ["Good", "Data", "Machine"]
second = ["Morning", "Science", "Learning"]

count = 0

for item in first:
    finalstring = first[count] + " " + second[count]
    count = count + 1
    print(finalstring)



#zip(list1,list2)

for a,b in zip(first,second):
    finalstring = a + " " + b
    print(finalstring)
