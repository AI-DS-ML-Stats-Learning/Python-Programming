class PyCharm:
    def execute(self):
        print("Compiling")
        print("Executing")
    
class PyCharm1:
    def execute(self):
        print("Code Checks")
        print("Debugger")
        print("Interpretor")
        print("Compiling")
        print("Executing") 

class Laptop:
    # def __init__(self, ide):
    #     ide.execute()
    def code(self, ide):
        ide.execute()
    
# ide = PyCharm()
'''The above ide can now be changed to a different class. 
Why? Because, the inner method of Laptop has execute funciton in ide. 
Till the time, our new class also has execute as its method, we are good to change. This is duck typing'''
ide = PyCharm1()
# lap1 = Laptop(ide)  -- when __init__ was defined
lap1 = Laptop()  #'''When init is not defined'''
lap1.code(ide)

