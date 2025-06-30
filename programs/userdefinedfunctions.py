# fixed arguments
def display(a,b):
    ''' this is doc string - help documentation'''
    c = a + b
    return c

total = display(10,20)
print(total)

### default arguments
def display(a = 0,b = 0,c = 0,d = 0):
    print(a,b,c,d)

display()
display(10)
display(10,20)
display(10,20,30)
display(10,20,30,40)


# variable length arguments
def display(*args):
    for val in args:
        print(val)

display(10,20,30,40,5,56,4343,43)


def displayinfo(**kwargs):   #**kwargs is the dicttionary
    print(kwargs)
    for key,value in kwargs.items():
        print(key,value)


displayinfo(chap1 = 10 , chap2 = 20)