import random

from past.builtins import xrange


def partition(x, l, r, pivot):
    """
    :param x: Source array (list)
    :param l: left border of partitioning range (int)
    :param r: right border (not included) of partitioning range (int)
    :param pivot: pivot element to divide array (any item from x[l, r)).
    :return: il, ir -- desired partition
    This function should reorder elements of x within [l, r) region
    in the way, these conditions are true:
    x[l:il] < pivot
    x[il:ir] == pivot
    x[ir:r] > pivot
    """
    il = l
    ir = l
    print("-------" + "pivot " + str(pivot) + str(x) + " " + str(x[l:r]))
    for j in range(l, r):
        if x[j] == pivot:
            x[j], x[ir] = x[ir], x[j]
            ir += 1
        else:
            if x[j] < pivot:
                x[j], x[il] = x[il], x[j]
                if x[j] == pivot:
                    x[j], x[ir] = x[ir], x[j]
                ir += 1
                il += 1
    print("afrer " + "pivot " + str(pivot) + str(x) + " " + str(x[l:r]))
    return il, ir


def qsort(x, l=0, r=None):
    if r is None:
        r = len(x)
    if (r - l) > 1:
        pivot = x[random.randint(l, r - 1)]
        #print(" qsort before " + str(x) + " l r " + str(l) + " " + str(r))
        il, ir = partition(x, l, r, pivot)
        #print(" qsort " + str(x) + " il ir " + str(il) + " " + str(ir))
        qsort(x, l, il)
        qsort(x, ir, r)


if __name__ == '__main__':
    # N = int(input())
    # x = list(map(int, input().split()))
    # qsort(x)
    # print(' '.join(map(str, x)))
    for i in range(2000):
        arr = [random.randint(-10, 10) for _ in xrange(50)]
        #arr = [7, -7, 3, -7, -9]
        print("s = " + str(arr))
        arr2 = arr.copy()
        qsort(arr)
        arr2.sort()
        print("q=" + str(arr))
        print(arr2)
        print(arr == arr2)
        if not (arr == arr2):
            break
