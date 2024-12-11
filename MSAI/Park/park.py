from collections import deque


def bfs(G, visited, d, p, s):
    vertex_queue = deque([s])
    while vertex_queue:
        v = vertex_queue.popleft()
        visited[v] = 2
        for u in G[v]:
            if not visited[u]:
                visited[u] = 1
                vertex_queue.append(u)
                d[u] = d[v] + 1
                p[u] = v
    return d


if __name__ == '__main__':
    N, M = map(int, input().split())
    park = [input().strip() for _ in range(N)]
    G = [set() for i in range(N * M)]
    start = None
    target = None
    n = 0
    for i in range(N):
        for j in range(M):
            if park[i][j] == '.' or park[i][j] == 'E' or park[i][j] == 'X':
                if i + 1 < N and park[i + 1][j] in ('.', 'E', 'X'):
                    G[n].add(n + M)
                if i - 1 >= 0 and park[i - 1][j] in ('.', 'E', 'X'):
                    G[n].add(n - M)
                if j + 1 < M and park[i][j + 1] in ('.', 'E', 'X'):
                    G[n].add(n + 1)
                if j - 1 >= 0 and park[i][j - 1] in ('.', 'E', 'X'):
                    G[n].add(n - 1)
            if park[i][j] == 'E':
                start = n
            elif park[i][j] == 'X':
                target = n
            n += 1
    visited = [False] * (N * M)
    d = [0] * (N*M)
    p = [0] * (N*M)
    shortest = bfs(G, visited, d, p, start)
    print(-1 if shortest[target] == 0 else shortest[target])
