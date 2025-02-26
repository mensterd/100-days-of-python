from tkinter import *
from quiz_brain import QuizBrain

CHECK_IMAGE_PATH = "images/true.png"
CROSS_IMAGE_PATH = "images/false.png"
PAD_X = 4
PAD_Y = 4
# Background color
THEME_COLOR = "#375362"


class QuizInterface:
    """ Creates the GUI; takes a QuizBrain object to proces """
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window_bg_color = "#375362"
        self.canvas_font = ("Ariel", 20, "italic")
        self.label_font = ("bold")
        self.define_main_window()

        self.define_images()
        self.create_labels()
        self.create_canvas()
        self.create_buttons()

        self.get_next_question()

        self.window.mainloop()



    def define_main_window(self):
        """ Sets the window configuration """
        self.window.title("Quizler")
        self.window.config(padx=10, pady=10, background=self.window_bg_color)


    def define_images(self):
        """ Sets the button images """
        self.image_button_check = PhotoImage(file=CHECK_IMAGE_PATH)
        self.image_button_cross = PhotoImage(file=CROSS_IMAGE_PATH)


    def create_labels(self):
        """ Creates and displays the label """
        self.label_score = Label(text="Score: 0", pady=2, font=self.label_font, background=self.window_bg_color,
                                 foreground="white", anchor="c")  # center
        self.label_score.grid(row=0, column=1)


    def create_canvas(self):
        """ Creates and displays the canvas """
        self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125, text="Tekst hier", width=290, font=self.canvas_font)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)


    def create_buttons(self):
        """ Creates and displays buttons """
        self.button_check = Button(image=self.image_button_check, padx=PAD_X, pady=PAD_Y, highlightthickness=0, borderwidth=0,
                              command=self.check_true_answer)
        self.button_check.grid(row=2, column=0)

        self.button_cross = Button(image=self.image_button_cross, padx=PAD_X, pady=PAD_Y, highlightthickness=0, borderwidth=0,
                              command=self.check_false_answer)
        self.button_cross.grid(row=2, column=1)




    def get_next_question(self):
        """ gets the next question if available, displays it and sets gui accordingly """
        if self.quiz.still_has_questions():
            # If there are any questions left, set canvas background to white
            self.canvas.config(background="white")
            # Fetch question from question bank
            q_text = self.quiz.next_question()
            # Display question text on canvas
            self.canvas.itemconfig(self.canvas_text, text=q_text)
            # Display current score on label
            self.label_score["text"] = f"Score: {self.quiz.score}"
        else:
            # If there are no more questions
            self.canvas.itemconfig(self.canvas_text, text="You have reached the end of the quiz.")
            self.canvas.config(background="white")
            # Disable buttons
            self.button_cross.config(state=DISABLED)
            self.button_check.config(state=DISABLED)


    def check_true_answer(self):
        """ Checks if 'True' was the right answer """
        is_correct = self.quiz.check_answer("True")
        # Give feedback on this answer
        self.give_feedback(is_correct)


    def check_false_answer(self):
        """ Checks if 'False' was the right answer """
        is_correct = self.quiz.check_answer("False")
        # Give feedback on this answer
        self.give_feedback(is_correct)


    def give_feedback(self, answer:bool):
        """ Checks if the given answer was correct and returns True or False accordingly"""
        if answer:
            # Sets feedback text
            feedback_text = "You got it right!"
            # Sets canvas background to green
            self.canvas.config(background="green")
        else:
            # Sets feedback text
            feedback_text = "No, that's wrong."
            # Sets canvas background to red
            self.canvas.config(background="red")

        # Displays feedback text on canvas
        self.canvas.itemconfig(self.canvas_text, text=feedback_text)
        # Waits for 1 sec. and gets a new question
        self.window.after(1000, self.get_next_question)

