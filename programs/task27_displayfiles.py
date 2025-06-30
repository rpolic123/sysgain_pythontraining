

'''
write a program to display all the files and directories from current directory line by line

'''

## display all the files and directories
import os
try:
    files = os.listdir()
    for file in files:
        print(file)
except Exception as err:
    print(err)




#### display all the files and directories from C:\\
import os

try:
    files = os.listdir("C:\\")
    for file in files:
        print(file)
except Exception as err:
    print(err)




import os

try:
    files = os.listdir("C:\\")
    for file in files:
        if file.endswith("xlsx"):
            print(file)
except Exception as err:
    print(err)
