def animalFunction():
    x = "Animal Function"
    print(x)
    
    def horseFunction():
        y = "horse Function"
        print(y)  
        horseFunction()    
animalFunction()

        
        
x = 200

def outerFunction():
    x = 100
    print("Inside outerFunction:", x)
outerFunction()
print("Global Variable:", x)   


def innerFunction():
    global x
    x = 150
    print("Inside innerFunction:", x)

innerFunction()
print("Global Variable:", x)    


#  example of The non local keyword inside the inner function

def outerFunction():
    x = 100
    def innerFunction():
        nonlocal x
        x = 200
        print("Inside innerFunction:", x)
    
    innerFunction()
    print("After innerFunction:", x)

outerFunction()
      