def is_good(n, k, a, max_jump):
    x = 0
    count = 0
    while x < n:
        count += 1
        for jump in range(max_jump, 0, -1):
            nx = x + jump
            if (nx >= n) or a[nx - 1] == '1':
                x = nx
                break
            else:
                return False
        return count <= k


def jumping_frog():
    n, k = map(int, input().split())
    a = input()
    left = 1
    right = n
    while left < right:
        mid = (left + right) // 2
        if is_good(n, k, a, mid):
            right = mid
        else:
            left = mid + 1
    print(left)


if __name__ == '__main__':
    jumping_frog()
