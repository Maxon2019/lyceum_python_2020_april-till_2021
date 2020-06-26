"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within
the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often
referred to as Pascal case).
"""


def to_camel_case(text):
    text_first = text
    text = text.title()

    if text.count('-') > 0:
        text_list = text.split('-')
        text_first_list = text_first.split('-')
    else:
        text_list = text.split('_')
        text_first_list = text_first.split('-')
    if text_list[0] == text_first_list[0]:
        pass
    else:
        text_list[0] = text_list[0].lower()

    return ''.join(text_list)


if __name__ == "__main__":
    print(to_camel_case("The-stealth-warrior"))
