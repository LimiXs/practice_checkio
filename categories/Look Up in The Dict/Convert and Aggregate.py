"""
You are given a list of tuples. Each tuple consists of two values: a string and an integer.
You need to create and return a dictionary, where keys are string values from input tuples and
values are aggregated (summed) integer values from input tuples for each specific key.
The resulted dictionary should not include items with empty key or zero value.
https://py.checkio.org/en/mission/convert-and-aggregate/
"""


def conv_aggr(data: list[tuple[str, int]]) -> dict[str, int]:
    result = {}

    for elm in data:
        key = elm[0]
        value = elm[1]

        if not key:
            continue

        if key not in result:
            result[key] = value
        else:
            result[key] += value

    return {key: val for key, val in result.items() if val != 0}


print("Example:")
print(conv_aggr([("a", 7), ("b", 8), ("a", 10)]))

assert conv_aggr([("a", 7), ("b", 8), ("a", 10)]) == {"a": 17, "b": 8}
assert conv_aggr([]) == {}
assert conv_aggr([("a", 5), ("a", -5)]) == {}
assert conv_aggr([("a", 5), ("a", 5), ("a", 0)]) == {"a": 10}
assert conv_aggr([("a", 5), ("", 15)]) == {"a": 5}

print("The mission is done! Click 'Check Solution' to earn rewards!")
