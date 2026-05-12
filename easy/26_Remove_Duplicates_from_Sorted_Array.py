def removeDuplicates(nums: list[int]) -> int:
    for i in range(len(nums) - 1):
        if isinstance(nums[i], int):
            for j in range(i + 1, len(nums)):
                if isinstance(nums[j], int) and nums[i] == nums[j]:
                    nums[j] = '*'
    i = 0
    while i < len(nums):
        if nums[i] == '*':
            nums.pop(i)
            nums.append('_')
        else:
            i += 1
    return len([x for x in nums if isinstance(x, int)])
