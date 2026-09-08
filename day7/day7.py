# Create and write details to a file
with open("details.txt","w") as file:
 file.write("name:praveena\n")
 file.write("age:26\n")
 file.write("coures:python\n")
 file.write("loction:tirupati\n")
 print ("details written sucussfully!")

#read and file
with open("details.txt", "r") as file:
    content = file.read()

print(content)
# List of items
items = ["Laptop", "Mobile", "Keyboard", "Mouse", "Headphones"]

# Write items line by line
with open("items.txt", "w") as file:
    for item in items:
        file.write(item + "\n")

print("Items written successfully!")
import json
student={
    "name": "Praveen Reddy",
    "age": 22,
    "course": "Python",
    "marks": 85
}

# Create JSON file
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

# Read JSON file

with open("student.json", "r") as file:
    data = json.load(file)

# Print keys and values
for key, value in data.items():
    print(key, ":", value)