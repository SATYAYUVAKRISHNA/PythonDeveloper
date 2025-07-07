def reverse_list(lst):
    start = 0
    end = len(lst) - 1
    while start < end:
        # Swap elements
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst

# Example usage:
lst = [int(x) for x in input("Enter list elements separated by space: ").split()]
print("Reversed list:", reverse_list(lst))