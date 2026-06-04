def findErrorNums(nums: list[int]) -> list[int]:
    nums.sort()
    duplicate = -1
    missing = 1
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            duplicate = nums[i]
        elif nums[i] + 1 != nums[i + 1]:
            missing = nums[i] + 1
    if nums[0] != 1:
        missing = 1
    elif nums[-1] != len(nums):
        missing = len(nums)
    return [duplicate, missing]
