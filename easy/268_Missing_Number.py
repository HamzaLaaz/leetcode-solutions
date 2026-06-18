def missingNumber(nums: list[int]) -> int:
    nums.sort()
    for i in range(len(nums)):
        if i not in nums:
            return i
    return i + 1
