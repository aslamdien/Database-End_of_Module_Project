import mysql.connector
from tkinter import *
from tkinter import messagebox
from datetime import *

mydb = mysql.connector.connect(user = 'lifechoices', password = '@Lifechoices1234', host = '127.0.0.1', database = 'End_of_Module', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

mycursor.execute('Select * from register')

date_now = datetime.now().date().strftime("%Y-%m-%d")
time_now = datetime.now().time().strftime('%H:%M:%S')
time_reset = time().replace(hour=0,minute=0,second=0)

root = Tk()
root.title("Login Page")
root.geometry("500x300")
root.config(bg = "#4850c8")

my_pic = PhotoImage(file = "life.png")
background = Label(root, image = my_pic).place(x=100, y=10)

def admin_page(event):
    root.destroy()
    import admin1

root.bind("<Control-a>", admin_page)

class login:
    def __init__(self, master):
        self.usernamelab = Label(master, text = "Please Enter Your Name:")
        self.usernamelab.place(x=50, y=150)
        self.usernameEnt = Entry(master)
        self.usernameEnt.place(x=220, y=150)

        self.passwordlab = Label(master, text = "Please Enter Your Password:")
        self.passwordlab.place(x=30, y=200)
        self.passwordEnt = Entry(master)
        self.passwordEnt.place(x=220, y=200)

        self.loginbtn = Button(master, text = "Login", command = self.login)
        self.loginbtn.place(x=150, y=250)

        self.registerbtn = Button(master, text = "Register New User", command = self.register)
        self.registerbtn.place(x=250, y=250)

    def login(self):
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
            sql  = "UPDATE register SET date_of_entry = %s, loged_in = %s, loged_out = %s WHERE ID= %s"
            user_id = results[0][0]
            values = (date_now, time_now, time_reset, user_id)
            mycursor.execute(sql, values)
            mydb.commit()
            messagebox.showinfo("Loged In", "Login Successful! Enjoy Your Day")
            root.destroy()
            import logout
        else:
            messagebox.showerror("Error", "Login Unsuccessful")
            self.usernameEnt.delete(0,END)
            self.passwordEnt.delete(0,END)


    def register(self):
        root.destroy()
        import register


x = login(root)
root.mainloop()
