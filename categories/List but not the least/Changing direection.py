"""
You are given a sequence of integers.
Your task in this mission is to find, how many times the sorting direction was changed in the given sequence.
If the elements are equal - the previous sorting direction remains the same,
if the sequence starts from the same elements - look for the next different to determine the sorting direction.

There are three sorting directions:

on the chunk 1, 2, 2 - up (increasing);
on the chunk 2, 1 - down (decreasing);
and on the chunk 1, 2, 2 - up again.
So, you have two points of changing the sorting direction: #1 - from up to down, and #2 - from down to up.
That's the result your function should return.
https://py.checkio.org/en/mission/changing-direction/
"""


def changing_direction(elements: list[int]) -> int:
    result = 0

    direction = None
    for i in range(1, len(elements)):
        if elements[i] > elements[i-1]:
            new_direction = "up"
        elif elements[i] < elements[i-1]:
            new_direction = "down"
        else:
            new_direction = direction

        if new_direction != direction and direction is not None:
            result += 1
        direction = new_direction

    return result


print("Example:")
print(changing_direction([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
