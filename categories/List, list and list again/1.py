def sorted_groups(items: list[int]) -> list[int]:
    if len(items) < 2:
        return items

    group_items = []
    index_start = 0

    for i, num in enumerate(items):
        if i == 0:
            continue

        if num < items[i-1]:
            group_items.append(items[index_start:i])
            index_start = i
            if len(items) == i + 1:
                group_items.append([items[-1]])

        if len(items) == i + 1 and not num < items[i-1]:
            group_items.append(items[index_start:i + 1])

    group_items.sort(key=lambda x: x[0], reverse=True)
    return sum(group_items, [])


print("Example:")
print(sorted_groups([5, 1, 5, 0, 5]))

# These "asserts" are used for self-checking
assert sorted_groups([]) == []
assert sorted_groups([5]) == [5]
assert sorted_groups([5, 1, 5, 0, 5]) == [5, 5, 0, 5, 1]
assert sorted_groups([5, 5, 1]) == [5, 5, 1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
