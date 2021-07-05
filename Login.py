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

id_numberlab = Label(root, text = "Please Enter ID Number:")
id_numberlab.place(x=50, y=100)
id_numberEnt = Entry(root)
id_numberEnt.place(x=220, y=100)

def login():
    for i in mycursor:
        if usernameEnt.get() == i[0] and id_numberEnt.get() == i[3]:
            messagebox.showinfo("Loged In", "Access Granted")
            break

        elif usernameEnt.get() != i[0] and id_numberEnt.get() != i[3]:
            messagebox.showerror("Access Denied", "Please Enter Correct Users Name Or ID Number")
            usernameEnt.delete(0, END)
            id_numberEnt.delete(0, END)
            break


loginbtn = Button(root, text = "Login", command = login)
loginbtn.place(x=150, y=150)

registerbtn = Button(root, text = "Register New User")
registerbtn.place(x=250, y=150)

root.mainloop()
