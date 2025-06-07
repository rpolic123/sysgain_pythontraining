'''
write a program to reverse a string without using [::-1]

Enter any string:  python
nohtyp
'''

text = input("Enter any string :")  #python


rev_text = ""

for char in text:
    rev_text = char + rev_text
print("String reverse:", rev_text)


# method2
data = list(text)  # ["p","y","t","h","o","n"]
data.reverse()       #['n', 'o', 'h', 't', 'y', 'p']
string = "".join(data)
print("String reverse :",string)

