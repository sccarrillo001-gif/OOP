import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("450x500")

class Queue:
    def __init__(self):
        self.element = []

    def enqueue(self, val):
        self.element.append(val)

class Stack:
    def __init__(self):
        self.element = []

    def push(self, q_obj):
        self.element.append(q_obj)

    def pop(self):
        if self.element:
            self.element.pop()

    def displayStack(self):
        if len(self.element) == 0:
            output_label.config(text="Stack is empty")
        else:
            result = "Queues in Stack:\n"
            for q in self.element:
                result = result + str(q.element) + "\n"
            output_label.config(text=result)


newQ = None
s1 = Stack()

def show(x):
    global newQ

    if x == "NewQueue":
        newQ = Queue()    
        output_label.config(text="New Queue created")

    elif x == "Enqueue":
        if newQ is None:
            output_label.config(text="Create a queue first")
            return

        val = valueTxt.get("1.0", "end-1c")
        valueTxt.delete("1.0", "end")

        if val != "":
            newQ.enqueue(val)   
            output_label.config(text="Added: " + val)
        else:
            output_label.config(text="Enter a value")

    elif x == "stack":
        if newQ is None:
            output_label.config(text="No queue to push")
            return

        s1.push(newQ)
        output_label.config(text="Queue added to Stack")
        newQ = None    

    elif x == "unstack":
        s1.pop()

    elif x == "Display":
        s1.displayStack()



valueTxt = Text(top, height=2, width=20)
valueTxt.place(x=130, y=50)

B1 = Button(top, text="NewQueue", width=10, height=2, command=lambda: show("NewQueue"))
B1.place(x=50, y=120)

B2 = Button(top, text="Enqueue", width=10, height=2, command=lambda: show("Enqueue"))
B2.place(x=150, y=120)

B3 = Button(top, text="Stack", width=10, height=2, command=lambda: show("stack"))
B3.place(x=250, y=120)

B4 = Button(top, text="Unstack", width=10, height=2, command=lambda: show("unstack"))
B4.place(x=100, y=180)

B5 = Button(top, text="Display", width=10, height=2, command=lambda: show("Display"))
B5.place(x=200, y=180)

output_label = Label(top, text="Welcome")
output_label.place(x=50, y=250)

top.mainloop()
