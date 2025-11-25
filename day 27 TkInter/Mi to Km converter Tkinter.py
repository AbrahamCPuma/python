import tkinter as tk

#  window config
window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300,height=200)
window.config(padx=50,pady=50,background="white")

#   functions

def calculate():
    number = float(input_box.get())
    lb_output.config(text=number * 1.6)

#   main

#   widgets

input_box = tk.Entry(width=20,background="white",borderwidth=2)
input_box.grid(row=0,column=1)

lb_miles = tk.Label(text="Miles",font=("Calibri",12),background="white")
lb_miles.grid(row=0,column=2)

lb_km = tk.Label(text="Km",font=("Calibri",12),background="white")
lb_km.grid(row=1,column=2)

lb_equal = tk.Label(text="is equal to",font=("Calibri",12),background="white")
lb_equal.grid(row=1,column=0)

lb_output = tk.Label(text="",font=("Calibri",12),background="white")
lb_output.grid(row=1,column=1)

button_calculate = tk.Button(text="Calculate",background="white",border=1,command=calculate)
button_calculate.grid(row=2,column=1)



window.mainloop()