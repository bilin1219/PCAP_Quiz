from quiz_struct import QuizQuestion

quiz_header = "PCAP Programming Essentials in Python Essentials 2 PE2 Module 4"
quiz_description = """
    PCAP Programming Essentials in Python Essentials 2 PE2 Module 4"""
quiz_information = """
    PCAP Programming Essentials in Python Essentials 2 PE2 Module 4  
    Test Quizzes Exam Answers"""
quiz_link = "[Click here to learn more >](https://pythoninstitute.org/pcap)"

# Define the questions, correct answers, and possible answers
quiz = {
    1: QuizQuestion('''Which of the following open modes allow you to perform read operations? (Select twoanswers)''',
                    None,
                    None,
                    None,
                    {'A': 'r', 'B': 'a', 'C': 'r+', 'D': 'w'},
                    ['A', 'C'],
                    ),
    2: QuizQuestion('''What is the expected result of executing the code?''',
                                       '''
                                        def I():  
                                            s = 'abcdef'  
                                            for c in s[::2]:  
                                                yield c  

                                        for x in I():  
                                            print(x, end=' ')''',
                                       None,
                                       None,
                                       {'A': 'It will print abcdef', 'B': 'It will print an empty line',
                                        'C': 'It will print bdf', 'D': 'It will print ace'},
                                       ['D'],
                                       ),
    3: QuizQuestion('''What keyword would you use to define an anonymous function?''',
                    None,
                    None,
                    None,
                    {'A': 'afun', 'B': 'lambda', 'C': 'def', 'D': 'yield'},
                    ['B'],
                    ),
    4: QuizQuestion('''Select the true statements. (Select two answers)''',
                                       None,
                                       None,
                                       None,
                                       {'A': 'The lambda function can accept a maximum of two arguments',
                                        'B': 'The lambda function can evaluate multiple expressions',
                                        'C': 'The lambda function can evaluate only one expressrion',
                                        'D': 'The lambda function can accept any number of arguments'},
                                       ['C', 'D'],
                                       ),
    5: QuizQuestion('''Look at the code below:''',
                                                          '''
                                                          my_list = [1, 2, 3]  
                                                          # insert line of code here.  
                                                          print(foo)''',
                                                          '''Which snippet would you insert in order for the program to output the following result(tuple):''',
                                                          '''1, 4, 27''',
                                                          {'A': 'foo = list(map(lambda x: x**x, my_list))',
                                                           'B': 'foo = tuple(map(lambda x: x*x, my_list))',
                                                           'C': 'foo = list(map(lambda x: x*x, my_list))',
                                                           'D': 'foo = tuple(map(lambda x: x**x, my_list))'},
                                                          ['D'],
                                                          ),
    6: QuizQuestion('''What is the expected output of the following code?''',
                    '''
                    from datetime import date  
                    date_1 = date(1992, 1, 16)  
                    date_2 = date(1992, 2, 5)  
                    print(date_1 - date_2)''',
                    None,
                    None,
                    {'A': '345', 'B': '345 days', 'C': '345, 0:00:00', 'D': '345 days, 0:00:00'},
                    ['D'],
                    ),
    7: QuizQuestion('''Which program will produce the following output:''',
                                       '''Mo Tu We Th Fr Sa Su''',
                                       None,
                                       None,
                                       {'A': 'import calendar print(calendar.weekheader(3))',
                                        'B': 'import calendar print(calendar.weekheader(2))',
                                        'C': 'import calendar print(calendar.week)',
                                        'D': 'import calendarprint(calendar.weekheader())'},
                                       ['B'],
                                       ),
    8: QuizQuestion('''What is the expected result of executing the following code?''',
                    '''
                    def o(p):  
                        def q():  
                            return '*' *p 
                        return q  

                    r = o(1)  
                    s = o(2)  
                    print(r9) + s())''',
                    None,
                    None,
                    {'A': 'it will print ***', 'B': 'it will print ***', 'C': 'it will print **',
                     'D': 'it will print *'},
                    ['A'],
                    ),
    9: QuizQuestion('''Look at the code below:''',
                                       '''
                                       my_tuple = (0, 1, 2. 3, 4, 5, 6)  
                                       # Insert line of code here.  
                                       print(foo)''',
                                       '''Which snippet would you insert in order for the program to output the following result(list):''',
                                       '''[2, 3, 4, 5, 6]''',
                                       {'A': 'foo = list(filter(lambda x: x-0 and x-1, my_tuple))',
                                        'B': 'foo - list(filter(lambda x: x==0 and x==1, my_tuple))',
                                        'C': 'foo = tuple(filter(lambda x: x>1, my_tuple))',
                                        'D': 'foo = tuple(filter(lambda x: x-0 and x-1, my_tuple))'},
                                       ['A'],
                                       ),
    10: QuizQuestion('''What is the expected result of executing the following code?''',
                     '''
                     def fun(n):  
                        s = '+'  
                        for i in range(n): 
                            s += s  
                            yield s  
                     
                     for x in fun(2):  
                        print(x, end='')''',
                     None,
                     None,
                     {'A': 'It will print +++', 'B': 'It will print ++', 'C': 'It will print ++++++',
                      'D': 'It will print +'},
                     ['C'],
                     ),
    11: QuizQuestion('''What is the meaning of the value represented by errno.EEXITS ?''',
                                         None,
                                         None,
                                         None,
                                         {'A': 'File doesnâ€™t exist', 'B': 'Bad file number', 'C': 'Permission denied',
                                          'D': 'File exists'},
                                         ['D'],
                                         ),
    12: QuizQuestion('''What is the expected result of the following code?''',
                                                             '''
                                                             b = bytearray(3)  
                                                             print(b)''',
                                                             None,
                                                             None,
                                                             {'A': '3', 'B': "bytearray(b'\\x00\\x00\\x00')",
                                                              'C': 'bytearray(0, 0, 0)', 'D': "bytearray(b'3')"},
                                                             ['B'],
                                                             ),
    13: QuizQuestion('''What is the expected output of the following code?''',
                     '''
                     from datetime import datetime  
                     datetime = datetime(2019, 11, 27, 11, 27, 22)  
                     print(datetime.strftime('%y/%B/%d %H:%M:%s'))''',
                     None,
                     None,
                     {'A': '19/November/27 11:27:22', 'B': '2019/Nov/27 11:27:22', 'C': '2019/11/27 11:27:22',
                      'D': '19/11/27 11:27:22'},
                     ['A'],
                     ),
    14: QuizQuestion('''What is the expected output of the following code?''',
                                         '''
                                         import os  
                                         os.mkdir('pictures')  
                                         os.chdir('pictures')  
                                         os.mkdir('thumbnails')  
                                         os.chdir('thumbnails')  
                                         os.mkdir('tmp')  
                                         os.chdir('../')  
                                         print(os.getcwd())''',
                                         None,
                                         None,
                                         {'A': 'The orint to the thumbnails directory',
                                          'B': 'The path to the pitcures directory',
                                          'C': 'The path to the tmp directory', 'D': 'The path to the root directory'},
                                         ['B'],
                                         ),
    15: QuizQuestion('''What is the expected output of the following code?''',
                                                             '''
                                                             import os  
                                                             os.mkdir('thumbnails')  
                                                             os.chdir('thumbnails')  
                                                             sizes = ['small', 'medium', 'large']  
                                                             for size in sizes:  
                                                                os.mkdir(size)  

                                                             print(os.listdir())''',
                                                             None,
                                                             None,
                                                             {'A': "['.', '..', 'large', 'small', 'medium']", 'B': '[]',
                                                              'C': "['.', 'large', 'small', 'medium']",
                                                              'D': "['large', 'small', 'medium']"},
                                                             ['D'],
                                                             ),
    16: QuizQuestion('''What is the expected result of the following code?''',
                     '''
                     import calendar  
                     c = calendar.Calendar()  
                     for weekday in c.iterweekdays():  
                        print(weekday, end="")''',
                     None,
                     None,
                     {'A': '1 2 3 4 5 6 7', 'B': 'Su Mo Tu We Th Fr Sa', 'C': '0 1 2 3 4 5 6 7',
                      'D': 'Mo Tu We Th Fr Sa Su'},
                     ['C'],
                     )
    }
