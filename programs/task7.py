
'''
wrrite a program to reverse a list without list.reverse() and [::-1]
'''

alist = [45,67,21,65,32,96,10]
print("Initial list:", alist)
rev_list= []

for num in alist:
    rev_list = [num] + rev_list

print("After reversing :", rev_list)