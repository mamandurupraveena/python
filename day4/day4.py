#Data Structures in python:Data structures are used to store and organize multiple pieces of data in Python.
#These are very important.
#1 Lists
#2 Tuples
#4 Sets
#5 Dictionaries
#6 String methods
#7 List & dictionary comprehensions

#list[]:
#sum of 5 numbers
numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total = total + num

print("Numbers:", numbers)
print("Sum:", total)
#output:
#Numbers: [10, 20, 30, 40, 50]
#Sum: 150

#add and remove
numbers.append(60)
numbers.remove(20)
print(numbers)
#output:
#[10,30,40,50,60]
# 3. Sort without sort()
for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)
#tuple():
movies =('RRR','bahubali','pushpa','KGF','KGF2')
print(movies[2])
#sets:
set1={1,2,3,4,5,6}
set2={8,7,8,9,5,4}
# Union
print( set1.union(set2))

# Intersection
print( set1.intersection(set2))

# Difference
print( set1.difference(set2))
#output:
#{1, 2, 3, 4, 5, 6, 7, 8, 9}
#{4, 5}
#{1, 2, 3, 6}
#Dictionaries
student={
    "name":"praveena",
            "age": 25 ,
            "marks" : 89 
            }
print(student)
#output:{'name': 'praveena', 'age': 25, 'makes': 89}
#marks update
student["marks"] = 90
#add new key
student["branch"] = "cse"
print(student)
#output:
#{'name': 'praveena', 'age': 25, 'marks': 90, 'branch': 'cse'}
for key in student.keys():

    print(key)
    #output:
#name
#age
#marks
#branch
for value in student.values():
    
    print(value)
    #output:
#name
#age
#marks
#branch
#praveena
#25
#90
#cse

