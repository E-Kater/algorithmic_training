def bisect_left(x, key):
    l = -1
    r = len(x)
    while r - l > 1:
        m = (l + r) // 2
        if x[m] < key:
            l = m
        else:
            r = m
    return r


def bisect_right(x, key):
    l = -1
    r = len(x)
    while r - l > 1:
        m = (l + r) // 2
        if x[m] <= key:
            l = m
        else:
            r = m
    return r


if __name__ == '__main__':
    N, M = map(int, input().split())
    x1 = list(map(int, input().split()))
    x1.sort()
    for i in range(M):
        l1, r1 = map(int, input().split())
        print(bisect_right(x1, r1) - bisect_left(x1, l1))
