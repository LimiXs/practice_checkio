"""
You are given some string where you need to find its middle character(s).
The string may contain one word, a few symbols or a whole sentence.
If the length of the string is even, then you should return two middle characters,
but if the length is odd, return just one.
https://py.checkio.org/en/mission/middle-characters/
"""


def middle(text: str) -> str:
    if len(text) <= 2:
        return text

    if len(text) % 2 == 0:
        start = int((len(text) - 2) / 2)
        result = text[start: start + 2]
    else:
        start = int((len(text) - 1) / 2)
        result = text[start: start + 1]
    return result


print("Example:")
print(middle("example"))

# These "asserts" are used for self-checking
assert middle("example") == "m"
assert middle("test") == "es"

print("The mission is done! Click 'Check Solution' to earn rewards!")
