import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("400x400")

class Queue:
    def __init__(self):
        self.element = []

    def enqueue(self):
        val = valueTxt.get(1.0, "end-1c")
        if val:
            self.element.append(val)
            valueTxt.delete("1.0", "end")
            output_label.config(text="Added: " + val)

        else:
            output_label.config(text="Enter a value")

    def dequeue(self):
        if self.element:
            removed = self.element.pop(0)

        else:
            output_label.config(text="Queue is empty")

    def displayQueue(self):
        if not self.element:
            output_label.config(text="Queue is empty")
        else:
            result = "Elements in Queue: "
        for i in self.element:
            result += i + ", "
        result = result[:-2]
        output_label.config(text=result)


def show(x):
    try:
        if x == "CreateQ":
            q1.enqueue()
        elif x == "Dequeue":
            q1.dequeue()
        elif x == "Display":
            q1.displayQueue()
    except Exception as e:
        output_label.config(text="Error")


valueTxt = Text(top, height=2, width=20)
valueTxt.place(x=130, y=50)

B1 = Button(top, text="CreateQ", width=10, height=2, command=lambda: show("CreateQ"))
B1.place(x=60, y=120)

B2 = Button(top, text="Dequeue", width=10, height=2, command=lambda: show("Dequeue"))
B2.place(x=160, y=120)

B3 = Button(top, text="Display", width=10, height=2, command=lambda: show("Display"))
B3.place(x=260, y=120)

output_label = Label(top, text="Queue: []")
output_label.place(x=70, y=200)

q1 = Queue()



top.mainloop()
