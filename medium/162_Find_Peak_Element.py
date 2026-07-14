def findPeakElement(nums: list[int]) -> int:
    k = 0
    for i in range(1, len(nums)):
        if nums[k] < nums[i]:
            k = i
    return k
