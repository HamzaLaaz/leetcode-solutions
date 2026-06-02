def strStr(haystack: str, needle: str) -> int:
    j = 0
    lh = len(haystack)
    ln = len(needle)
    if ln <= lh:
        while j < lh:
            i = 0
            if haystack[j] == needle[i]:
                k = j
                while i < ln:
                    if haystack[k] == needle[i]:
                        i += 1
                        if k < lh - 1:
                            k += 1
                    else:
                        break
                if i == ln:
                    return j
            j += 1
    return -1
