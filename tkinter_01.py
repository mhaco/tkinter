from tkinter import *

root = Tk()

topFrame = Frame(root)

topFrame.pack()

bottomFrame = Frame(root)

bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red", command="hello")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")

button1.pack()
button2.pack()
button3.pack()
button4.pack()

root.mainloop()

