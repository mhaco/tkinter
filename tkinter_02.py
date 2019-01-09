from tkinter import *

rooot = Tk()
rooot.geometry('500x500')
rooot.title("Registration Form")

label_0 = Label(rooot, text="Registration form", width=20, font=("bold", 20),fg='green')
label_0.place(x=90, y=53)

label_1 = Label(rooot, text="Full name", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(rooot)
entry_1.place(x=240, y=130)

label_2 = Label(rooot, text="Email", width=20, font=("", 10))
label_2.place(x=68, y=180)

entry_2 = Entry(rooot)
entry_2.place(x=240, y=180)

label_3 = Label(rooot, text="gender", width=20, font=("", 10))
label_3.place(x=70, y=230)
#entry_3 = Entry(rooot)
#entry_3.place(x=240, y=240)
var = IntVar()
Radiobutton(rooot, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
Radiobutton(rooot, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)

label_4 = Label(rooot, text="country",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['Iran','USA','canada', 'India', 'China', 'Russia', 'Lobnan']
c=StringVar()
droplist=OptionMenu(rooot,c, *list1)
droplist.config(width=15)
c.set('select your country')
droplist.place(x=240, y=280)

label_4 = Label(rooot, text="Programming", width=20, font=("bold",10))
label_4.place(x=85, y=330)
var_1 = IntVar()
Checkbutton(rooot, text="c++",var=var_1).place(x=235, y=330)
var_2 = IntVar()
Checkbutton(rooot, text="python",var=var_2).place(x=290, y=330)

Button(rooot, text="submit", width=20, bg='brown',fg='white').place(x=180,y=380)


rooot.mainloop()