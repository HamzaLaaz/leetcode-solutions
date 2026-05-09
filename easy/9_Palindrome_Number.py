def isPalindrome(self, x: int) -> bool:
    text = str(x)
    rev_text = ""
    l_t = len(text)
    l_m = l_t - 1
    while l_m >= 0:
        rev_text += text[l_m]
        l_m -= 1
    new_text = ""
    l_m = 0
    while l_m < l_t:
        new_text += text[l_m]
        l_m += 1
    return rev_text.lower() == new_text.lower()
