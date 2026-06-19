class School:
    name = "RNS Memorial High School"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    @classmethod
    def class_method(cls):
        cls.name = "RNSMH"
    
    def call_class_method(self):
        self.class_method()


# Pass the method reference WITHOUT parenthesis, so it doesn't run immediately.
# Instead, the button will run it later when clicked.
    # A function that takes another function/method as a callback
def click_button(action):
    print("Button clicked!")
    action()  # Now we add parenthesis to execute it!
s1 = School(20,30,10)

print(f"m1 marks for student is {s1.m1}")
print(f"m2 marks for student is {s1.m2}")
print(f"m3 marks for student is {s1.m3}")
# School.class_method() #call the setter/method to apply
# s1.call_class_method() 
click_button(s1.call_class_method)
print(School.name)