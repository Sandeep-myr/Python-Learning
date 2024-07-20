#  Just Like a java it is difficult to remember all the name of the method so from parent class we are using same method name 

class String :
    def __init__(self, data):
        self.data = data
    
    def  className(self):
        print(f"This is a String Class {self.data}")
            
            
class Integer :
    def __init__(self, data):
        self.data = data
    
    def className(self):
        print(f"This is a Integer Class {self.data} ")

class Boolean :
    def __init__(self, data):
        self.data = data
    
    def className(self):
        print(f"This is a Boolean Class {self.data}")


str1 = String("Ramesh")
int1 = Integer(123)
bool1 = Boolean(True)

for i in (str1,bool1,int1):
    i.className()         