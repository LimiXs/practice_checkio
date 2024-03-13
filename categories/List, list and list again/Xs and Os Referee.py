"""
https://py.checkio.org/en/mission/x-o-referee/
"""


def checkio(game_result: list[str]) -> str:
    for row in game_result:
        if row[0] == row[1] == row[2] and row[0] != ".":
            return row[0]

    rotated_result = zip(*game_result)

    for row in rotated_result:
        if row[0] == row[1] == row[2] and row[0] != ".":
            return row[0]

    if game_result[0][0] == game_result[1][1] == game_result[2][2] and game_result[0][0] != ".":
        return game_result[0][0]

    if game_result[2][0] == game_result[1][1] == game_result[0][2] and game_result[2][0] != ".":
        return game_result[2][0]

    return "D"


print("Example:")
print(checkio(["X.O", "XX.", "XOO"]))

# These "asserts" are used for self-checking
assert checkio(["X.O", "XX.", "XOO"]) == "X"
assert checkio(["OO.", "XOX", "XOX"]) == "O"
assert checkio(["OOX", "XXO", "OXX"]) == "D"
assert checkio(["O.X", "XX.", "XOO"]) == "X"

print("The mission is done! Click 'Check Solution' to earn rewards!")
