from random import randint


def zap():
    c = 0
    l = []
    while c < 100:
        l.append(randint(-20, 40))
        c += 1
    print(l)
    print(bool(sum(l)))


if __name__ == '__main__':
    zap()
