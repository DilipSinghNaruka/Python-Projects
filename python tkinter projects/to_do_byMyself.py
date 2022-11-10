import tkinter 
from tkinter import Button, Entry, Label, Listbox, StringVar, Tk, ttk
from typing import List

 

def entery():
    seeta=ent.get()
    a.append(seeta)
    listUpdate()



def listUpdate():
    # clearList()
    for i in a:
        a.insert('end', i)


ram = Tk()
ram.title("To-do list")
lbl = Label(ram,text="To do List",font=("Arial",30)).pack()
lbl = Label(ram,text="Enter task below",font=("Arial",15)).pack()
var = StringVar()
ent = Entry(ram,textvariable=var).pack()
btn = Button(ram,text="Add task",command=entery).pack()
btn = Button(ram,text="Delete").pack()
btn = Button(ram,text="Delete all").pack()
btn = Button(ram,text="Exit").pack()
a = Listbox(ram).pack()

ram.mainloop()