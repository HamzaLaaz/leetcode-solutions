def searchRange(nums: list[int], target: int) -> list[int]:
    new = []
    for i in range(len(nums)):
        if nums[i] == target:
            new.append(i)
    if new:
        return [min(new), max(new)]
    return [-1, -1]
