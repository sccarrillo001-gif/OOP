import tkinter as tk
from tkinter import *
top = Tk()
top.geometry("500x500")

answer = Text(width=55, height=2)
answer.place(x=100, y=100)
class Queue:
    def __init__(self):
        self.element = []

    def enqueue(self):
        x = valuetxt.get(1.0, "end-1c")
        self.element.append(x)

    def dequeue(self):
        self.element.remove(0)

    def displayQueue(self):
        print("Elements in queue:")
        for i in self.element:
            print(i)

def show(x): #myFunction
        try:
            if x == "e":
                q1.enqueue()
            elif x == "d":
                q1.dequeue()
            elif x == "ds":
                q1.display()

            else:
        answer.insert(tk.INSERT, x)

    except:
        answer.delete(1.0, END)
                answer.insert(tk.INSERT, "Invalid Expression")


#Main Code
q1 = Queue()
q2 = Queue()



valuetxt = Button(top, text="enqueue", width=10, height=5, command=lambda: show("e"))
valuetxt.place(x=200, y=150)

dequeue = Button(top, text="dequeue", width=10, height=5, command=lambda: show("de"))
dequeue.place(x=400, y=150)

display = Button(top, text="display", width=10, height=5, command=lambda: show("ds"))
display.place(x=400, y=150)

top.mainloop()