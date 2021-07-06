from tkinter import *
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(user = 'lifechoices', password = '@Lifechoices1234', host = '127.0.0.1', database = 'End_of_Module', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

root = Tk()
root.title("Register")
root.geometry("500x500")

subheading = Label(root, text = "Your Details", font = "DejaVuSarif 15")
subheading.place(x=180, y=10)

fisrt_namelab = Label(root, text = "PLease Enter First Name:")
fisrt_namelab.place(x = 50, y = 50)
fisrt_nameEnt = Entry(root)
fisrt_nameEnt.place(x=220, y=50)

last_namelab = Label(root, text = "Please Enter Last Name:")
last_namelab.place(x = 50, y = 80)
last_nameEnt = Entry(root)
last_nameEnt.place(x=220, y=80)

id_numberlab = Label(root, text = "Please Enter ID Number:")
id_numberlab.place(x=50, y=130)
id_numberEnt = Entry(root)
id_numberEnt.place(x=220, y=130)

phone_numberlab = Label(root, text= "Please Enter Phone Number:")
phone_numberlab.place(x=20, y=180)
phone_numberEnt = Entry(root)
phone_numberEnt.place(x=220, y=180)

next_of_kin_heading = Label(root, text="Next Of Kin Contact Details", font = "DejaVuSarif 15")
next_of_kin_heading.place(x=100, y=230)

next_of_kin_namelab = Label(root, text = "Next of Kin`s Name:")
next_of_kin_namelab.place(x=70, y=270)
next_of_kin_nameEnt = Entry(root)
next_of_kin_nameEnt.place(x=220, y=270)

next_of_kin_contactlab = Label(root, text = "Next of Kin`s Mobile Number:")
next_of_kin_contactlab.place(x=15, y=300)
next_of_kin_contactEnt = Entry(root)
next_of_kin_contactEnt.place(x=220, y=300)

def register():
    fisrt_nameEnt.get()
    last_nameEnt.get()
    id_numberEnt.get()
    phone_numberEnt.get()
    next_of_kin_nameEnt.get()
    next_of_kin_contactEnt.get()

    if fisrt_nameEnt.get() == '' or last_nameEnt.get() == '' or id_numberEnt.get() == '' or phone_numberEnt.get() == '' or next_of_kin_nameEnt.get() == '' or next_of_kin_contactEnt.get() == '':
        messagebox.showerror("Error", "Please Fill Out All Information")
    elif len(id_numberEnt.get()) != 13:
        messagebox.showerror("Error", "Invalid ID Number")
    elif len(phone_numberEnt.get()) != 10:
        messagebox.showerror("Error", "Please Enter Valid Phone Number")
        phone_numberEnt.delete(0, END)
    elif len(next_of_kin_contactEnt.get()) != 10:
        messagebox.showerror("Error", "Please Enter Valid Next of Kin Number")
        next_of_kin_contactEnt.delete(0,END)

    else:
        mycursor = mydb.cursor()
        insert1 = (
            "INSERT INTO register (name, surname, id_number, phone_number) VALUES (%s, %s, %s, %s)"
        )
        val1 = (fisrt_nameEnt.get(), last_nameEnt.get(), id_numberEnt.get(), phone_numberEnt.get())

        insert2 = (
            "INSERT INTO next_of_kin (name, mobile_number) VALUES (%s, %s)"
        )
        val2 = (next_of_kin_nameEnt.get(), next_of_kin_contactEnt.get())

        try:
            mycursor.execute(insert1, val1)
            mycursor.execute(insert2, val2)

            mydb.commit()
        except:
            mycursor.execute('Select * from register')
            mycursor.execute('Select * from next_of_kin')

registerbtn = Button(root, text = "Register", command = register)
registerbtn.place(x=100, y=400)

clearbtn = Button(root, text="Clear")
clearbtn.place(x=200, y=400)

root.mainloop()
