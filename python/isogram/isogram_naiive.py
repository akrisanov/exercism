import string


def is_isogram(word: str) -> bool:
    word = word.lower()
    repeatable = string.whitespace + string.punctuation

    for char in word:
        if char not in repeatable and word.count(char) > 1:
            return False
    return True
