import re
from collections import Counter

PATTERN = r"[a-z0-9]+(?:'[a-z]+)?"


def count_words(sentence: str) -> dict[str, int]:
    return Counter(re.findall(PATTERN, sentence.lower()))
