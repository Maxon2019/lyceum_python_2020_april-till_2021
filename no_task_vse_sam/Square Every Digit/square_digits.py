"""Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer"""


def square_digits(num):
    lst = []
    nums_list = list(str(num))
    for i in nums_list:
        k = nums_list[nums_list.index(i)]
        k = int(k) ** 2
        lst.append(str(k))
    return int("".join(lst))


if __name__ == "__main__":
    print(square_digits(9119))
    '''ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)'''  # лучшее решение
