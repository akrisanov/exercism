def get_rounds(number: int) -> list[int]:
    """

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return list(range(number, number + 3))


def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return [*rounds_1, *rounds_2]


def list_contains_round(rounds: list[int], number: int) -> bool:
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    return number in rounds


def card_average(hand: list[int]) -> float:
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand: list[int]) -> bool:
    """

    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """

    hand_avg = card_average(hand)
    approx_avg = card_average([hand[0], hand[-1]])
    median = hand[int(len(hand) / 2)]

    return hand_avg in (approx_avg, median)


def average_even_is_average_odd(hand: list[int]) -> bool:
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    rounds_odd_idx = hand[::1]
    rounds_even_idx = hand[::2]

    return card_average(rounds_odd_idx) == card_average(rounds_even_idx)


JOE_CARD = 11


def maybe_double_last(hand: list[int]) -> list[int]:
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == JOE_CARD:
        hand[-1] *= 2
    return hand
