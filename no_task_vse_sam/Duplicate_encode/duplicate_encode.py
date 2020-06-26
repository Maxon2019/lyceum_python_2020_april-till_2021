"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if
that character appears only once in the original string, or ")" if that character appears more than once in the 
original string. Ignore capitalization when determining if a character is a duplicate.
"""


def duplicate_encode(word):
    word = word.lower()
    word_list = list(word)
    for i in word_list:
        counter = word_list.count(i)
        if counter > 1:
            word = word.replace(i, ')')
        elif counter <= 1:
            word = word.replace(i, '(')
    return word


if __name__ == "__main__":
    print(duplicate_encode('cHG(za T I zwTSRGTP v!amPnu(!cHSQu'))
