from tkinter import *
from tkinter import ttk
import mysql.connector

mydb = mysql.connector.connect(user = 'lifechoices', password = '@Lifechoices1234', host = '127.0.0.1', database = 'End_of_Module', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

root = Tk()
root.title("Admin")
root.geometry("1000x600")
class admin:
    def __init__(self, master):
        self.treeView = ttk.Treeview(master, selectmode = 'browse')
        # define our columns
        self.treeView["columns"] = ("ID","Name", "Surname", "Phone Number", "ID Number","Password", "Next of Kin ID")
        # Format Our Columns
        self.treeView.column("#0", width=0, stretch=NO)
        self.treeView.column("ID", anchor=CENTER, width = 40)
        self.treeView.column("Name", anchor=W, width=100)
        self.treeView.column("Surname", anchor=W, width=100)
        self.treeView.column("Phone Number", anchor=W, width=150)  # phantom column
        self.treeView.column("ID Number", anchor=W, width=150)
        self.treeView.column("Password", anchor=W, width=150)
        self.treeView.column("Next of Kin ID", anchor=CENTER, width=150)
        # Create Headings
        # self.tree_view_admin.heading("#0", text="", anchor=CENTER)
        self.treeView.heading("ID", text = "ID", anchor = CENTER)
        self.treeView.heading("Name", text="Name", anchor=CENTER)
        self.treeView.heading("Surname", text="Surname", anchor=CENTER)
        self.treeView.heading("Phone Number", text="Phone Number", anchor=CENTER)
        self.treeView.heading("ID Number", text="ID Number", anchor=CENTER)
        self.treeView.heading("Password", text="Password", anchor=CENTER)
        self.treeView.heading("Next of Kin ID", text="Next of Kin ID ", anchor=CENTER)
        self.treeView.place(x=100, y=100)
        xy = mycursor.execute('Select * from register')
        for i in mycursor:
           #print(i)
           self.treeView.insert("", 'end', iid = i[0], values = (i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
x = admin(root)
root.mainloop()
