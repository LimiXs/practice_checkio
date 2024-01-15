def nested_sum(items):
    total = 0
    for i in items:
        if isinstance(i, list):
            total += nested_sum(i)
        else:
            total += i
    return total


print(nested_sum([[5, 4, 7], [3, 4, 5], [4]]))
