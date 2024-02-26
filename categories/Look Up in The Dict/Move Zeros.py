"""
You are given a list of integers. Move all zeros in the list to the end of it.
The order of non-zero elements should not change.
https://py.checkio.org/en/mission/move-zeros/
"""
from typing import Iterable


def move_zeros(items: list[int]) -> Iterable[int]:

    result = [x for x in items if x != 0]
    zero_count = items.count(0)

    for _ in range(zero_count):
        result.append(0)

    return result


print("Example:")
print(list(move_zeros([0, 1, 0, 3, 12])))

# These "asserts" are used for self-checking
assert list(move_zeros([0, 1, 0, 3, 12])) == [1, 3, 12, 0, 0]
assert list(move_zeros([0])) == [0]

print("The mission is done! Click 'Check Solution' to earn rewards!")
