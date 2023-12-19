from collections import Counter

if __name__ == '__main__':
    s = input()
    cnt = Counter(s)
    print(cnt)
    print(sorted(cnt.keys()))
    half = "" # asdsa -> as
    mid = "" # asdsa -> d half + mid + half[::-1]
    cnt_cutted = [c for c in cnt.keys() if cnt[c] % 2 == 1]
    cnt_cutted2 = {k:v for (k, v) in cnt.items() if k in cnt_cutted and cnt[k] -1 > 0}
    cnt_even = [c for c in cnt.keys() if cnt[c] % 2 == 0]
    filtered_cnt = {k:v for (k, v) in cnt.items() if k in cnt_cutted2.keys() or k in cnt_even}
    #odd - нч
    #even - ч
    min_cnt_cutted = min("".join(cnt_cutted))
    for c in sorted(filtered_cnt):
        if cnt[c] // 2 > 0:
            half+= c * (cnt[c] // 2)
    res = half + min_cnt_cutted + half[::-1]
    print(res)


