from collections import Counter

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    cnter = Counter(arr)
    l = len(arr)
    keys_count = len(cnter.keys())

    if l == keys_count and min(arr) > 0:
        print('OK')
    else:
        print('BAD')

