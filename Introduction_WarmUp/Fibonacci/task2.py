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


if __name__ == '__main__':
    main()
