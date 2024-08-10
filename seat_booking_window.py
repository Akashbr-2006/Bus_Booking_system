import tkinter
window=tkinter.Tk()
seat_selected=[]
seat_selected.clear()
def update_seat(seat_no):
    seat_selected.append(seat_no)



img=tkinter.PhotoImage(file="A:\\program\\Practice\\img.png")

window.title("Bus seat selecter")
fram=tkinter.Frame(window)
fram.pack()
bus_info=tkinter.Label(fram,text="Bus name:VRl\nBus number:KA13NB2869\n",)
bus_info.grid(column=0,row=0,sticky="e")
bus_seat_grid=tkinter.LabelFrame(fram,text="Select the seat")
bus_seat_grid.grid(column=0,row=1)


no0=tkinter.Label(bus_seat_grid)
no0.grid(row=0,column=0)

no1=tkinter.Label(bus_seat_grid,text="1")
no1.grid(row=1,column=0)

no2=tkinter.Label(bus_seat_grid,text="2")
no2.grid(row=2,column=0)

no3=tkinter.Label(bus_seat_grid,text="3")
no3.grid(row=3,column=0)

a=tkinter.Label(bus_seat_grid,text="A")
a.grid(row=0,column=1)

b=tkinter.Label(bus_seat_grid,text="B")
b.grid(row=0,column=2)

c=tkinter.Label(bus_seat_grid,text="C")
c.grid(row=0,column=3,padx=(20,0))

d=tkinter.Label(bus_seat_grid,text="D")
d.grid(row=0,column=4)

e=tkinter.Label(bus_seat_grid,text="E")
e.grid(row=0,column=5)

#seat layout

seat_a1=tkinter.Button(bus_seat_grid,text="A1",image=img,command='update_seat("A1")')
seat_a1.grid(row=1,column=1)

seat_a2=tkinter.Button(bus_seat_grid,text="A2",image=img,command='update_seat("A2")')
seat_a2.grid(row=2,column=1)

seat_a3=tkinter.Button(bus_seat_grid,text="A3",image=img,command='update_seat("A3")')
seat_a3.grid(row=3,column=1)

seat_b1=tkinter.Button(bus_seat_grid,text="B1",image=img,command=update_seat("B1"))
seat_b1.grid(row=1,column=2)

seat_b2=tkinter.Button(bus_seat_grid,text="B2",image=img,command=update_seat("B2"))
seat_b2.grid(row=2,column=2)

seat_b3=tkinter.Button(bus_seat_grid,text="B3",image=img,command=update_seat("B3"))
seat_b3.grid(row=3,column=2)


seat_c1=tkinter.Button(bus_seat_grid,text="C1",image=img,command=update_seat("C1"))
seat_c1.grid(row=1,column=3,padx=(20,0))

seat_c2=tkinter.Button(bus_seat_grid,text="C2",image=img,command=update_seat("C2"))
seat_c2.grid(row=2,column=3,padx=(20,0))

seat_c3=tkinter.Button(bus_seat_grid,text="C3",image=img,command=update_seat("C3"))
seat_c3.grid(row=3,column=3,padx=(20,0))

seat_d1=tkinter.Button(bus_seat_grid,text="D1",image=img,command=update_seat("D1"))
seat_d1.grid(row=1,column=4)

seat_d2=tkinter.Button(bus_seat_grid,text="D2",image=img,command=update_seat("D2"))
seat_d2.grid(row=2,column=4)

seat_d3=tkinter.Button(bus_seat_grid,text="D3",image=img,command=update_seat("D3"))
seat_d3.grid(row=3,column=4)

seat_e1=tkinter.Button(bus_seat_grid,text="E1",image=img,command=update_seat("E1"))
seat_e1.grid(row=1,column=5)

seat_e2=tkinter.Button(bus_seat_grid,text="E2",image=img,command=update_seat("E2"))
seat_e2.grid(row=2,column=5)

seat_e3=tkinter.Button(bus_seat_grid,text="E3",image=img,command=update_seat("E3"))
seat_e3.grid(row=3,column=5)


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