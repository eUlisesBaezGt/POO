from tkinter import *


class winA(Toplevel):
    def __init__(self, parent=None):
        super().__init__(master=parent)
        self.title = "winA"
        Label(self, text="winA", font=("Arial", 16), fg="red", bg="white", width=30, height=2,
              relief="ridge", anchor="center", justify="center").pack()