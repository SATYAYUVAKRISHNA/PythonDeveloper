from collections import Counter

def find_duplicates():
    nums = list(map(int, input("Enter list of numbers separated by space: ").split()))
    counts = Counter(nums)
    duplicates = [num for num, count in counts.items() if count > 1]
    print("Duplicate elements:", duplicates if duplicates else "None")

find_duplicates()