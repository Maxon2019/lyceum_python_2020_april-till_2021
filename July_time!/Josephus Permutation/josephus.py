"""Well, Josephus and another man were the last two and, as we now know every detail of the story, you may have 
correctly guessed that they didn't exactly follow through the original idea. 

You are now to create a function that returns a Josephus permutation, taking as parameters the initial array/list of 
items to be permuted as if they were in a circle and counted out every k places until none remained. 

Tips and notes: it helps to start counting from 1 up to n, instead of the usual range 0..n-1; k will always be >=1.

For example, with n=7 and k=3 josephus(7,3) should act this way.

[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out and goes into the result [3]
[1,2,4,5,7] => 6 is counted out and goes into the result [3,6]
[1,4,5,7] => 2 is counted out and goes into the result [3,6,2]
[1,4,5] => 7 is counted out and goes into the result [3,6,2,7]
[1,4] => 5 is counted out and goes into the result [3,6,2,7,5]
[4] => 1 is counted out and goes into the result [3,6,2,7,5,1]
[] => 4 is counted out and goes into the result [3,6,2,7,5,1,4]
So our final result is:

josephus([1,2,3,4,5,6,7],3)==[3,6,2,7,5,1,4]"""


def josephus(items, skip):
    fin = []
    skip -= 1  # pop automatically skips the dead guy
    if len(items) >= skip:
        idx = skip
        return items
    elif not ''.join(items).isdigit():
        return []
    else:
        idx = skip - len(items)
    if len(items) == 0:
        return items

    while len(items) > 1:
        fin.append(items.pop(idx))  # kill prisoner at idx
        idx = (idx + skip) % len(items)
    print('survivor: ', items[0])
    fin.append(items[0])
    return fin


if __name__ == '__main__':
    print(josephus([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],40))
