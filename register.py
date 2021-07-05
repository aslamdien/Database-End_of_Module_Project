from tkinter import *
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(user = 'lifechoices', password = '@Lifechoices1234', host = '127.0.0.1', database = 'End_of_Module', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

root = Tk()
root.title("Register")
root.geometry("500x500")

fisrt_namelab = Label(root, text = "PLease Enter First Name:")
fisrt_namelab.place(x = 50, y = 20)
fisrt_nameEnt = Entry(root)
fisrt_nameEnt.place(x=220, y=20)

last_namelab = Label(root, text = "Please Enter Last Name:")
last_namelab.place(x = 50, y = 70)
last_nameEnt = Entry(root)
last_nameEnt.place(x=220, y=70)


root.mainloop()


