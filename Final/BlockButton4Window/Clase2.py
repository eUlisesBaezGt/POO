from tkinter import *

class Window_1(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Window 1")
        label = Label(self, text="This is the window 1")
        label.pack()
