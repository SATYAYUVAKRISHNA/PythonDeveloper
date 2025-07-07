def check_substring():
    s1 = input("Enter the main string: ")
    s2 = input("Enter the substring to search: ")

    if s2 in s1:
        print(f"Yes, '{s2}' is a substring of '{s1}'.")
    else:
        print(f"No, '{s2}' is not a substring of '{s1}'.")

# Call the function
check_substring()