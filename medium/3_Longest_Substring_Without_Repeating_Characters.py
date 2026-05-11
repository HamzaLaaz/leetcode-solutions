def lengthOfLongestSubstring(s: str) -> int:
    check = ""
    result = []
    for c in s:
        if c not in check:
            check += c
        else:
            result.append(len(check))
            i = check.index(c) + 1
            check = check[i:] + c
    result.append(len(check))
    return max(result)
