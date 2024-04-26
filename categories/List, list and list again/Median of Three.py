"""
https://py.checkio.org/en/mission/median-of-three/
"""

from typing import Iterable


def median_three(els: Iterable[int]) -> Iterable[int]:
    result = []
    if len(list(els)) < 3:
        return els

    for i, v in enumerate(list(els)):
        if i == 0 or i == 1:
            result.append(v)
            continue

        median = els[i-2:i+1]
        result.append(sorted(median)[1])

    return result


print("Example:")
print(list(median_three([1, 2, 3, 4, 5, 6, 7])))

assert median_three([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 2, 3, 4, 5, 6]
assert median_three([1]) == [1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
