LYRICS = (
    ("first", "a Partridge in a Pear Tree"),
    ("second", "two Turtle Doves"),
    ("third", "three French Hens"),
    ("fourth", "four Calling Birds"),
    ("fifth", "five Gold Rings"),
    ("sixth", "six Geese-a-Laying"),
    ("seventh", "seven Swans-a-Swimming"),
    ("eighth", "eight Maids-a-Milking"),
    ("ninth", "nine Ladies Dancing"),
    ("tenth", "ten Lords-a-Leaping"),
    ("eleventh", "eleven Pipers Piping"),
    ("twelfth", "twelve Drummers Drumming"),
)


def recite(start_verse: int, end_verse: int) -> list[str]:
    return [
        f"On the {LYRICS[nth_day][0]} day of Christmas my true love gave to me: "
        f"{', '.join(LYRICS[nth_gift][1] for nth_gift in range(nth_day, 0, -1))}"
        f"{', and ' if nth_day > 0 else ''}{LYRICS[0][1]}."
        for nth_day in range(start_verse - 1, end_verse)
    ]
