def runningSum(nums: list[int]) -> list[int]:
    new = []
    result = 0
    for n in nums:
        result += n
        new.append(result)
    return new
