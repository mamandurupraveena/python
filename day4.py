    #data structures in Python:
    #1. Lists
    #2. Tuples
    #3. Sets
    #4. Dictionaries
#lists:Used to store multiple values. You can change the values.
number = [10,20,30,40,50] #list
print (number)
print(number[0])
number.append(60)
print(number)   
#output:
#[10, 20, 30, 40, 50]
#10
#[10, 20, 30, 40, 50, 60]
#tuples:Similar to a list, but cannot be changed after creation.
names = ("John", "Alice", "Bob") #tuple
print(names)
print(names[1])
#output:
#Alice
#set:Stores unique values. Duplicate values are automatically removed.
locals = {"New York", "Los Angeles", "Chicago", "New York"} #set
print(locals)
#output:
#{'Los Angeles', 'New York', 'Chicago'}
#dictionaries:Used to store key-value pairs. Each key must be unique.
person = {"name": "John", "age": 30, "city": "tirupati"} #dictionary
print(person)
print(person["city"])
#output:
#{'name': 'John', 'age': 30, 'city': 'tirupati'}
#tirupati
#strings:A string is an immutable sequence of characters.
course = "python programming" #string
print(course)
print(course[0])
print(course[0:6])
print(course[7:18])
#output:
#python programming
#p
#python
#programming