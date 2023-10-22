import resource
import time


def main():
    time_start = time.perf_counter()
    x1, y1 = input().split()
    x2, y2 = input().split()
    dx = abs(int(x1) - int(x2))
    dy = abs(int(y1)-int(y2))
    print(dx + dy)

    time_elapsed = (time.perf_counter() - time_start)
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print(f"Memory used: {mem} Mb")
    print(f"Total time: {time_elapsed} secs")


if __name__ == '__main__':
    main()
