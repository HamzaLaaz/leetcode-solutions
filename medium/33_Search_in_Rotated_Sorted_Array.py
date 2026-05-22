def search(nums: list[int], target: int) -> int:
    for i, nb in enumerate(nums):
        if nb == target:
            return i
    return -1
