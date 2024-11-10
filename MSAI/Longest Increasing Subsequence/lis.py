
import bisect


def lis_fast(A):
    if not A:
        return 0
    tails = []

    for num in A:
        pos = bisect.bisect_left(tails, num)

        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)


def lis(N, A):
    d = [1] * N
    for i in range(N):
        for k in range(i):
            if A[k] < A[i]:
                d[i] = max(d[i], d[k] + 1)
    return max(d)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    m = lis_fast( a)
    print(m)
