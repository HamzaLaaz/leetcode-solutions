def maxProduct(n: int) -> int:
    s = str(n)
    new = []
    for c in s:
        new.append(int(c))
    result = []
    for i in range(len(new) - 1):
        for j in range(i + 1, len(new)):
            result.append(new[i] * new[j])
    return max(result)
