def swap_numbers():
    a = int(input("Enter first number (a): "))
    b = int(input("Enter second number (b): "))

    print("Before Swapping:")
    print(f"a = {a}")
    print(f"b = {b}")

    # Swapping without using a third variable
    a = a + b
    b = a - b
    a = a - b

    print("After Swapping:")
    print(f"a = {a}")
    print(f"b = {b}")

# Call the function
swap_numbers()