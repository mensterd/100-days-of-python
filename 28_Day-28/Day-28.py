from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Nr of timer repetitions
reps = 0
# timer var, used to manage the windows.after() event
var_timer = None

def disable_start_button():
    button_start.config(state=DISABLED, background="light grey")

def enable_start_button():
    button_start.config(state=NORMAL, background="SystemButtonFace")


# ---------------------------- TIMER RESET ------------------------------- # 
# Button Reset event handler
def button_reset_timer():
    global var_timer, reps
    window.after_cancel(var_timer)

    # Reset reps
    reps = 0

    # Reset all text
    label_checks.config(text="")
    label_timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(canvas_timer_text, text="00:00")

    # Enable startbutton
    enable_start_button()


# ---------------------------- TIMER MECHANISM ------------------------------- # 
# Button Start event handler
def button_start_timer():
    global reps
    reps += 1

    disable_start_button()

    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps == 8:
        count_down(long_break_secs)
        label_timer.config(text="Take 20!", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        label_timer.config(text="Take 5!", fg=PINK)
    else:
        count_down(work_secs)
        label_timer.config(text="Working...", fg=GREEN)

    print(f"Nr. reps: {reps}")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count_from):
    # Holds the window.after reference so it can be canceled in the button_reset_timer() function
    global var_timer

    # Calculate amount min. en sec
    count_min = count_from // 60
    count_sec = count_from % 60

    # If less then 2 digits, put a zero before it (estetics)
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    time_text = f"{count_min}:{count_sec}"

    canvas.itemconfig(canvas_timer_text, text=time_text)
    if count_from > 0:
        var_timer = window.after(1000, count_down, count_from - 1)
    else:
        button_start_timer()
        # Put a checkmark on for each work session. For each 2 sessions is 1 work session
        marks = ""
        work_sessions = reps // 2
        # Add a checkmark for each work rep
        for n in range(work_sessions):
            marks += "✓"
        # Put checks on screen
        label_checks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)
# window.geometry("500x500")


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# Create variable from canvas.text. (zodat later de tekst aangepast kan worden, werkt ook zonder toekenning aan var)
canvas_timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Labels
label_timer = Label(text="Timer", font=(FONT_NAME, 33, "bold"), justify="center")
# Put padding around the Label
label_timer.config(padx=10, pady=10, bg=YELLOW, fg=GREEN)
# put on screen
label_timer.grid(column=1, row=0)

label_checks = Label(font=(FONT_NAME, 30, "bold"), justify="center")
# Put padding around the Label
label_checks.config(padx=10, pady=10, bg=YELLOW, fg=GREEN)
# Put on screen
label_checks.grid(column=1, row=3)


# Buttons
button_start = Button(text="Start", command=button_start_timer)
# Highlightthickness=0 sets the tiny white border around the button to 0
button_start.config(width=10, height=1, font={FONT_NAME, 10, "bold"}, highlightthickness=0)
button_start.grid(column=0, row=4)

button_reset = Button(text="Reset", command=button_reset_timer)
button_reset.config(width=10, height=1, font={FONT_NAME, 10, "bold"}, highlightthickness=0)
button_reset.grid(column=2, row=4)

window.mainloop()
