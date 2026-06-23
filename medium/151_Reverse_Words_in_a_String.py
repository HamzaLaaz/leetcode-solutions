def reverseWords(s: str) -> str:
    s.strip()
    new = s.split()
    rev = ""
    for n in new[:0:-1]:
        rev += n
        rev += " "
    rev += new[0]
    return rev
