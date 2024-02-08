"""
Calculate sum of integers from 1 to given N (including).
https://py.checkio.org/en/mission/sum-of-integers/
"""


def sum_up_to_n(N: int) -> int:
    return sum([i for i in range(0, N + 1)])


print("Example:")
print(sum_up_to_n(11))

# These "asserts" are used for self-checking
assert sum_up_to_n(1) == 1
assert sum_up_to_n(2) == 3
assert sum_up_to_n(3) == 6
assert sum_up_to_n(4) == 10
assert sum_up_to_n(5) == 15
assert sum_up_to_n(10) == 55
assert sum_up_to_n(20) == 210
assert sum_up_to_n(100) == 5050
assert sum_up_to_n(200) == 20100
assert sum_up_to_n(500) == 125250

print("The mission is done! Click 'Check Solution' to earn rewards!")
