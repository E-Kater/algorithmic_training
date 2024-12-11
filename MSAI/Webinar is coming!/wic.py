from heapq import heappush, heappop

inf = 10 ** 10

if __name__ == '__main__':
    N, M = map(int, input().split())
    s, f = map(int, input().split())
    G = [{} for i in range(N)]
    for i in range(M):
        x, y, w = map(int, input().split())
        G[x][y] = w
        G[y][x] = w

    h = []
    d = [inf] * N
    p = [-1] * N
    v = -1
    S = {-1}
    d[s] = 0
    heappush(h, (d[s], s))
    while h:
        while v in S and h:
            v = heappop(h)[1]
        if v not in S:
            S.add(v)
        for u in G[v]:
            new_d = d[v] + G[v][u]
            if new_d < d[u]:
                heappush(h, (new_d, u))
                d[u] = new_d
                p[u] = v

    if d[f] == inf:
        print(-1)
    else:
        path = []
        v = f
        while v != -1:
            path.append(v)
            v = p[v]

        print(d[f])
        print(len(path))
        print(' '.join(map(str, path[::-1])))
