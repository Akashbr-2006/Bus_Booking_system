import pymysql
connectin=pymysql.connect(host='localhost',
                          user='root',
                          password='1#nmnmnm1#',
                          database='test')
Coursor=connectin.cursor()
Coursor.execute("select * from student;")
data=Coursor.fetchall()
for item in data:
    print(item[0])