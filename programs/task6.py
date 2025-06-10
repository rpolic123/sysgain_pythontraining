
'''
write a progarm to count character frequencies:


Enter a string :  hello

h : 1 time
e : 1 time
l : 2 times
o : 1 time


'''

text = input("Enter a string :")

list_text = list(text)   #[ "h","e","l","l","o"]
data= set(text)          # ["h","e","l","o"]

for char in data: #["h","e","l","o"]
    print(char.ljust(5), ":",list_text.count(char),"times")
