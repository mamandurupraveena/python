#1.What is Python?

#Python is a high-level, interpreted, general-purpose programming language. It is known for its simple and readable syntax, which makes it easy for beginners to learn and use.

#2.Why use Python?
# *Easy to learn – Python syntax is simple and similar to everyday English.
# *Beginner-friendly – Good for people starting programming.
# *Versatile – Used for web development, automation, data analysis, AI, machine learning, and more.
# *Large libraries – Thousands of libraries are available for different tasks.
# *Cross-platform – Works on Windows, macOS, and Linux.
# *Strong community – Many tutorials, documentation, and developer communities are available.
# *Used in AI & Data Science – Popular libraries include NumPy, Pandas, TensorFlow, and PyTorch.
# *Automation – Python can automate repetitive tasks such as file handling, data processing, and report generation.


# simple example
#input 
name = "Praveena"
print("Hello", name)

# output : Hello Praveena

# 3. variables
# variables are used to store data values

### example:

name = "Praveena"  # string variable
age = 20  # integer variable
height = 5.6  # float variable
is_student = True  # boolean variable

print("name:", name)
print("age:", age)
print("height:", height)
print("is_student:", is_student)

##output:
#name: Praveena
#age: 20
#height: 5.6
#is_student: True

#### data types ####
# * int – for integers 
# * float – for decimal numbers
# * str – for strings
# * bool – for boolean values
# * list – for ordered collections
# * tuple – for ordered, immutable collections
# * dict – for key-value pairs
# * set – for unordered collections of unique elements

#example:
name = "Praveena"  # str
age = 20  # int
height = 5.6  # float
is_student = True  # boolean
subjects = ["Python", "Git", "SQL"]  # list
student_location = ("India", "AP")  # tuple 
skills = {"Python", "Git", "SQL"}  # set
student_details = {     
    "name": "Praveena",
    "age": 20,
    "height": 5.6,
   "is_student": True
}  # dict



print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(subjects))
print(type(student_location))
print(type(skills))
print(type(student_details))

# output: 
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'list'>
# <class 'tuple'>
# <class 'set'>
# <class 'dict'>

 # type conversion ###
# Type conversion means changing a value from one data type to another.
# string-integer conversion

name = "Praveena"
age = int("20")
print(age)  # 20
print(type(age))  # <class 'int'>

# integer-string conversion
int_value = 20
str_value = str(int_value)
print(str_value)  # "20"
print(type(str_value))  # <class 'str'>
# integer-float conversion

int_value = 20
float_value = float(int_value)
print(float_value)  # 20.0
print(type(float_value))  # <class 'float'>

# float-integer conversion

float_value = 20.5
int_value = int(float_value)
print(int_value)  # 20
print(type(int_value))  # <class 'int'>

# integer-boolean conversion

int_value = 1
bool_value = bool(int_value)
print(bool_value)  # True
print(type(bool_value))  # <class 'bool'>

#input with type conversion
# input() function is used to take input from the user. By default, it takes input as a string. We can convert it to other data types using type conversion functions like int(), float(), etc.
age = int(input("Enter your age: "))
print("Your age is:", age)

# output: 
# Enter your age: 20
# Your age is: 20

height = float(input("Enter your height: "))
print("Your height is:", height)

# output:
# Enter your height: 5.6
# Your height is: 5.6
#string input 

string_input = input("Enter a string: ")
print("You entered:", string_input)

# output:
# Enter a string: Hello
# You entered: Hello
