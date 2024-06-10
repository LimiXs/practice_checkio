#  https://py.checkio.org/en/mission/beat-the-previous/
def beat_previous(digits: str) -> list[int]:
    if not digits:
        return []

    result = [int(digits[0])]
    cur_max = int(digits[0])

    digits = digits[1:]

    while digits:
        zero_flag = True

        for i, v in enumerate(digits):
            if zero_flag and v == '0':
                digits = digits[i+1:]
                break

            if v > cur_max:
                cur_max = v
                result.append(int(v))
                digits = digits[i+1:]
                break

    return result


print("Example:")
print(beat_previous("001203"))

# These "asserts" are used for self-checking
assert beat_previous("600005") == [6]
assert beat_previous("6000050") == [6, 50]
assert beat_previous("045349") == [0, 4, 5, 34]
assert beat_previous("77777777777777777777777") == [7, 77, 777, 7777, 77777, 777777]

print("The mission is done! Click 'Check Solution' to earn rewards!")
