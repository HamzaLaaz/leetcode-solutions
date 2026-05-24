def isPalindrome(s: str) -> bool:
    text = ""
    for char in s:
        if char.isalpha() or char.isdigit():
            text += char
    rev = text[::-1]
    return rev.lower() == text.lower()
