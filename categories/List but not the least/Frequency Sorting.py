"""
Sort the given sequence so that its elements should be grouped and groups end up in the decreasing frequency order,
that is, the number of times element appears in the sequence. If two elements have the same frequency,
their groups should end up according to the natural order of elements.
https://py.checkio.org/en/mission/frequency-sorting/
"""
from collections.abc import Iterable


def frequency_sorting(numbers: list[int]) -> Iterable[int]:
    uniq_numbers = set(numbers)
    count_numbers = {}
    for v in uniq_numbers:
        count_numbers[v] = numbers.count(v)

    sorted_dict = dict(sorted(sorted(count_numbers.items()), key=lambda x: x[1], reverse=True))
    result = []
    for key, value in sorted_dict.items():
        result.extend([key] * value)
    return result


print("Example:")
print(list(frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10])))

# These "asserts" are used for self-checking
assert list(frequency_sorting([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
assert list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])) == [
    4,
    4,
    4,
    3,
    3,
    11,
    11,
    7,
    13,
]
assert list(frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10])) == [10, 10, 21, 21, 55, 55, 99, 99]

print("The mission is done! Click 'Check Solution' to earn rewards!")
