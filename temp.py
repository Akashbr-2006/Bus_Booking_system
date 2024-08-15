import tkinter


window=tkinter.Tk()
window.title("XYZ Bus booking")
window.geometry("600x417")
window.configure(background="#21201c")


image=tkinter.PhotoImage(file="A:\\get-hub\\Bus_Booking_system\\img.png")
imagee=tkinter.Label(window,image=image)
imagee.place(relheight=1.0,relwidth=1.0)
frame=tkinter.Frame(window)
#frame.configure(background="black")
frame.place(relx=0.5,rely=0.4,anchor="center")

bus_searching_frame=tkinter.LabelFrame(frame,background="white")
bus_searching_frame.pack(fill="both", expand=True, padx=10, pady=10)
from_=tkinter.Label(bus_searching_frame,text="From:")
from_.grid(column=0,row=0,sticky="w")
from_entry=tkinter.Entry(bus_searching_frame,background="white")
from_entry.grid(row=1,column=0,padx=10)
to_entry=tkinter.Label(bus_searching_frame,text="To:")
to_entry.grid(row=0,column=1,sticky="w")
to_entry=tkinter.Entry(bus_searching_frame,background="white")
to_entry.grid(row=1,column=1)
date=tkinter.Label(bus_searching_frame,text="Date:")
date.grid(row=0,column=2,sticky="w")
date_entry=tkinter.Entry(bus_searching_frame)
date_entry.grid(row=1,column=2,padx=10)
search_button=tkinter.Button(bus_searching_frame,text="Search Busses",background="red",foreground="white",font=("Calisto"))
search_button.grid(row=3,column=1,pady=(40,20))

window.mainloop()