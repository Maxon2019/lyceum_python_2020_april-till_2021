def lena_zachem(n, comp_list):
    L = 1
    day = 0
    min_list = []
    while L <= n:

        l1 = L
        mins = 0
        day = 0

        while l1 <= len(comp_list):
            mins += sum(comp_list[day:l1])
            day += 1
            l1 += 1

        min_list.append(mins)
        L+=1

    for i in min_list:
        min_list[min_list.index(i)] = str(i)
    return ' '.join(min_list)


if __name__ == '__main__':
    n = int(input())
    comp_list = list(input().split())
    for i in comp_list:
        comp_list[comp_list.index(i)] = int(i)
    print(lena_zachem(n, comp_list))