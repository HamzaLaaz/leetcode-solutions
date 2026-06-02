def singleNumber(nums: list[int]) -> int:
    i = 0
    while i < len(nums):
        a = nums[i]
        nums[i] = "*"
        if a not in nums:
            return a
        else:
            nums[i] = a
        i += 1
    return 0
