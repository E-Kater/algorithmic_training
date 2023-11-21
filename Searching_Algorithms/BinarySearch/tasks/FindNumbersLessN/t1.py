from bisect import *

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    a = int(input())
    arr.sort()
    ans = bisect_left(arr, a)
    print(ans)
