

import sys
try:
    #fobj acts like cursor or handler
    with open("customers1111.txt","r") as fobj:
        for line in fobj:
            line = line.strip()
            print(line)

except Exception as err:  # default exception
    print(err)
    print(sys.exc_info())
print("regular program")
