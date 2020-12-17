def greta_dev(list_of_pieces, m):
    mid_state = []
    counter = 0
    while counter < m:
        state = list_of_pieces[counter]
        l = state[0]
        r = state[1]
        k = state[2]
        if k == 1:
            mid_state.append((r - l + 1) / (r - l + 1))
        else:
            mid_state.append((r - l + 1) // 2 / (r - l + 1))
        counter += 1

    return int(sum(mid_state) + 1 // len(mid_state))


if __name__ == '__main__':
    counter = 0
    list_of_pieces = []
    n, m = map(int, input().split())
    while counter < m:
        inp_list = list(input().split())
        for i in inp_list:
            inp_list[inp_list.index(i)] = int(i)
        list_of_pieces.append(inp_list)
        counter += 1
    print(greta_dev(list_of_pieces, m))
