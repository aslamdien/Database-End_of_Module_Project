from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from datetime import *

mydb = mysql.connector.connect(user = 'lifechoices', password = '@Lifechoices1234', host = '127.0.0.1', database = 'End_of_Module', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

mycursor.execute('Select * from next_of_kin')

date_now = datetime.now().date().strftime("%Y-%m-%d")
time_now = datetime.now().time().strftime('%H:%M:%S')

root = Tk()
root.title("Admin: User Next of Kin")
root.geometry("800x700")
root.config(bg ="#010101")

my_pic = PhotoImage(file = "Lifechoices-300x91.png")
background = Label(root, image = my_pic).place(x=250, y=10)
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
        self.treeView["columns"] = ("ID","Name", "Mobile", "NOKO")
        # Name and Size Our Columns
        self.treeView.column("#0", width=0, minwidth = 100, stretch = NO)
        self.treeView.column("ID", anchor=CENTER, width = 40)
        self.treeView.column("Name", anchor =W, width = 100)
        self.treeView.column("Mobile", anchor=W, width=150)
        self.treeView.column("NOKO", anchor=W, width=200)



        # Create Headings
        # self.tree_view_admin.heading("#0", text="", anchor=CENTER)
        self.treeView.heading("ID", text = "ID", anchor = CENTER)
        self.treeView.heading("Name", text = "Name", anchor=CENTER)
        self.treeView.heading("Mobile", text="Mobile Number", anchor=CENTER)
        self.treeView.heading("NOKO", text="Is Next of KIn Of", anchor=CENTER)


        self.treeView.place(x=170, y=120)

        #Sript rows into odd and evens
        self.treeView.tag_configure("odd", background = "grey")
        self.treeView.tag_configure("even", background = "green")


        # Frames
        self.frame1 = LabelFrame(master)
        self.frame1.place(x=30, y=420, width = 400, height = 175)

        # Labels
        self.namelab = Label(master, text = "Name:")
        self.namelab.place(x=50, y=440)

        self.mobilelab = Label(master, text = "Mobile Number:")
        self.mobilelab.place(x=50, y=490)

        name = StringVar()
        mobile = StringVar()
        ntk = StringVar()


        #Entries
        self.nameEnt = Entry(master, textvariable = name)
        self.nameEnt.place(x=100, y=440)

        self.mobileEnt = Entry(master, textvariable = mobile)
        self.mobileEnt.place(x=160, y=490)

        self.en = Entry(master, textvariable = ntk)


        #Button
        self.selectUpdateBtn = Button(master, text = "Select for Update", command = self.select)# Select for Update
        self.selectUpdateBtn.place(x=450, y=440)

        self.updateBTN = Button(master, text = "Update", command = self.update)# Update Button
        self.updateBTN.place(x = 450, y=490)
        self.updateBTN.config(state = "disabled")

        self.cancelbtn = Button(master, text = "CANCEL", command = self.cancel)# Cancel Button
        self.cancelbtn.place(x = 450, y =540)

        self.backbtn = Button(master, text = "Back", command = self.back)
        self.backbtn.place(x=550, y= 540)

        count = 0
        for i in mycursor:
           #print(i)
           if count % 2 == 0:
               self.treeView.insert("", 'end', iid = count, values = (i[0], i[1], i[2], i[3]), tags = ("even",))
           else:
               self.treeView.insert("", 'end', iid = count, values = (i[0], i[1], i[2], i[3]), tags = ("odd",))
           count += 1
        mydb.commit()



    def select(self):
        curItem = self.treeView.focus()
        values = self.treeView.item(curItem, "values")
        if curItem == '':
            messagebox.showerror("Error", "Please Select A Row To Update")

        else:
            self.nameEnt.insert(0, values[1])
            self.mobileEnt.insert(0, values[2])
            self.en.insert(0, values[3])
            self.selectUpdateBtn.config(state = "disabled")
            self.updateBTN.config(state = "normal")

    def update(self):
        curItem = self.treeView.focus()
        values = self.treeView.item(curItem, "values")

        self.treeView.item(curItem, values=(values[0], self.nameEnt.get(), self.mobileEnt.get(), self.en.get()))

        mycursor.execute(
            'UPDATE next_of_kin SET name = %s, mobile_number = %s WHERE ID = %s',
            (self.nameEnt.get(), self.mobileEnt.get(), values[0])
        )
        mydb.commit()
        messagebox.showinfo("Update", "Successful")
        self.nameEnt.delete(0,END)
        self.mobileEnt.delete(0,END)
        self.en.delete(0,END)
        self.selectUpdateBtn.config(state = "normal")
        self.updateBTN.config(state = "disabled")

    def cancel(self):
        self.nameEnt.delete(0,END)
        self.mobileEnt.delete(0,END)
        self.selectUpdateBtn.config(state = "normal")
        self.updateBTN.config(state = "disabled")

    def back(self):
        root.destroy()
        import admin1

x = admin_login(root)
root.mainloop()
