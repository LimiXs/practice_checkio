"""
Your function should create a list of lists,
that represents a two-dimensional grid with the given number of rows and cols.

This grid should contain integers (int) from start to start + rows * cols - 1 in ascending order,
but the elements of every odd-index row have to be listed in descending order,
so that when read in ascending order, the numbers zigzag through the two-dimensional grid.
https://py.checkio.org/en/mission/zigzag-array/
"""


def create_zigzag(rows: int, cols: int, start: int = 1) -> list[list[int]]:
    result = []
    for row in range(rows):
        if row % 2 == 0:
            result.append(list(range(start, start + cols)))
        else:
            result.append(list(range(start + cols - 1, start - 1, -1)))
        start += cols
    return result


print("Example:")
print(create_zigzag(3, 5))

# These "asserts" are used for self-checking
assert create_zigzag(3, 5) == [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15]]
assert create_zigzag(5, 1) == [[1], [2], [3], [4], [5]]
assert create_zigzag(3, 3, 5) == [[5, 6, 7], [10, 9, 8], [11, 12, 13]]

print("The mission is done! Click 'Check Solution' to earn rewards!")
