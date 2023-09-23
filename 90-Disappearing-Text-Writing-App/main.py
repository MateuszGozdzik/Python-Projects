from tkinter import *
import math


GREY = "#2D4356"
WHITE = "#000"
FONT_NAME = "Courier"


window = Tk()
window.title("Writing App")
window.config(padx=100, pady=50, bg=GREY)

canvas = Canvas(width=200, height=224, bg=GREY, highlightthickness=0)
timer_text = canvas.create_text(100, 130, text="00:00", font = (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

text = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=WHITE, bg=GREY)
text.grid(column=1, row = 0)

start_button = Button(text="Start", highlightthickness=0, highlightbackground=GREY)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, highlightbackground=GREY)
reset_button.grid(column=2, row=2) 

checkbox = Label(text="", bg=GREY, fg=WHITE)
checkbox.grid(column=1, row=3)


window.mainloop()