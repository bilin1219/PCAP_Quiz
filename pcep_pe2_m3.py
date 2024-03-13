from quiz_struct import QuizQuestion

quiz_header = "PCAP Programming Essentials in Python Essentials 2 PE2 Module 3"
quiz_description = """
    PCAP Programming Essentials in Python Essentials 2 PE2 Module 3"""
quiz_information = """
    PCAP Programming Essentials in Python Essentials 2 PE2 Module 3  
    Test Quizzes Exam Answers"""
quiz_link = "[Click here to learn more >](https://pythoninstitute.org/pcap)"

# Define the questions, correct answers, and possible answers
quiz = {1: QuizQuestion('''What will be the result of executing the following code?''',
                        '''
                        class Ex(Exception):  
                            def_init_(self,msg):  
                                Exception._init_(self,msg + msg)  
                                self.args = (msg,)  
                                try:  
                                    raise Ex('ex')  
                                except Ex as e:  
                                    print(e)  
                                except Exception as e:  
                                    print(e)''',
                        None,
                        None,
                        {'A': 'it will print ex', 'B': 'it will print exex', 'C': 'it will print an empty line',
                         'D': 'it will raise an unhandled exception'},
                        ['A'],
                        ),
        2: QuizQuestion('''A data structure described as LIFO is actually a:''',
                        None,
                        None,
                        None,
                        {'A': 'list', 'B': 'stack', 'C': 'heap', 'D': 'tree'},
                        ['B'],
                        ),
        3: QuizQuestion('''What will be the output of the following code?''',
                        '''
                        class A:  
                            A = 1  
                            print(hasattr(A, 'A'))''',
                        None,
                        None,
                        {'A': '0', 'B': 'False', 'C': '1', 'D': 'True'},
                        ['D'],
                        ),
        4: QuizQuestion('''What will be the effect of running the following code?''',
                        '''
                        class A:  
                            def_init_(self,v):  
                            self._a = v + 1  

                        a = A(0)  
                        print(a._a)''',
                        None,
                        None,
                        {'A': '2', 'B': 'The code will raise an AttributeError exception', 'C': '0', 'D': '1'},
                        ['B'],
                        ),
        5: QuizQuestion('''What will be the result of executing the following code?''',
                        '''
                        class A:  
                            pass  
                            
                        class B(A):  
                            pass  
                            
                        class C(B):  
                            pass  
                            
                        print(issubclass(C,A))''',
                        None,
                        None,
                        {'A': 'it will print 1', 'B': 'it will print False',
                         'C': 'it will print True', 'D': 'it will raise an exception'},
                        ['C'],
                        ),
        6: QuizQuestion('''What will be the result of executing the following code?''',
                        '''
                        class A:  
                            def_str_(self):  
                            return 'a'  

                        class B:  
                            def_str_(self):  
                            return 'b'  

                        class C(A, B):  
                            pass  
                            
                        o = C()  
                        print(o)''',
                        None,
                        None,
                        {'A': 'it will print b', 'B': 'it will print c', 'C': 'it will print a',
                         'D': 'it will raise an exception'},
                        ['C'],
                        ),
        7: QuizQuestion('''What will be the result of executing the following code?''',
                        '''
                        class A:  
                            def a(self):  
                                print('a')  

                        class B:  
                            def a(self):  
                                self.a()  

                        o = C()  
                        o.c()''',
                        None,
                        None,
                        {'A': 'it will raise an exception', 'B': 'it will print a',
                         'C': 'it will print c', 'D': 'it will print b'},
                        ['D'],
                        ),
        8: QuizQuestion('''What will be the result of executing the following code?''',
                        '''
                        try:  
                            raise Exception(1,2,3)  
                        except Exception as e:  
                            print (len(e.args))''',
                        None,
                        None,
                        {'A': 'it will print 1', 'B': 'it will print 2', 'C': 'it will raise as unhandled exception',
                         'D': 'it will print 3'},
                        ['D'],
                        ),
        9: QuizQuestion('''What will be the output of the following code?''',
                        '''
                        class A:  
                            X = 0  
                            def __init__(self,v = 0):  
                                self.Y = v  
                                A.X += v  

                        a = A()  
                        b = A(1)  
                        c = A(2)  
                        print(c.X)''',
                        None,
                        None,
                        {'A': '2', 'B': '3', 'C': '0', 'D': '1'},
                        ['B'],
                        ),
        10: QuizQuestion(
            '''If the classâ€™s constructor is declared as below, which one of the assignments is valid?''',
            '''
            class Class:  
                def __init__(self):  
                    pass''',
            None,
            None,
            {'A': 'object = Class', 'B': 'object = Class()', 'C': 'object = Class(self)',
             'D': 'object = Class(object)'},
            ['B'],
        ),
        11: QuizQuestion('''What will be the result of executing the following code?''',
                         '''
                         def f(x):  
                            try:  
                                x = x / x  
                            except:  
                                print("a",end='')  
                            else:  
                                print("b",end='')  
                            finally:  
                                print("c",end='')  

                            f(1)f(0)''',
                         None,
                         None,
                         {'A': 'it will raise an unhandled exception', 'B': 'it will print bcac',
                          'C': 'it will print acac', 'D': 'it will print bcbc'},
                         ['B'],
                         ),
        12: QuizQuestion(
            '''If there is a superclass named A and a subclass named B, which one of the presentedinvocations should you put instead of the comment?''',
            '''
            class A:  
                def __init__(self):  
                    self.a = 1  

            class B(A):  
                def __init__(self):  
                    # put selected line here.  
                    self.b = 2''',
            None,
            None,
            {'A': 'A.__init__(self)', 'B': '__init__()', 'C': 'A.__init__()', 'D': 'A.__init__(1)'},
            ['A'],
        ),
        13: QuizQuestion('''What will be the result of executing the following code?''',
                         '''
                         class A:  
                            def__init__(self):  
                                pass  
                                
                         a = A(1)  
                         print(hasattr(a,'A'))''',
                         None,
                         None,
                         {'A': '1', 'B': 'False', 'C': 'it will raise an exception', 'D': 'True'},
                         ['C'],
                         ),
        14: QuizQuestion('''What will be the result of executing the following code?''',
                         '''
                         class A:  
                            def__init__(self):  
                                return 'a'  

                         class B(A):  
                            def__init__(self):  
                                return 'b'  

                         class c(B):  
                            pass  
                            
                         o = C()  
                         print(o)''',
                         None,
                         None,
                         {'A': 'it will print c', 'B': 'it will print b', 'C': 'it will print a',
                          'D': 'it will raise an exception'},
                         ['B'],
                         ),
        15: QuizQuestion('''What will be the output of the following code?''',
                         '''
                         class A:  
                            def__init__(self,v = 1):  
                                self.v = v  
                            def set(self,v):  
                                self.v = v  
                                return v  

                        a = A()  
                        print(a.set(a.v + 1))''',
                         None,
                         None,
                         {'A': '2', 'B': '1', 'C': '3', 'D': '0'},
                         ['A'],
                         ),
        16: QuizQuestion('''What will be the result of executing the following code?''',
                         '''
                         class A:  
                            v = 2  
                         class B(A):   
                            v = 1  
                         class C(B):  
                            pass  
                            
                         o =C()  
                         print(o.v)''',
                         None,
                         None,
                         {'A': 'it will raise an exception', 'B': 'it will print 2',
                          'C': 'it will print an empty line', 'D': 'it will print 1'},
                         ['D'],
                         )
        }
