"""
Sort the given list so that its elements should be grouped and those groups end up in the decreasing frequency order,
that is, the number of times element appears in list. If two elements have the same frequency,
their groups should end up in the same order as the first appearance of element in the list.
https://py.checkio.org/en/mission/sort-array-by-element-frequency/
"""
from typing import Iterable


def frequency_sort(items: list[str | int]) -> Iterable[str | int]:
    if len(items) <= 1:
        return items

    seen = set()
    uniq = [x for x in items if not (x in seen or seen.add(x))]
    seen = {k: items.count(k) for k in uniq}

    group_seen = {}
    for k, v in seen.items():
        if v not in group_seen:
            group_seen[v] = [k]
        else:
            group_seen[v].append(k)

    group_seen = dict(sorted(group_seen.items(), key=lambda x: x[0], reverse=True))
    result = []
    for key in group_seen:
        for value in group_seen[key]:
            result.extend([value] * key)

    return result


print("Example:")
print(list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])))

# These "asserts" are used for self-checking
assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 2, 2, 2, 6, 6]
assert list(frequency_sort(["bob", "bob", "carl", "alex", "bob"])) == [
    "bob",
    "bob",
    "bob",
    "carl",
    "alex",
]
assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
assert list(frequency_sort([])) == []
assert list(frequency_sort([1])) == [1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
