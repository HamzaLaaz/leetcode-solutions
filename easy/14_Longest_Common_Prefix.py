def longestCommonPrefix(strs: list[str]) -> str:
    result = ""
    _str = strs[0]
    if len(strs) == 1:
        return _str
    j = 0
    for char in _str:
        chck = char
        i = 1
        while i < len(strs):
            if j >= len(strs[i]):
                return result if result else ""
            chck2 = strs[i][j]
            if chck == chck2:
                i += 1
                continue
            else:
                return result if result else ""
            i += 1
        result += chck
        j += 1
    return result
