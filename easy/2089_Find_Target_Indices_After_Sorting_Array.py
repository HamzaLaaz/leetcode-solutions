def targetIndices(nums: list[int], target: int) -> list[int]:
    new = []
    nums.sort()
    for i, n in enumerate(nums):
        if n == target:
            new.append(i)
    return new
