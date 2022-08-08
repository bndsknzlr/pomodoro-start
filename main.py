import tkinter
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔ "
reps = 0
work_list = [0, 2, 4, 6]
pause_list = [1, 3, 5]
timer_test = ""
check_mark = ""

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer_test)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.configure(text="Timer", bg=YELLOW, fg=GREEN)
    checkmark_label.config(text="", bg=YELLOW, fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    count_down(WORK_MIN*60)
    timer_label.configure(text="Work", bg=YELLOW, fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    count_min = math.floor(count / 60)
    count_sec = count % 60
    # correct formatting double zero
    if count_sec == 0:
        count_sec = "00"
    # correct formatting under ten
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    # set timer label

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # counting
    if count > 0 and reps < 8:
        global timer_test
        timer_test = window.after(1, count_down, count - 1)
    elif count == 0:
        reps += 1
        if reps >= 1:
            rep_proof = reps % 2
            if rep_proof == 1:
                global check_mark
                global checkmark_label
                check_mark += CHECKMARK
                checkmark_label.config(text=check_mark, bg=YELLOW, fg=GREEN)
                checkmark_label.grid(row=3, column=1)
            else:
                pass
        if reps not in work_list:
            if reps in pause_list:
                count = short_break_sec
                timer_label.configure(text="Break", bg=YELLOW, fg=PINK)
            else:
                count = long_break_sec
                timer_label.configure(text="Break", bg=YELLOW, fg=RED)
        else:
            count = work_sec
            timer_label.configure(text="Work", bg=YELLOW, fg=GREEN)
        count_down(count)
    else:
        reset_timer()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# timer label in middle of the screen
timer_label = tkinter.Label(text="Timer", font=("Courier", 55, "normal"))
timer_label.configure(bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

# canvas with pic and text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# button that starts the timer
start_button = tkinter.Button(text="Start", command=start_timer)
start_button.config(bg=YELLOW, highlightbackground=YELLOW)
start_button.grid(row=2, column=0, sticky=W)

# button that resets the timer
reset_button = tkinter.Button(text="Reset", command=reset_timer)
reset_button.config(bg=YELLOW, highlightbackground=YELLOW)
reset_button.grid(row=2, column=2, sticky=E)

# # label that shows the rounds
checkmark_label = tkinter.Label(font=55)
checkmark_label.config(bg=YELLOW, fg=GREEN)

window.mainloop()
