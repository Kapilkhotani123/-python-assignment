# In Iteractive Manner
"""def factorial(num):
    sum = 1
    for i in range(num):
        sum *= (i+1)
    return sum"""

# In Recurcive Manner
def factorial(num):
    if(num==1): return num
    else:
        return num*factorial(num-1)

number = int(input("Enter a number: "))
fact = factorial(number)
print(f"Factorial of {number} is: {fact}")  