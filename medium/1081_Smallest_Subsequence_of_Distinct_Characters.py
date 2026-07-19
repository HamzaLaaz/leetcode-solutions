def smallestSubsequence(s: str) -> str:
    d = {}
    for i in range(len(s)):
        d[s[i]] = i
    new = []
    for j, c in enumerate(s):
        if j == 0:
            new.append(c)
        if c not in new:
            for _ in range(len(new)):
                if c < new[-1]:
                    if j < d[new[-1]]:
                        new.pop()
                    else:
                        break
            new.append(c)
    return "".join(c for c in new)
