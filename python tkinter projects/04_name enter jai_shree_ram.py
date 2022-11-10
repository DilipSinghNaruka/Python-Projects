from tkinter import *
import tkinter as tk
from tkinter import ttk

def func():
    x= var.get()
    print(x)
    lbl2.config(text=x)

ram = tk.Tk()
ram.title("Jai Shree Ram")
ram.config(bg="gray")
lbl =Label(ram,text="Jai Shree Ram ",bg="white",fg="orange",font=('Arial',30),)
lbl.place(x=500,y=100)
lbl =Label(ram,text="Type here what do you want to print here ",bg="white",fg="orange",font=('Arial',20))
lbl.place(x=500,y=200)
lbl2 =Label(ram,text="yes here print do you want ",bg="gray",fg="red",font=('Arial',25))
lbl2.place(x=500,y=500)

var =StringVar()
type_text = Entry(bd=6,font=('Arial',12),fg="white",bg="gray",textvariable=var)
type_text.place(x=500,y=300,width=200,heigh=40)
btn = Button(text='Press Here',bd=6,command=func)
btn.place(x=500,y=400,width=80,heigh=30)
ram.mainloop()