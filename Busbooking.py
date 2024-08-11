import pymysql
import tkinter
                            #bus_seat_selection 
def update_status(seat_number):
    Connection=pymysql.connect(host='localhost',
                          user='root',
                          password='1#nmnmnm1#',
                          database='booking_system')
    Coursor=Connection.cursor()
    Coursor.execute("SELECT * FROM booking_system.seat_info;")
    print(Coursor.fetchall())
update_status(1)