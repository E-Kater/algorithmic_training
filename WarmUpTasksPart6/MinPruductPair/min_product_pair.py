
if __name__ == '__main__':
    a = list(map(int, input().split()))
    a.sort()
    ans1 = a[0] * a[1]
    ans2 = a[0] * a[-1]
    ans3 = a[-2] * a[-1]
    print(min(ans1, ans2, ans3))