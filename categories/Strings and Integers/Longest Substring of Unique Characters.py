"""
Given a string, find the length of the longest substring without repeating characters.
https://py.checkio.org/en/mission/longest-substring-of-unique-characters/
"""


def longest_substr(s: str) -> int:
    stack = ''
    sub_list = []
    while s:
        for i in s:
            if i not in stack:
                stack += i
            else:
                sub_list.append(stack)
                stack = ''

        sub_list.append(stack)
        stack = ''
        s = s[1:]

    return len(max(sub_list, key=len)) if sub_list else 0


print("Example:")
print(longest_substr("abcabcbb"))

# These "asserts" are used for self-checking
assert longest_substr("abcabcbb") == 3
assert longest_substr("bbbbb") == 1
assert longest_substr("pwwkew") == 3
assert longest_substr("abcdef") == 6
assert longest_substr("") == 0
assert longest_substr("au") == 2
assert longest_substr("dvdf") == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")
