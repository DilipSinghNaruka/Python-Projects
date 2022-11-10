from tkinter import *
import tkinter as tk
from tkinter import ttk
import os


ram = tk.Tk()
def shutdown():
     return os.system("shutdown /s /t 1") 
    
def out():
    return exit()
   

btn = Button(text='shutdown',command=shutdown)
btn.place(x=100,y=100)
btn2 = Button(text='no-shutdown',command=out)
btn2.place(x=200,y=100)
ram.mainloop()