import pymysql
connectin=pymysql.connect(host='localhost',
                          user='root',
                          password='1#nmnmnm1#',
                          database='booking_system')
Coursor=connectin.cursor()
Coursor.execute("select * from seat_info;")
data=Coursor.fetchall()
for item in data:
    print(item[0])