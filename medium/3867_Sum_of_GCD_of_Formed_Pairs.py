import math


def gcdSum(nums: list[int]) -> int:
    k = nums[0]
    new = []
    result = 0
    for i in range(len(nums)):
        if k < nums[i]:
            k = nums[i]
        new.append(math.gcd(k, nums[i]))
    new.sort()
    if len(new) % 2:
        new.pop((len(new) // 2))
    for i in range(len(new) // 2):
        j = (i * (-1)) - 1
        result += math.gcd(new[i], new[j])
    return result
