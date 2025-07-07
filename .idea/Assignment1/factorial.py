#(a).using loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
n = int(input("Enter a number: "))
print("Factorial:", factorial(n))

#(b).using the built-in math.factorial
import math

n = int(input("Enter a number: "))
print("Factorial:", math.factorial(n))
