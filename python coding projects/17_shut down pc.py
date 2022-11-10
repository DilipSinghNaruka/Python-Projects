# import os
# check=input("shut down your pc ?(y/n)")
# if check=='n':
#     exit()
# else:
# #     os.system("shutdown/s/t 1" )


import os

shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")

if shutdown == 'no':
    exit()  #exit ka meaning hai esss code ko band kara dena
else:
    os.system("shutdown /s /t 1")  #"shutdown /s /t 1" ye cmd ki ek command hai jisse system shutdown hota hai 

