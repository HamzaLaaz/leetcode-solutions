def findDuplicates(nums: list[int]) -> list[int]:
    nums.sort()
    new = []
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            new.append(nums[i])
    result = set(new)
    return list(result)
