#class method
#Class methods in Python are used when a method needs to operate on the class itself, rather than on a specific instance of the class. 
#They receive the class as their first argument (conventionally named cls), allowing them to access and modify class-level attributes or create new instances of the class.

#static method 
#Static methods in Python are used for functionalities that are logically related to a class but do not require access 
#to the instance or class state. They are declared using the @staticmethod decorator and do not receive an implicit first argument (like self for instance methods or cls for class methods
#Static methods are ideal for utility functions that perform operations related to the class's domain but don't depend on any specific instance data or class attributes. They help in organizing code by keeping related functionalities within the class namespace, improving code readability and maintainability.




class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Calling static methods directly on the class
result_add = MathUtils.add(5, 3)
result_multiply = MathUtils.multiply(4, 2)

print(f"Addition result: {result_add}")
print(f"Multiplication result: {result_multiply}")

class Configuration:
    MAX_RETRIES = 3

    @classmethod
    def set_max_retries(cls, value):
        cls.MAX_RETRIES = value




class student:
    course = 'DSA'
    list_of_instances = []

    def __init__(self, name):
        self.name = name
        student.list_of_instances.append(self)

    @classmethod
    def get_course(cls):
        return f"Course: {cls.course}"

    @classmethod
    def get_instance_count(cls):
        return f"Number of instances: {len(cls.list_of_instances)}"

    @staticmethod
    def welcome_message():
        return "Welcome student"

# Creating instances
g1 = student('Alice')
g2 = student('Bob')

# Calling class methods
print(student.get_course())  
print(student.get_instance_count())  

# Calling static method
print(student.welcome_message())        



#decorators
#Python decorators are a powerful and elegant feature that allow modification or enhancement of the behavior of functions
# or methods without directly altering their source code. They are essentially functions that take another function as an argument, add some functionality, and return a new function (or a callable object).
"""
The @property decorator in Python is a built-in decorator that allows methods within a class to be accessed and managed like attributes, enhancing encapsulation and providing controlled access to data. It serves as a more "Pythonic" and readable alternative to explicitly defining getter, setter, and deleter methods.
Key aspects of @property:

    Getter:
    The @property decorator is applied to a method that retrieves the value of an attribute. This method acts as the "getter" for the property, allowing you to access the attribute using direct dot notation (e.g., object.attribute) rather than calling a method (e.g., object.get_attribute()). 

Setter:
To enable modification of the attribute's value, a setter method is defined using the @<property_name>.setter decorator. This method is automatically invoked when you assign a new value to the property (e.g., object.attribute = new_value). Setters are commonly used for data validation or performing actions when an attribute is updated.
Deleter:
Similarly, a deleter method can be defined using the @<property_name>.deleter decorator. This method is called when the del statement is used on the property (e.g., del object.attribute), allowing for custom cleanup or resource management upon attribute deletion. 
"""


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """The radius property."""
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius

# Usage
my_circle = Circle(5)
print(my_circle.radius)  # Accesses the getter
my_circle.radius = 7     # Calls the setter
print(my_circle.radius)
# del my_circle.radius   # Calls the deleter