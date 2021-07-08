from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(user = 'lifechoices', password = '@Lifechoices1234', host = '127.0.0.1', database = 'End_of_Module', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()



root = Tk()
root.title("Admin Register Info")
root.geometry("1000x700")
class admin:
    def __init__(self, master):
        global mycursor
        # Style For Treeview
        self.style = ttk.Style()
        self.style.theme_use('clam')
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
        self.treeView["columns"] = ("ID","Name", "Surname", "ID Number", "Phone Number","Password")
        # Name and Size Our Columns
        self.treeView.column("#0", width=0, minwidth = 100, stretch = NO)
        self.treeView.column("ID", anchor=CENTER, width = 40)

        self.treeView.column("Name", anchor=W, width=100)
        self.treeView.column("Surname", anchor=W, width=100)
        self.treeView.column("ID Number", anchor=W, width=150)  # phantom column
        self.treeView.column("Phone Number", anchor=W, width=150)
        self.treeView.column("Password", anchor=W, width=150)

        # Create Headings
        # self.tree_view_admin.heading("#0", text="", anchor=CENTER)
        self.treeView.heading("ID", text = "ID", anchor = CENTER)

        self.treeView.heading("Name", text="Name", anchor=CENTER)
        self.treeView.heading("Surname", text="Surname", anchor=CENTER)
        self.treeView.heading("ID Number", text="ID Number", anchor=CENTER)
        self.treeView.heading("Phone Number", text="Phone Number", anchor=CENTER)
        self.treeView.heading("Password", text="Password", anchor=CENTER)

        self.treeView.place(x=150, y=50)

        #Sript rows into odd and evens
        self.treeView.tag_configure("odd", background = "grey")
        self.treeView.tag_configure("even", background = "green")

        # Frames
        self.frame1 = LabelFrame(master)
        self.frame1.place(x=30, y=370, width = 900, height = 175)

        # Labels
        self.namelab = Label(master, text = "Name:")
        self.namelab.place(x=50, y=390)

        self.surnamelab = Label(master, text = "Surname:")
        self.surnamelab.place(x=50, y=440)

        self.id_numberlab = Label(master, text = "ID Number:")
        self.id_numberlab.place(x=50, y=490)

        self.phone_numberlab = Label(master, text = "Phone Number:")
        self.phone_numberlab.place(x=300, y=390)

        self.passwordlab = Label(master, text = "Password:")
        self.passwordlab.place(x=335, y=440)

        self.next_of_kin_namelab = Label(master, text = "Next Of Kin Name:")
        self.next_of_kin_namelab.place(x= 600, y=390)

        self.next_of_kin_contactlab = Label(master, text = "Next Of Kin Contact:")
        self.next_of_kin_contactlab.place(x=600, y=440)

        #Entries
        self.nameEnt = Entry(master)
        self.nameEnt.place(x=100, y=390)

        self.surnameEnt = Entry(master)
        self.surnameEnt.place(x=120, y=440)

        self.id_numberEnt = Entry(master)
        self.id_numberEnt.place(x=130, y=490)

        self.phone_numberEnt = Entry(master)
        self.phone_numberEnt.place(x=410,y=390)

        self.passwordEnt = Entry(master)
        self.passwordEnt.place(x=410, y=440)

        self.next_of_kin_nameEnt = Entry(master)
        self.next_of_kin_nameEnt.place(x=730,y=390 )

        self.next_of_kin_contactEnt = Entry(master)
        self.next_of_kin_contactEnt.place(x=740, y =440)

        #Buttons
        self.addbtn = Button(master, text = "Add New Member", command = self.add)
        self.addbtn.place(x=50, y=560)

        self.deletebtn = Button(master, text = "Delete", command = self.delete)
        self.deletebtn.place(x=200, y=560)

        xy = mycursor.execute('Select * from register')
        count = 0
        for i in mycursor:
           #print(i)
           if count % 2 == 0:
               self.treeView.insert("", 'end', iid = count, values = (i[0], i[2], i[3], i[4], i[5], i[6]), tags = ("even",))
           else:
               self.treeView.insert("", 'end', iid = count, values = (i[0], i[2], i[3], i[4], i[5], i[6]), tags = ("odd",))
           count += 1
        mydb.commit()


    def add(self):
        global mycursor, count
        self.nameEnt.get()
        self.surnameEnt.get()
        self.id_numberEnt.get()
        self.phone_numberEnt.get()
        self.next_of_kin_nameEnt.get()
        self.next_of_kin_contactEnt.get()
        self.passwordEnt.get()

        for i in mycursor:
            self.treeView.insert("", 'end', iid = count, values = (i[0], self.nameEnt.get(), self.surnameEnt.get(), self.id_numberEnt.get(), self.phone_numberEnt.get(), self.passwordEnt.get()))
            count += 1

        if self.nameEnt.get() == '' or self.surnameEnt.get() == '' or self.id_numberEnt.get() == '' or self.phone_numberEnt.get() == '' or self.next_of_kin_nameEnt.get() == '' or self.next_of_kin_contactEnt.get() == '' or self.passwordEnt.get() == '':
            messagebox.showerror("Error", "Please Fill Out All Information")

        else:
            mycursor = mydb.cursor()
            insert1 = (
                "INSERT INTO register (name, surname, id_number, phone_number, password) VALUES (%s, %s, %s, %s, %s)"
            )
            val1 = (self.nameEnt.get(), self.surnameEnt.get(), self.id_numberEnt.get(), self.phone_numberEnt.get(), self.passwordEnt.get())

            insert2 = (
                "INSERT INTO next_of_kin (name, mobile_number, next_of_kin_of) VALUES (%s, %s, %s)"
            )
            val2 = (self.next_of_kin_nameEnt.get(), self.next_of_kin_contactEnt.get(), self.nameEnt.get())

            mycursor.execute(insert1, val1)
            mycursor.execute(insert2, val2)

            mydb.commit()
            messagebox.showinfo("Approved", "Registration Has Been Approved")

        for i in mycursor:
            self.treeView.insert("", 'end', iid = count, values = (i[0], self.nameEnt.get(), self.surnameEnt.get(), self.id_numberEnt.get(), self.phone_numberEnt.get(), self.passwordEnt.get()))
            count += 1

        self.nameEnt.delete(0,END)
        self.surnameEnt.delete(0,END)
        self.id_numberEnt.delete(0,END)
        self.phone_numberEnt.delete(0,END)
        self.passwordEnt.delete(0,END)
        self.next_of_kin_nameEnt.delete(0,END)
        self.next_of_kin_contactEnt.delete(0,END)

    def delete(self):
        x = self.treeView.selection()[0]
        self.treeView.delete(x)


x = admin(root)
root.mainloop()
