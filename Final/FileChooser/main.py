import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

# from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Open File Dialog')
root.resizable(False, False)

process = tk.Tk()
process.title('Process')
process.resizable(False, False)
process.withdraw()


def close():
    global process, root
    process.destroy()
    root.deiconify()


def processwin(path):
    if path != '':
        with open(path, 'r') as f:
            text = f.read()
            print(text)
        root.withdraw()
        process.deiconify()
        ttk.Label(process, text=text).pack()
        process.protocol("WM_DELETE_WINDOW", close)


def select_file():
    filetypes = (('Text files', '*.txt'), ('All files', '*.*'))
    path = fd.askopenfilename(title='Choose file', initialdir='./', filetypes=filetypes)
    processwin(path)
    # showinfo(title='Selected File', message=path)


open_button = ttk.Button(root, text='Open a File', command=select_file)

open_button.pack(expand=True)
root.mainloop()
