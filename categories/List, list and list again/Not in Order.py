def not_order(data: list[int]) -> int:
    if len(data) <= 2:
        return 0
    sort_data = sorted(data)

    result = 0
    for i, v in enumerate(sort_data):
        if v != data[i]:
            result += 1

    return result


print("Example:")
print(not_order([1, 1, 4, 2, 1, 3]))

# These "asserts" are used for self-checking
assert not_order([1, 1, 4, 2, 1, 3]) == 3
assert not_order([]) == 0
assert not_order([1, 1, 1, 1, 1]) == 0
assert not_order([1, 2, 3, 4, 5]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
