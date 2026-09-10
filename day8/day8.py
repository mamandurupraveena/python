#create a student class .
class student:
 def __init__(self,name,age,branch):
    print("object created")
    self.name = name
    self.age = age
    self.branch = branch
#2.Add a method to print all details.

 def display_details(self):
  print ("Name:",self.name)
  print ("Age:",self.age)
  print("Branch:",self.branch)
  #3.Create a constructor that prints "Object Created".
 
student1=student("praveena","26","cse")
student1.display_details()
print()
#4.Create two classes with inheritance (e.g., Animal → Dog).
class animal:
   def sound(self):
    print("animals make a sound")

class dog(animal):
   def sound(self):
     print("dog sound")   

dog1 = dog()
dog1.sound

class cat:
    def sound(self):
        print("cat meows")

class cow:
    def sound(self):
        print("cow moos")
   
animals = [dog(), cat(), cow()]
for animal in animals:
    animal.sound()