def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    new = set()
    for i, num in enumerate(nums):
        if num in new:
            return True
        new.add(num)
        if len(new) > k:
            new.remove(nums[i - k])
    return False
