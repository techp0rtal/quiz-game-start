from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():# if quiz still has questions remaining
    quiz.next_question()
    #quiz.check_answer()

print("You've completed the quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}.")





#print(question_bank)
# This creates a list of question objects, each being initialized with a Q and an A
#
# for question in question_data:
#     question = Question(question["text"], question["answer"])
#     question_bank.append(question)
#     print(question_bank)
# Why didn't this work? ^^^