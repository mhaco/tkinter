from tkinter import *
import sqlite3
rout= Tk()
rout.geometry('500x500')

Fullname=StringVar()
Email=StringVar
var= IntVar
c=StringVar()
var1= IntVar()

def database():
    name1=Fullname.get()
    email=Email.get()
    gender=var.get()
    country=c.get()
    prog=var.get()
    conn= sqlite3.connect('Form.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('Create table if not exists student (Fullname Text, Email Text, Gender Text, Programming Text)')
    cursor.execute('Insert into student(Fullname,Email,Country,Programming) Values(?,?,?,?,?)', (name1,email,gender,country,prog,))
    conn.commit()


label_0= Label(rout, text="Registration form", width=20, font=("bold",20))
label_0.place(x=90,y=53)

label_1 = Label(rout, text="Full name", width=20, font=("bold",10))
label_1.place(x=80,y=130)

entry_1 = Entry(rout, textvar=Fullname)
entry_1.place(x=240,y=130)

label_2=Label(rout, text="Email",width=20,font=("bold",10))
label_2.place(x=68,y=180)

entry_2=Entry(rout, textvar=Email)
entry_2.place(x=240,y=180)

label_3=Label(rout, text="Gender", width=20, font=("bold", 10))
label_3.place(x=68,y=240)

Radiobutton(rout, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(rout, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)
#adiobutton(rooot, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)
label_4= Label(rout, text="country",width=20, font=("bold",10))
label_4.place(x=70,y=280)

list1 = ['Iran', 'Canada', 'UK', 'Russia','USA']

droplist=OptionMenu(rout,c,*list1)
droplist.config(width=15)
c.set('select your country')
droplist.place(x=240,y=280)

label_4 = Label(rout, text="Programming", width=20, font=("bold",10))
label_4.place(x=85,y=330)
var2= IntVar()
Checkbutton(rout, text="c++", var=var1).place(x=235,y=330)
Checkbutton(rout, text="python", var=var2).place(x=290,y=330)

Button(rout, text="submit", width=20, bg='brown',fg='white').place(x=180,y=380)


rout.mainloop()