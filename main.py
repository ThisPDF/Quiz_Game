from quiz_brain import QuizTest

new_test = QuizTest()
while new_test.still_has_questions():
    new_test.next_question()
