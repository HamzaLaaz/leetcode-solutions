def shiftingLetters(s: str, shifts: list[int]) -> str:
    result = 0
    new = list(s)
    for i in range(len(shifts) - 1, -1, -1):
        result = (result + shifts[i]) % 26
        new[i] = chr((ord(new[i]) - 97 + result) % 26 + 97)
    return "".join(new)
