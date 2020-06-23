alphabet = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10',
            'k': '11', 'l': '12', 'm': '13',
            'n': '14', 'o': '15', 'p': '16', 'q': '17',
            'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}
nums = list('1234567890')

num_text = []


def alphabet_position(text):
    mini_text = text.lower()
    for i in mini_text:
        if i == '':
            num_text.append('')
        elif i in nums:
            num_text.append('')
        elif i == ' ':
            num_text.append('')
        else:
            num_text.append(alphabet[i])
    for i in num_text:
        if i == '':
            num_text.remove(i)
    nums_text = ' '.join(num_text)
    return nums_text


if __name__ == "__main__":
    print(alphabet_position('OI11JOJO111'))
