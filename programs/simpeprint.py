

#list
alist = [10,30,40,50]
alist[0] = 100
print("After changes :", alist)





#tuple
#atup = (10,20,30,40,50)
#atup[0] = 100
#print("After changes :", atup)


# 
atup = (10,20,30,40,50)
alist = list(atup)  # typecasting : converting from one object to another object
alist[0] = 1000     # making changes
atup = tuple(alist) # reconverting back
print("After changes :", atup)


aset = {10,10,10,20,20,30,30,56,43,43,56,32,45,23,4,5454}
print(aset)
aset = {10,10,10,20,20,30,30,"unix","unix","java",45.43}
print(aset)