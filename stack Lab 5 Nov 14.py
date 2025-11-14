import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("400x400")
class Stack:
    def __init__(self):
        self.element = []

    def push(self):
        self.element.append((valueTxt.get(1.0, "end-1c")))
        valueTxt.delete(1.0, "end")

    def pop(self):
        if len(self.element) > 0:
            self.element.pop()
        else:
            output_label.config(text="Stack is empty")

    def displaystack(self):
        if len(self.element) == 0:
            output_label.config(text="Stack is empty")
        else:
            result = "Elements in Stack: "
            for i in self.element:
                result = result + i + ", "
            result = result
            output_label.config(text=result)


def show(x):
    try:
        if x == "Stack":
            s1.push()
        elif x == "Unstack":
            s1.pop()
        elif x == "Display":
            s1.displaystack()
    except Exception as e:
        output_label.config(text="Error")


valueTxt = Text(top, height=2, width=20)
valueTxt.place(x=130, y=50)

B1 = Button(top, text="Stack", width=10, height=2, command=lambda: show("Stack"))
B1.place(x=60, y=120)

B2 = Button(top, text="Unstack", width=10, height=2, command=lambda: show("Unstack"))
B2.place(x=160, y=120)

B3 = Button(top, text="Display", width=10, height=2, command=lambda: show("Display"))
B3.place(x=260, y=120)

output_label = Label(top, text="welcome")
output_label.place(x=70, y=200)

s1 = Stack()

top.mainloop()