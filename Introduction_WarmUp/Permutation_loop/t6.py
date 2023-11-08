def minFalseIndex(v):
    for i in range(len(v)):
        if v[i] is False:
            return i
    return -1

def perm2():
    perm = list(map(int, input().split()))
    temp_perm = [x - 1 for x in perm]
    #temp_perm2 = list(map(lambda x: x - 1, perm))
    cnt_loops = 0
    # i = 0
    starting_index = 0
    current_index = starting_index
    # 2 3 1 5 4
    # 1 2 0 4 3
    # t t t f f
    # 6 3 1 5 2 4
    # i = 2
    # e = 1
    current_element = temp_perm[current_index]
    starting_element = temp_perm[starting_index]
    min_index = minFalseIndex(visited)
    while min_index != -1:
        visited[starting_index] = True
        current_index = temp_perm[current_index]
        current_element = temp_perm[current_index]
        temp_perm[current_index] = -1
        visited[current_index] = True
        if starting_index == current_index or minFalseIndex(visited) == -1:
            cnt_loops += 1
            starting_index = minFalseIndex(visited)
            current_index = starting_index
        min_index = minFalseIndex(visited)

    print(cnt_loops)

if __name__ == '__main__':
    perm = list(map(int, input().split()))
    temp_perm = [x - 1 for x in perm]
    #temp_perm2 = list(map(lambda x: x - 1, perm))
    cnt_loops = 0
    visited = [False] * len(perm)
    # i = 0
    # if visited[i] == False
    starting_index = 0
    current_index = starting_index
    # 2 3 1 5 4
    # 1 2 0 4 3
    # t t t f f
    # 6 3 1 5 2 4
    # i = 2
    # e = 1
    current_element = temp_perm[current_index]
    starting_element = temp_perm[starting_index]
    min_index = minFalseIndex(visited)
    while min_index != -1:
        visited[starting_index] = True
        current_index = temp_perm[current_index]
        current_element = temp_perm[current_index]
        visited[current_index] = True
        if starting_index == current_index or minFalseIndex(visited) == -1:
            cnt_loops += 1
            starting_index = minFalseIndex(visited)
            current_index = starting_index
        min_index = minFalseIndex(visited)

    print(cnt_loops)


