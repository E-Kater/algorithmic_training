import resource
import time


def main():
    time_start = time.perf_counter()
    n = int(input())
    arr = [0, 1]
    while len(arr) <= n:
        arr.append(arr[-1] + arr[-2])

    time_elapsed = (time.perf_counter() - time_start)
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print(arr[n])
    print(f"Memory used: {mem} Mb")
    print(f"Total time: {time_elapsed} secs")


def fibonacci2(n):
    prev = 0
    curr = 1
    for i in range(n):
        prev, curr = curr, prev + curr
    return prev


def fibonacci(n):
    if n <= 1:
        return n
    prev = curr = 1
    for i in range(2, n + 1):
        prev, curr = curr, prev + curr
    return prev


if __name__ == '__main__':
    main()
