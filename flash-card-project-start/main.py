import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
WORD_FONT = ("Ariel",60,"bold")
LANG_FONT = ("Ariel",40,"italic")
eng_word = ""
random_french_word = ""
random_pair = {}
timer = None

try:
    csv_data = pd.read_csv("learningbasicpy/flash-card-project-start/data/to_learn_french_words.csv")
    print(len(csv_data))
except:
    csv_data_original = pd.read_csv("learningbasicpy/flash-card-project-start/data/french_words.csv")
    to_learn = csv_data_original.to_dict(orient="records")
else:
    to_learn = csv_data.to_dict(orient="records")


def right():
  
    global random_pair
    to_learn.remove(random_pair)
    data_to_learn = pd.DataFrame(to_learn)
    data_to_learn.to_csv("learningbasicpy/flash-card-project-start/data/to_learn_french_words.csv",index=False)
    generate_word()

def wrong():
    generate_word()

def generate_word():
    global timer, eng_word, random_french_word, random_pair

    if timer:
        window.after_cancel(timer)

    if len(to_learn) > 0:
        random_pair = random.choice(to_learn)
        random_french_word = random_pair.get('French')
        eng_word = random_pair.get('English')
        canvas.itemconfig(lb_word, text=random_french_word, fill= "black")
        canvas.itemconfig(lb_lang, text="French", fill= "black")
        canvas.itemconfig(img_bk,image=img_card_front)
        
        timer = window.after(3000, show_word)

    else:
        # End of game state
        canvas.itemconfig(lb_word, text="You learned\neverything!", fill="black")
        canvas.itemconfig(lb_lang, text="Congratulations!", fill="black")
        canvas.itemconfig(img_bk, image=img_card_front)
        # Disable buttons so they don't cause errors
        bt_right.config(state="disabled")
        bt_wrong.config(state="disabled")
    


def show_word():
    global eng_word
    
    canvas.itemconfig(lb_word, text=eng_word, fill= "white")
    canvas.itemconfig(lb_lang, text="English", fill= "white")
    canvas.itemconfig(img_bk,image=img_card_back)
    



window = tk.Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



img_card_front = tk.PhotoImage(file="learningbasicpy/flash-card-project-start/images/card_front.png")
img_card_back = tk.PhotoImage(file="learningbasicpy/flash-card-project-start/images/card_back.png")
img_right = tk.PhotoImage(file="learningbasicpy/flash-card-project-start/images/right.png")
img_wrong = tk.PhotoImage(file="learningbasicpy/flash-card-project-start/images/wrong.png")

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img_bk = canvas.create_image(400, 263, image=img_card_front)
lb_lang = canvas.create_text(400,150,text="Language",font=LANG_FONT)
lb_word = canvas.create_text(400,263,text="Word", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)


bt_right = tk.Button(image=img_right, highlightthickness=0, command=right)
bt_wrong = tk.Button(image=img_wrong, highlightthickness=0, command=wrong)
bt_wrong.grid(column=0,row=1)
bt_right.grid(column=1,row=1)


generate_word()

window.mainloop()
