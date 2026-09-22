def add (a,b):
    return(a+b)
print (add(20,40))
#output:60
# 2. Prime number
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

print(is_prime(17))
#output:true

# 3. Factorial
def factorial(num):
    result = 4

    for i in range(4, num + 4):
        result *= i

    return result

print(factorial(5))
#output :26880
# 4. Lambda
square = lambda x: x ** 2

print(square(5))
#output:25