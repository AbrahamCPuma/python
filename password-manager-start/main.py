import tkinter as tk
from tkinter import messagebox, END
import pandas as pd
import os
import random
import string
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():

    letters = string.ascii_letters  # "abc...xyzABC...XYZ"
    char = "!@#$%&*"
    numbers = string.digits         # "0123456789"

    # --- Get User Input (No changes here) ---
    in_letters = random.randint(8,10)
    in_char = random.randint(2,4)
    in_numbers = random.randint(2,4)

    # --- Generate Password ---

    # Use list comprehensions to generate the characters and combine them into one list.
    # This is a more concise and Pythonic way to write the original for-loops.
    password_chars = [random.choice(letters) for _ in range(in_letters)]
    password_chars += [random.choice(char) for _ in range(in_char)]
    password_chars += [random.choice(numbers) for _ in range(in_numbers)]

    # Shuffle the list of characters to mix them up.
    random.shuffle(password_chars)
    # Join the list of characters back into a single string.
    password = "".join(password_chars)
    input_pass.delete(0,END)
    input_pass.insert(0,password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_web.get()
    email = input_email.get()
    password = input_pass.get()

    if website == "":
        messagebox.showerror(title="Error",message="Please add a website")
    elif password == "":
        messagebox.showerror(title="Error",message="Please add a password")
    elif email == "":
        messagebox.showerror(title="Error",message="Please add an email")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            data = {
                "website": [website],
                "email": [email],
                "password": [password]
            }
            export_data = pd.DataFrame(data)
            csv_path = "D:/python/learningbasicpy/password-manager-start/passwordData.csv"
            if not os.path.isfile(csv_path):
                export_data.to_csv(csv_path, index=False)
            else:
                export_data.to_csv(csv_path, mode="a", header=False, index=False)
    


# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.config(bg="white",padx=50,pady=50)
window.title("Password Manager")


file_img = "D:/python/learningbasicpy/password-manager-start/logo.png"
img_logo = tk.PhotoImage(file=file_img)
canvas = tk.Canvas(width=200,height=200,bg="white",highlightthickness=0)
canvas.create_image(100,100,image=img_logo)
canvas.grid(column=1,row=0,sticky=tk.W)

#   column 0
lb_website = tk.Label(text="Website:",bg="white")
lb_website.grid(column=0, row=1)

lb_email = tk.Label(text="Email/Username:",bg="white")
lb_email.grid(column=0, row=2)

lb_pass = tk.Label(text="Password",bg="white")
lb_pass.grid(column=0, row=3)

# column 1

input_web = tk.Entry(width=51,highlightbackground="lightblue",highlightthickness=2)
input_web.grid(column=1,row=1,columnspan=2,sticky=tk.W)
input_web.focus()

input_email = tk.Entry(width=51,highlightbackground="lightblue",highlightthickness=2)
input_email.grid(column=1,row=2,columnspan=2,sticky=tk.W)
input_email.insert(0,"ab@gmail.com")

input_pass = tk.Entry(width=31,highlightbackground="lightblue",highlightthickness=2)
input_pass.grid(column=1,row=3,sticky=tk.W)

bt_add = tk.Button(text="Add",width=43,bg="white",highlightbackground="black",highlightthickness=2,command=save)
bt_add.grid(column=1,row=4,columnspan=2,sticky=tk.W)

#   column 2

bt_gen_pass = tk.Button(text="Generate Password",bg="white",highlightbackground="black",highlightthickness=2,command=generator)
bt_gen_pass.grid(column=2,row=3,sticky=tk.W)

window.mainloop()