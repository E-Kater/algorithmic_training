# Python program for implementation of Bogo Sort
import random


# Sorts array a[0..n-1] using Bogo sort
def bogoSort(a):
    n = len(a)
    while not is_sorted(a):
        shuffle(a)


# To check if array is sorted or not
def is_sorted(a):
    n = len(a)
    for i in range(0, n - 1):
        if a[i] > a[i + 1]:
            return False
    return True


# To generate permutation of the array
def shuffle(a):
    n = len(a)
    for i in range(0, n):
        r = random.randint(0, n - 1)
        a[i], a[r] = a[r], a[i]


# Sorts array a[0..n-1] using Bogo sort
def bogoSort2(a):
    while not sorted(a) == a:
        random.shuffle(a)


if __name__ == '__main__':
    # Driver code to test above
    a = [3, 2, 4, 1, 0, 5]
    bogoSort(a)
    print("Sorted array :")
    for i in range(len(a)):
        print("%d" % a[i]),
    a2 = [31, 22, 14, 51, 10, 5]
    bogoSort2(a2)
    print("Sorted array2 :")
    for i in range(len(a2)):
        print("%d" % a2[i]),
