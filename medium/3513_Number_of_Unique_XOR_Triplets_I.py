def uniqueXorTriplets(nums: list[int]) -> int:
    n = len(nums)
    if n <= 2:
        return n
    result = 4
    while result <= n:
        result *= 2
    return result
