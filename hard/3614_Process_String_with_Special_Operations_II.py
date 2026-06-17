def processStr(s: str, k: int) -> str:
    lent = 0
    for c in s:
        if c == "*":
            if lent:
                lent -= 1
        elif c == "#":
            lent *= 2
        elif c == "%":
            continue
        else:
            lent += 1
    if k >= lent:
        return "."
    for c in s[::-1]:
        if c == '*':
            lent += 1
        elif c == '%':
            k = lent - k - 1
        elif c == '#':
            lent //= 2
            if k >= lent:
                k -= lent
        else:
            if k == lent - 1:
                return c
            lent -= 1
