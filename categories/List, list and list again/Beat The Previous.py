#  https://py.checkio.org/en/mission/beat-the-previous/
def beat_previous(digits: str) -> list[int]:
    if not digits:
        return []

    result = [int(digits[0])]
    cur_max = int(digits[0])

    digits = digits[1:]
    while digits:

        counter = 0
        raise_value = int(digits[0])
        while cur_max >= raise_value:
            counter += 1
            if cur_max > raise_value and counter == len(digits):
                break

            raise_value = int(str(raise_value) + digits[counter])
            if counter == len(digits) - 1:
                break

        if cur_max > raise_value:
            break

        result.append(raise_value)
        if counter == len(digits) - 1:
            break
        cur_max = raise_value
        digits = digits[counter+1:]

    return result


print("Example:")
print(beat_previous("77777777777777777777777"))

# These "asserts" are used for self-checking
assert beat_previous("600005") == [6]
assert beat_previous("6000050") == [6, 50]
assert beat_previous("045349") == [0, 4, 5, 34]
assert beat_previous("77777777777777777777777") == [7, 77, 777, 7777, 77777, 777777]

print("The mission is done! Click 'Check Solution' to earn rewards!")
