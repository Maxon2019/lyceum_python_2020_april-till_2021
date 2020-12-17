k = [2, 3, 4, 5, 6, 7, 8, 9]


def stringer(st):
    return [str(item) for item in st]


def inter(t):
    return [int(item) for item in t]


def checker(k, num):
    n = 0
    fin = []
    lst = []
    fir = num
    while n < 8:
        while num >= k[n]:
            lst.append(num % k[n])
            num = num // k[n]
        lst.append(num)

        lst = ''.join(stringer(lst))
        lst = lst.lstrip('0')
        fin.append(lst)
        n += 1
        num = fir
        lst = []
    return max(inter(fin))


if __name__ == '__main__':
    num = int(input())
    print(checker(k, num))
