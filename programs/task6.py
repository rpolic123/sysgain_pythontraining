
'''
write a progarm to count character frequencies:


Enter a string :  hello

h : 1 time
e : 1 time
l : 2 times
o : 1 time


'''

text = input("Enter a string :")

list_text = list(text)
data= set(text)

for char in data:
    print(char.ljust(5), ":",list_text.count(char),"times")
