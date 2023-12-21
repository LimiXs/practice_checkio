"""
Sort the integers in sequence in sequence. But the position of zeros should not be changed.
https://py.checkio.org/en/mission/sort-except-zero/
"""
from collections.abc import Iterable


def except_zero(items: list[int]) -> Iterable[int]:
    result = [0 if i == 0 else 1 for i in items]
    non_zero_sorted = sorted([i for i in items if i != 0])
    counter = 0
    for i, item in enumerate(result):
        if item == 1:
            result[i] = non_zero_sorted[counter]
            counter += 1
    return result


print("Example:")
print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

# These "asserts" are used for self-checking
assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
assert list(except_zero([0, 0])) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")
