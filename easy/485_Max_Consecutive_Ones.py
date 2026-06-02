def findMaxConsecutiveOnes(nums: list[int]) -> int:
    consecutive = []
    count = 0
    for n in nums:
        if n:
            count += 1
        else:
            consecutive.append(count)
            count = 0
    consecutive.append(count)
    return max(consecutive)
