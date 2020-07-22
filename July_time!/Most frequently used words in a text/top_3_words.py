"""Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the 
top-3 most occurring words, in descending order of the number of occurrences. 

Assumptions: A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII. (No 
need to handle fancy punctuation.) Matches should be case-insensitive, and the words in the result should be 
lowercased. Ties may be broken arbitrarily. If a text contains fewer than three unique words, then either the top-2 
or top-1 words should be returned, or an empty array if a text contains no words.
 """
symbols = ['"', '.', ',', ':', ';', '(', ')', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%',
           '^', '&', '*', '/', '|']


def top_3_words(text):
    d = dict()
    print(len(symbols))
    counter = 0
    text = list(text)
    print(text)

    while len(symbols) > counter:
        if symbols[counter] in text:
            it = text.count(symbols[counter])
            while it > 0:
                text.remove(symbols[counter])
                print(f'replaced {symbols[counter]}')
                it -= 1

        counter += 1

    text = ''.join(text)
    text.strip()
    text = text.split()
    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Convert the characters in line to
        # lowercase to avoid case mismatch
        line = line.lower()
        # Split the line into words
        words = line.split(" ")
        # Iterate over each word in line
        for word in words:

            # Check if the word is already in dictionary
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1

    # Print the contents of dictionary
    ke = list(d.keys())
    val = list(d.values())
    print(len(ke))
    lst = []

    for key in ke:
        print(key, ":", d[key])
        if key.isalpha():
            break
        else:
            return []

    if len(ke) == 0:
        return []

    if len(ke) == 1:
        lst.extend(ke)

    if len(ke) == 2:
        lst.append(ke[val.index(max(val))])
        ke.remove(ke[val.index(max(val))])
        lst.extend(ke)

    if len(ke) > 2:
        counter = 0
        while counter < 3:
            lst.append(ke[val.index(max(val))])
            ke.remove(ke[val.index(max(val))])
            val.remove(max(val))
            counter += 1

    return lst


if __name__ == '__main__':
    print(top_3_words("  ...  "))
'''
import re
from collections import Counter

top_3_words=lambda t:[w for w,c in Counter(re.findall("'*[a-z][a-z']*",t.lower())).most_common(3)]'''