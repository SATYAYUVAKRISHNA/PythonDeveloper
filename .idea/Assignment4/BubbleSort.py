def bubble_sort():
    arr = list(map(int, input("Enter numbers: ").split()))
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("Sorted List:", arr)

bubble_sort()