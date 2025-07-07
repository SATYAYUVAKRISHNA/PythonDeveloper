def decimal_to_binary():
    n = int(input("Enter a decimal number: "))
    binary = bin(n)[2:]  # Remove the '0b' prefix
    print(f"Binary of {n} is: {binary}")

# Call the function
decimal_to_binary()