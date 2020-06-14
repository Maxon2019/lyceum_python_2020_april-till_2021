def add_binary(a, b):
    sum_list = []
    sum = a + b
    while sum % 2 != 0:
        sum_list.append(str(sum % 2))
        sum = sum // 2
    binaric = ''.join(sum_list)
    return binaric


if __name__ == "__main__":
    print(add_binary(12, 51))
