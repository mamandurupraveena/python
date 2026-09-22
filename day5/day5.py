# 1. Reverse a string
text = "Python"
print("Reverse:", text[::-2])
#output:
#Reverse: nhy
# 2. Count a character
text = "banana"
character = "a"
print("Character count:", text.count(character))
#output:
#Character count: 3
# 3. Check palindrome
text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
#output:
#Palindrome
# 4. Title case
full_name = "praveen reddy"
print(full_name.title())
#output:
#Praveen Reddy