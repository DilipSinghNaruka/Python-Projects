#  file readed and executed in command line interface
import os
# main values given
a = 1
da = "op"
# loop started
while a == 1:
    #  file readed
    f = open('C:\\Users\\run.txt', 'r')
    data = f.read()
    # print(data)
    # execution of the file content
    if data == da:
        pass
    else:
        os.system(data)
        da = data
