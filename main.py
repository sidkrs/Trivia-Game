#run this file
from question_model import Question
from data import question_data
from quiz_ai import QuizAI

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(problem=question_text, sol=question_answer)
    question_bank.append(new_question)

quiz = QuizAI(question_bank)

while quiz.questions_left() == True:
    quiz.next_question()

print("End of Quiz")
print(f"Final Score: {quiz.score}/{quiz.question_number}")
