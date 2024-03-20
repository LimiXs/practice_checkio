"""
You have to split a given list into two lists inside an Iterable.
If input sequence has an odd amount of elements, then the first list inside result Iterable should have more elements.
If input sequence has no elements, then two empty lists inside result Iterable should be returned.
https://py.checkio.org/en/mission/split-list/
"""
from typing import Any, Iterable


def split_list(items: list[Any]) -> Iterable[list[Any]]:
    if not items:
        return [[], []]
    if len(items) == 1:
        return [items[0:], []]

    if len(items) % 2 == 0:
        return [items[0:int(len(items) / 2)], items[int(len(items) / 2):]]
    return [items[0:int(len(items) / 2 + 1)], items[int(len(items) / 2 + 1):]]


print("Example:")
print(list(split_list([1, 2, 3, 4, 5, 6])))

assert list(split_list([1, 2, 3, 4, 5, 6])) == [[1, 2, 3], [4, 5, 6]]
assert list(split_list([1, 2, 3])) == [[1, 2], [3]]
assert list(split_list(["banana", "apple", "orange", "cherry", "watermelon"])) == [
    ["banana", "apple", "orange"],
    ["cherry", "watermelon"],
]
assert list(split_list([1])) == [[1], []]
assert list(split_list([])) == [[], []]

print("The mission is done! Click 'Check Solution' to earn rewards!")
