import math


def findGCD(nums: list[int]) -> int:
    return math.gcd(max(nums), min(nums))
