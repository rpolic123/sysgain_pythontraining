
name = "python programming"

print(name.capitalize())
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