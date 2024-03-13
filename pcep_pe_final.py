from quiz_struct import QuizQuestion

quiz_header = "PCAP Programming Essentials in Python Essentials Final Exam"
quiz_description = """
    PCAP Programming Essentials in Python Essentials Final Exam"""
quiz_information = """
    PCAP Programming Essentials in Python Essentials Final Exam  
    Test Quizzes Exam Answers"""
quiz_link = "[Click here to learn more >](https://pythoninstitute.org/pcap)"

# Define the questions, correct answers, and possible answers
quiz = {1: QuizQuestion('''What is the expected output of the following snippet?''',
                        '''
                        a = True  
                        b = False  
                        a = a or bb = a and ba = a or b  
                        print(a, b)''',
                        None,
                        None,
                        {'A': 'False False', 'B': 'True False', 'C': 'False True', 'D': 'True False'},
                        ['D'],
                        ),
        2: QuizQuestion('''What is the expected output of the following snippet?''',
                        '''print(len([i for i in range(0, -2)]))''',
                        None,
                        None,
                        {'A': '3', 'B': '1', 'C': '2', 'D': '0'},
                        ['D'],
                        ),
        3: QuizQuestion('''How many stars * will the following snippet send to the console?''',
                        '''
                        i = 4  
                        while i > 0:  
                            i -= 2  
                            print("*")  
                            if i == 2:  
                                break  
                        else:  
                            print("*")''',
                        None,
                        None,
                        {'A': 'two', 'B': 'one', 'C': 'zero',
                         'D': 'The snippet will enter an infinite loop, constantly printing one * per line'},
                        ['B'],
                        ),
        4: QuizQuestion('''What is the sys.stdout stream normally associated with?''',
                        None,
                        None,
                        None,
                        {'A': 'The printer', 'B': 'The keyboard', 'C': 'A null device',
                         'D': 'The screen'},
                        ['D'],
                        ),
        5: QuizQuestion('''What is the excepted output of the following snippet?''',
                        '''
                        class X:  
                            pass  
                            
                        class Y(X):  
                            pass  
                            
                        class Z(Y):  
                            pass  
                            
                        x = X()  
                        z = Z()  
                        print(isinstance(x, z), isinstance(z, X))''',
                        None,
                        None,
                        {'A': 'True True', 'B': 'True False', 'C': 'False True', 'D': 'False False'},
                        ['C'],
                        ),
        6: QuizQuestion('''What is the excepted output of the following snippet?''',
                        '''
                        class A:  
                            def __init__(self,name):  
                                self.name = name  

                        a = A("class")  
                        print(a)''',
                        None,
                        None,
                        {'A': 'class', 'B': 'name', 'C': 'A number',
                         'D': 'A string ending with a long hexadecimal number'},
                        ['D'],
                        ),
        7: QuizQuestion('''What is the excepted result of executing the following code?''',
                        '''
                        class A:  
                            pass  
                            
                        class B:  
                            pass  
                            
                        class C(A, B):  
                            pass  
                            
                        print(issubclass(C, A) and issubclass(C, B))''',
                        None,
                        None,
                        {'A': 'The code will print True', 'B': 'The code will raise an exception',
                         'C': 'The code will print an empty line', 'D': 'The code will print False'},
                        ['A'],
                        ),
        8: QuizQuestion('''What is the excepted output of the following code?''',
                        '''
                        from datetime import datetime  
                        datetime = datatime(2019, 11, 27, 11, 27, 22)
                        print(datetime.strftime('%Y/%m/%d %H:%M:%S'))''',
                        None,
                        None,
                        {'A': '19/11/27 11:27:22', 'B': '2019/Nov/27 11:27:22',
                         'C': '2019/11/27 11:27:22', 'D': '2019/November/27 11:27:22'},
                        ['C'],
                        ),
        9: QuizQuestion('''What is the excepted output of the following code?''',
                        '''
                        my_string_1 = 'Bond'  
                        my_string_2 = 'James Bond'  
                        print(my_string_1.isalpha(), my_string_2.isalpha())''',
                        None,
                        None,
                        {'A': 'False True', 'B': 'True True', 'C': 'False False',
                         'D': 'True False'},
                        ['D'],
                        ),
        10: QuizQuestion('''The meaning of a Keyword argument is determined by its:''',
                         None,
                         None,
                         None,
                         {'A': 'both name and value assigned to it', 'B': 'position within the argument list',
                          'C': 'connection with existing variables', 'D': 'value only'},
                         ['A'],
                         ),
        11: QuizQuestion('''Knowing that the function named m, and the code contains the following import statement:''',
                         '''from f import m''',
                         '''Choose the right way to invoke the function:''',
                         None,
                         {'A': 'mod.f()', 'B': 'The function cannot be invoked because the import statement is invalid',
                          'C': 'f()', 'D': 'mod:f()'},
                         ['B'],
                         ),
        12: QuizQuestion('''The Exception class contains a property named args -what is it?''',
                         None,
                         None,
                         None,
                         {'A': 'A dictionary', 'B': 'A list', 'C': 'A string', 'D': 'A tuple'},
                         ['D'],
                         ),
        13: QuizQuestion('''What is PEP 8?''',
                         None,
                         None,
                         None,
                         {
                             'A': 'A document that provides coding conventions and style guide for the C code computing the Cimplementation of Python',
                             'B': 'A document that describes the development and release schedule for Python versions',
                             'C': 'A document that describes an extension to Pythonâ€™s import mechanism which improves sharing of Pythonsource code files',
                             'D': 'A document that provides coding conventions and style guide for Python code'},
                         ['D'],
                         ),
        14: QuizQuestion('''Which is the expected behavior of the following snippet?''',
                         '''
                         def fun(x):  
                            return 1 if x % 2 != else 2  

                        print(fun(fun(1)))''',
                         None,
                         None,
                         {'A': 'The program will output None', 'B': 'The code will cause a runtime error',
                          'C': 'The program will output 2', 'D': 'The program will output 1'},
                         ['B'],
                         ),
        15: QuizQuestion('''Which operator would you use to check whether two values are equal?''',
                         None,
                         None,
                         None,
                         {'A': '===', 'B': 'is', 'C': '==', 'D': '='},
                         ['C'],
                         ),
        16: QuizQuestion('''What is the name of the directory/folder created by Python used to store pyc files?''',
                         None,
                         None,
                         None,
                         {'A': '__pycfiles', 'B': '__pyc__', 'C': '__pycache__', 'D': '__cache__'},
                         ['C'],
                         ),
        17: QuizQuestion(
            '''What can you do if you want to tell your module users that a particular variable shouldnot be accessed directly?''',
            None,
            None,
            None,
            {'A': 'Start its name with __or__', 'B': 'Start its name with a capital letter',
             'C': 'Use its number instead of its name', 'D': 'Build its name with lowercase letters only'},
            ['A'],
        ),
        18: QuizQuestion('''What is the expected output of the following snippet?''',
                         '''
                         d = ('one': 1, 'three': 3, 'two':2)
                         for k in sorted(d.values()):  
                            print(k, end=' ')''',
                         None,
                         None,
                         {'A': '1 2 3', 'B': '3 1 2', 'C': '3 2 1', 'D': '2 3 1'},
                         ['A'],
                         ),
        19: QuizQuestion('''Select the true statements. (Select two answers)''',
                         None,
                         None,
                         None,
                         {
                             'A': 'The first parameter of a class method dose not have to be named self',
                             'B': 'The first parameter of a class method must be named self',
                             'C': 'If a class contains the __init__ method, it can return a value',
                             'D': 'If a class contains the __init__ method, it cannot return any value'},
                         ['A', 'D'],
                         ),
        20: QuizQuestion('''Select the true statements. (Select two answers)''',
                         None,
                         None,
                         None,
                         {'A': 'PyPI is short for Python Package Index',
                          'B': 'PyPI is the only existing Python repository',
                          'C': 'PyPI is one of many existing Python repository',
                          'D': 'PyPI is short for Python Package Installer'},
                         ['A', 'D'],
                         ),
        21: QuizQuestion('''What is the expected output of the following snippet?''',
                         '''
                         t = (1, 2, 3, 4)  
                         t = t[-2:-1]  
                         t = t[-1]  
                         print(t)''',
                         None,
                         None,
                         {'A': '(3)', 'B': '(3,)', 'C': '3', 'D': '33'},
                         ['C'],
                         ),
        22: QuizQuestion('''What is the expected effect of running the following code?''',
                         '''
                         class A:  
                            def __init__(self, v):  
                                self._a = v + 1  

                        a = A(0)  
                        print(a._a)''',
                         None,
                         None,
                         {'A': 'The code will raise an AttributeError exception', 'B': 'The code will output 1',
                          'C': 'The code will output 2', 'D': 'The code will output 0'},
                         ['B'],
                         ),
        23: QuizQuestion(
            '''Which of the following functions provided by the os module are available in bothWindows and Unix? (Select two answers)''',
            None,
            None,
            None,
            {'A': 'chdir()', 'B': 'getgid()', 'C': 'getgroups()', 'D': 'mkdir()'},
            ['A', 'D'],
        ),
        24: QuizQuestion('''What is the expected output of the following piece of code?''',
                         '''v = 1 + 1 // 2 + 1 / 2 + 2''',
                         None,
                         None,
                         {'A': '4.0', 'B': '3', 'C': '3.5', 'D': '4'},
                         ['C'],
                         ),
        25: QuizQuestion('''If s is a stream opened in read mode, the following line:''',
                         '''q = s.readlines()''',
                         '''will assign q as :''',
                         None,
                         {'A': 'dictionary', 'B': 'tuple', 'C': 'list', 'D': 'string'},
                         ['C'],
                         ),
        26: QuizQuestion('''Which of the following sentences is true about the snippet below?''',
                         '''
                         str_1 = 'string'  
                         str_2 = str_1[:]''',
                         None,
                         None,
                         {'A': 'str_1 is longer than str_2', 'B': 'str_1 and str_2 are different (but equal) strings',
                          'C': 'str_1 and str_2 are different names of the same string',
                          'D': 'str_2 is longer than str_1'},
                         ['B'],
                         ),
        27: QuizQuestion('''What is the expected result of executing the following code?''',
                         '''
                         class A:  
                            def __init__(self):  
                                pass 
                            def f(self):  
                                return 1  
                            def g():  
                                return self.f()  

                        a = A()  
                        print(a.g())''',
                         None,
                         None,
                         {'A': 'The code will output True', 'B': 'The code will output 0',
                          'C': 'The code will output 1', 'D': 'The code will raise an exception'},
                         ['D'],
                         ),
        28: QuizQuestion('''What is the expected output of the following code, located in the file module.py?''',
                         '''print(__name__)''',
                         None,
                         None,
                         {'A': 'main', 'B': 'modle.py', 'C': '__main__', 'D': '__module.py__'},
                         ['C'],
                         ),
        29: QuizQuestion('''What is the excepted output of the following code?''',
                         '''
                         def a(x):  
                            def b():  
                                return x + x  
                            return b  
                        x = a('x')  
                        y = a('')  
                        print(x() + y())''',
                         None,
                         None,
                         {'A': 'xx', 'B': 'xxxx', 'C': 'xxxxxx', 'D': 'x'},
                         ['A'],
                         ),
        30: QuizQuestion('''What is the excepted behavior of the following piece of code?''',
                         '''
                         x = 16  
                         while x > 0:  
                            print('*', end='')  
                            x //= 2''',
                         None,
                         None,
                         {'A': 'The code will output *****', 'B': 'The code will output ***',
                          'C': 'The code will output *', 'D': 'The code will error an infinite loop'},
                         ['A'],
                         ),
        31: QuizQuestion(
            '''A package directory/folder may contain a file intended to initialize the package. What isits name?''',
            None,
            None,
            None,
            {'A': 'init.py', 'B': '__init.py__', 'C': '__init__.', 'D': '__init__.py'},
            ['D'],
        ),
        32: QuizQuestion('''If there is a finally: branch inside the try: block, we can say that:''',
                         None,
                         None,
                         None,
                         {'A': 'the finally: branch will always be executed',
                          'B': 'the finally: branch wonâ€™t be executed if any of the except: branch is executed',
                          'C': 'the finally: branch wonâ€™t be executed if no exception is raised',
                          'D': 'the finally: branch will be executed when there is no else: branch'},
                         ['A'],
                         ),
        33: QuizQuestion('''What value will be assigned to the x variable?''',
                         '''
                         z = 2  
                         y = 1  
                         x = y < z or z > y and y > z or z < y''',
                         None,
                         None,
                         {'A': 'True', 'B': 'False', 'C': '0', 'D': '1'},
                         ['A'],
                         ),
        34: QuizQuestion('''If you want to write a byte arrayâ€™s content to a stream, which method can you use?''',
                         None,
                         None,
                         None,
                         {'A': 'writeto()', 'B': 'writefrom()', 'C': 'write()', 'D': 'writebytearray()'},
                         ['C'],
                         ),
        35: QuizQuestion('''What is the expected behavior of the following snippet?''',
                         '''
                         try: 
                            raise Exceptionexcept:  
                            print("c")  
                        except BaseException:  
                            print("a")  
                        except Exception:  
                            print("b")''',
                         None,
                         None,
                         {'A': 'The code will cause an error', 'B': 'The code will output b',
                          'C': 'The code will output c', 'D': 'The code will output a'},
                         ['A'],
                         ),
        36: QuizQuestion('''What is true about the following code snippet?''',
                         '''
                         def fun(par2, par1):  
                            return par2 + par1  

                        print(fun(par2 = 1, 2))''',
                         None,
                         None,
                         {'A': 'The code is erroneous',
                          'B': 'The code will output 3',
                          'C': 'The code will output 2',
                          'D': 'The code will output 1'},
                         ['A'],
                         ),
        37: QuizQuestion('''What is the expected output of the following piece of code?''',
                         '''
                         x, y, z = 3, 2, 1  
                         z, y, x = x, y, z  
                         print(x, y, z)''',
                         None,
                         None,
                         {'A': '2 1 3', 'B': '1 2 2', 'C': '3 2 1', 'D': '1 2 3'},
                         ['D'],
                         ),
        38: QuizQuestion('''What is the expected output of the following snippet?''',
                         '''
                         d = {}  
                         d['2'] = [1, 2]  
                         d['1'] = [3, 4]  
                         for x in d.keys():  
                            print(d[x][1], end="")''',
                         None,
                         None,
                         {'A': '24', 'B': '31', 'C': '13', 'D': '42'},
                         ['A'],
                         ),
        39: QuizQuestion('''What is the expected output of the following snippet?''',
                         '''
                         try: 
                            raise Exceptionexcept BaseException: print("a", end='')else: print("b", end='')finnaly: print("c")''',
                         None,
                         None,
                         {'A': 'bc', 'B': 'a', 'C': 'ab', 'D': 'ac'},
                         ['D'],
                         ),
        40: QuizQuestion('''If the class constructor is declared as below:''',
                         '''
                         class Class:  
                            def __init__(self):  
                                pass''',
                         '''which one of the assignments is valid?''',
                         None,
                         {'A': 'object = Class()', 'B': 'object = Class(1,2)',
                          'C': 'object = Class(None)', 'D': 'object = Class(1)'},
                         ['A'],
                         ),
        41: QuizQuestion('''What is the expected output of the following code?''',
                         '''
                         from datetime import timedelta  
                         delta = timedelta(weeks = 1, days = 7, hours = 11)  
                         print(delta)''',
                         None,
                         None,
                         {'A': '7 days, 11:00:00', 'B': '2 weeks, 11:00:00', 'C': '1 week, 7 days, 11 hours',
                          'D': '14 days, 11:00:00'},
                         ['D'],
                         ),
        42: QuizQuestion(
            '''What is the expected output of the following piece of code if the user enters two lines containing 1 and 2 respectively?''',
            '''
            y = input()  
            x = input()  
            print(x + y)''',
            None,
            None,
            {'A': '2', 'B': '21', 'C': '12', 'D': '3'},
            ['B'],
        ),
        43: QuizQuestion('''What is the expected behavior of the following snippet?''',
                         '''
                         my_string = 'abcdef'  
                         def fun(s):  
                            del s[2]  
                            return s  
                        print(fun(my_string))''',
                         None,
                         None,
                         {'A': 'The program will cause an error', 'B': 'The program will output abdef',
                          'C': 'The program will output acdef', 'D': 'The program will output abcef'},
                         ['A'],
                         ),
        44: QuizQuestion('''What is true about the following snippet?''',
                         '''
                         def fun(d, k, v):  
                            d[k] = v  

                        my_dictionary = {}  
                        print(fun(my_dictionary, '1', 'v'))''',
                         None,
                         None,
                         {'A': 'The code is erroneous', 'B': 'The code will output None',
                          'C': 'The code will output v', 'D': 'The code will output 1'},
                         ['B'],
                         ),
        45: QuizQuestion('''What is the expected output of the following code?''',
                         '''
                         class A:  
                            A = 1  
                            def __init__(self):  
                                self.a = 0  

                        print(hasattr(A, 'A'))''',
                         None,
                         None,
                         {'A': 'False', 'B': '1', 'C': '0', 'D': 'True'},
                         ['D'],
                         ),
        46: QuizQuestion('''What is the expected behavior of the following code?''',
                         '''x = """"""print(len(x))''',
                         None,
                         None,
                         {'A': 'The code will output 2', 'B': 'The code will output 3',
                          'C': 'The code will cause an error', 'D': 'The code will output 1'},
                         ['D'],
                         ),
        47: QuizQuestion('''What is the expected output of the following code?''',
                         '''
                         import calendar  
                         c = calendar.Calendar(calendar.SUNDAY)  
                         for weekday in c.iterweekdays():  
                            print(weekday, end=" ")''',
                         None,
                         None,
                         {'A': '7 1 2 3 4 5 6', 'B': '6 0 1 2 3 4 5', 'C': 'Su Mo Tu We Th Fr Sa', 'D': 'Su'},
                         ['B'],
                         ),
        48: QuizQuestion('''What is the expected output of the following code?''',
                         '''
                         def fun(n):  
                            s = ' '  
                            for i in range(n):  
                                s += '*'  
                                yield s  
                                
                        for x in fun(3):  
                            print(x, end='')''',
                         None,
                         None,
                         {'A': '****', 'B': '******', 'C': '2***', 'D': '*'},
                         ['B'],
                         ),
        49: QuizQuestion('''What is the expected output of the following code?''',
                         '''
                         t = (1, )  
                         t = t[0] + t[0]  
                         print(t)''',
                         None,
                         None,
                         {'A': '2', 'B': '(1, )', 'C': '(1, 1)', 'D': '1'},
                         ['A'],
                         ),
        50: QuizQuestion('''What is the expected result of executing the following code?''',
                         '''
                         class A:  
                            def a(self):  
                                print('a')  

                        class B:  
                            def a(self):  
                                print('b')  

                        class C(A, B):  
                            def c(self):  
                                self.a()  

                        o = C()  
                        o.c()''',
                         None,
                         None,
                         {'A': 'The code will print c', 'B': 'The code will print a',
                          'C': 'The code will raise an exception', 'D': 'The code will print b'},
                         ['B'],
                         ),
        51: QuizQuestion('''What is the expected behavior of the following code snippet?''',
                         '''
                         my_list = [1, 2, 3, 4]  
                         my_list = list(map(lambda x: 2*x, my_list))  
                         print(my_list)''',
                         None,
                         None,
                         {'A': 'The code will cause a runtime error', 'B': 'The code will output 1 2 3 4',
                          'C': 'The code will output 10', 'D': 'The code will output 2 4 6 8'},
                         ['D'],
                         ),
        52: QuizQuestion('''What is the expected behavior of the following piece of code?''',
                         '''
                         d = {1: 0, 2: 1, 3: 2, 0: 1}  
                         x = 0  
                         for y in range(len(d)):  
                            x = d[x]print(x)''',
                         None,
                         None,
                         {'A': 'The code will output 0', 'B': 'The code will output 1',
                          'C': 'The code will cause a runtime error',
                          'D': 'The code will output 2'},
                         ['A'],
                         ),
        53: QuizQuestion(
            '''What pip operation would you use to check what Python packages have been installedso far?''',
            None,
            None,
            None,
            {'A': 'show', 'B': 'list', 'C': 'help', 'D': 'dir'},
            ['B'],
        ),
        54: QuizQuestion('''What is true about the following line of code?''',
                         '''print(len((1, )))''',
                         None,
                         None,
                         {'A': 'The code will output 0', 'B': 'The code is erroneous', 'C': 'The code will output 1',
                          'D': 'The code will output 2'},
                         ['C'],
                         ),
        55: QuizQuestion('''Which line properly invokes the function defined as below?''',
                         '''
                         def fun(a, b, c=0):  
                            # function body''',
                         None,
                         None,
                         {'A': 'fun(b=0, b=0)', 'B': 'fun(a=1, b=0, c=0)', 'C': 'fun(1, c=2)',
                          'D': 'fun(0)'},
                         ['B'],
                         ),
        56: QuizQuestion('''What is the expected behavior of the following code?''',
                         '''
                         import os  
                         os.makedirs('pictures/thumbnails')  
                         os.rmdir('pictures')''',
                         None,
                         None,
                         {'A': 'The code will delete both the pictures and thumbnails directories',
                          'B': 'The code will delete the pictures directory only', 'C': 'The code will raise an error',
                          'D': 'The code will delete the thumbnails directory only'},
                         ['C'],
                         ),
        57: QuizQuestion('''What is true about the following piece of code?''',
                         '''print("a", "b", "c", sep=" ' ")''',
                         None,
                         None,
                         {'A': 'The code is erroneous', 'B': 'The code will output abc',
                          'C': "The code will output a'b'c", 'D': 'The code will output a b c'},
                         ['C'],
                         ),
        58: QuizQuestion('''What is the expected behavior of the following code?''',
                         '''
                         x = "\"  
                         print(len(x))''',
                         None,
                         None,
                         {'A': 'The code will output 3', 'B': 'The code will cause an error',
                          'C': 'The code will output a2', 'D': 'The code will output 1'},
                         ['B'],
                         ),
        59: QuizQuestion('''What is the expected output of the following code?''',
                         '''
                         class A:  
                            A = 1  
                            def __init__(self, v=2):  
                                self.v = v + A.A  
                                A.A += 1  
                            def set(self, v):  
                                self.v +=v  
                                A.A += 1  
                                return  

                        a = A()  
                        a.set(2)  
                        print(a.v)''',
                         None,
                         None,
                         {'A': '7', 'B': '1', 'C': '3', 'D': '5'},
                         ['D'],
                         ),
        60: QuizQuestion('''How many empty lines will the following snippet send to the console?''',
                         '''
                        my_list = [[c for c in range(r)] for r in range(3)]  
                        for element in my_list:  
                            if len(element) < 2:  
                                print()''',
                         None,
                         None,
                         {'A': 'two', 'B': 'three', 'C': 'zero', 'D': 'one', 'E': '99'},
                         ['A'],
                         )
        }
