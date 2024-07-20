
try:
 a = 10
 b =0 
 result = a/b
 print(result)
except ArithmeticError:
    print("Exception Is Coming" ,ArithmeticError )
except:
    print("Exception Is Coming In Else Condition")   
       
       
 # use of the finally block 
try:
    a = 10
    b =0
    result = a/b
    print(result)
except ArithmeticError:
    print("Exception Is Coming" ,ArithmeticError )
finally:
    print("This is the finally block")
    
    
print("------------------------------------------------------------------------------------------------")    
# file handling exceptions
try:
    file = open("C:\\Users\\sandeepsahu\\Downloads\\abc.txt","w")
    try:
         file.write("Somethin i am write")
    except:
          print("Exception Is Coming In Write Operation")
except:
     print("Exception Is Coming In File Opening") 
finally:
    print("write operation done")     
    
# raising the exception according to scenario
    try:
        if(a>b):
            raise ValueError("a is greater than b")
        else:
            raise Exception("a is not greater than b")
    except ValueError as ve: 
                  print("Exception Is Coming",ve)
           
    