'''
 write a script to perform the below operations :

1. display current working directory
2. display login name
3. display all environment variables
4. display today's date ( timestamp )
5. display May months calendar
6. display all .py files and its size in bytes
7. display the modified time of employees.csv file
8. display current process id

'''

import os
import datetime
import calendar
try:
    pwd = os.getcwd()
    print("Current working directory :", pwd)
    print("loginame :", os.getlogin())
    print("display all enviornment variables:")
    for key,value in os.environ.items():
        print(key)
        print(value)
        print("------")
    print(datetime.datetime.now())
    print(calendar.month(2025,5))
    print(calendar.calendar(2025))


    for file in os.listdir():
        if file.endswith(".py"):
            print(file.ljust(20), os.path.getsize(file),"bytes")

    print(os.getpid())
except Exception as err:
    print(err)

