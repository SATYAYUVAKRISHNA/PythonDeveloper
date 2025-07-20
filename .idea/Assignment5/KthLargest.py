import heapq

def find_k_largest():
    nums = list(map(int, input("Enter list of numbers: ").split()))
    k = int(input("Enter value of k: "))
    if k > len(nums):
        print("k cannot be greater than the number of elements.")
        return
    result = heapq.nlargest(k, nums)
    print(f"{k} largest elements are:", result)

find_k_largest()