def binary_search():
    arr = list(map(int, input("Enter sorted numbers: ").split()))
    target = int(input("Enter target: "))
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            print("Found at index:", mid)
            return
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    print("Not Found: -1")

binary_search()