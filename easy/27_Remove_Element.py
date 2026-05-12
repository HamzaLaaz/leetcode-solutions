def removeElement(nums: list[int], val: int) -> int:
    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = '*'
    i = 0
    while i < len(nums):
        if nums[i] == '*':
            nums.pop(i)
            nums.append('_')
        else:
            i += 1
    return len([x for x in nums if isinstance(x, int)])
