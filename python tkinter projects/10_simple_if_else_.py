import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
root.title("Try code")

entry = tk.Entry(root)
entry.pack()

def on_button():
    if entry.get() == "screen":
        slabel = tk.Label(root, text="Screen was entered")
        slabel.pack()
    else:
        tlabel = tk.Label(root, text="")
        tlabel.pack()

button = tk.Button(root, text="Enter", command=on_button)
button.pack()

root.mainloop()