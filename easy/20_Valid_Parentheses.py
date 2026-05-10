def isValid(s: str) -> bool:
    text = ""
    for x in s:
        if x in "{}[]()":
            text += x
        text = text.replace('{}', "")
        text = text.replace('()', "")
        text = text.replace('[]', "")
    return text == ""
