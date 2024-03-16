from quiz_struct import QuizQuestion

quiz_header = "PCAP Programming Essentials in Python Essentials 1 Part 1 Summary"
quiz_description = """
    PCAP Programming Essentials in Python Essentials 1 PE1 Part 1 Summary"""
quiz_information = """
    PCAP Programming Essentials in Python Essentials 1 PE1 Part 1 Summary  
    Test Quizzes Exam Answers"""
quiz_link = "[Click here to learn more >](https://pythoninstitute.org/pcap)"

# Define the questions, correct answers, and possible answers
quiz = {1: QuizQuestion('''What is the output of the following snippet?''',
                        '''
                        tup = (1, 2, 4, 8)  
                        tup = tup[-2:-1]  
                        tup = tup[-1]  
                        print(tup)''',
                        None,
                        None,
                        {'A': '44', 'B': '4', 'C': '(4)', 'D': '(4,)'},
                        ['B'],
                        ),
        2: QuizQuestion(
            '''Assuming that my_tuple is a correctly created tuple, the fact that tuples are immutablemeans that the following instruction:''',
            '''my_tuple[1] = my_tuple[1] + my_tuple[0]''',
            None,
            None,
            {'A': 'may be illegal if the tuple contains strings', 'B': 'is illegal',
             'C': 'can be executed if and only if the tuple contains at least two elements', 'D': 'is full correct'},
            ['B'],
        ),
        3: QuizQuestion(
            '''Which of the following lines correctly. invoke the function defined below? (Select two answers)''',
            '''
            def fun(a, b, c=0):  
              #Body of the function.''',
            None,
            None,
            {'A': 'fun()', 'B': 'fun(0, 1, 2)', 'C': 'fun(b=0, a=0)', 'D': 'fun(b=1)'},
            ['B', 'C'],
        ),
        4: QuizQuestion('''The meaning of a positional argument is determined by:''',
                        None,
                        None,
                        None,
                        {'A': 'its position within the argument list', 'B': 'its connection with existing variables',
                         'C': 'its value', 'D': 'the argumentâ€™s name specified along with its value'},
                        ['A'],
                        ),
        5: QuizQuestion('''What will happen when you attempt to run the following code?''',
                        '''print(Hello, World)''',
                        None,
                        None,
                        {'A': 'The code will raise the AttributeError exception.',
                         'B': 'The code will raise the systemError exception.',
                         'C': 'The code will raise the ValueError exception.',
                         'D': 'The code will print Hello World to the console.',
                         'E': 'The code will raise the TyepError exception.'},
                        ['B'],
                        ),
        6: QuizQuestion('''The following snippet:''',
                        '''
                        def func(a, b):  
                          reeturn b ** a  
                          
                        print(func(b=2, 2))''',
                        None,
                        None,
                        {'A': 'will output 4', 'B': 'will output None',
                         'C': 'will output 2', 'D': 'is erroneous'},
                        ['D'],
                        ),
        7: QuizQuestion('''The following snippet:''',
                        '''
                        def function_1(a):  
                          return None  
                          
                        def function_2(a):  
                          return function_1(a) * functin_1(a)  
                          
                        print(function_2(2))''',
                        None,
                        None,
                        {'A': 'will output 16',
                         'B': 'will crate a runtime error',
                         'C': 'will output 4',
                         'D': 'will output 2'},
                        ['B'],
                        ),
        8: QuizQuestion('''What is the output of the following snippet?''',
                        '''
                        def fun(x):  
                          if c % 2 == 0:  
                            return 1  
                          else:  
                            return 2  
                            
                        print(fun(fun(2)))''',
                        None,
                        None,
                        {'A': '2', 'B': 'None', 'C': '1', 'D': 'the code will cause a runtime error', 'E': '2'},
                        ['D'],
                        ),
        9: QuizQuestion('''What is the output of the following piece of code?''',
                        '''print("a", "b", "c", sep="sep")''',
                        None,
                        None,
                        {'A': 'a b c', 'B': 'abc', 'C': 'asepbsepcsep', 'D': 'asepbsepc'},
                        ['D'],
                        ),
        10: QuizQuestion('''Which of the following sentences are true about the code? (Select two answers)''',
                         '''
                         nums = [1, 2, 3]  
                         vals = nums''',
                         None,
                         None,
                         {'A': 'nums and vals are different names of the same list', 'B': 'vals is longer than nums',
                          'C': 'nums and vals are different lists', 'D': 'nums has the same length as vals'},
                         ['A', 'D'],
                         ),
        11: QuizQuestion('''What is the output of the following snippet?''',
                         '''
                         my_list = [1, 2]  
                         for v in range(2):  
                           my_list.insert(-1, my_list[v])  
                           
                         print(my_list)''',
                         None,
                         None,
                         {'A': '[1, 2, 2, 2]', 'B': '[1, 2, 1, 2]', 'C': '[2, 1, 1, 2]',
                          'D': '[1, 1, 1, 2]'},
                         ['D'],
                         ),
        12: QuizQuestion('''What is the output of the following snippet?''',
                         '''
                         dct = {}  
                         dct['1'] = (1, 2)  
                         dct['2'] = (2, 1)  
                         for x in dct.keys():  
                           print(dct[x][1], end="")''',
                         None,
                         None,
                         {'A': '21', 'B': '(2,1)', 'C': '12', 'D': '(1,2)'},
                         ['A'],
                         ),
        13: QuizQuestion('''What is the output of the following piece of code?''',
                         '''
                         x = 1 // 5 + 1 / 5  
                         print(x)''',
                         None,
                         None,
                         {'A': '0.0', 'B': '0', 'C': '0.4', 'D': '0.2'},
                         ['D'],
                         ),
        14: QuizQuestion('''What is the output of the following piece of code?''',
                         '''
                         x = 1  
                         y = 2  
                         x, y z = x, x, y   
                         z, y, z = x, y, z  
                         print(x, y, z)''',
                         None,
                         None,
                         {'A': '2 1 2', 'B': '1 2 2', 'C': '1 1 2', 'D': '1 2 1'},
                         ['C'],
                         ),
        15: QuizQuestion('''The result of the following division:''',
                         '''1 // 2''',
                         None,
                         None,
                         {'A': 'is equal to 0.5', 'B': 'is equal to 0',
                          'C': 'is equal to 0.0', 'D': 'cannot be predicted'},
                         ['B'],
                         ),
        16: QuizQuestion('''What is the output of the following snippet?''',
                         '''
                         def fun(inp =2, out =3):  
                           return inp * out  
                           
                         print(fun(out =2))''',
                         None,
                         None,
                         {'A': '4', 'B': '6', 'C': '2', 'D': 'the snippet is erroneous and will cause SyntaxError'},
                         ['A'],
                         ),
        17: QuizQuestion('''What is the expected behavior of the following program?''',
                         '''
                         foo = (1, 2, 3)  
                         foo.index(0)''',
                         None,
                         None,
                         {'A': 'The program will cause a ValueError exception.',
                          'B': 'The program will output 1 to the screen.',
                          'C': 'The program will cause a SyntaxError exception.',
                          'D': 'The program will cause a TypeError exception.',
                          'E': 'The program will cause an AttributeError exception.'},
                         ['A'],
                         ),
        18: QuizQuestion('''What is the output of the following snippet?''',
                         '''
                         def fun(x, y):  
                           if x == y:  
                             return x  
                           else:  
                             return fun(x, y-1)  
                             
                         print(fun(0,3))''',
                         None,
                         None,
                         {'A': '1', 'B': '2',
                          'C': 'the snippet will cause a runtime error',
                          'D': '0'},
                         ['D'],
                         ),
        19: QuizQuestion('''How many element does the lst list contain?''',
                         '''lst = [i for i in range(-1, -2)]''',
                         None,
                         None,
                         {'A': 'two', 'B': 'three', 'C': 'zero', 'D': 'one'},
                         ['C'],
                         ),
        20: QuizQuestion(
            '''What is the output of the following piece of code if the user enters two lines containing 2 and 4 respectively?''',
            '''
            x = float(input())  
            y = float(input())  
            print(y **(1 / x))''',
            None,
            None,
            {'A': '4.0', 'B': '2.0', 'C': '0.0', 'D': '1.0'},
            ['B'],
        ),
        21: QuizQuestion('''What is the output of the following code if the user enters a 0 ?''',
                         '''
                         try:  
                           value = input("Enter a value: ")  
                           print(int(value) / len(value))  
                         except ValueError:  
                           print("Bad input...")  
                         except ZeroDivisionError:  
                           print("Very bad input...")  
                         except TypeErrorq:  
                           print("Very very bad input...")  
                         except:  
                           print("Booo!")''',
                         None,
                         None,
                         {'A': 'Very bad input...', 'B': 'Very very bad input...', 'C': 'Bad input...', 'D': 'Booo!',
                          'E': '0.0', 'F': '1.0'},
                         ['E'],
                         ),
        22: QuizQuestion('''What is the output of the following snippet?''',
                         '''
                         dct = {'one': 'two', 'three': 'one', 'two': 'three'}  
                         v = dct['three']  
                         for k in range(len(dct)):  
                           v = dct[v]  
                         print(v)''',
                         None,
                         None,
                         {'A': 'two', 'B': "('one', 'two', 'three')", 'C': 'three', 'D': 'one'},
                         ['D'],
                         ),
        23: QuizQuestion('''What value will be assigned to the x variable?''',
                         '''
                         z = 0  
                         y = 0  
                         x = y < z and z > y or y > z and z < y''',
                         None,
                         None,
                         {'A': 'False', 'B': '0', 'C': '1', 'D': 'True'},
                         ['D'],
                         ),
        24: QuizQuestion(
            '''What is the output of the following piece of the code if the user enters two lines containing 3 and 6 respectively?''',
            '''
            y = input()  
            x = input()  
            print(x + y)''',
            None,
            None,
            {'A': '36', 'B': '3', 'C': '63', 'D': '6'},
            ['C'],
        ),
        25: QuizQuestion(
            '''Which of the following variable names are illegal and will cause the SystemErrorexception? (Select two answers)''',
            None,
            None,
            None,
            {'A': 'print', 'B': 'in', 'C': 'for', 'D': 'in'},
            ['B', 'C'],
        ),
        26: QuizQuestion('''What is the expected behavior of the following program?''',
                         '''
                         try:  
                           print(5/0)  
                           break:  
                         except:  
                           print("Sorry, something went wrong...")  
                         except(ValueError, ZeroDivisionError):  
                           print("Too bad...")''',
                         None,
                         None,
                         {
                             'A': 'The program will cause a ValueError exception and output the following message Too bad...',
                             'B': 'The program will cause a SyntaxError exception', 
                             'C': 'The program will cause a ValueError exception and output a default error message.',
                             'D': 'The program will raise an exception handle by the first except block.',
                             'E': 'The program will cause a ZeroDivisionError exception and output the following message: Toobad...',
                             'F': 'The program will cause a ZeroDivisionError exception and output a default error message.'},
                         ['B'],
                         ),
        27: QuizQuestion('''Take a look at the snippet and choose the true statement:''',
                         '''
                         nums = [1, 2, 3]  
                         vals = nums  
                         del vals[:]''',
                         None,
                         None,
                         {'A': 'the snippet will cause a runtime error',
                          'B': 'vals is longer than nums', 'C': 'nums is longer than vals',
                          'D': 'nums and vals have the same length'},
                         ['D'],
                         ),
        28: QuizQuestion('''What is the output of the following snippet?''',
                         '''
                         my_list = [x * x for x in range (5)]  
                         def fun(lst):  
                           del lst[lst[2]]  
                           return lst  
                         
                         print(fun(my_list))''',
                         None,
                         None,
                         {'A': '[0 , 1, 4, 9]', 'B': '[0, 1, 4, 16]',
                          'C': '[0, 1, 9, 16]', 'D': '[1, 4, 9, 16]'},
                         ['A'],
                         ),
        29: QuizQuestion('''What is the output of the following snippet?''',
                         '''
                         dd = {"1": "0", "0": "1"}  
                         for x in dd.vals():  
                           print(x, end="")''',
                         None,
                         None,
                         {'A': '0 1', 'B': '1 0', 'C': '0 0',
                          'D': 'the code is erroneous(the dict object has no vals() method)'},
                         ['D'],
                         ),
        30: QuizQuestion(
            '''What is the output of the following piece of code if the user enters two lines containing 3 and 2 respectively?''',
            '''
            x = int(input())  
            y = int(input())  
            x = x % y  
            y = y % x  
            print(y)''',
            None,
            None,
            {'A': '1', 'B': '3', 'C': '2', 'D': '0'},
            ['D'],
        ),
        31: QuizQuestion(
            '''Which of the following snippets shows the correct way of handling multiple excepting ina single except clause?''',
            None,
            None,
            None,
            {'A': 'except TypeError, ValueError, ZeroDivisinError: # Some code.',
             'B': 'except: (TypeError, ValueError, ZeroDivisinError) # Some code.',
             'C': 'except TypeError, ValueError, ZeroDivisinError # Some code.',
             'D': 'except: TypeError, ValueError, ZeroDivisinError # Some code.',
             'E': 'except: (TypeError, ValueError, ZeroDivisinError): # Some code.',
             'F': 'except (TypeError, ValueError, ZeroDivisinError) # Some code.'},
            ['E'],
        ),
        32: QuizQuestion('''An operator able to check two values are not equal is code as:''',
                         None,
                         None,
                         None,
                         {'A': '=/=', 'B': '!=', 'C': '<>', 'D': 'not =='},
                         ['B'],
                         ),
        33: QuizQuestion('''What will be the output of the following snippet?''',
                         '''
                         a = 1  
                         b = 0  
                         a = a ^ b  
                         b = a ^ b  
                         a = a ^ b  
                         print (a, b)''',
                         None,
                         None,
                         {'A': '1 1', 'B': '0 0', 'C': '1 0', 'D': '0 1'},
                         ['D'],
                         ),
        34: QuizQuestion('''How many stars (*) will the following snippet send to the console?''',
                         '''
                         i = 0  
                         while i < i + 2:  
                           i += 1  
                           print("*")  
                         else:  
                           print("*")''',
                         None,
                         None,
                         {'A': 'zero', 'B': 'the snippet will enter an infinite loop, printing one star per line',
                          'C': 'one', 'D': 'two'},
                         ['B'],
                         ),
        35: QuizQuestion('''How many hashes (*) will the following snippet send to the console?''',
                         '''
                         lst = [[x for x in range(3)] for y in range(3)]  
                         for r in range(3):  
                            for c in rang(3):  
                              if lst[r][c] % 2 != 0:  
                                print("#")''',
                         None,
                         None,
                         {'A': 'nine', 'B': 'zero', 'C': 'three', 'D': 'six'},
                         ['C'],
                         )
        }
