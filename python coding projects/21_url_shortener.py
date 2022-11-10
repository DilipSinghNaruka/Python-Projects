import pyshorteners

link = input("Type your link :-")

print(pyshorteners.Shortener().tinyurl.short(link))    #tinyurl.short ka usee karan jaruri hai 