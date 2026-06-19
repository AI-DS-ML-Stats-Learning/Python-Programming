class School:
    name = "RNS"
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        self.name = ''
        self.__class__.name = "RNSD"

school1 = School(20, 30)
print(school1.m1)
print(school1.m2)
print(school1.name)
print(School.name)

'''
## When you read school1.name:

1. Python first checks: Does school1's instance dictionary have name?
2. If Yes (e.g. because of self.name = '' in __init__), it returns that value.
3. If No, Python checks: Does the School class dictionary have name?
4. If Yes, it returns the class variable.

## When you write school1.name = "New":

1. Python always writes directly to school1's instance dictionary.
2. It never touches the class dictionary when assigning via an instance.


## The Best Practice: self.__class__ or Class Name

Because of the write trap, the rule of thumb is:
1. If you want to read a class variable: You can use self.variable_name (as long as you haven't shadowed it with self.variable_name = ... in __init__).
2. If you want to modify a class variable: You must refer to the class. You can do this in two ways:
    1. Using the class name directly: School.name = "New Name"
    2. Using self.__class__ (highly recommended for flexibility): self.__class__.name = "New Name". (This dynamically gets the class of the current instance, which is great if subclasses are involved!)

'''