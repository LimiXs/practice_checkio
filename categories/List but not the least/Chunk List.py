"""
Split list into smaller lists of the same size (chunks).
The last chunk can be smaller than the default chunk-size.
If the given list is empty, then you shouldn't have any chunks at all.
https://py.checkio.org/en/mission/chunk/
"""
from collections.abc import Iterable


def nested_sum(items):
    total = 0
    for i in items:
        if isinstance(i, list):
            total += nested_sum(i)
        else:
            total += i
    return total


def chunking_by(items: list[int], size: int) -> Iterable[list[int]]:
    result = []
    start = 0
    end = size
    while sum(items) != nested_sum(result):
        result.append(items[start:end])
        start += size
        end += size
    return result


print("Example:")
print(list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)))

# These "asserts" are used for self-checking
assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [[5, 4, 7], [3, 4, 5], [4]]
assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
assert list(chunking_by([5, 4], 7)) == [[5, 4]]
assert list(chunking_by([], 3)) == []
assert list(chunking_by([4, 4, 4, 4], 4)) == [[4, 4, 4, 4]]

print("The mission is done! Click 'Check Solution' to earn rewards!")
