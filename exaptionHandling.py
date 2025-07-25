"""    Try: This block will test the excepted error to occur
    Except:  Here you can handle the error
    Else: If there is no exception then this block will be executed
    Finally: Finally block always gets executed either exception is generated or not"""


"""
colors =['red','blue','yellow','pink','black','white']
try:
    print(colors[10])
except IndexError:
    print("Please enter a correct index")
else:
    print('')        
"""
#To raise an exception by yourself, you’ll use the raise statement, which has the following general syntax:
#raise [expression [from another_expression]]

# raise [expression [from another_expression]]

"""
for i in range(10):
    try:
        print(colors[i])
    except IndexError:
        print("Please enter a correct index") 
"""

"""

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
else:
    print(f"You entered: {num}")  """      


"""
# Python code to illustrate working of try()  
def divide(x, y): 
    try: 
        # Floor Division : Gives only Fractional
        # Part as Answer 
        result = x // y 
        print("Yeah ! Your answer is :", result) 
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ") 
  
# Look at parameters and note the working of Program 
divide(3, 2) 
divide(3, 0)    """



#catching multiple exceptions in python

"""
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {e}")"""


"""try:
    x = int(input("Enter a number: "))
    result = 10 / x
except Exception as e:
    print(f"An error occurred: {e}")
else:    
    print("result",result)
finally:
    print("This will always work, its comming from finally block")
"""

"""    
try:
    print('jkfjak',fa)
except Exception as e:
    print(e)    """



"""try:
    a=2000
    if a<4000:
        raise ValueError("Not enough money")
except Exception as e:
    print(e)
else:
    print("You have enough money") """  


"""
a=2000
if a<4000:
    raise ValueError("Not enough money")     """



from math import sqrt
def is_positive_even(number):
    if not isinstance(number, int):
        raise NotInt(f"{number} is not an integer. Please enter a valid integer number")
    if number<2:
        raise LessThenZero(f"The number is expected to be greater then 1 , got {number}")
    if number%2==0:
        print(f"{number} is a positive even number")
    else:
        print(f"{number} is a odd number")   

number=int(input("Enter a number "))    
is_positive_even(number)  