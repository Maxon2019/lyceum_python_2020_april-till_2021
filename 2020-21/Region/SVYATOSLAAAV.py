def printers(N, X):
    max_pages = 0
    if X == 2:
        max_pages = 2 ** (N - 1) +1
    else:
        max_pages += printers(N-1,X-1)
    return max_pages


if __name__ == '__main__':
    N = int(input())
    X = int(input())
    print(printers(N, X))
