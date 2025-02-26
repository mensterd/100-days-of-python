import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None


    def still_has_questions(self)->int:
        """ Checks if there are still questions in de bank """
        return self.question_number < len(self.question_list)


    def next_question(self) -> str:
        """ gets the next question en returns it as string """
        self.current_question = self.question_list[self.question_number]
        # Raises current question number
        self.question_number += 1
        # html.unescape() removes control codes from the api retrieved text
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"


    def check_answer(self, user_answer:str) -> bool:
        """ Checks if given answer is correct. Takes user answer as string and returns bool """
        # Checks if given answer was the correct answer
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            # If correct, raise score return True
            self.score += 1
            return True
        else:
            return False

        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")
