from time import perf_counter
from resource import getrusage, RUSAGE_SELF


def main():
    # F_N = F_N-1 + F_N-2
    time_start = perf_counter()
    n = int(input())
    arr = [0, 1, 1]
    if n > 2:
        while len(arr) <= n:
            arr.append(arr[-2] + arr[-1])

    print(arr[n])
    mem = getrusage(RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print(f"Time elapsed: {perf_counter() - time_start}")
    print(f"Memory used: {mem} Mb")


if __name__ == "__main__":
    main()

# Алгоритмическая сложность алгоритма
# O(n-2) ~ O(n)

# Амортизационная сложность!!
# Как правильно мерить память и время ? getsize
