from tkinter import *

window = Tk()

window.title("My GUI")
window.minsize(width=400, height=400)

myLabel = Label(text="This is a Label",font=("Arial",24))
myLabel.pack()

myLabel["text"] = "New Text"
myLabel.config(text="New Text")


def button_clicked():
    print("I ot clicked")
    myLabel.config(text=input.get())


button = Button(text="Click Me", command=button_clicked)
button.pack()


input = Entry(width=20)
input.pack()


window.mainloop()