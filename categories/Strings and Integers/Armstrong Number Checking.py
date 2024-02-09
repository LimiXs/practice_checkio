"""
In number theory, an Armstrong number (after Michael F. Armstrong) or narcissistic number in a given number base
(10 for this mission) is a number that is the sum of its own digits each raised to the power of the number of digits.
For example, 153 is an Armstrong number because 13 + 53 + 33 == 153.
https://py.checkio.org/en/mission/armstrong-number-checking/
"""


def is_armstrong(num: int) -> bool:
    str_num = str(num)
    pow_len = len(str_num)

    result = 0
    for v in str_num:
        result += int(v)**int(pow_len)

    return True if result == num else False


print("Example:")
print(is_armstrong(11))

# These "asserts" are used for self-checking
assert is_armstrong(153) == True
assert is_armstrong(370) == True
assert is_armstrong(947) == False
assert is_armstrong(371) == True
assert is_armstrong(407) == True
assert is_armstrong(163) == False
assert is_armstrong(100) == False
assert is_armstrong(8208) == True
assert is_armstrong(930) == False
assert is_armstrong(4) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
