

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    res1 = a // 10
    res2 = b // 10
    res3 = (res1+res2) // 3
    print(min(res1, res2, res3))