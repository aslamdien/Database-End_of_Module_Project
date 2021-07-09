import mysql.connector
from tkinter import *
from tkinter import messagebox
from datetime import *

mydb = mysql.connector.connect(user = 'lifechoices', password = '@Lifechoices1234', host = '127.0.0.1', database = 'End_of_Module', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

mycursor.execute('Select * from register')

root = Tk()
root.title("Login Page")
root.geometry("500x300")
root.config(bg = "#4850c8")

my_pic = PhotoImage(file = "life.png")
background = Label(root, image = my_pic).place(x=100, y=10)

date = StringVar()
time = StringVar()
reset = StringVar()

def admin_page(event):
    root.destroy()
    import admin1

root.bind("<Control-a>", admin_page)

usernamelab = Label(root, text = "Please Enter Your Name:")
usernamelab.place(x=50, y=150)
usernameEnt = Entry(root)
usernameEnt.place(x=220, y=150)

datenow = Entry(root, textvariable = date)
timenow = Entry(root, textvariable = time)
resetnow = Entry(root, textvariable = reset)


passwordlab = Label(root, text = "Please Enter Your Password:")
passwordlab.place(x=30, y=200)
passwordEnt = Entry(root)
passwordEnt.place(x=220, y=200)


def login():
    global i
    for i in mycursor:
        if usernameEnt.get() == i[2] and passwordEnt.get() == i[6]:
            messagebox.showinfo("Logging Out", "See You Soon")
            root.destroy()
            import logout
            break

        elif usernameEnt.get() == None or passwordEnt.get() == None:
            messagebox.showerror("Error", "Please fill Out Information")
        elif usernameEnt.get() != i[2] or passwordEnt.get() != i[6]:
            messagebox.showerror("Access Denied", "Unknown User")
            usernameEnt.delete(0, END)
            passwordEnt.delete(0, END)


        elif usernameEnt.get() == None or passwordEnt.get() == None:
            messagebox.showerror("Error", "Please fill Out Information")
        elif usernameEnt.get() != i[2] and passwordEnt.get() != i[6]:
            messagebox.showerror("Access Denied", "Unknown User")
            usernameEnt.delete(0, END)
            passwordEnt.delete(0, END)


def register():
    root.destroy()
    import register

loginbtn = Button(root, text = "Login", command = login)
loginbtn.place(x=150, y=250)

registerbtn = Button(root, text = "Register New User", command = register)
registerbtn.place(x=250, y=250)

root.mainloop()
