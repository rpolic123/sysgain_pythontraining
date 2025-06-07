

'''
write a program to count no. of words in a sentence.

sample output:

Enter a sentence: I love python programming language
word count:  5
'''

name = input("Enter any string :")
data = name.split(" ")
print("no. of words: ", len(data))