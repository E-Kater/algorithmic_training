import resource
import time


def main():
    time_start = time.perf_counter()
    perm = list(map(int, input().split()))
    perm = [x - 1 for x in perm]
    n = len(perm)
    ans = 0
    visited = [False] * n
    for start in range(n):
        if visited[start]:
            continue
        ans += 1
        current = start
        while current != start:
            visited[current] = True
            current = perm[current]

    print(ans)

    time_elapsed = (time.perf_counter() - time_start)
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print(f"Memory used: {mem} Mb")
    print(f"Total time: {time_elapsed} secs")


def main_without_visited():
    time_start = time.perf_counter()
    perm = list(map(int, input().split()))
    perm = [x - 1 for x in perm]
    n = len(perm)
    ans = 0
    for start in range(n):
        if perm[start] == -1:
            continue
        ans += 1
        current = start
        while current != start:
            current = perm[current]
            perm[current] = -1

    print(ans)

    time_elapsed = (time.perf_counter() - time_start)
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print(f"Memory used: {mem} Mb")
    print(f"Total time: {time_elapsed} secs")


if __name__ == '__main__':
    main()
    main_without_visited()
