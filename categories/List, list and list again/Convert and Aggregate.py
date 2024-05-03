"""
You are given a list of tuples. Each tuple consists of two values: a string and an integer.
You need to create and return a dictionary, where keys are string values from input tuples and values are aggregated
(summed) integer values from input tuples for each specific key.
The resulted dictionary should not include items with empty key or zero value.

https://py.checkio.org/en/mission/convert-and-aggregate/
"""


def conv_aggr(data: list[tuple[str, int]]) -> dict[str, int]:
    result = {}
    for key, value in data:
        if key and value:
            result[key] = result.get(key, 0) + value
    result = {k: v for k, v in result.items() if v != 0}
    return result


print("Example:")
print(conv_aggr([("a", 7), ("b", 8), ("a", 10)]))

assert conv_aggr([("a", 7), ("b", 8), ("a", 10)]) == {"a": 17, "b": 8}
assert conv_aggr([]) == {}
assert conv_aggr([("a", 5), ("a", -5)]) == {}
assert conv_aggr([("a", 5), ("a", 5), ("a", 0)]) == {"a": 10}
assert conv_aggr([("a", 5), ("", 15)]) == {"a": 5}

print("The mission is done! Click 'Check Solution' to earn rewards!")
