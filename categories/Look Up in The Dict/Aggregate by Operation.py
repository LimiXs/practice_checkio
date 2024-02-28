"""
https://py.checkio.org/en/mission/aggregate-by-operation/
"""
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0,
    "=": lambda _, b: b
}


def aggr_operation(data: list[tuple[str, int]]) -> dict[str, int]:
    result = {}
    for elm in data:

        operator = elm[0][0]
        name_val = elm[0][1:]
        if not name_val:
            continue

        if name_val not in result:
            result[name_val] = 0

        operation = operations.get(operator, None)
        if operation is None:
            continue
        result[name_val] = operation(result[name_val], elm[1])

    new_r = {key: val for key, val in result.items() if val != 0}
    print(new_r)
    return new_r


print(aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]))

# These "asserts" are used for self-checking
assert aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]) == {"a": 70, "b": -8}
assert aggr_operation([]) == {}
assert aggr_operation([("+a", 5), ("+a", -5), ("-a", 5), ("-a", -5)]) == {}
assert aggr_operation([("*a", 0), ("=a", 0), ("/a", 0), ("-a", -5)]) == {"a": 5}

print("The mission is done! Click 'Check Solution' to earn rewards!")
