def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    numbers = list(nums)
    numbers.sort()
    d = {}
    for i, nb in enumerate(numbers):
        if nb not in d:
            d[nb] = i
    new = []
    for nb in nums:
        new.append(d[nb])
    return new
