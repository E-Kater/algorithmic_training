

def selection_sort(arr):
    sz = len(arr)
    for ind in range(sz):
        min_indx = ind
        for j in range(ind + 1, sz, 1):
            if arr[j] < arr[min_indx]:
                min_indx = j
        arr[ind], arr[min_indx] = arr[min_indx], arr[ind]


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(arr)
    selection_sort(arr)
    print(arr)
