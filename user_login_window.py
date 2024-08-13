import pymysql
import tkinter
from tkinter import messagebox

def error_windo(msg):
    messagebox.showerror("error 303",msg)


def check():
    ented_user_id=userid_entry.get()
    user_pass_entry=login_pass_entry.get()
    query="select * from booking_system.user_info where user_id='"+ented_user_id+"';"
    Cursor.execute(query)
    user_info=Cursor.fetchall()
    if user_info==():
        error_windo("user not found ")
    elif user_info[0][1]==user_pass_entry and user_info[0][0]==ented_user_id:
        print("loged in")
        #command to call the bus search windo is not written
    elif user_info[0][1]!=user_pass_entry or user_info[0][0]!=ented_user_id: 
            error_windo("wronge password please try agian")

#sql connection

def mysql():
     Connection=pymysql.connect(host='localhost',
                           user='root',
                           password='1#nmnmnm1#',
                           database='booking_system'
                           )
     Cursor=Connection.cursor()
     return Cursor
Cursor=mysql()


#user login interface



window=tkinter.Tk()
window.title("XYZ Bus booking")
window.geometry("600x600")
window.configure(background="#21201c")

login_interface=tkinter.Frame(window,background="#21201c")
login_interface.place(relx=0.5, rely=0.5, anchor="center",relwidth=0.8,relheight=1.0)

frame_1=tkinter.LabelFrame(login_interface,background="#21201c")
frame_1.place(relx=0.5, rely=0.4, anchor="center",relwidth=0.6,relheight=0.4)

#login_frame

user_id=tkinter.Label(frame_1,text="Username or email address",font=6,background="#21201c",fg="white")
user_id.grid(column=0,row=0,sticky="w",pady=(7,0))

userid_entry=tkinter.Entry(frame_1,background="black",width=25,font=3,foreground="white")
userid_entry.grid(column=0,row=1,sticky="w")

login_pass=tkinter.Label(frame_1,text="Password",background="#21201c",fg="white",font=6)
login_pass.grid(row=2,column=0,sticky="w",pady=(7,0))

login_pass_entry=tkinter.Entry(frame_1,background="black",foreground="white",width=25,font=4)
login_pass_entry.grid(column=0,row=3,sticky="w")

login_button=tkinter.Button(frame_1,text="login",command=check,background= "#8AAB1D",foreground="white",font=6)
login_button.grid(row=4,column=0,pady=10)


#help_frame
help_frame=tkinter.LabelFrame(login_interface,background="#21201c",foreground="white",width=200, height=100)
help_frame.place(relx=0.5, rely=0.7, anchor="center",relheight=0.12,relwidth=0.6)

forget_password=tkinter.Label(help_frame,text="forget password",background="#21201c",foreground="#2759e3",font=("Arial",12,"underline"))
forget_password.grid(row=0,column=0)
help=tkinter.Label(help_frame,text="help",background="#21201c",foreground="#2759e3",font=("Arial",12,"underline"))
help.grid(row=1,column=0,pady=10,padx=122)
help.bind("<Button-1>")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


#sign_in frame

window.mainloop()