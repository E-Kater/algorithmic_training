def getMatrixMinor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

def getMatrixDeternminant(m):
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    determinant = 0
    for c in range(len(m)):
        determinant += ((-1) ** c) * m[0][c] * getMatrixDeternminant(getMatrixMinor(m, 0, c))
    return determinant


def main():
    n = int(input())
    a = []
    for i in range(0, n):
        a.append([int(j) for j in input().split()])
    print(getMatrixDeternminant(a))


if __name__ == '__main__':
    main()
