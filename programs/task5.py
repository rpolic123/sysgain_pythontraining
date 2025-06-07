

'''

write a program to count how many uppercase , lowercase letters and digits are  in  a string


Enter a string: PyTHon108
Uppercase letters: 3
Lowercase letters: 3
Digits : 3
'''


text = input("Enter a string :")
upper = 0
lower = 0
digits = 0
for char in text:
    if char.isupper() :
        upper+=1
    elif char.islower():
        lower+=1
    elif char.isdigit():
        digits+=1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
print("Digits:",digits)
