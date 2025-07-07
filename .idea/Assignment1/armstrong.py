def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    return total == n

# Example usage
n = int(input("Enter a number: "))
print("Is Armstrong number?", is_armstrong(n))