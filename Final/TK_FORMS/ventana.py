import tkinter as tk
from tkinter import filedialog as fd


class Alumno:
    def __init__(self, nombre, edad):
        self.name = nombre
        self.age = edad


class App:
    def __init__(self, root):
        self.lista = []
        # setting title
        root.title("GUI FORMS")
        # # setting window size
        width = 739
        height = 656
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        label_name = tk.Label(root, fg="#333333", text="Name")
        label_name.place(x=30, y=40, width=70, height=25)

        label_age = tk.Label(root, fg="#333333", text="Age")
        label_age.place(x=30, y=110, width=70, height=25)

        self.txt_name = tk.StringVar()
        self.txt_name.set("")
        self.GLineEdit_Name = tk.Entry(root, borderwidth="1px", fg="#333333", textvariable=self.txt_name)
        self.GLineEdit_Name.place(x=160, y=40, width=70, height=25)

        self.txt_age = tk.StringVar()
        self.txt_age.set("")
        self.GLineEdit_Age = tk.Entry(root, borderwidth="1px", fg="#333333", textvariable=self.txt_age)
        self.GLineEdit_Age.place(x=160, y=110, width=70, height=25)

        button_add = tk.Button(root, bg="#efefef", justify="center", text="Add", command=self.Cbutton_add)
        button_add.place(x=70, y=190, width=70, height=25)

        button_update = tk.Button(root, bg="#efefef", justify="center", text="Update", command=self.Cbutton_update)
        button_update.place(x=230, y=190, width=70, height=25)

        button_delete = tk.Button(root, bg="#efefef", justify="center", text="Delete", command=self.Cbutton_delete)
        button_delete.place(x=80, y=470, width=70, height=25)

        button_export = tk.Button(root, bg="#efefef", justify="center", text="Export", command=self.Cbutton_export)
        button_export.place(x=250, y=470, width=70, height=25)

        button_import = tk.Button(root, bg="#efefef", justify="center", text="Import", command=self.Cbutton_import)
        button_import.place(x=410, y=470, width=70, height=25)

        self.GListBox_List = tk.Listbox(root, borderwidth="1px", fg="#333333")
        self.GListBox_List.place(x=50, y=240, width=263, height=200)

        scrollbar = tk.Scrollbar(self.GListBox_List)
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        scrollbar.config(command=self.GListBox_List.yview)

        self.GListBox_List.configure(yscrollcommand=scrollbar.set)

        self.GListBox_List.bind("<<ListboxSelect>>", self.itemSelect)

    def Cbutton_add(self):
        nombre = self.GLineEdit_Name.get()
        edad = self.GLineEdit_Age.get()
        if len(nombre) < 3 or not edad.isdigit():
            return
        alumno = Alumno(nombre, edad)
        self.lista.append(alumno)
        self.GListBox_List.insert(len(self.lista) - 1, (alumno.name + ' , ' + alumno.age))
        self.txt_name.set("")
        self.txt_age.set("")

    def Cbutton_update(self):
        index = self.last_selected
        nombre = self.GLineEdit_Name.get()
        edad = self.GLineEdit_Age.get()
        if len(nombre) < 3 or not edad.isdigit():
            return
        self.lista[index].name = nombre
        self.lista[index].age = edad
        self.GListBox_List.delete(index)
        self.GListBox_List.insert(index, (nombre + ' , ' + edad))

    def Cbutton_delete(self):
        for i in self.GListBox_List.curselection():
            del [self.lista[i]]
            self.GListBox_List.delete(i)

    def itemSelect(self, event):
        index = self.GListBox_List.curselection()
        if len(index) == 0:
            return
        index = index[0]
        self.last_selected = index
        alumno = self.lista[index]
        self.txt_name.set(alumno.name)
        self.txt_age.set(alumno.age)

    def Cbutton_export(self):
        with open('alumnos.csv', 'w') as f:
            for alumno in self.lista:
                f.write(alumno.name + ',' + alumno.age + '\n')
        with open('alumnos.txt', 'w') as f:
            for alumno in self.lista:
                f.write(alumno.name + ',' + alumno.age + '\n')

    def Cbutton_import(self):
        temp = []
        filetypes = (('Text files', '*.txt'), ('CSV files', '*.csv'), ('All files', '*.*'))
        path = fd.askopenfilename(title='Choose file', filetypes=filetypes)

        if path != '':
            with open(path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    name, age = line.split(',')
                    alumno = Alumno(name, age)
                    temp.append(alumno)
                self.lista = temp
                self.GListBox_List.delete(0, tk.END)
                for alumno in self.lista:
                    self.GListBox_List.insert(tk.END, (alumno.name + ' , ' + alumno.age))
