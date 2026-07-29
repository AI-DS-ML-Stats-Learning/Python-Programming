# class Student:
    
#     def sum_func(self, *args):
#         for i in args:
#             print(i)
        
# s1 = Student()
# s1.sum_func(20, 30, 45)

'''The typical method to overload - add conditions for typecheck within the same method'''
# class Student:
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2
    
#     def sum_func(self, a = None, b = None, c = None):
#         s = 0

#         if a!=None and b!=None and c!= None:
#             s=a+b+c
#         elif a!= None and b!=None:
#             s = a+b
#         else:
#             s = a

#         return s
            

# s1 = Student(20, 40)

# print(s1.sum_func(4, 10))

'''using singledispatchmethod'''

from functools import singledispatchmethod

class Student:
    @singledispatchmethod
    def process(self, m1):
        print(f"Fallback to default method of type {type(m1)}")
    
    '''_ in the method name does not matter here, as all the method linked to @process.register is associated to the method process'''
    @process.register
    def _(self, value:int):
        print(f"Got the type {type(value)} in the input")
    
    @process.register
    def _(self, value:list):
        print(f"Encountered the type {type(value)} variable")

s1 = Student()

# s1.process("salil")
# s1.process([3, 4,5])
s1.process(34)