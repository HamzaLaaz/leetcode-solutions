def reverseVowels(s: str) -> str:
    result = []
    check = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
    new = []
    for i in range(len(s)):
        if s[i] in check:
            new.append(s[i])
    new.reverse()
    i = 0
    for j in range(len(s)):
        if s[j] in check:
            result.append(new[i])
            i += 1
        else:
            result.append(s[j])
    return "".join(result)
