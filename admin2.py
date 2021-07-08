from tkinter import *
from tkinter import ttk
import mysql.connector

mydb = mysql.connector.connect(user = 'lifechoices', password = '@Lifechoices1234', host = '127.0.0.1', database = 'End_of_Module', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

root = Tk()
root.title("Admin Loged Info")
root.geometry("1000x600")
class admin_login:
    def __init__(self, master):

        # Style For Treeview
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.style.configure("Treeview",
                             background = "silver",
                             rowheight = 25,
                             fieldbackground = "silver"
                             )
        self.style.map('Treeview',
                       background=[('selected', 'lime green')]
                       )
        # Create Treeview
        self.treeView = ttk.Treeview(master, selectmode = 'browse')
        # define our columns
        self.treeView["columns"] = ("ID","Date", "Name", "Surname", "Loged In", "Loged Out")
        # Name and Size Our Columns
        self.treeView.column("#0", width=0, minwidth = 100, stretch = NO)
        self.treeView.column("ID", anchor=CENTER, width = 40)
        self.treeView.column("Date", anchor = CENTER, width = 100)
        self.treeView.column("Name", anchor=W, width=100)
        self.treeView.column("Surname", anchor=W, width=100)
        self.treeView.column("Loged In", anchor=CENTER, width=150)  # phantom column
        self.treeView.column("Loged Out", anchor=CENTER, width=150)


        # Create Headings
        # self.tree_view_admin.heading("#0", text="", anchor=CENTER)
        self.treeView.heading("ID", text = "ID", anchor = CENTER)
        self.treeView.heading("Date", text = "Name", anchor=CENTER)
        self.treeView.heading("Name", text="Name", anchor=CENTER)
        self.treeView.heading("Surname", text="Surname", anchor=CENTER)
        self.treeView.heading("Loged In", text="Loged In", anchor=CENTER)
        self.treeView.heading("Loged Out", text="Loged Out", anchor=CENTER)


        self.treeView.place(x=150, y=50)

        #Sript rows into odd and evens
        self.treeView.tag_configure("odd", background = "grey")
        self.treeView.tag_configure("even", background = "green")

        #Buttons

        xy = mycursor.execute('Select * from register')
        count = 0
        for i in mycursor:
           #print(i)
           if count % 2 == 0:
               self.treeView.insert("", 'end', iid = count, values = (i[0], i[1], i[2], i[3], i[8], i[9]), tags = ("even",))
           else:
               self.treeView.insert("", 'end', iid = count, values = (i[0], i[1], i[2], i[3], i[8], i[9]), tags = ("odd",))
           count += 1
        mydb.commit()

x = admin_login(root)
root.mainloop()
