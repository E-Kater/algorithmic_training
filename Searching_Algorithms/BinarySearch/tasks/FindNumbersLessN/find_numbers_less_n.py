from bisect import *


def find(arr, queries):
    for query in queries:
        print(bisect_left(arr, query), end="\n")


if __name__ == '__main__':
    a = list(map(int, input().split()))
    q = map(int, input().split())
    a.sort()
    find(a, q)
