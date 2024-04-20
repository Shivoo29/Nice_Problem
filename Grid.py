# Positioning with Tkinter's Grid System
from tkinter import *

root = Tk()

# create a label widget
mylabel1 = Label(root, text="Hello, world!")
mylabel2 = Label(root, text="Hi, world!")
mylable5 = Label(root, text="How are you, world?").grid(row=3, column=3)
mylabel3 = Label(root, text="What's up, world?")
mylabel4 = Label(root, text="Goodbye, world!")
# putting everything in a grid

mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=1)
mylabel3.grid(row=2, column=2)
mylabel4.grid(row=4, column=4)



root.mainloop()