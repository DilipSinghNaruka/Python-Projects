from pywinauto import application
import time
application=application.Application()
application.start("notepad.exe")  #yaha start ka mtlb hai software ko start krna 
application.Notepad.edit.TypeKeys('Hello I am Dilip, I am creating a automatice open notepad')
#yaha edit ka mtlb hai jo software ham kholenge usme ye words automatically type ho jayega 
#


          #    open and type anything automatic

# from pywinauto import application
# import time
# application=application.Application()
# application.start("notepad.exe")
# application.Notepad.edit.TypeKeys('hello  world')

