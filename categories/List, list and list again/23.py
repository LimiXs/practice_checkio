"""
The main architect of the city wants to build a new highest building.
You have to help him find the current highest building in the city.
https://py.checkio.org/en/mission/the-highest-building/
"""


def highest_building(buildings: list[list[int]]) -> list[int]:
    buildings = list(map(list, zip(*buildings)))

    heights = [sum(building) for building in buildings]

    highest_building = max(range(len(heights)), key=heights.__getitem__) + 1
    highest_height = max(heights)

    return [highest_building, highest_height]


print("Example:")
print(highest_building([[0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1]]))

# These "asserts" are used for self-checking
assert highest_building([[0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1]]) == [
    3,
    4,
]
assert highest_building([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]) == [
    4,
    1,
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
