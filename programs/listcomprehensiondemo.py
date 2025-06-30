

# method1
for val in range(1,10):
    print(val)


# method2 - using list comprehension
# [expression forloop]
output = [  val+5  for val in range(1,10)]
print(output)



squares = [x**2 for x in range(10)]
print(squares)



for val in range(1,10):
    if val % 2 == 0:
        print(val)


evens = [x for x in range(2,20) if x % 2 == 0]
print(evens)


words = ['Python', 'is', 'awesome', 'AI', 'GPT']
short_words = [word for word in words if len(word) <= 3]
print(short_words)



names = ['alice', 'bob', 'charlie']
upper_names = [name.upper() for name in names]