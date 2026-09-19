#operators #operators are symbols that perform operations on variables and values. In Python, there are several types of operators, including arithmetic, comparison, logical, assignment, and bitwise operators.
#Arithmetic Operators 
a=10
b=5
c=a+b  # Addition
d=a-b  # Subtraction
e=a*b  # Multiplication
f=a/b  # Division
g=a%b  # Modulus
h=a**b # Exponentiation
print("Addition:", c)
print("Subtraction:", d)
print("Multiplication:", e)
print("Division:", f)
print("Modulus:", g)
print("Exponentiation:", h)
#output:
#Addition: 15
#Subtraction: 5
#Multiplication: 50
#Division: 2.0
#Modulus: 0
#Exponentiation: 100000

#Comparison operators
a1=20
b1=6
print("a1 > b1:", a1 > b1)
print("a1 < b1:", a1 < b1)
print("a1 == b1:", a1 == b1)
print("a1 != b1:", a1 != b1)
print("a1 >= b1:", a1 >= b1)
print("a1 <= b1:", a1 <= b1)
#output:
#a1 > b1: True
#a1 < b1: False
#a1 == b1: False
#a1 != b1: True
#a1 >= b1: True
#a1 <= b1: False
#Assignment operators
x=10
print("x:", x)
x+=5  # Equivalent to x = x + 5
print("x after +=:", x)
x-=3  # Equivalent to x = x - 3
print("x after -=:", x)
x*=2  # Equivalent to x = x * 2
print("x after *=:", x)
x/=4  # Equivalent to x = x / 4
print("x after /=:", x)
#output:
#x: 10 
#x after +=: 15
#x after -=: 12
#x after *=: 24
#x after /=: 6.0
#logical operators
a2 = True
b2 = False
print("a2 and b2:", a2 and b2)
print("a2 or b2:", a2 or b2)
print("not a2:", not a2)
#output:
#a2 and b2: False
#a2 or b2: True
#not a2: False

#membership operators(in,not in)

# Membership operators are used to test whether a value is present in a sequence (like a list, tuple, or string) or not. There are two membership operators in Python: `in` and `not in`.
# Example:
my_list = [1, 2, 3, 4, 5]
print("3 in my_list:", 3 in my_list)
print("6 in my_list:", 6 in my_list)
print("3 not in my_list:", 3 not in my_list)
#output:
#3 in my_list: True
#6 in my_list: False
#3 not in my_list: False

#identity operators
# Identity operators are used to compare the memory locations of two objects. There are two identity operators in Python: `is` and `is not`.
# Example:
x1 = [1, 2, 3]
y1 = [1, 2, 3]
z1 = x1
print("x1 is y1:", x1 is y1)
print("x1 is z1:", x1 is z1)
print("x1 is not y1:", x1 is not y1)
#output:
#x1 is y1: False
#x1 is z1: True
#x1 is not y1: True