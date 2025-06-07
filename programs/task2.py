
#write a program to convert the string to uppercase only if its length 
# is more than 10 characters else display the same string.


name = input("Enter any name :")

if len(name) > 10 :
    print("String:",name)
else:
    print(f"length of the {name} is less than 10 chars")