"""Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even
indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing
just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if
there are multiple words. Words will be separated by a single space(' '). """


def transform_word(s):
    return ''.join(x.upper() if i % 2 == 0 else x.lower() for i, x in enumerate(s))


def to_weird_case(string):
    return ' '.join(transform_word(s) for s in string.split())


if __name__ == '__main__':
    print(to_weird_case('Weird string case'))
