"""
A median is a numerical value separating the upper half of a sorted list of numbers from the lower half.
In list where there are an odd number of entities, the median is the number found in the middle of the list.
If the list contains an even number of entities,
then there is no single middle value,
instead the median becomes the average of the two numbers found in the middle.
For this mission, you are given a non-empty list of integers (int).
With it, you must separate the upper half of the numbers from the lower half and find the median.

Input: List with integers (int).

Output: The median as an integer or float (int | float).

Examples:

assert checkio([1, 2, 3, 4, 5]) == 3
assert checkio([3, 1, 2, 5, 3]) == 3
assert checkio([1, 300, 2, 200, 1]) == 2
assert checkio([3, 6, 20, 99, 10, 15]) == 12.5

https://py.checkio.org/en/mission/median/
"""


def checkio(data: list[int]) -> int | float:
    if not data:
        return 0
    if len(data) == 1:
        return data[0]

    data.sort()
    medium = int(len(data) / 2)

    if len(data) % 2 == 0:
        left = data[medium - 1]
        right = data[medium]
        return (left + right) / 2

    return data[int(len(data) / 2 - 0.5)]


print("Example:")
print(checkio([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert checkio([1, 2, 3, 4, 5]) == 3
assert checkio([3, 1, 2, 5, 3]) == 3
assert checkio([1, 300, 2, 200, 1]) == 2
assert checkio([3, 6, 20, 99, 10, 15]) == 12.5
assert checkio([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
assert checkio([0, 7, 1, 8, 4, 9, 5, 6, 2, 3]) == 4.5
assert checkio([33, 56, 62]) == 56
assert checkio([21, 56, 84, 82, 52, 9]) == 54
assert checkio([100, 1, 1, 1, 1, 1, 1]) == 1
assert checkio([64, 6, 92, 7, 70, 5]) == 35.5

print("The mission is done! Click 'Check Solution' to earn rewards!")
