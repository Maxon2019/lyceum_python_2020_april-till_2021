def ifer(d, sh, k, y):
    if d <= k and y == True:
        d = k // 2
        sh = k // 2 + 1
    elif d - k < sh - 1:
        d -= k - (sh - d)
        sh -= sh - d
    else:
        d -= k
    return d, sh


def petya(d, sh, k):
    if d == sh:
        return ifer(d, sh, k, y=True)
    elif d > sh:
        return ifer(d, sh, k, y=False)
    else:
        d, sh = sh, d
        return ifer(d, sh, k, y=False)


if __name__ == '__main__':
    d = int(input())
    sh = int(input())
    k = int(input())
    print(petya(d, sh, k)[0], petya(d, sh, k)[1])
