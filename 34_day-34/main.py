from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []

# iterate over all API fetched questions
for question in question_data:
    # Get question text from Dictionary
    question_text = question["question"]
    # Get correct answer from Dictionary
    question_answer = question["correct_answer"]
    # Create a Question object from the fetched data
    new_question = Question(question_text, question_answer)
    # Append the question object to question_bank list
    question_bank.append(new_question)

# Initialize quizbrain, the main logic
quiz = QuizBrain(question_bank)
# Initialize the GUI
quiz_ui = QuizInterface(quiz)


# Prints only after game window is closed
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
