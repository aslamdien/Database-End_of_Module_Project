import mysql.connector
from tkinter import *
from tkinter import messagebox

# Testing the login

mydb = mysql.connector.connect(user = 'lifechoices', password = '@Lifechoices1234', host = '127.0.0.1', database = 'hospital', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

xy = mycursor.execute('Select * from login')

root = Tk()
root.title("Login Page")
root.geometry("500x300")

usernamelab = Label(root, text = "Please Enter Username:")
usernamelab.place(x=50, y=50)
usernameEnt = Entry(root)
usernameEnt.place(x=220, y=50)

passwordlab = Label(root, text = "Please Enter Password:")
passwordlab.place(x=50, y=100)
passwordEnt = Entry(root, show = "*")
passwordEnt.place(x=220, y=100)

def login():
    global i
    for i in mycursor:
        if usernameEnt.get() == i[0] and passwordEnt.get() == i[1]:
            messagebox.showinfo("Loged In", "Access Granted")
            break

    if usernameEnt.get() == "" and passwordEnt.get() == "":
        messagebox.showerror("Access Denied", "Please Fill In Everything")
    elif usernameEnt.get() != i[0] or passwordEnt.get() != i[1]:
        messagebox.showerror("Error", "Please Enter Username And Password")
        usernameEnt.delete(0, END)
        passwordEnt.delete(0, END)


loginbtn = Button(root, text = "Login", command = login)
loginbtn.place(x=150, y=150)


root.mainloop()

