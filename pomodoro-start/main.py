import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
work_reps = 0
checkm = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    global work_reps
    global checkm
    reps = 0
    work_reps = 0
    checkm = ""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    lb_timer.config(text=f"Timer",fg=GREEN)
    lb_check.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    
    global reps
    global work_reps
    global checkm
    reps += 1
    print(reps)
    if reps > 0:
        work_sec = WORK_MIN *60
        short_break = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN *60
        match reps:
            case 1 | 3 | 5 | 7:
                count_down(work_sec)
                work_reps += 1
                if work_reps > 1:
                    checkm += "✓"
                lb_check.config(text=checkm)
                lb_timer.config(text=f"WORK ({work_reps})",fg=GREEN)
                
            case 2 | 4 | 6:
                count_down(short_break)
                lb_timer.config(text="BREAK",fg=PINK)
            case 8:
                count_down(long_break_sec)
                lb_timer.config(text="BREAK",fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else: 
         start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)



canvas = tk.Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
img_tomato = tk.PhotoImage(file="D:/python/learningbasicpy/pomodoro-start/tomato.png")
canvas.create_image(100, 112, image=img_tomato)
timer_text = canvas.create_text(100,132, text="00:00",fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)


lb_timer = tk.Label(text="Timer",font=(FONT_NAME,30,"bold"),bg=YELLOW,fg=GREEN)
lb_timer.grid(column=1,row=0)

lb_check = tk.Label(text="",font=(FONT_NAME,15,"bold"),bg=YELLOW,fg=GREEN)
lb_check.grid(column=1,row=3)

bt_start = tk.Button(text="Start",bg="white",command=start_timer)
bt_start.grid(column=0,row=2)

bt_reset = tk.Button(text="Reset",bg="white",command=reset)
bt_reset.grid(column=2,row=2)

window.mainloop()