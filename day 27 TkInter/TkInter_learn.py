from tkinter import *

window = Tk()

window.title("My GUI")
window.minsize(width=400, height=400)
window.config(padx=100,pady=100)

myLabel = Label(text="This is a Label",font=("Arial",24))
myLabel.grid(column=0,row=0)

myLabel["text"] = "New Text"
myLabel.config(text="New Text",padx=100,pady=100)


def button_clicked():
    print("I ot clicked")
    myLabel.config(text=input.get())


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1,row=1)


input = Entry(width=20)
input.grid(column=3,row=2)

Newbutton = Button(text="New Button")
Newbutton.grid(column=2,row=0)

window.mainloop()