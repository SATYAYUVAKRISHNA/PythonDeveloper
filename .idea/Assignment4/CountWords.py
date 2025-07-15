def count_words():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    print("Word Count:", len(words))

count_words()