def sequentialDigits(low: int, high: int) -> list[int]:
    new = []
    n = "123456789"
    for ln in range(len(str(low)), len(str(high)) + 1):
        for i in range(10 - ln):
            nums = int(n[i:i + ln])
            if low <= nums <= high:
                new.append(nums)
    return new
