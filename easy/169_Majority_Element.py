def majorityElement(nums: list[int]) -> int:
    d = {}
    for n in nums:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
    for k, v in d.items():
        if len(nums) == 3:
            if v == 2:
                return k
        elif v > len(nums) // 2:
            return k
    return 0
