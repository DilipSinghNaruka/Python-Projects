from tkinter import *
from PIL import Image, ImageTk
ram = Tk()
# ram.maxsize(700,800)
# ram.minsize(700,800)
text = Label(text="Jai shree Ram",font=("Arial",15))
text.pack()
san = Label(text="sata yug\n")
san.pack()
krishna = Label(text="+ jai shree krishna ",font = ("Arial",13),)
krishna.pack()
radha = Label(text="+ radhe krishna",font = ("Arial",12))
radha.pack()




dilip = PhotoImage(file="screenshot (5).png")
lable = Label(image=dilip,)
lable.pack()
#
           #in stars code not running without any error 

#***** photo =PhotoImage(file="Screenshot (5).png")
# image = Image.open("WIN_20210713_12_18_39_Pro.jpg")
# photo = ImageTk.PhotoImage(image)
# krishna_lable = Label(Image=photo)
# krishna_lable.pack() ******     









ram.mainloop()