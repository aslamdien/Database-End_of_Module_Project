
from tkinter import *
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(user = 'lifechoices', password = '@Lifechoices1234', host = '127.0.0.1', database = 'End_of_Module', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

root = Tk()
root.title("Register")
root.geometry("600x600")
root.config(bg = "white")

def admin_page(event):
    root.destroy()
    import admin1

root.bind("<Control-a>", admin_page)

class register:
    def __init__(self, master):
        self.subheading = Label(root, text = "Your Details", font = "DejaVuSarif 15")
        self.subheading.place(x=240, y=10)

        self.fisrt_namelab = Label(master, text = "PLease Enter First Name:")
        self.fisrt_namelab.place(x = 110, y = 50)
        self.fisrt_nameEnt = Entry(master)
        self.fisrt_nameEnt.place(x=280, y=50)

        self.last_namelab = Label(master, text = "Please Enter Last Name:")
        self.last_namelab.place(x = 110, y = 80)
        self.last_nameEnt = Entry(master)
        self.last_nameEnt.place(x=280, y=80)

        self.id_numberlab = Label(master, text = "Please Enter ID Number:")
        self.id_numberlab.place(x=110, y=130)
        self.id_numberEnt = Entry(master)
        self.id_numberEnt.place(x=280, y=130)

        self.phone_numberlab = Label(master, text= "Please Enter Phone Number:")
        self.phone_numberlab.place(x=80, y=180)
        self.phone_numberEnt = Entry(master)
        self.phone_numberEnt.place(x=280, y=180)

        self.next_of_kin_heading = Label(master, text="Next Of Kin Contact Details", font = "DejaVuSarif 15")
        self.next_of_kin_heading.place(x=180, y=230)

        self.next_of_kin_namelab = Label(master, text = "Next of Kin`s Name:")
        self.next_of_kin_namelab.place(x=130, y=270)
        self.next_of_kin_nameEnt = Entry(root)
        self.next_of_kin_nameEnt.place(x=280, y=270)

        self.next_of_kin_contactlab = Label(master, text = "Next of Kin`s Mobile Number:")
        self.next_of_kin_contactlab.place(x=75, y=300)
        self.next_of_kin_contactEnt = Entry(master)
        self.next_of_kin_contactEnt.place(x=280, y=300)

        self.passwordHeading = Label(master, text = "Create Password", font = "DejaVuSarif 15")
        self.passwordHeading.place(x=220, y=350)

        self.passwordlab = Label(master, text = "Please Enter A Password:")
        self.passwordlab.place(x=110, y=390)
        self.passwordEnt = Entry(master, show = "*")
        self.passwordEnt.place(x=280, y=390)

        self.confirmLab = Label(master, text = "Confirm Your Password:")
        self.confirmLab.place(x=110, y=420)
        self.confirmEnt = Entry(master, show = "*")
        self.confirmEnt.place(x=280, y=420)

        self.registerbtn = Button(master, text = "Register", command = self.register)
        self.registerbtn.place(x=100, y=500)

        self.clearbtn = Button(master, text="Clear")
        self.clearbtn.place(x=200, y=500)

        self.showpass = Button(master, text = "Show Password", command = self.show)
        self.showpass.place(x=280, y=450)

    def register(self):
        self.fisrt_nameEnt.get()
        self.last_nameEnt.get()
        self.id_numberEnt.get()
        self.phone_numberEnt.get()
        self.next_of_kin_nameEnt.get()
        self.next_of_kin_contactEnt.get()
        self.passwordEnt.get()
        self.confirmEnt.get()

        if self.fisrt_nameEnt.get() == '' or self.last_nameEnt.get() == '' or self.id_numberEnt.get() == '' or self.phone_numberEnt.get() == '' or self.next_of_kin_nameEnt.get() == '' or self.next_of_kin_contactEnt.get() == '' or self.passwordEnt.get() == '' or self.confirmEnt.get() == '':
            messagebox.showerror("Error", "Please Fill Out All Information")
        elif len(self.id_numberEnt.get()) != 13:
            messagebox.showerror("Error", "Invalid ID Number")
        elif len(self.phone_numberEnt.get()) != 10:
            messagebox.showerror("Error", "Please Enter Valid Phone Number")
            self.phone_numberEnt.delete(0, END)
        elif len(self.next_of_kin_contactEnt.get()) != 10:
            messagebox.showerror("Error", "Please Enter Valid Next of Kin Number")
            self.next_of_kin_contactEnt.delete(0,END)
        elif self.confirmEnt.get() != self.passwordEnt.get():
            messagebox.showerror("Error", "Password Do Not Match!")

        else:
            mycursor = mydb.cursor()
            insert1 = (
                "INSERT INTO register (name, surname, id_number, phone_number, password) VALUES (%s, %s, %s, %s, %s)"
            )
            val1 = (self.fisrt_nameEnt.get(), self.last_nameEnt.get(), self.id_numberEnt.get(), self.phone_numberEnt.get(), self.confirmEnt.get())

            insert2 = (
                "INSERT INTO next_of_kin (name, mobile_number) VALUES (%s, %s)"
            )
            val2 = (self.next_of_kin_nameEnt.get(), self.next_of_kin_contactEnt.get())

            try:
                mycursor.execute(insert1, val1)
                mycursor.execute(insert2, val2)

                mydb.commit()
                messagebox.showinfo("Approved", "Registration Has Been Approved")
                root.destroy()
                import Login
            except:
                mycursor.execute('Select * from register')
                mycursor.execute('Select * from next_of_kin')




    def show(self):
        self.passwordEnt.config(show = '')
        self.confirmEnt.config(show = '')

x = register(root)
root.mainloop()
