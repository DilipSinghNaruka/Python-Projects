from tkinter import *
from tkinter import ttk
import pyshorteners as ps
import pyperclip 

ram = Tk()
ram.title("Url Shotner")

def shortner():
    n = str(s.get())
    k = ps.Shortener()
    m = k.tinyul.short(n)
    global r 
    r.set(str(m))

def copy_to_clipboard():
    pyperclip.copy(r.get())
    



title = Label(ram,text="This is Url Shotner",font=("Arial",30,"bold"))
title.place(x=370,y=0)


enterlink = Label(ram,text="Paste Your Link here:-",font=("Arial",15,))
enterlink.place(x=0,y=100)

s = StringVar()
enterlink_entry = Entry(ram,bd=5,textvariable=s).place(x=250,y=100,height=30,width=300)

enterlink_btn = Button(ram,text="Press it for shotner",command=shortner).place(x=350,y=150)


enterlink_result = Label(ram,text="shotened URL:- ",font=("Arial",15,))
enterlink_result.place(x=59,y=200)

r = StringVar()
enterlink_entry = Entry(ram,bd=5,textvariable=r).place(x=300,y=200,height=30,width=200)

enterlink_entry_btn = Button(ram,text="Copy This link",command=copy_to_clipboard).place(x=350,y=250)

ram.mainloop()