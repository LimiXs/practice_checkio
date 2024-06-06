#  https://py.checkio.org/en/mission/colorful-disks/
def count_discs(discs: tuple[int, ...]) -> int:
    if not discs:
        return 0
    if len(discs) == 1:
        return 1

    max_value = max(discs)
    reversed_discs = list(reversed(list(discs)))
    cur_max = reversed_discs[0]

    result = 1
    for i, v in enumerate(reversed_discs):
        if v == max_value:
            result += 1
            break

        if i == 0 or v < reversed_discs[i - 1]:
            continue

        if v > reversed_discs[i - 1]:
            if cur_max > v:
                continue
            result += 1
            cur_max = v

    return result


print("Example:")
print(count_discs((3, 6, 7, 4, 5, 1, 2)))

# These "asserts" are used for self-checking
assert count_discs((3, 6, 7, 4, 5, 1, 2)) == 3
assert count_discs((6, 5, 4, 3, 2, 1)) == 6
assert count_discs((5,)) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
