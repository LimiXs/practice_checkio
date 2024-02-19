"""
Given two integers, n and k, the task is to count how many numbers between 1 and n (inclusive) are divisible by k.
"""


def count_divisible(n: int, k: int) -> int:
    result = 0
    for i in range(1, n + 1):
        if i % k == 0:
            result += 1
    return result


print("Example:")
print(count_divisible(2, 1))

# These "asserts" are used for self-checking
assert count_divisible(10, 2) == 5
assert count_divisible(10, 3) == 3
assert count_divisible(10, 5) == 2
assert count_divisible(15, 4) == 3
assert count_divisible(20, 6) == 3
assert count_divisible(100, 10) == 10
assert count_divisible(200, 25) == 8
assert count_divisible(50, 7) == 7
assert count_divisible(60, 8) == 7
assert count_divisible(70, 9) == 7

print("The mission is done! Click 'Check Solution' to earn rewards!")
