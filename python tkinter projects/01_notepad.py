from tkinter import *
from tkinter import messagebox
from tkinter import ttk,filedialog
# import csv
import os
win = Tk()
win.title("Dilip's Notepad")
# win.geometry('400x200')
textarea = Text(win,height=50,width=180)
a = 0
for i in range(a):
    textarea.insert(END,i)
textarea.pack(fill=Y)



#..............................................

def open():
    global name
    name= filedialog.askopenfilename(parent=win,initialdir=os.getcwd(),title="plese select a file")

#...............................................
    

def exit():
        win.destroy()

#------------------------------------------------------
def new():
    win.title("Untitled - Notepad")
    file = None
    textarea.delete(1.0,END)

#------------------------------------------------------
def save():
    global file 
    file = filedialog.asksaveasfilename(initialfile='Untitled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files","*.*"),
                                            ("Text Documents","*.txt")])

    #  file =open(file,"w")
    #  file.write(textarea.get(1.0,END))
    #  file.close()

#--------------------------------------------------------

def cut():
    global cutt
    cutt = textarea.event_generate("<<Cut>>")

#--------------------------------------------------

def copy():
    global copyy
    coppy = textarea.event_generate("<<Copy>>")

#..................................................

def paste():
    global pastee
    pastee = textarea.event_generate("<<Paste>>")

#...................................................

def info():
    global infoo
    infoo= messagebox.showinfo("Notepad by Dilip", "Create By Dilip Singh Naruka")

#....................................................

def pagesetup():
    global pagesetup
    pagesetup = messagebox.showinfo("Notepad by Dilip", "On The Process Please Wait...")

#...................................................

def print():
    global print
    print=messagebox.showinfo("Notepad by Dilip", "On The Process Please Wait...")

#..................................................

def undo():
    global undo
    undo =messagebox.showinfo("Notepad", "On The Process Please Wait...")

#......................................................





my_menu = Menu(win)
win.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File",menu=file_menu)

new = Menu(file_menu)
file_menu.add_cascade(label="New",command=new)
file_menu.add_separator()

new = Menu(file_menu)
file_menu.add_cascade(label="New Window",command=undo)
file_menu.add_separator()

new = Menu(file_menu)
file_menu.add_cascade(label="Open..",command=open)
file_menu.add_separator()

new = Menu(file_menu)
file_menu.add_cascade(label="Save",command=save)
file_menu.add_separator()

new = Menu(file_menu)
file_menu.add_cascade(label="Save As",)
file_menu.add_separator()

new = Menu(file_menu)
file_menu.add_cascade(label="Page Setup",command=pagesetup)
file_menu.add_separator()

new = Menu(file_menu)
file_menu.add_cascade(label="Print",command=print)
file_menu.add_separator()

new = Menu(file_menu)
file_menu.add_cascade(label="Exit",command=exit)
file_menu.add_separator()

file_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit",menu=file_menu)
file_menu.add_separator()

undo =Menu()
file_menu.add_cascade(label="Undo",command=undo)
file_menu.add_separator()

undo =Menu()
file_menu.add_cascade(label="Cut",command=cut)
file_menu.add_separator()

undo =Menu()
file_menu.add_cascade(label="Copy",command=copy)
file_menu.add_separator()

undo =Menu()
file_menu.add_cascade(label="Paste",command=paste)
file_menu.add_separator()

undo =Menu()
file_menu.add_cascade(label="Delete",command=undo)
file_menu.add_separator()

undo =Menu()
file_menu.add_cascade(label="Search With Bing",command=undo)
file_menu.add_separator()

undo =Menu()
file_menu.add_cascade(label="Find",command=undo)
file_menu.add_separator()

undo =Menu()
file_menu.add_cascade(label="Find next",command=undo)
file_menu.add_separator()

undo =Menu()
file_menu.add_cascade(label="Find Previous",command=undo)
file_menu.add_separator()

undo =Menu()
file_menu.add_cascade(label="replace..",command=undo)
file_menu.add_separator()

undo =Menu()
file_menu.add_cascade(label="Go To...",command=undo)
file_menu.add_separator()

undo =Menu()
file_menu.add_cascade(label="Select All",command=undo)
file_menu.add_separator()

undo =Menu()
file_menu.add_cascade(label="Time/Date ",command=undo)
file_menu.add_separator()



file_menu = Menu(my_menu)
my_menu.add_cascade(label="Formate",menu=file_menu)
file_menu.add_separator()

word_wrape = Menu()
file_menu.add_cascade(label="word wrape",command=undo)
file_menu.add_separator()

word_wrape = Menu()
file_menu.add_cascade(label="Font..",command=undo)
file_menu.add_separator()


file_menu = Menu(my_menu)
my_menu.add_cascade(label="View",menu=file_menu)
# file_menu.add_separator()

zoom = Menu()
file_menu.add_cascade(label="Zoom",menu=zoom)
# file_menu.add_separator()

zoom = Menu()
file_menu.add_cascade(label="Status Bar",command=undo)
# file_menu.add_separator()

zoom1=Menu()
zoom.add_cascade(label="Zoom In",command=undo)

zoom1=Menu()
zoom.add_cascade(label="Zoom Out",command=undo)


zoom1=Menu()
zoom.add_cascade(label="Restore Default Zoom ",command=undo)


file_menu = Menu(file_menu)
my_menu.add_cascade(label="Help",menu=file_menu)


helpp = Menu()
file_menu.add_cascade(label="View Help",command=undo)
file_menu.add_separator()

helpp = Menu()
file_menu.add_cascade(label="Send FeedBack",command=undo)
file_menu.add_separator()

helpp = Menu()
file_menu.add_cascade(label="About Notepad", command=info)
file_menu.add_separator()



win.mainloop()