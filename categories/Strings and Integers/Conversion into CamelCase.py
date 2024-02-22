"""
Your mission is to convert the name of a function from the Python format
(for example "my_function_name") into CamelCase ("MyFunctionName")
where the first char of every word is in uppercase and all words are concatenated without any intervening characters.
https://py.checkio.org/en/mission/conversion-into-camelcase/
"""


def to_camel_case(name: str) -> str:
    lst = name.split("_")

    for i in range(len(lst)):
        lst[i] = lst[i].capitalize()

    return "".join(lst)


if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('this_function_is_empty'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
