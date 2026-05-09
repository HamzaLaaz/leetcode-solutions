def twoSum(nums: list[int], target: int) -> list[int]:
    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            result = nums[i] + nums[j]
            if result == target:
                return [i, j]
            j += 1
        i += 1
    return []
