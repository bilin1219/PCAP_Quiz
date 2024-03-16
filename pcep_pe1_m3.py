from quiz_struct import QuizQuestion

quiz_header = "PCAP Programming Essentials in Python Essentials 1 PE1 Module 3"
quiz_description = """
    PCAP Programming Essentials in Python Essentials 1 PE1 Module 3"""
quiz_information = """
    PCAP Programming Essentials in Python Essentials 1 PE1 Module 3  
    Test Quizzes Exam Answers"""
quiz_link = "[Click here to learn more >](https://pythoninstitute.org/pcap)"

# Define the questions, correct answers, and possible answers
quiz = {1: QuizQuestion('''How many stars (*) will the following snippet send to the console?''',
                        '''
                        i = 0  
                        while i <= 3:   
                          i += 2  
                          print("+")''',
                        None,
                        None,
                        {'A': 'three', 'B': 'zero', 'C': 'one', 'D': 'two'},
                        ['D'],
                        ),
        2: QuizQuestion('''After execution of the following snippet, the sum of the all vals elements will equal to:''',
                        '''
                        vals = [0, 1, 2]  
                        vals.insert(0, 1)  
                        del vals[1]''',
                        None,
                        None,
                        {'A': '3', 'B': '4', 'C': '2', 'D': '5'},
                        ['B'],
                        ),
        3: QuizQuestion('''How many hashes(#) will the following snippet send to the console?''',
                        '''
                        for i in range(1):  
                          print("#")  
                        else:  
                          print("#")''',
                        None,
                        None,
                        {'A': 'zero', 'B': 'three', 'C': 'two', 'D': 'one'},
                        ['C'],
                        ),
        4: QuizQuestion('''How many hashes(#) will the following snippet send to the console?''',
                        '''
                        var = 0  
                        while var < 6:  
                          var += 1  
                          if var % 2 == 0:  
                            continue  
                          print("#")''',
                        None,
                        None,
                        {'A': 'zero', 'B': 'three', 'C': 'two', 'D': 'one'},
                        ['B'],
                        ),
        5: QuizQuestion('''What is the output of the following snippet?''',
                        '''
                        my_list = [3, 1, -2]  
                        print(my_list[my_list(-1)])''',
                        None,
                        None,
                        {'A': '-2', 'B': '-1', 'C': '3', 'D': '1'},
                        ['D'],
                        ),
        6: QuizQuestion('''How many stars(#) will the following snippet send to the console?''',
                        '''
                        var = 0  
                        while i <= 5:  
                          i += 1  
                          if vi % 2 == 0:  
                            break  
                          print("*")''',
                        None,
                        None,
                        {'A': 'three', 'B': 'two', 'C': 'one', 'D': 'zero'},
                        ['C'],
                        ),
        7: QuizQuestion('''What is the output of the following snippet?''',
                        '''
                        my_list = [1, 2, 3, 4]  
                        print(my_list[-3:-2])''',
                        None,
                        None,
                        {'A': '[2, 3]', 'B': '[2, 3, 4]', 'C': '[]', 'D': '[2]'},
                        ['D'],
                        ),
        8: QuizQuestion('''How many hashes(#) will the following snippet send to the console?''',
                        '''
                        var = 1  
                        while var < 10:  
                          print("#")  
                          var = var << 1''',
                        None,
                        None,
                        {'A': 'two', 'B': 'eight', 'C': 'four', 'D': 'one'},
                        ['C'],
                        ),
        9: QuizQuestion('''What is the output of the following snippet?''',
                        '''
                        my_list_1 = [1, 2, 3]  
                        my_list_2 = []  
                        for v in my_list_1:  
                          my_list_2.insert(0, v)  
                        print(my_list_2)''',
                        None,
                        None,
                        {'A': '[1, 2, 3]', 'B': '[3, 2, 1]', 'C': '[3, 3, 3]', 'D': '[1, 1, 1]'},
                        ['B'],
                        ),
        10: QuizQuestion('''Take a look at the snippet, and choose the true statements: (Select two answers)''',
                         '''
                         nums = [1, 2, 3]  
                         vals = nums  
                         del vals[1:2]''',
                         None,
                         None,
                         {'A': 'nums is longer than vals', 'B': 'nums and vals are of the same length',
                          'C': 'nums and vals refer to the same list', 'D': 'nums is replicated and assigned to vals'},
                         ['B', 'C'],
                         ),
        11: QuizQuestion('''What is the output of the following snippet?''',
                         '''
                         my_list = [[0, 1, 2, 3] for i in rage(2)]  
                         print(my_list[2][0])''',
                         None,
                         None,
                         {'A': '1', 'B': '2', 'C': '0',
                          'D': 'the snippet will cause a runtime error'},
                         ['D'],
                         ),
        12: QuizQuestion('''What value will be assigned to the x variable?''',
                         '''
                         z = 10  
                         y = 0  
                         x = y < z and z > y or y > z and z < y''',
                         None,
                         None,
                         {'A': '1', 'B': '0', 'C': 'True', 'D': 'False'},
                         ['C'],
                         ),
        13: QuizQuestion('''Which of the following sentences are true? (Select two answers)''',
                         '''
                         nums = [1, 2, 3]  
                         vals = nums[-1:-2]''',
                         None,
                         None,
                         {'A': 'nums and vals are two different lists',
                          'B': 'vals is longer than nums', 'C': 'nums and vals are of the same length',
                          'D': 'nums is longer than vals'},
                         ['A', 'D'],
                         ),
        14: QuizQuestion('''What is the output of the following snippet?''',
                         '''
                         a = 1  
                         b = 0  
                         c = a & b  
                         d = a | b  
                         e = a ^ b  
                            
                         print(c + d + e)''',
                         None,
                         None,
                         {'A': '1', 'B': '0', 'C': '3', 'D': '2'},
                         ['D'],
                         ),
        15: QuizQuestion('''What is the output of the following snippet?''',
                         '''
                         my_list = [1, 2, 3]  
                         for v in range(len(my_list)):  
                           my_list.insert(1, my_list[v])  
                         print(my_list)''',
                         None,
                         None,
                         {'A': '[1, 2, 3, 1, 2, 3]', 'B': '[1, 2, 3, 3, 2, 1]',
                          'C': '[1, 1, 1, 1, 2, 3]', 'D': '[3, 2, 1, 1, 2, 3]'},
                         ['C'],
                         ),
        16: QuizQuestion('''An operator able to check whether two values are equal is code as:''',
                         None,
                         None,
                         None,
                         {'A': '=', 'B': '!=', 'C': '==', 'D': '==='},
                         ['C'],
                         ),
        17: QuizQuestion('''The second assignment:''',
                         '''
                         vals = [0, 1, 2]  
                         vals[0], vals[2] = vals[2], vals[0]''',
                         None,
                         None,
                         {'A': 'doesn\'t change the list', 'B': 'reverses the list',
                          'C': 'shortens the list', 'D': 'extends the list'},
                         ['B'],
                         ),
        18: QuizQuestion('''What is the output of the following snippet?''',
                         '''
                         t = [[3-i for i in range (3)] for j in range (3)]  
                         s = 0 for i in range(3):  
                           s += t[i][i]
                         print(s)''',
                         None,
                         None,
                         {'A': '4', 'B': '7', 'C': '02', 'D': '6'},
                         ['D'],
                         ),
        19: QuizQuestion('''The value eventually assigned to x is equal to :''',
                         '''
                         x = 1  
                         x = x == x''',
                         None,
                         None,
                         {'A': '0', 'B': '1', 'C': 'True', 'D': 'False'},
                         ['C'],
                         ),
        20: QuizQuestion('''How many elements does the my_list list contain?''',
                         '''my_list = [i for i in range(-1, 2)]''',
                         None,
                         None,
                         {'A': 'two', 'B': 'three', 'C': 'four', 'D': 'one'},
                         ['B'],
                         )}
