"""class animal:
    def __init__(self,name):
        self.name=name
    def display_name(self):
        pass
class dog(animal):
    def display_name(self):
        return f"name is {self.name}  "
a=animal('tom')
d=dog('jerry')
print(d.display_name())"""    
                


#types of Python Inheritance
"""
    Single Inheritance: A child class inherits from one parent class.
    Multiple Inheritance: A child class inherits from more than one parent class.
    Multilevel Inheritance: A class is derived from a class which is also derived from another class.
    Hierarchical Inheritance: Multiple classes inherit from a single parent class.
    Hybrid Inheritance: A combination of more than one type of inheritance.  
    """     

"""
class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)  # Using super() to call Person's __init__()
        self.salary = salary
        self.post = post

emp = Employee('neha',448, 200000,"intern")  
print(emp.name,emp.idnumber, emp.salary ,emp.post) 
"""
   




class Person:
    def __init__(self, name):
        self.name = name
        
class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)  # Using super() to call Person's __init__()
        self.salary = salary


class job:
    def __init__(self,salary):
        self.salary=salary 

class EmployeePersonJob(Employee, job):
    def __init__(self,name,salary):
        Employee.__init__(self,name,salary)
        job.__init__(self,salary)

class Manager(EmployeePersonJob):
    def __init__(self,name,salary,department):
        EmployeePersonJob.__init__(self,name,salary)
        self.department=department
class AssistantManager(EmployeePersonJob):
    def __init__ (self,name,salary,team_size):
        EmployeePersonJob.__init__(self,name,salary)
        self.team_size = team_size

class SeniorManager(Manager,AssistantManager):
    def __init__(self,name,salary,department,team_size):
        Manager.__init__(self,name,salary,department)
        AssistantManager.__init__(self,name,salary,team_size)
        
emp = Employee('neha', 200000)  
print(emp.name,emp.salary )  

emp2=EmployeePersonJob('neha',200000)
 
print(emp2.name,emp2.salary ) 

mng = Manager('neha',200000,'it')

print(mng.name,mng.salary,mng.department)

ast_mng= AssistantManager('neha',200000,20)
print(ast_mng.name,ast_mng.salary,ast_mng.team_size)

sen_mng=SeniorManager('neha',200000,'it',20)
print(sen_mng.name,sen_mng.salary,sen_mng.department,sen_mng.team_size)




