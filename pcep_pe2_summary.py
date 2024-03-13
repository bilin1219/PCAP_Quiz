from quiz_struct import QuizQuestion

quiz_header = "PCAP Programming Essentials in Python Essentials 2 PE2 Summary"
quiz_description = """
    PCAP Programming Essentials in Python Essentials 2 PE2 Summary"""
quiz_information = """
    PCAP Programming Essentials in Python Essentials 2 PE2 Summary  
    Test Quizzes Exam Answers"""
quiz_link = "[Click here to learn more >](https://pythoninstitute.org/pcap)"

# Define the questions, correct answers, and possible answers
quiz = {1: QuizQuestion('''The following code:''',
                        '''
                        x = "\\\\"  
                        print(len(x))''',
                        None,
                        None,
                        {'A': 'will print 1', 'B': 'will print 2', 'C': 'will cause an error', 'D': 'will print 3'},
                        ['B'],
                        ),
        2: QuizQuestion(
            '''What information can be read using the uname function provided by the os module? (Select two answers)''',
            '''
            import os  
            os.mkdir('pictures')  
            os.chdir('pictures')  
            print(os.getcwd())''',
            None,
            None,
            {'A': 'Last login date.', 'B': 'Current path', 'C': 'Operating system name', 'D': 'Hardware identifier'},
            ['C', 'D'],
        ),
        3: QuizQuestion('''The following statement:''',
                        '''assert var != 0''',
                        None,
                        None,
                        {'A': 'is erroneous', 'B': 'has no effect', 'C': 'will stop the program when var == 0',
                         'D': 'will stop the program when var !=0'},
                        ['C'],
                        ),
        4: QuizQuestion('''What is the except output of the following code?''',
                        '''
                        class A:  
                            A = 1  
                            def __init__(self):  
                                self.a = 0  

                        print(hasattr(A, 'a'))''',
                        None,
                        None,
                        {'A': '0', 'B': 'True', 'C': '1', 'D': 'False'},
                        ['D'],
                        ),
        5: QuizQuestion('''What is the excepted result of the following code?''',
                        '''
                        from datetime import timedelta  
                        delta = timedelta(weeks = 1, days = 7, hours = 11)  
                        print(delta * 2)''',
                        None,
                        None,
                        {'A': '28 days, 22:00:00',
                         'B': '2 weeks, 14 days, 22 hours',
                         'C': '7 days, 22:00:00',
                         'D': 'The code will raise an exception'},
                        ['A'],
                        ),
        6: QuizQuestion('''What is the excepted output of the following code?''',
                        '''
                        class A:  
                            def __init__(self, v=2)  
                            def set(self, v=1):  
                                self.v += v  
                                return self.v  
                        a = A()  
                        b = a  
                        b.set()  
                        print(a.v)''',
                        None,
                        None,
                        {'A': '1', 'B': '0', 'C': '2', 'D': '3'},
                        ['D'],
                        ),
        7: QuizQuestion('''What is the expected effect of running the following code?''',
                        '''
                        class A:  
                            def __init__(self, v):  
                                self.__a = v + 1  

                        a = A(0)  
                        print(a.__a)''',
                        None,
                        None,
                        {'A': 'The code will raise an AttributeError except',
                         'B': 'The code will print 2', 'C': 'The code will print 0',
                         'D': 'The code will print 1'},
                        ['A'],
                        ),
        8: QuizQuestion(
            '''Knowing that a function named fun() resides in a module named mod, and was imported usingthe following statement:''',
            '''from mod import fun''',
            '''choose the right to invoke the fun() function:''',
            None,
            {'A': 'mod:fun()', 'B': 'mod::fun()', 'C': 'fun()', 'D': 'mod.fun()'},
            ['C'],
        ),
        9: QuizQuestion('''What output will appear after running the following snippet?''',
                        None,
                        None,
                        None,
                        {'A': 'The number of all the entities residing in the math module',
                         'B': 'A string containing the fully qualified name of the module', 'C': 'An error message',
                         'D': 'A list of all the entities residing in the math module'},
                        ['D'],
                        ),
        10: QuizQuestion('''Look at the code below:''',
                         '''
                         import random  
                         #  
                         # Insert lines of code here.  
                         #  
                         print(a, b, c)''',
                         '''Which lines of code would you insert so that it is possible for the program to output the followingresult:''',
                         '''6 82 0''',
                         {
                             'A': 'a = random.randint(0, 100) b = random.randrange(10, 100, 3) c = random.choice((0, 100, 3))',
                             'B': 'a = random.choice((0, 100, 3)) b = random.randrange(10, 100, 3) c = random.randint(0, 100)',
                             'C': 'a = random.randrange(10, 100, 3) b = random.randint(0, 100) c = random.choice((0, 100, 3))',
                             'D': 'a = random.randint(0, 100)b = random.choice((0, 100, 3))c = random.randrange(10, 100, 3)'},
                         ['A'],
                         ),
        11: QuizQuestion('''What is the expected result of the following code?''',
                         '''
                         from datetime import datetime  
                         datetime_1 = datetime(2019, 11, 27, 11, 27, 22)  
                         datetime_2 = datetime(2019, 11, 27, 0, 0, 0)  
                         print(datetime_1 - datetime_2)''',
                         None,
                         None,
                         {'A': 'o days', 'B': '0 days, 11:27:22', 'C': '11:27:22',
                          'D': '11 hours, 27 minutes, 22 seconds'},
                         ['C'],
                         ),
        12: QuizQuestion('''What is the expected result of the following code?''',
                         '''
                         import calendar  
                         calendar.setfirstweekday(calendar.SUNDAY)  
                         print(calendar.weekheader(3))''',
                         None,
                         None,
                         {'A': 'Su Mo Tu We Th We Fr Sa', 'B': 'Sun Mon Tue Wed Thu Fri Sat',
                          'C': 'Tu', 'D': 'Tue'},
                         ['B'],
                         ),
        13: QuizQuestion('''what is the expected result of executing the following code?''',
                         '''
                         class A:  
                            def a(self):  
                                print('a')  

                         class B:  
                            def a(self):  
                                print('b')  

                         class C(B, A):  
                            def c(self):  
                                self.a()  

                         o = C()  
                         o.c()''',
                         None,
                         None,
                         {'A': 'The code will print c', 'B': 'The code will raise an exception',
                          'C': 'The code will print b', 'D': 'The code will print a'},
                         ['C'],
                         ),
        14: QuizQuestion('''Look at the following code:''',
                         '''
                         numbers [0, 2, 7, 9, 10]  
                         # Insert line of code here.  
                         print(list(foo))''',
                         '''Which line would you insert in order for the program to produce the expected output?''',
                         '''[0, 4, 49, 81, 100]''',
                         {'A': 'foo = lambda num: num ** 2, numbers',
                          'B': 'foo = lambda num: num * 2, numbers)',
                          'C': 'foo = filter(lambda num: num ** 2, numbers)',
                          'D': 'foo = map(lambda num : num ** 2, numbers)'},
                         ['D'],
                         ),
        15: QuizQuestion('''What is the expected result of executing the following code?''',
                         '''
                         class I:  
                            def __init__(self):  
                                self.s = 'abc'  
                                self.i = 0   

                            def __init__(self):  
                                return self   
                                
                            def __next__(self):  
                                if self.i == len(self.s):  
                                    raise StopIteration  
                                v = self.s[self.i]  
                                self.i += 1  
                                return v  

                         for x in I():  
                            print(x, end='')''',
                         None,
                         None,
                         {'A': 'The code will print 210', 'B': 'The code will print abc',
                          'C': 'The code will print 012', 'D': 'The code will print cba'},
                         ['B'],
                         ),
        16: QuizQuestion('''The compiled Python bytecode is stored in files which have their names ending with:''',
                         None,
                         None,
                         None,
                         {'A': 'py', 'B': 'pyb', 'C': 'pc', 'D': 'pyc'},
                         ['D'],
                         ),
        17: QuizQuestion('''Which pip command would you use to uninstall a previously install package?''',
                         None,
                         None,
                         None,
                         {'A': 'pip delete packagename', 'B': 'pip --uninstall packagename',
                          'C': 'pip --remove packagename', 'D': 'pip uninstall packagename'},
                         ['D'],
                         ),
        18: QuizQuestion('''What is the excepted result of executing the following code?''',
                         '''
                         try:  
                            raise Exception(1, 2, 3)  
                         except Exception as e:  
                            print(len(e.args))''',
                         None,
                         None,
                         {'A': 'The code will raise an unhandled exception',
                          'B': 'The code will print 2', 'C': 'The code will print 3',
                          'D': 'The code will print 1'},
                         ['C'],
                         ),
        19: QuizQuestion('''What is the excepted result of the following snippet?''',
                         '''
                         try:  
                            raise Exceptionexcept BaseException: print("a")except Exception: print("b")except: print("c")''',
                         None,
                         None,
                         {'A': 'b', 'B': 'a', 'C': 'An error message', 'D': '1'},
                         ['B'],
                         ),
        20: QuizQuestion('''What is the expected result of executing the following code?''',
                         '''
                         class A:  
                            pass  
                            
                         class B(A):  
                            pass  
                            
                        class C(B):  
                            pass  
                            
                        print(issubclass(A, C))''',
                         None,
                         None,
                         {'A': 'The code will print Ture', 'B': 'The code will print 1',
                          'C': 'The code will print False',
                          'D': 'The code will raise an exception'},
                         ['C'],
                         ),
        21: QuizQuestion(
            '''If you want to fill a byte array with data read in from a stream, which method you can use?''',
            None,
            None,
            None,
            {'A': 'The read() method', 'B': 'The readbytes() method', 'C': 'The readfrom() method',
             'D': 'The readinto() method'},
            ['D'],
        ),
        22: QuizQuestion('''The following code:''',
                         '''print(float("1.3"))''',
                         None,
                         None,
                         {'A': 'will print 1.3', 'B': 'will print 13', 'C': 'will print 1,3',
                          'D': 'will raise a ValueError exception'},
                         ['A'],
                         ),
        23: QuizQuestion('''The following code:''',
                         '''print(chr(ord('p) + 2))''',
                         '''will print:''',
                         None,
                         {'A': 'q', 'B': 's', 'C': 'r', 'D': 't'},
                         ['C'],
                         ),
        24: QuizQuestion('''If there are more than one except: branch after the try: clause, we can say that:''',
                         None,
                         None,
                         None,
                         {'A': 'exactly one except: block will be executed',
                          'B': 'one or more except: blocks will be executed',
                          'C': 'not more than one except: block will be executed',
                          'D': 'none of the except: blocks will be executed'},
                         ['C'],
                         ),
        25: QuizQuestion('''If the class constructor is declared in the following way:''',
                         '''
                         class Class:  
                            def __init__(self, vla = 0):  
                                pass''',
                         '''which one of the assignments is invalid?''',
                         None,
                         {'A': 'object = Class(1)', 'B': 'object = Class(None)',
                          'C': 'object = Class(1, 2)', 'D': 'object = Class()'},
                         ['C'],
                         ),
        26: QuizQuestion('''What is the expected result of the following snippet?''',
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
                         {'A': 'The code will cause a syntax error', 'B': '1', 'C': 'b', 'D': 'a'},
                         ['A'],
                         ),
        27: QuizQuestion('''What is the expected result of the following code?''',
                         '''
                         def my_fun(n):  
                            s = '+'  
                            for i in range(n):  
                                s += s  
                                yield s  

                         for x in my_fun(2):  
                            print(x, end='')''',
                         None,
                         None,
                         {'A': 'The code will print +', 'B': 'The code will print +++',
                          'C': 'The code will print ++', 'D': 'The code will print ++++++'},
                         ['D'],
                         ),
        28: QuizQuestion('''Look at the following code:''',
                         '''
                         numbers = [i*i for i in range(5)]  
                         # Insert line of code here.  
                         print(foo)''',
                         '''Which line would you insert in order for the program to produce the expected output?''',
                         '''[1, 9]''',
                         {'A': 'foo = list(filter(lambda x: x % 2, numbers))',
                          'B': 'foo = list(filter(lambda x: x / 2, numbers))',
                          'C': 'foo = list(map(lambda x: x % 2, numbers))',
                          'D': 'foo = list(map(lambda x: x // 2, numbers))'},
                         ['A'],
                         ),
        29: QuizQuestion('''What is the expected result of executing the following code?''',
                         '''
                         def o(p):  
                            def q():  
                                return '*' * p  
                            return q  

                         r = o(1)  
                         s = o(2)  
                         print(r() + s())''',
                         None,
                         None,
                         {'A': 'The code will print ***', 'B': 'The code will print ****', 'C': 'The code will print *',
                          'D': 'The code will print **'},
                         ['A'],
                         ),
        30: QuizQuestion('''The following statement:''',
                         '''from a.b import c''',
                         '''causes the import of:''',
                         None,
                         {'A': 'entity a from module b from package c',
                          'B': 'entity b from module a from package c',
                          'C': 'entity c from module a from package b',
                          'D': 'entity c from module b from package a'},
                         ['D'],
                         ),
        31: QuizQuestion('''The sys.stderr stream is normally associated with:''',
                         None,
                         None,
                         None,
                         {'A': 'the keyboard', 'B': 'the printer', 'C': 'a null device', 'D': 'the screen'},
                         ['D'],
                         ),
        32: QuizQuestion('''What will be the output of the following code, located in the p.py file?''',
                         '''print(__name__)''',
                         None,
                         None,
                         {'A': 'main', 'B': 'p.py', 'C': '__main__', 'D': '__p.py__'},
                         ['C'],
                         ),
        33: QuizQuestion('''Assuming that the open() invocation has gone successfully, the following snippet:''',
                         '''
                         for x in open('file', 'rt')  
                            print(x)''',
                         '''will:''',
                         None,
                         {'A': 'read the file character by character', 'B': 'read the file line by line',
                          'C': 'read the whole file at once', 'D': 'cause an exception'},
                         ['B'],
                         ),
        34: QuizQuestion('''If a is a stream opened in read mod, the following line:''',
                         '''q = s.read(1)''',
                         '''will read:''',
                         None,
                         {'A': 'one line from the stream', 'B': 'one kilobyte from the stream',
                          'C': 'one buffer from the stream', 'D': 'one character from the stream'},
                         ['D'],
                         ),
        35: QuizQuestion('''The following line of code:''',
                         '''for line in open('text.txt', 'rt'):''',
                         None,
                         None,
                         {'A': 'is invalid because open returns nothing',
                          'B': 'is invalid because open returns a non-iterable object',
                          'C': 'is invalid because open returns an iterable object',
                          'D': 'may be valid if line is a list'},
                         ['C'],
                         ),
        36: QuizQuestion('''What is the expected result of the following code?''',
                         '''
                         import os  
                         os.mkdir('pictures')  
                         os.chdir('pictures')  
                         print(os.getcwd())''',
                         None,
                         None,
                         {'A': 'The code will print the owner of the created directory',
                          'B': 'The code will print the content of the created directory',
                          'C': 'The code will print the name of the created directory',
                          'D': 'The code will print the path to the created directory'},
                         ['D'],
                         ),
        37: QuizQuestion(
            '''Assuming that the following three files a.py, and c.py reside in the same directory, what willbe the output produced after running the c.py file?''',
            '''
            # file a.py  
            print("a", end='')  
            # file b.py  
            import a  
            print("b", end='')  
            # file c.py  
            print("c", end='')  

            import a  
            import b''',
            None,
            None,
            {'A': 'cab', 'B': 'cab', 'C': 'abc', 'D': 'bac'},
            ['A'],
        ),
        38: QuizQuestion('''What is the expected result of executing the following code?''',
                         '''
                         class A:  
                            def __init__(self):  
                                pass  
                                
                         a = A(1)  
                         print(hasattr(a, 'A'))''',
                         None,
                         None,
                         {'A': 'The code will print 1', 'B': 'The code will raise an exception',
                          'C': 'The code will print False', 'D': 'The code will print True'},
                         ['B'],
                         ),
        39: QuizQuestion('''The following code:''',
                         '''
                         x = " \\"  
                         print(len(x))''',
                         None,
                         None,
                         {'A': 'will print 1', 'B': 'will print 3', 'C': 'will print 2',
                          'D': 'will cause an error'},
                         ['C'],
                         ),
        40: QuizQuestion(
            '''Which of the following commands would you use to check pip's version? (Select two answers)''',
            None,
            None,
            None,
            {'A': 'pip version', 'B': 'pip --version', 'C': 'pip-version', 'D': 'pip3 --version'},
            ['B', 'D'],
        )
    }
