EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2  # equal to the time it takes to prepare a single layer


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.

    Parameters
    ----------
    elapsed_bake_time : int
        baking time already elapsed

    Returns
    -------
    int
        remaining bake time derived from 'EXPECTED_BAKE_TIME'
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate how many minutes you would spend making layers
    of the lasagna."""
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(
    number_of_layers: int, elapsed_bake_time: int
) -> int:  # noqa
    """Return elapsed cooking time.

    This function takes two numbers representing the number of layers
    & the time already spent baking and calculates the total elapsed
    minutes spent cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
