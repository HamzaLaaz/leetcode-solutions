def balancedStringSplit(s: str) -> int:
    count, a, b = 0, 0, 0
    for char in s:
        if char == "R":
            a += 1
        if char == "L":
            b += 1
        if a == b:
            count += 1
            a, b = 0, 0
    return count
