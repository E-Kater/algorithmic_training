def main():
    n, k = map(int, input().split())
    t = max(n // k, 1)
    up = (t + 1) * k
    down = t * k
    up_delta = up - n
    down_delta = n - down

    print("up", up)
    print("down", down)
    print("up_delta", up_delta)
    print("down_delta", down_delta)
    res = min(abs(up_delta), abs(down_delta))
    print(res)


if __name__ == "__main__":
    main()

# Алгоритмическая сложность О(С) = О(1)
