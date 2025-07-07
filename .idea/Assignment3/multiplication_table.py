def multiplication_table():
    n = int(input("Enter a number to print its multiplication table: "))

    print(f"\nMultiplication Table of {n}:\n")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Call the function
multiplication_table()