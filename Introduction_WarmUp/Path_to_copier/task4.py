import resource
import time


def main():
    time_start = time.perf_counter()
    n, k = map(int, input().split())
    # // operator divides the first number by the second number and rounds the
    # result down to the nearest integer( or whole number).
    i = max(n // k, 1)
    opt1 = abs(n - k * i)
    i += 1
    opt2 = abs(n - k * i)
    res = min(opt1, opt2)
    print(res)
    time_elapsed = (time.perf_counter() - time_start)
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print(f"Memory used: {mem} Mb")
    print(f"Total time: {time_elapsed} secs")


if __name__ == '__main__':
    main()
