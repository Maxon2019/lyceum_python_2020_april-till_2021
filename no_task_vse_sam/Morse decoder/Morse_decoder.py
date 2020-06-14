MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', '': '','SOS': '...---...',
                   '!': '-.-.--'}

def decoder(message):
    # extra space added at the end to access the
    # last morse code
    message = message.strip()
    i=0
    message += ' '
    decoder = ''
    citext = ''
    for letter in message:
        # checks for space
        if letter != ' ':
            # counter to keep track of space
            i = 0
            # storing morse code of a single character
            citext += letter
            # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
            # if i = 2 that indicates a new word
            if i == 2:
                # adding space to separate words
                decoder += ' '
            else:
                # accessing the keys using their values
                decoder += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''

    return decoder


def coder(message):
    Mcode = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # along with a space to separate
            # morse codes for different characters
            Mcode += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            Mcode += ' '

    return Mcode


if __name__ == '__main__':
    print(coder('SOS! I HAVE JUST BROKE MY STICK.'))
    print(decoder('... --- ... -.-.--  ..  .... .- ...- .  .--- ..- ... -  -... .-. --- -.- .  -- -.--  ... - .. -.-. -.- .-.-.- '))