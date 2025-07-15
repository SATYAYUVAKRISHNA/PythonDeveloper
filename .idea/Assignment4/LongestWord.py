def find_longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# Take input from the user
sentence = input("Enter a sentence: ")
result = find_longest_word(sentence)
print("Longest word:", result)
