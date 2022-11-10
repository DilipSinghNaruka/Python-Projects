# from tkinter import *
# import time

# def clocktime(time1=""):
#     time2=time.strftime("%H:%M:%S")
#     if time2!=time1:
#         time1=time2
#         clock.config(text=time2)
#         clock.after(20,clocktime)
# clockface=TK()
# clock=Label(clockface,fond="time 15 bold")
# clock.pack(fill="both",expand=1)
# clocktime()
# clockface.mainloop()




# importing whole module
from tkinter import *
from tkinter.ttk import *
 
# importing strftime function to
# retrieve system's time
from time import strftime
 
# creating tkinter window
root = Tk()
root.title('Clock')
 
# This function is used to
# display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)
 
# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'purple',
            foreground = 'white')
 
# Placing clock at the centre
# of the tkinter window
lbl.place(x=50,y=50)
time()
 
mainloop()