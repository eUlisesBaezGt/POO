import tkinter as tk

# Create a window
root = tk.Tk()
# root.geometry('605x560')
root.resizable(False, False)
root.title("KA's Calculator")

flag = False


def key_down(event):
    global flag
    if not flag:
        if event.char.isdigit():
            click(event.char)
        elif event.char == ".":
            click(".")
        elif event.char == "=":
            equal()
        elif event.char == "c" or event.char == "C":
            clear()
        elif event.char == "+":
            click("+")
        elif event.char == "-":
            click("-")
        elif event.char == "*":
            click("*")
        elif event.char == "/":
            click("/")
        elif event.char == '\r':
            equal()
        else:
            print("you pressed: " + event.char)
        flag = True


def key_up(event):
    global flag
    if flag:
        flag = False


# root.bind(<KeyPress-Return>, lambda event: button_click(event))
root.bind('<KeyPress>', key_down)
root.bind('<KeyRelease>', key_up)


# create a space for results
result = tk.StringVar()
result.set("0")
result_label = tk.Label(root, textvariable=result, anchor="e", justify="right")
result_label.configure(bg="orange", fg="black", font=("Arial", 20, "bold"), width=40, height=2)
result_label.grid(row=0, column=0, columnspan=6)


# cget command returns the complete value
def click(param):
    param = str(param)
    global result
    if result.get() == "0":
        result.set(param)
    else:
        result.set(result.get() + param)


def clear():
    result.set("0")


def equal():
    global result
    result.set(eval(result.get()))


# create Button for each number
button_1 = tk.Button(root, text="1", padx=40, pady=26, command=lambda: click(1))
button_1.configure(bg="green", fg="white", font=("Arial", 20, "bold"), width=2, height=2)
button_1.grid(row=3, column=0)
button_2 = tk.Button(root, text="2", padx=40, pady=26, command=lambda: click(2))
button_2.configure(bg="green", fg="white", font=("Arial", 20, "bold"), width=2, height=2)
button_2.grid(row=3, column=1)
button_3 = tk.Button(root, text="3", padx=40, pady=26, command=lambda: click(3))
button_3.configure(bg="green", fg="white", font=("Arial", 20, "bold"), width=2, height=2)
button_3.grid(row=3, column=2)
button_4 = tk.Button(root, text="4", padx=40, pady=26, command=lambda: click(4))
button_4.configure(bg="green", fg="white", font=("Arial", 20, "bold"), width=2, height=2)
button_4.grid(row=2, column=0)
button_5 = tk.Button(root, text="5", padx=40, pady=26, command=lambda: click(5))
button_5.configure(bg="green", fg="white", font=("Arial", 20, "bold"), width=2, height=2)
button_5.grid(row=2, column=1)
button_6 = tk.Button(root, text="6", padx=40, pady=26, command=lambda: click(6))
button_6.configure(bg="green", fg="white", font=("Arial", 20, "bold"), width=2, height=2)
button_6.grid(row=2, column=2)
button_7 = tk.Button(root, text="7", padx=40, pady=26, command=lambda: click(7))
button_7.configure(bg="green", fg="white", font=("Arial", 20, "bold"), width=2, height=2)
button_7.grid(row=1, column=0)
button_8 = tk.Button(root, text="8", padx=40, pady=26, command=lambda: click(8))
button_8.configure(bg="green", fg="white", font=("Arial", 20, "bold"), width=2, height=2)
button_8.grid(row=1, column=1)
button_9 = tk.Button(root, text="9", padx=40, pady=26, command=lambda: click(9))
button_9.configure(bg="green", fg="white", font=("Arial", 20, "bold"), width=2, height=2)
button_9.grid(row=1, column=2)
button_0 = tk.Button(root, text="0", padx=40, pady=26, command=lambda: click(0))
button_0.configure(bg="green", fg="white", font=("Arial", 20, "bold"), width=2, height=2)
button_0.grid(row=4, column=1)

# create Button for each operator
button_add = tk.Button(root, text="+", padx=40, pady=26, command=lambda: click("+"))
button_add.config(bg="red", fg="white", font=("Arial", 20, "bold"), width=2, height=2)
button_add.grid(row=1, column=3)
button_sub = tk.Button(root, text="-", padx=40, pady=26, command=lambda: click("-"))
button_sub.config(bg="red", fg="white", font=("Arial", 20, "bold"), width=2, height=2)
button_sub.grid(row=2, column=3)
button_mul = tk.Button(root, text="*", padx=40, pady=26, command=lambda: click("*"))
button_mul.config(bg="red", fg="white", font=("Arial", 20, "bold"), width=2, height=2)
button_mul.grid(row=3, column=3)
button_div = tk.Button(root, text="/", padx=40, pady=26, command=lambda: click("/"))
button_div.config(bg="red", fg="white", font=("Arial", 20, "bold"), width=2, height=2)
button_div.grid(row=4, column=3)
button_equal = tk.Button(root, text="=", padx=40, pady=26, command=lambda: equal())
button_equal.config(bg="blue", fg="white", font=("Arial", 20, "bold"), height=14, width=3)
button_equal.grid(row=1, column=5, rowspan=4)
button_clear = tk.Button(root, text="C", padx=40, pady=26, command=lambda: clear())
button_clear.config(bg="gray", fg="white", font=("Arial", 20, "bold"), width=2, height=2)
button_clear.grid(row=4, column=0)
button_dot = tk.Button(root, text=".", padx=40, pady=26, command=lambda: click("."))
button_dot.config(bg="gray", fg="white", font=("Arial", 20, "bold"), width=2, height=2)
button_dot.grid(row=4, column=2)

root.mainloop()
