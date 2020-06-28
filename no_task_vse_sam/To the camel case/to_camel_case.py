"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within
the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often
referred to as Pascal case).
"""


def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0] + ''.join([x.capitalize() for x in removed[1:]])


if __name__ == "__main__":
    print(to_camel_case("The_stealth_warrior"))
