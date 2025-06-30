
# open the connection
# define query
# execute query
# fetch the output
# close the connections


import pymysql
import sys
try:
    #step1
    conn = pymysql.connect(host="localhost",port=3306,user="root",password="yourpassword")
    print(conn)   ##  0x3kdky
    if conn:
        cursor = conn.cursor() 
        #step2:
        query = "select * from empdb.employee"
        #step3
        cursor.execute(query)
        #step4
        for record in cursor.fetchall():
            print(record)
        #step5
        conn.close()
except Exception as err:
    print(err)
    print(sys.exc_info())

