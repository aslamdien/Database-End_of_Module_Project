import datetime
import pdb
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
        self.treeView["columns"] = ("ID","Date", "Name", "Surname","Reason", "Loged In", "Loged Out", "Loged")
        # Name and Size Our Columns
        self.treeView.column("#0", width=0, minwidth = 100, stretch = NO)
        self.treeView.column("ID", anchor=CENTER, width = 40)
        self.treeView.column("Date", anchor = CENTER, width = 100)
        self.treeView.column("Name", anchor=W, width=100)
        self.treeView.column("Surname", anchor=W, width=100)
        self.treeView.column("Reason", anchor=CENTER, width=180)
        self.treeView.column("Loged In", anchor=CENTER, width=110)  # phantom column
        self.treeView.column("Loged Out", anchor=CENTER, width=110)
        self.treeView.column("Loged", anchor=CENTER, width=120)

        # Create Headings
        # self.tree_view_admin.heading("#0", text="", anchor=CENTER)
        self.treeView.heading("ID", text = "ID", anchor = CENTER)
        self.treeView.heading("Date", text = "Date", anchor=CENTER)
        self.treeView.heading("Name", text="Name", anchor=CENTER)
        self.treeView.heading("Surname", text="Surname", anchor=CENTER)
        self.treeView.heading("Reason", text = "Reason For Attendance",anchor=CENTER)
        self.treeView.heading("Loged In", text="Loged In", anchor=CENTER)
        self.treeView.heading("Loged Out", text="Loged Out", anchor=CENTER)
        self.treeView.heading("Loged",text = "Log In or Out", anchor=CENTER)


        self.treeView.place(x=70, y=120)

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
        in_or_out = StringVar()
        reason = StringVar()

        #Entries
        self.date = Entry(master, textvariable = date)
        self.name = Entry(master, textvariable = name)
        self.surname = Entry(master, textvariable = surname)
        self.log1 = Entry(master, textvariable = loggin)
        self.log2 = Entry(master, textvariable = loggOut)
        self.inORout= Entry(master, textvariable = in_or_out)
        self.reason = Entry(master, textvariable = reason)


        self.log_InEnt = Entry(master, textvariable = log_in)
        self.log_InEnt.place(x=200, y=440)
        self.log_InEnt.config(width = 2)

        self.log_OutEnt = Entry(master, textvariable = log_out)
        self.log_OutEnt.place(x=200, y=490)
        self.log_OutEnt.config(width = 2)


        #Button
        self.checkbtn = Button(master, text = "Check Loged In and Loged Out ", command = self.check)
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
               self.treeView.insert("", 'end', iid = count, values = (i[0], i[1], i[2], i[3],i[7], i[9], i[10],i[11]), tags = ("even",))
           else:
               self.treeView.insert("", 'end', iid = count, values = (i[0], i[1], i[2], i[3],i[7], i[9], i[10], i[11]), tags = ("odd",))
           count += 1
        mydb.commit()



    def logIn(self):
        curItem = self.treeView.focus()
        values = self.treeView.item(curItem, "values")
        if curItem == '':
            messagebox.showerror("Error", "Please Select A Row To Log In")

        else:
            self.date.insert(0, date_now)
            self.name.insert(0, values[2])
            self.surname.insert(0, values[3])
            self.reason.insert(0, values[4])
            self.log1.insert(0, time_now)
            self.log2.insert(0, time_reset)
            self.inORout.insert(0, "Log In")
            self.treeView.item(curItem, values=(values[0], self.date.get(), self.name.get(), self.surname.get(),self.reason.get(), self.log1.get(), self.log2.get(), self.inORout.get()))

            mycursor.execute('UPDATE register SET date_of_entry = %s,loged_in = %s , loged_out = %s, in_or_out = %s WHERE ID = %s',
                             (self.date.get(),self.log1.get(), self.log2.get(), self.inORout.get(),values[0]))

            mydb.commit()
            messagebox.showinfo("Update", "Login Update Successful")
            self.date.delete(0, END)
            self.name.delete(0, END)
            self.surname.delete(0, END)
            self.log1.delete(0, END)
            self.log2.delete(0, END)
            self.reason.delete(0, END)
            self.inORout.delete(0, END)
            self.log_InEnt.config(state = "normal")
            self.log_InEnt.delete(0, END)
            self.log_OutEnt.config(state = "normal")
            self.log_OutEnt.delete(0, END)


    def logOut(self):
        curItem = self.treeView.focus()
        values = self.treeView.item(curItem, "values")
        if curItem == '':
            messagebox.showerror("Error", "Please Select A Row To Log Out")

        else:
            self.date.insert(0, values[1])
            self.name.insert(0, values[2])
            self.surname.insert(0, values[3])
            self.reason.insert(0, values[4])
            self.log1.insert(0, values[5])
            self.log2.insert(0, time_now)
            self.inORout.insert(0, "Log Out")
            self.treeView.item(curItem, values=(values[0], self.date.get(), self.name.get(), self.surname.get(),self.reason.get(), self.log1.get(), self.log2.get(), self.inORout.get()))

            mycursor.execute( 'UPDATE register SET loged_out = %s, in_or_out = %s WHERE ID = %s',
                              (self.log2.get(), self.inORout.get(), values[0]))


            mydb.commit()
            messagebox.showinfo("Update", "LogOut Update Successful")
            self.date.delete(0, END)
            self.name.delete(0, END)
            self.surname.delete(0, END)
            self.log1.delete(0, END)
            self.log2.delete(0, END)
            self.inORout.delete(0, END)
            self.reason.delete(0,END)
            self.log_InEnt.config(state = "normal")
            self.log_InEnt.delete(0, END)
            self.log_OutEnt.config(state = "normal")
            self.log_OutEnt.delete(0, END)

    def check(self):
        self.log_InEnt.config(state = "normal")
        self.log_InEnt.delete(0,END)
        self.log_OutEnt.config(state = "normal")
        self.log_OutEnt.delete(0, END)
        mydb = mysql.connector.connect(user = 'lifechoices', password = '@Lifechoices1234', host = '127.0.0.1', database = 'End_of_Module', auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()

        mycursor.execute('Select in_or_out, COUNT(*) FROM register GROUP BY in_or_out ORDER BY in_or_out')
        results = mycursor.fetchall()
        self.log_InEnt.insert(0, results[0][1])
        self.log_InEnt.config(state="readonly")
        self.log_OutEnt.insert(0,results[1][1])
        self.log_OutEnt.config(state = "readonly")


    def back(self):
        root.destroy()
        import admin1

x = admin_login(root)
root.mainloop()
