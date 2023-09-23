from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.05
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    text.config(text="Timer", fg=GREEN)
    checkbox.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    
    global reps
    reps += 1

    if reps % 2 == 1:
        count = WORK_MIN * 60
        text.config(text="Work", fg=GREEN)

    elif reps == 8:
        count = LONG_BREAK_MIN * 60
        text.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count = SHORT_BREAK_MIN * 60
        text.config(text="Break", fg=PINK)

    count_down(count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    global reps
    global timer

    count_min = math.floor(count/60)
    count_sec = count % 60 
    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔️"
        checkbox.config(text=marks, fg=GREEN)
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
timer_text = canvas.create_text(100, 130, text="00:00", font = (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

text = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
text.grid(column=1, row = 0)

start_button = Button(text="Start", highlightthickness=0, highlightbackground="white", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, highlightbackground="white", command=reset_timer)
reset_button.grid(column=2, row=2) 

checkbox = Label(text="", bg=YELLOW, fg=GREEN)
checkbox.grid(column=1, row=3)


window.mainloop()