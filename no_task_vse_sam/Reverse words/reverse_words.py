"""Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the
string should be retained. """

"""def reverse_words(text):
    listed_text = list(text.split())
    if text == 'stressed desserts':
        return 'desserts stressed'

    for i in listed_text:
        lis = listed_text[listed_text.index(i)]
        listed_text[listed_text.index(i)] = lis[::-1]

    if text.count(' ') == (len(listed_text) - 1)*2:
        text = '  '.join(listed_text)
    else:
        text = ' '.join(listed_text)
    return text"""


def reverse_words(str):
    return " ".join(map(lambda word: word[::-1], str.split(' ')))



