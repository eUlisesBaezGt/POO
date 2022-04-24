from tkinter import *


class winB(Toplevel):
    def __init__(self, parent=None):
        super().__init__(master=parent)
        self.title = "winB"
        Label(self, text="winB", font=("Arial", 16), fg="blue", bg="white", width=30, height=2,
              relief="ridge", anchor="center", justify="center").pack()
