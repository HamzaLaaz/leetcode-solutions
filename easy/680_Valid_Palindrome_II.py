def is_pal(lf, r, s):
    while lf < r:
        if s[lf] != s[r]:
            return False
        lf += 1
        r -= 1
    return True


def validPalindrome(s: str) -> bool:
    lf, r = 0, len(s) - 1
    while lf < r:
        if s[lf] != s[r]:
            return is_pal(lf + 1, r, s) or is_pal(lf, r - 1, s)
        lf += 1
        r -= 1
    return True
