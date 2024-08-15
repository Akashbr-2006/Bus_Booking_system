import tkinter
import pymysql


seat_selected=[]
window=tkinter.Tk()

def sql():
    Cursor=pymysql.connect(host='localhost',
                           user='root',
                           password='1#nmnmnm1#',
                           database='booking_system'
                           ).cursor()
    return Cursor
cursor=sql()
def update_seat(seat_no,button):
    if seat_no not in seat_selected:
        seat_selected.append(seat_no)
        button.config(bg="green") 
        cursor.execute("INSERT INTO `booking_system`.`seat_info` (`seat_no`) VALUES ('"+seat_no+"');")
    else:
        seat_selected.remove(seat_no)
        button.config(bg="SystemButtonFace")
def create_seat_button(row, col, seat_no):
    button = tkinter.Button(bus_seat_grid, text=seat_no, image=img, bg="SystemButtonFace",
                            command=lambda: update_seat(seat_no, button) )
    if seat_no in seat_selected:
        button.config(bg="red")
        button.config(state="disabled")
    if col == 3 :
        x=20
    else:
        x=0
    button.grid(row=row, column=col, padx=(x, 0))
    return button
def get_reserved_data():
    cursor.execute("SELECT * FROM booking_system.seat_info;")
    reserved_data=cursor.fetchall()
    for sublist in reserved_data:
        for no in sublist:
            seat_selected.append(no)
    
get_reserved_data()

img=tkinter.PhotoImage(file="A:\\get-hub\\Bus_Booking_system\\Bg_image\\seat.png")

window.title("Bus seat selecter")
window.geometry("600x600")
fram=tkinter.Frame(window)
fram.pack()

dest="" 
bus_info=tkinter.Label(fram,text='Bus name:VRl\nBus number:KA13NB2869\nBus destation:'+dest+'\n ')
bus_info.grid(column=0,row=0,sticky="e")
bus_seat_grid=tkinter.LabelFrame(fram,text="Select the seat")
bus_seat_grid.grid(column=0,row=1)

#seat_index

no0=tkinter.Label(bus_seat_grid).grid(row=0,column=0)
no1=tkinter.Label(bus_seat_grid,text="1").grid(row=1,column=0)
no2=tkinter.Label(bus_seat_grid,text="2").grid(row=2,column=0)
no3=tkinter.Label(bus_seat_grid,text="3").grid(row=3,column=0)
a=tkinter.Label(bus_seat_grid,text="A").grid(row=0,column=1)
b=tkinter.Label(bus_seat_grid,text="B").grid(row=0,column=2)
c=tkinter.Label(bus_seat_grid,text="C").grid(row=0,column=3,padx=(20,0))
d=tkinter.Label(bus_seat_grid,text="D").grid(row=0,column=4)
e=tkinter.Label(bus_seat_grid,text="E").grid(row=0,column=5)

#seat layout

create_seat_button(1, 1, "A1")
create_seat_button(2, 1, "A2")
create_seat_button(3, 1, "A3")
create_seat_button(1, 2, "B1")
create_seat_button(2, 2, "B2")
create_seat_button(3, 2, "B3")
create_seat_button(1, 3, "C1")
create_seat_button(2, 3, "C2")
create_seat_button(3, 3, "C3")
create_seat_button(1, 4, "D1")
create_seat_button(2, 4, "D2")
create_seat_button(3, 4, "D3")
create_seat_button(1, 5, "E1")
create_seat_button(2, 5, "E2")
create_seat_button(3, 5, "E3")

terms_frame = tkinter.LabelFrame(fram, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
Terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
Terms_check.grid(row=0,column=0)

button = tkinter.Button(fram, text="Book Seat",background="red")
button.grid(row=3, column=0, sticky="news",  padx=20, pady=10)

window.mainloop()
print("SELECTED SEAT ARE ",seat_selected)