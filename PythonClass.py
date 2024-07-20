class employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __str__(self):
     return f" {self.name}"  f" {self.age}"  f" {self.salary}"
            
x = employee("Sandeep",23,20000)

print(x)

# conclusion 
# python k andar class create karne k time pe ager value constructor me deni hai to __init__ use karna padega aur first argunment self rahega java ,me this keyword use karte the yaha par ham self keyword ka use karege
print("------------------------------------------------------------------------------------------------")

#  we are also delete the complete object 

class passport:
    pass

x = passport()
print(x)


        