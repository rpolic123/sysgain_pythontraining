
name = "python programming"

print(name.capitalize())
print(name)
print(name.title())
print(name.replace("python","ruby"))
print(name.center(40))
print(name.center(40,"*"))
print(name.endswith("g"))
print(name.endswith("q"))
print(name.startswith("p"))
print(name.startswith("w"))
print(name.find("gra"))  # if substring found.. returns the starting index
print(name.find("qer"))  # if substring is not round.. retuns -1
print(name.isalpha())
print(name.isalnum())
print(name.isupper())
print(name.isdigit())
print(name.islower())

aname = " python  "
print(len(aname))
print(aname.strip())  # will remove whitespaces at both ends
print(len(aname.strip())) # remove whitespaces first and then get the string length
print(len(aname.rstrip()))
print(len(aname.lstrip()))

print(name.split(" "))  # converting string to the list

# string formatting
string = "I love {} and {}" # template
print(string.format("python","ML"))
print(string.format("c","C++"))
print(string.format("Hyderabad","Bangalore"))

# fstring 
name = "Rita"
age = 30
print(f"My name is {name} and my age is {age} years")

lang1 = "python"
lang2 = "ML"
print(f"I love {lang1} and {lang2}")




print(name.isalpha())
print(name.isalnum())
print(name.isupper())
print(name.isdigit())
print(name.islower())

# simple if
name = "python"
if name.islower():
    print("String is lower")

# if-else
if name.islower():
    print("String is lower")
    print("inside if")
    print("Still inside if")
else:
    print("String is upper")

# if-elif-eif-elif-elif-else
lang = input("Enter any language :")
if lang == "python":
    print("you entered python")
elif lang == "unix":
    print("you entered unix")
elif lang == "java":
    print("you entered java")
elif lang == "genai":
    print("you entered genai")
else:
    print("you entered someother language")

# range(start,stop,step)
for i in range(1,11):
    print(i)


for i in range(1,11,2):
    print(i)

for i in range(11,1,-1):
    print(i)

name = "python"
for char in name:
    print(char)


name = "python"
for char in name[::-1]:
    print(char)