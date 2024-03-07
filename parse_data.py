import os
from quiz_struct import QuizQuestion

def parse_quiz_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    quiz = {}
    question_id = None
    question = None
    code = None
    directive = None
    output = None
    answer_list = {}

    for line in lines:
        line = line.strip()
        if line.startswith("Question"):
            question_id = int(line.split()[1])
        elif line.startswith(('A.','B.','C.','D.','E.','F.','G.')):
            answer_key = line[0]
            answer_value = line[3:]
            answer_list[answer_key] = answer_value
        elif line.startswith("_"):
            quiz[question_id] = QuizQuestion(question, code, directive, output, answer_list)
            question = code = directive = output = None
            answer_list = {}
        elif question is None:
            question = line
        elif code is None:
            code = line
        elif directive is None:
            directive = line
        elif output is None:
            output = line

    return quiz

def parse_answers_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    answers = {}

    for line in lines:
        line = line.strip()
        id, list_of_answers = line.split('. ')
        answers[int(id)] = [answer.strip() for answer in list_of_answers.split(',')]

    return answers



# Define the path to the file on the Desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop/00_PythonWIP/Pcap_Quiz")

quiz = parse_quiz_file(os.path.join(desktop_path, 'questions.dat'))

# Define the questions, correct answers, and possible answers
answers = parse_answers_file(os.path.join(desktop_path, 'answers.dat'))
for answer_id, answer in answers.items():
    #print(answer_id, answer)
    quiz[answer_id].set_correct_answers(answer)

for question_id, question in quiz.items():
    #print(question)
    pass

print(quiz)

