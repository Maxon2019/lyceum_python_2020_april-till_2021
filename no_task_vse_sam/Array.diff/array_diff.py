"""Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the
result.

It should remove all values from list a, which are present in list b.If a value is present in b, all of its occurrences
must be removed from the other"""


def array_diff(a, b):
    for i in b:
        if i in a:
            counter = a.count(i)
            if counter >= 0:
                while counter != 0:
                    a.remove(i)
                    counter -= 1
            else:
                pass

        else:
            pass
    return a


if __name__ == "__main__":
    print(array_diff([1, 2, 2, 2, 3], [2]))
    # лучшее [x for x in a if x not in b]
