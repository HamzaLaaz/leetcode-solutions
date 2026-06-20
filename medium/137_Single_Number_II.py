def singleNumber(nums: list[int]) -> int:
    for i in range(len(nums)):
        k = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                k += 1
        if k == 1:
            return nums[i]
