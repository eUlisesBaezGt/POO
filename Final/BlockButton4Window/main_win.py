from tkinter import *
from winA import winA
from winB import winB


# 3 states of the button: normal (default), disabled (gray button/disabled), active (focused, pressed)

# Functions to disable each button

def diswinA():
    btn_winA["state"] = DISABLED


def diswinB():
    btn_winB["state"] = DISABLED


# Create a window
root = Tk()
root.resizable(False, False)
root.title("KA's BlockButton4Window")

# create the main label
Label(root, text="COMMAND WINDOW", font=("Arial", 16), fg="red", bg="white", width=30, height=2,
         relief="ridge", anchor="center", justify="center").grid(row=0, column=0, columnspan=2)

# create the buttons
btn_winA = Button(root, text="Window A", font=("Arial", 16), fg="red", bg="blue", width=30, height=2,
                     relief="ridge", anchor="center", justify="center",
                     command=lambda: [winA(), diswinA()])
btn_winA.grid(row=1, column=0, columnspan=2)

btn_winB = Button(root, text="Window B", font=("Arial", 16), fg="green", bg="yellow", width=30, height=2,
                     relief="ridge", anchor="center", justify="center",
                     command=lambda: [winB(), diswinB()])
btn_winB.grid(row=2, column=0, columnspan=2)

btn_exit = Button(root, text="Exit", font=("Arial", 16), fg="yellow", bg="red", width=30, height=2, relief="ridge",
                     anchor="center", justify="center", command=root.destroy)
btn_exit.grid(row=3, column=0, columnspan=2)

root.mainloop()
