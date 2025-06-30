

'''
write a program to delete all the .xlsx files from current directory


'''

import os
try:
    files = os.listdir()

    for file in files:
        if file.endswith("xlsx"):
            os.remove(file)
            print(file, "is removed")
except Exception as err:
    print(err)

import os
try:
    files = os.listdir()

    for file in files:
        if ".xlsx" in file:  
            os.remove(file)
            print(file, "is removed")
except Exception as err:
    print(err)

import os
import re
try:
    files = os.listdir()

    for file in files:
        if re.search("xlsx",file,re.I): 
                os.remove(file)
                print(file, "is removed")
except Exception as err:
    print(err)