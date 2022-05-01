from tkinter import *
import pandas as pd
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

df = pd.read_csv("MuertesTotalesCOVID.csv")


class app(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Datos CSV")

        self.tree = ttk.Treeview(self)
        columns = list(df.columns)
        self.Combo = ttk.Combobox(self, values=list(df["Pais"].unique()), state="readonly")
        self.Combo.pack()
        self.Combo.bind("<<ComboboxSelected>>", self.select_currency)
        self.tree["columns"] = columns
        self.tree.pack(expand=TRUE, fill=BOTH)

        for i in columns:
            self.tree.column(i, anchor="w")
            self.tree.heading(i, text=i, anchor="w")

        for index, row in df.iterrows():
            self.tree.insert("", "end", text=index, values=list(row))

    def select_currency(self, event=None):
        self.tree.delete(*self.tree.get_children())
        for index, row in df.loc[df["Pais"].eq(self.Combo.get())].iterrows():
            self.tree.insert("", "end", text=index, values=list(row))
            self.showPlot(row[0])

    def showPlot(self, paisSeleccionado):

        plt.rcParams["figure.figsize"] = [120.00, 50]
        plt.rcParams["figure.autolayout"] = True
        columns = ["Fecha", paisSeleccionado]
        df = pd.read_csv("MuertesTotalesCOVIDPorFecha.csv", usecols=columns)

        root = Tk()

        figure = Figure(figsize=(10, 4), dpi=140)
        plot = figure.add_subplot(1, 1, 1)
        plot.set_title(paisSeleccionado, size=14)
        plot.set_xlabel('Fecha', size=8)
        plot.set_ylabel('Decesos', size=10)
        plot.plot(df["Fecha"], df[paisSeleccionado])
        canvas = FigureCanvasTkAgg(figure, root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0)


ws = app()
ws.mainloop()
