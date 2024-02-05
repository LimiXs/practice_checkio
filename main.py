def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
    mistakes = 0
    if len(str1) != len(str2):
        mistakes += mistakes

    for i in range(0, len(min(str1, str2, key=len))):

        print(str1[i], str2[i])
        if str1[i] != str2[i]:
            print(i, mistakes)
            mistakes += 1

    return False if mistakes >= threshold else True


print("Example:")
# print(fuzzy_string_match("apple", "bpple", 0))

# These "asserts" are used for self-checking
# assert fuzzy_string_match("apple", "appel", 2) == True
# assert fuzzy_string_match("apple", "bpple", 1) == True
# assert fuzzy_string_match("apple", "bpple", 0) == False
# assert fuzzy_string_match("apple", "apples", 1) == True
# assert fuzzy_string_match("apple", "bpples", 2) == True
# assert fuzzy_string_match("apple", "apxle", 1) == True
assert fuzzy_string_match("apple", "pxxli", 3) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
