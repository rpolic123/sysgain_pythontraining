

'''
write a program to square each number in a list

nums = [1,2,3,4]

output:
[1,2,9,16]

'''


nums = [1,2,3,4]
output = []
for val in nums:
    output.append(val ** 2)
print(output)