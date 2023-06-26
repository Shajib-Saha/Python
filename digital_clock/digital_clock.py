import time
from tkinter import *

root = Tk()
root.configure(background='black')

def start():
    text = time.strftime("%H:%M:%S")
    Label1.config(text=text)  # Update the label instance
    Label1.after(200, start)

Label1 = Label(root, font=("DS-Digital", 100), fg="red", bg="black")
Label1.grid(row=0, column=1)  # Call grid() on Label1, not Label

print("Done")
start()
root.mainloop()
