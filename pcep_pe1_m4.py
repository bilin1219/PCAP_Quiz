from quiz_struct import QuizQuestion

quiz_header = "PCAP Programming Essentials in Python Essentials 1 PE1 Module 4"
quiz_description = """
    PCAP Programming Essentials in Python Essentials 1 PE1 Module 4"""
quiz_information = """
    PCAP Programming Essentials in Python Essentials 1 PE1 Module 4  
    Test Quizzes Exam Answers"""
quiz_link = "[Click here to learn more >](https://pythoninstitute.org/pcap)"

# Define the questions, correct answers, and possible answers
quiz = {1: QuizQuestion(
    '''Which of the following lines properly starts a function using two parameters, both withzeroed default values?''',
    None,
    None,
    None,
    {'A': 'def fun (a=b=0) :', 'B': 'def fun (a=0, b=0) :', 'C': 'fun fun (a=0, b) :', 'D': 'fun fun (a, b=0) :'},
    ['B'],
    ),
    2: QuizQuestion('''What is the output of the following snippet?''',
                    '''
                    def fun(x):  
                      if x % 2 == 0:  
                        return 1  
                      else:  
                        return  
                        
                    print(fun(fun(2)) + 1)''',
                    None,
                    None,
                    {'A': '1', 'B': 'None', 'C': 'the code will cause a runtime error', 'D': '2'},
                    ['C'],
                    ),
    3: QuizQuestion('''Which of the following statement are true? (Select two answers)''',
                    None,
                    None,
                    None,
                    {'A': 'The None value can be assigned to variables',
                     'B': 'The None value cannot be used outside functions',
                     'C': 'The None value can be used as an argument of arithmetic operators',
                     'D': 'The None value can be compared with variables'},
                    ['A', 'D'],
                    ),
    4: QuizQuestion('''The following snippet:''',
                    '''
                    def func_1(a):  
                      return a ** a  
                      
                    def func_2(a): 
                      return func_1(a) * func_1(a)  
                      
                    print(func_2(2))''',
                    None,
                    None,
                    {'A': 'will output 2', 'B': 'will output 16',
                     'C': 'will output 4', 'D': 'is erroneous'},
                    ['B'],
                    ),
    5: QuizQuestion(
        '''What code would you insert instead of the comment to obtain the expected output? Expected output: abc''',
        '''
        dictionary = {}  
        my_list = ['a', 'b', 'c', 'd']  
        for i in range(len(my_list) - 1):  
          dictionary[my_list[i]] = (my_list[i], )
          
        for i in sorted(dictionary.key()):  
          k = dictionary[i] 
          # Insert your code here.''',
        None,
        None,
        {'A': 'print(k["0"])', 'B': "print(k['0'])", 'C': 'print(k)', 'D': 'print(k[0])'},
        ['D'],
    ),
    6: QuizQuestion('''The following snippet:''',
                    '''
                    def func(a, b):  
                      return a ** a  
                    
                    print(func(2))''',
                    None,
                    None,
                    {'A': 'is erroneous', 'B': 'will output 2', 'C': 'will output 4', 'D': 'will return None'},
                    ['A'],
                    ),
    7: QuizQuestion('''What is the output of the following snippet?''',
                    '''
                    def fun(inp=2, out=3):  
                      return inp * out  
                      
                    print(fn(out =2))''',
                    None,
                    None,
                    {'A': '2', 'B': '6', 'C': '4', 'D': 'the snippet is erroneous'},
                    ['C'],
                    ),
    8: QuizQuestion(
        '''Assuming that my_tuple is a correctly created tuple, the fact that tuples are immutablemeans that the following instruction:''',
        '''my_tuple[1] = my_tuple[1] + my_tuple[0]''',
        None,
        None,
        {'A': 'can be executed if and only if the tuple contains at least two elements', 'B': 'is illegal',
         'C': 'may be illegal if the tuple contains string', 'D': 'is fully correct'},
        ['B'],
    ),
    9: QuizQuestion('''A function defined in the following way: (Select two answers)''',
                    '''
                    def function(x=0):  
                      return x''',
                    None,
                    None,
                    {'A': 'may be invoked with exactly one argument',
                     'B': 'must be invoked with exactly one argument', 'C': 'must be invoked without any argument',
                     'D': 'may be invoked without any argument'},
                    ['A', 'D'],
                    ),
    10: QuizQuestion('''What is the output o the following snippet?''',
                     '''
                     def fun(x):  
                       x += 1  
                       return x
                     
                     x = 2  
                     x = fun(x + 1)  
                     print(x)''',
                     None,
                     None,
                     {'A': '3', 'B': '5', 'C': 'the code erroneous', 'D': '4'},
                     ['D'],
                     ),
    11: QuizQuestion('''What is the output of the following snippet?''',
                     '''
                     my_list = ['Mary', 'had', 'a', 'little', 'lamb']  
                     def my_list(my_list):  
                       del my_list[3]  
                       mylist[3] = 'ram'
                         
                     print(my_list(my_list))''',
                     None,
                     None,
                     {'A': '[\'Mary\', \'had\', \'a\' ,\'lamb\']',
                      'B': '[\'Mary\', \'had\', \'a\' ,\'ram\']',
                      'C': '[\'Mary\', \'had\', \'a\' ,\'little\', \'lamb\']',
                      'D': 'no output, the snippet is erroneous'},
                     ['D'],
                     ),
    12: QuizQuestion('''What is the output of the following snippet?''',
                     '''
                     def f(x):   
                       if x == 0:  
                         return 0  
                       return x + f(x - 1)
                         
                     print(f(3))''',
                     None,
                     None,
                     {'A': '6', 'B': 'the code is erroneous', 'C': '1', 'D': '3'},
                     ['A'],
                     ),
    13: QuizQuestion('''What is the output of the following snippet?''',
                     '''
                     tup = (1, 2, 4, 8)  
                     tup = tup[1:-1]  
                     tup = tup[0]  
                     print(tup)''',
                     None,
                     None,
                     {'A': 'the snippet is erroneous', 'B': '(12)', 'C': '(2, )', 'D': '2'},
                     ['D'],
                     ),
    14: QuizQuestion('''What is the output of the following snippet?''',
                     '''
                     def fun(x):  
                       global y  
                       y = x * x  
                       return y  
                       
                     fun(2)  
                     print(y)''',
                     None,
                     None,
                     {'A': 'the code will cause a runtime error', 'B': '4',
                      'C': 'None', 'D': '2'},
                     ['B'],
                     ),
    15: QuizQuestion('''What is the output of the following snippet?''',
                     '''
                     dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}  
                     v = dictionary['one']  
                     for k in range(len(dictionary)):  
                       v = dictionary[v]  
                     print(v)''',
                     None,
                     None,
                     {'A': 'three', 'B': 'one', 'C': '(\'one\', \'two\', \'three\')', 'D': 'two'},
                     ['D'],
                     ),
    16: QuizQuestion(
        '''Select the true statements about the try-exception block in relation to the followingexample. (Select two answers.)''',
        '''
        try:  
          # Some code is here...  
        except:  
          # some code is here...''',
        None,
        None,
        {'A': 'if you suspect that a snippet may raise an exception, you should place it in the try block',
         'B': 'The code that follows the try statement will be executed if the code in the except clause runs into an error.',
         'C': 'The code that follows the except statement will be executed if the code in the try clause runs into an error.',
         'D': 'If there is a syntax error in code located in the try block, the except branch will not handle it, and a SyntaxError exception will be raised instead.'},
        ['A', 'C'],
    ),
    17: QuizQuestion('''Which one if the following lines properly starts a parameterless function definition?''',
                     None,
                     None,
                     None,
                     {'A': 'def fun:', 'B': 'def fun():', 'C': 'function fun():', 'D': 'fun function():'},
                     ['B'],
                     ),
    18: QuizQuestion('''What is the output of the following snippet?''',
                     '''
                     def fun(x, y, x):  
                       return x + 2 * y + 3 * z  
                     
                     print(fun(0, z=1, y=3))''',
                     None,
                     None,
                     {'A': '9', 'B': '0', 'C': '3', 'D': 'the snippet is erroneous'},
                     ['A'],
                     ),
    19: QuizQuestion('''What is the output of the following code?''',
                     '''
                     try:  
                       value = input("Enter a value: ")  
                       print(value/value)  
                     except:  
                       print("Bad input...")
                     except ZeroDivisionError:  
                       print("Very bad input...")  
                     except TypeError:  
                       print("Very very bad input...")  
                     except:  
                       print("Booo!")''',
                     None,
                     None,
                     {'A': 'Booo!', 'B': 'Bad input...',
                      'C': 'Very very bad input...',
                      'D': 'Very bad input...'},
                     ['C'],
                     ),
    20: QuizQuestion('''What is the output of the following snippet?''',
                     '''
                     def any():  
                       print(var + 1, end ='')
                         
                     var = 1  
                     any()  
                     print(var)''',
                     None,
                     None,
                     {'A': '12', 'B': '22', 'C': '11', 'D': '21'},
                     ['D'],
                     ),
    21: QuizQuestion('''The fact that tuples belong to sequence types means that:''',
                     None,
                     None,
                     None,
                     {'A': 'they can be indexed and sliced like lists',
                      'B': 'they can be extended using the .append() method',
                      'C': 'they can be modified using the del instruction',
                      'D': 'they are actually lists'},
                     ['A'],
                     ),
    22: QuizQuestion('''A built-in function is a function which:''',
                     None,
                     None,
                     None,
                     {'A': 'is hidden from programmers',
                      'B': 'has been placed within your code by another programmer',
                      'C': 'has to be imported before use',
                      'D': 'comes with Python, ans is an integer part of Python'},
                     ['D'],
                     )
}
