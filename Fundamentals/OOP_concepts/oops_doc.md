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

    Employee.sample_method(arg1_value)
    employee1 = Employee()
    employee1.firstname()
] 
    -> here we took arg1 as an input variable for example.
    -> so, we see that we directly use the class name to call a class method
    -> inside the class method we use 'cls.name' to access variables
    -> 'cls' as the first argument refers to the class "Employee". Using 'cls' is standard but we can use any other name like 'classname', etc, it would still point to the class "Employee" as the method itself is changed to class method using the decorator @classmethod.
3. Static methods - This method can print static values. It can also take parameters which can be passed at the time of object creation or when trying to access this method. It is defined using @staticmethod decorator


Inner Class - This is a class within a class. Refer to the inner class file to see how it works.

inheritance (Is - A) - 
    1. Single-level inheritance - To access the parent variables, super().__init__() is used.
    2. Multi-level inheritance - This is a hierarchy inheritance. C inherits from B, B inherits from A [A -> B -> C]
    3. Multiple-level inheritance - One subclass inherits from more than one super class at a time [A + B -> C] C inherits both from A and B in one go. This follows a MRO approach, where if we call super in the subclass, only one parent class is triggered, so we have to ensure to handle that.

Constructor in inheritance - 
    1. A sublcass can call the constructor of the superclass - 
        a. When an __init__ (constructor) does not exist in subclass. If exists, init of subclass will be triggered
        b. When, within sublass super().__init__() is defined within the constructor of the subclass, then both super and sublcass init will be triggered.
    2. MRO - Method Resolution Order

composition (Has - A) - This is one of the preferred approach to system design. The reaosn being, it does not faces the MRO priority problem, and instead of calling or referring class directly, we refer to that class's object. Also, concept of **kwargs can be avoided here.

Coupling - Coupling refers to how dependent classes are on each other. 
    1. Tightly Coupled [The Bad way] - Tightly coupled where subclasses know a lot of details about the parent class and can break anytime when parent class is changed. So basically, "Inheritance" is a tightly coupled structure.
    2. Loose Coupling [The Good way] - If classes can interact with each other without needing to know their internal structures or how they are created, they are loosely coupled. So basically, "Composition" is a loosely coupled structure.

Dependecny Injection - Dependency Injection is the action (or technique) we use to achieve loose coupling. Instead of a class creating the objects it needs to do its job (its "dependencies"), those objects are "injected" (passed) into the class from the outside. Example - [
    # 1. Create the dependencies first
        my_house = House("Burrabazar")
        my_flat = Flat("Behala")

        # 2. INJECT them into the Student
        s1 = Student("Salil", my_house, my_flat)
] -> refer to composition files.

Polymorphism - 
    1. Duck Typing - This is the most primitive form of Polymorphism. So, basically, Python supports "dynamic typing", which means, if we create any variable or pass any argument, it can be changed anytime. 
        For example - 
            x = 5 can be changed to x = "Salil", this means there is not type declared to variable 'c' like java/c
        Similarly, if we pass any argument 
            def first_func (arg1):
                pass
            and if arg1 is of list type and later we change it to dict type, it will not be a problem, hoping that inner commands of function is flexible with the type of input variable.
    2. Operator Overloading - Operator Overloading is the ability to redefine the behavior of built-in Python operators (like +, ==, or >) for custom classes. This is achieved by implementing their corresponding special "dunder" (double-underscore) methods (like __add__ or __eq__) inside the class.
    3. Method Overloading - Where we have 2 methods in a single class, with the same name but different kind of parameters. But since in Python, we can't have 2 methods with same name in same class, hence this is not applicable using the conventional way. But we can tweak and achieve this - 
        1. Within the same method, we can do typ checks and manipulate the method to perform different operations accordingly
        2. We can import singledispacthmethod from functools and use it, which helps in method overloading similar to Java/C
    4. Method Overriding - This is basically, overriding a parent class method with that of the child class method. Suppose, a method named "execute()" is defined both in parent and child class. When this is invoked in python with the child class's object, python triggers child class's "execute()" and overrides parent class's method.

encapsulation

abstratction

ABC - Abstract Base Classes



Topic 6: __slots__ (Advanced Memory Optimization)
To understand __slots__, we have to look at how Python stores variables inside objects by default.

1. The Default Way: __dict__
Normally, every object you create in Python has a hidden dictionary called __dict__. All instance variables you create (like self.name or self.age) are stored as keys and values inside this dictionary.

python


class Student:
    def __init__(self, name):
        self.name = name
s = Student("Salil")
print(s.__dict__)  # Output: {'name': 'Salil'}
Pros: Highly flexible. You can add new attributes to s at runtime (e.g., s.grade = "A" works).
Cons: Dictionaries consume a lot of memory because they use hash tables. If you create 1,000,000 students, the memory overhead of the dictionaries becomes massive.
2. The Optimized Way: __slots__
If you know your class will only ever need a fixed set of attributes, you can define __slots__ at the class level.

This tells Python: "Do not create a __dict__ dictionary for instances. Instead, allocate a fixed, tiny block of memory specifically for these attributes."

python


class OptimizedStudent:
    # Tell Python to allocate memory ONLY for these two attributes
    __slots__ = ("name", "age")
    def __init__(self, name, age):
        self.name = name
        self.age = age
Benefits of __slots__:
Massive Memory Savings: Reduces memory usage by 50% to 80%!
Faster Performance: Reading/writing attributes is slightly faster.
Typo Prevention: If you try to assign a misspelled attribute (like s.nme = "Salil"), Python will instantly raise an AttributeError instead of silently creating a new variable.