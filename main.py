from question_model import Question
from data import question_data

question_bank = [

]
#print(question_bank)
# This creates a list of question objects, each being initialized with a Q and an A
#
# for question in question_data:
#     question = Question(question["text"], question["answer"])
#     question_bank.append(question)
#     print(question_bank)

for question in question_data:
    question_text =question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
print(question_bank)

