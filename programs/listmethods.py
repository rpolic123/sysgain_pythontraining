

alist = [56,34,62,61,39,9,2,4,6,72]

# add single object
alist.append(39)
print("After appending :",alist)
alist.append(41)
print("After appending :", alist)
# adding multiple values to the end of list
alist.extend([81,29,43])
print("After extending :",alist)
#list.insert(index,value)
alist.insert(0,100)
print("After indexing :",alist )
alist.pop(0)  #0 is the index  # list.pop(index) # will remove value at that index
print("After pop opertaion :",alist)
alist.pop(3)
print("After pop opertaion :",alist)
alist.remove(72)  # 72 is the value
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

