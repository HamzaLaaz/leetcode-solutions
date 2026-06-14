def findWords(words: list[str]) -> list[str]:
    rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    new = []
    for word in words:
        for row in rows:
            if word[0].lower() in row:
                result = ""
                for char in word:
                    if char.lower() in row:
                        result += char
                    else:
                        break
                if result == word:
                    new.append(word)
    return new
