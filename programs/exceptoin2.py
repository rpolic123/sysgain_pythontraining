

import sys
try:
    #fobj acts like cursor or handler
    fobj =  open("customers111111.txt","r")

except Exception as err:  # default exception
    print(err)
    print(sys.exc_info())
else:
    for line in fobj:
        line = line.strip()
        print(line)
finally:
    print("end of file reading")
    fobj.close()









import sys
try:
    with open("customers.txt", "r") as fobj:
        for line in fobj:
            print(line.strip())
except Exception as err:
    print(err)
    print(sys.exc_info())
finally:
    print("end of file reading")







import sys

fobj = None 
try:
    # fobj acts like cursor or handler
    fobj = open("customers11111.txt", "r")

except Exception as err:  # default exception
    print(err)
    print(sys.exc_info())

else:
    for line in fobj:
        line = line.strip()
        print(line)

finally:
    print("end of file reading")
    if fobj is not None:
        fobj.close()
