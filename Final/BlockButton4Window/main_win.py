from tkinter import *
from winA import winA
from winB import winB


# 3 states of the button: normal (default), disabled (gray button/disabled), active (focused, pressed)

# Functions to disable/enable each button and to close the window

def crwina():
    global wa
    wa = winA()


def diswina():
    global wa
    btn_winA['state'] = 'disabled'
    # root.withdraw()
    wa.protocol("WM_DELETE_WINDOW", close_a)


def close_a():
    global wa
    btn_winA['state'] = 'normal'
    wa.destroy()
    # root.deiconify()


def crwinb():
    global wb
    wb = winB()


def diswinb():
    global wb
    btn_winB['state'] = 'disabled'
    # root.withdraw()
    wb.protocol("WM_DELETE_WINDOW", close_b)


def close_b():
    global wb
    btn_winB['state'] = 'normal'
    wb.destroy()
    # root.deiconify()


# Create a window
root = Tk()
root.resizable(False, False)
root.title("KA's BlockButton4Window")
wa = None
wb = None

# create the main label
Label(root, text="COMMAND WINDOW", font=("Arial", 16), fg="red", bg="white", width=30, height=2,
      relief="ridge", anchor="center", justify="center").grid(row=0, column=0, columnspan=2)

# create the buttons
btn_winA = Button(root, text="Window A", font=("Arial", 16), fg="red", bg="blue", width=30, height=2,
                  relief="ridge", anchor="center", justify="center",
                  command=lambda: [crwina(), diswina()])
btn_winA.grid(row=1, column=0, columnspan=2)

btn_winB = Button(root, text="Window B", font=("Arial", 16), fg="green", bg="yellow", width=30, height=2,
                  relief="ridge", anchor="center", justify="center",
                  command=lambda: [crwinb(), diswinb()])
btn_winB.grid(row=2, column=0, columnspan=2)

btn_exit = Button(root, text="Exit", font=("Arial", 16), fg="yellow", bg="red", width=30, height=2, relief="ridge",
                  anchor="center", justify="center", command=root.destroy)
btn_exit.grid(row=3, column=0, columnspan=2)

root.mainloop()

# root.withdraw() y root.deiconify() posibles para un caso tipo "no se puede hacer nada hasta regresar a la ventana
# principal de comandos y cerrar las demás"
