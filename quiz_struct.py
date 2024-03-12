import sample_01


class QuizQuestion:
    def __init__(self, question, code, directive, output, answer_list, correct=None):
        self.question = question
        self.code = code
        self.directive = directive
        self.output = output
        self.answer_list = answer_list
        self.correct_answers = correct

    def __str__(self):
        """
        Returns a string representation of the Quiz object.

        The string includes the question, code, directive, output, answer list, and correct answer list (if available).

        Returns:
            str: A string representation of the Quiz object.
        """
        fields = [
            f"Question: {self.question}",
            f"Code: {self.code}" if self.code is not None else "",
            f"Directive: {self.directive}" if self.directive is not None else "",
            f"Output: {self.output}" if self.output is not None else "",
            f"Answer list: {self.answer_list}" if self.answer_list is not None else "",
            f"Correct list: {self.correct_answers}" if self.correct_answers is not None else "",
        ]
        return "\n".join(field for field in fields if field)

    def __repr__(self):
        """
        Returns a string representation of the QuizQuestion object.
        """
        fields = [
            f"QuizQuestion('''{self.question}'''",
            f"'''{self.code}'''" if self.code is not None else "None",
            f"'''{self.directive}'''" if self.directive is not None else "None",
            f"'''{self.output}'''" if self.output is not None else "None",
            f"{self.answer_list}",
            f"{self.correct_answers}",
            ")"
        ]
        return ",\n".join(field for field in fields if field)


    def set_correct_answers(self, answers):
        self.correct_answers = answers

    def verify_answers(self, answers):
            """
            Verifies the given answers against the correct answers and returns the score as a fraction or whole number.

            Args:
                answers (list): A list of user-selected answers.

            Returns:
                float: The score as a fraction or whole number.
            """
            if self.correct_answers is None or isinstance(answers, list) is False:
                return 0

            if len(answers) == len(self.answer_list):
                # if the number of answers is the same as the number of possible answers, then user selected all the answers
                return 0

            correct = 0
            for answer in answers:
                if answer in self.correct_answers:
                    correct += 1

            # fraction or whole number?
            return correct / len(self.correct_answers)


class Quiz:
    def __init__(self, quiz_header, quiz_description, quiz_information, quiz_link, quiz):
        self.quiz_header = quiz_header
        self.quiz_description = quiz_description
        self.quiz_information = quiz_information
        self.quiz_link = quiz_link
        self.quiz = quiz
