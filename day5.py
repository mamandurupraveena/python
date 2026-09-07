#functions in python:
#A function is a block of code that performs a specific task. It can take inputs, perform operations, and return outputs. Functions help in organizing code, making it reusable, and improving readability.
#def print_message():
 #   print("Hello, World!")
#print_message() #This calls the function and prints the message to the console.
#output: Hello, World!
#basic function:
from ast import keyword


def greet():
    print("Hello, there!")
greet() #This calls the function and prints the greeting message to the console.
#output: Hello, there!
#function with parameters:
def greet_person(name):
    print(f"Hello, {name}!")
greet_person("Alice") #This calls the function with the argument "Alice" and prints the personalized greeting message to the console.
#output: Hello, Alice!
#function with multiple parameters:
def greet_person_age(name, age):
    print(f"Hello, {name}! You are {age} years old.")
greet_person_age("Bob", 25) #This calls the function with the arguments "Bob" and 25 and prints the personalized greeting message with the person's age to the console.
#output: Hello, Bob! You are 25 years old.
#function with return :
def add(a, b):
    return a + b
result = add(5, 3)
print(result) #output: 8

#different types of functions:
#1. Built-in functions: These are functions that are already defined in Python and can be used without any additional code. Examples include print(), len(), type(), etc.
#2. User-defined functions: These are functions that are defined by the user to perform specific tasks. They are created using the def keyword and can take parameters and return values.        
def multiply(x, y):
    return x * y
result = multiply(4, 6)
print(result) #output: 24   
#no parameter no return:
def print_greeting():
    print("Hello, World!")
print_greeting() #output: Hello, World!
#parameter no return:
def greet(name):
    print(f"Hello, {name}!")
greet("Alice") #output: Hello, Alice!   
#parameter with return:
def add_numbers(a, b):
    return a * b
result = add_numbers(5, 3)
print(result) #output: 15
    #example programs:
def calculate_area(length, width):
    area = length * width
    return area
result = calculate_area(10, 5)
print(result) #output: 50
#arguments and parameters:
#In Python, arguments are the values that are passed to a function when it is called, while parameters are the variables that are defined in the function's definition to receive those values. Parameters act as placeholders for the arguments that will be provided when the function is invoked.
def student_info(name, age, grade):
    print(f"Name: {name}, Age: {age}, Grade: {grade}")

student_info("Naveena", 20, "A")
#keyword arguments:
#In Python, keyword arguments are a way to pass arguments to a function by explicitly specifying the parameter names along with their corresponding values. This allows you to provide arguments in any order, making the code more readable and flexible.
def student_info(name, age, grade):
    print(f"Name: {name}, Age: {age}, Grade: {grade}")

student_info(name="ramu", age=40, grade="b")
#Default Arguments:
def greet_person(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
greet_person("Alice") #output: Hello, Alice!
greet_person("Bob", "Hi") #output: Hi, Bob!
#*args:*args allows a function to accept multiple positional arguments.
def print_values(*args):
    for value in args:
        print(value)
print_values(1, 2, 3, 4, 5) #output: 1 2 3 4 5
#**kwargs: **kwargs allows a function to accept multiple keyword arguments. 
def print_key_values(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_key_values(name="Alice", age=30, city="New York") #output: name: Alice age: 30 city: New York