def shuffle(nums: list[int], n: int) -> list[int]:
    n_nums = nums[n:]
    new = []
    for i in range(n):
        new.append(nums[i])
        new.append(n_nums[i])
    return new
