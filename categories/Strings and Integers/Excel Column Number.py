"""
Given a string that represents the column title as appears in an Excel sheet, return its corresponding column number.

But how does the Excel column numbering actually work? Well, the column number is like decimal number,
but with base (radix) 26 and "digits" A-Z. Read more about number bases. Let's look at the exact numbers:

Excel   Decimal
    A   1
   ..
    Z   26
https://py.checkio.org/en/mission/excel-column-number/
"""


def column_number(name: str) -> int:
    result = 0
    while name:
        result += (26 ** (len(name) - 1)) * (ord(name[0]) - 64)
        name = name[1:]

    return result


print("Example:")
print(column_number("AA"))

# These "asserts" are used for self-checking
assert column_number("A") == 1
assert column_number("Z") == 26
assert column_number("AB") == 28
assert column_number("ZY") == 701

print("The first mission is done! Click 'Check' to earn cool rewards!")
