"""
A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.
https://py.checkio.org/en/mission/perfect-number-checking/
"""


def is_perfect(n: int) -> bool:

    div_list = [i for i in range(1, n) if n % i == 0]

    return False if sum(div_list) != n else True


print("Example:")
print(is_perfect(3))

# These "asserts" are used for self-checking
assert is_perfect(6) == True
assert is_perfect(2) == False
assert is_perfect(28) == True
assert is_perfect(20) == False
assert is_perfect(496) == True
assert is_perfect(30) == False
assert is_perfect(8128) == True
assert is_perfect(100) == False
assert is_perfect(500) == False
assert is_perfect(1000) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
