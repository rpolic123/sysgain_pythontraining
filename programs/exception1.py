import sys
try:
    #fobj acts like cursor or handler
    with open("customers1111.txt","r") as fobj:
        for line in fobj:
            line = line.strip()
            print(line)
except TypeError as err:
    print(err)
    print(sys.exc_info())
except ValueError as err:
    print(err)
    print(sys.exc_info())
except (KeyError,IndexError) as err:
    print("Invalid index or key")
    print(err)
    print(sys.exc_info())
except FileNotFoundError as err:
    print("File is not found")
    print(err)
    print(sys.exc_info())
except Exception as err:  # default exception
    print(err)
    print(sys.exc_info())
print("regular program")
