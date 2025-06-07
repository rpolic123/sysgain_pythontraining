
'''
write a program to replace all the vowels in a string with *.

Enter a string: python
pyth*n

'''

text = input("Enter a string :")  #python
vowels = "aeiouAEIOU"
result = ""
for char in text:
    if char in vowels:
        result = result + "*"
    else:
        result = result + char
print("Output:", result)


#p
result : p 

#y
result : py

#t
result: pyt

#h
result : pyth

#o
result : pyth*