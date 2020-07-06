"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks
untouched.
"""
symbols = ['/', ',', '.', "'", '"', '!', '#', '@', '%', '(', ')', '=', '+', '*', '&', '?', '_', '-', ':', ';', '<', '>']


def pig_it(text):
    final_list = []
    to_pig_text_list = text.split()
    for i in to_pig_text_list:
        if i in symbols:
            final_list.append(i)
        else:
            first_let = i[0]
            i = i.replace(i[0], '')
            i += first_let + 'ay'
            final_list.append(i)
    return ' '.join(final_list)


if __name__ == '__main__':
    print(pig_it('Hello world !'))
