def longestPalindrome(s: str) -> str:
    result = ""
    if len(s) < 2:
        return s
    for i in range(len(s)):
        check = ""
        for j in range(i, len(s)):
            check += s[j]
            if check == check[::-1]:
                if len(check) > len(result):
                    result = check
    return result
