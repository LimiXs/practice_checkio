#  https://py.checkio.org/en/mission/list-beautify/
def list_beautify(data: list[list[int]]) -> str:
    transposed_data = list(map(list, zip(*data)))

    column_limit = {}
    for i, elm in enumerate(transposed_data):
        max_length = max(len(str(item)) for item in elm)
        column_limit[i] = max_length

    result = '['
    for k, row in enumerate(data):
        result += '['
        result += ', '.join(str(elm).rjust(column_limit[i]) for i, elm in enumerate(row))
        if k == len(data) - 1:
            result += ']'
        else:
            result += '],\n '
    result += ']'
    return result


print("Example:")
print(list_beautify([[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]))

# These "asserts" are used for self-checking
assert (
    list_beautify([[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]])
    == "[[ 1,   2,   10,  150],\n [10,   2, 1000,    2],\n [ 1, 120,    1, 1000]]"
)
assert list_beautify([[1, 10, 100, -1000]]) == "[[1, 10, 100, -1000]]"
assert (
    list_beautify([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
    == "[[1, 1, 1, 1, 1],\n [1, 1, 1, 1, 1],\n [1, 1, 1, 1, 1]]"
)
assert (
    list_beautify([[1, 1, -1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
    == "[[1, 1, -1, 1, 1],\n [1, 1,  1, 1, 1],\n [1, 1,  1, 1, 1]]"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
