import datetime
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from datetime import *

mydb = mysql.connector.connect(user = 'lifechoices', password = '@Lifechoices1234', host = '127.0.0.1', database = 'End_of_Module', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

mycursor.execute('Select * from register')

date_now = datetime.now().date().strftime("%Y-%m-%d")
time_now = datetime.now().time().strftime('%H:%M:%S')
time_reset = time().replace(hour=0,minute=0,second=0)


root = Tk()
root.title("Admin Loged Info")
root.geometry("1000x800")
root.config(bg ="#010101")

my_pic = PhotoImage(file = "Lifechoices-300x91.png")
background = Label(root, image = my_pic).place(x=350, y=10)
class admin_login:
    def __init__(self, master):
        global mycursor
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
        self.treeView.heading("Date", text = "Date", anchor=CENTER)
        self.treeView.heading("Name", text="Name", anchor=CENTER)
        self.treeView.heading("Surname", text="Surname", anchor=CENTER)
        self.treeView.heading("Loged In", text="Loged In", anchor=CENTER)
        self.treeView.heading("Loged Out", text="Loged Out", anchor=CENTER)


        self.treeView.place(x=150, y=120)

        #Sript rows into odd and evens
        self.treeView.tag_configure("odd", background = "grey")
        self.treeView.tag_configure("even", background = "green")

        self.frame1 = LabelFrame(master)
        self.frame1.place(x=30, y=430, width = 900, height = 175)

        # Labels
        self.logInlab = Label(master, text = "Who is Loged in:")
        self.logInlab.place(x=50, y=440)

        self.logoutlab = Label(master, text = "Who Is Loged Out:")
        self.logoutlab.place(x=50, y=490)

        date = StringVar()
        name = StringVar()
        surname = StringVar()
        log_in = StringVar()
        log_out = StringVar()
        loggin = StringVar()
        loggOut = StringVar()

        #Entries
        self.date = Entry(master, textvariable = date)
        self.name = Entry(master, textvariable = name)
        self.surname = Entry(master, textvariable = surname)
        self.log1 = Entry(master, textvariable = loggin)
        self.log2 = Entry(master, textvariable = loggOut)


        self.log_InEnt = Entry(master, textvariable = log_in)
        self.log_InEnt.place(x=200, y=440)

        self.log_OutEnt = Entry(master, textvariable = log_out)
        self.log_OutEnt.place(x=200, y=490)


        #Button
        self.checkbtn = Button(master, text = "Check Loged In and Loged Out ")
        self.checkbtn.place(x=50, y=560)

        self.logInbtn = Button(master, text = "Log In", command = self.logIn)
        self.logInbtn.place(x= 300, y = 560)

        self.logOutBtn = Button(master, text = "Log out", command = self.logOut)
        self.logOutBtn.place(x=400, y=560)

        self.backbtn = Button(master, text = "Back", command = self.back)
        self.backbtn.place(x=550, y= 560)

        count = 0
        for i in mycursor:
           #print(i)
           if count % 2 == 0:
               self.treeView.insert("", 'end', iid = count, values = (i[0], i[1], i[2], i[3], i[8], i[9]), tags = ("even",))
           else:
               self.treeView.insert("", 'end', iid = count, values = (i[0], i[1], i[2], i[3], i[8], i[9]), tags = ("odd",))
           count += 1
        mydb.commit()



    def logIn(self):
        curItem = self.treeView.focus()
        values = self.treeView.item(curItem, "values")
        self.date.insert(0, date_now)
        self.name.insert(0, values[2])
        self.surname.insert(0, values[3])
        self.log1.insert(0, time_now)
        self.log2.insert(0, time_reset)
        self.treeView.item(curItem, values=(values[0], self.date.get(), self.name.get(), self.surname.get(), self.log1.get(), self.log2.get()))

        mycursor.execute('UPDATE register SET date_of_entry = %s,loged_in = %s , loged_out = %s WHERE ID = %s',
                         (self.date.get(),self.log1.get(), self.log2.get(),values[0]))

        mydb.commit()
        messagebox.showinfo("Update", "Login Update Successful")
        self.date.delete(0, END)
        self.name.delete(0, END)
        self.surname.delete(0, END)
        self.log1.delete(0, END)
        self.log2.delete(0, END)


    def logOut(self):
        curItem = self.treeView.focus()
        values = self.treeView.item(curItem, "values")
        self.date.insert(0, values[1])
        self.name.insert(0, values[2])
        self.surname.insert(0, values[3])
        self.log1.insert(0, values[4])
        self.log2.insert(0, time_now)
        self.treeView.item(curItem, values=(values[0], self.date.get(), self.name.get(), self.surname.get(), self.log1.get(), self.log2.get()))

        mycursor.execute( 'UPDATE register SET loged_out = %s WHERE ID = %s',
                          (self.log2.get(),values[0]))


        mydb.commit()
        messagebox.showinfo("Update", "LogOut Update Successful")
        self.date.delete(0, END)
        self.name.delete(0, END)
        self.surname.delete(0, END)
        self.log1.delete(0, END)
        self.log2.delete(0, END)

    def back(self):
        root.destroy()
        import admin1

x = admin_login(root)
root.mainloop()
