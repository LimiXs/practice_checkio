def sorted_groups(items: list[int]) -> list[int]:
    groups, i = [], 1

    while items:
        if len(items) == 1:
            groups.append([items.pop()])
            break
        if i < len(items) and items[i] == items[i - 1]:
            i += 1
            continue
        if i < len(items) and items[i] > items[i - 1]:
            while i < len(items) and items[i] >= items[i - 1]:
                i += 1
        elif i < len(items) and items[i] < items[i - 1]:
            while i < len(items) and items[i] <= items[i - 1]:
                i += 1
        groups.append(items[:i])
        items, i = items[i:], 1
    result = []
    for group in sorted(groups):
        result += group

    return result


print("Example:")
print(sorted_groups([5, 1, 5, 0, 5]))

# These "asserts" are used for self-checking
assert sorted_groups([]) == []
assert sorted_groups([5]) == [5]
assert sorted_groups([5, 1, 5, 0, 5]) == [5, 5, 0, 5, 1]
assert sorted_groups([5, 5, 1]) == [5, 5, 1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
