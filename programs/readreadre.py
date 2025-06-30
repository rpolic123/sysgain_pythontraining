


### re = regular expressions
# matching     re.match()
# substution   re.sub()
# searching    #. re.searh()


import re  # searching  # substitution # replacing
with open("employee.csv") as fobj:
    for line in fobj:
        line = line.strip()
        if re.search("Male",line):
            print(line)