

aset = {10,10,10,20,20,20,30,30,30}
bset = {30,30,30,30,40,40,40,50}

print(aset)
print(bset)

#union 
print(aset.union(bset))

#intersection
print(aset.intersection(bset))

# differnce
print(aset.difference(bset))
print(bset.difference(aset))

print(aset.issubset(bset))  # if all the elements of A are present in B then True or else False
print(aset.issuperset(bset)) # if all the elements of B are present i A then True or else False

aset.add(10)
print("After addding :", aset)
aset.add(100)
print("After addding :", aset)



