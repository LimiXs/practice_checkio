"""
"Sometimes, zeros resemble very tasty donut.
And every time we finish a donut, we want another, and then another, and then another..."

You are given list of integers (int).
Your task in this mission is to duplicate (..., 🍩, ... --> ..., 🍩, 🍩, ...)
all zeros (think about donuts ;-P) and return the result as any Iterable.
https://py.checkio.org/en/mission/duplicate-zeros/
"""

from collections.abc import Iterable


def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    result = []
    for val in donuts:
        if val == 0:
            result = result + [0, 0]
        else:
            result.append(val)
    return result


print("Example:")
print(list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])))

# These "asserts" are used for self-checking
assert list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])) == [
    1,
    0,
    0,
    2,
    3,
    0,
    0,
    4,
    5,
    0,
    0,
]
assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]

print("The mission is done! Click 'Check Solution' to earn rewards!")
