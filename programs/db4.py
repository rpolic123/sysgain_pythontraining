
# top down approach
import os
import pymysql
import csv
import sys
try:
    #step1
    conn = pymysql.connect(host="localhost",port=3306,user="root",password="yourpassword")
    print(conn)   ##  0x3kdky
    if conn:
        cursor = conn.cursor() 
        #step2:
        filename = "employee.csv"
        if os.path.exists(filename) and os.path.isfile(filename):
            with open(filename,"r") as fobj:
                

                reader = csv.reader(fobj)
                count = 0
                for line in reader:

                    query = "insert into empdb.employee values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(*line)
                    #step3
                    cursor.execute(query)
                    #step4
                    count = count + 1
                    #step5
                print(count ,  "records inserted")
                conn.commit()   
                conn.close()
        else:
            print("file not found..")
except Exception as err:
    print(err)
    print(sys.exc_info())
