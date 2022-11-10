from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from random import randint

ram = Tk()
ram.title("Love Calculator")

def love():
    number = randint(0,100)
    showinfo("Love persancetage",f"loving %is {number}")

lbl = Label(ram,text="type first name:--")
lbl.place(x=10,y=10)
lbl = Label(ram,text="type second name:--")
lbl.place(x=10,y=50)

lbl1 = Entry()
lbl1.place(x=150,y=10)
lbl1 = Entry()
lbl1.place(x=150,y=52)

btn = Button(text="Press It",command=love)
btn.place(x=200, y=80)



ram.mainloop()