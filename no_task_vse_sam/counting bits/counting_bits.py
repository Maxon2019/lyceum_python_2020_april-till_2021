def countBits(n):
    i = 0
    binaric = []
    num = n
    while num != 1:
        binaric.append(str(num % 2))
        num = num // 2
    if num == 1:
        binaric.append('1')
    binaric = ''.join(binaric[::-1])
    for bit in binaric:
        if bit == '1':
            i += 1
    return i


if __name__ == "__main__":
    print(countBits(1234))
