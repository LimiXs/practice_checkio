"""
You have a list. Each value from that list can be either a string or an integer. Your task here is to return two values.
The first one is a concatenation of all strings from the given list.
The second one is a sum of all integers from the given list.
"""
from typing import Tuple


def sum_by_types(items: list) -> Tuple[str, int]:
    sum_str = ""
    sum_int = 0
    for i in items:
        str_type = str(type(i))
        if str_type == "<class 'str'>":
            sum_str += i
        elif str_type == "<class 'int'>":
            sum_int += i
    return tuple([sum_str, sum_int])


if __name__ == "__main__":
    print("Example:")
    print(sum_by_types([]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_by_types([]) == ("", 0)
    assert sum_by_types([1, 2, 3]) == ("", 6)
    assert sum_by_types(["1", 2, 3]) == ("1", 5)
    assert sum_by_types(["1", "2", 3]) == ("12", 3)
    assert sum_by_types(["1", "2", "3"]) == ("123", 0)
    assert sum_by_types(["size", 12, "in", 45, 0]) == ("sizein", 57)
    print("Coding complete? Click 'Check' to earn cool rewards!")
