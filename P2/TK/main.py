from tkinter import *

window = Tk()

window.title("KA's app")
window.geometry('700x600')

label = Label(window, text="Kikin Academy")
label.pack(anchor=CENTER)
label.config(fg="gold", bg="black", font=("Verdana", 24))
label.grid(row=0, column=0, columnspan=2)


def clicked():
    label.configure(text="Button was clicked !!")


btn = Button(window, text="Click Me", command=clicked)
btn.grid(row=2, column=0, sticky="nsew", padx=50, pady=50)

btn2 = Button(window, text="#2 Click Me", command=clicked)
btn2.grid(row=2, column=1, sticky="nsew", padx=50, pady=50)

window.mainloop()
