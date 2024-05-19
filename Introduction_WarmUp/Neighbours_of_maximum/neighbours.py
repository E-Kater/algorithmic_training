def main():
    n = int(input())
    arr = list(map(int, input().split()))
    res = dict()
    max_value = max(arr)
    for i in range(0, n):
        if arr[i] == max_value:
            if i - 1 >= 0:
                res[i - 1] = arr[i - 1]
            res[i] = arr[i]
            if i + 1 < n:
                res[i + 1] = arr[i + 1]
    r = list(res.values())
    print(*r, sep=" ")


if __name__ == '__main__':
    main()
