#what is  an iterator
#An iterator is an object that allows us to go through a collection one item at a time.
#Python uses two important functions:

#iter() → creates an iterator
#next() → gets the next value
numbers = [10, 20, 30]

my_iterator = iter(numbers)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
#output :
#10
#20
#30
#2. What is a Generator?

#A generator is a simple way to create an iterator.

#Generators use the yield keyword instead of return.


def numbers():
    yield 40
    yield 50
    yield 60

for number in numbers():
    print(number)
    #output :
    #40
    #50
    #60

def count_numbers():
    for i in range(1, 7):
        yield i

for num in count_numbers():
    print(num)
#output:
# 1
# 2
# 3
# 4
# 5
# 6    
#what is decorator
#A decorator is a function that adds extra functionality to another function without changing the original function's code.
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    
    return wrapper


@my_decorator
def hello():
    print("Hello Python")


hello()
#output:
#Before function
#Hello Python
#After function
#error handling
try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)

except ValueError:
    print("Please enter a number")
#output:
# Enter your age: 25
#Your age is: 25    
#or
#Enter your age: abc
#please enter a number

 #libraries
import math

number = 25

print(math.sqrt(number))
#output: 5.0

import random

number = random.randint(1, 10)

print(number)
#output:9
import requests

response = requests.get("https://example.com")

print(response.status_code)
#output:
#2000