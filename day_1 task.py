
print("===== Student Information =====")

name = input("Enter your name: ")

age = int(input("Enter your age: "))

course = input("Enter your course: ")

marks = float(input("Enter your marks: "))


# Different Python Data Types

is_student = True                         # bool

subjects = ["Python", "Git", "SQL"]       # list

student_location = ("India", "AP")       # tuple

skills = {"Python", "Git", "SQL"}        # set

student_details = {                       # dict
    "name": name,
    "age": age,
    "course": course,
    "marks": marks
}


print("\n===== Student Details =====")

print("Name:", name)

print("Age:", age)

print("Course:", course)

print("Marks:", marks)

print("Is Student:", is_student)

print("Subjects:", subjects)

print("Location:", student_location)

print("Skills:", skills)

print("Student Details:", student_details)


print("\n===== Data Types =====")

print("Name type:", type(name))

print("Age type:", type(age))

print("Course type:", type(course))

print("Marks type:", type(marks))

print("Is Student type:", type(is_student))

print("Subjects type:", type(subjects))

print("Location type:", type(student_location))

print("Skills type:", type(skills))

print("Student Details type:", type(student_details))

