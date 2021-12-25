def convert(number: int) -> str:
    words = {3: "Pling", 5: "Plang", 7: "Plong"}
    return "".join([word for div, word in words.items() if number % div == 0]) or str(
        number
    )


# flake8: noqa
# Conditionals:
# def convert(number: int) -> str:
#     raindrops = ""

#     if number % 3 == 0:
#         raindrops += "Pling"
#     if number % 5 == 0:
#         raindrops += "Plang"
#     if number % 7 == 0:
#         raindrops += "Plong"

#     return raindrops or str(number)
