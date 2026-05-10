def romanToInt(s: str) -> int:
    symbole = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    new = [n for n in s]
    i = 0
    result = 0
    while i + 1 < len(new):
        x = symbole[new[i]]
        if new[i] == 'C':
            if new[i + 1] == 'D':
                x = 400
            if new[i + 1] == 'M':
                x = 900
        if new[i] == 'X':
            if new[i + 1] == 'L':
                x = 40
            if new[i + 1] == 'C':
                x = 90
        if new[i] == 'I':
            if new[i + 1] == 'V':
                x = 4
            if new[i + 1] == 'X':
                x = 9
        result += x
        if x != symbole[new[i]]:
            i += 2
        else:
            i += 1
    if i < len(new):
        result += symbole[new[i]]
    return result
