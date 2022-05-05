import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

from Files import *


def close_process2():
    global process, root
    process2.destroy()
    root.deiconify()


def processwin():
    path = "analisis.txt"
    global root, process
    with open(path, 'r') as f:
        text = f.read()
    root.withdraw()
    process.configure(background='green')
    process.deiconify()
    ttk.Label(process, text=text).pack()
    process.protocol("WM_DELETE_WINDOW", processwin2)


def processwin2():
    path = "currency_amount.txt"
    global process2, process
    with open(path, 'r') as f:
        text = f.read()
    process.destroy()
    process2.deiconify()
    ttk.Label(process2, text=text).pack()
    process2.protocol("WM_DELETE_WINDOW", close_process2)


def select_file():
    global root
    filetypes = (('Text files', '*.txt'), ('All files', '*.*'))
    path = fd.askopenfilename(title='Choose file', initialdir='./', filetypes=filetypes)
    p = ttk.Label(root, text=path).grid(row=1, column=0)
    fn = path.split('/')[-1]
    ttk.Label(root, text=fn).grid(row=2, column=0)
    cont = ttk.Button(root, text='Continue to results', command=processwin).grid(row=0, column=0)


if __name__ == '__main__':
    read_file()
    print_analysis()
    print_currency_amount()

    # ------------------------------------------------------------------------------------------------------
    root = tk.Tk()
    root.title('Analisis de archivo bancario GUI')
    root.geometry('450x300')
    root.resizable(False, False)
    root.configure(background='blue')
    open_button = ttk.Button(root, text='Open a File', command=select_file).grid(row=0, column=0)

    process = tk.Tk()
    process.title('Analisis')
    process.resizable(False, False)
    process.withdraw()

    process2 = tk.Tk()
    process2.title('Currency Amount')
    process2.resizable(False, False)
    process2.configure(background='yellow')
    process2.withdraw()

    root.mainloop()
