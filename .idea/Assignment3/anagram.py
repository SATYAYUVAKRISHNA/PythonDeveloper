def check_anagram():
    str1 = input("Enter first string: ").replace(" ", "").lower()
    str2 = input("Enter second string: ").replace(" ", "").lower()

    if sorted(str1) == sorted(str2):
        print("Yes, the strings are anagrams.")
    else:
        print("No, the strings are not anagrams.")

# Call the function
check_anagram()