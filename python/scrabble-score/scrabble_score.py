VALUES = {
    **dict.fromkeys({"A", "E", "I", "O", "U", "L", "N", "R", "S", "T"}, 1),
    **dict.fromkeys({"D", "G"}, 2),
    **dict.fromkeys({"B", "C", "M", "P"}, 3),
    **dict.fromkeys({"F", "H", "V", "W", "Y"}, 4),
    **dict.fromkeys({"K"}, 5),
    **dict.fromkeys({"J", "X"}, 8),
    **dict.fromkeys({"Q", "Z"}, 10),
}


def score(word: str) -> int:
    return sum([VALUES[letter] for letter in word.upper()])
