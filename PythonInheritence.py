class Company:
    def __init__(self, name, location):
        self.name= name
        self.location= location
     
class Employee(Company):
    
    def __init__(self, name, age, salary, department, company):
        self.name= name
        self.age= age
        self.salary= salary
        self.department= department
        self.company= company
        
    def __str__(self):
        return f"Employee: {self.name}, Age: {self.age}, Salary: {self.salary}, Department: {self.department}, company_name: {self.company.name} , Company_Location: {self.company.location}"            
    
x = Employee("Samay",23,12345.00,"Mechanical Engineering",Company("Tata Motors","Delhi"))

print(x)
    