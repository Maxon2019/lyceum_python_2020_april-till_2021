"""A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers or a range of integers denoted by the starting integer separated from the end integer in the
range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered
a range unless it spans at least 3 numbers. For example ("12, 13, 15-17") Complete the solution so that it takes a
list of integers in increasing order and returns a correctly formatted string in the range format. """


def solution(lst):
    res = []
    if lst:
        tmp, i, ln = lst[0], 0, len(lst)
        while i < ln:
            tmp, j = lst[i], i
            while j < ln - 1 and lst[j + 1] == lst[j] + 1:
                j += 1
            if j - i > 1:
                tmp = str(lst[i]) + "-" + str(lst[j])
                i = j + 1
            else:
                i = (j if j > i else i + 1)
            res.append(tmp)
    return ",".join(str(x) for x in res)


if __name__ == '__main__':
    print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
