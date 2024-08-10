import pymysql
import tkinter


#sql connection

Connection=pymysql.connect(host='localhost',
                           user='root',
                           password='1#nmnmnm1#',
                           database='booking_system'
                           )
Cursor=Connection.cursor()
#Cursor.execute("SELECT * FROM user_info;")
#print(Cursor.fetchall())


#user login interface
window=tkinter.Tk()
window.title("XYZ Bus booking")
login_interface=tkinter.Frame(window)
login_interface.pack(expand=True, fill='both')
frame_1=tkinter.LabelFrame(login_interface,background="#21201c")
frame_1.grid(row=0,column=0)
user_id=tkinter.Label(frame_1,text="Username or email address",font=6,background="#21201c",fg="white")
user_id.grid(column=0,row=0,sticky="w",pady=(7,0))
userid_entry=tkinter.Entry(frame_1,background="black",width=25,font=3,foreground="white")
userid_entry.grid(column=0,row=1,sticky="w")
user_pass=tkinter.Label(frame_1,text="Password",background="#21201c",fg="white",font=6)
user_pass.grid(row=2,column=0,sticky="w",pady=(7,0))
user_pass_entry=tkinter.Entry(frame_1,background="black",foreground="white",width=25,font=4)
user_pass_entry.grid(column=0,row=3,sticky="w")
login_button=tkinter.Button(frame_1,text="login",command=None,background= "#8AAB1D",foreground="white",font=6)
login_button.grid(row=4,column=0,pady=10)
sign_in_button=tkinter.Button(text="Sign in",)
frame_2=tkinter.LabelFrame(login_interface,text="Help",background="#21201c",foreground="white")
frame_2.grid(row=1,column=0)
help=tkinter.Label(frame_2,text="help")
help.grid(row=0,column=0,pady=10,padx=100)
help.bind("<Button-1>")


window.mainloop()

