def is_palindrome(s):
    return s == s[::-1]

# Example usage
s = input("Enter a string: ")
print("Is palindrome?", is_palindrome(s))