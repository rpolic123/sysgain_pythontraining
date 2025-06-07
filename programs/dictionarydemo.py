##### dictionary
book = {"chap1":10 , "chap2":20 ,"chap3":30}

print(book)

# add new keyvalue pairs
book["chap4"] = 40    #"chap4":40 will be added to dictionary
book["chap5"] = 50
print(book)

# display individual values
print(book["chap1"]) # 10
print(book["chap2"]) # 20


# display only keys
print(book.keys())

# only values
print(book.values())

# pairs
print(book.items())

# remove key-value
book.pop("chap1")  # chap1:10 will be removed
print("After pop operation :",book)

#remove last key-value
book.popitem()
print("After popitem :",book)
book.popitem()
print("After popitem :",book)

# combining two dictionaries
newbook = {"chap8":80,"chap9":90,"chap3":300}
finalbook = {**book,**newbook}
print("Final dictionary:",finalbook)

#method2
book.update(newbook)
print("updated book is :", book)



# dsiplay all the keys line by line 
for key in book.keys():
    print(key)


# display values
for v in book.values():
    print(v)

# display key and value at a time
for k,v in book.items():
    print(k,v)


## iterating list
alist = [10,20,30]
for val in alist:
    print(val)

# iterating string
name = "python"
for char in name:
    print(char)

# convert list to string
data = ["python","unix","java"]
string = "-".join(data)
print(string)