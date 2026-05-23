def maxRotateFunction(nums: list[int]) -> int:
    x = len(nums)
    total = sum(nums)
    result = 0
    for i, num in enumerate(nums):
        result += i * num
    max_rlt = result
    for i in range(x - 1, 0, -1):
        result = result + total - x * nums[i]
        max_rlt = max(max_rlt, result)
    return max_rlt
