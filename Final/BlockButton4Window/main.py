from tkinter import *
from Clase import Window_2
from Clase2 import Window_1

master = Tk()

def disableButton1():
    btn_Window1["state"] = DISABLED

def disableButton2():
    btn_Window2["state"] = DISABLED

label = Label(master, text="This is the main window")
label.grid(column=0, row=0, rowspan=2)

btn_Window1 = Button(master, text="Click to open window 1", command=lambda: [Window_1(), disableButton1()])
btn_Window1.grid(column=0, row=2)

btn_Window2 = Button(master, text="Click to open window 2", command=lambda: [Window_2(), disableButton2()])
btn_Window2.grid(column=1, row=2)



master.mainloop()
