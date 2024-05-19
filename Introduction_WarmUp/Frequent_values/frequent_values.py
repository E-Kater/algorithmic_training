from collections import Counter


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    res = []
    cnter = Counter(arr)
    for i in cnter.keys():
        if cnter[i] >= k:
            res.append(i)
    print(*res, sep=" ")


if __name__ == '__main__':
    main()
