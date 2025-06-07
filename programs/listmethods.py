
alist = [56,34,62,61,39,9,2,4,6,72]
# add single object
print("After appending :",alist)
alist.append(50)
print("After appending :", alist)
# adding multiple values to the end of list
alist.extend([45,32,5])
print("After extending :",alist)
#list.insert(index,value)
alist.insert(1,23)
print("After inserting :",alist )
alist.pop(0)  #0 is the index  # list.pop(index) # will remove value at that index
print("After pop opertaion :",alist)
alist.pop(3)  # 3 is the index
print("After pop opertaion :",alist)

if 720 in alist:
    alist.remove(720)  # 72 is the value
    print("After removing: :",alist)
    
alist.reverse()
print("Reversing :",alist)
alist.sort()  # ascending order
print("After sorting :",alist)
alist.sort(reverse=True) # descending order
print("After sorting:",alist)



alist = [56,34,62,61,39,9,2,4,6,72]
for val in alist:
    print(val)




### write a  program to check whether 34 is existing in the list or not.

# method1
alist = [56,34,62,61,39,9,2,4,6,72,34,34,34]
getcount = alist.count(34)
if getcount > 0 :
    print("value found")
else:
    print("value not found")

# method2
if 34 in alist :
    print("value found")
else:
    print("value not found")


name = "python programming"
if "gram" in name :
    print("substring found")
else:
    print("substring not found")


