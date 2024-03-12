"""
This script implements a GUI for a PCAP (Certified Associate in Python Programming) quiz.
It uses the Streamlit library to create a web-based interface for the quiz.

The quiz questions, correct answers, and possible answers are imported from the 'quiz' module in 'sample_01.py'.

The script initializes the session state variables and displays the quiz instructions and topics.

For each question, it displays the question number, progress bar, and the question itself.
If the question has code or a directive, it is also displayed.
The user can select their answer from the possible answers provided.
When the user clicks the 'Next' button, the script checks the user's answer, updates the session state variables,
and moves to the next question.

After all questions have been answered, the script displays the user's score and the cumulative percentage of correct answers.
"""

from sample_01 import quiz
import streamlit as st
import time
import available_exams

# Set Streamlit page configuration
st.set_page_config(page_title="PCAP QUIZ", page_icon=":tada:", layout="wide")

<<<<<<< HEAD
# Display available exams
with st.container():
    exam_name = st.selectbox('Which test would you like to do today?', available_exams.AvailableExams.keys())
    st.write("---")
    if 'exam_name' in st.session_state and st.session_state.exam_name != exam_name:
        st.session_state.exam_name = exam_name
        st.rerun()
=======
# Display quiz instructions and topics
with st.container():
    st.subheader("Exam: PCAP – Certified Associate in Python Programming")
    st.write("""
    Exam version: PCAP-31-02  
    Exam duration: 65 minutes (exam items) + 10 minutes  
    Number of questions: 40  
    Format: Single-choice and multiple-choice questions  
    Passing score: 70% (28/40 points)  
    Exam item weight: each question is worth 1 point
    """)
    st.write("""
    This Sample Test covers the following topics:  
    1. Control and Evaluations (questions 1-10, 25%)  
    2. Data Aggregates (questions 11-20, 25%)  
    3. Functions and Modules (questions 21-30, 25%)  
    4. Classes, Objects, and Exceptions (questions 31-40, 25%)
    """)
    st.write("[Click here to learn more >](https://pythoninstitute.org/pcap)")
>>>>>>> 167032c1f2ff1d675e6e0805e6f9197f8e1439e8

# Initialize the session state
if 'exam_name' not in st.session_state:
    st.session_state.exam_name = exam_name
if 'question_num' not in st.session_state:
    st.session_state.question_num = 1
if 'correct_answers' not in st.session_state:
    st.session_state.correct_answers = 0.0
if 'user_answer' not in st.session_state:
    st.session_state.user_answer = None
if 'exam_start_time' not in st.session_state:
    st.session_state.exam_start_time = time.time()
if 'exam_duration' not in st.session_state:
    st.session_state.exam_duration = (65 + 10) * 60

<<<<<<< HEAD
exam = available_exams.AvailableExams[st.session_state.exam_name]
quiz_header = exam.quiz_header
quiz_description = exam.quiz_description
quiz_information = exam.quiz_information
quiz_link = exam.quiz_link
quiz = exam.quiz

# Display quiz instructions and topics
with st.container():
    st.subheader(quiz_header)
    st.write(quiz_description)
    st.write(quiz_information)
    st.write(quiz_link)
    st.write("---")

=======
# Check if there are more questions to display
>>>>>>> 167032c1f2ff1d675e6e0805e6f9197f8e1439e8
if st.session_state.question_num in quiz.keys():
    # Get the question, correct answer, and possible answers for the current question
    question = quiz[st.session_state.question_num]

    # Display the question
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info(f"Question {st.session_state.question_num} of {len(quiz)}")
        with col2:
            st.success(f"Correct Answers {st.session_state.correct_answers} of {len(quiz)}")
        with col3:
            st.progress((time.time() - st.session_state.exam_start_time) / st.session_state.exam_duration, "Time used: {:02d}:{:02d}".format(int((time.time() - st.session_state.exam_start_time) / 60), int((time.time() - st.session_state.exam_start_time) % 60)))

    st.write(question.question)

    if question.code is not None:
        st.code(question.code, language="python", line_numbers=False)

    if question.directive is not None:
        st.write(question.directive)

    if question.output is not None:
        st.warning(question.output)

    if len(question.correct_answers) > 1:
        rs = st.multiselect('Response:',
                       list(map(lambda item: f"{item[0]}. {item[1]}", question.answer_list.items())))
        st.session_state.user_answer = [r[0] for r in rs]
    else:
        st.session_state.user_answer = [
            st.radio('Response:', list(map(lambda item: f"{item[0]}. {item[1]}", question.answer_list.items())))[
                0]]

    # Check the user's answer when they press the 'Next' button
    if st.button('Next'):
        st.session_state.question_num += 1
        st.session_state.correct_answers += question.verify_answers(st.session_state.user_answer)
        st.session_state.user_answer = None
        st.rerun()
else:
    st.write(f"You answered {st.session_state.correct_answers} out of {len(quiz)} questions correctly.")
    st.write(f"Cumulative percent answered: {st.session_state.correct_answers / len(quiz) * 100}%")
    st.write(f"Time used: {int((time.time() - st.session_state.exam_start_time) / 60)} minutes and {int((time.time() - st.session_state.exam_start_time) % 60)} seconds")
    del st.session_state['exam_name']
    del st.session_state['question_num']
    del st.session_state['correct_answers']
    del st.session_state['user_answer']
    del st.session_state['exam_start_time']
    del st.session_state['exam_duration']