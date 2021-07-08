import mysql.connector
from tkinter import *
from tkinter import messagebox

mydb = mysql.connector.connect(user = 'lifechoices', password = '@Lifechoices1234', host = '127.0.0.1', database = 'End_of_Module', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

xy = mycursor.execute('Select * from register')

root = Tk()
root.title("Login Page")
root.geometry("500x300")

usernamelab = Label(root, text = "Please Enter Your Name:")
usernamelab.place(x=50, y=50)
usernameEnt = Entry(root)
usernameEnt.place(x=220, y=50)

passwordlab = Label(root, text = "Please Enter Your Password:")
passwordlab.place(x=30, y=100)
passwordEnt = Entry(root)
passwordEnt.place(x=220, y=100)

def login():
    global i
    for i in mycursor:
        if usernameEnt.get() == i[0] and passwordEnt.get() == i[5]:
            messagebox.showinfo("Loged In", "Access Granted")
            break

    if usernameEnt.get() == '' or passwordEnt.get() == '':
        messagebox.showerror("Error", "Please fill Out Information")
    elif usernameEnt.get() != i[2] and passwordEnt.get() != i[6]:
        messagebox.showerror("Access Denied", "Unknown User")
        usernameEnt.delete(0, END)
        passwordEnt.delete(0, END)

def register():
    root.destroy()
    import register

loginbtn = Button(root, text = "Login", command = login)
loginbtn.place(x=150, y=150)

registerbtn = Button(root, text = "Register New User", command = register)
registerbtn.place(x=250, y=150)

root.mainloop()
