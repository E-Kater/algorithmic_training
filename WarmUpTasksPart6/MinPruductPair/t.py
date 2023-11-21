

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    arr.sort()
    # 1 2 3 4
    ans1 = arr[0] * arr[1]
    # -1 1 2 3
    ans2 = arr[0] * arr[-1]
    # -1 -2 -3 -4
    # -4 -3 -2 -1
    ans3 = arr[-2] * arr[-1]
    print(min(ans1, ans2, ans3))
