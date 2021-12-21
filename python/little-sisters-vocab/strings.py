UN_PREFIX = "un"
EN_SUFFIX = "en"


def add_prefix_un(word: str) -> str:
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """

    return UN_PREFIX + word


def make_word_groups(vocab_words: list[str]) -> str:
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    prefix = vocab_words[0]
    new_words = [prefix + word for word in vocab_words[1:]]

    return " :: ".join([prefix, *new_words])


def remove_suffix_ness(word: str) -> str:
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """
    root_word = word.removesuffix("ness")
    return root_word[:-1] + "y" if root_word.endswith("i") else root_word


def noun_to_verb(sentence: str, index: int) -> str:
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """

    return sentence[:-1].split()[index] + EN_SUFFIX
