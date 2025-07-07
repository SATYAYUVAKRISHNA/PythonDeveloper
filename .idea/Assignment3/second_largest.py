def find_second_largest():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    unique_numbers = list(set(numbers))  # Remove duplicates
    unique_numbers.sort()

    if len(unique_numbers) < 2:
        print("There is no second largest number.")
    else:
        print("Second largest number is:", unique_numbers[-2])

# Call the function
find_second_largest()