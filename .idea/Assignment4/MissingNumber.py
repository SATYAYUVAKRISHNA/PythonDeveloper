def find_missing_number():
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    print("Missing Number:", expected_sum - actual_sum)

find_missing_number()