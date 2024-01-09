"""
Create and return a new Iterable that contains the same elements as the given list items,
but with the reversed order of the elements inside every maximal strictly ascending subsequence.
This function should not modify the contents of the original list.
https://py.checkio.org/en/mission/reverse-every-ascending/
"""
from collections.abc import Iterable


def reverse_ascending(items: list[int]) -> Iterable[int]:
    res = []
    start = 0
    for i in range(1, len(items)):
        if items[i] <= items[i - 1]:
            res += items[start:i][::-1]
            start = i
    return res + items[start:][::-1]


print("Example:")
print(list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])))

# These "asserts" are used for self-checking
assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [
    10,
    7,
    5,
    4,
    8,
    7,
    2,
    3,
    1,
]
assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([])) == []
assert list(reverse_ascending([1])) == [1]
assert list(reverse_ascending([1, 1])) == [1, 1]
assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
