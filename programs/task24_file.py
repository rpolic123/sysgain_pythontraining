

'''

write a program to read employee.csv and replace all the lines containing
 United-States with USA and write the output to 12_June_2025.csv
 	

'''




with open("employee.csv") as fr,   open("usa_data.csv","w") as fw:
    for line in fr:
        line = line.strip()
        line = line.replace("United-States","USA")
        print(line)
        fw.write(line + "\n")