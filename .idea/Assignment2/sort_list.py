def sort_list(lst):
    return sorted(lst)

# Example usage:
lst = [int(x) for x in input("Enter list elements separated by space: ").split()]
print("Sorted list:", sort_list(lst))
