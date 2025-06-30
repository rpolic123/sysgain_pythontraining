

import pymysql
import sys
try:
    #step1
    conn = pymysql.connect(host="localhost",port=3306,user="root",password="yourpassword")
    print(conn)   ##  0x3kdky
    if conn:
        cursor = conn.cursor() 
        #step2:
        #query = "insert into empldb.employee values('private','inter')"
        query = "insert into empdb.employee values('{}','{}')".format('public','10thclass')
        #step3
        cursor.execute(query)
        #step4
        print("1 record inserted")

        #step5
        conn.commit()
        conn.close()
except Exception as err:
    print(err)
    print(sys.exc_info())
