def findDisappearedNumbers(nums: list[int]) -> list[int]:
    nembers = set(nums)
    new = []
    for i in range(1, len(nums) + 1):
        if i not in nembers:
            new.append(i)
    return new
