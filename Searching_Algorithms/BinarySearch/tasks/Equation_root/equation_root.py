ITER = 100


def f(x, c):
    return x ** 5 - 10 * x + c


def find_root(c):
    left = -10
    right = 10
    for _ in range(ITER):
        mid = (left + right) / 2
        if f(mid, c) < 0:
            left = mid
        else:
            right = mid
    return (left + right) / 2


if __name__ == '__main__':
    a = int(input())
    ans = find_root(a)

    print("ans=%.2f" % ans)
