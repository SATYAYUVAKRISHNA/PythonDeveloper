def even_or_odd(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
x = int(input("Enter a number: "))
print("The number is", even_or_odd(x))
