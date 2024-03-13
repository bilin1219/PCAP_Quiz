import os
from quiz_struct import QuizQuestion
import re

def parse_question_line(line):
    """
    Parses a line of text containing a question and returns the question ID and question text.

    Args:
        line (str): The line of text containing the question.

    Returns:
        tuple: A tuple containing the question ID (int) and question text (str).
               If the line does not match the expected format, returns (None, None).
    """
    match = re.match(r'(\d{1,2})\.\s*(.*)', line)
    if match:
        question_id = int(match.group(1))
        question_text = match.group(2)
        return question_id, question_text
    else:
        return None, None
    

def parse_quiz_file(file_path):
    """
    Parses a quiz file and returns a dictionary containing the quiz questions.

    Args:
        file_path (str): The path to the quiz file.

    Returns:
        dict: A dictionary containing the quiz questions, where the keys are the question IDs
              and the values are instances of the QuizQuestion class.

    """
    with open(file_path, 'r') as f:
        lines = f.readlines()

    quiz = {}
    index = 0
    question_id = None
    question = None
    code = None
    directive = None
    output = None
    answer_list = {}

    for line in lines:
        line = line.strip()
        if line.startswith(('1. ','2. ','3. ','4. ','5. ','6. ','7. ','8. ','9. ','10. ','11. ','12. ','13. ','14. ','15. ','16. ','17. ','18. ','19. ','20. ','21. ','22. ','23. ','24. ','25. ','26. ','27. ','28. ','29. ','30. ','31. ','32. ','33. ','34. ','35. ','36. ','37. ','38. ','39. ','40. ','41. ','42. ','43. ','44. ','45. ','46. ','47. ','48. ','49. ','50. ','51. ','52. ','53. ','54. ','55. ','56. ','57. ','58. ','59. ','60. ',)):
            question_id, question = parse_question_line(line)
        elif line.startswith(('A.')):
            answer_key = chr(ord(line[0]) + index)
            index += 1
            answer_value = line[3:]
            answer_list[answer_key] = answer_value
        elif line.startswith(('B.','C.','D.','E.','F.','G.')):
            answer_key = line[0]
            answer_value = line[3:]
            answer_list[answer_key] = answer_value
        elif line.startswith("---"):
            quiz[question_id] = QuizQuestion(question, code, directive, output, answer_list)
            question = code = directive = output = None
            index = 0
            answer_list = {}
        elif code is None:
            code = line
        elif directive is None:
            directive = line
        elif output is None:
            output = line

    return quiz

def parse_answers_file(file_path):
    """
    Parses a file containing answers and returns a dictionary of answers.

    Args:
        file_path (str): The path to the file containing the answers.

    Returns:
        dict: A dictionary where the keys are question IDs and the values are lists of answers.
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()

    answers = {}

    for line in lines:
        line = line.strip()
        id, list_of_answers = line.split('. ')
        answers[int(id)] = [answer.strip() for answer in list_of_answers.split(',')]

    return answers



# Define the path to the file on the Desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop/00_PythonWIP/data")

quiz = parse_quiz_file(os.path.join(desktop_path, 'pcep_pe1_summary_q.dat'))

# Define the questions, correct answers, and possible answers
answers = parse_answers_file(os.path.join(desktop_path, 'pcep_pe1_summary_a.dat'))
for answer_id, answer in answers.items():
    #print(answer_id, answer)
    quiz[answer_id].set_correct_answers(answer)

for question_id, question in quiz.items():
    #print(question)
    pass

print(quiz)

