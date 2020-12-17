def progs_c(alll, c__, com):
    if 2*c__ > alll:
        return c__ // com
    else:
        return -1


if __name__ == '__main__':
    alll =int(input())
    c__ = int(input())
    com = int(input())
    print(progs_c(alll, c__, com))