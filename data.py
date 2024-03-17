from question_model import Question
import requests
import time

question_bank = []
headers = {'Accept': 'application/json'}

question_data = requests.get("https://opentdb.com/api.php?amount=10&type=boolean", headers=headers)
while question_data.json()["response_code"] != 0:
    question_data = requests.get("https://opentdb.com/api.php?amount=10&type=boolean", headers=headers)
    time.sleep(5)
question_text = question_data.json()["results"]

for question in question_text:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)
