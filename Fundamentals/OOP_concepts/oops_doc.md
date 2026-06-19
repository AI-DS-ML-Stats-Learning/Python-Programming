Object Oriented Programming - Doc

Class -> blueprint of pieces , invent/create your own data types and objects
    methods/functions
        instance method -> 
            __init__ [initialize the contents of an object from a class] -> this is a constructor
            __str__ 
    

Objects/Instances
1. instance variables - to access these, we just need to mention the intance name - For example [
    class Employee:
        def __init__(self, m1, m2):
            self.m1 = m1
            self.m2 = m2

    employee1 = Employee(20, 40)
    print(employee1.m1)
]

2. class variables - to access these, we need to call the class name as these are accessible within the class. For example - [
    class Employee:
        school = "RNS"
        def __init__(self, m1, m2):
            self.m1 = m1
            self.m2 = m2

    employee1 = Employee(20, 40)
    print(Employee.school)
]

Properties -> feature in python that provides defense mechansim for control over attribites

decorator -> functions that modify the behaviour of other functions
    @classmethod
    getter/setter -> getters are called accessor methods as they just fetch the values; setter methods are also known as mutator methods as they change the values of the variables


function becomes method when its attached to an object


Tpes of methods in Python OOP - 
1. Instance methods - all regular methods are instance methods. Their first argument will be "self" - referring to the instance name. They will be accessed using the instance name. Like [
    class Employee:
        def __init__(self):
            pass
        
        def first_name(self):
            pass
    employee1 = Employee()
    employee1.firstname()
]
    -> as a result the dunder init method (__init__) is also an instance method
    -> inside the instance method we use 'self.name' to access variables
2. Class Methods - a method that takes reference to the class as its first argument. It is defined using decortaor @classmethod. It is used using class name. Like [
    class Employee:
    def __init__(self):
        pass
    
    def first_name(self):
        pass

    @classmethod
    def sample_method(cls, arg1):
        pass

    Employee.cample_method(arg1_value)
    employee1 = Employee()
    employee1.firstname()
] 
    -> here we took arg1 as an input variable for example.
    -> so, we see that we directly use the class name to call a class method
    -> inside the class method we use 'cls.name' to access variables
    -> 'cls' as the first argument refers to the class "Employee". Using 'cls' is standard but we can use any other name like 'classname', etc, it would still point to the class "Employee" as the method itself is changed to class method using the decorator @classmethod.
3. Static methods - 


Inner Class  - 

inheritance (Is - A) - 
    1. Single-level inheritance
    2. Multi-level inheritance
    3. Multiple-level inheritance

composition (Has - A) -

Constructor in inheritance - 
    1. A sublcass can call the constructor of the superclass - 
        a. When an __init__ (constructor) does not exist in subclass. If exists, init of subclass will be triggered
        b. When, within sublass super().__init__() is defined within the constructor of the subclass, then both super and sublcass init will be triggered.
    2. MRO - Method Resolution Order

encapsulation

abstratction
polymorphism

Overloading
    operator overloading

Overriding