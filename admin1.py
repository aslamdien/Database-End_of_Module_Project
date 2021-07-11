from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


mydb = mysql.connector.connect(user = 'lifechoices', password = '@Lifechoices1234', host = '127.0.0.1', database = 'End_of_Module', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

mycursor.execute('Select * from register', 'Select * from next_of_kin')


root = Tk()
root.title("Admin Register Info")
root.geometry("1000x800")
root.config(bg ="#010101")

my_pic = PhotoImage(file = "Lifechoices-300x91.png")
background = Label(root, image = my_pic).place(x=350, y=10)
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

        self.treeView.place(x=150, y=120)

        #Sript rows into odd and evens
        self.treeView.tag_configure("odd", background = "grey")
        self.treeView.tag_configure("even", background = "green")

        # Frames
        self.frame1 = LabelFrame(master)
        self.frame1.place(x=30, y=430, width = 900, height = 175)

        # Labels
        self.namelab = Label(master, text = "Name:")
        self.namelab.place(x=50, y=440)

        self.surnamelab = Label(master, text = "Surname:")
        self.surnamelab.place(x=50, y=490)

        self.id_numberlab = Label(master, text = "ID Number:")
        self.id_numberlab.place(x=50, y=540)

        self.phone_numberlab = Label(master, text = "Phone Number:")
        self.phone_numberlab.place(x=300, y=440)

        self.passwordlab = Label(master, text = "Password:")
        self.passwordlab.place(x=335, y=490)

        self.next_of_kin_namelab = Label(master, text = "Next Of Kin Name:")
        self.next_of_kin_namelab.place(x= 600, y=440)

        self.next_of_kin_contactlab = Label(master, text = "Next Of Kin Contact:")
        self.next_of_kin_contactlab.place(x=600, y=490)

        name = StringVar()
        surname = StringVar()
        id = StringVar()
        phone = StringVar()
        password = StringVar()
        nok_name = StringVar()
        nok_contact = StringVar()

        #Entries
        self.nameEnt = Entry(master, textvariable = name)
        self.nameEnt.place(x=100, y=440)

        self.surnameEnt = Entry(master, textvariable = surname)
        self.surnameEnt.place(x=120, y=490)

        self.id_numberEnt = Entry(master, textvariable = id)
        self.id_numberEnt.place(x=130, y=540)

        self.phone_numberEnt = Entry(master, textvariable = phone)
        self.phone_numberEnt.place(x=410,y=440)

        self.passwordEnt = Entry(master, textvariable = password)
        self.passwordEnt.place(x=410, y=490)

        self.next_of_kin_nameEnt = Entry(master, textvariable = nok_name)
        self.next_of_kin_nameEnt.place(x=730,y=440 )

        self.next_of_kin_contactEnt = Entry(master, textvariable = nok_contact)
        self.next_of_kin_contactEnt.place(x=740, y =490)


        # Buttons
        self.addbtn = Button(master, text = "Add New Member", command = self.add)# Add records Button
        self.addbtn.place(x=50, y=640)

        self.deletebtn = Button(master, text = "Delete", command = self.delete)# Delete Button
        self.deletebtn.place(x=230, y=640)

        self.selectUpdateBtn = Button(master, text = "Select for Update", command = self.select)# Select for Update
        self.selectUpdateBtn.place(x=330, y=640)

        self.updateBTN = Button(master, text = "Update", command = self.update)# Update Button
        self.updateBTN.place(x = 330, y=680)
        self.updateBTN.config(state = "disabled")

        self.cancelbtn = Button(master, text = "CANCEL", command = self.cancel)# Cancel Button
        self.cancelbtn.place(x = 500, y =640)

        self.nextOfkin= Button(master, text = "View Next of Kin", command = self.nok)# View next of kin
        self.nextOfkin.place(x= 50, y= 720)

        self.viewLog = Button(master, text ="View LogIn AND LogOut Records", command = self.log)
        self.viewLog.place(x=200, y=720)


        count = 0
        for i in mycursor:
           #print(i)
           if count % 2 == 0:
               self.treeView.insert("", 'end', iid = count, values = (i[0], i[2], i[3], i[4], i[5], i[6]), tags = ("even",))
           else:
               self.treeView.insert("", 'end', iid = count, values = (i[0], i[2], i[3], i[4], i[5], i[6]), tags = ("odd",))
           count += 1



    # Add Function
    def add(self):
        self.nameEnt.get()
        self.surnameEnt.get()
        self.id_numberEnt.get()
        self.phone_numberEnt.get()
        self.next_of_kin_nameEnt.get()
        self.next_of_kin_contactEnt.get()
        self.passwordEnt.get()

        if self.nameEnt.get() == '' or self.surnameEnt.get() == '' or self.id_numberEnt.get() == '' or self.phone_numberEnt.get() == '' or self.next_of_kin_nameEnt.get() == '' or self.next_of_kin_contactEnt.get() == '' or self.passwordEnt.get() == '':
            messagebox.showerror("Error", "Please Fill Out All Information")
        elif len(self.id_numberEnt.get()) != 13:
            messagebox.showerror("Error", "Invalid ID Number")
        elif len(self.phone_numberEnt.get()) != 10:
            messagebox.showerror("Error", "Please Enter Valid Phone Number")
            self.phone_numberEnt.delete(0, END)
        elif len(self.next_of_kin_contactEnt.get()) != 10:
            messagebox.showerror("Error", "Please Enter Valid Next of Kin Number")
            self.next_of_kin_contactEnt.delete(0,END)

        else:
            mycursor.execute('INSERT INTO register (name, surname, id_number, phone_number, password) VALUES (%s, %s, %s, %s, %s)', (self.nameEnt.get(), self.surnameEnt.get(), self.id_numberEnt.get(), self.phone_numberEnt.get(), self.passwordEnt.get()))
            mycursor.execute('INSERT INTO next_of_kin (name, mobile_number, next_of_kin_of) VALUES (%s, %s, %s)',(self.next_of_kin_nameEnt.get(), self.next_of_kin_contactEnt.get(), self.nameEnt.get()))

            # New info insert
            self.treeView.insert("", 'end', text = "", values = (mycursor.lastrowid, self.nameEnt.get(), self.surnameEnt.get(), self.id_numberEnt.get(), self.id_numberEnt.get(), self.passwordEnt.get()))

            mydb.commit()
            messagebox.showinfo("Approved", "Registration Has Been Approved")

            self.nameEnt.delete(0,END)
            self.surnameEnt.delete(0,END)
            self.id_numberEnt.delete(0,END)
            self.phone_numberEnt.delete(0,END)
            self.passwordEnt.delete(0,END)
            self.next_of_kin_nameEnt.delete(0,END)
            self.next_of_kin_contactEnt.delete(0,END)

    # Delete Function
    def delete(self):
        x = self.treeView.selection()[0]
        id = self.treeView.item(x)['values'][0]
        del_query1 = "DELETE FROM register WHERE ID = %s"
        del_query2 = "DELETE FROM next_of_kin WHERE ID = %s"
        select_item = (id,)
        mycursor.execute(del_query1, select_item)
        mycursor.execute(del_query2, select_item)
        mydb.commit()

        self.treeView.delete(x)
        messagebox.showinfo("Delete", "Record Has Been, Deleted")

    def select(self):
        curItem = self.treeView.focus()
        values = self.treeView.item(curItem, "values")
        if curItem == '':
            messagebox.showerror("Error", "Please Choose A Record to Update")

        else:
           self.nameEnt.insert(0, values[1])
           self.surnameEnt.insert(0, values[2])
           self.id_numberEnt.insert(0, values[3])
           self.phone_numberEnt.insert(0, values[4])
           self.passwordEnt.insert(0, values[5])
           self.next_of_kin_nameEnt.config(state = "disabled")
           self.next_of_kin_contactEnt.config(state = "disabled")
           self.selectUpdateBtn.config(state = "disabled")
           self.updateBTN.config(state = "normal")

    def update(self):
        curItem = self.treeView.focus()
        values = self.treeView.item(curItem, "values")
        self.nameEnt.get()
        self.surnameEnt.get()
        self.id_numberEnt.get()
        self.phone_numberEnt.get()
        self.passwordEnt.get()
        self.treeView.item(curItem, values=(values[0], self.nameEnt.get(), self.surnameEnt.get(), self.id_numberEnt.get(), self.phone_numberEnt.get(), self.passwordEnt.get()))

        mycursor.execute(
            'UPDATE register SET name = %s, surname = %s, id_number = %s, phone_number = %s, password = %s WHERE ID = %s',
            (self.nameEnt.get(), self.surnameEnt.get(), self.id_numberEnt.get(), self.phone_numberEnt.get(), self.passwordEnt.get(), values[0])
        )
        mydb.commit()
        messagebox.showinfo("Updated", "Infomation Successfully Updated")
        self.nameEnt.delete(0,END)
        self.surnameEnt.delete(0,END)
        self.id_numberEnt.delete(0,END)
        self.phone_numberEnt.delete(0,END)
        self.passwordEnt.delete(0,END)
        self.next_of_kin_nameEnt.config(state = "normal")
        self.next_of_kin_contactEnt.config(state = "normal")
        self.selectUpdateBtn.config(state = "normal")
        self.updateBTN.config(state = "disabled")

    def cancel(self):
        self.nameEnt.delete(0,END)
        self.surnameEnt.delete(0,END)
        self.id_numberEnt.delete(0,END)
        self.phone_numberEnt.delete(0,END)
        self.passwordEnt.delete(0,END)
        self.next_of_kin_nameEnt.delete(0,END)
        self.next_of_kin_nameEnt.config(state="normal")
        self.next_of_kin_contactEnt.delete(0,END)
        self.next_of_kin_contactEnt.config(state = "normal")
        self.selectUpdateBtn.config(state = "normal")
        self.updateBTN.config(state = "disabled")

    def nok(self):
        root.destroy()
        import admin3

    def log(self):
        root.destroy()
        import admin2

x = admin(root)
root.mainloop()
