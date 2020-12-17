def vasya(N, K, X, Y):
    v_zad = (N // K) * Y
    b_zad = (N - N // K) * X
    return v_zad + b_zad


if __name__ == '__main__':
    N = int(input())
    K = int(input())
    X = int(input())
    Y = int(input())
    print(vasya(N, K, X, Y))
