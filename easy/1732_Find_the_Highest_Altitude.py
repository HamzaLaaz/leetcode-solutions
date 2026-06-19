def largestAltitude(gain: list[int]) -> int:
    new = [0]
    result = 0
    for n in gain:
        result += n
        new.append(result)
    return max(new)
