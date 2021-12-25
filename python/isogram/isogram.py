import re


def is_isogram(word: str) -> bool:
    cleaned_word = re.sub(r"\s|-", "", word.lower())
    chars = [char for char in cleaned_word if char.isalpha()]
    return len(cleaned_word) == len(set(chars))
