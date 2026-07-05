def arraySign(nums: list[int]) -> int:
    if 0 in nums:
        return 0
    k = 0
    for n in nums:
        if n < 0:
            k += 1
    return -1 if k % 2 else 1
