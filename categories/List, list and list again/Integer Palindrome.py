"""
https://py.checkio.org/en/mission/integer-palindrome/
"""


def int_palindrome(number: int, B: int) -> bool:
    cur_div = number
    result = ''

    while cur_div != 0:
        remainder = cur_div % B
        if remainder < 10:
            result += str(remainder)
        else:
            result += chr(ord('A') + remainder - 10)
        cur_div = int(cur_div / B)

    return result == result[::-1]


print("Example:")
print(int_palindrome(6, 3))

# These "asserts" are used for self-checking
assert int_palindrome(6, 2) == False
assert int_palindrome(34, 2) == False
assert int_palindrome(455, 2) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
