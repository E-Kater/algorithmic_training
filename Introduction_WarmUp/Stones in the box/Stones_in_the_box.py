from collections import deque


def rotateTheBox(box: list[list[str]]) -> list[list[str]]:
    m, n = len(box), len(box[0])
    ans = [[None] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            ans[j][m - i - 1] = box[i][j]
    for j in range(m):
        q = deque()
        for i in range(n - 1, -1, -1):
            if ans[i][j] == '#':
                q.clear()
            elif ans[i][j] == '.':
                q.append(i)
            elif q:
                ans[q.popleft()][j] = 'O'
                ans[i][j] = '.'
                q.append(i)
    return ans


def main():
    n, m = map(int, input().split())
    a = []
    for i in range(0, n):
        a.append(list(input()))
    res = rotateTheBox(a)
    for i in range(0, m):
       print(*res[i], sep="")


if __name__ == '__main__':
    main()
