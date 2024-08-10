import pymysql
import tkinter
                            #bus_seat_selection 
def update_status(seat_number):
    Connection=pymysql.connect(host='localhost',
                          user='root',
                          password='1#nmnmnm1#',
                          database='test')
    Coursor=Connection.cursor()
    Coursor.execute("SELECT * FROM test.seat_info where status = 0;")
    print(Coursor.fetchall())
update_status(1)