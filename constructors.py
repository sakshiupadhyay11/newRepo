#types
#Default constructors
#Parameterized constructors

#Default constructor 
#it does not take any parameters other then self
class student:
    def __init__(self):
        self.name="jiya"
        self.age=20
        self.id=42
s1=student()
print('name',s1.name)  
print('age',s1.age)  
print('id',s1.id)   

class employee:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id

e1=employee('Nick',26,446)
print('name is ',e1.name) 
print('age is ',e1.age) 
print('id is ',e1.id)        
class employee:
    def __init__(self):
        print("obj is created ,constructor is working  ")
        
    def __del__(self):
        print("destructor is working")
def create_obj():   
    print("creating object")
    obj=employee()
    print("create_obj fucntion end")
    return obj
print("calling create_obj fucntion")
obj=create_obj()
print('program end')



        