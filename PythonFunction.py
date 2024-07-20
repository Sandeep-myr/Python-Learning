#  in python we learn the function 

def greet(name,standard,age):
    print(f"Hello, {name} Your class is {standard} and your age is {age}!")

greet("sandeep",12.18,22)

print("---------------------------------------------------------------------------------------------------")

# function with default argument

def greet_default(name,standard=12.18,age=18):
    print(f"Hello, {name} Your class is {standard} and your age is {age}!")

greet_default("sandeep")

print("---------------------------------------------------------------------------------------------------")

# function with variable number of arguments

def greet_varargs(*args):
    print(f"Hello, {args[0]}! Your details are:")
    for arg in args[1:]:
     print(arg)
 
greet_varargs("sandeep",12.18,18,"M","23-02-2001")    
     
print("--------------------------------------------------------------------------------------------------------")

# keywords argunment are also possible in python
def keyword_args(subject1,subject2,subject3):
     print(f"Hello, your subjects are {subject1}, {subject2} and {subject3}!")

keyword_args(subject3="physics",subject1="Math",subject2="Hindi")     
  
print("--------------------------------------------------------------------------------------------------------")
# Arbitary keywords argunment are also possible in python

def arbitrary_keyword_args(**kwargs):
     print(f"Hello, your subjects are:")
     for key,value in kwargs.items():
      print(f"{key} : {value}")  
  
arbitrary_keyword_args(physics = "PR Tiwari", Math="Vidhata Tripathi",Hindi="BP Mishra")  
     
print("--------------------------------------------------------------------------------------------------------")
# This function is a placeholder or a stub function.
# It is used to define a function without implementing any functionality.
# The 'pass' keyword in Python is used when a statement is required syntactically but you do not want any command or code to execute.
# In this case, the 'pass_function' does nothing and returns None when called.

def pass_function():
    pass
def pass_function():
    pass     
pass_function()



        
    
    