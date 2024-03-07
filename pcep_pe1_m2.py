from quiz_struct import QuizQuestion

quiz_header = "PCAP Programming Essentials in Python Essentials 1 PE1 Module 2"
quiz_description = """
    PCAP Programming Essentials in Python Essentials 1 PE1 Module 2"""
quiz_information = """
    PCAP Programming Essentials in Python Essentials 1 PE1 Module 2  
    Test Quizzes Exam Answers"""
quiz_link = "[Click here to learn more >](https://pythoninstitute.org/pcap)"

# Define the questions, correct answers, and possible answers
quiz = {
    1: QuizQuestion('''The \n digraph forces the print() function to:''',
                    '''stop its execution''',
                    '''duplicate the character next to the digraph''',
                    '''break the output line''',
                    {},
                    ['C'],
                    ),
    2: QuizQuestion(
        '''What is the output of the following snippet if the user enters two lines containing 2 and 4respectively?''',
        '''
        x = int(input())  
        y = int(intpu())  
        x = x / yy = y / x  
        print(y)''',
        None,
        None,
        {'A': '8.0', 'B': 'the code will cause a runtime error', 'C': '4.0', 'D': '2.0'},
        ['A'],
    ),
    3: QuizQuestion('''What is the output of the following snippet?''',
                    '''
                    z = y = x = 1  
                    print(x, y, z, sep='*')''',
                    None,
                    None,
                    {'A': '1 1 1', 'B': 'x*y*z', 'C': '1*1*1', 'D': 'x y z'},
                    ['C'],
                    ),
    4: QuizQuestion('''What is the output of the following snippet?''',
                    '''
                    x = 1 / 2 + 3 // 3 + 4 ** 2  
                    print(x)''',
                    None,
                    None,
                    {'A': '8.5', 'B': '0', 'C': '17.5', 'D': '17'},
                    ['C'],
                    ),
    5: QuizQuestion(
        '''What is the output of the following snippet if the user enter two lines containing 2 and 4 respectively?''',
        '''
        x = int(input())  
        y = int(input())  
        print(x + y)''',
        None,
        None,
        {'A': '2', 'B': '24', 'C': '4', 'D': '6'},
        ['D'],
    ),
    6: QuizQuestion('''Which of the following variable names are illegal? (Select two answers)''',
                    None,
                    None,
                    None,
                    {'A': 'true', 'B': 'and', 'C': 'TRUE', 'D': 'True'},
                    ['B', 'D'],
                    ),
    7: QuizQuestion('''The result of the following division:''',
                    '''1 / 1''',
                    None,
                    None,
                    {'A': 'is equal to 1.0', 'B': 'is equal to', 'C': '1',
                     'D': 'cannot be evaluated', 'E': 'cannot be predicted'},
                    ['A'],
                    ),
    8: QuizQuestion('''The ** operator:''',
                    None,
                    None,
                    None,
                    {'A': 'does not exist',
                     'B': 'performs duplicated multiplication',
                     'C': 'performs exponentiation',
                     'D': 'perform floating-point multiplication'},
                    ['C'],
                    ),
    9: QuizQuestion('''What is the output of the following snippet?''',
                    '''
                    y = 2 + 3 * 5.  
                    print(Y)''',
                    None,
                    None,
                    {'A': 'the snippet will cause an execution error', 'B': '25.', 'C': '17', 'D': '17.0'},
                    ['A'],
                    ),
    10: QuizQuestion('''What is the output of the following snippet?''',
                     '''
                     x = 1  
                     y = 2  
                     z = x  
                     x = y  
                     y = z  
                     print (x, y)''',
                     None,
                     None,
                     {'A': '1 2', 'B': '1 1', 'C': '2 2', 'D': '2 2'},
                     ['D'],
                     ),
    11: QuizQuestion('''The 80 prefix means that the number after it is denoted as:''',
                     None,
                     None,
                     None,
                     {'A': 'hexadecimal', 'B': 'octal', 'C': 'decimal', 'D': 'binary'},
                     ['B'],
                     ),
    12: QuizQuestion(
        '''The value twenty point twelve times ten raised to the power of eight should be written as:''',
        None,
        None,
        None,
        {'A': '20.12*10^8', 'B': '20E12.8', 'C': '20.12E8.0', 'D': '20.12Eo'},
        ['D'],
    ),
    13: QuizQuestion(
        '''What is the output of the following snippet if the user enter two lines containing 2 and 4 respectively?''',
        '''
        x = int(intput())  
        y = int(intput())  
        x = x // y  
        y = y //x  
        print(y)''',
        None,
        None,
        {'A': 'the code will cause a runtime error', 'B': '2.0', 'C': '8.0', 'D': '4.0'},
        ['A'],
    ),
    14: QuizQuestion(
        '''What is the output of the following snippet if the user enter two lines containing 11 and 4 respectively?''',
        '''
        x = int(intput())   
        y = int(intput())  
        x = x % y  
        x = x % y  
        y = y % x  
        print(y)''',
        None,
        None,
        {'A': '3', 'B': '2', 'C': '4', 'D': '1'},
        ['D'],
    ),
    15: QuizQuestion('''The print() function can output values of:''',
                     None,
                     None,
                     None,
                     {'A': 'not more than five arguments', 'B': 'any number of arguments (including zero)',
                      'C': 'any number of arguments (excluding zero)', 'D': 'just one argument'},
                     ['B'],
                     ), 16: QuizQuestion(
        '''What is the output of the following snippet if the user enters two lines containing 3 and 6 respectively?''',
        '''
        x = input()  
        y = int(input())  
        print(x * y)''',
        None,
        None,
        {'A': '333333', 'B': '36', 'C': '18', 'D': '666'},
        ['A'],
    ),
    17: QuizQuestion('''Left-sided binding determines that the result of the following expression:''',
                     '''1 // 2 * 3''',
                     '''is equal to :''',
                     None,
                     {'A': '0.0', 'B': '0', 'C': '4.5', 'D': '0.166666666666666666'},
                     ['B'],
                     ),
    18: QuizQuestion('''Which of the following statement are true? (Select two answers)''',
                     None,
                     None,
                     None,
                     {'A': 'The result of the / operator is always an integer value.',
                      'B': 'The ** operator uses right-sided binding.',
                      'C': 'Adding precedes multiplication.',
                      'D': 'The right argument of the % operator cannot be zero.'},
                     ['B', 'D'],
                     ),
    19: QuizQuestion(
        '''What is the output of the following snippet if the user enters two lines containing 2 and 4 respectively?''',
        '''
        x = input()  
        y = input()  
        print(x + y)''',
        None,
        None,
        {'A': '4', 'B': '2', 'C': '6', 'D': '24'},
        ['D'],
    ),
    20: QuizQuestion('''The meaning of the keyword parameter is determined by:''',
                     None,
                     None,
                     None,
                     {'A': 'its value', 'B': 'the argumentâ€™s name specified along with is value',
                      'C': 'its connection with exiting variables',
                      'D': 'its position within the argument list'},
                     ['B'],
                     )}
