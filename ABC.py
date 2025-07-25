from abc import ABC, abstractmethod 
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
"""
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("Area of circle is ",3.14*self.radius**2)
    def perimeter(self):
        print("Perimeter of circle is ",3.14*self.radius*2)
"""

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
    def perimeter(self):
        return 3.14*self.radius*2


class rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    def perimeter(self):
        return self.l*2+self.b*2
    
class triangle(shape):
    def __init__(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
#TypeError: Can't instantiate abstract class triangle without an implementation for abstract methods 'area', 'perimeter' 
        
    
c1=circle(8)    
print("Area of circle is ",c1.area())
print("Perimeter of circle is ",c1.perimeter())


r1=rectangle(2,4)
print("Area of rectangle is ",r1.area())
print("Perimeter of rectangle is ",r1.perimeter())

#t1=triangle(4,2,5)
#typeError: Can't instantiate abstract class triangle without an implementation for abstract methods 'area', 'perimeter'



