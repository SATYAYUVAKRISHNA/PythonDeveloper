def longest_increasing_subsequence():
    nums = list(map(int, input("Enter list of numbers: ").split()))
    if not nums:
        print("Empty list!")
        return
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print("Length of LIS:", max(dp))

longest_increasing_subsequence()