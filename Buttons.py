from tkinter import *
root = Tk()

def myClick():
    mylable = Label(root, text="I have been clicked!")
    mylable.pack()

myButton = Button(root, text="click me!", padx=50, pady=50, command=myClick, fg="blue", bg="yellow")
myButton.pack()

root.mainloop()
