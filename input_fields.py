from tkinter import *

root = Tk()

e = Entry(root, width=50,)
e.pack()
e.insert(0, "enter your Name: ")

def myClick():
    hello = "Hello " + e.get()
    mylable = Label(root, text=hello)
    mylable.pack()

myButton = Button(root, text="click me!", padx=50, pady=50, command=myClick, fg="blue", bg="yellow")
myButton.pack()

root.mainloop()