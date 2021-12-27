import re

PATTERN = r"[A-Z0-9]+(?:'[A-Z]+)?"


def abbreviate(words: str) -> str:
    return "".join(word[0] for word in re.findall(PATTERN, words.upper()))
