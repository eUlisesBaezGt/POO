from tkinter import *

class Window_2(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Window 2")
        label = Label(self, text="This is the window 2")
        label.pack()
