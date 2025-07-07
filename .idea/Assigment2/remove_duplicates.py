def remove_duplicates(lst):
    return list(set(lst))

# Example usage:
lst = [int(x) for x in input("Enter list elements separated by space: ").split()]
print("List after removing duplicates:", remove_duplicates(lst))
