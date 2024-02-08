"""
This function should take an list of strings and determine the longest common prefix among all the strings.
If there is no common prefix, it should return an empty string.
https://py.checkio.org/en/mission/longest-common-prefix/
"""


def longest_prefix(arr: list[str]) -> str:
    result = ""
    if "" in arr:
        return result

    min_word = min(arr, key=len)
    start_len = len(min_word)

    for i in range(start_len - 1, -1, -1):
        iter_part = min_word[0:i + 1]
        set_parts = set([word[0:i + 1] for word in arr])
        if len(set_parts) == 1:
            return iter_part

    return result


print("Example:")
print(longest_prefix(["flower", "flow", "flight"]))

# These "asserts" are used for self-checking
assert longest_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_prefix(["dog", "racecar", "car"]) == ""
assert longest_prefix(["apple", "application", "appetizer"]) == "app"
assert longest_prefix(["a"]) == "a"
assert longest_prefix(["", "b"]) == ""
assert longest_prefix(["same", "same", "same"]) == "same"
assert longest_prefix(["mismatch", "mister", "miss"]) == "mis"
assert longest_prefix(["alphabet", "alpha", "alphadog"]) == "alpha"
assert longest_prefix(["book", "boot", "booster"]) == "boo"
assert longest_prefix(["short", "shore", "shot"]) == "sho"

print("The mission is done! Click 'Check Solution' to earn rewards!")
