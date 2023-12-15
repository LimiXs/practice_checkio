"""
In this mission you should follow a given list of instructions which will get you to a certain point on the map.
A list of instructions is a string, each letter of this string points you in the direction of your next step.

The letter "f" - tells you to move forward, "b" - backward, "l" - left, and "r" - right.

It means that if the list of your instructions is "fflff" then you should move forward two times,
make one step to the left and then again move two times forward.

Now, let's imagine that you are in the position (0, 0). If you move forward your position will change to (0, 1).
If you move again it will be (0, 2). If your next step is to the left then your position will become (-1, 2).
After the next two steps forward your coordinates will be (-1, 4).

Your goal is to find your final coordinates. Like in our case they are (-1, 4).

Input: A string (str).

Output: A tuple or list of two integers (int).

https://py.checkio.org/en/mission/follow-instructions/
"""
COMMANDS = {
    'f': (1, 1),
    'b': (1, -1),
    'r': (0, 1),
    'l': (0, -1)
}


def follow(instructions: str) -> tuple[int, int] | list[int]:
    result = [0, 0]

    for pointer in instructions:
        index = COMMANDS.get(pointer)[0]
        operation = COMMANDS.get(pointer)[1]
        result[index] += operation

    return result[0], result[1]


print("Example:")
print(list(follow("fflff")))

# These "asserts" are used for self-checking
assert list(follow("fflff")) == [-1, 4]
assert list(follow("ffrff")) == [1, 4]
assert list(follow("fblr")) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")
