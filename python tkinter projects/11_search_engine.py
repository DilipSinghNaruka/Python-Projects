# from selenium import webdriver
# from tkinter import *


# ram = Tk()
# ram.geometry("650x500")
# ram.configure(bg='white')
# ram.resizable(0,0)


# def modules():
#     driver = webdriver.Chrome(executable_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')

#     e1= entry.get()
#     driver.get(f'https://pypi.org/project/{e1}/')

#     x = driver.find_element_by_id("pip-command")

#     pypi_result = x.text

#     lblname = Label(ram,text=pypi_result,font="arial 18 bold",bg="white",fg='DodgerBlue2')
#     lblname.place(x=50,y=350)
#     driver.close()

# entry = Entry(ram,font="arial 18 bold")
# entry.place(x=50,y=250,width=550)

# button = Button(ram, text='\U0001F50E', font= "arial 14 bold", bg='white',fg='DodgerBlue2',command=modules)
# button.place(x=560,y = 250)


# intro= Label(ram,text="PYPI\n(PYTHON PACKAGE INDEX)",font="arial 30 bold", bg = 'DodgerBlue2',fg = 'white')
# intro.place(x= 0, y=0,width=700)

# lblname = Label(ram,text="Enter Module Name:-",font="arial 18 bold",bg='white',fg='DodgerBlue2')
# lblname.place(x=50,y=200)

# ram.mainloop()













from selenium import webdriver
import webbrowser
from tkinter import*


root = Tk()
root.geometry("650x500")
root.configure(bg='white')
root.resizable(0,0)


def modules():
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    e1 = entry.get()
    driver.get(f'https://google.com/{e1}/')
    x = driver.find_element_by_id("pip-command")
    pypi_result = x.text
    lblname = Label(root, text=pypi_result, font="arial 18 bold", bg='white', fg='DodgerBlue2')
    lblname.place(x=50, y=350)
    driver.close()

entry = Entry(root,font="arial 18 bold")
entry.place(x=50,y=250,width=550)

button = Button(root,text='\U0001F50E',font="arial 14 bold",bg='white',fg='DodgerBlue2',command=modules)
button.place(x=560,y=250)

intro = Label(root,text="PYPI\n(PYTHON PACKAGE INDEX)",font="arial 30 bold",bg='DodgerBlue2',fg='white')
intro.place(x=0,y=0,width=700)
lblname  = Label(root,text="Enter Module Name:-",font="arial 18 bold",bg='white',fg='DodgerBlue2')
lblname.place(x=50,y=200)

root.mainloop()