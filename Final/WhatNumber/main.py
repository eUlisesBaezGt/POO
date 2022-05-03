import tkinter as tk


def odd_even():
    global result, o_e
    if int(result.get()) % 2 == 0:
        o_e.set("ODD/EVEN ---> NO/YES")
    else:
        o_e.set("ODD/EVEN ---> YES/NO")


def leap_year():
    global result, leap
    year = int(result.get())
    if (year % 400 == 0) and (year % 100 == 0):
        leap.set("LEAP ---> YES")
    elif (year % 4 == 0) and (year % 100 != 0):
        leap.set("LEAP ---> YES")
    else:
        leap.set("LEAP ---> NO")


def multiple_of():
    global result, multiple
    m = " "
    if int(result.get()) % 2 == 0:
        m += " TWO"
    if int(result.get()) % 3 == 0:
        m += " THREE"
    if int(result.get()) % 5 == 0:
        m += " FIVE"
    elif int(result.get()) % 7 == 0:
        m += " SEVEN"
    multiple.set("MULTIPLE OF ---> " + m)


def prime_number():
    global result, prime
    num = int(result.get())
    n_flag = False
    for number in range(2, num):
        if (num % number) == 0:
            n_flag = True
            break
    if n_flag:
        prime.set("PRIME ---> NO")
    else:
        prime.set("PRIME ---> YES")


def check():
    odd_even()
    leap_year()
    multiple_of()
    prime_number()


def op(param):
    global result
    if param == "+":
        act = int(result.get())
        new = act + 1
        if new < 0:
            result.set("0")
        else:
            result.set(str(new))
    elif param == "-":
        act = int(result.get())
        new = act - 1
        if new < 0:
            result.set("0")
        else:
            result.set(str(new))
    check()


def write(param):
    param = str(param)
    global result
    if result.get() == "0":
        result.set(param)
    else:
        result.set(result.get() + param)
    check()


root = tk.Tk()
root.resizable(False, False)
root.title("WHAT number?")

flag = False


def clear():
    result.set("0")


def erase():
    if len(result.get()) == 1:
        result.set("0")
    else:
        result.set(result.get()[:-1])
    check()


def key_down(event):
    global flag
    if not flag:
        if event.char.isdigit():
            write(event.char)
        elif event.char == "+":
            op("+")
        elif event.char == "-":
            op("-")
        elif event.char == '\r':
            check()
        elif event.char == '\b':
            erase()
        elif event.char == "c" or event.char == "C":
            clear()
        else:
            print("you pressed: " + event.char)
        flag = True


def key_up(event):
    global flag
    if flag:
        flag = False


root.bind('<KeyPress>', key_down)
root.bind('<KeyRelease>', key_up)

result = tk.StringVar()
result.set("0")
result_label = tk.Label(root, textvariable=result, anchor="e", justify="right")
result_label.configure(bg="orange", fg="black", font=("Arial", 20, "bold"), width=48, height=2)
result_label.grid(row=0, column=0, columnspan=6)

# add +1 button
button_add = tk.Button(root, text="+", padx=40, pady=26, command=lambda: op("+"))
button_add.config(bg="red", fg="white", font=("Arial", 20, "bold"), width=2, height=2)
button_add.grid(row=1, column=4)

# add -1 button
button_sub = tk.Button(root, text="-", padx=40, pady=26, command=lambda: op("-"))
button_sub.config(bg="red", fg="white", font=("Arial", 20, "bold"), width=2, height=2)
button_sub.grid(row=1, column=1)

# add odd/even label
o_e = tk.StringVar()
o_e.set("ODD/EVEN ---> NO/NO")
o_e_label = tk.Label(root, textvariable=o_e, anchor="e", justify="right")
o_e_label.configure(bg="green", fg="black", font=("Arial", 20, "bold"), width=48, height=2)
o_e_label.grid(row=2, column=0, columnspan=6)

# add leap year label
leap = tk.StringVar()
leap.set("LEAP ---> NO")
leap_label = tk.Label(root, textvariable=leap, anchor="e", justify="right")
leap_label.configure(bg="blue", fg="black", font=("Arial", 20, "bold"), width=48, height=2)
leap_label.grid(row=3, column=0, columnspan=6)

# add multiple label
multiple = tk.StringVar()
multiple.set("MULTIPLE OF ---> ONE ")
multiple_label = tk.Label(root, textvariable=multiple, anchor="e", justify="right")
multiple_label.configure(bg="pink", fg="black", font=("Arial", 20, "bold"), width=48, height=2)
multiple_label.grid(row=4, column=0, columnspan=6)

# add prime label
prime = tk.StringVar()
prime.set("PRIME ---> NO")
prime_label = tk.Label(root, textvariable=prime, anchor="e", justify="right")
prime_label.configure(bg="lightblue", fg="black", font=("Arial", 20, "bold"), width=48, height=2)
prime_label.grid(row=5, column=0, columnspan=6)

root.mainloop()
