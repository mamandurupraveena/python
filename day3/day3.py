#control flow
#control flow statements are used to control the execution of a program. There are three types of control flow statements in Python: selection statements, iteration statements, and jump statements.
#Selection statements are used to select a block of code to execute based on a condition. There are two types of selection statements in Python: if statements and if-else statements.
# Example:
x = 10
if x > 5:
    print("x is greater than 5")
#output:
#x is greater than 5

# Example:
y = 3
if y > 10:
    print("y is greater than 10")
else:
    print("y is not greater than 10")
#output:
#y is not greater than 10

# Example:
z = 10
if x > 5:
    print("z is greater than 5")
elif x == 5:
    print("z is equal to 5")
else:
    print("z is less than 5")
#output:
#z is greater than 5
#Nested conditions
c = 10
d = 20
if c > 5:
    if d > 15:
        print("Both conditions are true")
    else:
        print("c is greater than 5, but c is not greater than 15")
else:
    print("c is not greater than 5")
# loops
for loop in range(5):
    print("This is loop iteration:", loop)
#output:
#This is loop iteration: 0
#This is loop iteration: 1
#This is loop iteration: 2
#This is loop iteration: 3
#This is loop iteration: 4
#while loops
while_loop = 0
while while_loop < 7:
    print("This is while loop iteration:", while_loop)
    while_loop += 1
   # output:
#This is while loop iteration: 0 
# This is while loop iteration: 1
# This is while loop iteration: 2
# This is while loop iteration: 3
# This is while loop iteration: 4 
# This is while loop iteration: 5
# This is while loop iteration: 6

# Loop control statements
# Loop control statements are used to control the flow of a loop. There are three types of loop control statements in Python: break, continue, and pass.
#break statement
for loop in range(5):
    if loop == 3:
        break
    print("This is loop iteration:", loop)
#output:
#This is loop iteration: 0
#This is loop iteration: 1
#This is loop iteration: 2
#continue statement
for loop in range(5):
    if loop == 2:
        continue
    print("This is loop iteration:", loop)
    #output:
#This is loop iteration: 0
#This is loop iteration: 1
#This is loop iteration: 3
#This is loop iteration: 4
#pass statement
for loop in range(4):
    if loop == 1:
        pass
    print("This is loop iteration:", loop)
    #output:
#This is loop iteration: 0
#This is loop iteration: 1
#This is loop iteration: 2
#This is loop iteration: 3
