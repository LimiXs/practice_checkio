"""
You are given a sequence of integers, which are elements of arithmetic progression -
the difference between the consecutive elements is constant.
But this sequence is unsorted and one element is missing...good luck!

assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4
https://py.checkio.org/en/mission/missing-number/
"""


def missing_number(items: list[int]) -> int:
    if len(items) <= 2:
        return 0

    sorted_items = sorted(items)

    for i, elem in enumerate(sorted_items):
        if i == 0:
            continue
        if elem - items[i - 1] != 1:
            return items[i - 1] + 1
    return 0


print("Example:")
print(missing_number([1, 4, 2, 5]))

# These "asserts" are used for self-checking
assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
