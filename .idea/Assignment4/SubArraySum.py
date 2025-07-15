def subarray_with_sum():
    arr = list(map(int, input("Enter numbers: ").split()))
    target = int(input("Enter target sum: "))
    start, curr_sum = 0, 0

    for end in range(len(arr)):
        curr_sum += arr[end]
        while curr_sum > target and start < end:
            curr_sum -= arr[start]
            start += 1
        if curr_sum == target:
            print(f"Subarray indices: ({start}, {end})")
            return

    print("No subarray found: -1")

subarray_with_sum()