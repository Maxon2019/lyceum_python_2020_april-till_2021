from random import randint, random


def many():
    c = 0
    l = []
    while c < 12:
        f = randint(163, 190)
        l.append(f)
        c+=1
    c = 0
    while c < 6:
        print(l[c], l[c + 1])
        c += 2


if __name__ == '__main__':
    many()
