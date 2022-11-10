from tkinter import *
import tkinter as tk
from tkinter import Tk
import pyqrcode 
from pyqrcode import QRCode


ram = tk.Tk()
ram.title("QRCODE MAKER ")

text = Label(ram,text="paste your link here:-")
text.place(x=100,y=100)

a =StringVar()
type_ = Entry(ram,textvariable=a)
type_.place(x=250,y=100)

url = pyqrcode.create(a)
url.svg("myQR.svg",scale =8)

btn = Button(text="create",command=url)
btn.place(x=200,y=200)


ram.mainloop()
