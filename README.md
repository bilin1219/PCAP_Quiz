# PCAP Quiz

This project implements a GUI for a PCAP (Certified Associate in Python Programming) quiz using the Streamlit library. The quiz questions, correct answers, and possible answers are imported from the static files defined in 'pcep_pe{test_type}.py' and 'sample_01.py'.

# Files
- available_exams.py - library of available tests
- gui.py - The entry point of the application
- parse_data.py - parser for the first data type such as 'questions.dat' and 'answers.dat'
- parse_data_new.py - parser for the second data type such as 'pcep_pe{test-type}_q.dat' and 'pcep_pe{test-type}_a.dat'
- pcep_pe1_m1.py - static test definitions for PE1 module 1
- pcep_pe1_m2.py - static test definitions for PE1 module 2
- pcep_pe1_m3.py - static test definitions for PE1 module 3
- pcep_pe1_m4.py - static test definitions for PE1 module 4
- pcep_pe1_summary.py - static test definitions for PE1 summary
- pcep_pe2_m1.py - static test definitions for PE2 module 1
- pcep_pe2_m2.py - static test definitions for PE2 module 2
- pcep_pe2_m3.py - static test definitions for PE2 module 3
- pcep_pe2_m4.py - static test definitions for PE2 module 4
- pcep_pe2_summary.py - static test definitions for PE2 summary
- pcep_pe_final.py  - static test definitions for PE1 and PE2 final
- quiz_struct.py - test definitions structure
- sample_01.py - static test definitions for PCAP
- requirements.txt - project library dependency

# Directory
- data - files with data extracted from PDF

## Features

- Web-based interface for the quiz.
- Displays the quiz instructions and topics.
- For each question, it displays the question number, progress bar, and the question itself.
- If the question has code or a directive, it is also displayed.
- The user can select their answer from the possible answers provided.
- When the user clicks the 'Next' button, the script checks the user's answer, updates the session state variables, and moves to the next question.
- After all questions have been answered, the script displays the user's score and the cumulative percentage of correct answers.

## Installation

1. Clone this repository.
2. Install the required dependencies with `pip install -r requirements.txt`.
3. Run `streamlit run gui.py` to start the application.

## Usage

Navigate to the URL provided by Streamlit in your web browser to start the quiz.
Ex: Local URL: http://localhost:8501

## License

This project is licensed under the terms of the MIT license.

## Demo
![gui](https://github.com/bilin1219/PCAP_Quiz/assets/153024920/4a4f011b-5c7a-42db-98c5-db8af8ddcf2c)
