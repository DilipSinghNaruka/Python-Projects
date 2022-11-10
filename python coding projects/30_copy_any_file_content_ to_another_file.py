filename = input("Type file name with address :-")
with open(filename, "r") as f:
    content = f.read()

copyfilename = input("Type new file name with address :-")
with open(copyfilename,"w") as f:
    f.write(content)