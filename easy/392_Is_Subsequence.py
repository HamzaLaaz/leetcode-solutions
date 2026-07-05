def isSubsequence(self, s: str, t: str) -> bool:
    result = ""
    i = 0
    for c in t:
        if i < len(s) and c == s[i]:
            result += c
            i += 1
    return result == s
