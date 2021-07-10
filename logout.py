import mysql.connector
from tkinter import *
from tkinter import messagebox
from datetime import *

mydb = mysql.connector.connect(user = 'lifechoices', password = '@Lifechoices1234', host = '127.0.0.1', database = 'End_of_Module', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

xy = mycursor.execute('Select * from register')

time_now = datetime.now().time().strftime('%H:%M:%S')

root = Tk()
root.title("LogOut Page")
root.geometry("500x300")
root.config(bg = "#4850c8")

my_pic = PhotoImage(file = "life.png")
background = Label(root, image = my_pic).place(x=100, y=10)

class logout:
    def __init__(self, master):
        self.usernamelab = Label(master, text = "Please Enter Your Name:")
        self.usernamelab.place(x=50, y=150)
        self.usernameEnt = Entry(master)
        self.usernameEnt.place(x=220, y=150)

        self.passwordlab = Label(master, text = "Please Enter Your Password:")
        self.passwordlab.place(x=30, y=200)
        self.passwordEnt = Entry(master)
        self.passwordEnt.place(x=220, y=200)

        self.loginbtn = Button(master, text = "Log Out", command = self.logout)
        self.loginbtn.place(x=150, y=250)

    def logout(self):
        if self.usernameEnt.get() == '' or self.passwordEnt.get() == '':
             messagebox.showerror("Error", "Please fill Out Information")

        mydb = mysql.connector.connect(user = 'lifechoices', password = '@Lifechoices1234', host = '127.0.0.1', database = 'End_of_Module', auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        sql = "SELECT * FROM register WHERE name=%s AND password=%s"
        values = (self.usernameEnt.get(), self.passwordEnt.get())
        mycursor.execute(sql, values)
        results = mycursor.fetchall()
        if len(results) > 0:
            mycursor = mydb.cursor()
            sql  = "UPDATE register SET loged_out = %s WHERE ID= %s"
            user_id = results[0][0]
            values = (time_now,user_id)
            mycursor.execute(sql, values)
            mydb.commit()
            messagebox.showinfo("Log Out Successful", "See You Soon")
            root.destroy()
            import Login
        else:
            messagebox.showerror("Error", "LogOut Unsuccessful")
            self.usernameEnt.delete(0,END)
            self.passwordEnt.delete(0,END)



x = logout(root)
root.mainloop()
