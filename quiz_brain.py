from data import question_bank


class QuizTest:
    def __init__(self):
        self.question = 0
        self.score = 0
        self.questionList = question_bank

    def next_question(self):
        user_answer = input(f"Q.{self.question + 1}. {self.questionList[self.question].text} True/False: ") or "i"
        self.check_answer(user_answer, self.questionList[self.question].answer)
        self.question += 1

    def still_has_questions(self):
        return len(self.questionList) > self.question

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower() or answer[0].lower() == correct_answer[0].lower():
            self.score += 1
        print(f"Current Score: {self.score}/{self.question + 1} ")
