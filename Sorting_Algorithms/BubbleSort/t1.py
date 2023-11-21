


if __name__ =='__main__':
    arr = list(map(int, input().split()))
    l = len(arr)
    print(arr)
    for i in range(l):
        for j in range(l):
            if arr[i] < arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
                print(arr)
    print(arr)
