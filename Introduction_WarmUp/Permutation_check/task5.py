import resource
import time
from collections import *


def main():
    time_start = time.perf_counter()
    arr = list(map(int, input().split()))
    # A Counter is a dict subclass for counting hashable objects.
    # It is a collection where elements are stored as dictionary keys
    # and their counts are stored as dictionary values.
    # Counts are allowed to be any integer value including zero or negative counts.
    # The Counter class is similar to bags or multisets in other languages.
    cnt = Counter(arr)
    ans = max(arr) == len(cnt) and max(cnt.values()) == 1
    print("OK" if ans else "BAD")

    time_elapsed = (time.perf_counter() - time_start)
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print(f"Memory used: {mem} Mb")
    print(f"Total time: {time_elapsed} secs")


if __name__ == '__main__':
    main()
