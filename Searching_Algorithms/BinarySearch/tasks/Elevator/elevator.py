from bisect import *
from itertools import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    m = list(map(int, input().split()))
    b = list(accumulate([1] + a))
    for mi in m:
        floor = bisect(b, mi)
        print(floor if floor <= n else -1, end="\n")
